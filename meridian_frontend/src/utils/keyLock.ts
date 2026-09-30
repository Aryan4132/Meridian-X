// KeyLock — password gate for revealing API keys / secrets in Settings.
// Password is set during initial startup (SetupWizard) and stored as a
// SHA-256 hash in localStorage. Unlock sessions expire after 10 minutes.

const HASH_KEY = 'meridian_keylock_hash';
const UNLOCK_UNTIL_KEY = 'meridian_keylock_unlocked_until';

export const KEYLOCK_SESSION_MS = 10 * 60 * 1000;

async function sha256Hex(text: string): Promise<string> {
  const data = new TextEncoder().encode(text);
  // crypto.subtle requires a secure context; fall back to a simple hash otherwise.
  try {
    if (crypto?.subtle) {
      const digest = await crypto.subtle.digest('SHA-256', data);
      return Array.from(new Uint8Array(digest))
        .map(b => b.toString(16).padStart(2, '0'))
        .join('');
    }
  } catch {
    // fall through to FNV fallback
  }
  let h1 = 0x811c9dc5;
  for (let i = 0; i < text.length; i++) {
    h1 ^= text.charCodeAt(i);
    h1 = Math.imul(h1, 0x01000193) >>> 0;
  }
  return `fnv1a-${h1.toString(16)}`;
}

export function hasKeyLockPassword(): boolean {
  try {
    return !!localStorage.getItem(HASH_KEY);
  } catch {
    return false;
  }
}

export async function setKeyLockPassword(password: string): Promise<void> {
  const hash = await sha256Hex(`meridian-keylock::${password}`);
  try {
    localStorage.setItem(HASH_KEY, hash);
    localStorage.removeItem(UNLOCK_UNTIL_KEY);
  } catch {
    // storage unavailable — ignore
  }
}

export async function verifyKeyLockPassword(password: string): Promise<boolean> {
  let stored: string | null = null;
  try {
    stored = localStorage.getItem(HASH_KEY);
  } catch {
    return false;
  }
  if (!stored) return false;
  const hash = await sha256Hex(`meridian-keylock::${password}`);
  return hash === stored;
}

export function isKeyLockUnlocked(): boolean {
  try {
    const until = Number(localStorage.getItem(UNLOCK_UNTIL_KEY) || 0);
    return Date.now() < until;
  } catch {
    return false;
  }
}

export function unlockKeyLockSession(): void {
  try {
    localStorage.setItem(UNLOCK_UNTIL_KEY, String(Date.now() + KEYLOCK_SESSION_MS));
  } catch {
    // ignore
  }
}

export function lockKeyLockSession(): void {
  try {
    localStorage.removeItem(UNLOCK_UNTIL_KEY);
  } catch {
    // ignore
  }
}

export function remainingUnlockMs(): number {
  try {
    const until = Number(localStorage.getItem(UNLOCK_UNTIL_KEY) || 0);
    return Math.max(0, until - Date.now());
  } catch {
    return 0;
  }
}
