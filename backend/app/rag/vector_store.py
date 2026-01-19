import chromadb
from chromadb.config import Settings
from typing import List, Dict, Any
from app.core.config import get_settings
from app.rag.embeddings import get_embedding_service

settings = get_settings()

class VectorStore:
    def __init__(self):
        """Inicializa Chroma con persistencia"""
        self.client = chromadb.Client(Settings(
            persist_directory=settings.CHROMA_PERSIST_DIR,
            anonymized_telemetry=False
        ))
        self.embedding_service = get_embedding_service()
        self.collection = self.client.get_or_create_collection(
            name="enterprise_docs",
            metadata={"hnsw:space": "cosine"}
        )
    
    def add_documents(self, texts: List[str], metadatas: List[Dict[str, Any]], ids: List[str]):
        """Añade documentos al vector store"""
        embeddings = self.embedding_service.embed_documents(texts)
        self.collection.add(
            embeddings=embeddings,
            documents=texts,
            metadatas=metadatas,
            ids=ids
        )
    
    def search(self, query: str, n_results: int = 5) -> List[Dict[str, Any]]:
        """Busca documentos similares"""
        query_embedding = self.embedding_service.embed_text(query)
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )
        
        formatted_results = []
        for i in range(len(results['ids'][0])):
            formatted_results.append({
                'id': results['ids'][0][i],
                'document': results['documents'][0][i],
                'metadata': results['metadatas'][0][i],
                'distance': results['distances'][0][i] if 'distances' in results else None
            })
        
        return formatted_results
    
    def delete_document(self, doc_id: str):
        """Elimina documento por ID"""
        self.collection.delete(ids=[doc_id])
    
    def get_all_documents(self) -> List[Dict[str, Any]]:
        """Lista todos los documentos"""
        result = self.collection.get()
        return [
            {"id": id_, "metadata": meta}
            for id_, meta in zip(result['ids'], result['metadatas'])
        ]

# Singleton
_vector_store = None

def get_vector_store() -> VectorStore:
    global _vector_store
    if _vector_store is None:
        _vector_store = VectorStore()
    return _vector_store
