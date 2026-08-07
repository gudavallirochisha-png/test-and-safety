import React from 'react';

export interface Column<T> {
  header: string;
  accessorKey?: keyof T;
  cell?: (row: T) => React.ReactNode;
  className?: string;
}

interface DataTableProps<T> {
  columns: Column<T>[];
  data: T[];
  keyExtractor: (item: T) => string;
  emptyMessage?: string;
}

export function DataTable<T>({
  columns,
  data,
  keyExtractor,
  emptyMessage = 'No records found matching criteria.',
}: DataTableProps<T>) {
  return (
    <div className="w-full overflow-x-auto rounded-xl border border-slate-800 bg-slate-900/80 shadow-md backdrop-blur-sm">
      <table className="w-full text-left text-xs border-collapse">
        <thead className="bg-slate-950/80 text-slate-400 uppercase tracking-wider font-mono text-[11px] border-b border-slate-800">
          <tr>
            {columns.map((col, idx) => (
              <th key={idx} className={`px-4 py-3.5 font-semibold ${col.className || ''}`}>
                {col.header}
              </th>
            ))}
          </tr>
        </thead>
        <tbody className="divide-y divide-slate-800/60 text-slate-300">
          {data.length === 0 ? (
            <tr>
              <td colSpan={columns.length} className="px-4 py-8 text-center text-slate-400 text-sm">
                {emptyMessage}
              </td>
            </tr>
          ) : (
            data.map((row) => (
              <tr key={keyExtractor(row)} className="hover:bg-slate-800/40 transition-colors">
                {columns.map((col, idx) => (
                  <td key={idx} className={`px-4 py-3.5 align-middle ${col.className || ''}`}>
                    {col.cell ? col.cell(row) : col.accessorKey ? String(row[col.accessorKey] ?? '') : null}
                  </td>
                ))}
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
}

export default DataTable;
