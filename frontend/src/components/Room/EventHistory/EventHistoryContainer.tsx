import React, { useEffect, useState } from 'react';
import EventList from './EventList';
import EventHistoryLoader from './EventHistoryLoader';
import EventHistoryError from './EventHistoryError';
import { GameEventType } from '../../../../types/types';

interface EventHistoryContainerProps {
  roomId: string;
}

const EventHistoryContainer: React.FC<EventHistoryContainerProps> = ({ roomId }) => {
  const [events, setEvents] = useState<GameEventType[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let isMounted = true; // Flaga do zapobiegania wyścigom danych

    const fetchEvents = async () => {
      try {
        const response = await fetch(`/api/game/events/history/${roomId}`); 
        if (!response.ok) {
          throw new Error('Błąd podczas ładowania wydarzeń');
        }
        const data = await response.json();
        if (isMounted) {
          setEvents(data);
          setLoading(false);
        }
      } catch (err: any) {
        if (isMounted) {
          setError(err.message);
          setLoading(false);
        }
      }
    };

    fetchEvents();

    return () => {
      isMounted = false; // Czyszczenie efektu
    };
  }, [roomId]); // roomId jako zależność

  if (loading) return <EventHistoryLoader />;
  if (error) return <EventHistoryError message={error} />;
  
  return <EventList events={events} />;
};

export default EventHistoryContainer;
