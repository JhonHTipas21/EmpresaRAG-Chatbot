'use client';

import { useEffect, useRef } from 'react';
import ReactMarkdown from 'react-markdown';
import type { Components } from 'react-markdown';
import { Bot, User, FileText } from 'lucide-react';

interface Message {
  role: 'user' | 'assistant';
  content: string;
  sources?: any[];
}

export default function MessageList({ messages }: { messages: Message[] }) {
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const markdownComponents: Components = {
    p: (props) => <p className="mb-2 last:mb-0" {...props} />,
    ul: (props) => <ul className="list-disc ml-4 mb-2" {...props} />,
    ol: (props) => <ol className="list-decimal ml-4 mb-2" {...props} />,
  };

  return (
    <div className="flex-1 overflow-y-auto p-4 space-y-4">
      {messages.length === 0 && (
        <div className="flex flex-col items-center justify-center h-full text-gray-500">
          <Bot className="w-16 h-16 mb-4 text-primary-500" />
          <p className="text-lg font-medium">¡Hola! ¿En qué puedo ayudarte?</p>
          <p className="text-sm mt-2">Pregúntame sobre los documentos de la empresa</p>
        </div>
      )}

      {messages.map((message, index) => (
        <div
          key={index}
          className={`flex items-start gap-3 ${
            message.role === 'user' ? 'flex-row-reverse' : ''
          }`}
        >
          <div
            className={`shrink-0 w-8 h-8 rounded-full flex items-center justify-center ${
              message.role === 'user'
                ? 'bg-primary-500 text-white'
                : 'bg-gray-200 text-gray-700'
            }`}
          >
            {message.role === 'user' ? <User size={18} /> : <Bot size={18} />}
          </div>

          <div
            className={`max-w-[70%] rounded-2xl px-4 py-3 ${
              message.role === 'user'
                ? 'bg-primary-500 text-white'
                : 'bg-white border border-gray-200 text-gray-800'
            }`}
          >
            <ReactMarkdown className="prose prose-sm max-w-none" components={markdownComponents}>
              {message.content}
            </ReactMarkdown>

            {/* Fuentes */}
            {message.sources && message.sources.length > 0 && (
              <div className="mt-3 pt-3 border-t border-gray-200">
                <p className="text-xs font-semibold text-gray-600 mb-2 flex items-center gap-1">
                  <FileText size={14} /> Fuentes:
                </p>
                <div className="space-y-1">
                  {message.sources.map((source, idx) => (
                    <div key={idx} className="text-xs text-gray-600">
                      📄 {source.document} {source.page && `(Pág. ${source.page})`}
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>
      ))}

      <div ref={bottomRef} />
    </div>
  );
}
