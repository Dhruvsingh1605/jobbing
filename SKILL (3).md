---
name: site-linkedin
description: LinkedIn playbook for the job-hunt pack. Profile setup, job search URLs, Easy Apply form mechanics (shadow DOM), hiring-post search, referral messages, and how to confirm a submission.
---

# LinkedIn playbook

Site mechanics as last verified Nov 2026. Sites change: when something here is wrong, follow `job-hunt-learning-loop` (log it in `site-notes.md`, propose a fix to this skill).

## Profile
- URL: `https://www.linkedin.com/in/me/`. Sections: headline, About, Experience (each with bullet descriptions), Skills (up to 50; pin top 3 for target roles), Projects, Publications, Honors, Languages, Featured.
- Open to Work: ask whether they want it recruiter-only (usually yes if currently employed).
- Easy Apply resumes live at Settings → Data privacy → Job application settings. Check which resume is default; upload the latest with `file_upload` if needed and record it in `site-notes.md`.
- The account email may differ from the professional email. That's fine for Easy Apply; confirmations go to the LinkedIn account email.

## Job search
`https://www.linkedin.com/jobs/search/?keywords=<ROLE>&location=<COUNTRY>&f_AL=true&f_TPR=r604800&sortBy=DD`
- `f_AL=true` Easy Apply only (drop it to include company-site jobs) · `f_TPR=r604800` past week (`r86400` = 24 h) · `sortBy=DD` newest
- `f_E=` experience levels, comma-joined (`%2C`): 1 intern, 2 entry, 3 associate, 4 mid-senior, 5 director
- `f_WT=` 1 onsite, 2 remote, 3 hybrid
- The card's experience/posted info is a hint only. "Reposted" means an old job. Open the full JD (and the company career page for big companies) before applying.

Extract cards fast (run on the results page, scroll the list first):
```js
[...document.querySelectorAll('li[data-occludable-job-id]')].map(li=>({id:li.dataset.occludableJobId,
 text:li.innerText.replace(/\s+/g,' ').slice(0,220)}))
```
Job page: `https://www.linkedin.com/jobs/view/<id>/`

## Easy Apply
1. Click "Easy Apply". The modal often renders inside a shadow root at `#interop-outlet`. If `document.querySelector` finds nothing, search shadow roots recursively:
```js
function deepAll(sel, root=document){const out=[...root.querySelectorAll(sel)];
 root.querySelectorAll('*').forEach(e=>{if(e.shadowRoot) out.push(...deepAll(sel,e.shadowRoot))});return out}
deepAll('input,select,textarea,button').map(e=>[e.tagName,e.name||e.id,e.getAttribute('aria-label')||e.innerText?.trim().slice(0,40)])
```
2. Step through pages: contact info → resume (pick the right one, or upload) → questions → review.
3. Questions: answer from `standard-answers.md`. Numeric fields take numbers only ("11", not "11 LPA"); some notice-period fields are in months. LinkedIn pre-fills from earlier answers. **Review every pre-filled answer**; they may be stale or wrong for this job.
4. Long text: typing can drop characters. Set the value with the native setter, then read it back:
```js
function setVal(el,v){const p=el.tagName==='TEXTAREA'?HTMLTextAreaElement.prototype:HTMLInputElement.prototype;
 Object.getOwnPropertyDescriptor(p,'value').set.call(el,v);['input','change','blur'].forEach(t=>el.dispatchEvent(new Event(t,{bubbles:true})))}
```
5. Review page: **untick "Follow <company>"**. Submit.
6. **Success signal:** "Your application was sent" / "Application submitted" dialog, and the job shows "Applied". Then close the dialog.

## Hiring posts (email applications, referrals)
`https://www.linkedin.com/search/results/content/?keywords=<hiring ROLE resume>&datePosted=%22past-week%22&sortBy=%22date_posted%22`
- Broad keywords ("hiring ML engineer resume") return more than tight quoted phrases.
- Expand "…see more" before reading. Capture the email exactly; a wrong domain causes bounces (check the poster's other posts if one bounces).
- Then hand off to `cold-email-referrals`.

## Messages and referrals
- People search: `https://www.linkedin.com/search/results/people/?keywords=<company> <role>`; filter by current company.
- Connection notes are short (~200–300 chars). Send only per the candidate's approval rules.

## Known quirks
- Some actions may be blocked by a permission check in the browser tool; if a click is refused, tell the candidate and add the job to Pending.
- Easy Apply jobs sometimes have an external "Apply" instead; treat those with `site-company-ats`.
