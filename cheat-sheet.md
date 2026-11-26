# Cheat sheet: GitHub and AI signoff

Printable version: [cheat-sheet.pdf](cheat-sheet.pdf) · Workshop: [overview](README.md) · Setting up a repository: [maintainer cheat sheet](maintainer-cheat-sheet.md)

## Words

| | |
|---|---|
| **Repository** | A shared project folder that keeps every version of every file |
| **main** | The official version of the repository |
| **Commit** | One saved version, with a note: what changed, who, when |
| **Branch** | Your own working copy; doesn't disturb `main` |
| **Pull request (PR)** | "Please take my changes into `main`": the change, comments and checks |
| **Merge** | The changes go into `main` |
| **Issue** | A note, a question or a request |
| **Release** | A named, frozen version (e.g. `v1.0.0`); with Zenodo it gets a DOI |

## Change something, in the browser

1. **Edit:** open the file → pencil. **New file:** *Add file → Create new file*. **Upload:** *Add file → Upload files*.
2. **Commit changes…** → **Create a new branch … and start a pull request** → **Propose changes**.
3. **Create pull request**.
4. **Tick the AI declaration** in the description (you can tick right there).
5. Checks green → **Merge pull request** → **Confirm merge** → **Delete branch**.

## The AI declaration: G · H · A

| | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **G** How much did AI generate? | Nothing, I did it | AI **helped** (suggested, polished) | AI **wrote big parts**, I steered | An agent did it **mostly alone** |
| **H** How did a human check it? | Whole result looks right and plausible | **Tried it**: reran / recomputed, read the important parts | **Every line**, number and reference | **Independently confirmed**: other method, or a second person |
| **A** Did an independent AI check it? | No (the chat that wrote it doesn't count) | A **fresh session** checked it, without the chat | A **different, capable model**, with a committed report | Different model **with new evidence**, and the report |

- **G:** tick exactly one, the highest of any substantial part; for G1–G3 also tick the model(s).
- **H, A:** tick the highest level you actually did (H2 includes H0 and H1). Nothing ticked under A = A0.
- **A1–A3:** fill `AI-Review-Findings:` with the worst finding (`none` · `trivial` · `minor` · `major` ·
  `critical`); **A2/A3** also name the model and the report. A finding doesn't block the merge, it is recorded;
  major or critical: better fix it and have it reviewed again first.
- **Findings in the report:** F0 nothing open · F1 minor · F2 major · F3 critical · F- no independent AI review
  since the line last changed.
- **Minimums:** a repository can require more (`[policy]` in its `SIGNOFF.toml`, e.g. at least H1).
- **You are responsible** for what you merge, whoever or whatever wrote it.

## IMGAgent: ask and sign off

Write in a new issue or a comment (not in a code box), folders separated by commas:

```text
@IMGAgent ask notes, analysis
When does the coffee reach 60 °C?
```

```text
@IMGAgent signoff
I checked results/summary.md line by line against the data. Please record H2, reviewer Jane Doe.
```

`ask` answers from those folders only. `signoff` confirms what it understood or asks, then opens a pull request
that changes `SIGNOFF.toml`: check *Files changed*, tick your human review, merge. One request at a time.
Without AI: *Issues → New issue → Signoff: declare or attest files*. More: `@IMGAgent help`.

**Setting up a file:** `@IMGAgent setup aisignoff` (`SIGNOFF.toml`), `setup reuse` (`REUSE.toml` and `LICENSES/`),
`setup docs` (a documentation site) or `setup citation` (`CITATION.cff`) answers with a form, filled in with
defaults. Change what you need (tick boxes; values via *⋯ → Edit*), tick **Done**: a pull request, declared G0.

## An AI review after the merge

```text
@IMGAgent review analysis with notes
Does the fit match what the lab notes assume?
```

A quick review (**A1**) of the first folders, reading the `with` folders. IMGAgent answers with the findings and
opens a pull request that only adds a record file to `reviews/`: leave its declaration unticked, check that the
findings are fair, merge. Each file then shows its own highest finding (F0–F3). `reviews/` is add-only: a later
review adds a new file. The reviewer changes nothing; fixing is the author's.

## Red check?

Open **Details** on the check. Usual reasons: no or two G boxes · G1–G3 without a model · only H0 where H1 is required ·
A1–A3 without findings line · A2/A3 without report · a file in `reviews/` changed, or a record file next to other
changes · page not reloaded.

## Releases and DOIs (Zenodo)

1. Once: log in at zenodo.org with GitHub → *GitHub* → **Sync now** → switch the repository **On**; add `CITATION.cff` (`@IMGAgent setup citation`).
2. Each time: **Releases → Draft a new release** → new tag `v1.0.0` → **Publish release**.
3. Zenodo archives it and mints a DOI: **version DOI** (cite in papers) + **concept DOI** (always the newest; for the badge).
4. Practise on sandbox.zenodo.org: real DOIs can't be deleted.

## Golden rules

One change per pull request · never put unpublished data, personal data or passwords into a public
repository or an AI tool · when unsure, declare more AI generation and less review rather than the other way round, and say why in the description.

[AI policy (full definitions)](https://github.com/industrial-mathematics-group/.github/blob/main/.github/CONTRIBUTING.md#ai-assisted-contributions) ·
[aisignoff](https://github.com/industrial-mathematics-group/aisignoff) ·
Optional app for working with folders on your computer: [GitHub Desktop](https://desktop.github.com/)
