import React from 'react';
import { useParams, useNavigate, NavigateFunction } from 'react-router-dom';
import Chat from '../components/Chat/ChatRoom';
import './css/RoomPage.css'

interface RoomPageProps{
  roomId: string;
}

const RoomPage: React.FC<RoomPageProps> = () => {
  const params = useParams();
  const roomId = params.roomId;
  const navigate: NavigateFunction = useNavigate();

  return (
    <div className="room-page columns is-gapless is-fullheight">
      {/* Lewy Panel - Lista Graczy */}
      <aside className="column is-3 p-4 has-background-grey-dark">
        <h2 className="title is-4 has-text-white">🧙‍♂️ Postacie</h2>
        <ul className="player-list">
          <li>Thalion - HP: 20/20</li>
          <li>Grom - HP: 18/25</li>
        </ul>
        <button className="button is-danger mt-4" onClick={() => navigate('/dashboard')}>⬅ Powrót</button>
      </aside>

      {/* Środkowy Panel - Historia i Rzuty Kością */}
      <main className="column is-6 p-4 has-background-dark">
        <h1 className="title has-text-white has-text-centered">🏰 Pokój: {roomId}</h1>
        <div className="story-log">
          <p className="has-text-white">Narracja przygody pojawi się tutaj...</p>
        </div>
        <button className="button is-primary mt-4 ml-5">🎲 Rzuć Kością</button>
      </main>

      {/* Prawy Panel - Czat */}
      <aside className="column is-3 p-4 has-background-grey-dark is-fullheight">
        <h2 className="title is-4 has-text-white">💬 Czat</h2>
        <div className="chat-container">
          {roomId && <Chat roomId={roomId} />}
        </div>
      </aside>
    
    </div>
  );
};

export default RoomPage;
