import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MainLayout from './components/MainLayout';
import Dashboard from './pages/Dashboard';
import RoomPage from './pages/RoomPage';
import Profile from './pages/Profile';
import Settings from './pages/Settings';
import LoginPage from './pages/LoginPage';
import { useParams } from 'react-router';

interface AppProps {
  // Add any props you want to pass to the component here
}

const App: React.FC<AppProps> = () => {
  return (
    <Router>
      <Routes>
        {/* Home Page */}
        <Route path="/" element={
            <LoginPage />
        } />

        {/* Dashboard Page */}
        <Route path="/dashboard" element={
          <MainLayout>
            <Dashboard />
          </MainLayout>
        } />

        {/* Room Page */}
        <Route
          path="/room/:roomId"
          element={
              <RoomPage roomId={useParams().roomId || 'defaultRoomId'} />
        }
        />

        {/* Profile Page */}
        <Route
          path="/profile"
          element={
            <MainLayout>
              <Profile id="profile" onRender={() => console.log('Profile rendered')} />
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
};

export default App;