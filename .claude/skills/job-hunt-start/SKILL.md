---
name: job-hunt-start
description: Entry point and index for the job-hunt skill pack. Use for any job-search request (apply, resume, portals, cold email, follow-ups); routes to the right skill and checks onboarding is done.
---

# Job hunt: start here

This pack automates a job search end to end in the candidate's own Chrome and Gmail: onboarding → resume → portal profiles → search → apply → cold email/referrals → follow-ups, with a learning loop so mistakes don't repeat.

## Step 0: is the candidate onboarded?
Look for the candidate files (Project knowledge, attached files, or memory): `candidate-profile.md`, `job-preferences.md`, `standard-answers.md`, `mistakes-log.md`, `applications-tracker.md`, `site-notes.md`, and a base resume.
- Missing or mostly empty → run **job-hunt-onboarding** first. Say so in one line and start.
- Present → read `mistakes-log.md` first, then route.

## Routing

| The candidate says… | Use |
|---|---|
| "set me up", first time, "update my details/criteria" | `job-hunt-onboarding` |
| "make/tailor my resume for this JD", "cover letter", "will it pass ATS" | `resume-builder` |
| "create/complete/update my profile on <site>" | `portal-profile-setup` + `site-<name>` |
| "find jobs", "what's out there" | `job-search-screening` + site skills |
| "apply to N jobs", "do today's run", a list of job links | `job-apply-runner` (uses search, resume and site skills) |
| "email this recruiter", "LinkedIn hiring posts", "ask for referrals", "reply to this recruiter" | `cold-email-referrals` |
| "any replies?", "follow up", "tracker", "set a daily check" | `followup-tracker` |
| any correction or new answer, on every run | `job-hunt-learning-loop` |

Site skills: `site-linkedin`, `site-naukri`, `site-instahyre`, `site-hirist`, `site-foundit`, `site-yc-startups`, `site-company-ats` (Workday, Oracle, Greenhouse, Lever…).

## Full daily run (when they say "do everything")
1. `followup-tracker`: replies and follow-ups first (fast, high value).
2. `job-search-screening` across their platforms.
3. `job-apply-runner` on the shortlist (tailored resumes where their rules say).
4. `cold-email-referrals` for email posts and referral targets found during search.
5. Update `applications-tracker.md`; short report; learning-loop summary.

## Rules that apply to every skill in the pack
- **Their criteria, not defaults.** Filters, answers, resume layout and approvals come from the candidate files. Never assume another candidate's values.
- **Truthful always.** Only skills and numbers from `candidate-profile.md`; skills obey the honesty buckets.
- **Sales framing.** Never state a negative; if the honest answer fails a requirement, skip the job.
- **Their accounts.** Claude never handles passwords; the candidate does logins, OTPs and captchas.
- **Approvals.** Applications vs emails/messages: follow `job-preferences.md` (default: apply freely, draft emails for approval).
- **Browser hygiene.** One browser agent, new tabs, close what you opened, never close their tabs.
- **Learn.** Every correction goes to the candidate files immediately (`job-hunt-learning-loop`).
- Keep reports short: counts, a table, what's pending for them.
