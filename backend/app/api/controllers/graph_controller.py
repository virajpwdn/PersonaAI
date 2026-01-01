from api.graph.graph import graph
from api.schema.graph import MessageInput, MessageResponse
from api.model.chat import Chat
from sqlalchemy.orm import Session
from typing import Optional

def personna_user_message(db: Session, message_input: MessageInput, connection_id):
    """
    Controller function that:
    1. Prepares input for the graph
    2. Runs the graph with checkpoint
    3. Saves conversation to database
    4. Returns response
    """
    
    initial_state = {
        "user_query": message_input.message,
        "is_question_relevant": Optional[bool],
        "enhanced_prompt": Optional[str],
        "memory": Optional[str],
        "memory_check": Optional[bool],
        "memory_update_check": Optional[bool],
        "final_response": Optional[str]
    }
    
    config = {"configurable": {"thread_id": connection_id}}
    
    # graph invoke
    final_state = graph.invoke(initial_state, config=config)
    
    # saving graph message into database
    conversation = Chat(
        connection_id = connection_id,
        role = "ai",
        content = final_state["llm_response"],
        user_id = message_input.user_id
    )
    
    db.add(conversation)
    db.commit()
    db.refresh(conversation)
    
    return MessageResponse(
        response=final_state["llm_response"]
    )
    
    # return {"data": "success"}