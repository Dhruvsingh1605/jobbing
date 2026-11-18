---
name: resume-builder
description: Builds or tailors an ATS-optimised resume (and cover letter) for a JD in the candidate's own layout, from their files, then verifies page count and fill and runs a keyword audit.
---

# Resume builder (tailor, compile, verify, audit)

## Before you start
- Read the candidate files: `candidate-profile.md`, `job-preferences.md`, `mistakes-log.md`, and the base resume (Project knowledge, attached files, or memory). If they don't exist, stop and run `job-hunt-onboarding` first.
- Get the JD. If only a role title is given, web-search current postings for that title and build a keyword list from 3–5 of them.

## Workflow
1. **Plan first (unless the candidate said "just build it").** Send a short plan: sections, which jobs/projects go in, bullets per item, which JD keywords each bullet covers, what's being cut. Ask only questions the files can't answer.
2. **Build from the candidate's base, in their layout.** The "Resume rules" in `job-preferences.md` decide layout, length, section order and style; they override the defaults below.
   - Base is `.tex`: edit a copy.
   - Base is `.docx`: edit a copy with the docx skill, keeping their styles; convert to PDF with LibreOffice for checks.
   - Base is only a PDF: recreate its layout in LaTeX once (match margins, fonts, section order, header style), show it to the candidate, and save the approved `.tex` as the new base.
   - No resume, or they chose the pack template: use `assets/resume_template.tex`.
3. **Compile:** `pdflatex -interaction=nonstopmode file.tex` twice (hyperlinks).
4. **Verify (never skip):**
   - `python scripts/page_fill.py file.pdf --pages <N>` (N from their resume rules, default 1) → exact page count, last page ≥97% filled (≤3% empty at the bottom).
   - `pdftotext file.pdf -` and confirm the last expected words appear (content can clip silently at the page edge).
5. **Audit** with `scripts/ats_scan.py` (see below). Fix truthful misses, recompile, re-verify.
6. **Deliver** as `Firstname_Lastname_Resume_<Company>.pdf`. Send with SendUserFile. Save the tailored `.tex` too.

## Content rules (defaults: the candidate's resume rules win)
- Black and white, hyperlinks blue, standard headers (Summary, Experience, Projects, Skills, Education, Achievements) so ATS parsers read them.
- Newest and most relevant work gets the most space. Primary work (they built it) gets full bullets; secondary work gets one-liners at most.
- Each bullet: max 2 lines, ONE story: action → system/technique → metric. Never mix two projects in one bullet.
- Lead bullets with the technical substance the JD asks for, not product or client names. Client names: at most once, in one deployment bullet.
- Tailoring = reordering and rewriting bullets by JD priority using exact JD phrasing where it's true. Not keyword stuffing.
- Every included item must signal something the JD asks for. When short on space, cut by relevance; when filling space, add only JD-relevant content.
- When the candidate says remove something, remove it everywhere.
- Only skills from the **Confirmed** bucket in bullets; **Limited** skills only in the Skills line; **Never claim** skills nowhere.
- Follow framing notes in `candidate-profile.md` (e.g. award wording, names never to mention).
- Never invent numbers. Anything added that isn't in the files: list it at the end. Anything the candidate must fill: **bold** it and list under "Action required".

## ATS audit (`scripts/ats_scan.py`)
1. Build a keyword JSON from the JD, grouped: `hard_requirements`, `role_core`, `workflow_verbs`, `governance_quality`, `soft_collab` (soft skills are the most-missed group). Example in `assets/keywords_example.json`.
2. Run `python scripts/ats_scan.py file.pdf keywords.json` → per-group hits/misses and an overall %.
3. Classify each miss: (a) **truthfully addable** → add/reword using exact JD phrasing (e.g. spell out "Retrieval-Augmented Generation" next to "RAG"); (b) **genuine gap** → never add; give the candidate a one-line honest interview answer.
4. Fix, recompile, re-verify page fill, re-scan. Report before → after score in one line.

## Fitting tricks (LaTeX)
- Too long: tighten wording first, then cut the least JD-relevant bullet, then reduce `\vspace` between sections, then margins (not below 0.4in), then font 10.5pt → 10pt.
- Too short: add one JD-relevant bullet or project, or increase section spacing slightly.
- Gmail attachment payload is small for some tools: build with standard non-embedded fonts (e.g. `\usepackage{mathptmx}` and `\pdfmapfile{=pdftex_ndl14.map}`, no math symbols) to get a ~10–30 KB PDF when attaching via a connector.

## Cover letter (when asked)
Max one page, four short paragraphs (2–3 sentences each): why this role/company → strongest matching achievement → second proof point → polite close. Only facts from the files. Deliver as `Firstname_Lastname_CoverLetter_<Company>.pdf` (or a doc if they want to edit it).

## Learning loop
Any correction to a resume (wording, layout, a rule like "never mention X") goes through `job-hunt-learning-loop`: log it in `mistakes-log.md`, and if it's a standing style rule, add it to "Resume rules" in `job-preferences.md` so every future build follows it.
