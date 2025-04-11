import React, { useState } from 'react';
import axios from '../axiosConfig';
import { useNavigate } from 'react-router-dom';
import LoginForm from '../components/LoginPage/LoginForm';
import LoginError from '../components/LoginPage/LoginError';

const LoginPage: React.FC = () => {
  const [errorMessage, setErrorMessage] = useState<string>(''); // Stan dla komunikatów o błędach
  const navigate = useNavigate(); // Hook do nawigacji

  const handleSubmit = async ({ username, password }: { username: string; password: string }) => {
    try {
      // Wysłanie danych logowania do API
      const response = await axios.post(`/api/accounts/login/`, {
        username,
        password,
      });

      // Załadowanie tokenów do localStorage (lub innego mechanizmu przechowywania)
      const { access, refresh } = response.data;
      localStorage.setItem('access_token', access);
      localStorage.setItem('refresh_token', refresh);

      // Po pomyślnym logowaniu przekierowanie na stronę dashboardu
      navigate('/dashboard');
    } catch (error) {
      console.error('❌ Błąd logowania:', error);
      // Ustawienie komunikatu o błędzie, gdy logowanie się nie powiedzie
      setErrorMessage('Niepoprawna nazwa użytkownika lub hasło');
    }
  };

  return (
    <div>
      <section className="section has-background-dark" style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
        <div className="container" style={{ flexGrow: 1, display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
          {errorMessage && <LoginError errorMessage={errorMessage} />}
          <LoginForm onSubmit={handleSubmit} />
        </div>
      </section>
    </div>
  );
};

export default LoginPage;
