import React, {useState, useEffect, useRef} from 'react';
import { Component } from 'react';
import Chat from './Chat';
import '../css/Room.css';
import { useParams } from 'react-router-dom';


const Room = () => {
	const { roomId } = useParams();

	return (
			<div className="room-container">
				<h2 className="title is-size-2 has-text-centered has-text-weight-bold">Pokój: {roomId}</h2>
				<Chat roomId={roomId}></Chat>
			</div>
		)
}

export default Room;
