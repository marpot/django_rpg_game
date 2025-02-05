import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import RoomList from '../components/RoomList'; 
import ChatLobby from '../components/Chat/ChatLobby'; 

const Dashboard = () => {
  const navigate = useNavigate();
  const [rooms, setRooms] = useState([]);

  useEffect(() => {
    const fetchedRooms = [
      { id: 1, name: 'Pokój 1' },
      { id: 2, name: 'Pokój 2' },
      { id: 3, name: 'Pokój 3' },
    ];
    setRooms(fetchedRooms);
  }, []);

  // Funkcja do przejścia do pokoju
  const navigateToRoom = (roomId) => {
    navigate(`/room/${roomId}`);
  };

  return (
    <div className="no-scroll">
      <h1 className="title has-text-centered has-text-weight-bold is-size-1 has-text-primary mt-5">Komnata Przygód</h1>

      {/* Lista pokoi */}
      <div className="rooms-section">
        <RoomList rooms={rooms} onRoomClick={navigateToRoom} />
      </div>

      {/* Czat w poczekalni */}
      <div className="section chat-section">
        <h2 className="title is-size-3 has-text-centered has-text-weight-bold is-size-1 has-text-primary mt-5">Poczekalnia</h2>
        <ChatLobby /> {/* Wywołanie komponentu ChatLobby dla poczekalni */}
      </div>
    </div>
  );
};

export default Dashboard;
