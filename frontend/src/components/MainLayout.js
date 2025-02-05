import React from 'react';
import Sidebar from './Sidebar';


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
