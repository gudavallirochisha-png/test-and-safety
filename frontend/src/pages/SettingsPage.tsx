import React, { useState } from 'react';
import PageHeader from '../components/common/PageHeader';
import { useTrustStore } from '../store/useTrustStore';
import {
  BellIcon,
  CpuChipIcon,
  InformationCircleIcon,
  PaintBrushIcon,
} from '@heroicons/react/24/outline';

export const SettingsPage: React.FC = () => {
  const { addToast } = useTrustStore();
  const [emailAlerts, setEmailAlerts] = useState(true);
  const [slackAlerts, setSlackAlerts] = useState(true);
  const [autoQuarantine, setAutoQuarantine] = useState(true);

  const handleSaveSettings = (e: React.FormEvent) => {
    e.preventDefault();
    addToast({
      type: 'success',
      title: 'Configuration Updated',
      message: 'Trust & Safety agent threshold and notification settings persisted.',
    });
  };

  return (
    <div className="space-y-6">
      <PageHeader
        title="System & Agent Configuration"
        subtitle="Manage risk score boundaries, real-time alert dispatch, and AI model parameters"
        badge="SYSTEM CONFIG"
      />

      <form onSubmit={handleSaveSettings} className="space-y-6">
        {/* Theme Settings */}
        <div className="bg-slate-900 border border-slate-800 rounded-xl p-5 shadow-lg space-y-3">
          <h3 className="text-sm font-bold text-white flex items-center gap-2 border-b border-slate-800 pb-3">
            <PaintBrushIcon className="w-5 h-5 text-sky-400" /> Platform Design Theme
          </h3>
          <div className="flex items-center justify-between text-xs">
            <div>
              <span className="text-white font-semibold block">Dark Mode Theme (Default)</span>
              <span className="text-slate-400">High-contrast slate palette optimized for SOC monitoring environments</span>
            </div>
            <span className="px-2.5 py-1 rounded bg-sky-500/10 text-sky-400 font-mono text-xs border border-sky-500/20">
              Active Dark Mode
            </span>
          </div>
        </div>

        {/* Notification Settings */}
        <div className="bg-slate-900 border border-slate-800 rounded-xl p-5 shadow-lg space-y-4">
          <h3 className="text-sm font-bold text-white flex items-center gap-2 border-b border-slate-800 pb-3">
            <BellIcon className="w-5 h-5 text-sky-400" /> Real-time Alert Notification Channels
          </h3>
          <div className="space-y-3">
            <div className="flex items-center justify-between text-xs">
              <div>
                <span className="text-white font-semibold block">Critical Email Alerts</span>
                <span className="text-slate-400">Dispatch instant email to SOC team on critical severity alerts</span>
              </div>
              <input
                type="checkbox"
                checked={emailAlerts}
                onChange={(e) => setEmailAlerts(e.target.checked)}
                className="w-4 h-4 rounded bg-slate-950 border-slate-800 text-sky-500 focus:ring-sky-500"
              />
            </div>
            <div className="flex items-center justify-between text-xs pt-2 border-t border-slate-800/60">
              <div>
                <span className="text-white font-semibold block">Slack Incident Channel Webhook</span>
                <span className="text-slate-400">Post automated JSON payloads to #trust-safety-alerts</span>
              </div>
              <input
                type="checkbox"
                checked={slackAlerts}
                onChange={(e) => setSlackAlerts(e.target.checked)}
                className="w-4 h-4 rounded bg-slate-950 border-slate-800 text-sky-500 focus:ring-sky-500"
              />
            </div>
          </div>
        </div>

        {/* AI Agent Configuration (Placeholder Parameters) */}
        <div className="bg-slate-900 border border-slate-800 rounded-xl p-5 shadow-lg space-y-4">
          <h3 className="text-sm font-bold text-white flex items-center gap-2 border-b border-slate-800 pb-3">
            <CpuChipIcon className="w-5 h-5 text-sky-400" /> AI Micro-Agent Parameters (Phase 2 Placeholder)
          </h3>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label className="text-[11px] font-mono text-slate-400 block mb-1">
                XGBoost High Risk Threshold (0.0 - 1.0)
              </label>
              <input
                type="number"
                step="0.05"
                defaultValue={0.85}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg px-3 py-2 text-xs font-mono text-white focus:outline-none focus:border-sky-500"
              />
            </div>
            <div>
              <label className="text-[11px] font-mono text-slate-400 block mb-1">
                DistilBERT Toxicity Threshold (0.0 - 1.0)
              </label>
              <input
                type="number"
                step="0.05"
                defaultValue={0.75}
                className="w-full bg-slate-950 border border-slate-800 rounded-lg px-3 py-2 text-xs font-mono text-white focus:outline-none focus:border-sky-500"
              />
            </div>
          </div>

          <div className="flex items-center justify-between text-xs pt-2 border-t border-slate-800/60">
            <div>
              <span className="text-white font-semibold block">Auto-Quarantine High Severity Listings</span>
              <span className="text-slate-400">Freeze seller payouts instantly when risk score &gt; 90%</span>
            </div>
            <input
              type="checkbox"
              checked={autoQuarantine}
              onChange={(e) => setAutoQuarantine(e.target.checked)}
              className="w-4 h-4 rounded bg-slate-950 border-slate-800 text-sky-500 focus:ring-sky-500"
            />
          </div>
        </div>

        {/* System Information */}
        <div className="bg-slate-900 border border-slate-800 rounded-xl p-5 shadow-lg space-y-3">
          <h3 className="text-sm font-bold text-white flex items-center gap-2 border-b border-slate-800 pb-3">
            <InformationCircleIcon className="w-5 h-5 text-sky-400" /> Platform Telemetry & System Info
          </h3>
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs font-mono">
            <div className="p-3 rounded bg-slate-950 border border-slate-800">
              <span className="text-slate-400 block text-[10px]">Framework</span>
              <span className="text-white font-bold">React 19 + Vite</span>
            </div>
            <div className="p-3 rounded bg-slate-950 border border-slate-800">
              <span className="text-slate-400 block text-[10px]">State Engine</span>
              <span className="text-white font-bold">Zustand 4.5</span>
            </div>
            <div className="p-3 rounded bg-slate-950 border border-slate-800">
              <span className="text-slate-400 block text-[10px]">Styling System</span>
              <span className="text-white font-bold">Tailwind CSS v3.4</span>
            </div>
            <div className="p-3 rounded bg-slate-950 border border-slate-800">
              <span className="text-slate-400 block text-[10px]">Data Mode</span>
              <span className="text-emerald-400 font-bold">Phase 2 Mock JSON</span>
            </div>
          </div>
        </div>

        <button
          type="submit"
          className="px-6 py-2.5 rounded-lg bg-sky-500 hover:bg-sky-400 text-white text-xs font-semibold shadow-lg shadow-sky-500/20 transition-all"
        >
          Save System Configuration
        </button>
      </form>
    </div>
  );
};

export default SettingsPage;
