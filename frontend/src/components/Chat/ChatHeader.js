import React from "react";

const ChatHeader = ({ roomId }) => {
  return (
    <div className="chat-header">
      <h2>Pokój: {roomId}</h2>
    </div>
  );
};

export default ChatHeader;
