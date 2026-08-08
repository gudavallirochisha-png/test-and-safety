import apiClient from './apiClient';
import overviewMock from '../data/overview.json';
import productsMock from '../data/products.json';
import transactionsMock from '../data/transactions.json';
import reviewsMock from '../data/reviews.json';
import alertsMock from '../data/alerts.json';
import auditMock from '../data/audit.json';
import analyticsMock from '../data/analytics.json';

export const trustService = {
  // Health Check
  getHealth: async () => {
    try {
      return await apiClient.get('/health');
    } catch {
      return { status: 'healthy (offline fallback)', database_status: 'mock' };
    }
  },

  // Dashboard Summary & Analytics
  getDashboardSummary: async () => {
    try {
      return await apiClient.get('/dashboard/summary');
    } catch {
      return {
        total_products: overviewMock.totalProducts,
        verified_products: 140000,
        flagged_products: 2850,
        total_transactions: overviewMock.totalTransactions,
        high_risk_transactions: 28720,
        blocked_transactions: 1280,
        total_reviews: overviewMock.totalReviews,
        flagged_reviews: 4200,
        open_alerts: overviewMock.totalFraudAlerts,
        agent_status: overviewMock.agents,
      };
    }
  },

  getAnalytics: async () => {
    try {
      return await apiClient.get('/analytics');
    } catch {
      return analyticsMock;
    }
  },

  // Products API
  getProducts: async (page = 1, limit = 50) => {
    try {
      const res: any = await apiClient.get(`/products?page=${page}&limit=${limit}`);
      return Array.isArray(res) && res.length > 0 ? res : productsMock;
    } catch {
      return productsMock;
    }
  },

  verifyProduct: async (payload: any) => {
    try {
      return await apiClient.post('/products/verify', payload);
    } catch {
      return { product: payload, decision: {}, alert_created: false, audit_log_id: 'AUD-MOCK' };
    }
  },

  // Risk / Transactions API
  getTransactions: async (page = 1, limit = 50) => {
    try {
      const res: any = await apiClient.get(`/risk/transactions?page=${page}&limit=${limit}`);
      return Array.isArray(res) && res.length > 0 ? res : transactionsMock;
    } catch {
      return transactionsMock;
    }
  },

  analyzeRisk: async (payload: any) => {
    try {
      return await apiClient.post('/risk/analyze', payload);
    } catch {
      return { transaction: payload, decision: {}, alert_created: false, audit_log_id: 'AUD-MOCK' };
    }
  },

  // Reviews API
  getReviews: async (page = 1, limit = 50) => {
    try {
      const res: any = await apiClient.get(`/reviews?page=${page}&limit=${limit}`);
      return Array.isArray(res) && res.length > 0 ? res : reviewsMock;
    } catch {
      return reviewsMock;
    }
  },

  analyzeReview: async (payload: any) => {
    try {
      return await apiClient.post('/reviews/analyze', payload);
    } catch {
      return { review: payload, decision: {}, alert_created: false, audit_log_id: 'AUD-MOCK' };
    }
  },

  // Fraud Alerts API
  getAlerts: async (page = 1, limit = 10, severity?: string) => {
    try {
      const query = severity && severity !== 'all' ? `&severity=${severity}` : '';
      const res: any = await apiClient.get(`/alerts?page=${page}&limit=${limit}${query}`);
      if (res && res.items) {
        return res.items;
      }
      return Array.isArray(res) && res.length > 0 ? res : alertsMock;
    } catch {
      return alertsMock;
    }
  },

  updateAlertStatus: async (alertId: string, status: string, resolution_notes?: string) => {
    try {
      return await apiClient.patch(`/alerts/${alertId}/status`, { status, resolution_notes });
    } catch {
      return { alert_id: alertId, status, resolution_notes };
    }
  },

  resolveAlert: async (alertId: string) => {
    try {
      return await apiClient.patch(`/alerts/${alertId}/status`, { status: 'RESOLVED', resolution_notes: 'Resolved by analyst' });
    } catch {
      return { alert_id: alertId, status: 'RESOLVED' };
    }
  },

  // Audit Logs API
  getAuditLogs: async (page = 1, limit = 20) => {
    try {
      const res: any = await apiClient.get(`/audit-logs?page=${page}&limit=${limit}`);
      if (res && res.items) {
        return res.items;
      }
      return Array.isArray(res) && res.length > 0 ? res : auditMock;
    } catch {
      return auditMock;
    }
  },
};

export default trustService;
