import React, { useState } from 'react';
import PageHeader from '../components/common/PageHeader';
import DataTable, { Column } from '../components/data/DataTable';
import RiskBadge from '../components/common/RiskBadge';
import ConfidenceBadge from '../components/common/ConfidenceBadge';
import StatusChip from '../components/common/StatusChip';
import SearchBox from '../components/data/SearchBox';
import FilterPanel from '../components/data/FilterPanel';
import reviewsData from '../data/reviews.json';
import { ReviewModerationItem } from '../types';
import { useTrustStore } from '../store/useTrustStore';

import {
  ChatBubbleBottomCenterTextIcon,
  StarIcon,
  UserCircleIcon,
  CheckIcon,
  XMarkIcon,
} from '@heroicons/react/24/outline';

export const ReviewModerationPage: React.FC = () => {
  const [reviews] = useState<ReviewModerationItem[]>(reviewsData as any);
  const [selectedReview, setSelectedReview] = useState<ReviewModerationItem>(reviews[0]);
  const [search, setSearch] = useState('');
  const [filterRisk, setFilterRisk] = useState('all');
  const { addToast } = useTrustStore();

  const handleAction = (status: string) => {
    addToast({
      type: status === 'PUBLISHED' ? 'success' : 'error',
      title: `Review ${status}`,
      message: `Review ${selectedReview.id} updated to ${status}.`,
    });
  };

  const filteredReviews = reviews.filter((rev) => {
    const matchesSearch =
      rev.productTitle.toLowerCase().includes(search.toLowerCase()) ||
      rev.reviewerName.toLowerCase().includes(search.toLowerCase()) ||
      rev.reviewText.toLowerCase().includes(search.toLowerCase());
    const matchesRisk = filterRisk === 'all' || rev.riskLevel === filterRisk;
    return matchesSearch && matchesRisk;
  });

  const columns: Column<ReviewModerationItem>[] = [
    {
      header: 'Product',
      cell: (row) => (
        <div>
          <div className="font-bold text-white text-xs">{row.productTitle}</div>
          <div className="text-[10px] text-slate-400 font-mono">{row.id}</div>
        </div>
      ),
    },
    {
      header: 'Reviewer',
      cell: (row) => (
        <div>
          <div className="text-xs text-slate-200 font-medium">{row.reviewerName}</div>
          <div className="text-[10px] text-slate-400 font-mono">{row.reviewerId}</div>
        </div>
      ),
    },
    {
      header: 'Rating',
      cell: (row) => (
        <div className="flex items-center gap-1 text-amber-400 font-mono font-bold text-xs">
          <StarIcon className="w-3.5 h-3.5 fill-amber-400" />
          {row.rating}.0
        </div>
      ),
    },
    {
      header: 'Toxicity Score',
      cell: (row) => <ConfidenceBadge score={row.distilBertToxicityScore} label="DistilBERT" />,
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
      header: 'Action',
      cell: (row) => (
        <button
          onClick={() => setSelectedReview(row)}
          className={`px-2.5 py-1 rounded text-xs font-semibold transition-colors ${
            selectedReview.id === row.id
              ? 'bg-sky-500 text-white'
              : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
          }`}
        >
          Inspect
        </button>
      ),
    },
  ];

  return (
    <div className="space-y-6">
      <PageHeader
        title="Review & Content Safety Moderation"
        subtitle="DistilBERT NLP Classification for spam URLs, toxicity score, and incentivized fake feedback"
        badge="DistilBERT NLP"
      />

      {/* Selected Review Details & Model Predictions Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Review Content Panel */}
        <div className="lg:col-span-2 bg-slate-900 border border-slate-800 rounded-xl p-5 shadow-lg space-y-4">
          <div className="flex items-center justify-between border-b border-slate-800 pb-3">
            <div>
              <h3 className="text-sm font-bold text-white">{selectedReview.productTitle}</h3>
              <p className="text-xs text-slate-400 font-mono">Review Ref: {selectedReview.id}</p>
            </div>
            <RiskBadge level={selectedReview.riskLevel} />
          </div>

          {/* Text Box */}
          <div className="p-4 rounded-lg bg-slate-950 border border-slate-800 text-xs text-slate-200 leading-relaxed font-mono">
            "{selectedReview.reviewText}"
          </div>

          {/* Flagged Categories */}
          {selectedReview.flaggedCategories.length > 0 && (
            <div>
              <span className="text-[11px] text-slate-400 font-mono uppercase block mb-1.5">DistilBERT Flagged Categories:</span>
              <div className="flex flex-wrap gap-1.5">
                {selectedReview.flaggedCategories.map((cat, i) => (
                  <span key={i} className="px-2 py-0.5 rounded text-[11px] font-mono bg-rose-500/10 text-rose-400 border border-rose-500/20">
                    {cat}
                  </span>
                ))}
              </div>
            </div>
          )}

          <div className="flex gap-2 pt-2 border-t border-slate-800">
            <button
              onClick={() => handleAction('PUBLISHED')}
              className="px-4 py-2 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 text-xs font-semibold hover:bg-emerald-500/30 flex items-center gap-1"
            >
              <CheckIcon className="w-4 h-4" /> Publish Review
            </button>
            <button
              onClick={() => handleAction('REJECTED')}
              className="px-4 py-2 rounded bg-rose-500/20 text-rose-300 border border-rose-500/30 text-xs font-semibold hover:bg-rose-500/30 flex items-center gap-1"
            >
              <XMarkIcon className="w-4 h-4" /> Purge & Block
            </button>
          </div>
        </div>

        {/* DistilBERT Prediction Card & Reviewer History */}
        <div className="space-y-4">
          {/* Prediction Metrics */}
          <div className="bg-slate-900 border border-slate-800 rounded-xl p-5 shadow-lg space-y-3">
            <h3 className="text-sm font-bold text-white flex items-center gap-2 border-b border-slate-800 pb-2">
              <ChatBubbleBottomCenterTextIcon className="w-5 h-5 text-sky-400" /> Model Intelligence
            </h3>
            <div className="space-y-2 text-xs font-mono">
              <div className="flex justify-between py-1 border-b border-slate-800/60">
                <span className="text-slate-400">Toxicity Score:</span>
                <span className="font-bold text-rose-400">{selectedReview.distilBertToxicityScore}%</span>
              </div>
              <div className="flex justify-between py-1 border-b border-slate-800/60">
                <span className="text-slate-400">Sentiment Score:</span>
                <span className="font-bold text-sky-400">{selectedReview.distilBertSentimentScore}</span>
              </div>
              <div className="flex justify-between py-1 border-b border-slate-800/60">
                <span className="text-slate-400">Fake Probability:</span>
                <span className="font-bold text-amber-400">{selectedReview.isFakeReviewProb}%</span>
              </div>
            </div>
          </div>

          {/* Reviewer History Card */}
          <div className="bg-slate-900 border border-slate-800 rounded-xl p-5 shadow-lg space-y-3">
            <h3 className="text-sm font-bold text-white flex items-center gap-2 border-b border-slate-800 pb-2">
              <UserCircleIcon className="w-5 h-5 text-sky-400" /> Reviewer Metadata
            </h3>
            <div className="space-y-2 text-xs">
              <div className="flex justify-between py-1 border-b border-slate-800/60">
                <span className="text-slate-400">Name:</span>
                <span className="text-white font-semibold">{selectedReview.reviewerName}</span>
              </div>
              <div className="flex justify-between py-1 border-b border-slate-800/60 font-mono">
                <span className="text-slate-400">Account Age:</span>
                <span className="text-slate-300">{selectedReview.reviewerHistoryStats.accountAgeDays} days</span>
              </div>
              <div className="flex justify-between py-1 border-b border-slate-800/60 font-mono">
                <span className="text-slate-400">Total Reviews:</span>
                <span className="text-slate-300">{selectedReview.reviewerHistoryStats.totalReviews}</span>
              </div>
              <div className="flex justify-between py-1 border-b border-slate-800/60 font-mono">
                <span className="text-slate-400">Flagged Ratio:</span>
                <span className="text-rose-400 font-bold">{(selectedReview.reviewerHistoryStats.flaggedRatio * 100).toFixed(0)}%</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Review Table */}
      <div className="space-y-4">
        <div className="flex flex-col sm:flex-row items-center justify-between gap-4">
          <SearchBox value={search} onChange={setSearch} placeholder="Filter reviews by product title or reviewer..." />
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
          data={filteredReviews}
          keyExtractor={(item) => item.id}
        />
      </div>
    </div>
  );
};

export default ReviewModerationPage;
