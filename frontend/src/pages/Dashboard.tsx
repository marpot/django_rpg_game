import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import RoomList from '../components/RoomList';
import ChatLobby from '../components/Chat/ChatLobby';
import 'bulma/css/bulma.min.css';

interface Room {
  id: string;
  name: string;
}

const Dashboard = () => {
  const navigate = useNavigate();
  const [rooms, setRooms] = useState<Room[]>([]);

  useEffect(() => {
    const fetchedRooms: Room[] = [
      { id: "1", name: 'Pokój 1' },
      { id: "2", name: 'Pokój 2' },
      { id: "3", name: 'Pokój 3' },
    ];
    setRooms(fetchedRooms);
  }, []);

  // Funkcja do przejścia do pokoju
  const navigateToRoom = (roomId: string) => {
    navigate(`/room/${roomId}`);
  };

  return (
    <div className="hero is-fullheight">
      <div className="hero-body is-fullheight has-background-dark">
        <div className="container">
          <h1 className="title has-text-warning has-text-centered">Labirynt Przygód</h1>
          <div className="columns">
            <div className="column is-6">
              {/* Lista pokoi */}
              <div className="box has-background-dark has-text-black">
                <RoomList rooms={rooms} onRoomClick={navigateToRoom} />
              </div>
            </div>
            <div className="column is-6">
              {/* Czat w poczekalni */}
              <div className="box has-background-dark has-text-black">
                <h2 className="title has-text-primary">Poczekalnia</h2>
                <ChatLobby /> {/* Wywołanie komponentu ChatLobby dla poczekalni */}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;