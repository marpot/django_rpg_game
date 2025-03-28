import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { AxiosResponse } from 'axios'; // Add this import

import RoomList from '../components/RoomList';
import ChatLobby from '../components/Chat/ChatLobby';
import CreateRoomForm from '../components/CreateRoomForm';

import axios from 'axios';
import 'bulma/css/bulma.min.css';
import { Room } from '../../types/types';

// Dynamiczne ustawienie proxy
axios.defaults.baseURL = process.env.REACT_APP_API_URL || 'http://localhost:8000';



const Dashboard = () => {
  const navigate = useNavigate();
  const [rooms, setRooms] = useState<Room[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [showCreateRoomForm, setShowCreateRoomForm] = useState<boolean>(false);

  const Authorization = 'Authorization';
  const token = localStorage.getItem('access'); 

  useEffect(() => {
    axios.get<Room[]>('/api/chat/rooms/', { // Remove the comma and pass the options object as the second argument
      headers: {
        [Authorization]: `Bearer ${token}`,
      }
    })
      .then((response: AxiosResponse<Room[]>) => {
        console.log("📌 Otrzymane dane:", response.data);

        if (Array.isArray(response.data)) {
          const updatedRooms: Room[] = response.data.map((room: any) => ({
            id: String(room.id),  // Zamiana id na string
            name: room.name ?? 'Nieznana nazwa',
            adventure: String(room.adventure ?? ''), // Zamiana adventure na string
          }));
          setRooms(updatedRooms);
        } else {
          setError("Błąd podczas przetwarzania danych.");
        }
        setLoading(false);
      })
      .catch(error => {
        setError("Błąd podczas pobierania pokoi.");
        setLoading(false);
        console.error(error);
      });
  }, []);

  const navigateToRoom = (roomId: string) => {
    if (!roomId) {
      setError("Nieprawidłowy identyfikator pokoju.");
      return;
    }
    navigate(`/room/${roomId}`);
  };

  const handleRoomCreated = () => {
    setShowCreateRoomForm(false);
  };

  return (
    <div className="hero is-fullheight">
      <div className="hero-body is-fullheight has-background-dark">
        <div className="container">
          <h1 className="title has-text-warning has-text-centered">Labirynt Przygód</h1>

          {loading && <div className="notification is-info">Ładowanie...</div>}
          {error && <div className="notification is-danger">{error}</div>}
          <div className="columns">
            <div className="column is-6">
              <div className="box has-background-dark has-text-black">
                {!loading && rooms.length === 0 ? (
                  <p className="has-text-centered">Brak dostępnych pokoi.</p>
                ) : (
                  <RoomList rooms={rooms} onRoomClick={navigateToRoom} />
                )}
              </div>
            </div>
            <div className="column is-6">
              <div className="box has-background-dark has-text-black">
                <h2 className="title has-text-primary">Poczekalnia</h2>
                <ChatLobby />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;