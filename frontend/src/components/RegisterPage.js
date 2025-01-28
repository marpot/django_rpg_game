import React, { useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const RegisterPage = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = {
      username,
      email,
      password
    };

    try {
      await axios.post('http://127.0.0.1:8000/api/accounts/register/', data);
      setMessage('Rejestracja zakończona sukcesem!');
      setError('');
    } catch (err) {
      setError('Błąd rejestracji: ' + err.response.data);
      setMessage('');
    }
  };

  return (
    <div>
      <section className="section">
        <div className="container">
          <h1 className="title has-text-centered">Rejestracja</h1>
          {message && <p style={{ color: 'green' }}>{message}</p>}
          {error && <p style={{ color: 'red' }}>{error}</p>}
          
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

            {/* Pole email */}
            <div className="field">
              <label className="label" htmlFor="email">Email:</label>
              <div className="control">
                <input
                  className="input"
                  type="email"
                  id="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
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
                  Zarejestruj się
                </button>
              </div>
            </div>

          	<div className="field has-text-centered">
            	<p>Masz już konto? <Link to="/">Zaloguj się</Link>></p>
          	</div>
          </form>
        </div>
      </section>
    </div>
  );
};

export default RegisterPage;
