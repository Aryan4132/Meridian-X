import React from 'react';
import { Eye, EyeOff, Loader2, Plus, RefreshCw, Save, Trash2 } from 'lucide-react';
import GlowCard from '../../components/ui/GlowCard';
import HoloButton from '../../components/ui/HoloButton';
import PasswordInput from './PasswordInput';
import { API_BASE_URL } from '../../config';

export interface IntegrationsTabProps {
  backendUrl: string;
  setBackendUrl: (v: string) => void;
  backendApiKey: string;
  setBackendApiKey: (v: string) => void;
  backendStatusMsg: { text: string; isError: boolean } | null;
  isTestingBackend: boolean;
  handleTestBackendConnection: () => void;
  handleSaveBackendConfig: () => void;
  handleResetBackendConfig: () => void;
  tavilyKey: string;
  setTavilyKey: (v: string) => void;
  discordToken: string;
  setDiscordToken: (v: string) => void;
  telegramToken: string;
  setTelegramToken: (v: string) => void;
  telegramChatId: string;
  setTelegramChatId: (v: string) => void;
  vaultKeys: any[];
  showVaultSecrets: boolean;
  setShowVaultSecrets: (v: boolean | ((prev: boolean) => boolean)) => void;
  fetchVaultKeys: (unmasked?: boolean) => void;
  handleDeleteVaultKey: (k: string) => void;
  vkName: string;
  setVkName: (v: string) => void;
  vkEnvVar: string;
  setVkEnvVar: (v: string) => void;
  vkSecret: string;
  setVkSecret: (v: string) => void;
  vkCategory: string;
  setVkCategory: (v: string) => void;
  vkBaseUrl: string;
  setVkBaseUrl: (v: string) => void;
  handleAddVaultKey: () => void;
  smtpEmail: string;
  setSmtpEmail: (v: string) => void;
  smtpPassword: string;
  setSmtpPassword: (v: string) => void;
  smtpServer: string;
  setSmtpServer: (v: string) => void;
  smtpPort: number;
  setSmtpPort: (v: number) => void;
  imapServer: string;
  setImapServer: (v: string) => void;
  mcpServers: Record<string, any>;
  handleDeleteCustomMcpServer: (name: string) => void;
  newServerName: string;
  setNewServerName: (v: string) => void;
  newServerCommand: string;
  setNewServerCommand: (v: string) => void;
  newServerArgs: string;
  setNewServerArgs: (v: string) => void;
  newServerEnv: string;
  setNewServerEnv: (v: string) => void;
  handleAddCustomMcpServer: () => void;
  mcpCatalog: any[];
  handleInstallMcp: (id: string) => void;
  keysUnlocked: boolean;
  requestUnlock: () => void;
  isKeyLockUnlocked: () => boolean;
}

export default function IntegrationsTab({
  backendUrl,
  setBackendUrl,
  backendApiKey,
  setBackendApiKey,
  backendStatusMsg,
  isTestingBackend,
  handleTestBackendConnection,
  handleSaveBackendConfig,
  handleResetBackendConfig,
  tavilyKey,
  setTavilyKey,
  discordToken,
  setDiscordToken,
  telegramToken,
  setTelegramToken,
  telegramChatId,
  setTelegramChatId,
  vaultKeys,
  showVaultSecrets,
  setShowVaultSecrets,
  fetchVaultKeys,
  handleDeleteVaultKey,
  vkName,
  setVkName,
  vkEnvVar,
  setVkEnvVar,
  vkSecret,
  setVkSecret,
  vkCategory,
  setVkCategory,
  vkBaseUrl,
  setVkBaseUrl,
  handleAddVaultKey,
  smtpEmail,
  setSmtpEmail,
  smtpPassword,
  setSmtpPassword,
  smtpServer,
  setSmtpServer,
  smtpPort,
  setSmtpPort,
  imapServer,
  setImapServer,
  mcpServers,
  handleDeleteCustomMcpServer,
  newServerName,
  setNewServerName,
  newServerCommand,
  setNewServerCommand,
  newServerArgs,
  setNewServerArgs,
  newServerEnv,
  setNewServerEnv,
  handleAddCustomMcpServer,
  mcpCatalog,
  handleInstallMcp,
  keysUnlocked,
  requestUnlock,
  isKeyLockUnlocked,
}: IntegrationsTabProps) {
  return (
    <>
      {/* Frontend & Backend Server Integration */}
      <GlowCard className="glass" style={{ padding: 16 }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 12 }}>
          <div className="section-label" style={{ margin: 0 }}>🌐 Core Frontend & Backend Integration</div>
          <span style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono' }}>
            Active Endpoint: {API_BASE_URL}
          </span>
        </div>

        <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
          <div>
            <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
              Backend Server URL
            </label>
            <input
              type="text"
              value={backendUrl}
              onChange={(e) => setBackendUrl(e.target.value)}
              placeholder="http://127.0.0.1:4132 or https://my-backend-server.com"
              className="input-base"
              style={{ width: '100%', fontSize: 12 }}
            />
          </div>

          <PasswordInput
            label="Backend API Key (Required for Remote/Protected Server)"
            value={backendApiKey}
            onChange={setBackendApiKey}
            placeholder="Enter Meridian secret API key"
            requireUnlock
            keysUnlocked={keysUnlocked}
            onRequestUnlock={requestUnlock}
          />

          {backendStatusMsg && (
            <div style={{
              padding: '8px 12px',
              borderRadius: 'var(--radius-sm)',
              fontSize: 11,
              fontFamily: 'JetBrains Mono',
              background: backendStatusMsg.isError ? 'rgba(244, 63, 94, 0.15)' : 'rgba(16, 185, 129, 0.15)',
              border: backendStatusMsg.isError ? '1px solid rgba(244, 63, 94, 0.4)' : '1px solid rgba(16, 185, 129, 0.4)',
              color: backendStatusMsg.isError ? '#f87171' : '#34d399'
            }}>
              {backendStatusMsg.text}
            </div>
          )}

          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginTop: 4 }}>
            <HoloButton
              type="button"
              variant="ghost"
              size="sm"
              onClick={handleTestBackendConnection}
              disabled={isTestingBackend}
            >
              {isTestingBackend ? <Loader2 className="animate-spin" size={12} /> : <RefreshCw size={12} />}
              {isTestingBackend ? 'Testing...' : 'Test Connection'}
            </HoloButton>

            <HoloButton
              type="button"
              variant="primary"
              size="sm"
              onClick={handleSaveBackendConfig}
            >
              <Save size={12} />
              Save & Connect
            </HoloButton>

            <HoloButton
              type="button"
              variant="ghost"
              size="sm"
              onClick={handleResetBackendConfig}
            >
              Reset Defaults
            </HoloButton>
          </div>
        </div>
      </GlowCard>

      {/* Integrations */}
      <GlowCard className="glass" style={{ padding: 16 }}>
        <div className="section-label">Integrations & Tokens</div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
          <PasswordInput label="Tavily API Key (Web Search)" value={tavilyKey} onChange={setTavilyKey} placeholder="tvly-..." requireUnlock keysUnlocked={keysUnlocked} onRequestUnlock={requestUnlock} />
          <PasswordInput label="Discord Bot Token" value={discordToken} onChange={setDiscordToken} placeholder="MT..." requireUnlock keysUnlocked={keysUnlocked} onRequestUnlock={requestUnlock} />
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8 }}>
            <PasswordInput label="Telegram Bot Token" value={telegramToken} onChange={setTelegramToken} placeholder="bot..." requireUnlock keysUnlocked={keysUnlocked} onRequestUnlock={requestUnlock} />
            <div>
              <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>Chat ID</label>
              <input type="text" value={telegramChatId} onChange={e => setTelegramChatId(e.target.value)} placeholder="123456789" className="input-base" />
            </div>
          </div>
        </div>
      </GlowCard>

      {/* Universal Encrypted Secret Vault */}
      <GlowCard className="glass" style={{ padding: 16 }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 12 }}>
          <div className="section-label" style={{ margin: 0 }}>🔐 Universal API Key & Secret Vault</div>
          <button
            type="button"
            onClick={() => {
              if (showVaultSecrets) { setShowVaultSecrets(false); fetchVaultKeys(false); }
              else if (keysUnlocked || isKeyLockUnlocked()) { setShowVaultSecrets(true); fetchVaultKeys(true); }
              else requestUnlock();
            }}
            style={{ background: 'none', border: 'none', cursor: 'pointer', color: 'var(--accent)', fontSize: 11, display: 'flex', alignItems: 'center', gap: 4, fontFamily: 'JetBrains Mono' }}
          >
            {showVaultSecrets ? <EyeOff size={12} /> : <Eye size={12} />}
            {showVaultSecrets ? 'Mask Keys' : 'Unmask Keys'}
          </button>
        </div>

        {/* List of active custom keys */}
        {vaultKeys.length > 0 ? (
          <div style={{ display: 'flex', flexDirection: 'column', gap: 8, marginBottom: 16 }}>
            {vaultKeys.map(k => (
              <div key={k.env_var} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '10px 12px', background: 'var(--bg-surface)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <span style={{ fontSize: 12, fontWeight: 700, color: 'var(--text-bright)' }}>{k.name}</span>
                    <span style={{ fontSize: 9, padding: '2px 6px', background: 'var(--accent-muted)', color: 'var(--accent)', borderRadius: 'var(--radius-sm)', fontFamily: 'JetBrains Mono' }}>
                      {k.category || 'LLM Provider'}
                    </span>
                    <span style={{ fontSize: 10, color: 'var(--accent)', fontFamily: 'JetBrains Mono', fontWeight: 600 }}>
                      ${k.env_var}
                    </span>
                  </div>
                  <div style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono' }}>
                    Key: {(keysUnlocked && showVaultSecrets) ? k.api_key : '••••••••••••••••'} {k.base_url && `· Base: ${k.base_url}`}
                  </div>
                </div>
                <HoloButton type="button" variant="danger" size="sm" onClick={() => handleDeleteVaultKey(k.env_var)}>
                  <Trash2 size={12} />
                </HoloButton>
              </div>
            ))}
          </div>
        ) : (
          <div style={{ fontSize: 11, color: 'var(--text-dim)', padding: '10px 0', textAlign: 'center', border: '1px dashed var(--border-subtle)', borderRadius: 'var(--radius-sm)', marginBottom: 16 }}>
            No custom API keys registered in encrypted vault yet. Add Groq, OpenRouter, Mistral, SerpAPI or any custom tool key below.
          </div>
        )}

        {/* Add New Key Form */}
        <div style={{ borderTop: '1px solid var(--border-subtle)', paddingTop: 12, display: 'flex', flexDirection: 'column', gap: 10 }}>
          <label style={{ fontSize: 10, color: 'var(--accent)', fontFamily: 'JetBrains Mono', display: 'block', textTransform: 'uppercase', letterSpacing: '0.06em', fontWeight: 600 }}>
            + Add Dynamic API Key or Cloud Secret
          </label>

          <div style={{ display: 'grid', gridTemplateColumns: '1.2fr 1fr', gap: 8 }}>
            <div>
              <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Service Name</label>
              <input type="text" value={vkName} onChange={e => setVkName(e.target.value)} placeholder="e.g. Groq Cloud / OpenRouter" className="input-base" style={{ height: 32, fontSize: 11 }} />
            </div>
            <div>
              <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Env Var Name</label>
              <input type="text" value={vkEnvVar} onChange={e => setVkEnvVar(e.target.value.toUpperCase())} placeholder="e.g. GROQ_API_KEY" className="input-base" style={{ height: 32, fontSize: 11, fontFamily: 'JetBrains Mono' }} />
            </div>
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: '1.5fr 1fr', gap: 8 }}>
            <div>
              <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>API Key / Secret Token</label>
              <input type="password" value={vkSecret} onChange={e => setVkSecret(e.target.value)} placeholder="gsk_... / sk-or-v1-..." className="input-base" style={{ height: 32, fontSize: 11, fontFamily: 'JetBrains Mono' }} />
            </div>
            <div>
              <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Category</label>
              <select value={vkCategory} onChange={e => setVkCategory(e.target.value)} className="select-base" style={{ height: 32, fontSize: 11 }}>
                <option value="LLM Provider">LLM Provider</option>
                <option value="Search & Web">Search & Web</option>
                <option value="Audio & Voice">Audio & Voice</option>
                <option value="Vision & Media">Vision & Media</option>
                <option value="Vector DB">Vector DB</option>
                <option value="Custom Tool">Custom Tool</option>
              </select>
            </div>
          </div>

          <div>
            <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Base URL / Custom Endpoint (Optional)</label>
            <input type="text" value={vkBaseUrl} onChange={e => setVkBaseUrl(e.target.value)} placeholder="e.g. https://api.groq.com/openai/v1 (Optional)" className="input-base" style={{ height: 32, fontSize: 11, fontFamily: 'JetBrains Mono' }} />
          </div>

          <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: 4 }}>
            <HoloButton type="button" variant="primary" size="sm" onClick={handleAddVaultKey} disabled={!vkName.trim() || !vkEnvVar.trim() || !vkSecret.trim()}>
              <Plus size={12} /> Save Secret to Vault
            </HoloButton>
          </div>
        </div>
      </GlowCard>

      {/* Email Configuration */}
      <GlowCard className="glass" style={{ padding: 16 }}>
        <div className="section-label">Email Configuration (SMTP & IMAP)</div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8 }}>
            <div>
              <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>SMTP Email Address</label>
              <input type="email" value={smtpEmail} onChange={e => setSmtpEmail(e.target.value)} placeholder="your_email@gmail.com" className="input-base" />
            </div>
            <PasswordInput label="SMTP App-Specific Password" value={smtpPassword} onChange={setSmtpPassword} placeholder="16-character app password" requireUnlock keysUnlocked={keysUnlocked} onRequestUnlock={requestUnlock} />
          </div>
          <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr 2fr', gap: 8 }}>
            <div>
              <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>SMTP Server</label>
              <input type="text" value={smtpServer} onChange={e => setSmtpServer(e.target.value)} placeholder="smtp.gmail.com" className="input-base" style={{ fontFamily: "'JetBrains Mono', monospace" }} />
            </div>
            <div>
              <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>SMTP Port</label>
              <input type="number" value={smtpPort} onChange={e => setSmtpPort(parseInt(e.target.value) || 587)} placeholder="587" className="input-base" />
            </div>
            <div>
              <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>IMAP Server</label>
              <input type="text" value={imapServer} onChange={e => setImapServer(e.target.value)} placeholder="imap.gmail.com" className="input-base" style={{ fontFamily: "'JetBrains Mono', monospace" }} />
            </div>
          </div>
        </div>
      </GlowCard>

      {/* Model Context Protocol (MCP) Server Marketplace */}
      <GlowCard className="glass" style={{ padding: 16 }}>
        <div className="section-label" style={{ marginBottom: 10 }}>🔌 Model Context Protocol (MCP) Server Registry</div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
          <div style={{ fontSize: 11, color: 'var(--text-dim)', lineHeight: '1.5' }}>
            Manage connected Model Context Protocol (MCP) servers. Registered servers dynamically expose tools directly into the ReAct reasoning loop.
          </div>

          {/* Registered Custom Servers */}
          {Object.keys(mcpServers).length > 0 ? (
            <div>
              <label style={{ fontSize: 10, color: 'var(--accent)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 6, textTransform: 'uppercase', letterSpacing: '0.06em', fontWeight: 600 }}>
                Active Connected MCP Servers ({Object.keys(mcpServers).length})
              </label>
              <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                {Object.entries(mcpServers).map(([srvName, srvConfig]: [string, any]) => (
                  <div key={srvName} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '10px 12px', background: 'var(--bg-surface)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
                    <div style={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
                      <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ fontSize: 12, fontWeight: 700, color: 'var(--text-bright)' }}>{srvName}</span>
                        <span style={{ fontSize: 9, padding: '2px 6px', background: 'rgba(0, 217, 126, 0.15)', color: '#00D97E', borderRadius: 4, fontFamily: 'JetBrains Mono' }}>
                          Active
                        </span>
                      </div>
                      <div style={{ fontSize: 10, color: 'var(--accent)', fontFamily: 'JetBrains Mono' }}>
                        {srvConfig.command} {srvConfig.args?.join(' ')}
                      </div>
                    </div>
                    <HoloButton type="button" variant="danger" size="sm" onClick={() => handleDeleteCustomMcpServer(srvName)}>
                      <Trash2 size={12} />
                    </HoloButton>
                  </div>
                ))}
              </div>
            </div>
          ) : null}

          {/* Add Custom MCP Server Form */}
          <div style={{ borderTop: '1px solid var(--border-subtle)', paddingTop: 12, display: 'flex', flexDirection: 'column', gap: 10 }}>
            <label style={{ fontSize: 10, color: 'var(--accent)', fontFamily: 'JetBrains Mono', display: 'block', textTransform: 'uppercase', letterSpacing: '0.06em', fontWeight: 600 }}>
              + Enter / Register Custom MCP Server
            </label>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8 }}>
              <div>
                <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Server Name</label>
                <input type="text" value={newServerName} onChange={e => setNewServerName(e.target.value)} placeholder="e.g. Filesystem MCP / Git MCP" className="input-base" style={{ height: 32, fontSize: 11 }} />
              </div>
              <div>
                <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Command Executable</label>
                <input type="text" value={newServerCommand} onChange={e => setNewServerCommand(e.target.value)} placeholder="e.g. npx / uvx / node / python" className="input-base" style={{ height: 32, fontSize: 11, fontFamily: 'JetBrains Mono' }} />
              </div>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: '1.5fr 1fr', gap: 8 }}>
              <div>
                <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Arguments (Space Separated)</label>
                <input type="text" value={newServerArgs} onChange={e => setNewServerArgs(e.target.value)} placeholder="e.g. -y @modelcontextprotocol/server-filesystem C:/Projects" className="input-base" style={{ height: 32, fontSize: 11, fontFamily: 'JetBrains Mono' }} />
              </div>
              <div>
                <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Env Vars (KEY=VAL, ...)</label>
                <input type="text" value={newServerEnv} onChange={e => setNewServerEnv(e.target.value)} placeholder="API_KEY=xxx, TOKEN=yyy" className="input-base" style={{ height: 32, fontSize: 11, fontFamily: 'JetBrains Mono' }} />
              </div>
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: 2 }}>
              <HoloButton type="button" variant="primary" size="sm" onClick={handleAddCustomMcpServer} disabled={!newServerName.trim() || !newServerCommand.trim()}>
                <Plus size={12} /> Register MCP Server
              </HoloButton>
            </div>
          </div>

          {/* Catalog Servers */}
          <div style={{ borderTop: '1px solid var(--border-subtle)', paddingTop: 12 }}>
            <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 8, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
              1-Click Featured MCP Marketplace Catalog
            </label>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8 }}>
              {mcpCatalog.map(s => (
                <div key={s.id} style={{ display: 'flex', flexDirection: 'column', justifyContent: 'space-between', padding: '10px 12px', background: 'var(--bg-surface)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', gap: 8 }}>
                  <div>
                    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 4 }}>
                      <span style={{ fontSize: 12, fontWeight: 700, color: 'var(--text-bright)' }}>{s.name}</span>
                      <span style={{ fontSize: 9, padding: '2px 6px', background: s.installed ? 'color-mix(in srgb, var(--success) 15%, transparent)' : 'var(--accent-muted)', color: s.installed ? 'var(--success)' : 'var(--accent)', borderRadius: 'var(--radius-sm)', fontFamily: 'JetBrains Mono' }}>
                        {s.installed ? 'Installed' : s.category}
                      </span>
                    </div>
                    <div style={{ fontSize: 10, color: 'var(--text-dim)', lineHeight: '1.4' }}>{s.description}</div>
                    <div style={{ fontSize: 9, color: 'var(--accent)', fontFamily: 'JetBrains Mono', marginTop: 4 }}>{s.command}</div>
                  </div>
                  <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
                    <HoloButton
                      type="button"
                      variant={s.installed ? "ghost" : "primary"}
                      size="sm"
                      disabled={s.installed}
                      onClick={() => handleInstallMcp(s.id)}
                    >
                      {s.installed ? "Active" : "Install Server"}
                    </HoloButton>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </GlowCard>
    </>
  );
}
