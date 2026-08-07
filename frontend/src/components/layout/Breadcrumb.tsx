import React from 'react';
import { useLocation, Link } from 'react-router-dom';
import { ChevronRightIcon, HomeIcon } from '@heroicons/react/24/outline';

export const Breadcrumb: React.FC = () => {
  const location = useLocation();
  const pathnames = location.pathname.split('/').filter((x) => x);

  const routeNameMap: Record<string, string> = {
    products: 'Product Verification',
    orders: 'Order Risk Analysis',
    reviews: 'Review Moderation',
    alerts: 'Fraud Alerts',
    audit: 'Audit Logs',
    analytics: 'Analytics',
    settings: 'Settings',
    'not-found': '404 Page',
  };

  return (
    <nav className="flex items-center space-x-2 text-xs text-slate-400 mb-4 font-medium">
      <Link to="/" className="flex items-center gap-1 hover:text-slate-200 transition-colors">
        <HomeIcon className="w-3.5 h-3.5" />
        <span>Home</span>
      </Link>
      {pathnames.map((name, index) => {
        const routeTo = `/${pathnames.slice(0, index + 1).join('/')}`;
        const isLast = index === pathnames.length - 1;
        const displayName = routeNameMap[name] || name;

        return (
          <React.Fragment key={routeTo}>
            <ChevronRightIcon className="w-3 h-3 text-slate-600 shrink-0" />
            {isLast ? (
              <span className="text-sky-400 font-semibold">{displayName}</span>
            ) : (
              <Link to={routeTo} className="hover:text-slate-200 transition-colors">
                {displayName}
              </Link>
            )}
          </React.Fragment>
        );
      })}
    </nav>
  );
};

export default Breadcrumb;
