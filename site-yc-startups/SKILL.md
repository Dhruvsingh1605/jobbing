---
name: site-yc-startups
description: YC Work at a Startup playbook for the job-hunt pack. Profile, reading jobs from page JSON, picking the best jobs for the 5-per-week limit, and writing the founder note.
---

# YC Work at a Startup playbook

Site mechanics as last verified Nov 2026. When something here is wrong, follow `job-hunt-learning-loop`.

## Profile
- workatastartup.com uses its own profile (experience, education, skills, links, "what you're looking for"). There's no resume file in the apply flow, so the profile IS the application. Fill it fully from `candidate-profile.md`, bullets with metrics.

## Limit
- **5 applications per week** across the platform. Check how many are left before starting, rank candidates, and spend slots on the best fits (role match, salary, funding stage). Record the reset day in `site-notes.md`.

## Search (fast)
- Companies directory, e.g. India engineering roles, newest first:
  `https://www.workatastartup.com/companies?jobType=fulltime&layout=list-compact&locations=IN&role=eng&sortBy=created_desc`
  (change `locations` / `role` per their preferences; `remote` options exist in the UI).
- Pages embed structured data. On a company or listing page:
```js
const d=JSON.parse(document.querySelector('[data-page]').getAttribute('data-page'));
const c=d.props.rawCompany||d.props.company; (c?.jobs||[]).map(j=>({title:j.title,salary:j.salaryRange||j.salary,
 loc:j.locations||j.location,exp:j.minExperience||j.experience,id:j.id}))
```
  This beats scraping the rendered HTML. If keys change, `Object.keys(d.props)` and log the new path in `site-notes.md`.

## Apply
1. Click "Apply" on the job.
2. Write a 4–6 sentence note to the founder: why this company (specific to what they build), the candidate's most relevant achievement with a number, one more proof point, availability. No negatives. Set long text with a native value setter and read it back.
3. Click Send. **Success signal:** the button changes to "Applied".
