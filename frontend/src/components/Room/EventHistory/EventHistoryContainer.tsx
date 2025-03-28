import React, { useEffect, useState } from 'react';
import EventList from './EventList';
import EventHistoryLoader from './EventHistoryLoader';
import EventHistoryError from './EventHistoryError';
import { GameEventType } from '../../../../types/types';

const EventHistoryContainer: React.FC = () => {
  const [events, setEvents] = useState<GameEventType[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);;

  useEffect(() => {
    // Symulacja pobierania danych z backendu
    const fetchEvents = async () => {
      try {
        const response = await fetch('/api/events'); // Wymaga backendu z odpowiednim endpointem
        if (!response.ok) {
          throw new Error('Błąd podczas ładowania wydarzeń');
        }
        const data = await response.json();
        setEvents(data);
      } catch (err: any) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchEvents();
  }, []);

  if (loading) {
    return <EventHistoryLoader />;
  }

  if (error) {
    return <EventHistoryError message={error} />;
  }

  return (
    <div>
      <EventList events={events} />
    </div>
  );
};


export default EventHistoryContainer;