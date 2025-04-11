import axios from "../../axiosConfig";

export const handleSubmit = async (data: { username: string; password: string }) => {
  try {
    const response = await axios.post(`${process.env.REACT_APP_API_URL}/api/accounts/login/`, data);
    console.log('✅ Zalogowano', response.data);
  } catch (error) {
    console.error('❌ Błąd logowania:', error);
  }
};
