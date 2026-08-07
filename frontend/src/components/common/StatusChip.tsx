import React from 'react';

interface StatusChipProps {
  status: string;
}

export const StatusChip: React.FC<StatusChipProps> = ({ status }) => {
  const getStyle = (val: string) => {
    const formatted = val.toUpperCase();
    switch (formatted) {
      case 'APPROVED':
      case 'VERIFIED':
      case 'PUBLISHED':
      case 'PASSED':
        return 'bg-emerald-500/10 text-emerald-400 border-emerald-500/30';
      case 'BLOCKED':
      case 'REJECTED':
      case 'COUNTERFEIT_FLAGGED':
      case 'QUARANTINED':
        return 'bg-rose-500/10 text-rose-400 border-rose-500/30';
      case 'FLAGGED_FOR_REVIEW':
      case 'MANUAL_REVIEW':
      case 'PENDING_MODERATION':
      case 'FLAGGED':
      case 'ESCALATED':
        return 'bg-amber-500/10 text-amber-400 border-amber-500/30';
      default:
        return 'bg-slate-800 text-slate-300 border-slate-700';
    }
  };

  return (
    <span
      className={`inline-flex items-center px-2 py-0.5 rounded text-[11px] font-mono font-medium tracking-wide border ${getStyle(
        status
      )}`}
    >
      {status.replace(/_/g, ' ')}
    </span>
  );
};

export default StatusChip;
