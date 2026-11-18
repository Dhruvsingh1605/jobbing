---
name: job-hunt-learning-loop
description: Applies on every job-hunt run. Logs each correction, saves new form answers and site quirks to the candidate files, and turns repeated fixes into skill updates so mistakes never repeat.
---

# Job-hunt learning loop

The skill pack gets better for each candidate the more they use it. This skill says what to capture, where, and when.

## At the start of every run
Read `mistakes-log.md`, `standard-answers.md` and `site-notes.md` before doing anything else. Treat every line as a hard rule for this run.

## Capture triggers → where it goes

| What happened | Write to | Format |
|---|---|---|
| Candidate corrects something ("why did you…", "wrong", "don't do X") | `mistakes-log.md` → "Candidate-specific corrections" | `YYYY-MM-DD: what went wrong → rule from now on` |
| A form question wasn't covered and the candidate answered it | `standard-answers.md`, right section | The question pattern + their answer |
| A filter changes ("3+ is fine actually", "skip agencies") | `job-preferences.md` | Edit the filter in place; note the date |
| A resume style rule ("never put X", "projects first") | `job-preferences.md` → Resume rules | One line |
| A site behaved unexpectedly (new button, field rejects text, confirmation looks different, limit hit) | `site-notes.md` → that site → Learned | `date — quirk — what to do` |
| A fact about the candidate is new or changed (new metric, promotion, new skill confirmed) | `candidate-profile.md` | Edit in place; move skills between honesty buckets only when they say so |
| A company was found to be a low payer / bad fit and they want it skipped | `job-preferences.md` → Blocklist | Company name |

Rules:
- Write **immediately**, the moment it happens, not at the end of the run. If saving to the Project fails, keep a list and save at the end, and tell the candidate.
- Write the rule, not the story: "Read the full JD on the company page before applying" beats "Applied to JPMorgan by mistake".
- Never record a guess as a fact. Only what the candidate said or what you verified on the site.
- Before adding, check the file doesn't already say it; edit the existing line instead of duplicating.

## Saving the files
- Projects tool available: `project_read` the file, edit, `project_write` it back to the same path.
- Otherwise: update your working copy, and at the end of the run send the changed files with SendUserFile and ask the candidate to replace them in their Project or folder.

## Promoting a fix into the skills
When the same kind of fix shows up twice, or a site quirk would affect every user of that site:
1. Draft the change to the relevant skill (e.g. `site-naukri` → "Known quirks"; `job-apply-runner` → a rule).
2. If the `propose_skills` tool is available, propose it as an improvement (`edits` with old/new strings) so the candidate can save it with one click.
3. Otherwise produce the updated `SKILL.md`, zip the skill folder, send it, and tell them to re-upload it in Customize → Skills.
4. Suggest they share the improvement with whoever gave them the pack.

## End-of-run report (one block, short)
- Learned this run: 1–5 bullets of what was added and where.
- Needs the candidate: unanswered questions, blockers.
Don't list unchanged files.
