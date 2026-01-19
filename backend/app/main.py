from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import get_settings
from app.api.routes import routes_auth, routes_chat, routes_docs

settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    description="Chatbot empresarial con RAG",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(routes_auth.router)
app.include_router(routes_chat.router)
app.include_router(routes_docs.router)

@app.get("/")
async def root():
    return {
        "message": "EmpresaRAGChatbot API",
        "status": "online",
        "docs": "/docs"
    }

@app.get("/health")
async def health():
    return {"status": "healthy"}
