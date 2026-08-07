import { create } from 'zustand';
import { ToastMessage, FraudAlertItem } from '../types';
import trustService from '../services/trustService';

interface TrustState {
  sidebarOpen: boolean;
  notificationPanelOpen: boolean;
  searchQuery: string;
  alerts: FraudAlertItem[];
  toasts: ToastMessage[];
  activeFilterRiskLevel: string;
  loading: boolean;
  
  // Actions
  toggleSidebar: () => void;
  setSidebarOpen: (open: boolean) => void;
  toggleNotificationPanel: () => void;
  setSearchQuery: (query: string) => void;
  setActiveFilterRiskLevel: (level: string) => void;
  addToast: (toast: Omit<ToastMessage, 'id'>) => void;
  removeToast: (id: string) => void;
  fetchAlerts: () => Promise<void>;
  resolveAlert: (alertId: string) => Promise<void>;
}

export const useTrustStore = create<TrustState>((set) => ({
  sidebarOpen: true,
  notificationPanelOpen: false,
  searchQuery: '',
  alerts: [],
  toasts: [],
  activeFilterRiskLevel: 'all',
  loading: false,

  toggleSidebar: () => set((state) => ({ sidebarOpen: !state.sidebarOpen })),
  setSidebarOpen: (open) => set({ sidebarOpen: open }),
  toggleNotificationPanel: () => set((state) => ({ notificationPanelOpen: !state.notificationPanelOpen })),
  setSearchQuery: (query) => set({ searchQuery: query }),
  setActiveFilterRiskLevel: (level) => set({ activeFilterRiskLevel: level }),
  
  addToast: (toast) => {
    const id = `toast-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
    set((state) => ({ toasts: [...state.toasts, { ...toast, id }] }));
  },
  
  removeToast: (id) => {
    set((state) => ({ toasts: state.toasts.filter((t) => t.id !== id) }));
  },

  fetchAlerts: async () => {
    set({ loading: true });
    try {
      const data = await trustService.getAlerts();
      set({ alerts: data as FraudAlertItem[] });
    } catch {
      // Fallback handled in service
    } finally {
      set({ loading: false });
    }
  },
  
  resolveAlert: async (alertId) => {
    await trustService.resolveAlert(alertId);
    set((state) => ({
      alerts: state.alerts.map((alert) =>
        alert.id === alertId || (alert as any).alert_id === alertId ? { ...alert, isResolved: true } : alert
      ),
    }));
  },
}));
