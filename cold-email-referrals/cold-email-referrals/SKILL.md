---
name: cold-email-referrals
description: Finds LinkedIn/X hiring posts that ask for CVs by email, finds referral contacts, and writes personal cold emails, referral requests and recruiter replies with the right tailored resume attached.
---

# Cold emails, hiring posts, referrals and recruiter replies

## Before you start
- Read `candidate-profile.md`, `job-preferences.md`, `standard-answers.md`, `mistakes-log.md`, `applications-tracker.md`. Missing → `job-hunt-onboarding`.
- `job-hunt-learning-loop` applies throughout.
- Needs the Gmail connector (drafts, attachments, sending, checking replies) and Claude in Chrome (LinkedIn).
- **Approval:** follow `job-preferences.md`. Default: Claude drafts, the candidate approves, then Claude sends. Never send a LinkedIn message or email without approval unless they've said that's fine.

## A. Hiring posts that ask for email applications
1. Search posts (see `site-linkedin` → "Hiring posts"): role keywords + "hiring" / "share your resume" / "send CV", past week, newest first. Optionally X/Twitter with the same keywords.
2. Screen each post with `job-search-screening` filters (company size by the end employer, experience, location, post date).
3. For each passing post, note: poster's name and title, company, role, the email address exactly as written, any subject line they asked for, and the post link.
4. Build or pick the resume (`resume-builder`), named `Name_Resume_<Company>.pdf`.
5. Write the email (rules below), create a **Gmail draft with the PDF attached**, show the candidate a one-line list of drafts, send after approval.
6. Bounces: check the inbox a few minutes after sending. If one bounces, look for the right address (the poster's other posts, company domain format) and resend.

## B. Referral requests
1. For a target job, find 3–5 people at the company on LinkedIn: same team or role family, alumni of the candidate's college, or second-degree connections first.
2. First message (connection note ≤300 chars, or InMail/DM): who they are in one line, the job link/ID, one proof point, a polite ask for a referral. No resume dump.
3. If they agree, send what they ask for (resume, job ID, email) the same day.
4. Read the full JD on the company page BEFORE asking anyone (never ask for a referral to a job that fails the filters).

## C. Inbound recruiters
- Reply briefly and positively; don't re-pitch. LinkedIn: 1–2 sentences. Email: thanks, interest, one line of current role/stack, and any details they asked for (CTC, notice, location) from `standard-answers.md`.
- If they asked for a resume, tailor it to what their message says and attach it.

## Email writing rules (hard)
- Personal, courteous and specific. Never a terse mass-mail ("Hi, applying for X. Resume attached." + bullets).
- Structure: greeting by name ("Dear <Name>," or "Dear <Company> Hiring Team,") → where you saw the post/role and which role → 2–3 sentences in flowing prose on why they fit THIS role, with 2–3 real achievements matched to the JD → polite ask (consideration / a short call) → "Thank you for your time and consideration." → sign-off.
- Signature: name, current title and company, phone, LinkedIn and GitHub as clean links. Never paste `google.com/url?q=` redirect links.
- Subject: what the post asked for; otherwise `Application: <Role> — <Full Name>`.
- Length: 120–200 words. Match the tone of the thread when replying (casual if they were casual).
- Truthful, no negatives, only Confirmed skills, the candidate's framing rules (`candidate-profile.md`).
- The draft must contain the PDF attachment whenever a resume is mentioned. If the connector rejects a large file, rebuild the PDF smaller (see `resume-builder` → fitting tricks) rather than handing the attaching back.

## After sending
Log each email/message in the tracker's "Emails and referrals" table with a follow-up due date (from their preferences; default 2 days). `followup-tracker` takes it from there.
