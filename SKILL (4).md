---
name: job-search-screening
description: Finds fresh jobs across the candidate's portals and LinkedIn hiring posts, then screens each against their own filters (experience, post age, salary, company size, location, blocklist).
---

# Job search and screening

## Before you start
- Read `job-preferences.md`, `candidate-profile.md`, `mistakes-log.md`, `site-notes.md` and `applications-tracker.md`. Missing → run `job-hunt-onboarding`.
- `job-hunt-learning-loop` applies throughout.
- Searching happens in the candidate's Chrome (Claude in Chrome). Load the browser tools once, work in new tabs, close each tab when done with it.

## 1. Build the search list
- Keywords: each target role title + 2–3 synonyms (e.g. "ML Engineer", "Applied AI Engineer", "GenAI Engineer"). Take them from `job-preferences.md`; don't add role families they didn't choose.
- Platforms: in the candidate's priority order. For each, open the matching **site skill** (`site-linkedin`, `site-naukri`, `site-instahyre`, `site-hirist`, `site-foundit`, `site-yc-startups`) for search URLs, filters and fast extraction snippets.
- Pull candidates in bulk with the site skill's extraction snippet (title, company, experience, salary, location, posted date, link), not one screenshot at a time.

## 2. Screen: every hard filter, in this order (cheapest first)
1. **Already applied / skipped?** Check `applications-tracker.md` and the site's "Applied" marker. Skip duplicates.
2. **Blocklist:** company or company type on the candidate's blocklist → skip.
3. **Post age:** originally posted within their max age. Use the real date (site skills say where to find it). "Reposted" = old.
4. **Experience:** compare the JD's **minimum** to their cap. Read it from the **full JD**, ideally on the company's own career page; portal summaries are often wrong.
5. **Salary** (if listed): top of the range must clear their floor for that work mode.
6. **Company size / funding:** check the LinkedIn company page ("N employees") or a quick web search. Recruiter/agency posts: judge by the end employer; skip if unknown.
7. **Location / mode / shift / contract:** per their preferences.
8. **Role fit:** title and the first third of the JD match their target roles; skip "AI" titles that are really support, sales or a different stack.
9. **Hard requirements vs honesty buckets:** if a must-have skill is in their "Never claim" bucket, skip (don't apply and hope).

Record every skip with its reason in the tracker's "Skipped" table. That stops re-checking the same job on the next run.

## 3. Output
- A ranked shortlist: best fit first, big/high-paying companies first. Columns: Platform · Company · Role · Exp asked · Salary · Mode/location · Posted · Link · Apply route (Easy Apply / portal / company ATS / email).
- Hand off to `job-apply-runner` (portals and ATS) or `cold-email-referrals` (email posts, referrals).

## Tips for speed
- Search all platforms first, screen in one pass, then apply. Don't alternate.
- Open the full JD only for jobs that pass filters 1–3 (cheap checks first).
- When a filter is ambiguous for a job (e.g. "2–5 yrs preferred, 3 required"), use the stricter reading unless the candidate's preferences say otherwise; if it comes up often, ask once and save the answer via the learning loop.
