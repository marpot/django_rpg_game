import React from 'react';
import { Link } from 'react-router-dom'

const Sidebar = () => {
  return (
    <aside className="menu">
      <p className="menu-label mt-5 has-text-centered">Panel kontrolny</p>
      <ul className="menu-list has-text-centered">
        <li><Link to="/dashboard">Dashboard</Link></li>
        <li><Link to="/profile">Profil</Link></li>
        <li><Link to="/settings">Ustawienia</Link></li>
        <li><Link to="/">Wyloguj się</Link></li>
      </ul>
    </aside>
  );
};

export default Sidebar;
