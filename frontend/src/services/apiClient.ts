import axios from 'axios';

const API_BASE_URL = (import.meta as any).env?.VITE_API_BASE_URL || 'http://localhost:8000/api/v1';

export const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 10000,
});

// Response Interceptor
apiClient.interceptors.response.use(
  (response) => response.data,
  (error) => {
    console.error('API Request Error:', error.response?.data || error.message);
    return Promise.reject(error);
  }
);

export default apiClient;
