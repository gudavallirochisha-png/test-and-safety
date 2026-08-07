import React from 'react';

interface LoadingSkeletonProps {
  rows?: number;
  height?: string;
  className?: string;
}

export const LoadingSkeleton: React.FC<LoadingSkeletonProps> = ({
  rows = 4,
  height = 'h-12',
  className = '',
}) => {
  return (
    <div className={`space-y-3 animate-pulse ${className}`}>
      {Array.from({ length: rows }).map((_, idx) => (
        <div key={idx} className={`w-full bg-slate-800/60 rounded-lg ${height}`} />
      ))}
    </div>
  );
};

export default LoadingSkeleton;
