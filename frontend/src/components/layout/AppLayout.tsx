import React from 'react';
import { Outlet } from 'react-router-dom';
import Sidebar from './Sidebar';
import TopNav from './TopNav';
import Breadcrumb from './Breadcrumb';
import Footer from './Footer';
import NotificationPanel from './NotificationPanel';
import ToastComponent from '../feedback/ToastComponent';
import { useTrustStore } from '../../store/useTrustStore';

export const AppLayout: React.FC = () => {
  const { sidebarOpen } = useTrustStore();

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col font-sans antialiased">
      <Sidebar />
      
      <div className={`flex-1 flex flex-col transition-all duration-300 ${sidebarOpen ? 'pl-64' : 'pl-20'}`}>
        <TopNav />
        
        <main className="flex-1 p-4 sm:p-6 md:p-8 max-w-7xl w-full mx-auto">
          <Breadcrumb />
          <Outlet />
          <Footer />
        </main>
      </div>

      <NotificationPanel />
      <ToastComponent />
    </div>
  );
};

export default AppLayout;
