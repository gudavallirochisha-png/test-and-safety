import React from 'react';
import { AgentHealth } from '../../types';

interface AgentStatusCardProps {
  agent: AgentHealth;
}

export const AgentStatusCard: React.FC<AgentStatusCardProps> = ({ agent }) => {
  const getBadge = (status: string) => {
    switch (status) {
      case 'operational':
        return 'bg-emerald-500/10 text-emerald-400 border-emerald-500/30';
      case 'degraded':
        return 'bg-amber-500/10 text-amber-400 border-amber-500/30';
      default:
        return 'bg-rose-500/10 text-rose-400 border-rose-500/30';
    }
  };

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-xl p-5 shadow-md flex flex-col justify-between hover:border-slate-700 transition-colors">
      <div>
        <div className="flex items-center justify-between mb-3">
          <div className="flex items-center gap-2">
            <div className="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse" />
            <h3 className="text-base font-bold text-white">{agent.name}</h3>
          </div>
          <span className={`px-2 py-0.5 rounded text-[11px] font-mono border uppercase ${getBadge(agent.status)}`}>
            {agent.status}
          </span>
        </div>

        <div className="text-xs text-slate-400 font-mono mb-4 flex items-center justify-between border-b border-slate-800/80 pb-2">
          <span>Engine: <span className="text-slate-200">{agent.modelEngine}</span></span>
          <span>Version: <span className="text-slate-300">{agent.version}</span></span>
        </div>

        <div className="grid grid-cols-3 gap-2 text-center bg-slate-950/60 rounded-lg p-2.5 border border-slate-800/60">
          <div>
            <div className="text-[10px] text-slate-400 uppercase">Accuracy</div>
            <div className="text-sm font-bold text-emerald-400">{agent.accuracyPercentage}%</div>
          </div>
          <div>
            <div className="text-[10px] text-slate-400 uppercase">Latency</div>
            <div className="text-sm font-bold text-sky-400">{agent.avgLatencyMs}ms</div>
          </div>
          <div>
            <div className="text-[10px] text-slate-400 uppercase">24h Eval</div>
            <div className="text-sm font-bold text-slate-200">{(agent.processed24h / 1000).toFixed(0)}k</div>
          </div>
        </div>
      </div>

      <div className="mt-4 pt-2 text-[11px] text-slate-400 flex items-center justify-between">
        <span>Last Trained:</span>
        <span className="font-mono text-slate-300">{agent.lastTrained}</span>
      </div>
    </div>
  );
};

export default AgentStatusCard;
