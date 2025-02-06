import React from 'react';
import { Link } from 'react-router-dom'
import { useNavigate } from 'react-router-dom';


const Sidebar = () => {
  const navigate = useNavigate();

  return (
    <aside className="menu">
      <p className="menu-label mt-5 has-text-centered">Panel kontrolny</p>
      <ul className="menu-list has-text-centered">
        <button className="button is-fullwidth is-primary mt-5" onClick={() => navigate('/dashboard')}>Dashboard</button>
        <button className="button is-fullwidth is-primary mt-5" onClick={() => navigate('/profile')}>Profil</button>
        <button className="button is-fullwidth is-primary mt-5" onClick={() => navigate('/settings')}>Ustawienia</button>
        <button className="button is-fullwidth is-primary mt-5" onClick={() => navigate('/')}>Wyloguj się</button>
      </ul>
    </aside>
  );
};

export default Sidebar;
