import React from 'react';

const RoomList = ({ rooms, onRoomClick }) => {
  return (
    <div className="container">
      
      <div className="columns is-multiline">
        {rooms.map((room) => (
          <div className="column is-one-third" key={room.id}>
            <div
              className="box has-background-light p-4 is-flex is-flex-direction-column has-text-centered room-box"
              onClick={() => onRoomClick(room.id)}
              style={{
                cursor: 'pointer', 
                transition: 'transform 0.2s ease-in-out',
              }}
              onMouseEnter={(e) => e.currentTarget.style.transform = 'scale(1.05)'}
              onMouseLeave={(e) => e.currentTarget.style.transform = 'scale(1)'}
            >
              <h3 className="title is-4 has-text-primary">{room.name}</h3>
              <p className="subtitle is-6 has-text-grey">Dołącz do tego pokoju i rozpocznij grę!</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default RoomList;
