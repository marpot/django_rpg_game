import React, { useState, useEffect } from 'react';
import axios from 'axios';

type CreateRoomFormProps = {
  onRoomCreated: () => void;
};

const CreateRoomForm: React.FC<CreateRoomFormProps> = ({ onRoomCreated }) => {
  const [roomName, setRoomName] = useState<string>('');
  const [adventureId, setAdventureId] = useState<number | null>(null);
  const [adventures, setAdventures] = useState<{ id: number; title: string }[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  // Pobierz dostępne przygody
  useEffect(() => {
    const fetchAdventures = async () => {
      try {
        const response = await axios.get('http://localhost:8000/adventures/adventures');
        setAdventures(response.data); 
      } catch (err) {
        setError('Nie udało się pobrać przygód.');
      }
    };

    fetchAdventures();
  }, []);

  // Funkcja obsługująca wysyłanie formularza
  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const response = await axios.post(
        'http://localhost:8000/api/chat/rooms/',
        {
          name: roomName,
          adventure: adventureId,
        }
      );

      if (response.status === 201) {
        setRoomName('');
        setAdventureId(null);
        onRoomCreated(); // Wywołaj funkcję informującą o stworzeniu pokoju
      }
    } catch (error: any) {
      if (error.response) {
        // W przypadku błędu serwera
        setError(`Błąd: ${error.response.data.detail || 'Nie udało się utworzyć pokoju.'}`);
      } else {
        // W przypadku błędu połączenia lub innego problemu
        setError('Nie udało się utworzyć pokoju. Spróbuj ponownie później.');
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="create-room-form">
      <div className="field">
        <label htmlFor="roomName" className="label">Nazwa pokoju</label>
        <div className="control">
          <input
            type="text"
            id="roomName"
            value={roomName}
            onChange={(e) => setRoomName(e.target.value)}
            required
            className="input"
          />
        </div>
      </div>

      <div className="field">
        <label htmlFor="adventure" className="label">Wybierz przygodę (opcjonalnie)</label>
        <div className="control">
          <div className="select">
            <select
              id="adventure"
              value={adventureId || ''}
              onChange={(e) => setAdventureId(Number(e.target.value))}
            >
              <option value="">Brak przygody</option>
              {adventures?.map((adventure) => (
                <option key={adventure.id} value={adventure.id}>
                  {adventure.title}
                </option>
              ))}
            </select>
          </div>
        </div>
      </div>

      {error && <div className="notification is-danger">{error}</div>}

      <div className="field">
        <div className="control">
          <button type="submit" className={`button is-primary ${loading ? 'is-loading' : ''}`} disabled={loading}>
            Utwórz pokój
          </button>
        </div>
      </div>
    </form>
  );
};

export default CreateRoomForm;
