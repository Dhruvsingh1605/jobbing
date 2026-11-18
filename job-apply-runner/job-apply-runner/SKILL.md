---
name: job-apply-runner
description: Runs a batch of job applications end to end in the candidate's Chrome: takes screened jobs, tailors resumes when needed, fills forms from standard answers, confirms each, updates tracker.
---

# Job apply runner

Use when the candidate says "apply to N jobs", "do today's run", or hands over a list of links.

## Before you start (in this order)
1. Read all candidate files: `candidate-profile.md`, `job-preferences.md`, `standard-answers.md`, `mistakes-log.md`, `site-notes.md`, `applications-tracker.md`. Missing → run `job-hunt-onboarding`.
2. `job-hunt-learning-loop` applies throughout.
3. Load the Claude in Chrome tools in one go (tabs, navigate, computer, read_page, find, form_input, get_page_text, javascript_tool, file_upload).
4. Create a task list: one item per platform + "update tracker" + "verify submissions".
5. **Login check up front.** Open each platform you'll use and confirm it shows the candidate signed in with the right email. Ask them to log in to anything that isn't, all in ONE message, before starting. Don't discover login walls halfway.

## The loop
1. Get the shortlist from `job-search-screening` (or screen the links they gave you with the same filters).
2. For each job, **one at a time, end to end**:
   - Open the matching site skill (`site-linkedin`, `site-naukri`, `site-instahyre`, `site-hirist`, `site-foundit`, `site-yc-startups`, `site-company-ats`) and follow its apply steps.
   - **Resume:** if their preferences say tailor for this company type (e.g. big companies), build it with `resume-builder` BEFORE opening the form, named `Name_Resume_<Company>.pdf`. Otherwise use the resume already on the site, or their base resume.
   - Upload with the `file_upload` tool from the working directory. Ask the candidate only if the upload tool fails.
   - **Answer from `standard-answers.md`.** Fill every field, optional ones too. Skills fields: the JD's keywords that are in their Confirmed bucket.
   - **New question not covered:** if it's a simple fact you can derive truthfully from the files, answer and log it via the learning loop; otherwise ask the candidate (batch questions if several jobs are waiting). Never invent.
   - **Never state a negative.** If the only honest answer fails a hard requirement, skip the job and log why.
   - Untick "follow company", job alerts and marketing opt-ins before submitting.
   - **Confirm the submission** using the site skill's success signal (confirmation text, "Applied" state, network response, or confirmation email). Not confirmed = not counted.
   - Add a row to `applications-tracker.md` immediately.
   - Close the tab.
3. **Blockers** (captcha, OTP, "verify you are human", an account to create, a question only they can answer): if the candidate is present, ask right away. If they're away or asked for no interruptions, add the job to the tracker's "Pending" table and move on.

## Hard rules
- All browser work in this one conversation/agent. Never split browser work across parallel subagents (tabs get orphaned). Subagents are fine for web research only.
- Never close a tab the candidate is using or has signed in on.
- ATS forms expire when idle (Workday ~30–60 min): never pre-fill several and park them.
- Never trust "autofill from resume" output; check every field.
- Respect platform limits (e.g. YC 5/week) and pick the best-fit jobs for limited slots.
- Never type passwords. Never bypass captchas.

## Report (short)
- One line: applied N (by platform), pending M, skipped K.
- Table of applied jobs: Platform · Company · Role · Exp asked · Salary · Mode · Posted · Resume used.
- Pending items with the exact action needed from the candidate.
- What the learning loop recorded this run.
