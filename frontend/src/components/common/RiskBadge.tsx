import React from 'react';
import { RiskLevel } from '../../types';

interface RiskBadgeProps {
  level: RiskLevel;
  showDot?: boolean;
  className?: string;
}

export const RiskBadge: React.FC<RiskBadgeProps> = ({ level, showDot = true, className = '' }) => {
  const styles: Record<RiskLevel, { bg: string; text: string; border: string; dot: string; label: string }> = {
    low: {
      bg: 'bg-emerald-500/10',
      text: 'text-emerald-400',
      border: 'border-emerald-500/20',
      dot: 'bg-emerald-400',
      label: 'Low Risk',
    },
    medium: {
      bg: 'bg-amber-500/10',
      text: 'text-amber-400',
      border: 'border-amber-500/20',
      dot: 'bg-amber-400',
      label: 'Medium Risk',
    },
    high: {
      bg: 'bg-orange-500/10',
      text: 'text-orange-400',
      border: 'border-orange-500/20',
      dot: 'bg-orange-400',
      label: 'High Risk',
    },
    critical: {
      bg: 'bg-rose-500/10',
      text: 'text-rose-400',
      border: 'border-rose-500/30',
      dot: 'bg-rose-500 animate-pulse',
      label: 'Critical Alert',
    },
  };

  const current = styles[level] || styles.low;

  return (
    <span
      className={`inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-xs font-semibold border ${current.bg} ${current.text} ${current.border} ${className}`}
    >
      {showDot && <span className={`w-1.5 h-1.5 rounded-full ${current.dot}`} />}
      {current.label}
    </span>
  );
};

export default RiskBadge;
