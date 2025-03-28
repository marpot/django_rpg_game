import React from 'react';
import GameEvent from './GameEvent';
import { GameEventType } from '../../../../types/types';

interface EventListProps {
  events: GameEventType[];
}

const EventList: React.FC<EventListProps> = ({ events }) => {
  return (
    <div>
      {events.map((event, index) => (
        <GameEvent key={index} event={event} />
      ))}
    </div>
  );
};

export default EventList;