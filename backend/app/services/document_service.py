from pypdf import PdfReader
from fastapi import UploadFile, HTTPException
from typing import List
import uuid
from app.rag.vector_store import get_vector_store

class DocumentService:
    def __init__(self):
        self.vector_store = get_vector_store()
    
    async def process_pdf(self, file: UploadFile, category: str = "general") -> dict:
        """Procesa PDF y lo añade al vector store"""
        
        if not file.filename.endswith('.pdf'):
            raise HTTPException(status_code=400, detail="Solo se aceptan archivos PDF")
        
        # Leer PDF
        content = await file.read()
        reader = PdfReader(content)
        
        texts = []
        metadatas = []
        ids = []
        
        # Extraer texto por página
        for page_num, page in enumerate(reader.pages):
            text = page.extract_text()
            if text.strip():
                # Chunking simple (500 caracteres)
                chunks = [text[i:i+500] for i in range(0, len(text), 400)]  # overlap 100
                
                for chunk_idx, chunk in enumerate(chunks):
                    texts.append(chunk)
                    metadatas.append({
                        "filename": file.filename,
                        "page": page_num + 1,
                        "category": category,
                        "chunk": chunk_idx
                    })
                    ids.append(f"{file.filename}_{page_num}_{chunk_idx}_{uuid.uuid4().hex[:8]}")
        
        # Añadir al vector store
        self.vector_store.add_documents(texts, metadatas, ids)
        
        return {
            "filename": file.filename,
            "pages": len(reader.pages),
            "chunks": len(texts),
            "status": "processed"
        }
    
    def list_documents(self) -> List[dict]:
        """Lista documentos únicos"""
        all_docs = self.vector_store.get_all_documents()
        unique_files = {}
        
        for doc in all_docs:
            filename = doc['metadata'].get('filename', 'Unknown')
            if filename not in unique_files:
                unique_files[filename] = {
                    "filename": filename,
                    "category": doc['metadata'].get('category', 'general'),
                    "chunks": 1
                }
            else:
                unique_files[filename]["chunks"] += 1
        
        return list(unique_files.values())

def get_document_service() -> DocumentService:
    return DocumentService()
