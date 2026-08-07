import React from 'react';
import PageHeader from '../components/common/PageHeader';
import analyticsData from '../data/analytics.json';
import { ChartBarIcon, MapPinIcon, CpuChipIcon, ShieldExclamationIcon } from '@heroicons/react/24/outline';

export const AnalyticsPage: React.FC = () => {
  return (
    <div className="space-y-6">
      <PageHeader
        title="Platform Risk & Agent Performance Analytics"
        subtitle="Aggregated threat distribution across categories, hourly volume spikes, and geo-fraud heatmaps"
        badge="TELEMETRY & INSIGHTS"
      />

      {/* Grid Row 1: Bar Chart & Pie Chart Graphics */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Category Risk Bar Breakdown */}
        <div className="bg-slate-900 border border-slate-800 rounded-xl p-5 shadow-lg space-y-4">
          <div className="flex items-center justify-between">
            <h3 className="text-sm font-bold text-white flex items-center gap-2">
              <ChartBarIcon className="w-5 h-5 text-sky-400" /> Category Risk Volume Breakdown
            </h3>
            <span className="text-xs font-mono text-slate-400">By Product Category</span>
          </div>

          <div className="space-y-3 pt-2">
            {analyticsData.riskByType.map((item, i) => {
              const total = item.low + item.medium + item.high;
              const highPct = (item.high / total) * 100;
              const medPct = (item.medium / total) * 100;
              const lowPct = (item.low / total) * 100;

              return (
                <div key={i} className="space-y-1">
                  <div className="flex justify-between text-xs font-mono">
                    <span className="text-slate-200 font-semibold">{item.category}</span>
                    <span className="text-slate-400">{total} items evaluated</span>
                  </div>
                  <div className="h-3 w-full bg-slate-950 rounded-full overflow-hidden flex">
                    <div style={{ width: `${lowPct}%` }} className="bg-emerald-500 hover:bg-emerald-400 transition-all" />
                    <div style={{ width: `${medPct}%` }} className="bg-amber-500 hover:bg-amber-400 transition-all" />
                    <div style={{ width: `${highPct}%` }} className="bg-rose-500 hover:bg-rose-400 transition-all" />
                  </div>
                </div>
              );
            })}
          </div>

          <div className="flex items-center justify-end gap-4 text-[11px] font-mono text-slate-400 pt-2 border-t border-slate-800">
            <span className="flex items-center gap-1.5"><span className="w-2.5 h-2.5 rounded-full bg-emerald-500" /> Low</span>
            <span className="flex items-center gap-1.5"><span className="w-2.5 h-2.5 rounded-full bg-amber-500" /> Medium</span>
            <span className="flex items-center gap-1.5"><span className="w-2.5 h-2.5 rounded-full bg-rose-500" /> High Risk</span>
          </div>
        </div>

        {/* Hourly Threat Spike Line Chart Representation */}
        <div className="bg-slate-900 border border-slate-800 rounded-xl p-5 shadow-lg space-y-4">
          <div className="flex items-center justify-between">
            <h3 className="text-sm font-bold text-white flex items-center gap-2">
              <ShieldExclamationIcon className="w-5 h-5 text-sky-400" /> Hourly Threat Attack Velocity
            </h3>
            <span className="text-xs font-mono text-sky-400">Peak @ 21:00 UTC</span>
          </div>

          <div className="h-56 w-full flex items-end justify-between gap-2 pt-6 border-b border-slate-800 pb-2">
            {analyticsData.hourlyThreatVolume.map((item, idx) => (
              <div key={idx} className="flex-1 flex flex-col items-center gap-2 h-full justify-end group">
                <span className="text-[10px] font-mono text-slate-400 opacity-0 group-hover:opacity-100 transition-opacity">
                  {item.count}
                </span>
                <div
                  style={{ height: `${(item.count / 180) * 100}%` }}
                  className="w-full bg-gradient-to-t from-rose-600 to-amber-500 rounded-t-md group-hover:from-rose-500 transition-all shadow-md"
                />
                <span className="text-[10px] font-mono text-slate-400">{item.hour}</span>
              </div>
            ))}
          </div>

          <p className="text-xs text-slate-400">
            High threat velocity detected during evening hours corresponding to bot automated checkout scripts.
          </p>
        </div>
      </div>

      {/* Grid Row 2: Geo Fraud Heatmap & Model Accuracy Latency Matrix */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Geo Fraud Heatmap */}
        <div className="bg-slate-900 border border-slate-800 rounded-xl p-5 shadow-lg space-y-3">
          <h3 className="text-sm font-bold text-white flex items-center gap-2 border-b border-slate-800 pb-3">
            <MapPinIcon className="w-5 h-5 text-sky-400" /> Geographic Fraud Origin Heatmap
          </h3>
          <div className="space-y-2">
            {analyticsData.geoFraudHeatmap.map((geo, i) => (
              <div key={i} className="flex items-center justify-between p-2.5 rounded-lg bg-slate-950/60 border border-slate-800 text-xs">
                <div className="font-semibold text-white">{geo.country}</div>
                <div className="flex items-center gap-4 font-mono">
                  <span className="text-slate-400">{geo.fraudVolume} Incidents</span>
                  <span className={`px-2 py-0.5 rounded font-bold ${geo.riskScore > 50 ? 'bg-rose-500/10 text-rose-400 border border-rose-500/20' : 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20'}`}>
                    Risk: {geo.riskScore}
                  </span>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Model Accuracy & Latency Matrix */}
        <div className="bg-slate-900 border border-slate-800 rounded-xl p-5 shadow-lg space-y-3">
          <h3 className="text-sm font-bold text-white flex items-center gap-2 border-b border-slate-800 pb-3">
            <CpuChipIcon className="w-5 h-5 text-sky-400" /> Agent Accuracy vs Latency Matrix
          </h3>
          <div className="space-y-3">
            {analyticsData.agentAccuracyDistribution.map((item, i) => (
              <div key={i} className="p-3 rounded-lg bg-slate-950/60 border border-slate-800 space-y-2">
                <div className="flex justify-between text-xs">
                  <span className="font-bold text-white">{item.agent}</span>
                  <span className="font-mono text-emerald-400">{item.accuracy}% Accuracy</span>
                </div>
                <div className="flex items-center justify-between text-[11px] font-mono text-slate-400">
                  <span>Avg Latency: <span className="text-sky-400">{item.latency}ms</span></span>
                  <span>Evaluated 24h: <span className="text-slate-200">100k+</span></span>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default AnalyticsPage;
