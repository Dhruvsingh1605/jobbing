---
name: site-naukri
description: Naukri.com playbook for the job-hunt pack. Profile completion, search URLs, reading real post dates from job IDs, in-site apply with the chatbot questions, and confirming submissions.
---

# Naukri playbook

Site mechanics as last verified Nov 2026. When something here is wrong, follow `job-hunt-learning-loop`.

## Profile
- URL: `https://www.naukri.com/mnjuser/profile`. Sections: resume, resume headline, key skills, employment (each with description), education, IT skills, projects, profile summary, accomplishments (online profiles, work samples, publications, certifications), career profile (preferred roles, locations, salary), personal details, languages.
- Write employment and project descriptions as bullet points. Fill every section; profile strength affects recruiter search.
- Updating the profile (even re-saving the headline) bumps it in recruiter searches. Doing that on run days is worth it.

## Search
- Search URL pattern: `https://www.naukri.com/<role-slug>-jobs?k=<ROLE>&experience=<years>&jobAge=<days>` (e.g. `ml-engineer-jobs?k=ml%20engineer&experience=2&jobAge=7`). Add locations via the UI filters if the URL param doesn't stick.
- Recommended jobs: `https://www.naukri.com/mnjuser/recommendedjobs`. These lists include **old** postings; always check the date.
- **Real post date:** the job URL ends with a 12-digit job ID whose first 6 digits are DDMMYY (e.g. `...-021126500410` → 02 Nov 2026). Use it to enforce the post-age filter.
- The header "X–Y Yrs" can differ from the JD body; read the JD.

## Apply
1. On the job page, only plain **"Apply"** applies on Naukri. "Apply on company site" → treat with `site-company-ats` (or skip per their preferences).
2. Before clicking, untick "Follow <company> as you apply" (an `i[role=checkbox]` near the button) if present.
3. A side-panel **chatbot** may ask questions (notice period, CTC, experience in X, location). Answer from `standard-answers.md`; type numbers plainly; pick the closest chip option.
4. **Success signal:** the page shows "Applied" / "You have successfully applied", and the network request to `/myapply/saveApply` returns 200 (`multiApplyResp`). If unsure, check `https://www.naukri.com/myapply/historypage`.
5. Naukri sends no email per application. One summary email ("You applied for N jobs on <date>") arrives the next morning. Don't treat a missing email as failure.

## Known quirks
- Applications can't be withdrawn. Screen carefully first.
- The chatbot sometimes repeats a question if the answer format is wrong (e.g. text in a numeric field); re-answer with digits only.
- Hirist may redirect to a Naukri-style sign-in; see `site-hirist`.
