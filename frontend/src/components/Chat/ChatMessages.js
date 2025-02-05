import React, { useRef, useEffect } from "react";
import ChatMessage from "./ChatMessage";

const ChatMessages = ({ chatMessages }) => {
  const messagesEndRef = useRef(null);

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
