from langgraph.graph import START, END, StateGraph
from typing import TypedDict
from langchain_openai import OpenAI
import os
from dotenv import load_dotenv
from langgraph.checkpoint.postgres import PostgresSaver
from api.agents.agent import Agents

load_dotenv()

DB_URI=os.getenv("DATABASE_URL")

# Defining state
class AgentState(TypedDict):
    user_query: str
    is_question_relevant: bool | None
    enhanced_prompt: str | None
    memory: str | None
    memory_check: bool | None
    memory_update_check: bool | None
    memory_question: str | None
    final_response: str | None
    error: str | None
    
# Initialize checkpointer
# checkpointer = PostgresSaver.from_conn_string(DB_URI)
checkpointer_cm = PostgresSaver.from_conn_string(DB_URI)
checkpointer = checkpointer_cm.__enter__()
checkpointer.setup()


# Create Graph
workflow = StateGraph(AgentState)

def router_based_on_relavance(state: AgentState) -> str:
    if state["is_question_relevant"]:
        return "enhancer"
    else:
        return END

workflow.add_node("is_question_relevant", Agents.relevency_agent)
workflow.add_node("enhancer", Agents.enhancer_agent)

workflow.add_edge(START, "is_question_relevant")
workflow.add_conditional_edges("is_question_relevant", router_based_on_relavance, {
    "enhancer": "enhancer",
    END: END
})
workflow.add_edge("enhancer", END)

graph = workflow.compile(checkpointer=checkpointer)