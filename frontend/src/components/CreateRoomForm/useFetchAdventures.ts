import { useState, useEffect } from 'react';
import axios from 'axios';

const useFetchAdventures = () => {
  const [adventures, setAdventures] = useState<{ id: number; title: string }[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchAdventures = async () => {
      setLoading(true);
      try {
        const token = localStorage.getItem('token') || 
                     localStorage.getItem('access') || 
                     localStorage.getItem('accessToken');
        
        console.log('Token:', token);

        if (!token) {
          setError('Brak tokenu autoryzacyjnego.');
          setLoading(false);
          return;
        }

        const response = await axios.get('http://localhost:8000/api/adventures/', {
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json',
            'Accept': 'application/json',
          },
          withCredentials: true
        });

        console.log('Response:', response);

        if (response.data) {
          setAdventures(response.data);
        } else {
          setError('Nie udało się pobrać przygód.');
        }
      } catch (err) {
        console.error('Error:', err);
        setError('Nie udało się pobrać przygód.');
      } finally {
        setLoading(false);
      }
    };

    fetchAdventures();
  }, []);

  return { adventures, loading, error };
};

export default useFetchAdventures;