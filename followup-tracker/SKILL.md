---
name: followup-tracker
description: Keeps the applications tracker current, verifies submissions via portals and Gmail, drafts follow-ups for overdue replies, and can set a daily scheduled check that drafts but never sends.
---

# Follow-ups and tracking

## Before you start
- Read `applications-tracker.md`, `standard-answers.md`, `mistakes-log.md`, `job-preferences.md` (follow-up interval, approval rules).
- `job-hunt-learning-loop` applies throughout.

## 1. Verify what actually went through
Counts only include confirmed submissions. Cross-check:
- Portal "Applied" pages (site skills say where).
- Gmail confirmations: search e.g. `newer_than:2d (application OR applied OR "thank you for applying")`. Some sites email instantly (Hirist, most company ATS), some send a daily summary the next morning (Naukri), some never email (Instahyre); judge by the site's history page instead.
- Fix the tracker: anything unconfirmed goes back to Pending.

## 2. Check for replies
- Gmail: for every row in "Emails and referrals" and every application with a recruiter thread, open the thread. **Always check before saying something is pending or unsent.**
- LinkedIn messages (Chrome): read replies to referral requests and recruiter messages. Read only, unless the candidate approved sending.
- Update statuses: replied / interview / rejected / no reply N days.

## 3. Follow-ups
- No reply after the interval (default 2 days) and no follow-up in that window: draft a follow-up **in the same thread**. Same rules as `cold-email-referrals`: personal greeting, reference the earlier email and role, 2–3 sentence reminder of fit, polite ask, thanks, signature. Don't quote the old thread.
- A second follow-up at most, a week later. After that, mark it cold.
- Replies needing an answer (interview slots, CTC, documents): draft a reply using `standard-answers.md`.
- Send only per the candidate's approval rules. Default: drafts plus a short list, they say what to send.

## 4. Scheduled daily check (optional)
If they want it, create a **scheduled task** (use the session's scheduling tools) that runs daily at a time they choose. Its prompt must be standalone and include: where the candidate files live, steps 1–3 above, "create Gmail drafts only, never send", "LinkedIn read-only", the email writing rules, and "final reply = short list of Company/Person · status · what was drafted, ending with: reply in this chat with what to send". If it needs LinkedIn, the task must be allowed to use their computer (tell them how to turn that on in the task settings if it isn't).

## 5. Report
- One line of counts (applied this week, replies, interviews).
- Changes since last check, then drafts awaiting approval. Nothing changed → one line.
