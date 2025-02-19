import React from 'react';

interface ChatHeaderProps {
  roomId?: string | number;
}

const ChatHeader: React.FC<ChatHeaderProps> = ({ roomId }) => {
  return (
    <div className="chat-header">
      <h2>Pokój: {roomId}</h2>
    </div>
  );
};

export default ChatHeader;