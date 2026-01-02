from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from typing import TypedDict
from mem0 import MemoryClient
import logging
import json
import os

mem0 = os.getenv("MEM0_API_KEY")
model_1 = os.getenv("OPENAI_MODEL_1")
model_2 = os.getenv("OPENAI_MODEL_2")
model_3 = os.getenv("OPENAI_MODEL_3")

client = MemoryClient(api_key=mem0)
logger = logging.getLogger(__name__)

class AgentState(TypedDict):
    user_query: str
    is_question_relevant: bool
    enhanced_prompt: str
    memory: str
    memory_check: bool
    memory_update_check: bool
    memory_question: str
    final_response: str
    error: str
    

class Agents:
    def relevency_agent(state: AgentState):
        try:
            if not state["user_query"]:
                raise ValueError("user_query is missing in state")
            llm = ChatOpenAI(model=model_1, temperature=0)
            prompt = [
                SystemMessage(
                    content=(
                        "You are a classifier, you will get a query and you have to tell weather the query is related to business, finance, investment, or money. You have to only send yes or no."
                    )
                ),
                HumanMessage(
                    content=(state["user_query"])
                )
            ]
            
            response = llm.invoke(prompt)
            answer = response.content.strip().lower()
            print("CONTENT", answer)
            
            state["is_question_relevant"] = answer == "yes"
            if state["is_question_relevant"]:
                state["enhanced_prompt"] = state["user_query"]
            else:
                state["enhanced_prompt"] = state["user_query"]
                state["final_response"] = "I'm sorry, I can only answer questions related to business, finance, investment, or money."
                state["memory"] = ""
        except Exception as e:
            logging.exception("Relevency agent faild")
            
            state["is_question_relevant"] = False
            state["error"] = "Unable to determine the response at the moment"
            
        return state
    
    def enhancer_agent(state: AgentState):
        try:
            if not state["user_query"]:
                raise ValueError("user_query is missing in state")
            llm = ChatOpenAI(model=model_2, temperature=0)
            SYSTEM_PROMPT = """
            You are a copywriter with 50 years of experience. You have been correcting grammar, spelling, and punctuation, and you are a master of the English language. People take lessons from you.
            
            You will now receive a prompt. Your task is to correct it if there are any grammatical mistakes. If no mistakes are found, do not change the sentence—simply return it as it is.
            
            second, from the above query which you corrected make a question 

            example:
            Question: I want to start a business
            Answer: Does user has some business or is associated?
            
            RETURN FORMAT (STRICT JSON):
            {
                "corrected_query": "<corrected sentence>",
                "generated_question": "<question>"
            }
            """
            
            prompt = [
                SystemMessage(content=SYSTEM_PROMPT),
                HumanMessage(state['user_query'])
            ]
            
            response = llm.invoke(prompt)
            answer = response.content
            
            # parsing into JSON
            parsed = json.loads(answer)
            
            state["enhanced_prompt"] = parsed["corrected_query"]
            state["memory_question"] = parsed["generated_question"]
        except Exception as e:
            logging.exception("Enhancer agent failed")
            
            state["error"] = "Unable to determine the response at the moment"
        
        return state
    
    def add_memory_agent(state: AgentState, config):
        try:
            if state["memory_check"]:
                return state
            
            connection_id = config["configurable"]["thread_id"]
            
            retrival = client.search(state["memory_question"], filter={"user_id": connection_id})
            print("THIS IS RETRIVAL -> ", retrival)
            
            if retrival and len(retrival) > 0:
                state["memory"] = retrival[0].memory
                state["memory_check"] = True
            else:
                client.add(state["enhanced_prompt"], user_id=connection_id)
                state["memory_update_check"] = True
        except Exception as e:
            logger.exception("Add Memory Agent failed")
            state["error"] = "Unable to determine the response at the moment"
        
        return state
    
    def update_memory_agent(state: AgentState, config):
        try:
            if not state["enhanced_prompt"]:
                raise ValueError("Prompt is missing")
            
            connection_id = config["configurable"]["thread_id"]
            
            client.add(state['enhanced_prompt'], user_id = connection_id)
            state['memory_update_check'] = True
        except Exception as e:
            logger.exception("Update to memory agent failed")
            state["error"] = "Unable to po the response at the moment" 
            
        return state
    
    def process_agent(state: AgentState):
        try:
            llm = ChatOpenAI(model=model_3, temperature=0)
            SYSTEM_PROMPT = """
                You are “Buffett-inspired Business & Money Mentor” — a calm, plainspoken, rational advisor focused on long-term business thinking, capital allocation, and personal money management. Base guidance on widely known Warren Buffett principles from Berkshire Hathaway shareholder letters and annual meeting Q&A style; prioritize simplicity, incentives, and temperament. Never claim to be the real Warren Buffett.

                VOICE
                    Plain English, short paragraphs, minimal jargon.
                    Patient, humble, a bit witty (lightly), but never snarky.
                    Prefer principles + checklists over predictions.

                SCOPE (WHAT YOU DO)

                    Teach business fundamentals: durable competitive advantage (“moat”), management quality, incentives, unit economics, balance-sheet strength, and long-term compounding mindset.
                    Teach personal finance: budgeting, saving rate, emergency fund logic, avoiding high-interest debt, and building a long-term plan.
                    Teach “how to research”: what documents to read, what questions to ask, what numbers to compute, how to avoid common mistakes.

                HARD RULES (WHAT YOU NEVER DO)

                    No personalized financial advice, no “buy/sell/hold” on any stock/crypto, no price targets, no timing the market.
                    If asked for stock picks or specific tickers: refuse briefly and pivot to a research framework.
                    If user asks for illegal/unethical actions: refuse.

                RESPONSE FORMAT (DEFAULT)

                    One-sentence principle-first answer.
                    3–6 bullet research steps or a checklist.
                    2–4 risks/pitfalls (“What could go wrong”).
                    One clarifying question to tailor the framework (not a recommendation).

                EXAMPLES

                User: “Should I buy shares of XYZ?”
                Assistant: “Can’t help with buy/sell decisions, but can help you decide how to think.”

                    Circle of competence: Can you explain XYZ’s business model simply?

                    Moat: What prevents competitors from copying it?

                    Management: Are incentives aligned with owners?

                    Financials: 5–10 year history of ROIC, debt, free cash flow.

                    Valuation: Compare conservative intrinsic value range vs. current price (with margin of safety).
                    Pitfalls: Story-driven investing, leverage, ignoring opportunity cost.
                    Question: “What does XYZ sell, and who is its strongest competitor?”

                User: “How do I manage money better each month?”
                Assistant: “Build a system that makes good behavior automatic.”

                    Track spending for 30 days; find the top 3 leaks.

                    Set a target saving rate; automate it on payday.

                    Build an emergency fund; avoid high-interest debt.

                    Invest with a long time horizon; keep it simple and low-cost.
                    Pitfalls: Lifestyle creep, chasing hot returns, overconfidence.
                    Question: “Is your goal stability, aggressive saving, or a specific purchase timeline?”

            """
            
            response = llm.invoke(
                [
                    SystemMessage(SYSTEM_PROMPT),
                    HumanMessage(state["enhanced_prompt"])
                ]
            )
            
            answer = response.content
            print("FINAL ANSER -> ", answer)
            state["final_response"] = answer
            
        except Exception as e:
            logger.exception("Update to memory agent failed")
            state["error"] = "Unable to po the response at the moment" 
            
        return state