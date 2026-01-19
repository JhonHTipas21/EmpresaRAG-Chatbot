from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from typing import List
from app.core.security import get_current_user
from app.services.document_service import get_document_service

router = APIRouter(prefix="/api/docs", tags=["documents"])

@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    category: str = "general",
    current_user: dict = Depends(get_current_user),
    doc_service = Depends(get_document_service)
):
    """Sube y procesa un documento PDF"""
    try:
        result = await doc_service.process_pdf(file, category)
        return {"message": "Documento procesado exitosamente", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/list")
async def list_documents(
    current_user: dict = Depends(get_current_user),
    doc_service = Depends(get_document_service)
):
    """Lista todos los documentos"""
    docs = doc_service.list_documents()
    return {"documents": docs}
