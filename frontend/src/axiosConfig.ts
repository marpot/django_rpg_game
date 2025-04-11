import axios, { AxiosResponse } from 'axios';

axios.defaults.baseURL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

export type { AxiosResponse };

export default axios;