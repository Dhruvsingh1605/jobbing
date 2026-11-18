# Job-hunt agent (Claude Code project)

Skills live in `.claude/skills/` (router: `job-hunt-start`). They were written for claude.ai Projects, so use this mapping:

- **Candidate files** live in `candidate/` (candidate-profile, job-preferences, standard-answers, mistakes-log, applications-tracker, site-notes, plus the base resume). Skills say "Project knowledge" or `project_read`/`project_write`: read and edit these local files instead. Skills say `SendUserFile`: save the file under `candidate/output/` and give the path.
- **Skill paths:** `scripts/page_fill.py` and `scripts/ats_scan.py` are in `.claude/skills/resume-builder/`. Run them with `venv\Scripts\python.exe -I` (has numpy + Pillow). `pdflatex`, `pdftotext`, `pdfinfo` and `pdftoppm` are installed (MiKTeX, Poppler); refresh PATH in a fresh shell if they aren't found.
- **Browser:** the skills assume Claude in Chrome tools. If no browser tools are connected, say so and stop browser steps; never fake them.
- **Gmail:** needs the claude.ai Gmail connector authorized. Drafts only unless `candidate/job-preferences.md` says sending is allowed.
- **Scheduling:** `followup-tracker`'s daily check uses the schedule/cron tools.
- `propose_skills` doesn't exist here: when the learning loop wants a skill change, edit the file in `.claude/skills/` directly and say what changed.
- Address the user as Bhidu. Candidate data is private: never put it in web requests.
- Onboarding is not done yet: `candidate/` files are still blank templates. Run `job-hunt-onboarding` first.
