import React from "react";
import ChatHeader from "./ChatHeader";
import ChatMessages from "./ChatMessages";
import ChatInput from "./ChatInput";
import useChat from "./useChat";
import "../css/Chat.css";


interface ChatProps {
  roomId?: string; 
}

const Chat: React.FC<ChatProps> = ({ roomId }) => {
  const { chatMessages, sendMessage, isTokenValid } = useChat(roomId ?? '');

  if (!isTokenValid) return <div>Brak tokena dostępu</div>;
  if (!roomId) return <div>Pokój nie został wybrany.</div>;

  return (
    <div className="box-chat-container">
      <ChatHeader roomId={roomId} />
      <ChatMessages chatMessages={chatMessages} />
      <ChatInput sendMessage={sendMessage} />
    </div>
  );
};

export default Chat;
