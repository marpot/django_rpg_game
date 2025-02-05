import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';
import 'bulma/css/bulma.min.css';

import MainLayout from './components/MainLayout';  //importujemy MainLayout żeby było menu po lewej stronie i importujemy w routach w których ma być

import Dashboard from './pages/Dashboard';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import Profile from './pages/Profile';
import Settings from './pages/Settings';
import RoomPage from './pages/RoomPage';

function App() {
  return (
    <Router>
      <Routes>
        {/* Login Page */}
        <Route path="/" element={<LoginPage />} />

        {/* Register Page */}
        <Route path="/register" element={<RegisterPage />} />

        {/* Dashboard with Sidebar and Roomlist */}
        <Route path="/dashboard" element={
            <MainLayout>
              <Dashboard />
            </MainLayout>
          } 
        />

        {/* Room */}
        <Route 
          path="/room/:roomId"
          element={<RoomPage /> 
        } 
         />
          

        {/* Profile Page */}
        <Route 
          path="/profile" 
          element={
            <MainLayout>
              <Profile />
            </MainLayout>
          } 
        />

        {/* Settings Page */}
        <Route 
          path="/settings" 
          element={
            <MainLayout>
              <Settings />
            </MainLayout>
          } 
        />
      </Routes>
    </Router>
  );
}

export default App;
