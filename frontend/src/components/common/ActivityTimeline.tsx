import React from 'react';
import { AuditLogItem } from '../../types';
import StatusChip from './StatusChip';

interface ActivityTimelineProps {
  activities: AuditLogItem[];
}

export const ActivityTimeline: React.FC<ActivityTimelineProps> = ({ activities }) => {
  return (
    <div className="space-y-4">
      {activities.map((item, idx) => (
        <div key={item.id || idx} className="relative pl-6 pb-4 border-l border-slate-800 last:border-l-0 last:pb-0">
          <div className="absolute -left-1.5 top-1 w-3 h-3 rounded-full bg-sky-500 border-2 border-slate-900" />
          <div className="flex items-center justify-between gap-2 mb-1">
            <span className="text-xs font-bold text-white">{item.agentName}</span>
            <span className="text-[11px] font-mono text-slate-400">
              {new Date(item.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
            </span>
          </div>
          <p className="text-xs text-slate-300 mb-2">{item.details}</p>
          <div className="flex items-center gap-2">
            <StatusChip status={item.status} />
            <span className="text-[11px] text-slate-400 font-mono">Entity: {item.entityId}</span>
          </div>
        </div>
      ))}
    </div>
  );
};

export default ActivityTimeline;
