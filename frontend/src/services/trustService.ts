import apiClient from './apiClient';
import overviewMock from '../data/overview.json';
import productsMock from '../data/products.json';
import transactionsMock from '../data/transactions.json';
import reviewsMock from '../data/reviews.json';
import alertsMock from '../data/alerts.json';
import auditMock from '../data/audit.json';

export const trustService = {
  // Health
  getHealth: async () => {
    try {
      return await apiClient.get('/health');
    } catch {
      return { status: 'healthy (fallback)', database_status: 'mock' };
    }
  },

  // Analytics Dashboard
  getAnalytics: async () => {
    try {
      return await apiClient.get('/analytics');
    } catch {
      return overviewMock;
    }
  },

  // Products API
  getProducts: async () => {
    try {
      const res = await apiClient.get('/products');
      return Array.isArray(res) && res.length > 0 ? res : productsMock;
    } catch {
      return productsMock;
    }
  },

  createProduct: async (payload: any) => {
    try {
      return await apiClient.post('/products', payload);
    } catch {
      return payload;
    }
  },

  // Orders / Transactions API
  getTransactions: async () => {
    try {
      const res = await apiClient.get('/orders');
      return Array.isArray(res) && res.length > 0 ? res : transactionsMock;
    } catch {
      return transactionsMock;
    }
  },

  // Reviews API
  getReviews: async () => {
    try {
      const res = await apiClient.get('/reviews');
      return Array.isArray(res) && res.length > 0 ? res : reviewsMock;
    } catch {
      return reviewsMock;
    }
  },

  // Fraud Alerts API
  getAlerts: async () => {
    try {
      const res = await apiClient.get('/alerts');
      return Array.isArray(res) && res.length > 0 ? res : alertsMock;
    } catch {
      return alertsMock;
    }
  },

  resolveAlert: async (alertId: string) => {
    try {
      return await apiClient.put(`/alerts/${alertId}/resolve`);
    } catch {
      return { alert_id: alertId, is_resolved: true };
    }
  },

  // Audit Logs API
  getAuditLogs: async () => {
    try {
      const res = await apiClient.get('/audit');
      return Array.isArray(res) && res.length > 0 ? res : auditMock;
    } catch {
      return auditMock;
    }
  },

  // Placeholder AI APIs
  evaluateRisk: async (payload: any) => {
    try {
      return await apiClient.post('/ai/risk', { payload });
    } catch {
      return { prediction: 'High Risk', confidence: 0.94, reason: 'Placeholder until XGBoost model' };
    }
  },

  evaluateReview: async (payload: any) => {
    try {
      return await apiClient.post('/ai/review', { payload });
    } catch {
      return { prediction: 'Toxic Review Detected', confidence: 0.96, reason: 'Placeholder until DistilBERT model' };
    }
  },

  evaluateProduct: async (payload: any) => {
    try {
      return await apiClient.post('/ai/product', { payload });
    } catch {
      return { prediction: 'Authentic Verified', confidence: 0.98, reason: 'Placeholder until YOLO model' };
    }
  },
};

export default trustService;
