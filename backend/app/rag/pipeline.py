from typing import List, Dict
from app.rag.vector_store import get_vector_store
from app.rag.llm import get_llm_service
from app.models.chat import ChatMessage, Source

class RAGPipeline:
    def __init__(self):
        self.vector_store = get_vector_store()
        self.llm = get_llm_service()
    
    def query(self, user_message: str, history: List[ChatMessage] = []) -> tuple[str, List[Source], int]:
        """Pipeline RAG completo"""
        
        # 1. Retrieve: buscar documentos relevantes
        search_results = self.vector_store.search(user_message, n_results=5)
        
        # 2. Construir contexto
        context = "\n\n".join([
            f"[Documento: {r['metadata'].get('filename', 'Unknown')} - Página {r['metadata'].get('page', 'N/A')}]\n{r['document']}"
            for r in search_results
        ])
        
        # 3. Construir prompt
        system_prompt = """Eres un asistente empresarial experto. Tu trabajo es responder preguntas usando ÚNICAMENTE la información de los documentos proporcionados.

REGLAS ESTRICTAS:
- Si la información NO está en los documentos, di explícitamente "No encontré información sobre esto en los documentos disponibles."
- SIEMPRE cita el documento y página de donde sacaste la información.
- Sé preciso, profesional y conciso.
- No inventes ni asumas información."""

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"CONTEXTO DE DOCUMENTOS:\n\n{context}\n\n---\n\nPREGUNTA DEL USUARIO: {user_message}"}
        ]
        
        # 4. Generate: llamar LLM
        answer, tokens = self.llm.generate(messages)
        
        # 5. Preparar fuentes
        sources = [
            Source(
                document=r['metadata'].get('filename', 'Unknown'),
                page=r['metadata'].get('page'),
                content=r['document'][:200] + "...",
                score=1 - (r['distance'] or 0)
            )
            for r in search_results[:3]
        ]
        
        return answer, sources, tokens

# Singleton
_rag_pipeline = None

def get_rag_pipeline() -> RAGPipeline:
    global _rag_pipeline
    if _rag_pipeline is None:
        _rag_pipeline = RAGPipeline()
    return _rag_pipeline
