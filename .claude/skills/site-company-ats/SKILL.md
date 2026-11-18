---
name: site-company-ats
description: Playbook for company career sites and ATS (Workday, Oracle HCM, Greenhouse, Lever, SuccessFactors, iCIMS). Accounts, autofill clean-up, session timeouts, uploads, and confirming submission.
---

# Company career sites / ATS playbook

Site mechanics as last verified Nov 2026. When something here is wrong, follow `job-hunt-learning-loop`.

## Before opening any ATS application
- Confirm the job passes the filters using the JD **on this site** (it's the source of truth for experience and post date).
- If the candidate's rules say tailor for this company, the tailored PDF (`Name_Resume_<Company>.pdf`) must exist before you open the form.
- Accounts: Workday, Oracle and SuccessFactors need one account **per company**. The candidate creates it (password, email verification) using their professional email; check for typos in the signed-in email. Ask for all needed accounts in one message at the start of the run.

## General flow
1. One application at a time, end to end, while the candidate is reachable for captchas.
2. Upload the resume first (`file_upload`) where the site offers "Autofill with resume"; it saves typing.
3. **Then check every autofilled field.** Autofill is unreliable.
4. Fill all remaining fields from `standard-answers.md`, optional ones too. Voluntary disclosures: per their standard answers.
5. Untick talent-community / job-alert / SMS opt-ins unless they want them.
6. Submit. **Success signal:** a confirmation page ("Thank you for applying" / "Application submitted") and usually a confirmation email within minutes. Check Gmail before counting it.

## Per-ATS notes
- **Workday** (`*.myworkdayjobs.com`): sessions expire after ~30–60 min idle and wipe the form, so never pre-fill and park. "Autofill with Resume" mangles dates and skills; fix them. Multi-step: My Information → My Experience → Application Questions → Voluntary Disclosures → Review. Some companies show a post-submit "Complete Questionnaire" asking for an employee number; that's for ex-employees only, leave it.
- **Oracle HCM / Taleo** (`*.oraclecloud.com`): resume autofill can leave **Employer Name blank**, put "and gt" in place of ">", and **copy the Projects section into the last job's achievements**. Open and clean every experience entry.
- **Greenhouse** (`boards.greenhouse.io`, `job-boards.greenhouse.io`) and **Lever** (`jobs.lever.co`): usually no account; single page. Custom questions at the bottom; links fields want full URLs.
- **SuccessFactors / iCIMS / Rippling / Ashby / others:** follow the same general flow. Log the specifics in `site-notes.md` the first time.
- **Cloudflare "Verify you are human" / captchas:** the candidate ticks it. Ask, then continue.

## Known quirks
- Some company sites redirect to a different ATS domain mid-flow; the login there may be separate.
- If a form needs something only the candidate can provide (e.g. document scans, ID numbers), add it to Pending with the exact field name. Never store ID numbers in the candidate files.
