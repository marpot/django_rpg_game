import React from 'react';
import { GameEventType } from 'types/types';

interface GameEventProps{
    event: GameEventType;
}

const GameEvent: React.FC<GameEventProps> = () => {
    return (
        <div>
            <h2>Wydarzenie w grze</h2>
            <p>To jest przykładowe wydarzenie</p>
        </div>
    )
}

export default GameEvent;