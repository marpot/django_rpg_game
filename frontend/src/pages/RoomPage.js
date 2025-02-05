import React from 'react';
import { useParams } from 'react-router-dom';
import Chat from '../components/Chat/ChatRoom';   

const RoomPage = () => {
  const { roomId } = useParams();

  return (
    <div className="room-page is-fullheight is-flex is-flex-direction-column">
      <div className="container">
        <h1 className="title has-text-centered mt-5">Witamy w pokoju nr {roomId}!</h1>
        <div className="content">
          <div>
            tutaj zrobimy panel postaci, przyciski itp. a może po boku? trzeba ładnie ostylować ten pokój i stronę logowania. Pamiętaj o przycisku powrotu
          </div>
        </div>
      </div>
      <div className="chat-container">
        <Chat roomId={roomId} />
      </div>
    </div>
  );
};

export default RoomPage;
