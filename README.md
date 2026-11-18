# Job Hunt Skill Pack for Claude

Automates your job search with Claude: build and tailor resumes, set up job-portal profiles, find and screen jobs, apply, send cold emails and referral requests, and follow up. It learns from your corrections as you go.

Everything runs in **your** Chrome and **your** Gmail. Claude never sees your passwords: you log in, and Claude does the clicking and typing.

## What's inside (16 skills)

| # | Skill | What it does |
|---|---|---|
| 0 | `job-hunt-start` | Index and router. Say anything job-related and it picks the right skill |
| 1 | `job-hunt-onboarding` | One-time setup: your data, criteria, resume, logins. Creates your candidate files |
| 2 | `job-hunt-learning-loop` | Records every correction so mistakes never repeat |
| 3 | `resume-builder` | Tailors your resume to a JD in your layout, checks page fill, ATS keyword audit |
| 4 | `portal-profile-setup` | Creates and completes portal profiles to 100% |
| 5 | `job-search-screening` | Finds fresh jobs and filters them by your criteria |
| 6 | `job-apply-runner` | Applies in batches, end to end, and confirms each one |
| 7 | `cold-email-referrals` | Hiring-post emails, referral requests, recruiter replies |
| 8 | `followup-tracker` | Tracker, reply checks, follow-up drafts, optional daily scheduled check |
| 9–15 | `site-linkedin`, `site-naukri`, `site-instahyre`, `site-hirist`, `site-foundit`, `site-yc-startups`, `site-company-ats` | Per-site playbooks: search URLs, apply steps, how to confirm, known quirks |

## Setup (about 30 minutes, once)

1. **Claude plan:** Pro or higher recommended, since applying runs use a lot of messages.
2. **Turn on code execution:** Settings → Capabilities → "Code execution and file creation" (may be called "Create and edit files").
3. **Upload the skills:** go to Customize → Skills → "+" → Create skill → Upload a skill. Upload **each zip in `zips/`** (one per skill). Keep them all toggled on.
4. **Install Claude in Chrome** (the browser extension), sign in, and use it in the Chrome profile you'll job-hunt from.
5. **Connect Gmail** in Claude's connectors (needed for emails, attachments and follow-ups).
6. **Create a Project** in Claude called "Job Hunt". Do all job-hunt chats inside it, because your candidate files live there.
7. In that Project, start a chat and say: **"Set me up for job hunting"**. Have ready: your resume, your LinkedIn URL (or LinkedIn profile PDF), project write-ups, and your phone for OTPs.

Onboarding asks about **your own** criteria (experience cap, salary floor, company size, locations, companies to avoid, how much Claude may do without asking) and builds your resume in **your** preferred layout.

## Daily use (just say it in the Project)
- "Apply to 30 jobs today"
- "Tailor my resume for this JD: <paste/link>"
- "Complete my Naukri profile"
- "Find LinkedIn hiring posts and email them"
- "Ask for referrals at <company>"
- "Any replies? Draft follow-ups"
- "Do the full daily run"

## Your files (created by onboarding)
`candidate-profile.md`, `job-preferences.md`, `standard-answers.md`, `mistakes-log.md`, `applications-tracker.md`, `site-notes.md`, plus your base resume. You can open and edit them any time in the Project.

## What you still do yourself
- Logins, OTPs, captchas, "verify you are human", Google sign-in pop-ups.
- Approving emails and LinkedIn messages (unless you tell Claude it can send).
- Profile photos.

## When something goes wrong
Just correct Claude in plain words ("that job needed 5 years, why did you apply?"). It logs the rule and follows it from then on. If a site changed and a site skill is out of date, Claude will offer an updated skill you can re-upload. Please share it back so everyone's pack gets better.

## Honest-use notes
- Claude applies only with facts from your files. No invented skills or numbers.
- Respect each site's terms and limits. Don't use this to mass-spam recruiters; every email is written to a specific person and role.
