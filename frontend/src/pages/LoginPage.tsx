import React, { useState } from 'react';
import axios, { AxiosResponse } from 'axios';
import { useNavigate } from 'react-router-dom';
import { Link } from 'react-router-dom';

interface LoginResponse {
  access: string;
  refresh: string;
}

interface LoginPageProps {}

const LoginPage: React.FC<LoginPageProps> = () => {
  const [username, setUsername] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const [errorMessage, setErrorMessage] = useState<string>('');

  const navigate = useNavigate();

  // Funkcja do dekodowania tokena JWT
  const decodeJWT = (token: string) => {
    try {
      const base64Url = token.split('.')[1];
      const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
      const jsonPayload = decodeURIComponent(atob(base64).split('').map(c => 
        '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2)
      ).join(''));
      return JSON.parse(jsonPayload);
    } catch (error) {
      console.error('Błąd dekodowania tokena:', error);
      return null;
    }
  };

  // Funkcja do obsługi wysyłania formularza
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log('Username:', username);
    console.log('Password:', password);
    setErrorMessage('');

    try {
      const response: AxiosResponse<LoginResponse> = await axios.post('http://127.0.0.1:8000/api/accounts/login/', {
        username,
        password,
      });

      // Logowanie odpowiedzi z backendu
      console.log('🔍 Odpowiedź z backendu:', response.data);

      if (response.data.access && response.data.refresh) {
        // Dekodowanie tokena access
        const decodedToken = decodeJWT(response.data.access);
        console.log('🔍 Zdekodowany token:', decodedToken);
        
        if (!decodedToken || !decodedToken.user_id) {
          throw new Error('Nie można zdekodować userId z tokena!');
        }

        // Zapisywanie tokenów
        localStorage.setItem('access', response.data.access);
        localStorage.setItem('refresh', response.data.refresh);
        localStorage.setItem('userId', String(decodedToken.user_id));
        localStorage.setItem('username', username);

        // Sprawdzanie czy tokeny zostały poprawnie zapisane
        const savedAccess = localStorage.getItem('access');
        const savedRefresh = localStorage.getItem('refresh');
        const savedUserId = localStorage.getItem('userId');
        const savedUsername = localStorage.getItem('username');

        console.log('🔑 Zapisane dane:');
        console.log('Access token:', savedAccess);
        console.log('Refresh token:', savedRefresh);
        console.log('UserID:', savedUserId, 'Typ:', typeof savedUserId);
        console.log('Username:', savedUsername);

        if (savedAccess && savedRefresh && savedUserId && savedUsername) {
          console.log('✅ Zalogowano pomyślnie i zapisano tokeny');
          navigate('/dashboard');
        } else {
          throw new Error('Błąd przy zapisywaniu tokenów!');
        }
      } else {
        throw new Error('Brak tokenów w odpowiedzi!');
      }
    } catch (error: unknown) {
      console.error('❌ Błąd logowania:', error);
      setErrorMessage('Niepoprawna nazwa użytkownika lub hasło');
    }
  };

  return (
    <div>
      <section className="section has-background-dark" style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
        <div className="logo-container" style={{ maxWidth: '250px', width: '100%', margin: '0 auto' }}>
          <img
            src="/images/logo_eldoria.png"
            alt="Logo"
            style={{
              maxWidth: '100%',
              height: 'auto',
              objectFit: 'contain',
              marginBottom: '20px',
            }}
          />
        </div>
        <div className="container" style={{ flexGrow: 1, display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
          {errorMessage && <p style={{ color: 'red' }}>{errorMessage}</p>}
          <form onSubmit={handleSubmit}>
            {/* Pole użytkownika */}
            <div className="field">
              <label className="label has-text-white" htmlFor="username">
                Nazwa użytkownika:
              </label>
              <div className="control">
                <input
                  className="input has-text-white"
                  type="text"
                  id="username"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  required
                />
              </div>
            </div>

            {/* Pole hasła */}
            <div className="field">
              <label className="label has-text-white" htmlFor="password">
                Hasło:
              </label>
              <div className="control">
                <input
                  className="input has-text-white"
                  type="password"
                  id="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                />
              </div>
            </div>

            {/* Przycisk */}
            <div className="field">
              <div className="control">
                <button className="button is-primary is-fullwidth" type="submit">
                  Zaloguj
                </button>
              </div>
            </div>
          </form>
        </div>
        <div className="field has-text-centered" style={{ marginTop: '20px' }}>
          <p className="has-text-white">
            Nie masz jeszcze konta? <Link to="/register">Zarejestruj się</Link>
          </p>
        </div>
      </section>
    </div>
  );
};

export default LoginPage;
