from fastapi import APIRouter, Depends, HTTPException
from app.models.chat import ChatRequest, ChatResponse
from app.core.security import get_current_user
from app.rag.pipeline import get_rag_pipeline
import uuid

router = APIRouter(prefix="/api/chat", tags=["chat"])

@router.post("/query", response_model=ChatResponse)
async def chat_query(
    request: ChatRequest,
    current_user: dict = Depends(get_current_user)
):
    """Endpoint principal de chat con RAG"""
    try:
        pipeline = get_rag_pipeline()
        
        answer, sources, tokens = pipeline.query(
            user_message=request.message,
            history=request.history
        )
        
        session_id = request.session_id or str(uuid.uuid4())
        
        return ChatResponse(
            answer=answer,
            sources=sources,
            session_id=session_id,
            tokens_used=tokens
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en RAG: {str(e)}")
