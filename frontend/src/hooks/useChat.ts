'use client';

import { useState } from 'react';
import { apiClient } from '@/lib/apiClient';

interface Message {
  role: 'user' | 'assistant';
  content: string;
  sources?: any[];
}

export function useChat() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState(false);
  const [sessionId, setSessionId] = useState<string | null>(null);

  const sendMessage = async (content: string) => {
    // Añadir mensaje del usuario
    const userMessage: Message = { role: 'user', content };
    setMessages((prev: Message[]) => [...prev, userMessage]);
    setLoading(true);

    try {
      const response = await apiClient.sendMessage(content, sessionId || undefined, messages);

      // Añadir respuesta del bot
      const botMessage: Message = {
        role: 'assistant',
        content: response.answer,
        sources: response.sources,
      };
      setMessages((prev: Message[]) => [...prev, botMessage]);
      setSessionId(response.session_id);
    } catch (error: any) {
      const errorMessage: Message = {
        role: 'assistant',
        content: 'Lo siento, hubo un error al procesar tu mensaje. Por favor intenta de nuevo.',
      };
      setMessages((prev: Message[]) => [...prev, errorMessage]);
    } finally {
      setLoading(false);
    }
  };

  const clearChat = () => {
    setMessages([]);
    setSessionId(null);
  };

  return { messages, loading, sendMessage, clearChat };
}
