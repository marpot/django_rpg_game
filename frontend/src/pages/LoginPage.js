import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { Link } from 'react-router-dom';

const LoginPage = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  const navigate = useNavigate();

  // Funkcja do obsługi wysyłania formularza
  const handleSubmit = async (e) => {
    e.preventDefault(); 
    console.log('Username:', username); 
    console.log('Password:', password); 
    setErrorMessage('');

    try {
      const response = await axios.post('http://127.0.0.1:8000/api/accounts/login/', {
        username: username,
        password: password,
      });

      console.log('🔍Odpowiedź z backendu:', response.data);

      if (response.data.access && response.data.refresh) {
        localStorage.setItem('access', response.data.access);
        localStorage.setItem('refresh', response.data.refresh);
        localStorage.setItem('username', username);
        console.log('✅ Zalogowano pomyślnie');
        navigate('/dashboard');
      } else {
        throw new Error('Brak tokenów w odpowiedzi!');
      }
    } catch (error) {
      console.error('❌ Błąd logowania:', error.response ? error.response.data : error.message);
      setErrorMessage(error.response?.data?.detail || 'Niepoprawna nazwa użytkownika lub hasło');
    }
  };

  return (
    <div>
      <section className="section"> 
        <div className="container"> 
          <h1 className="title has-text-centered">Logowanie</h1>
          {errorMessage && <p style={{ color: 'red' }}>{errorMessage}</p>}
          <form onSubmit={handleSubmit}>
            {/* Pole użytkownika */}
            <div className="field">
              <label className="label" htmlFor="username">Nazwa użytkownika:</label>
              <div className="control">
                <input 
                  className="input" 
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
              <label className="label" htmlFor="password">Hasło:</label>
              <div className="control">
                <input 
                  className="input" 
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
        <div className="field has-text-centered" style={{ marginTop: '20px'}}>
            <p>Nie masz jeszcze konta? <Link to="/register">Zarejestruj się</Link>></p>
        </div>
      </section>
    </div>
  );
}

export default LoginPage;
