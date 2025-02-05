import React from "react";

const ChatMessage = ({ user, text }) => {
  return (
    <div className={`notification ${user === "Ty" ? "right" : "left"}`}>
      <strong>{user}: </strong> {text}
    </div>
  );
};

export default ChatMessage;
