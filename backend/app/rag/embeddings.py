from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np

class EmbeddingService:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """Inicializa modelo de embeddings local"""
        self.model = SentenceTransformer(model_name)
    
    def embed_text(self, text: str) -> List[float]:
        """Genera embedding de un texto"""
        embedding = self.model.encode(text, convert_to_tensor=False)
        return embedding.tolist()
    
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Genera embeddings para múltiples documentos"""
        embeddings = self.model.encode(texts, convert_to_tensor=False, show_progress_bar=True)
        return embeddings.tolist()

# Singleton
_embedding_service = None

def get_embedding_service() -> EmbeddingService:
    global _embedding_service
    if _embedding_service is None:
        _embedding_service = EmbeddingService()
    return _embedding_service
