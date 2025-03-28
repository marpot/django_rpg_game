import { useState } from 'react';
import axios from 'axios';

const useCreateRoomForm = (onRoomCreated: () => void) => {
  const [roomName, setRoomName] = useState<string>('');
  const [adventureId, setAdventureId] = useState<number | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setLoading(true);
    setError(null);

    if (!roomName.trim()) {
      setError('Nazwa pokoju jest wymagana.');
      setLoading(false);
      return;
    }

    const token = localStorage.getItem('access');
    
    if (!token) {
      setError('Brak tokenu autoryzacyjnego.');
      setLoading(false);
      return;
    }

    try {
      const response = await axios.post(
        'http://localhost:8000/api/chat/rooms/',
        {
          name: roomName,
          adventure: adventureId ?? null,
        },
        {
          headers: {
            'Authorization': `Bearer ${token}`,
          },
          withCredentials: true,
        }
      );

      if (response.status === 201) {
        setRoomName('');
        setAdventureId(null);
        onRoomCreated();
      } else {
        setError('Nie udało się utworzyć pokoju. Spróbuj ponownie później.');
      }
    } catch (error: any) {
      setError('Nie udało się utworzyć pokoju. Spróbuj ponownie później.');
    } finally {
      setLoading(false);
    }
  };

  return { roomName, setRoomName, adventureId, setAdventureId, handleSubmit, loading, error };
};

export default useCreateRoomForm; 