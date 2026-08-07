import React from 'react';
import { useTrustStore } from '../../store/useTrustStore';
import { BellIcon, Bars3Icon, ShieldCheckIcon } from '@heroicons/react/24/outline';
import SearchBox from '../data/SearchBox';

export const TopNav: React.FC = () => {
  const { toggleSidebar, toggleNotificationPanel, searchQuery, setSearchQuery, alerts } = useTrustStore();
  const unresolvedAlertsCount = alerts.filter((a) => !a.isResolved).length;

  return (
    <header className="h-16 bg-slate-900/90 border-b border-slate-800 backdrop-blur-md sticky top-0 z-30 px-4 sm:px-6 flex items-center justify-between gap-4">
      <div className="flex items-center gap-3">
        <button
          onClick={toggleSidebar}
          className="p-2 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors sm:hidden"
        >
          <Bars3Icon className="w-5 h-5" />
        </button>

        <div className="w-64 sm:w-80">
          <SearchBox
            value={searchQuery}
            onChange={setSearchQuery}
            placeholder="Search products, orders, reviews, or sellers..."
          />
        </div>
      </div>

      <div className="flex items-center gap-4">
        {/* System Agent Status Pill */}
        <div className="hidden md:flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-xs font-mono">
          <ShieldCheckIcon className="w-4 h-4" />
          <span>3 Agents Online</span>
          <span className="w-2 h-2 rounded-full bg-emerald-400 animate-ping" />
        </div>

        {/* Notifications Drawer Trigger */}
        <button
          onClick={toggleNotificationPanel}
          className="relative p-2 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
        >
          <BellIcon className="w-5 h-5" />
          {unresolvedAlertsCount > 0 && (
            <span className="absolute top-1.5 right-1.5 w-2.5 h-2.5 rounded-full bg-rose-500 ring-4 ring-slate-900" />
          )}
        </button>
      </div>
    </header>
  );
};

export default TopNav;
