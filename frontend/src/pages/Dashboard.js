import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import RoomList from '../components/RoomList';


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

  const navigateToRoom = (roomId) => {
    navigate(`/room/${roomId}`);
  };

  return (
    <div className="section">
      <h1 className="title has-text-centered has-text-weight-bold is-size-1 has-text-primary mt-5">Komnata Przygód</h1>
      {/* Używamy RoomList i przekazujemy dane pokoi oraz funkcję do obsługi kliknięcia */}
      <RoomList rooms={rooms} onRoomClick={navigateToRoom} />
    </div>
  );
};

export default Dashboard;
