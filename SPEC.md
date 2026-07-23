# Spec: Clipboard AI Analysis Chatbot Integration

## Objective
Route clipboard item AI analysis directly into the main Chatbot interface (`Timeline` view) when clicking the `Zap` button, while adding explicit tooltips and copy controls to clipboard cards.

## Tech Stack
React, TypeScript, Lucide Icons, Vite, Custom Events, AppContext (`useApp`).

## Commands
- Build: `npm run build`
- Dev: `npm run dev`

## Boundaries
- Always: Ensure smooth tab switching to `timeline`, preserve full clipboard content, provide visual copy feedback.
- Ask first: Major layout refactors to `Timeline.tsx`.
- Never: Discard AI streaming responses.

## Success Criteria
1. Clicking `Zap` on a clipboard item switches active tab to `timeline`.
2. The clipboard content is dispatched as a prompt and streamed in the main Chatbot.
3. Tooltips (`title="Analyze in Chatbot"`, `title="Copy to clipboard"`) are visible on hover.
4. Clicking Copy copies item text to system clipboard with a temporary checkmark indicator.
