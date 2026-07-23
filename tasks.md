# Tasks - Clipboard Chatbot Integration

- [ ] Task 1: Add custom event listener in `Timeline.tsx` for `meridian:send-chat`
  - Acceptance: Receiving `meridian:send-chat` event appends prompt to chat messages and triggers `executeTask(prompt)`.
  - Verify: Build check & event test.
  - Files: `meridian_frontend/src/views/Timeline.tsx`

- [ ] Task 2: Update `Clipboard.tsx` to route analysis to Chatbot and add Copy button
  - Acceptance: Clicking `Zap` calls `setActiveTab('timeline')` and dispatches `meridian:send-chat`. Hovering shows `title="Analyze in Chatbot"`. Copy button copies text with visual checkmark feedback.
  - Verify: Build check & manual interaction test.
  - Files: `meridian_frontend/src/views/Clipboard.tsx`

- [ ] Task 3: Verify frontend build with `npm run build`
  - Acceptance: Build finishes with 0 errors.
  - Verify: Run `npm run build` in `meridian_frontend`.
