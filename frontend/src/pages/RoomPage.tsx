import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import Chat from '../components/Chat/ChatRoom';
import './css/RoomPage.css';
import { Room } from '../../types/types';
import EventHistoryContainer from '../components/Room/EventHistory/EventHistoryContainer';


const RoomPage: React.FC = () => {
  const { roomId } = useParams<{ roomId: string }>();  // Pobieramy roomId z parametrów URL
  const navigate = useNavigate();


  if (!roomId) {
    return <div>Brak dostępnego pokoju.</div>;  // Jeśli roomId nie istnieje, wyświetl komunikat
  }

  return (
    <div className="room-page columns is-gapless is-fullheight">
      <aside className="column is-3 p-4 has-background-grey-dark">
        <h2 className="title is-4 has-text-white">🧙‍♂️ Postacie</h2>
        <ul className="player-list">
          <li>Thalion - HP: 20/20</li>
          <li>Grom - HP: 18/25</li>
        </ul>
        <button className="button is-danger mt-4" onClick={() => navigate('/dashboard')}>⬅ Powrót</button>
      </aside>

      <main className="column is-6 p-4 has-background-dark">
        <h1 className="title has-text-white has-text-centered">🏰 Pokój: {roomId}</h1>
        <div className="story-log">
          <EventHistoryContainer roomId={roomId} />
        </div>
        <button className="button is-primary mt-4 ml-5">🎲 Rzuć Kością</button>
      </main>

      <aside className="column is-3 p-4 has-background-grey-dark is-fullheight">
        <h2 className="title is-4 has-text-white">💬 Czat</h2>
        <div className="chat-container">
          <Chat roomId={roomId} />
        </div>
      </aside>
    </div>
  );
};

export default RoomPage;
