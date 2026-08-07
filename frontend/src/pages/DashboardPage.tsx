import React from 'react';
import { PageHeader } from '../components/common/PageHeader';
import { StatCard } from '../components/common/StatCard';
import { AgentStatusCard } from '../components/common/AgentStatusCard';
import { ActivityTimeline } from '../components/common/ActivityTimeline';
import { useTrustStore } from '../store/useTrustStore';

import overviewData from '../data/overview.json';
import auditData from '../data/audit.json';

import {
  ShoppingBagIcon,
  ShieldCheckIcon,
  ChatBubbleBottomCenterTextIcon,
  BellAlertIcon,
  ArrowPathIcon,
  BoltIcon,
} from '@heroicons/react/24/outline';

export const DashboardPage: React.FC = () => {
  const { addToast } = useTrustStore();

  const handleQuickScan = () => {
    addToast({
      type: 'info',
      title: 'Agent Evaluation Triggered',
      message: 'Dispatched synchronous batch assessment to Risk, Review, and Authenticity agents.',
    });
  };

  return (
    <div className="space-y-6">
      <PageHeader
        title="Trust & Safety Command Center"
        subtitle="Real-time evaluation metrics across XGBoost, DistilBERT, and YOLO micro-agent pipelines"
        badge="LIVE TELEMETRY"
        actions={
          <button
            onClick={handleQuickScan}
            className="flex items-center gap-2 px-4 py-2 rounded-lg bg-sky-500 hover:bg-sky-400 text-white text-xs font-semibold shadow-lg shadow-sky-500/20 transition-all"
          >
            <BoltIcon className="w-4 h-4" />
            Trigger Micro-Scan
          </button>
        }
      />

      {/* Overview Metric Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard
          title="Total Products Screened"
          value={overviewData.totalProducts.toLocaleString()}
          change="12.4%"
          isPositive={true}
          icon={<ShieldCheckIcon className="w-5 h-5" />}
          subtitle="YOLO visual inspection active"
        />
        <StatCard
          title="Transactions Evaluated"
          value={overviewData.totalTransactions.toLocaleString()}
          change="8.1%"
          isPositive={true}
          icon={<ShoppingBagIcon className="w-5 h-5" />}
          subtitle="XGBoost risk engine v2.4"
        />
        <StatCard
          title="Reviews Moderated"
          value={overviewData.totalReviews.toLocaleString()}
          change="4.2%"
          isPositive={true}
          icon={<ChatBubbleBottomCenterTextIcon className="w-5 h-5" />}
          subtitle="DistilBERT NLP sentiment & toxicity"
        />
        <StatCard
          title="Fraud Alerts Triggered"
          value={overviewData.totalFraudAlerts.toLocaleString()}
          change="3.1%"
          isPositive={false}
          icon={<BellAlertIcon className="w-5 h-5" />}
          subtitle="Critical velocity & IP violations"
        />
      </div>

      {/* AI Agents Operational Status Grid */}
      <div>
        <h2 className="text-base font-bold text-white mb-3 flex items-center gap-2">
          <span className="w-2 h-2 rounded-full bg-emerald-400" />
          Active Micro-Agent Subsystems
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {overviewData.agents.map((agent) => (
            <AgentStatusCard key={agent.id} agent={agent as any} />
          ))}
        </div>
      </div>

      {/* Chart & Activity Timeline Split View */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Fraud Trend Chart (Dummy Graphic Representation) */}
        <div className="lg:col-span-2 bg-slate-900 border border-slate-800 rounded-xl p-5 shadow-lg flex flex-col justify-between">
          <div>
            <div className="flex items-center justify-between mb-4">
              <div>
                <h3 className="text-sm font-bold text-white">Monthly Prevented Loss Trend</h3>
                <p className="text-xs text-slate-400">Total fraud prevention volume in USD</p>
              </div>
              <span className="px-2.5 py-1 rounded bg-emerald-500/10 text-emerald-400 text-xs font-mono font-bold border border-emerald-500/20">
                +$1.45M Saved
              </span>
            </div>

            {/* Custom SVG / Bar Chart Graphic */}
            <div className="h-56 w-full flex items-end justify-between gap-3 pt-6 px-2 border-b border-slate-800 pb-2">
              {overviewData.monthlyFraudTrend.map((item, idx) => (
                <div key={idx} className="flex-1 flex flex-col items-center gap-2 h-full justify-end group">
                  <div className="text-[10px] font-mono text-slate-400 opacity-0 group-hover:opacity-100 transition-opacity">
                    ${(item.preventedLoss / 1000).toFixed(0)}k
                  </div>
                  <div
                    style={{ height: `${(item.preventedLoss / 350000) * 100}%` }}
                    className="w-full bg-gradient-to-t from-sky-600 to-indigo-500 rounded-t-md group-hover:from-sky-500 group-hover:to-indigo-400 transition-all shadow-md shadow-sky-500/10"
                  />
                  <span className="text-[11px] font-mono text-slate-400">{item.month}</span>
                </div>
              ))}
            </div>
          </div>

          <div className="mt-4 flex items-center justify-between text-xs text-slate-400">
            <span>Aggregated across 7 financial quarters</span>
            <span className="flex items-center gap-1 text-sky-400 font-mono">
              <ArrowPathIcon className="w-3.5 h-3.5" /> Updated 2 mins ago
            </span>
          </div>
        </div>

        {/* Recent Activities Timeline */}
        <div className="bg-slate-900 border border-slate-800 rounded-xl p-5 shadow-lg">
          <h3 className="text-sm font-bold text-white mb-4 flex items-center justify-between">
            <span>Agent Decision Audit Trail</span>
            <span className="text-xs font-mono text-slate-400">Live Stream</span>
          </h3>
          <ActivityTimeline activities={auditData.slice(0, 4) as any} />
        </div>
      </div>
    </div>
  );
};

export default DashboardPage;
