from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from typing import TypedDict
from mem0 import MemoryClient
import logging
import json

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
client = MemoryClient(api_key="your-api-key")
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
            state["enhanced_prompt"] = "Update the prompt"
        
        except Exception as e:
            logging.exception("Relevency agent faild")
            
            state["is_question_relevant"] = False
            state["error"] = "Unable to determine the response at the moment"
            
        return state
    
    def enhancer_agent(state: AgentState):
        try:
            if not state["user_query"]:
                raise ValueError("user_query is missing in state")
            
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
            
            state["enhanced_prompt"] = parsed.corrected_query
            state["memory_question"] = parsed.generated_question
        except Exception as e:
            logging.exception("Enhancer agent faild")
            
            state["error"] = "Unable to determine the response at the moment"
        
        return state
    

        