import React from 'react';

interface FilterOption {
  label: string;
  value: string;
}

interface FilterPanelProps {
  activeValue: string;
  onChange: (value: string) => void;
  options: FilterOption[];
  label?: string;
}

export const FilterPanel: React.FC<FilterPanelProps> = ({ activeValue, onChange, options, label }) => {
  return (
    <div className="flex items-center gap-2">
      {label && <span className="text-xs text-slate-400 font-medium">{label}:</span>}
      <div className="inline-flex bg-slate-900 border border-slate-800 p-1 rounded-lg gap-1">
        {options.map((opt) => (
          <button
            key={opt.value}
            onClick={() => onChange(opt.value)}
            className={`px-3 py-1 rounded-md text-xs font-medium transition-all ${
              activeValue === opt.value
                ? 'bg-sky-500/20 text-sky-400 border border-sky-500/30 shadow-sm'
                : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/60'
            }`}
          >
            {opt.label}
          </button>
        ))}
      </div>
    </div>
  );
};

export default FilterPanel;
