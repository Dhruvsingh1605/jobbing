---
name: job-hunt-onboarding
description: First-time setup for the job-hunt skill pack. Interviews the candidate, collects resume and career data, sets up portal logins and connectors, and writes the candidate files every other skill reads.
---

# Job-hunt onboarding

Run this once per candidate, before any other job-hunt skill. Re-run any section later when something changes (new job, new resume, new filters).

Goal: by the end, the candidate has **seven candidate files** saved where every future chat can read them, plus Chrome, Gmail and each job portal ready to use.

**Every candidate is different.** Experience, roles, salary, filters, resume layout and approvals all come from THIS candidate's answers. The templates show example values in `<angle brackets>` only to show the format; never carry an example value into a candidate's file without them confirming it. If they say "you decide", propose a value, say why, and get a yes.

| File | What it holds | Template |
|---|---|---|
| `candidate-profile.md` | Identity, contact, links, education, every job and project with metrics, skills (confirmed / limited / never claim) | `templates/candidate-profile.md` |
| `job-preferences.md` | Target roles, filters (experience cap, salary floor, company size, locations, post age), blocklist, platforms in priority order | `templates/job-preferences.md` |
| `standard-answers.md` | Ready answers for every routine form question, plus email/message style rules | `templates/standard-answers.md` |
| `mistakes-log.md` | Every correction the candidate makes, so it never repeats. Starts with the pack's known pitfalls | `templates/mistakes-log.md` |
| `applications-tracker.md` | Every application, email and referral with status and follow-up dates | `templates/applications-tracker.md` |
| `site-notes.md` | Per-site facts for this candidate (account email, which resume is uploaded, quirks learned on their runs) | `templates/site-notes.md` |
| `base-resume` (.tex, .docx or .pdf) | The candidate's master resume, in THEIR chosen layout; the base for all tailoring | (their own file) |

## Where the files live

Pick the first option that works and tell the candidate which one you used:
1. **Claude Project (recommended).** Ask the candidate to create a Project called "Job Hunt" and run every job-hunt chat inside it. If the Projects tool is available, save the files with `project_write`. If not, build the files, send them with SendUserFile, and ask the candidate to add them to the Project's knowledge.
2. **No Project:** send the files and tell the candidate to attach them at the start of each job-hunt chat.

Never keep the candidate's data only in this conversation.

## Step 1 — Explain the plan (one short message)

Say what onboarding covers (about 20–30 minutes): data collection, resume, accounts and logins, preferences, then a test run. Ask them to have ready: current resume, LinkedIn URL, any project write-ups, and their phone for OTPs.

## Step 2 — Collect career data

Ask for files first, questions second:
- Ask them to attach: latest resume (any format), older resumes, LinkedIn profile PDF (LinkedIn → profile → More → Save to PDF), project READMEs, papers, certificates, cover letters.
- Read everything, fill `candidate-profile.md` from the files, then ask only about gaps. Ask in batches with AskUserQuestion where the answer is a choice, plain text otherwise.

Must-have fields (ask until filled):
- Full name, phone, professional email (the one they'll use for all portals), current city, full postal address (forms ask), date of birth and gender (forms ask; optional if they prefer not), nationality/passport yes-no.
- Links: LinkedIn, GitHub, portfolio, papers (DOI/URL).
- Education: degree, branch, college, start/end month-year, grade/CGPA, roll number if forms ask, 10th/12th % (Indian forms often ask).
- Every job and internship: title, company, one-line company descriptor, location, start/end, work mode, and 3–8 bullet-level achievements with numbers.
- For each project: what it is, their role (primary builder vs contributor), stack, metric, link.
- Awards, publications, patents, certifications, languages spoken (with fluency).
- Experience numbers to state: full-time years, years including internships.
- Current CTC, expected CTC, notice period, earliest joining (what counts as "immediate").

**Skills honesty pass (critical).** Go through every skill/tool from their resume and JD keywords for their target roles. Put each into one of three buckets in `candidate-profile.md`:
- Confirmed hands-on: can be in bullets and answers.
- Limited: Skills section only, never in bullets.
- Never claim: not used. Never appears anywhere; prepare an honest interview answer instead.
Ask about anything ambiguous. Never move a skill up a bucket without the candidate saying so.

## Step 3 — Preferences and filters

Fill `job-preferences.md` by asking (use AskUserQuestion with options where possible):
- Target roles and role families (and adjacent roles they'd accept).
- Experience cap: the most years a JD's **minimum** may ask for (e.g. someone with 2 years may say "2–3 OK, 3+ skip"; someone with 6 may say "up to 7"). Ask; if they're unsure, suggest full-time years + 1.
- Seniority: which titles are OK (e.g. SDE II, Senior, Lead) and which are too junior/senior.
- Salary floor (and preferred), separately for remote / hybrid / onsite if they differ.
- Company filter: minimum employee count, funded startups OK?, companies or company types to never apply to (e.g. known low payers, current employer, ex-employers).
- Locations and work modes; open to relocation where; global remote only if open to hiring from their country?
- Max post age (default 7 days).
- Platforms to use, in priority order (see the list in `templates/job-preferences.md`).
- Daily/weekly targets (e.g. 30 applications a run).
- Approval level: may Claude submit applications without asking? Send emails without asking? (Default: applications yes, emails and LinkedIn messages only after approval.)

## Step 4 — Standard answers

Fill `standard-answers.md`. Pre-fill from the profile, then confirm the yes/no block in one batch. The point is that Claude never stops mid-application to ask a routine question again. Any question not covered later gets asked once, answered, and **added to this file**.

## Step 5 — Resume (their layout, their rules)

Ask (AskUserQuestion):
- **Layout:** keep their current resume's look (Claude recreates it in LaTeX, or keeps editing their .docx), or use the pack's plain ATS template (`resume-builder/assets/resume_template.tex`), or another resume they like (they attach it).
- **Length:** one page (default for under ~8 years' experience) or two.
- **Sections and order:** e.g. Summary yes/no, Projects before or after Experience, Publications, Achievements.
- **Tailoring level:** tailor for every application, only for big companies, or one resume per role family (e.g. "ML Engineer", "Data Scientist").
- **Their own style rules** (e.g. "no client names", "always show the award as Winner", font, colors). Save these in `job-preferences.md` under "Resume rules".

Then build the base with `resume-builder`, get their approval, and save it as `base-resume`. Agree the file-naming pattern: `Firstname_Lastname_Resume_<Company>.pdf`.

## Step 6 — Tools, connectors and logins

Walk through this checklist and confirm each item:
1. **Code execution / file creation** on in Claude settings (needed for skills).
2. **Claude in Chrome** extension installed, signed in, and running in the Chrome profile they use for job hunting. Claude applies through their real Chrome sessions.
3. **Gmail connector** connected (for cold emails, drafts with attachments, confirmation checks, follow-ups). Google Drive optional.
4. **Portal accounts:** for each platform in `job-preferences.md`, the candidate creates the account (or confirms it exists) and **logs in themselves in that Chrome profile**. Check, in the browser, that each site shows them signed in with the right email; typos in sign-up emails are common.
5. **Passwords and OTPs:** Claude never asks for, stores or types passwords. OTPs, captchas, "verify you are human" checks and Google sign-in pop-ups are done by the candidate; Claude pauses and asks.
6. Recommend turning off "follow company" and marketing emails where the portal allows.

Record in `job-preferences.md` which portals are live and logged in, and start `site-notes.md` with each site's account email and which resume is uploaded there.

## Step 7 — Save and test

- Save all files (see "Where the files live"). Show a short summary: what's filled, what's missing (bold), and next steps.
- Offer a test: `portal-profile-setup` on one portal, then `job-apply-portals` for 3 jobs, so they see the flow end to end.

## Learning loop starts here
Tell the candidate in one line: "Whenever I get something wrong, just correct me. I log it and won't repeat it." From then on, `job-hunt-learning-loop` applies on every run.

## Rules for this skill
- Use only what the candidate gave you. Never invent metrics, dates or skills. Mark unknowns as **TODO** and list them at the end.
- Do not store government ID numbers, bank or card numbers, or passwords in any file. "Has PAN: Yes" is fine; the number is not.
- Keep questions batched and short; don't re-ask what the files already answer.
