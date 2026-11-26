[← 3 Set up your repository](03-setup.md) · **4 IMGAgent** · [5 A website with the report →](05-pages.md)

# 4 · IMGAgent

**IMGAgent** is the group's assistant on GitHub; you met it in part 3, setting up `SIGNOFF.toml`. You talk to it by writing `@IMGAgent` and a command in an
issue (or a comment in one). It answers questions about the files of a repository, writes declarations
into `SIGNOFF.toml` for you, and reviews files. It only answers people with write access to the repository, and it never changes
`main` by itself: whatever it changes comes as a pull request that you check and merge.

Pascal has installed it on your workshop repository. Check: **Settings → GitHub Apps** lists **IMGAgent**.

| Command | What happens |
|---|---|
| `@IMGAgent ask <folders>` and a question | Answers from the files in those folders. Changes nothing |
| `@IMGAgent signoff` and your words | Records how files were made and reviewed: a pull request that changes `SIGNOFF.toml` |
| `@IMGAgent update <folders> with <folders>` and a task | Edits files in the first folders, reading the others; opens a pull request |
| `@IMGAgent review <folders> with <folders>` | A quick AI review (A1) of the first folders, reading the others; opens a pull request that records it in `reviews/` |
| `@IMGAgent make docs` | Writes a documentation site in `docs/`; opens a pull request |
| `@IMGAgent setup aisignoff`, `reuse`, `docs` or `citation` | A form for `SIGNOFF.toml`, `REUSE.toml`, `zensical.toml` or `CITATION.cff`, filled in with defaults; ticking **Done** opens a pull request, without AI (you used it in part 3) |
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

## Exercise 3 · Let IMGAgent review a folder (10 min)

`SIGNOFF.toml` says **A0** everywhere: no independent AI has checked anything yet. IMGAgent can do a quick
check and record it for you.

1. **Issues → New issue.** Title: `Review: analysis`. Text (the line after the command is optional and says
   what to look at):

   ```text
   @IMGAgent review analysis with notes
   Does the fit make assumptions the lab notes say might not hold?
   ```

   The folders before `with` are reviewed; the `with` folders are only read, as context. **Create.**
2. After a minute or two IMGAgent answers with its findings, each with a severity (`trivial`, `minor`,
   `major` or `critical`), and the highest one. Claude Sonnet reviews in a **new session**, without the
   conversation that wrote the files: that's **A1**.
3. It also opens a pull request: **Record a quick review of analysis (A1, highest finding: …)**. It only adds
   one small record file to the review folder `reviews/`, so its **AI declaration stays unticked**: a review
   is not content. PR-signoff says so in **Details**. Read the findings in its description: are they fair?
   Then merge it.

✅ **Check:** **Actions → File-signoff →** the newest run on `main`: `analysis` is at **A1** now. In the
report (part 5), the **Findings** axis colours each file of `analysis/` by its own highest finding: **F0** for
`none` or `trivial`, **F1** `minor`, **F2** `major`, **F3** `critical`. The other folders stay grey (**F-**):
no independent AI has seen them.

*Own repository:* review a folder you care about, with the folders that explain it after `with`, e.g.
`@IMGAgent review docs with src` (do the docs still describe the code?).

Good to know:

- **A finding doesn't block anything.** It is recorded and shown. Fixing is up to you, in a pull request of
  its own; the fixed lines go back to **F-** until the next review. The author never clears a finding:
  review again (`@IMGAgent review analysis`), which adds a new record file.
- **Add-only.** A pull request that changes or deletes a file in `reviews/` fails.
- **A1 is a quick check.** A thorough review by a **different** model with a written report is **A2**; how to
  record one is in [part 7](07-advanced.md) and the [maintainer cheat sheet](maintainer-cheat-sheet.md#9-pr-messages-what-maintainers-check).
- IMGAgent always reviews `main`, also when you ask in a pull request. A pull request's own review goes into
  its description; IMGAgent's answer has the three lines to copy.

## Optional · Let it change something

```text
@IMGAgent update paper with results
Add one sentence on the main limitation from the results summary to the abstract.
```

IMGAgent opens a pull request with the edit, with its own declaration ticked (the AI wrote it). You check the
change, tick your human review, and merge, or close it.

---

[← 3 Set up your repository](03-setup.md) · [5 A website with the report →](05-pages.md)
