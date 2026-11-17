[← 1 GitHub in five words](01-git-and-github.md) · **2 AI signoff** · [3 Set up your repository →](03-setup.md)

# 2 · AI signoff in plain words

## Why

We **welcome AI tools**: for writing, coding, analysing, making figures. What we ask is that everything that
goes into `main` says **honestly how it was made and how it was checked**. Funders, journals and readers
increasingly ask; the answer should be on record, not in someone's memory. And the record travels with the
files: into every copy, every release and the Zenodo archive.

## Three questions, one line

Every change answers three questions. The answer reads like **G2 · H1 · A0**.

| | Question | 0 | 1 | 2 | 3 |
|---|---|---|---|---|---|
| **G** | How much did **AI generate**? | I did it myself, no AI | AI **helped**: suggestions, polishing, a structure | AI **wrote big parts**, I steered and edited | An AI agent did it **mostly on its own** |
| **H** | How did a **human check** it? | Looked at it as a whole: does what was asked, plausible | **Tried it**: ran it or recomputed the key results, read the important parts | **Every line**: every sentence, number, formula, reference | **Independently confirmed**: another method, or a second person checked every line |
| **A** | Did an **independent AI** check it? | No (the chat that wrote it checking itself doesn't count) | A **fresh AI session**, without the original chat, checked it | A **different, capable model** checked it and wrote a report | A different model **produced new evidence** (new tests, a recomputation), with the report |

- **G:** tick the highest level of any substantial part. A spell checker doesn't count; ChatGPT rewriting a
  paragraph is G1; ChatGPT drafting the section is G2.
- **H and A build up:** H2 includes H0 and H1. Tick the highest one you actually did.
- **A2 and A3** need the report committed or linked, and one more line: `AI-Review-Findings:`, the worst
  problem the review found in the change (`none`, `trivial`, `minor`, `major`, `critical`). A `major` or
  `critical` finding has to be fixed and reviewed again before merging. For A0 and A1, leave the line empty.
- A repository can set **minimum levels**, such as "at least H1 for everything" (its `[policy]`).

### Examples from research

| What happened | Declaration |
|---|---|
| I wrote the notes myself and reread them | G0 · H2 · A0 |
| ChatGPT polished the English of my abstract; I read every sentence | G1 · H2 · A0 |
| Claude wrote the analysis script; I ran it and checked the numbers | G2 · H1 · A0 |
| Same, and then a fresh Claude session checked the script without our chat | G2 · H1 · A1 |
| An agent ran the analysis and wrote the summary; I checked the numbers | G3 · H1 · A0 |

The example project you'll use today has exactly these: see
[sample-project/HOW-THIS-WAS-MADE.md](sample-project/HOW-THIS-WAS-MADE.md). The
[full definitions](https://github.com/industrial-mathematics-group/.github/blob/main/.github/CONTRIBUTING.md#ai-assisted-contributions)
have a column for code and one for research and writing.

## Who is responsible?

**The person who opens the pull request.** By ticking a human review level you take responsibility for the
change, however it was made. AI can't take responsibility. If a bot opens the pull request for you, it names
you (`Responsible person: @you`) and you tick.

## Where the declaration is kept

| How the files get in | Where the declaration goes | Who writes it |
|---|---|---|
| A pull request (the usual way) | The ticked boxes in its description, which become the merge commit's message | You, by ticking |
| Files that are already in `main` | `SIGNOFF.toml`, a list of paths and their levels | **IMGAgent** (`@IMGAgent signoff` in an issue) or the issue form *Signoff: declare or attest files* |

You never have to edit `SIGNOFF.toml` by hand, except once when you set it up (part 3).

## What you get

- **Checks** on every pull request: red until the declaration is complete and meets the repository's minimum.
- **Labels** on each pull request (`ai:G2`, `human:H1`, `ai-review:A0`).
- **Badges** on the front page: the share of files and of merged pull requests at each level.
- **The interactive report**: every folder and file coloured by its levels. In part 5 you publish it.

---

[← 1 GitHub in five words](01-git-and-github.md) · [3 Set up your repository →](03-setup.md)
