import axios, { AxiosInstance, InternalAxiosRequestConfig, AxiosResponse } from 'axios';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

class APIClient {
  private client: AxiosInstance;

  constructor() {
    this.client = axios.create({
      baseURL: API_BASE_URL,
      headers: {
        'Content-Type': 'application/json',
      },
    });

    // Interceptor para añadir token automáticamente
    this.client.interceptors.request.use((config: InternalAxiosRequestConfig) => {
      const token = localStorage.getItem('token');
      if (token && config.headers) {
        config.headers.Authorization = `Bearer ${token}`;
      }
      return config;
    });

    // Interceptor para manejar errores
    this.client.interceptors.response.use(
      (response: AxiosResponse) => response,
      (error: any) => {
        if (error.response?.status === 401) {
          localStorage.removeItem('token');
          window.location.href = '/login';
        }
        return Promise.reject(error);
      }
    );
  }

  // Auth
  async register(username: string, email: string, password: string) {
    const response = await this.client.post('/api/auth/register', {
      username,
      email,
      password,
    });
    return response.data;
  }

  async login(username: string, password: string) {
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);

    const response = await this.client.post('/api/auth/login', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    });
    return response.data;
  }

  // Chat
  async sendMessage(message: string, sessionId?: string, history: any[] = []) {
    const response = await this.client.post('/api/chat/query', {
      message,
      session_id: sessionId,
      history,
    });
    return response.data;
  }

  // Docs
  async uploadDocument(file: File, category: string = 'general') {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('category', category);

    const response = await this.client.post('/api/docs/upload', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    });
    return response.data;
  }

  async listDocuments() {
    const response = await this.client.get('/api/docs/list');
    return response.data;
  }
}

export const apiClient = new APIClient();
