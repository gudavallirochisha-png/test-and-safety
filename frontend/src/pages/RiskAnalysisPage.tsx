import React, { useState } from 'react';
import PageHeader from '../components/common/PageHeader';
import DataTable, { Column } from '../components/data/DataTable';
import RiskBadge from '../components/common/RiskBadge';
import ConfidenceBadge from '../components/common/ConfidenceBadge';
import StatusChip from '../components/common/StatusChip';
import SearchBox from '../components/data/SearchBox';
import FilterPanel from '../components/data/FilterPanel';
import transactionsData from '../data/transactions.json';
import { TransactionRiskItem } from '../types';
import { useTrustStore } from '../store/useTrustStore';

import {
  ShoppingBagIcon,
  ShieldExclamationIcon,
  UserIcon,
  CpuChipIcon,
  CheckCircleIcon,
  XCircleIcon,
} from '@heroicons/react/24/outline';

export const RiskAnalysisPage: React.FC = () => {
  const [transactions] = useState<TransactionRiskItem[]>(transactionsData as any);
  const [selectedTxn, setSelectedTxn] = useState<TransactionRiskItem>(transactions[0]);
  const [search, setSearch] = useState('');
  const [filterRisk, setFilterRisk] = useState('all');
  const { addToast } = useTrustStore();

  const handleAction = (action: string) => {
    addToast({
      type: action === 'APPROVED' ? 'success' : 'error',
      title: `Order ${action}`,
      message: `Transaction ${selectedTxn.id} updated to ${action}.`,
    });
  };

  const filteredTransactions = transactions.filter((txn) => {
    const matchesSearch =
      txn.orderId.toLowerCase().includes(search.toLowerCase()) ||
      txn.customerName.toLowerCase().includes(search.toLowerCase()) ||
      txn.sellerName.toLowerCase().includes(search.toLowerCase()) ||
      txn.id.toLowerCase().includes(search.toLowerCase());
    const matchesRisk = filterRisk === 'all' || txn.riskLevel === filterRisk;
    return matchesSearch && matchesRisk;
  });

  const columns: Column<TransactionRiskItem>[] = [
    {
      header: 'Order ID',
      cell: (row) => (
        <div>
          <div className="font-bold text-white font-mono text-xs">{row.orderId}</div>
          <div className="text-[10px] text-slate-400 font-mono">{row.id}</div>
        </div>
      ),
    },
    {
      header: 'Customer',
      cell: (row) => (
        <div>
          <div className="text-xs text-slate-200">{row.customerName}</div>
          <div className="text-[10px] text-slate-400 font-mono">{row.location}</div>
        </div>
      ),
    },
    {
      header: 'Amount',
      cell: (row) => <span className="font-mono font-bold text-white text-xs">${row.amount.toFixed(2)}</span>,
    },
    {
      header: 'XGBoost Risk Score',
      cell: (row) => <ConfidenceBadge score={row.xgboostRiskScore} label="Risk" />,
    },
    {
      header: 'Severity',
      cell: (row) => <RiskBadge level={row.riskLevel} />,
    },
    {
      header: 'Status',
      cell: (row) => <StatusChip status={row.status} />,
    },
    {
      header: 'Action',
      cell: (row) => (
        <button
          onClick={() => setSelectedTxn(row)}
          className={`px-2.5 py-1 rounded text-xs font-semibold transition-colors ${
            selectedTxn.id === row.id
              ? 'bg-sky-500 text-white'
              : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
          }`}
        >
          Select
        </button>
      ),
    },
  ];

  return (
    <div className="space-y-6">
      <PageHeader
        title="Seller & Transaction Risk Analysis"
        subtitle="Gradient Boosted Decision Tree (XGBoost) feature evaluation for fraud detection"
        badge="XGBoost ENGINE"
      />

      {/* Selected Order Deep-Dive Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Risk Score Card & Prediction Panel */}
        <div className="bg-slate-900 border border-slate-800 rounded-xl p-5 shadow-lg space-y-4">
          <div className="flex items-center justify-between">
            <h3 className="text-sm font-bold text-white flex items-center gap-2">
              <CpuChipIcon className="w-5 h-5 text-sky-400" />
              XGBoost Evaluation Score
            </h3>
            <RiskBadge level={selectedTxn.riskLevel} />
          </div>

          <div className="text-center py-4 bg-slate-950/60 rounded-xl border border-slate-800/80">
            <div className="text-4xl font-extrabold font-mono tracking-tight text-rose-400">
              {selectedTxn.xgboostRiskScore} <span className="text-xs text-slate-500 font-sans">/ 100</span>
            </div>
            <div className="text-xs text-slate-400 mt-1">Recommended Action: <span className="font-bold text-white font-mono">{selectedTxn.recommendation}</span></div>
          </div>

          <div>
            <h4 className="text-xs font-bold text-slate-300 mb-2 flex items-center gap-1">
              <ShieldExclamationIcon className="w-4 h-4 text-amber-400" /> High-Weight Fraud Factors
            </h4>
            <div className="space-y-1.5">
              {selectedTxn.fraudFactors.length > 0 ? (
                selectedTxn.fraudFactors.map((factor, i) => (
                  <div key={i} className="text-xs text-slate-300 bg-slate-950 px-3 py-1.5 rounded border border-slate-800 font-mono">
                    • {factor}
                  </div>
                ))
              ) : (
                <div className="text-xs text-emerald-400 font-mono">No fraud factors detected</div>
              )}
            </div>
          </div>

          <div className="flex gap-2 pt-2 border-t border-slate-800">
            <button
              onClick={() => handleAction('APPROVED')}
              className="flex-1 py-2 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 text-xs font-semibold hover:bg-emerald-500/30 flex items-center justify-center gap-1"
            >
              <CheckCircleIcon className="w-4 h-4" /> Approve
            </button>
            <button
              onClick={() => handleAction('BLOCKED')}
              className="flex-1 py-2 rounded bg-rose-500/20 text-rose-300 border border-rose-500/30 text-xs font-semibold hover:bg-rose-500/30 flex items-center justify-center gap-1"
            >
              <XCircleIcon className="w-4 h-4" /> Reject Order
            </button>
          </div>
        </div>

        {/* Customer Information Panel */}
        <div className="bg-slate-900 border border-slate-800 rounded-xl p-5 shadow-lg space-y-3">
          <h3 className="text-sm font-bold text-white flex items-center gap-2 border-b border-slate-800 pb-3">
            <UserIcon className="w-5 h-5 text-sky-400" /> Customer Telemetry
          </h3>
          <div className="space-y-2 text-xs">
            <div className="flex justify-between py-1 border-b border-slate-800/60">
              <span className="text-slate-400">Name:</span>
              <span className="text-white font-semibold">{selectedTxn.customerName}</span>
            </div>
            <div className="flex justify-between py-1 border-b border-slate-800/60 font-mono">
              <span className="text-slate-400">Customer ID:</span>
              <span className="text-slate-300">{selectedTxn.customerId}</span>
            </div>
            <div className="flex justify-between py-1 border-b border-slate-800/60 font-mono">
              <span className="text-slate-400">IP Address:</span>
              <span className="text-sky-400">{selectedTxn.ipAddress}</span>
            </div>
            <div className="flex justify-between py-1 border-b border-slate-800/60 font-mono">
              <span className="text-slate-400">Device Fingerprint:</span>
              <span className="text-slate-300">{selectedTxn.deviceFingerprint}</span>
            </div>
            <div className="flex justify-between py-1 border-b border-slate-800/60">
              <span className="text-slate-400">Geolocation:</span>
              <span className="text-slate-200">{selectedTxn.location}</span>
            </div>
          </div>
        </div>

        {/* Order Details Panel */}
        <div className="bg-slate-900 border border-slate-800 rounded-xl p-5 shadow-lg space-y-3">
          <h3 className="text-sm font-bold text-white flex items-center gap-2 border-b border-slate-800 pb-3">
            <ShoppingBagIcon className="w-5 h-5 text-sky-400" /> Order & Gateway Context
          </h3>
          <div className="space-y-2 text-xs">
            <div className="flex justify-between py-1 border-b border-slate-800/60 font-mono">
              <span className="text-slate-400">Order Ref:</span>
              <span className="text-white font-bold">{selectedTxn.orderId}</span>
            </div>
            <div className="flex justify-between py-1 border-b border-slate-800/60">
              <span className="text-slate-400">Seller Name:</span>
              <span className="text-slate-200">{selectedTxn.sellerName}</span>
            </div>
            <div className="flex justify-between py-1 border-b border-slate-800/60">
              <span className="text-slate-400">Payment Gateway:</span>
              <span className="text-slate-200">{selectedTxn.paymentMethod}</span>
            </div>
            <div className="flex justify-between py-1 border-b border-slate-800/60">
              <span className="text-slate-400">Transaction Value:</span>
              <span className="text-emerald-400 font-bold font-mono">${selectedTxn.amount.toFixed(2)}</span>
            </div>
            <div className="flex justify-between py-1 border-b border-slate-800/60 font-mono">
              <span className="text-slate-400">Timestamp:</span>
              <span className="text-slate-400">{new Date(selectedTxn.timestamp).toLocaleString()}</span>
            </div>
          </div>
        </div>
      </div>

      {/* Transaction Table */}
      <div className="space-y-4">
        <div className="flex flex-col sm:flex-row items-center justify-between gap-4">
          <SearchBox value={search} onChange={setSearch} placeholder="Filter transactions by order, customer, seller..." />
          <FilterPanel
            activeValue={filterRisk}
            onChange={setFilterRisk}
            options={[
              { label: 'All Risks', value: 'all' },
              { label: 'Critical', value: 'critical' },
              { label: 'High', value: 'high' },
              { label: 'Medium', value: 'medium' },
              { label: 'Low', value: 'low' },
            ]}
          />
        </div>

        <DataTable
          columns={columns}
          data={filteredTransactions}
          keyExtractor={(item) => item.id}
        />
      </div>
    </div>
  );
};

export default RiskAnalysisPage;
