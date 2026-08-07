import React from 'react';
import { MagnifyingGlassIcon, XMarkIcon } from '@heroicons/react/24/outline';

interface SearchBoxProps {
  value: string;
  onChange: (value: string) => void;
  placeholder?: string;
  className?: string;
}

export const SearchBox: React.FC<SearchBoxProps> = ({
  value,
  onChange,
  placeholder = 'Search by ID, keyword, or seller...',
  className = '',
}) => {
  return (
    <div className={`relative flex items-center ${className}`}>
      <MagnifyingGlassIcon className="w-4 h-4 absolute left-3 text-slate-400 pointer-events-none" />
      <input
        type="text"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder={placeholder}
        className="w-full bg-slate-900 border border-slate-800 rounded-lg pl-9 pr-8 py-2 text-xs text-slate-100 placeholder-slate-500 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500 transition-colors"
      />
      {value && (
        <button
          onClick={() => onChange('')}
          className="absolute right-2.5 text-slate-400 hover:text-white p-0.5 rounded"
        >
          <XMarkIcon className="w-4 h-4" />
        </button>
      )}
    </div>
  );
};

export default SearchBox;
