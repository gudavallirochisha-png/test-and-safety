import React from 'react';
import { InboxIcon } from '@heroicons/react/24/outline';

interface EmptyStateProps {
  title?: string;
  description?: string;
  action?: React.ReactNode;
}

export const EmptyState: React.FC<EmptyStateProps> = ({
  title = 'No Data Available',
  description = 'There are no active records matching your current filter settings.',
  action,
}) => {
  return (
    <div className="flex flex-col items-center justify-center p-12 text-center bg-slate-900/60 border border-slate-800/80 rounded-xl">
      <div className="w-12 h-12 rounded-full bg-slate-800 flex items-center justify-center text-slate-400 mb-4">
        <InboxIcon className="w-6 h-6" />
      </div>
      <h3 className="text-base font-bold text-white mb-1">{title}</h3>
      <p className="text-xs text-slate-400 max-w-sm mb-6">{description}</p>
      {action}
    </div>
  );
};

export default EmptyState;
