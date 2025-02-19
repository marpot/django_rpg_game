import React from 'react';
import Chat from './Chat/Chat';
import '../css/Room.css';
import { useParams } from 'react-router-dom';

const Room: React.FC = () => {
  const { roomId } = useParams<{ roomId: string }>();
  const roomIdStr = roomId ?? undefined;

  return (
    <div className="room-container">
      <h2 className="title is-size-2 has-text-centered has-text-weight-bold">
        Pokój: {roomIdStr}
      </h2>
      <Chat roomId={roomIdStr} />
    </div>
  );
};

export default Room;
