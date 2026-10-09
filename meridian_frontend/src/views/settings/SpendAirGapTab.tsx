import React from 'react';
import GlowCard from '../../components/ui/GlowCard';
import HoloButton from '../../components/ui/HoloButton';

export interface SpendAirGapTabProps {
  airgapStatus: {
    airgap_active: boolean;
    proof_badge?: string;
    verified_at?: string;
    signature?: string;
  };
  handleToggleAirgap: (active: boolean) => void;
  budgetEnabled: boolean;
  handleToggleBudgetEnabled: (enabled: boolean) => void;
  newBudgetCap: string;
  setNewBudgetCap: (v: string) => void;
  handleUpdateBudgetCap: () => void;
  spendStats: {
    monthly_cost_usd?: number;
    budget_cap_usd?: number;
    budget_exceeded?: boolean;
    budget_enabled?: boolean;
  };
}

export default function SpendAirGapTab({
  airgapStatus,
  handleToggleAirgap,
  budgetEnabled,
  handleToggleBudgetEnabled,
  newBudgetCap,
  setNewBudgetCap,
  handleUpdateBudgetCap,
  spendStats,
}: SpendAirGapTabProps) {
  return (
    <>
      {/* Air-Gap Mode */}
      <GlowCard className="glass" style={{ padding: 16 }}>
        <div className="section-label">🔒 Air-Gap Mode & Network Isolation</div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '12px', background: 'var(--bg-surface)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
            <div>
              <div style={{ fontSize: 12, fontWeight: 700, color: 'var(--text-bright)' }}>Local-Only Air-Gap Isolation</div>
              <div style={{ fontSize: 10, color: 'var(--text-dim)', marginTop: 2 }}>
                Hard-blocks all cloud AI providers, remote Ollama servers, and external network calls. Forces 100% local model inference.
              </div>
            </div>
            <button
              type="button"
              onClick={() => handleToggleAirgap(!airgapStatus.airgap_active)}
              style={{
                padding: '6px 14px',
                fontSize: 11,
                fontFamily: 'JetBrains Mono',
                fontWeight: 600,
                borderRadius: 'var(--radius-sm)',
                border: airgapStatus.airgap_active ? '1px solid var(--success)' : '1px solid var(--border-subtle)',
                background: airgapStatus.airgap_active ? 'rgba(52, 211, 153, 0.15)' : 'var(--bg-panel)',
                color: airgapStatus.airgap_active ? 'var(--success)' : 'var(--text-main)',
                cursor: 'pointer'
              }}
            >
              {airgapStatus.airgap_active ? '🔒 AIR-GAP ACTIVE' : '🌐 CLOUD ALLOWED'}
            </button>
          </div>
          {airgapStatus.proof_badge && (
            <div style={{ fontSize: 10, color: 'var(--accent)', fontFamily: 'JetBrains Mono', background: 'var(--accent-muted)', padding: '6px 10px', borderRadius: 'var(--radius-sm)' }}>
              Proof Badge: {airgapStatus.proof_badge}
            </div>
          )}
        </div>
      </GlowCard>

      {/* Monthly Spend Budget Cap & Toggle */}
      <GlowCard className="glass" style={{ padding: 16 }}>
        <div className="section-label">💰 Monthly LLM Spend Budget & Cap Controls</div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
          
          {/* Enable / Disable Budget Enforcement Toggle */}
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '12px', background: 'var(--bg-surface)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
            <div>
              <div style={{ fontSize: 12, fontWeight: 700, color: 'var(--text-bright)' }}>Enforce Spend Budget Cap</div>
              <div style={{ fontSize: 10, color: 'var(--text-dim)', marginTop: 2 }}>
                Automatically block API calls when monthly spend exceeds your cap threshold.
              </div>
            </div>
            <button
              type="button"
              onClick={() => handleToggleBudgetEnabled(!budgetEnabled)}
              style={{
                padding: '6px 14px',
                fontSize: 11,
                fontFamily: 'JetBrains Mono',
                fontWeight: 600,
                borderRadius: 'var(--radius-sm)',
                border: budgetEnabled ? '1px solid var(--accent)' : '1px solid var(--border-subtle)',
                background: budgetEnabled ? 'var(--accent-muted)' : 'var(--bg-panel)',
                color: budgetEnabled ? 'var(--accent)' : 'var(--text-dim)',
                cursor: 'pointer'
              }}
            >
              {budgetEnabled ? 'ON (ENFORCED)' : 'OFF (DISABLED)'}
            </button>
          </div>

          {/* Budget Limit Input */}
          <div style={{ display: 'grid', gridTemplateColumns: '1fr auto', gap: 10, alignItems: 'end' }}>
            <div>
              <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                Monthly Spend Cap ($ USD)
              </label>
              <input
                type="number"
                step="0.50"
                min="1.00"
                value={newBudgetCap}
                onChange={e => setNewBudgetCap(e.target.value)}
                className="input-base"
                style={{ fontFamily: 'JetBrains Mono' }}
              />
            </div>
            <HoloButton type="button" variant="primary" size="sm" onClick={handleUpdateBudgetCap}>
              Save Cap
            </HoloButton>
          </div>

          {/* Current Monthly Cost Stats Meter */}
          <div style={{ padding: '12px', background: 'var(--bg-surface)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 6 }}>
              <span style={{ fontSize: 11, color: 'var(--text-main)', fontFamily: 'JetBrains Mono' }}>Current Month Spend</span>
              <span style={{ fontSize: 13, fontWeight: 700, color: spendStats.budget_exceeded ? 'var(--danger)' : 'var(--accent)', fontFamily: 'JetBrains Mono' }}>
                ${Number(spendStats.monthly_cost_usd || 0).toFixed(4)} / ${Number(spendStats.budget_cap_usd || 10).toFixed(2)}
              </span>
            </div>
            <div style={{ width: '100%', height: 6, background: 'var(--bg-panel)', borderRadius: 3, overflow: 'hidden' }}>
              <div
                style={{
                  width: `${Math.min(100, ((spendStats.monthly_cost_usd || 0) / (spendStats.budget_cap_usd || 10)) * 100)}%`,
                  height: '100%',
                  background: spendStats.budget_exceeded ? 'var(--danger)' : 'var(--accent)',
                  transition: 'width 0.3s ease'
                }}
              />
            </div>
          </div>
        </div>
      </GlowCard>
    </>
  );
}
