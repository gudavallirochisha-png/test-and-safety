import React from 'react';
import { ExclamationCircleIcon } from '@heroicons/react/24/outline';

interface ErrorStateProps {
  title?: string;
  message?: string;
  onRetry?: () => void;
}

export const ErrorState: React.FC<ErrorStateProps> = ({
  title = 'Evaluation Pipeline Error',
  message = 'An unexpected issue occurred while querying AI agent services.',
  onRetry,
}) => {
  return (
    <div className="flex flex-col items-center justify-center p-8 text-center bg-rose-950/20 border border-rose-900/30 rounded-xl">
      <div className="w-12 h-12 rounded-full bg-rose-900/30 flex items-center justify-center text-rose-400 mb-4 border border-rose-500/20">
        <ExclamationCircleIcon className="w-6 h-6" />
      </div>
      <h3 className="text-base font-bold text-white mb-1">{title}</h3>
      <p className="text-xs text-rose-300/80 max-w-sm mb-4">{message}</p>
      {onRetry && (
        <button
          onClick={onRetry}
          className="px-4 py-2 rounded-lg bg-rose-500/20 text-rose-300 border border-rose-500/30 text-xs font-semibold hover:bg-rose-500/30 transition-colors"
        >
          Retry Connection
        </button>
      )}
    </div>
  );
};

export default ErrorState;
