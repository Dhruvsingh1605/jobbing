---
name: portal-profile-setup
description: Creates or completes the candidate's profile on job portals (LinkedIn, Naukri, Instahyre, Hirist, Foundit, YC) from their files, to 100%, with bullet descriptions and the right resume.
---

# Portal profile setup and updates

Use for "set up my profile on X", "complete my Foundit profile", "update all portals with my new job/resume".

## Before you start
- Read `candidate-profile.md`, `standard-answers.md`, `job-preferences.md`, `mistakes-log.md`, `site-notes.md`. Missing → `job-hunt-onboarding`.
- `job-hunt-learning-loop` applies throughout.
- Account creation: the candidate signs up and logs in themselves (passwords, OTPs, Google sign-in are theirs). Claude fills everything after that. Before filling, check the signed-in email matches their professional email.

## Steps per portal
1. Open the site skill (`site-<name>`) for that portal's section list and quirks.
2. Read the whole profile page first (get_page_text) and list what's filled, what's missing and the completion %.
3. Fill top to bottom, saving each section before the next:
   - **Headline / title:** their current title exactly as in the profile (latest title only).
   - **Summary:** 3–5 lines, role + years + 2 strongest results + target roles. Keyword-rich for their target roles.
   - **Experience:** EVERY relevant job including internships. Descriptions as bullet points, one per line, 3–6 bullets, each with a metric. If the site has an existing description the candidate wrote, merge; never drop their metrics.
   - **Projects, awards, publications, certifications:** all of them, as bullets. If a site has no publications section, put papers under awards/accomplishments.
   - **Skills:** fill every slot, Confirmed bucket first, ordered by their target roles' JD frequency. Limited-bucket skills only if slots remain. Never "Never claim" skills.
   - **Preferences:** salary, notice, locations, work mode, roles from `standard-answers.md` / `job-preferences.md`.
   - **Personal details, languages, links:** fill all.
   - **Resume upload:** their latest base resume (`file_upload`), named `Firstname_Lastname_Resume.pdf`.
   - **Privacy:** if the site can hide the profile from their current employer, ask once whether they want that.
   - Turn off marketing/WhatsApp alerts if they asked to.
4. Re-read the page and confirm each section saved. Report the completion %.
5. Record in `site-notes.md`: account email, resume uploaded (name + date), anything the site couldn't take.

## Updating all portals (new job, promotion, new resume)
Update `candidate-profile.md` first, then go portal by portal in `job-preferences.md` order: title, current job entry, summary, skills, resume. Keep a checklist in the task list.

## Things only the candidate can do
Profile photo, OTPs, captchas, salary figures you don't have (some sites won't save an experience entry without it). Batch these into one message at the end.
