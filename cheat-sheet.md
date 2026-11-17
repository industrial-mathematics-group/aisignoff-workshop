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
- **A2/A3 only:** name the model and the report, and fill `AI-Review-Findings:` with the worst finding
  (`none` · `trivial` · `minor` · `major` · `critical`). Major or critical: fix it and review again first.
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

## Red check?

Open **Details** on the check. Usual reasons: no or two G boxes · G1–G3 without a model · only H0 where H1 is required ·
A2/A3 without report or findings line · page not reloaded.

## Releases and DOIs (Zenodo)

1. Once: log in at zenodo.org with GitHub → *GitHub* → **Sync now** → switch the repository **On**; add `CITATION.cff`.
2. Each time: **Releases → Draft a new release** → new tag `v1.0.0` → **Publish release**.
3. Zenodo archives it and mints a DOI: **version DOI** (cite in papers) + **concept DOI** (always the newest; for the badge).
4. Practise on sandbox.zenodo.org: real DOIs can't be deleted.

## Golden rules

One change per pull request · never put unpublished data, personal data or passwords into a public
repository or an AI tool · when unsure, declare more AI generation and less review rather than the other way round, and say why in the description.

[AI policy (full definitions)](https://github.com/industrial-mathematics-group/.github/blob/main/.github/CONTRIBUTING.md#ai-assisted-contributions) ·
[aisignoff](https://github.com/industrial-mathematics-group/aisignoff) ·
Optional app for working with folders on your computer: [GitHub Desktop](https://desktop.github.com/)
