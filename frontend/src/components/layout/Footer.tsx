import React from 'react';

export const Footer: React.FC = () => {
  return (
    <footer className="mt-12 py-6 border-t border-slate-800/80 text-center text-xs text-slate-500 flex flex-col sm:flex-row items-center justify-between gap-3">
      <div>
        © 2026 Enterprise Trust & Safety Platform. Engineered for Marketplace Security.
      </div>
      <div className="flex items-center gap-4 font-mono text-[11px]">
        <span className="flex items-center gap-1.5">
          <span className="w-2 h-2 rounded-full bg-emerald-400" />
          FastAPI Gateway: 24ms
        </span>
        <span>•</span>
        <span>XGBoost / DistilBERT / YOLO</span>
      </div>
    </footer>
  );
};

export default Footer;
