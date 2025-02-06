import React from 'react';

const RoomList = ({ rooms, onRoomClick }) => {
  return (
    <div className="container">
      <div className="columns is-multiline">
        {rooms.map((room) => (
          <div className="column is-one-third" key={room.id}>
            <div
              className="box p-4 is-flex is-flex-direction-column has-text-centered room-box has-background-primary-15"
              onClick={() => onRoomClick(room.id)}
            >
              <h3 className="title is-4 has-text-primary">{room.name}</h3>
              <p className="subtitle is-6 has-text-white">Dołącz do tego pokoju i rozpocznij grę!</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default RoomList;
