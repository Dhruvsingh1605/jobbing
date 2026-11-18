# Mistakes log — Dhruv Singh

Read this before every job-hunt run. When the candidate corrects anything, add a line here immediately (date, what went wrong, the rule from now on). The pre-filled entries below are pitfalls learned from earlier runs of this skill pack; keep them.

## Screening
- Portal experience ranges (LinkedIn, Naukri) are often wrong. Read the experience line in the full JD on the company's own page before applying or asking for a referral.
- "3+ years" and "3–5 years" mean minimum 3. Compare the minimum against the cap, never the maximum.
- Recommended / "jobs for you" lists show old postings. Check the real post date before applying.
- Don't apply to blocklisted companies even when the role looks perfect.

## Profiles on portals
- Write experience, project and award descriptions as bullet points, one per line, never paragraphs.
- Add every relevant experience, internships included, not only the current job.
- Don't overwrite a newer description the candidate wrote; merge, keeping their metrics.

## Application forms
- Fill every section, including optional ones (Languages, Skills, Summary).
- Never invent answers. If a question isn't in standard-answers.md, ask once, then save the answer there.
- Never trust ATS "Autofill with resume" output (Workday, Oracle HCM, etc.). Open and correct every field: employer names, dates, titles, education, and check that project text wasn't dumped into a job's description. Watch for mangled symbols (e.g. "and gt" where ">" should be) in autofilled text.
- Post-submit questionnaires asking for an employee number are for ex-employees only. Leave them.
- Check the signed-in email on each site matches the professional email (typos at sign-up are common).
- Name each tailored resume by company (`Name_Resume_<Company>.pdf`). Never refer to a resume file that hasn't been built yet.
- Big companies get a tailored resume built BEFORE opening the application.

## Browser
- Ask the candidate to log in to every site needed BEFORE starting, so the run isn't blocked halfway.
- Workday and similar ATS sessions expire after ~30–60 min idle and wipe the form. Do one application end to end, then the next; don't pre-fill many and park them.
- All browser work in ONE agent and one tab group. Parallel browser subagents orphan tabs where the candidate signed in.
- Close every tab Claude opened as soon as it's done with it; never close a tab the candidate is using.
- Only captchas, OTPs, "verify you are human" and Google sign-in pop-ups need the candidate. Resume uploads can be done with the file-upload tool.

## Email
- Never send terse, mass-mail-style bullet dumps. Every email is personal: name, where the post was seen, a 2–3 sentence pitch tied to their company/role, a polite ask, thanks, proper signature.
- Never paste Gmail "google.com/url?q=" redirect links; use clean URLs.
- Check Gmail before claiming a reply is pending or not sent.
- When an email should carry the resume, the draft must contain the PDF attachment.

## Candidate-specific corrections
- <YYYY-MM-DD>: <what happened> → <rule from now on>
- 2026-11-18: Base resume was rebuilt in LaTeX (9pt extarticle, 0.4in top/bottom margins) and fits exactly 1 page. page_fill.py measures from the full page edge, so with a 0.4in bottom margin the best possible reading is about 95-96%; treat 94%+ with the text area full as a PASS, and never shrink margins below 0.4in to chase 97%. → For one-page tailoring, check `pages=1` first, then fill >= 94%.
- 2026-11-18: LawYer is local only → never call it deployed, live or production. The "voice-calling agent" bullet at Timble was added by Dhruv's own description; no metrics, so do not invent any.
- 2026-11-18: In .tex files, write with the Write/Edit tools, not shell heredocs (they collapsed the double backslashes and broke the build).
