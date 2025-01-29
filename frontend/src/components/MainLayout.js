import React from 'react';
import Sidebar from './Sidebar';

//Pozwala na importowanie paczka bocznego w App.js
const MainLayout = ({ children }) => {
  return (
    <div className="columns">
      <div className="column is-one-fifth">
        <Sidebar />
      </div>
      <div className="column">
        {children}
      </div>
    </div>
  );
};

export default MainLayout;
