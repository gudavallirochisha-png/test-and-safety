import React, { useState } from 'react';
import PageHeader from '../components/common/PageHeader';
import DataTable, { Column } from '../components/data/DataTable';
import RiskBadge from '../components/common/RiskBadge';
import ConfidenceBadge from '../components/common/ConfidenceBadge';
import StatusChip from '../components/common/StatusChip';
import SearchBox from '../components/data/SearchBox';
import FilterPanel from '../components/data/FilterPanel';
import Modal from '../components/feedback/Modal';
import { useTrustStore } from '../store/useTrustStore';
import productsData from '../data/products.json';
import { ProductVerificationItem } from '../types';
import { CloudArrowUpIcon, EyeIcon, ShieldExclamationIcon } from '@heroicons/react/24/outline';

export const ProductVerificationPage: React.FC = () => {
  const [products] = useState<ProductVerificationItem[]>(productsData as any);
  const [search, setSearch] = useState('');
  const [filterRisk, setFilterRisk] = useState('all');
  const [selectedProduct, setSelectedProduct] = useState<ProductVerificationItem | null>(null);
  const { addToast } = useTrustStore();

  const handleSimulateScan = (e: React.FormEvent) => {
    e.preventDefault();
    addToast({
      type: 'success',
      title: 'YOLO v8 Visual Scan Complete',
      message: 'Product listing image evaluated against brand trademark vectors.',
    });
  };

  const filteredProducts = products.filter((item) => {
    const matchesSearch =
      item.productName.toLowerCase().includes(search.toLowerCase()) ||
      item.id.toLowerCase().includes(search.toLowerCase()) ||
      item.sellerName.toLowerCase().includes(search.toLowerCase());
    const matchesRisk = filterRisk === 'all' || item.riskLevel === filterRisk;
    return matchesSearch && matchesRisk;
  });

  const columns: Column<ProductVerificationItem>[] = [
    {
      header: 'Product',
      cell: (row) => (
        <div className="flex items-center gap-3">
          <img
            src={row.imageUrl}
            alt={row.productName}
            className="w-10 h-10 rounded-lg object-cover border border-slate-800"
          />
          <div>
            <div className="font-bold text-white text-xs">{row.productName}</div>
            <div className="text-[10px] font-mono text-slate-400">{row.id} • ${row.price.toFixed(2)}</div>
          </div>
        </div>
      ),
    },
    {
      header: 'Seller',
      cell: (row) => (
        <div>
          <div className="text-xs text-slate-200">{row.sellerName}</div>
          <div className="text-[10px] font-mono text-slate-400">{row.sellerId}</div>
        </div>
      ),
    },
    {
      header: 'Authenticity Score',
      cell: (row) => <ConfidenceBadge score={row.authenticityScore} label="YOLO" />,
    },
    {
      header: 'Risk Level',
      cell: (row) => <RiskBadge level={row.riskLevel} />,
    },
    {
      header: 'Status',
      cell: (row) => <StatusChip status={row.status} />,
    },
    {
      header: 'Actions',
      cell: (row) => (
        <button
          onClick={() => setSelectedProduct(row)}
          className="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-sky-400 transition-colors flex items-center gap-1 text-xs font-medium"
        >
          <EyeIcon className="w-4 h-4" /> Inspect
        </button>
      ),
    },
  ];

  return (
    <div className="space-y-6">
      <PageHeader
        title="Product Authenticity & Visual Verification"
        subtitle="YOLO v8 Object Detection & Trademark Logo Misalignment Inspection Engine"
        badge="COMPUTER VISION"
      />

      {/* Upload Product & Scan Form Split Card */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Upload Product Card */}
        <div className="lg:col-span-2 bg-slate-900 border border-slate-800 rounded-xl p-5 shadow-lg">
          <h3 className="text-sm font-bold text-white mb-4 flex items-center gap-2">
            <CloudArrowUpIcon className="w-5 h-5 text-sky-400" />
            Simulate Instant Image Authenticity Assessment
          </h3>
          <form onSubmit={handleSimulateScan} className="space-y-4">
            <div className="border-2 border-dashed border-slate-800 hover:border-sky-500/50 rounded-xl p-6 text-center cursor-pointer transition-colors bg-slate-950/40">
              <CloudArrowUpIcon className="w-10 h-10 text-slate-500 mx-auto mb-2" />
              <p className="text-xs font-semibold text-slate-300">Drop high-resolution product photos here</p>
              <p className="text-[10px] text-slate-500 mt-1">Supports PNG, JPG, WEBP (Max 15MB)</p>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
              <div>
                <label className="text-[11px] font-mono text-slate-400 block mb-1">Product Title</label>
                <input
                  type="text"
                  placeholder="e.g. Designer Leather Jacket"
                  defaultValue="Limited Edition Luxury Handbag"
                  className="w-full bg-slate-950 border border-slate-800 rounded-lg px-3 py-2 text-xs text-white focus:outline-none focus:border-sky-500"
                />
              </div>
              <div>
                <label className="text-[11px] font-mono text-slate-400 block mb-1">Declared Category</label>
                <input
                  type="text"
                  defaultValue="Fashion & Accessories"
                  className="w-full bg-slate-950 border border-slate-800 rounded-lg px-3 py-2 text-xs text-white focus:outline-none focus:border-sky-500"
                />
              </div>
            </div>

            <button
              type="submit"
              className="w-full py-2.5 rounded-lg bg-sky-500 hover:bg-sky-400 text-white font-semibold text-xs transition-colors shadow-lg shadow-sky-500/20"
            >
              Run YOLO Visual Verification Agent
            </button>
          </form>
        </div>

        {/* Quick Verification Stats Card */}
        <div className="bg-slate-900 border border-slate-800 rounded-xl p-5 shadow-lg flex flex-col justify-between">
          <div>
            <h3 className="text-sm font-bold text-white mb-2">Authenticity Model Overview</h3>
            <p className="text-xs text-slate-400 mb-4">Real-time object bounding box and logo comparison</p>
            <div className="space-y-3">
              <div className="p-3 rounded-lg bg-slate-950/60 border border-slate-800 flex justify-between items-center text-xs">
                <span className="text-slate-400">Total Scanned Today:</span>
                <span className="font-bold text-white font-mono">85,400</span>
              </div>
              <div className="p-3 rounded-lg bg-slate-950/60 border border-slate-800 flex justify-between items-center text-xs">
                <span className="text-slate-400">Counterfeit Detection Rate:</span>
                <span className="font-bold text-rose-400 font-mono">1.8%</span>
              </div>
            </div>
          </div>
          <div className="text-[11px] text-slate-400 border-t border-slate-800 pt-3">
            Active Neural Engine: <span className="font-mono text-sky-400">Ultralytics YOLO v8x-Vision</span>
          </div>
        </div>
      </div>

      {/* Filter and Search controls */}
      <div className="flex flex-col sm:flex-row items-center justify-between gap-4">
        <SearchBox value={search} onChange={setSearch} placeholder="Filter products by title, ID, or seller..." />
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

      {/* Product Table */}
      <DataTable
        columns={columns}
        data={filteredProducts}
        keyExtractor={(item) => item.id}
      />

      {/* Inspection Modal */}
      {selectedProduct && (
        <Modal
          isOpen={!!selectedProduct}
          onClose={() => setSelectedProduct(null)}
          title={`YOLO Inspection: ${selectedProduct.productName}`}
        >
          <div className="space-y-4">
            <div className="relative rounded-lg overflow-hidden border border-slate-800 max-h-64 flex justify-center bg-black">
              <img src={selectedProduct.imageUrl} alt={selectedProduct.productName} className="object-contain max-h-64" />
              {/* Simulated YOLO Bounding Box Overlay */}
              {selectedProduct.yoloDetections.length > 0 && (
                <div className="absolute inset-4 border-2 border-rose-500 bg-rose-500/10 rounded flex items-start justify-between p-2">
                  <span className="bg-rose-600 text-white text-[10px] font-mono px-1.5 py-0.5 rounded">
                    {selectedProduct.yoloDetections[0].label} ({Math.round(selectedProduct.yoloDetections[0].confidence * 100)}%)
                  </span>
                </div>
              )}
            </div>

            <div className="grid grid-cols-2 gap-3 text-xs font-mono">
              <div className="p-2.5 rounded bg-slate-950 border border-slate-800">
                <span className="text-slate-400 block text-[10px]">Authenticity Score</span>
                <span className="font-bold text-white text-sm">{selectedProduct.authenticityScore}%</span>
              </div>
              <div className="p-2.5 rounded bg-slate-950 border border-slate-800">
                <span className="text-slate-400 block text-[10px]">Risk Severity</span>
                <RiskBadge level={selectedProduct.riskLevel} />
              </div>
            </div>

            {selectedProduct.flaggedReasons.length > 0 && (
              <div className="p-3 rounded-lg bg-rose-950/20 border border-rose-900/30">
                <h4 className="text-xs font-bold text-rose-400 mb-1 flex items-center gap-1">
                  <ShieldExclamationIcon className="w-4 h-4" /> Flagged Violations
                </h4>
                <ul className="list-disc list-inside text-xs text-rose-300/80 space-y-1">
                  {selectedProduct.flaggedReasons.map((r, i) => (
                    <li key={i}>{r}</li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        </Modal>
      )}
    </div>
  );
};

export default ProductVerificationPage;
