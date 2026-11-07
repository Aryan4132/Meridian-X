# Meridian-X Chrome Extension Bridge

Connect your daily Google Chrome browser directly to Meridian-X local AI without any profile conflicts or re-authenticating your accounts.

## Features
- **Zero Profile Locking**: Automates your active tabs while your browser is running.
- **Your Accounts & Cookies**: Meridian can read and interact with your logged-in Google, YouTube, GitHub, Notion, or Jira tabs.
- **Bi-directional**: Agent can extract text, click buttons, submit inputs, and scroll smoothly.
- **Local & Private**: Communicates exclusively over `ws://127.0.0.1:4132/api/browser/extension` or `ws://127.0.0.1:8000/api/browser/extension`.

## Installation (30 Seconds)
1. Open Google Chrome.
2. In the URL bar, go to: `chrome://extensions/`
3. In the top right corner, toggle **Developer mode** to ON.
4. In the top left corner, click **Load unpacked**.
5. Select this directory:
   `c:\Users\aryan\OneDrive\Dokumen\Mini_Project\Meridian-X\meridian_extension`
6. Pin the **Meridian-X AI Bridge** icon to your toolbar.
7. The badge will show **ON** (green) whenever your Meridian-X backend is running.

