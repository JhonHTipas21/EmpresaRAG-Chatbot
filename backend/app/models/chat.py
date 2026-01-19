from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class ChatMessage(BaseModel):
    role: str = Field(..., pattern="^(user|assistant)$")
    content: str
    timestamp: Optional[datetime] = None

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=2000)
    session_id: Optional[str] = None
    history: List[ChatMessage] = []

class Source(BaseModel):
    document: str
    page: Optional[int] = None
    content: str
    score: float

class ChatResponse(BaseModel):
    answer: str
    sources: List[Source]
    session_id: str
    tokens_used: Optional[int] = None
