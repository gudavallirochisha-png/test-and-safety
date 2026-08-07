import React, { useState } from 'react';
import PageHeader from '../components/common/PageHeader';
import DataTable, { Column } from '../components/data/DataTable';
import StatusChip from '../components/common/StatusChip';
import ConfidenceBadge from '../components/common/ConfidenceBadge';
import SearchBox from '../components/data/SearchBox';
import Pagination from '../components/data/Pagination';
import auditData from '../data/audit.json';
import { AuditLogItem } from '../types';

export const AuditLogsPage: React.FC = () => {
  const [auditLogs] = useState<AuditLogItem[]>(auditData as any);
  const [search, setSearch] = useState('');
  const [currentPage, setCurrentPage] = useState(1);
  const pageSize = 10;

  const filteredLogs = auditLogs.filter((item) => {
    return (
      item.agentName.toLowerCase().includes(search.toLowerCase()) ||
      item.action.toLowerCase().includes(search.toLowerCase()) ||
      item.entityId.toLowerCase().includes(search.toLowerCase()) ||
      item.details.toLowerCase().includes(search.toLowerCase())
    );
  });

  const columns: Column<AuditLogItem>[] = [
    {
      header: 'Timestamp',
      cell: (row) => (
        <span className="font-mono text-slate-300 text-xs">
          {new Date(row.timestamp).toLocaleString()}
        </span>
      ),
    },
    {
      header: 'Agent Subsystem',
      cell: (row) => (
        <div className="font-bold text-white text-xs">
          {row.agentName}
        </div>
      ),
    },
    {
      header: 'Action Taken',
      cell: (row) => (
        <span className="font-mono font-bold text-sky-400 text-xs px-2 py-0.5 rounded bg-sky-500/10 border border-sky-500/20">
          {row.action}
        </span>
      ),
    },
    {
      header: 'Target Entity',
      cell: (row) => (
        <span className="font-mono text-slate-300 text-xs">
          {row.entityType}: {row.entityId}
        </span>
      ),
    },
    {
      header: 'Execution Status',
      cell: (row) => <StatusChip status={row.status} />,
    },
    {
      header: 'Model Confidence',
      cell: (row) => <ConfidenceBadge score={row.confidenceScore} />,
    },
    {
      header: 'Decision Details',
      cell: (row) => (
        <span className="text-slate-400 text-xs truncate max-w-xs block">
          {row.details}
        </span>
      ),
    },
  ];

  return (
    <div className="space-y-6">
      <PageHeader
        title="Compliance & Agent Audit Trail"
        subtitle="Immutable ledger of automated agent decisions, model confidence scores, and action enforcement"
        badge="AUDIT LEDGER"
      />

      <div className="flex flex-col sm:flex-row items-center justify-between gap-4">
        <SearchBox value={search} onChange={setSearch} placeholder="Search audit logs by agent, action, entity ID..." />
      </div>

      <DataTable
        columns={columns}
        data={filteredLogs}
        keyExtractor={(item) => item.id}
      />

      <Pagination
        currentPage={currentPage}
        totalPages={1}
        totalItems={filteredLogs.length}
        pageSize={pageSize}
        onPageChange={setCurrentPage}
      />
    </div>
  );
};

export default AuditLogsPage;
