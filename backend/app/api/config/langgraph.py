import os
from dotenv import load_dotenv
from langgraph.checkpoint.postgres import PostgresSaver

load_dotenv()

DB_URI=os.getenv("DATABASE_URL")

checkpointer = PostgresSaver.from_conn_string(DB_URI)

def init_checkpointer():
    """Initialize checkpointer - call this once when app starts"""
    checkpointer.setup()
