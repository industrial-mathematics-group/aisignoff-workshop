[← 3 Set up your repository](03-setup.md) · **4 IMGAgent** · [5 The report on GitHub Pages →](05-pages.md)

# 4 · IMGAgent

**IMGAgent** is the group's assistant on GitHub. You talk to it by writing `@IMGAgent` and a command in an
issue (or a comment in one). It answers questions about the files of a repository, and it writes declarations
into `SIGNOFF.toml` for you. It only answers people with write access to the repository, and it never changes
`main` by itself: whatever it changes comes as a pull request that you check and merge.

Pascal has installed it on your workshop repository. Check: **Settings → GitHub Apps** lists **IMGAgent**.

| Command | What happens |
|---|---|
| `@IMGAgent ask <folders>` and a question | Answers from the files in those folders. Changes nothing |
| `@IMGAgent signoff` and your words | Records how files were made and reviewed: a pull request that changes `SIGNOFF.toml` |
| `@IMGAgent update <folders> with <folders>` and a task | Edits files in the first folders, reading the others; opens a pull request |
| `@IMGAgent make docs` | Writes a documentation site in `docs/`; opens a pull request |
| `@IMGAgent help` | The list of commands |

Folders are written as paths, separated by commas: `notes`, `notes, analysis`, `analysis/fit_cooling.py`.
Not the whole repository (`.`), no wildcards. A command inside a grey code box or a quoted line is ignored.

## Exercise 1 · Ask your repository (5 min)

*Own repository:* ask about your own folders, and in exercise 2 declare the folders that were made differently
from the default.

1. **Issues → New issue** (choose **Blank issue** if GitHub offers forms). Title: `Questions about the coffee`.
2. As the text, write (the question may go on the next line):

   ```text
   @IMGAgent ask notes, analysis
   When does the coffee reach 60 °C, and how does the script compute that?
   ```

3. **Create.** After a minute IMGAgent answers with a comment, naming the files it used.
4. Ask more, as new **comments** in the same issue, for example:

   ```text
   @IMGAgent ask results, paper
   Does the abstract say the same as the results? List any number that differs.
   ```

   ```text
   @IMGAgent ask analysis, notes
   Which assumptions does the fit make that the lab notes say might not hold?
   ```

Answers come only from the folders you name, and are marked "An AI can be wrong". Try asking about a folder that
doesn't exist, or without a folder, to see the help it gives.

## Exercise 2 · Sign off files in your own words (10 min)

`SIGNOFF.toml` still says G0 · H2 · A0 for everything. Three folders were made differently
([HOW-THIS-WAS-MADE.md](sample-project/HOW-THIS-WAS-MADE.md)). Declare them, one at a time.

1. **Issues → New issue.** Title: `Signoff: analysis`. Text, in your own words, with your name, for example:

   ```text
   @IMGAgent signoff
   analysis/ was written by Claude Opus 5.5 from my instructions over a few rounds. I ran the
   script, checked that the numbers make sense and read the fitting function. No other AI
   reviewed it. Reviewer: Jane Doe.
   ```

2. IMGAgent answers with a table of what it understood (here: G2, Claude Opus 5.5, H1, A0), or asks what's
   missing. To answer or correct it, write a new comment that starts with `@IMGAgent signoff`.
3. A moment later a pull request appears: **Declare analysis/ (signoff request #…)**. Open it and look at
   **Files changed**: one new entry at the end of `SIGNOFF.toml`, with your words turned into levels.
   **Check every path, level and name: an AI read your words.**
4. In its description, **tick your human review** of that change (did it write down what you said? **H2**).
   The bot opened the pull request, but `Responsible person:` names you. Merge it.
5. Then the same for `results/` (an AI agent did it on its own; you checked the numbers) and for `paper/`
   (you wrote it, GPT Sol polished the English, you read every sentence). **Merge each pull request before you
   start the next**: they all add to the end of `SIGNOFF.toml`, and two open at once get in each other's way.

✅ **Check:** **Actions → File-signoff →** the newest run on `main`: the folder tree now shows `analysis` at
G2, `results` at G3, `paper` at G1.

Prefer a form? **Issues → New issue → Signoff: declare or attest files** asks the same questions as drop-downs,
without AI. The result is the same kind of pull request.

## Optional · Record a fresh-session check, A1 (5 min)

Open a **new** chat in an AI tool you use (no earlier conversation), paste `analysis/fit_cooling.py` and ask it
to look for mistakes, and to say how bad the worst one is (`none`, `trivial`, `minor`, `major`, `critical`).
Record what it found, in a new issue:

```text
@IMGAgent signoff
A fresh Claude session, without the original conversation, reviewed analysis/fit_cooling.py
as it is now and found nothing to fix. Please record it as an AI review, A1, findings: none.
```

That's an **attestation**: it raises the review of the file as it is now, and keeps how it was made. Every AI
review says what it found, A1 too: without the findings IMGAgent asks for them. You recorded this one yourself,
so it goes into `SIGNOFF.toml` like your other signoffs.

## Optional · An independent AI review as its own pull request, A2 (15 min)

A review by a **different** model, with a written report, is A2. It doesn't touch `SIGNOFF.toml`: it goes into
the **review folder** `reviews/`, in a pull request that adds only the report and a small record file.

1. **The review.** In a new chat with a different model than the one that wrote the file (the story says
   Claude wrote `analysis/`, so use ChatGPT, GPT Sol), paste `analysis/fit_cooling.py` and ask:

   ```text
   Review this script. Change nothing. Write a short report in Markdown: one line per finding, each with
   its severity (trivial, minor, major or critical), and at the top the most severe one ("none" if you
   found nothing).
   ```

2. **The commit it reviewed.** Open `analysis/fit_cooling.py` in your repository → **History** → the commit
   *Add the coffee cooling project* → the copy icon next to its short hash (it copies the full hash).
3. **The report.** **Add file → Create new file**, name `reviews/fit-cooling-review.md`, paste the report.
   **Commit changes… → Create a new branch … and start a pull request → Propose changes**, but **don't create the
   pull request yet**.
4. **The record file.** Switch to the new branch (the branch menu at the top left of the file list) → **Add
   file → Create new file**, name `reviews/fit-cooling-review.toml`, and fill in the hash and the worst finding:

   ```toml
   [[attestations]]
   commit = "paste the full hash here"
   path = "analysis/fit_cooling.py"
   AI-Review = "A2"
   AI-Reviewed-by = "GPT Sol (OpenAI), reviews/fit-cooling-review.md"
   AI-Review-Findings = "minor"
   ```

   **Commit directly to the branch.** Then **Pull requests → Compare & pull request → Create pull request**.
5. **Leave the AI declaration unticked.** The pull request only adds files to `reviews/`: it is a review, not
   content, and needs no declaration. PR-signoff says so in **Details**. Merge it.

✅ **Check:** in the report (part 5), `analysis/` is at **A2**, and on the **Findings** axis at **F1** if the
worst finding was `minor` (F0 for `none` or `trivial`).

Good to know:

- **Add-only.** A pull request that changes or deletes a file in `reviews/` fails. A second review, such as
  the one after a fix, goes into a new file.
- **A record file comes alone.** A pull request that adds one and changes anything outside `reviews/` fails:
  a change's own review is declared in its description (A2 with the report and the findings line).
- **The author never clears a finding.** Fixing is the author's work, in a pull request of its own; the fixed
  lines go back to F- until the next independent review attests both commits, the reviewed one and the fix.

## Optional · Let it change something

```text
@IMGAgent update paper with results
Add one sentence on the main limitation from the results summary to the abstract.
```

IMGAgent opens a pull request with the edit, with its own declaration ticked (the AI wrote it). You check the
change, tick your human review, and merge, or close it.

---

[← 3 Set up your repository](03-setup.md) · [5 The report on GitHub Pages →](05-pages.md)
