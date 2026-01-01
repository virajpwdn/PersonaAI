from api.model.personna import Persona
from sqlalchemy.orm import Session
from uuid import UUID
from sqlalchemy.exc import SQLAlchemyError
import logging
from fastapi import HTTPException

logger = logging.getLogger(__name__)

class MessageController:
    def create_persona(self, persona_name: str, user_id: UUID, db: Session):
        """
        To retive or create persona id
        """
        try:
            persona = (
                db.query(Persona).filter(Persona.user_id == user_id, Persona.persona_name == persona_name).first()
            )   
        
            if not persona:
                new_persona = Persona(
                user_id = user_id,
                persona_name = persona_name
            )
            else: 
                return {"data": "Your persona is available", "id": persona.id}
            
            db.add(new_persona)
            db.commit()
            db.refresh(new_persona)
            return {"data": "Your Persona has been created", "id": new_persona.id}
        except SQLAlchemyError as e:
            db.rollback()
            logger.exception("Database error in persona table")
            
            raise HTTPException(status_code=500, detail="Internal server error")
        
        except Exception as e:
            logger.exception("unexpected server error")
            raise HTTPException(status_code=500, detail="unexpected server error")