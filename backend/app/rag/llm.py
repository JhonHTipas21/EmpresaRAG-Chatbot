from openai import OpenAI
from app.core.config import get_settings
from typing import List, Dict

settings = get_settings()

class LLMService:
    def __init__(self):
        """Inicializa cliente OpenAI"""
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = "gpt-4o-mini"
    
    def generate(self, messages: List[Dict[str, str]], temperature: float = 0.2) -> tuple[str, int]:
        """Genera respuesta usando OpenAI"""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            max_tokens=1000
        )
        
        answer = response.choices[0].message.content
        tokens_used = response.usage.total_tokens
        
        return answer, tokens_used

# Singleton
_llm_service = None

def get_llm_service() -> LLMService:
    global _llm_service
    if _llm_service is None:
        _llm_service = LLMService()
    return _llm_service
