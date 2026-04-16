import axios from "../../axiosConfig";

export const handleSubmit = async (data: { username: string; password: string }) => {
  try {
    const response = await axios.post('/api/accounts/login/', data);   
     console.log('✅ Zalogowano', response.data);
  } catch (error) {
    console.error('❌ Błąd logowania:', error);
  }
};
