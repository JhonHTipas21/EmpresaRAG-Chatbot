'use client';

import { useEffect } from 'react';
import { useRouter } from 'next/navigation';
import ChatLayout from '@/components/chat/ChatLayout';
import MessageList from '@/components/chat/MessageList';
import MessageInput from '@/components/chat/MessageInput';
import { useChat } from '@/hooks/useChat';

export default function ChatPage() {
  const router = useRouter();
  const { messages, loading, sendMessage } = useChat();

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) {
      router.push('/login');
    }
  }, [router]);

  return (
    <ChatLayout>
      <div className="h-full flex flex-col max-w-5xl mx-auto bg-white rounded-t-3xl shadow-xl">
        <MessageList messages={messages} />
        <MessageInput onSend={sendMessage} loading={loading} />
      </div>
    </ChatLayout>
  );
}
