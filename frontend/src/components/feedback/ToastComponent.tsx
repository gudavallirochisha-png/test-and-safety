import React from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useTrustStore } from '../../store/useTrustStore';
import { XMarkIcon, CheckCircleIcon, ExclamationTriangleIcon, InformationCircleIcon } from '@heroicons/react/24/outline';

export const ToastComponent: React.FC = () => {
  const { toasts, removeToast } = useTrustStore();

  const getIcon = (type: string) => {
    switch (type) {
      case 'success':
        return <CheckCircleIcon className="w-5 h-5 text-emerald-400" />;
      case 'error':
        return <ExclamationTriangleIcon className="w-5 h-5 text-rose-400" />;
      case 'warning':
        return <ExclamationTriangleIcon className="w-5 h-5 text-amber-400" />;
      default:
        return <InformationCircleIcon className="w-5 h-5 text-sky-400" />;
    }
  };

  return (
    <div className="fixed bottom-5 right-5 z-50 flex flex-col gap-2 max-w-sm w-full pointer-events-none">
      <AnimatePresence>
        {toasts.map((toast) => (
          <motion.div
            key={toast.id}
            initial={{ opacity: 0, y: 20, scale: 0.95 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, scale: 0.95, x: 20 }}
            className="pointer-events-auto bg-slate-900 border border-slate-800 rounded-xl p-4 shadow-xl flex items-start gap-3"
          >
            <div className="mt-0.5">{getIcon(toast.type)}</div>
            <div className="flex-1">
              <h4 className="text-xs font-bold text-white">{toast.title}</h4>
              <p className="text-xs text-slate-400 mt-0.5">{toast.message}</p>
            </div>
            <button
              onClick={() => removeToast(toast.id)}
              className="text-slate-400 hover:text-white p-0.5 rounded"
            >
              <XMarkIcon className="w-4 h-4" />
            </button>
          </motion.div>
        ))}
      </AnimatePresence>
    </div>
  );
};

export default ToastComponent;
