---
name: site-hirist
description: Hirist.tech playbook for the job-hunt pack. Login, profile, search, apply with the salary pop-up, and confirming via the instant Application Successful email.
---

# Hirist playbook

Site mechanics as last verified Nov 2026. When something here is wrong, follow `job-hunt-learning-loop`.

## Account and profile
- Needs its own login (it may send you through a separate sign-in page). The candidate logs in once in their Chrome before the run.
- Profile: resume upload, experience, skills, salary, notice, preferred locations. Same rules as other portals: bullets, everything filled.

## Search
- Job URLs look like `https://www.hirist.tech/j/<slug>-<id>`. Use the site search with role keywords and the experience filter; sort by newest.
- Many listings are from recruitment agencies; judge by the end employer, or skip if it isn't named (per their preferences).

## Apply
1. Click "Apply".
2. A pop-up may ask for annual salary / expected salary / notice. Fill from `standard-answers.md`. If it offers "Finish this later" for optional profile steps, the application still goes through once required fields are done.
3. **Success signal:** Hirist emails **"Application Successful" within seconds**. Check Gmail (`from:hirist.tech newer_than:1d`). No email = not applied, even if the page looks done; the job page also still shows "Apply".

## Known quirks
- Agency posts often hide office days (e.g. 6-day office) in the JD body; read it fully.
