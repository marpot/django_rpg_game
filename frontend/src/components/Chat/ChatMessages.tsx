import React, { useRef, useEffect } from "react";
import ChatMessage from "./ChatMessage";
import "../css/Chat.css";

interface ChatMessageProps {
  id: number;
  text: string;
  user: string;
}


const ChatMessages: React.FC<{chatMessages: ChatMessageProps[];}> = ({ chatMessages }) => {
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chatMessages]);

  return (
    <div className="chat-messages">
      {chatMessages.map((msg) => (
        <ChatMessage key={msg.id} user={msg.user} text={msg.text} />
      ))}
      <div ref={messagesEndRef} />
    </div>
  );
};

export default ChatMessages;
