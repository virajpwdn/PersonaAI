from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.db import get_db
from api.schema.graph import MessageInput, MessageResponse, ConnectResponse
from api.controllers.graph_controller import personna_user_message
from api.controllers.message_controller import MessageController
import uuid
from api.model.chat import Chat
from api.model.personna import Persona
from api.middlewares.auth_middleware import verify_and_attach_user


router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/message", response_model=MessageResponse)
def send_message(message: MessageInput, db: Session = Depends(get_db), auth: Session = Depends(verify_and_attach_user)):
    """
    Send a message to the agent.
    The message will be processed by LangGraph and checkpointed to PostgreSQL.
    """
    connection_id = str(message.user_id) + str(message.pesona_id)

    conversation = Chat(
        role = message.role,
        content = message.message,
        connection_id = connection_id
    )
    
    db.add(conversation)
    db.commit()
    db.refresh(conversation)
        
    return personna_user_message(db, message, connection_id)
   

@router.get("/persona/connect/{persona_name}", response_model=ConnectResponse)
def get_pesona(persona_name: str, user_id: uuid.UUID, db: Session = Depends(get_db)):
    controller = MessageController()
    return controller.create_persona(persona_name, user_id, db)
