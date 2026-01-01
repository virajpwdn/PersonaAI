from langchain_openai import ChatOpenAI
from typing import TypedDict

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

class AgentState(TypedDict):
    user_query: str
    is_question_relevant: bool
    enhanced_prompt: str
    memory: str
    memory_check: bool
    memory_update_check: bool
    final_response: str
    

class Agents:
    def relevency_agent(state: AgentState):
        