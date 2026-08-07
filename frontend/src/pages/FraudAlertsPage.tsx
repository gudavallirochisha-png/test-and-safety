import React, { useState } from 'react';
import PageHeader from '../components/common/PageHeader';
import RiskBadge from '../components/common/RiskBadge';
import FilterPanel from '../components/data/FilterPanel';
import SearchBox from '../components/data/SearchBox';
import { useTrustStore } from '../store/useTrustStore';
import { CheckCircleIcon, ClockIcon } from '@heroicons/react/24/outline';

export const FraudAlertsPage: React.FC = () => {
  const { alerts, resolveAlert } = useTrustStore();
  const [filterSeverity, setFilterSeverity] = useState('all');
  const [search, setSearch] = useState('');

  const filteredAlerts = alerts.filter((alert) => {
    const matchesSearch =
      alert.title.toLowerCase().includes(search.toLowerCase()) ||
      alert.description.toLowerCase().includes(search.toLowerCase()) ||
      alert.alertCode.toLowerCase().includes(search.toLowerCase());
    const matchesSeverity = filterSeverity === 'all' || alert.severity === filterSeverity;
    return matchesSearch && matchesSeverity;
  });

  return (
    <div className="space-y-6">
      <PageHeader
        title="Fraud & Security Incident Alerts"
        subtitle="Real-time event stream aggregated from Risk, Review, and Authenticity evaluation pipelines"
        badge="SECURITY QUEUE"
      />

      {/* Filter and Search controls */}
      <div className="flex flex-col sm:flex-row items-center justify-between gap-4">
        <SearchBox value={search} onChange={setSearch} placeholder="Search alerts by code, title, or target..." />
        <FilterPanel
          activeValue={filterSeverity}
          onChange={setFilterSeverity}
          options={[
            { label: 'All Severities', value: 'all' },
            { label: 'Critical', value: 'critical' },
            { label: 'High', value: 'high' },
            { label: 'Medium', value: 'medium' },
          ]}
        />
      </div>

      {/* Alert Cards Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {filteredAlerts.map((alert) => (
          <div
            key={alert.id}
            className={`bg-slate-900 border rounded-xl p-5 shadow-lg flex flex-col justify-between transition-all ${
              alert.isResolved ? 'border-slate-800/60 opacity-60' : 'border-slate-800 hover:border-slate-700'
            }`}
          >
            <div>
              <div className="flex items-center justify-between gap-2 mb-3">
                <div className="flex items-center gap-2">
                  <span className="font-mono text-xs text-sky-400 font-bold px-2 py-0.5 rounded bg-sky-500/10 border border-sky-500/20">
                    {alert.alertCode}
                  </span>
                  <RiskBadge level={alert.severity} />
                </div>
                <span className="text-[11px] font-mono text-slate-400 flex items-center gap-1">
                  <ClockIcon className="w-3.5 h-3.5" />
                  {new Date(alert.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                </span>
              </div>

              <h3 className="text-sm font-bold text-white mb-2">{alert.title}</h3>
              <p className="text-xs text-slate-300 leading-relaxed mb-4">{alert.description}</p>
            </div>

            <div className="pt-3 border-t border-slate-800/80 flex items-center justify-between text-xs">
              <div className="font-mono text-[11px] text-slate-400">
                Source: <span className="text-slate-200">{alert.agentSource}</span> • Target: <span className="text-slate-200">{alert.targetType} ({alert.targetId})</span>
              </div>

              {!alert.isResolved ? (
                <button
                  onClick={() => resolveAlert(alert.id)}
                  className="px-3 py-1.5 rounded bg-sky-500/20 text-sky-400 border border-sky-500/30 text-xs font-semibold hover:bg-sky-500/30 transition-colors flex items-center gap-1"
                >
                  <CheckCircleIcon className="w-4 h-4" /> Resolve
                </button>
              ) : (
                <span className="text-emerald-400 font-semibold font-mono text-xs">Resolved</span>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default FraudAlertsPage;
