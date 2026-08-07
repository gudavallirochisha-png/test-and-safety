import React from 'react';
import { useTrustStore } from '../../store/useTrustStore';
import Drawer from '../feedback/Drawer';
import RiskBadge from '../common/RiskBadge';
import { CheckCircleIcon } from '@heroicons/react/24/outline';

export const NotificationPanel: React.FC = () => {
  const { notificationPanelOpen, toggleNotificationPanel, alerts, resolveAlert } = useTrustStore();

  return (
    <Drawer
      isOpen={notificationPanelOpen}
      onClose={toggleNotificationPanel}
      title="Critical Fraud Alerts"
      width="max-w-md"
    >
      <div className="space-y-4">
        {alerts.map((alert) => (
          <div
            key={alert.id}
            className={`p-4 rounded-xl border transition-all ${
              alert.isResolved
                ? 'bg-slate-950/40 border-slate-800/60 opacity-60'
                : 'bg-slate-900 border-slate-800 shadow-md'
            }`}
          >
            <div className="flex items-center justify-between gap-2 mb-2">
              <RiskBadge level={alert.severity} />
              <span className="text-[11px] font-mono text-slate-400">
                {new Date(alert.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
              </span>
            </div>

            <h4 className="text-sm font-bold text-white mb-1">{alert.title}</h4>
            <p className="text-xs text-slate-300 mb-3">{alert.description}</p>

            <div className="flex items-center justify-between pt-2 border-t border-slate-800/80 text-[11px] font-mono text-slate-400">
              <span>Source: {alert.agentSource}</span>
              {!alert.isResolved ? (
                <button
                  onClick={() => resolveAlert(alert.id)}
                  className="px-2.5 py-1 rounded bg-sky-500/20 text-sky-400 border border-sky-500/30 font-sans text-xs hover:bg-sky-500/30 transition-colors flex items-center gap-1"
                >
                  <CheckCircleIcon className="w-3.5 h-3.5" />
                  Resolve
                </button>
              ) : (
                <span className="text-emerald-400 font-semibold">Resolved</span>
              )}
            </div>
          </div>
        ))}
      </div>
    </Drawer>
  );
};

export default NotificationPanel;
