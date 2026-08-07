import React from 'react';

interface ConfidenceBadgeProps {
  score: number; // 0 to 100
  label?: string;
}

export const ConfidenceBadge: React.FC<ConfidenceBadgeProps> = ({ score, label }) => {
  let colorClass = 'text-emerald-400 bg-emerald-500/10 border-emerald-500/20';
  if (score < 50) {
    colorClass = 'text-rose-400 bg-rose-500/10 border-rose-500/20';
  } else if (score < 80) {
    colorClass = 'text-amber-400 bg-amber-500/10 border-amber-500/20';
  }

  return (
    <span className={`inline-flex items-center gap-1 px-2 py-0.5 rounded text-xs font-mono border ${colorClass}`}>
      {label && <span className="text-slate-400 font-sans">{label}:</span>}
      <span className="font-bold">{score.toFixed(1)}%</span>
    </span>
  );
};

export default ConfidenceBadge;
