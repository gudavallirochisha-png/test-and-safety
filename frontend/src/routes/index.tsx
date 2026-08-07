import React from 'react';
import { createBrowserRouter, RouterProvider, Navigate } from 'react-router-dom';
import AppLayout from '../components/layout/AppLayout';

import DashboardPage from '../pages/DashboardPage';
import ProductVerificationPage from '../pages/ProductVerificationPage';
import RiskAnalysisPage from '../pages/RiskAnalysisPage';
import ReviewModerationPage from '../pages/ReviewModerationPage';
import FraudAlertsPage from '../pages/FraudAlertsPage';
import AuditLogsPage from '../pages/AuditLogsPage';
import AnalyticsPage from '../pages/AnalyticsPage';
import SettingsPage from '../pages/SettingsPage';
import NotFoundPage from '../pages/NotFoundPage';

const router = createBrowserRouter([
  {
    path: '/',
    element: <AppLayout />,
    children: [
      {
        index: true,
        element: <DashboardPage />,
      },
      {
        path: 'products',
        element: <ProductVerificationPage />,
      },
      {
        path: 'orders',
        element: <RiskAnalysisPage />,
      },
      {
        path: 'reviews',
        element: <ReviewModerationPage />,
      },
      {
        path: 'alerts',
        element: <FraudAlertsPage />,
      },
      {
        path: 'audit',
        element: <AuditLogsPage />,
      },
      {
        path: 'analytics',
        element: <AnalyticsPage />,
      },
      {
        path: 'settings',
        element: <SettingsPage />,
      },
      {
        path: 'not-found',
        element: <NotFoundPage />,
      },
      {
        path: '*',
        element: <Navigate to="/not-found" replace />,
      },
    ],
  },
]);

export const AppRoutes: React.FC = () => {
  return <RouterProvider router={router} />;
};

export default AppRoutes;
