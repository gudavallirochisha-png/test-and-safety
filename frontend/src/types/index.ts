// TypeScript Domain Definitions for Enterprise AI Trust & Safety Platform

export type RiskLevel = 'low' | 'medium' | 'high' | 'critical';
export type AgentStatus = 'operational' | 'degraded' | 'maintenance' | 'offline';
export type AuditStatus = 'passed' | 'flagged' | 'quarantined' | 'escalated';
export type ActionType = 'APPROVE' | 'REJECT' | 'QUARANTINE' | 'FLAG' | 'AUTO_RESOLVE' | 'ESCALATE';

export interface OverviewMetrics {
  totalProducts: number;
  totalTransactions: number;
  totalReviews: number;
  totalFraudAlerts: number;
  riskDistribution: {
    low: number;
    medium: number;
    high: number;
    critical: number;
  };
  monthlyFraudTrend: Array<{
    month: string;
    fraudAttempts: number;
    preventedLoss: number;
  }>;
  systemHealth: {
    uptime: string;
    apiLatencyMs: number;
    throughputReqSec: number;
    activeAgentsCount: number;
  };
}

export interface AgentHealth {
  id: string;
  name: string;
  type: 'risk' | 'review' | 'authenticity';
  modelEngine: string;
  version: string;
  status: AgentStatus;
  accuracyPercentage: number;
  processed24h: number;
  avgLatencyMs: number;
  lastTrained: string;
}

export interface ProductVerificationItem {
  id: string;
  productName: string;
  sellerId: string;
  sellerName: string;
  category: string;
  price: number;
  imageUrl: string;
  uploadedAt: string;
  authenticityScore: number; // 0 to 100
  riskLevel: RiskLevel;
  yoloDetections: Array<{
    label: string;
    confidence: number;
    boundingBox: [number, number, number, number];
  }>;
  status: 'PENDING' | 'VERIFIED' | 'COUNTERFEIT_FLAGGED' | 'MANUAL_REVIEW';
  flaggedReasons: string[];
}

export interface TransactionRiskItem {
  id: string;
  orderId: string;
  customerId: string;
  customerName: string;
  sellerId: string;
  sellerName: string;
  amount: number;
  paymentMethod: string;
  ipAddress: string;
  deviceFingerprint: string;
  location: string;
  timestamp: string;
  xgboostRiskScore: number; // 0 to 100
  riskLevel: RiskLevel;
  fraudFactors: string[];
  recommendation: ActionType;
  status: 'APPROVED' | 'BLOCKED' | 'FLAGGED_FOR_REVIEW';
}

export interface ReviewModerationItem {
  id: string;
  productId: string;
  productTitle: string;
  reviewerId: string;
  reviewerName: string;
  reviewText: string;
  rating: number;
  timestamp: string;
  distilBertToxicityScore: number; // 0 to 100
  distilBertSentimentScore: number; // -1 to 1
  isFakeReviewProb: number; // 0 to 100
  riskLevel: RiskLevel;
  flaggedCategories: string[];
  status: 'PUBLISHED' | 'REJECTED' | 'PENDING_MODERATION';
  reviewerHistoryStats: {
    totalReviews: number;
    flaggedRatio: number;
    accountAgeDays: number;
  };
}

export interface FraudAlertItem {
  id: string;
  alertCode: string;
  title: string;
  description: string;
  severity: RiskLevel;
  agentSource: 'Risk Agent' | 'Review Agent' | 'Authenticity Agent';
  targetType: 'Seller' | 'Product' | 'Transaction' | 'User';
  targetId: string;
  timestamp: string;
  isResolved: boolean;
  assignedTo?: string;
}

export interface AuditLogItem {
  id: string;
  timestamp: string;
  agentName: string;
  action: ActionType;
  entityId: string;
  entityType: 'Product' | 'Order' | 'Review' | 'Seller';
  status: AuditStatus;
  confidenceScore: number;
  details: string;
}

export interface AnalyticsData {
  riskByType: Array<{ category: string; low: number; medium: number; high: number }>;
  hourlyThreatVolume: Array<{ hour: string; count: number }>;
  agentAccuracyDistribution: Array<{ agent: string; accuracy: number; latency: number }>;
  geoFraudHeatmap: Array<{ country: string; riskScore: number; fraudVolume: number }>;
}

export interface ToastMessage {
  id: string;
  type: 'success' | 'error' | 'warning' | 'info';
  title: string;
  message: string;
}
