import React from 'react';
import { Link } from 'react-router-dom';
import { ShieldExclamationIcon, HomeIcon } from '@heroicons/react/24/outline';

export const NotFoundPage: React.FC = () => {
  return (
    <div className="min-h-[70vh] flex flex-col items-center justify-center text-center p-6">
      <div className="w-16 h-16 rounded-full bg-rose-500/10 text-rose-400 border border-rose-500/20 flex items-center justify-center mb-4">
        <ShieldExclamationIcon className="w-8 h-8" />
      </div>
      <h1 className="text-4xl font-extrabold text-white tracking-tight font-mono mb-2">404</h1>
      <h2 className="text-lg font-bold text-slate-200 mb-2">Page Not Found</h2>
      <p className="text-xs text-slate-400 max-w-md mb-6">
        The target route or security evaluation asset you requested does not exist or has been quarantined.
      </p>
      <Link
        to="/"
        className="inline-flex items-center gap-2 px-4 py-2 rounded-lg bg-sky-500 hover:bg-sky-400 text-white text-xs font-semibold shadow-lg shadow-sky-500/20 transition-all"
      >
        <HomeIcon className="w-4 h-4" /> Return to Command Center
      </Link>
    </div>
  );
};

export default NotFoundPage;
