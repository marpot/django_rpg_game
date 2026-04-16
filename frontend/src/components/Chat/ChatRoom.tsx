// components/Chat/ChatRoom.tsx
import React, { useState, useEffect, useRef } from 'react';
import '../css/Chat.css';

interface ChatMessage {
  id: number;
  text: string;
  user: string;
}

const ChatRoom: React.FC<{ roomId: string }> = ({ roomId }) => {
  const [chatMessages, setChatMessages] = useState<ChatMessage[]>([{ id: 1, text: "Rozpocznij czat!", user: "System" }]);
  const [messageInput, setMessageInput] = useState<string>("");
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const socket = useRef<WebSocket | null>(null);
  const usernameRef = useRef<string>(localStorage.getItem('username') || 'Anonim');
  const accessToken = localStorage.getItem('access');
  const [isTokenValid, setIsTokenValid] = useState<boolean | null>(null);

  useEffect(() => {
    setIsTokenValid(!!accessToken);
  }, [accessToken]);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chatMessages]);

  const connectWebSocket = () => {
    if (socket.current && socket.current.readyState === WebSocket.OPEN) {
      console.log("⚠️ WebSocket jest już otwarty.");
      return;
    }

    const wsUrl = `ws://backend:8001/ws/chat/${roomId}/?token=${accessToken}`;
    socket.current = new WebSocket(wsUrl);

    socket.current.onopen = () => {
      console.log("✅ WebSocket połączony z pokojem");
    };

    socket.current.onerror = (error) => {
      console.error("❌ Błąd WebSocket", error);
    };

    socket.current.onmessage = (e) => {
      const data = JSON.parse(e.data);
      console.log("📩 Otrzymana wiadomość:", data);

      setChatMessages((prevMessages) => [
        ...prevMessages,
        {
          id: prevMessages.length + 1,
          text: data.message,
          user: data.sender || usernameRef.current || "Inny",
        },
      ]);
    };

    socket.current.onclose = () => {
      console.warn("⚠️ WebSocket zamknięty, próbuj ponownie połączyć za 3 sekundy...");
      socket.current = null;
      setTimeout(connectWebSocket, 3000);
    };
  };

  useEffect(() => {
    if (isTokenValid) {
      connectWebSocket();
      return () => {
        if (socket.current) {
          socket.current.close();
          socket.current = null;
        }
      };
    }
  }, [isTokenValid]);

  const sendMessage = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    if (!socket.current || socket.current.readyState !== WebSocket.OPEN) {
      console.error("❌ WebSocket nie jest otwarty. Nie można wysłać wiadomości.");
      return;
    }

    if (!messageInput.trim()) return;

    const messageData = {
      message: messageInput,
      sender: usernameRef.current,
    };

    socket.current.send(JSON.stringify(messageData));
    setMessageInput("");
  };

  return (
    <div className="box-chat-container">
      <div className="chat-messages">
        {chatMessages.map((msg) => (
          <div key={msg.id} className={`notification ${msg.user === 'Ty' ? 'right' : 'left'}`}>
            <strong>{msg.user}: </strong> {msg.text}
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>
      <form onSubmit={sendMessage} className="chat-form">
        <div className="field has-addons">
          <div className="control is-expanded">
            <input
              className="input"
              type="text"
              value={messageInput}
              onChange={(e) => setMessageInput(e.target.value)}
              placeholder="Napisz wiadomość..."
            />
          </div>
          <div className="control">
            <button type="submit" className="button is-info">
              Wyślij
            </button>
          </div>
        </div>
      </form>
    </div>
  );
};

export default ChatRoom;