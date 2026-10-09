import React from 'react';
import { Download, Loader2, RefreshCw, Trash2, Plus } from 'lucide-react';
import GlowCard from '../../components/ui/GlowCard';
import HoloButton from '../../components/ui/HoloButton';

export interface SystemGuardTabProps {
  checkSystemUpdate: () => void;
  isCheckingUpdate: boolean;
  updateInfo: any;
  handleTriggerUpdate: () => void;
  isTriggeringUpdate: boolean;
  updateMsg: string;
  cpuWarn: number;
  setCpuWarn: (v: number) => void;
  ramWarn: number;
  setRamWarn: (v: number) => void;
  diskWarn: number;
  setDiskWarn: (v: number) => void;
  distractions: string;
  setDistractions: (v: string) => void;
  isLowRam: boolean;
  toggleLowRamMode: (enabled?: boolean) => void;
  browserWidth: number;
  setBrowserWidth: (v: number) => void;
  browserHeight: number;
  setBrowserHeight: (v: number) => void;
  mcpServers: Record<string, any>;
  handleRemoveMcpServer: (name: string) => void;
  newServerName: string;
  setNewServerName: (v: string) => void;
  newServerCommand: string;
  setNewServerCommand: (v: string) => void;
  newServerArgs: string;
  setNewServerArgs: (v: string) => void;
  newServerEnv: string;
  setNewServerEnv: (v: string) => void;
  handleAddMcpServer: () => void;
  startupEnabled: boolean;
  handleToggleStartup: (enabled: boolean) => void;
  gameMode: boolean;
  handleGameMode: (enabled: boolean) => void;
  logLevel: string;
  setLogLevel: (v: string) => void;
  mongodbUri: string;
  setMongodbUri: (v: string) => void;
  securityGuardLevel: number;
  handleToggleSecurityGuard: (lvl: number) => void;
  autonomousMode: boolean;
  handleToggleAutonomous: (val: boolean) => void;
  pairHost: string;
  setPairHost: (v: string) => void;
  pairPort: string;
  setPairPort: (v: string) => void;
  pairSecret: string;
  setPairSecret: (v: string) => void;
  pairStatus: { text: string; isError: boolean } | null;
  handleVerifyPairing: () => void;
  isVerifyingPair: boolean;
}

export default function SystemGuardTab({
  checkSystemUpdate,
  isCheckingUpdate,
  updateInfo,
  handleTriggerUpdate,
  isTriggeringUpdate,
  updateMsg,
  cpuWarn,
  setCpuWarn,
  ramWarn,
  setRamWarn,
  diskWarn,
  setDiskWarn,
  distractions,
  setDistractions,
  isLowRam,
  toggleLowRamMode,
  browserWidth,
  setBrowserWidth,
  browserHeight,
  setBrowserHeight,
  mcpServers,
  handleRemoveMcpServer,
  newServerName,
  setNewServerName,
  newServerCommand,
  setNewServerCommand,
  newServerArgs,
  setNewServerArgs,
  newServerEnv,
  setNewServerEnv,
  handleAddMcpServer,
  startupEnabled,
  handleToggleStartup,
  gameMode,
  handleGameMode,
  logLevel,
  setLogLevel,
  mongodbUri,
  setMongodbUri,
  securityGuardLevel,
  handleToggleSecurityGuard,
  autonomousMode,
  handleToggleAutonomous,
  pairHost,
  setPairHost,
  pairPort,
  setPairPort,
  pairSecret,
  setPairSecret,
  pairStatus,
  handleVerifyPairing,
  isVerifyingPair,
}: SystemGuardTabProps) {
  return (
    <>
      {/* System Version & Auto-Update Engine */}
      <GlowCard className="glass" style={{ padding: 16 }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 12 }}>
          <div className="section-label" style={{ margin: 0 }}>🪐 System Version & Auto-Update Engine</div>
          <HoloButton type="button" variant="ghost" size="sm" onClick={checkSystemUpdate} disabled={isCheckingUpdate}>
            {isCheckingUpdate ? <Loader2 size={12} className="animate-spin" /> : <RefreshCw size={12} />}
            {isCheckingUpdate ? 'Checking GitHub...' : 'Check for Updates'}
          </HoloButton>
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 12, marginBottom: 12 }}>
          <div style={{ background: 'var(--bg-surface)', padding: 12, borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
            <div style={{ fontSize: 9, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', textTransform: 'uppercase' }}>Installed Version</div>
            <div style={{ fontSize: 16, fontWeight: 700, color: 'var(--accent)', fontFamily: 'JetBrains Mono', marginTop: 4 }}>
              v{updateInfo?.current_version || '0.2.3'}
            </div>
          </div>
          <div style={{ background: 'var(--bg-surface)', padding: 12, borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
            <div style={{ fontSize: 9, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', textTransform: 'uppercase' }}>GitHub Latest Version</div>
            <div style={{ fontSize: 16, fontWeight: 700, color: updateInfo?.update_available ? '#34D399' : 'var(--text-bright)', fontFamily: 'JetBrains Mono', marginTop: 4 }}>
              v{updateInfo?.version_on_github || '0.2.3'}
            </div>
          </div>
        </div>

        {updateInfo?.update_available ? (
          <div style={{ background: updateInfo.update_type === 'major' ? 'rgba(239, 68, 68, 0.12)' : 'rgba(16, 185, 129, 0.12)', border: updateInfo.update_type === 'major' ? '1px solid rgba(239, 68, 68, 0.3)' : '1px solid rgba(16, 185, 129, 0.3)', borderRadius: 'var(--radius-sm)', padding: 12 }}>
            <div style={{ fontSize: 12, fontWeight: 700, color: updateInfo.update_type === 'major' ? '#F87171' : '#34D399', display: 'flex', alignItems: 'center', gap: 6 }}>
              <span>✨ {updateInfo.update_type === 'major' ? 'Major Version Upgrade Available!' : updateInfo.auto_downloaded ? 'Patch Update Ready to Apply!' : 'Minor Update Ready!'}</span>
              <span style={{ fontSize: 9, background: 'var(--bg-surface)', padding: '2px 6px', borderRadius: 'var(--radius-sm)', textTransform: 'uppercase' }}>{updateInfo.update_type}</span>
            </div>
            <div style={{ fontSize: 11, color: 'var(--text-main)', marginTop: 6, lineHeight: 1.4 }}>
              {updateInfo.update_type === 'major'
                ? 'A major release has breaking architectural changes. Click below to upgrade.'
                : updateInfo.auto_downloaded
                  ? 'Patch assets were auto-downloaded in the background. Click below to pull final code and apply update.'
                  : 'A minor update is available. Click below to apply.'}
            </div>
            <div style={{ display: 'flex', gap: 8, marginTop: 10, alignItems: 'center' }}>
              <HoloButton type="button" variant="primary" size="sm" onClick={handleTriggerUpdate} disabled={isTriggeringUpdate}>
                {isTriggeringUpdate ? <Loader2 size={12} className="animate-spin" /> : <Download size={12} />}
                {isTriggeringUpdate ? 'Updating...' : updateInfo.update_type === 'major' ? 'Upgrade to Major Version' : 'Apply Update & Pull Code'}
              </HoloButton>
              {updateInfo.release_url && (
                <a href={updateInfo.release_url} target="_blank" rel="noreferrer" style={{ fontSize: 11, color: 'var(--accent)', textDecoration: 'none', fontFamily: 'JetBrains Mono' }}>
                  View Release Notes ↗
                </a>
              )}
            </div>
          </div>
        ) : (
          <div style={{ fontSize: 11, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono' }}>
            ✅ Meridian-X is running the latest version.
          </div>
        )}
        {updateMsg && (
          <div style={{ marginTop: 8, fontSize: 11, color: '#34D399', fontFamily: 'JetBrains Mono' }}>
            {updateMsg}
          </div>
        )}
      </GlowCard>

      {/* Proactive Guard Config */}
      <GlowCard className="glass" style={{ padding: 16 }}>
        <div className="section-label">Proactive Monitoring & System Guard</div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 8 }}>
            <div>
              <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>CPU Warn (%)</label>
              <input type="number" min="10" max="95" value={cpuWarn} onChange={e => setCpuWarn(parseFloat(e.target.value))} className="input-base" />
            </div>
            <div>
              <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>RAM Warn (%)</label>
              <input type="number" min="10" max="95" value={ramWarn} onChange={e => setRamWarn(parseFloat(e.target.value))} className="input-base" />
            </div>
            <div>
              <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>Disk Warn (%)</label>
              <input type="number" min="10" max="95" value={diskWarn} onChange={e => setDiskWarn(parseFloat(e.target.value))} className="input-base" />
            </div>
          </div>
          <div>
            <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>Distraction Websites Blocklist (comma-separated)</label>
            <input type="text" value={distractions} onChange={e => setDistractions(e.target.value)} className="input-base" />
          </div>
        </div>
      </GlowCard>

      {/* OPT-01 RAM & Performance Engine */}
      <GlowCard className="glass" style={{ padding: 16 }}>
        <div className="section-label">⚡ RAM & Performance Engine (OPT-01)</div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
            <div>
              <div style={{ fontSize: 12, fontWeight: 600, color: 'var(--text-bright)' }}>Low-RAM Performance Mode</div>
              <div style={{ fontSize: 10, color: 'var(--text-dim)', marginTop: 2 }}>Strips blurs, backdrop filters, animations, and box shadows to maintain memory under 45MB RAM.</div>
            </div>
            <label style={{ display: 'flex', alignItems: 'center', gap: 8, cursor: 'pointer' }}>
              <input
                type="checkbox"
                checked={isLowRam}
                onChange={e => toggleLowRamMode(e.target.checked)}
              />
              <span style={{ fontSize: 11, fontFamily: 'JetBrains Mono', color: isLowRam ? 'var(--accent)' : 'var(--text-dim)' }}>
                {isLowRam ? 'Enabled' : 'Disabled'}
              </span>
            </label>
          </div>
        </div>
      </GlowCard>

      {/* Browser Tool Config */}
      <GlowCard className="glass" style={{ padding: 16 }}>
        <div className="section-label">Web Browser Tool Settings</div>
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 12 }}>
          <div>
            <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>Viewport Width (px)</label>
            <input type="number" min="320" max="3840" value={browserWidth} onChange={e => setBrowserWidth(parseInt(e.target.value))} className="input-base" />
          </div>
          <div>
            <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>Viewport Height (px)</label>
            <input type="number" min="240" max="2160" value={browserHeight} onChange={e => setBrowserHeight(parseInt(e.target.value))} className="input-base" />
          </div>
        </div>
      </GlowCard>

      {/* MCP Servers Manager */}
      <GlowCard className="glass" style={{ padding: 16 }}>
        <div className="section-label">MCP Servers Manager</div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
          {/* Active Servers List */}
          {Object.keys(mcpServers).length > 0 ? (
            <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
              <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                Active Servers
              </label>
              {Object.entries(mcpServers).map(([name, srv]: [string, any]) => (
                <div key={name} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '10px 12px', background: 'var(--bg-surface)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
                    <div style={{ fontSize: 12, fontWeight: 700, color: 'var(--accent)' }}>
                      {name} <span style={{ fontSize: 9, color: 'var(--text-dim)', fontWeight: 400, fontFamily: 'JetBrains Mono' }}>({srv.command})</span>
                    </div>
                    {srv.args && srv.args.length > 0 && (
                      <div style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', wordBreak: 'break-all' }}>
                        args: {srv.args.join(' ')}
                      </div>
                    )}
                    {srv.env && Object.keys(srv.env).length > 0 && (
                      <div style={{ fontSize: 9, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono' }}>
                        env: {Object.entries(srv.env).map(([k, v]) => `${k}=${v}`).join(', ')}
                      </div>
                    )}
                  </div>
                  <HoloButton type="button" variant="danger" size="sm" onClick={() => handleRemoveMcpServer(name)}>
                    <Trash2 size={12} />
                  </HoloButton>
                </div>
              ))}
            </div>
          ) : (
            <div style={{ fontSize: 11, color: 'var(--text-dim)', padding: '12px 0', textAlign: 'center', border: '1px dashed var(--border-subtle)', borderRadius: 'var(--radius-sm)' }}>
              No active MCP servers configured. Add one below to extend agent capabilities.
            </div>
          )}

          {/* Add New Server Form */}
          <div style={{ borderTop: '1px solid var(--border-subtle)', paddingTop: 12, display: 'flex', flexDirection: 'column', gap: 10 }}>
            <label style={{ fontSize: 10, color: 'var(--accent)', fontFamily: 'JetBrains Mono', display: 'block', textTransform: 'uppercase', letterSpacing: '0.06em', fontWeight: 600 }}>
              Add Stdio MCP Server
            </label>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8 }}>
              <div>
                <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Server ID Name</label>
                <input type="text" value={newServerName} onChange={e => setNewServerName(e.target.value)} placeholder="e.g. sqlite" className="input-base" style={{ height: 32, fontSize: 11 }} />
              </div>
              <div>
                <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Startup Command</label>
                <input type="text" value={newServerCommand} onChange={e => setNewServerCommand(e.target.value)} placeholder="e.g. npx" className="input-base" style={{ height: 32, fontSize: 11 }} />
              </div>
            </div>

            <div>
              <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Arguments (comma-separated)</label>
              <input type="text" value={newServerArgs} onChange={e => setNewServerArgs(e.target.value)} placeholder="e.g. -y, @modelcontextprotocol/server-sqlite, --db, test.db" className="input-base" style={{ height: 32, fontSize: 11, fontFamily: 'JetBrains Mono' }} />
            </div>

            <div>
              <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Environment Variables (comma-separated KEY=VAL)</label>
              <input type="text" value={newServerEnv} onChange={e => setNewServerEnv(e.target.value)} placeholder="e.g. API_KEY=abc, DB_PATH=def" className="input-base" style={{ height: 32, fontSize: 11, fontFamily: 'JetBrains Mono' }} />
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: 4 }}>
              <HoloButton type="button" variant="primary" size="sm" onClick={handleAddMcpServer} disabled={!newServerName.trim() || !newServerCommand.trim()}>
                <Plus size={12} /> Add Server
              </HoloButton>
            </div>
          </div>
        </div>
      </GlowCard>

      {/* System */}
      <GlowCard className="glass" style={{ padding: 16 }}>
        <div className="section-label">System</div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
          {/* Startup Toggle */}
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '10px 12px', background: 'var(--bg-surface)', borderRadius: 'var(--radius-sm)' }}>
            <div>
              <div style={{ fontSize: 11, fontWeight: 600, color: 'var(--accent)', fontFamily: "'JetBrains Mono', monospace", marginBottom: 2 }}>Launch on Startup</div>
              <div style={{ fontSize: 10, color: 'var(--text-dim)' }}>Automatically start Meridian-X when Windows boots.</div>
            </div>
            <input
              type="checkbox"
              checked={startupEnabled}
              onChange={e => handleToggleStartup(e.target.checked)}
              style={{ width: 16, height: 16, accentColor: 'var(--accent)', cursor: 'pointer' }}
            />
          </div>

          {/* Game Mode */}
          {((window as any).__TAURI_INTERNALS__) && (
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '10px 12px', background: 'var(--bg-surface)', borderRadius: 'var(--radius-sm)' }}>
              <div>
                <div style={{ fontSize: 11, fontWeight: 600, color: 'var(--accent)', fontFamily: "'JetBrains Mono', monospace", marginBottom: 2 }}>Desktop Game Mode</div>
                <div style={{ fontSize: 10, color: 'var(--text-dim)' }}>Suspends Alt+M / Alt+V hotkeys during full-screen games.</div>
              </div>
              <input
                type="checkbox"
                checked={gameMode}
                onChange={e => handleGameMode(e.target.checked)}
                style={{ width: 16, height: 16, accentColor: 'var(--accent)', cursor: 'pointer' }}
              />
            </div>
          )}

          {/* Log Level & MongoDB URI */}
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 2fr', gap: 8, borderTop: '1px solid var(--border-subtle)', paddingTop: 10 }}>
            <div>
              <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>Log Level</label>
              <select value={logLevel} onChange={e => setLogLevel(e.target.value)} className="select-base" style={{ height: 32, fontSize: 11 }}>
                <option value="DEBUG">DEBUG</option>
                <option value="INFO">INFO</option>
                <option value="WARNING">WARNING</option>
                <option value="ERROR">ERROR</option>
                <option value="CRITICAL">CRITICAL</option>
              </select>
            </div>
            <div>
              <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>MongoDB URI</label>
              <input type="text" value={mongodbUri} onChange={e => setMongodbUri(e.target.value)} placeholder="mongodb://localhost:27017/meridian_kg" className="input-base" style={{ height: 32, fontSize: 11, fontFamily: "'JetBrains Mono', monospace" }} />
            </div>
          </div>
        </div>
      </GlowCard>

      {/* Security Guard Level 0/1 */}
      <GlowCard className="glass" style={{ padding: 16 }}>
        <div className="section-label">🛡️ System Guard & Execution Rights</div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 10 }}>
            <button
              type="button"
              onClick={() => handleToggleSecurityGuard(1)}
              style={{
                padding: 12,
                textAlign: 'left',
                borderRadius: 'var(--radius-sm)',
                border: securityGuardLevel === 1 ? '1.5px solid var(--accent)' : '1px solid var(--border-subtle)',
                background: securityGuardLevel === 1 ? 'var(--bg-surface)' : 'var(--bg-panel)',
                cursor: 'pointer'
              }}
            >
              <div style={{ fontSize: 12, fontWeight: 700, color: securityGuardLevel === 1 ? 'var(--accent)' : 'var(--text-bright)' }}>
                Level 1: Standard Guard
              </div>
              <div style={{ fontSize: 10, color: 'var(--text-dim)', marginTop: 4 }}>
                Requires confirmation prompt before running OS shell commands or mutating files.
              </div>
            </button>

            <button
              type="button"
              onClick={() => handleToggleSecurityGuard(0)}
              style={{
                padding: 12,
                textAlign: 'left',
                borderRadius: 'var(--radius-sm)',
                border: securityGuardLevel === 0 ? '1.5px solid var(--danger)' : '1px solid var(--border-subtle)',
                background: securityGuardLevel === 0 ? 'rgba(239, 68, 68, 0.12)' : 'var(--bg-panel)',
                cursor: 'pointer'
              }}
            >
              <div style={{ fontSize: 12, fontWeight: 700, color: securityGuardLevel === 0 ? 'var(--danger)' : 'var(--text-bright)' }}>
                Level 0: Unrestricted PC Access Mode
              </div>
              <div style={{ fontSize: 10, color: 'var(--text-dim)', marginTop: 4 }}>
                Bypasses approval gates. Allows Meridian-X full unrestricted OS execution without confirmation prompts.
              </div>
            </button>
          </div>
        </div>
      </GlowCard>

      {/* Continuous Autonomous Loop Mode */}
      <GlowCard className="glass" style={{ padding: 16 }}>
        <div className="section-label">🔄 Autonomous Continuous Loop Mode</div>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '12px', background: 'var(--bg-surface)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
          <div>
            <div style={{ fontSize: 12, fontWeight: 700, color: 'var(--text-bright)' }}>Continuous Autonomous ReAct Loop</div>
            <div style={{ fontSize: 10, color: 'var(--text-dim)', marginTop: 2 }}>
              Auto-continues multi-turn tool execution without requiring manual "continue" prompts.
            </div>
          </div>
          <button
            type="button"
            onClick={() => handleToggleAutonomous(!autonomousMode)}
            style={{
              padding: '6px 14px',
              fontSize: 11,
              fontFamily: 'JetBrains Mono',
              fontWeight: 600,
              borderRadius: 'var(--radius-sm)',
              border: autonomousMode ? '1px solid var(--accent-2)' : '1px solid var(--border-subtle)',
              background: autonomousMode ? 'rgba(52, 211, 153, 0.15)' : 'var(--bg-panel)',
              color: autonomousMode ? 'var(--accent-2)' : 'var(--text-dim)',
              cursor: 'pointer'
            }}
          >
            {autonomousMode ? '⚡ ENABLED (AUTO)' : '⏸️ MANUAL STEP'}
          </button>
        </div>
      </GlowCard>

      {/* Mobile Manual Pairing */}
      <GlowCard className="glass" style={{ padding: 16 }}>
        <div className="section-label">📱 Desktop-to-Mobile App Pairing</div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
          <div style={{ fontSize: 10, color: 'var(--text-dim)' }}>
            Pair Meridian Mobile companion app to sync backend control, voice triggers, and agent status. Enter details manually and verify.
          </div>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 100px', gap: 8 }}>
            <div>
              <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Desktop Host</label>
              <input type="text" value={pairHost} onChange={e => setPairHost(e.target.value)} placeholder="127.0.0.1" className="input-base" style={{ height: 32, fontSize: 11, fontFamily: 'JetBrains Mono' }} />
            </div>
            <div>
              <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Port</label>
              <input type="text" value={pairPort} onChange={e => setPairPort(e.target.value)} placeholder="4133" className="input-base" style={{ height: 32, fontSize: 11, fontFamily: 'JetBrains Mono' }} />
            </div>
          </div>
          <div>
            <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Pairing Secret</label>
            <input type="password" value={pairSecret} onChange={e => setPairSecret(e.target.value)} placeholder="paste pairing secret" className="input-base" style={{ height: 32, fontSize: 11, fontFamily: 'JetBrains Mono' }} />
          </div>
          {pairStatus && (
            <div style={{ fontSize: 11, color: pairStatus.isError ? 'var(--danger)' : 'var(--success)' }}>{pairStatus.text}</div>
          )}
          <div>
            <HoloButton type="button" variant="primary" size="sm" onClick={handleVerifyPairing} loading={isVerifyingPair} disabled={!pairSecret.trim()}>
              Verify Pairing
            </HoloButton>
          </div>
        </div>
      </GlowCard>
    </>
  );
}
