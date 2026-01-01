from langgraph.graph import START, END, StateGraph
from typing import TypedDict
from langchain_openai import OpenAI
import os
from dotenv import load_dotenv
from langgraph.checkpoint.postgres import PostgresSaver

load_dotenv()

DB_URI=os.getenv("DATABASE_URL")

# Defining state
class AgentState(TypedDict):
    message: list
    llm_response: str
    
# Initialize checkpointer
# checkpointer = PostgresSaver.from_conn_string(DB_URI)
checkpointer_cm = PostgresSaver.from_conn_string(DB_URI)
checkpointer = checkpointer_cm.__enter__()
checkpointer.setup()


# Create Graph
workflow = StateGraph(AgentState)

#!TODO Defining nodes -> later import them from agents directory
def hello(state: AgentState) -> AgentState:
    """Dummy Node"""
    openai = "Open Ai says hello world"
    state["llm_response"] = openai
    return state

workflow.add_node("hello", hello)

workflow.add_edge(START, "hello")
workflow.add_edge("hello", END)

graph = workflow.compile(checkpointer=checkpointer)