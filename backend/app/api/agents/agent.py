from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from typing import TypedDict

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

class AgentState(TypedDict):
    user_query: str
    is_question_relevant: bool
    enhanced_prompt: str
    memory: str
    memory_check: bool
    memory_update_check: bool
    memory_question: str
    final_response: str
    

class Agents:
    def relevency_agent(state: AgentState):
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
        answer = response.content
        print("CONTENT", answer)
        
        state["is_question_relevant"] = answer == "yes"
        state["final_response"] = "Update the prompt"
        
        return state
    
    def enhancer_agent(state: AgentState):
        SYSTEM_PRROMPT = """
           You are a copywriter with 50 years of experience. You have been correcting grammar, spelling, and punctuation, and you are a master of the English language. People take lessons from you.
           
           You will now receive a prompt. Your task is to correct it if there are any grammatical mistakes. If no mistakes are found, do not change the sentence—simply return it as it is.
        """
        
        prompt = [
            SystemMessage(content=SYSTEM_PRROMPT),
            HumanMessage(state['user_query'])
        ]
        
        response = llm.invoke(prompt)
        answer = response.content
        print("CONTENT FROM AGENT 2 ", answer)
        state["final_response"] = answer
        
        return state