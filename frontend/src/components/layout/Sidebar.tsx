import React from 'react';
import { NavLink } from 'react-router-dom';
import { useTrustStore } from '../../store/useTrustStore';
import {
  HomeIcon,
  ShieldCheckIcon,
  ShoppingBagIcon,
  ChatBubbleBottomCenterTextIcon,
  BellAlertIcon,
  ChartBarIcon,
  ClipboardDocumentCheckIcon,
  Cog6ToothIcon,
  ChevronLeftIcon,
  ChevronRightIcon,
  ShieldExclamationIcon,
} from '@heroicons/react/24/outline';

export const Sidebar: React.FC = () => {
  const { sidebarOpen, toggleSidebar, alerts } = useTrustStore();
  const unresolvedAlertsCount = alerts.filter((a) => !a.isResolved).length;

  const navigation = [
    { name: 'Dashboard', path: '/', icon: HomeIcon },
    { name: 'Products', path: '/products', icon: ShieldCheckIcon },
    { name: 'Orders Risk', path: '/orders', icon: ShoppingBagIcon },
    { name: 'Reviews', path: '/reviews', icon: ChatBubbleBottomCenterTextIcon },
    { name: 'Fraud Alerts', path: '/alerts', icon: BellAlertIcon, badge: unresolvedAlertsCount },
    { name: 'Analytics', path: '/analytics', icon: ChartBarIcon },
    { name: 'Audit Logs', path: '/audit', icon: ClipboardDocumentCheckIcon },
    { name: 'Settings', path: '/settings', icon: Cog6ToothIcon },
  ];

  return (
    <aside
      className={`fixed left-0 top-0 bottom-0 z-40 bg-slate-900 border-r border-slate-800 transition-all duration-300 flex flex-col justify-between ${
        sidebarOpen ? 'w-64' : 'w-20'
      }`}
    >
      <div>
        {/* Brand Header */}
        <div className="h-16 flex items-center justify-between px-4 border-b border-slate-800">
          <div className="flex items-center gap-3 overflow-hidden">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-sky-500 to-indigo-600 flex items-center justify-center text-white font-bold shadow-lg shadow-sky-500/20 shrink-0">
              <ShieldExclamationIcon className="w-6 h-6" />
            </div>
            {sidebarOpen && (
              <div className="truncate">
                <h1 className="text-sm font-bold text-white tracking-wide">Aegis Trust & Safety</h1>
                <p className="text-[10px] font-mono text-sky-400 uppercase tracking-widest">Enterprise v1.0</p>
              </div>
            )}
          </div>
          <button
            onClick={toggleSidebar}
            className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors hidden sm:flex"
          >
            {sidebarOpen ? <ChevronLeftIcon className="w-4 h-4" /> : <ChevronRightIcon className="w-4 h-4" />}
          </button>
        </div>

        {/* Navigation Menu */}
        <nav className="p-3 space-y-1">
          {navigation.map((item) => (
            <NavLink
              key={item.path}
              to={item.path}
              className={({ isActive }) =>
                `flex items-center justify-between px-3 py-2.5 rounded-lg text-xs font-semibold transition-all ${
                  isActive
                    ? 'bg-sky-500/15 text-sky-400 border border-sky-500/30 shadow-sm'
                    : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/60'
                }`
              }
            >
              <div className="flex items-center gap-3 min-w-0">
                <item.icon className="w-5 h-5 shrink-0" />
                {sidebarOpen && <span className="truncate">{item.name}</span>}
              </div>
              {sidebarOpen && item.badge ? (
                <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-rose-500/20 text-rose-400 border border-rose-500/30">
                  {item.badge}
                </span>
              ) : null}
            </NavLink>
          ))}
        </nav>
      </div>

      {/* Footer Profile Pill */}
      {sidebarOpen && (
        <div className="p-4 border-t border-slate-800/80 bg-slate-950/40">
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 rounded-full bg-slate-800 border border-slate-700 flex items-center justify-center text-sky-400 font-bold text-xs">
              TS
            </div>
            <div className="truncate">
              <div className="text-xs font-bold text-slate-200">Trust Operations</div>
              <div className="text-[10px] text-slate-400">Principal Engineer</div>
            </div>
          </div>
        </div>
      )}
    </aside>
  );
};

export default Sidebar;
