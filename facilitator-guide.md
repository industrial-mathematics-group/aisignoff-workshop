[← Overview](README.md)

# Facilitator guide

For Pascal (or whoever runs the session). Participants don't need this page.

**Format:** a short introduction, then everyone sets up their own repository in parallel while you do the same
steps on this repository on the projector. Then IMGAgent, the documentation site with the report, and Zenodo, then the advanced part.

## Before the workshop

### A week ahead: participants

- [ ] Send the link to [Before the workshop](00-before-the-workshop.md): account, user name to you, accept the
      invitation, create `workshop-<name>` (public, empty) in the organisation **or** transfer their own
      repository into it, Zenodo Sandbox login.
- [ ] Ask who brings their own repository, and look at those beforehand: existing workflows, a PR template
      or `.github/ISSUE_TEMPLATE/` of their own (then the signoff issue form must be copied in, see the
      maintainer cheat sheet §7), private (no Pages or Zenodo), or already a `SIGNOFF.toml`.
- [ ] Invite everyone to **industrial-mathematics-group** as members.

### Organisation settings (admin)

- [ ] *Organisation settings → Member privileges → Repository creation:* members may create **public**
      repositories (or create the `workshop-<name>` repositories yourself and make each person admin).
- [ ] *Organisation settings → Actions → General:* allow the actions the workflows use (`actions/*`, and
      `fsfe/reuse-action` for the optional REUSE step).
- [ ] The `.github` repository is public and its *Settings → Actions → General → Access* is **Accessible from
      repositories in the organization**.
- [ ] *Organisation settings → Third-party access → OAuth app policy:* if it is restricted, approve **Zenodo**
      and **Zenodo Sandbox** (they are separate apps), or participants can't see their organisation repositories
      on Zenodo (part 6). The first participant who requests access triggers an approval request you can grant.

### aisignoff and IMGAgent (by Thursday)

- [ ] The workshop follows **aisignoff 0.24.0**, the organisation's version since 26 November 2026
      (`ORG_VERSION` in `actions/setup-aisignoff/action.yml` of `industrial-mathematics-group/.github`). Nothing
      to raise.
- [ ] IMGAgent runs the release with the `setup` commands (`@IMGAgent help` lists `setup reuse|aisignoff|citation|docs`).
      Try `@IMGAgent setup aisignoff` and `setup docs` in a test repository: the form, **Done**, the pull request.
- [ ] Try `@IMGAgent review analysis with notes` in a test repository with the sample project (part 4,
      exercise 3): the answer with findings, and the pull request *Record a quick review of analysis …* that
      only adds a file to `reviews/` and goes green without a declaration.

### The day before: IMGAgent and the repositories

- [ ] *Organisation settings → GitHub Apps → IMGAgent → Configure → Repository access:* add every
      `workshop-<name>` repository, the transferred own repositories and `aisignoff-workshop` (or choose
      **All repositories**).
- [ ] Check the list of `workshop-*` repositories against the participants; chase the missing ones.
- [ ] Dry run: create `workshop-test`, go through parts 3 to 6 end to end with the pages open, then delete it.
      It shows how long each step takes with the current GitHub UI. Without GitHub, `tools/walkthrough.py`
      replays every pull request of parts 3 to 7 against the aisignoff release you have installed (usage at its
      top); with 0.24.0 all checks come out as the pages say.
- [ ] Print the [cheat sheet](cheat-sheet.pdf) for everyone, and the [maintainer cheat sheet](maintainer-cheat-sheet.pdf)
      for those who will maintain repositories.

### This repository as your demo repository

This repository starts plain on purpose: no workflows, no `SIGNOFF.toml`, no rules. You set it up live,
step by step with the participants. Differences from their repositories:

- **Step A:** nothing to upload; the example is already in `sample-project/`. Show the zip and the upload page
  anyway.
- **Step D:** be honest about this repository: everything in it, the guide and the example, was written by
  Claude (Claude Opus 5.5) and checked by you. A fitting `**` default is **G3 · H1 (or what you did) · A0**,
  with `Claude Opus 5.5 (Anthropic)` as `Assisted-by`: change them in the form on the projector, which shows how
  values are edited. A good moment to mention
  `exclude` too (files that need no declaration, such as `docs/build/**`; the review folder `reviews/` needs no
  entry, it is left out by itself). The participants'
  example story (G0/G1/G2/G3 by folder) is made up; their repositories role-play it.
- **Part 4:** for the signoff demo, use something true, e.g. *"The cheat sheet PDFs were made by Claude Opus 5.5
  on its own; I checked them against the Markdown (H1)"*, or an attestation of a page you read line by line.

### Own repositories in the session

Participants who bring a real repository follow the same steps with their own files: they skip step 3 A, and
declare what really happened (no role-play story). Watch for: step D's `**` default must be true for most of
*their* files, existing workflows may add required checks of their own, a private repository stops at part 4, and a
repository that already has `SIGNOFF.toml`, a docs site or `CITATION.cff` gets "already exists" from
`setup`: skip that step.

### The advanced part

- [ ] **7.1:** claude.ai connected to your GitHub account, a Claude project with the demo repository (this one
      after the live setup, or one prepared beforehand), and the Claude GitHub App installed on it. Prepare the
      task text (the one on the page asks it to tick its own part of the AI declaration). Agents can be slow on
      a live connection: have a pull request from a dry run open in a second tab as a fallback.
- [ ] **7.2:** start a real run beforehand (cluster jobs take longer than the session), so you can show the
      sandbox working, the job list on the cluster, and a finished pull request from the same setup. Keep
      tokens, keys, `.env` files and the cluster's account details off the projector.
- [ ] The message to land in both: whatever the agent and wherever it runs, the result is a pull request that
      a person inspects, declares and merges.

## Timing

| Time | Part | Notes |
|---|---|---|
| 0:00 | [1 GitHub in five words](01-git-and-github.md) | Pictures only. Show the history of an existing repository |
| 0:10 | [2 AI signoff](02-ai-signoff.md) | The levels table and "who is responsible" are the core |
| 0:20 | [3 Set up](03-setup.md) A–C | Everyone in step, wait at each ✅ check. Hands up when done |
| 0:35 | [3 Set up](03-setup.md) D | The IMGAgent form: show *⋯ → Edit* for the values once on the projector. Explain `[history]` while the checks run |
| 0:55 | [3 Set up](03-setup.md) E–F | The red→green moment in F is the payoff: give it time |
| 1:10 | Break | |
| 1:20 | [4 IMGAgent](04-imgagent.md) | Ask first (instant gratification), then signoff one folder at a time, then the review (exercise 3): start it before the last signoff, it takes a minute or two |
| 1:40 | [5 Website](05-pages.md) | `setup docs`, then the workflow as a pull request. While the deploy job runs: explain the findings axis and F- |
| 1:55 | [6 Zenodo](06-zenodo.md) | Sandbox only. Archiving takes a few minutes: start the release, then talk |
| 2:15 | [7.1 Basic agent workflow](07-advanced.md#71--a-basic-agent-workflow-claude-on-the-web) | Live: task → pull request → inspect → merge. About 15 min |
| 2:30 | [7.2 Showcase](07-advanced.md#72--showcase-an-advanced-setup) | Demonstration only, no setup. About 15 min |

Short on time: skip step F's "break it on purpose", step G (REUSE), the optional part of 4 (`update`), and step 4 of part 6.

## What to say at each step (talking points)

- **3 B, merge settings:** "The declaration is in the pull request's description. Only a merge commit with the
  description as its message carries it into history. Squash or rebase would drop it."
- **3 D:** IMGAgent only fills a template, no AI: that's why the pull request is G0. It was opened by an app,
  and `Responsible person:` makes the human who filled in the form responsible. The same form approach sets up
  REUSE (G), the docs site (5) and the citation (6).
- **3 E:** checks can only be required once they have run, which is why protection comes after D. Leave the
  bypass list empty and say why: on the playground, Claude with your admin login pushed straight to `main`
  because *Repository admin* was an "always" bypass, and a bypass also lifts force-push protection. "For pull
  requests only" is the safe way out. Come back to it in 7.2 (an agent as its own GitHub App can't bypass).
- **2:** the reviewer only reviews; its findings are recorded and shown (F0–F3, F-), never a gate. A1 says what
  it found too, so that there is a reference for what a different model finds at A2. Part 4's
  IMGAgent review is such an A1: a quick check, not a full review.
- **4:** IMGAgent writes declarations, it doesn't decide them: the person checks the diff and ticks. Each
  request costs the group a few cents. Who writes what: `SIGNOFF.toml` is what a person signs off (IMGAgent's
  pull requests, which you merge); AI reviews go into `reviews/`, add-only, in pull requests of their own that
  need no declaration (IMGAgent's review pull request is one). Each file gets its own findings level: point
  at the per-file list in the pull request.
- **5:** the report is public with the text of each file. The header's two flags (share without independent AI
  review, share with an open major or critical finding) are the quickest summary of a repository. The report
  lives in the docs site, so a repository keeps one Pages site for both.
- **6:** version DOI for a paper, concept DOI for the badge. Real DOIs are forever.
- **7.1:** go through *Files changed* slowly, comment on one line, let the agent answer with a new commit.
  Then tick an honest human review: "the AI wrote it" isn't one.
- **7.2:** the sandbox is why the agent may act without asking at every step; the pull request is why that is
  still safe for the repository. Point to the comparison table at the end of the page.

## What tends to go wrong

| Symptom | Cause and fix |
|---|---|
| No "By Industrial Mathematics Group" section under *Actions* | The repository isn't in the organisation, or the `.github` repository's templates aren't visible. Copy the workflow from `industrial-mathematics-group/.github/workflow-templates/` by hand (replace `$default-branch` with `main`) |
| IMGAgent's form doesn't come | IMGAgent isn't installed on the repository, or the command is in a code box. `@IMGAgent help` tests it |
| IMGAgent unticked **Done** | The problem is at the top of the form: usually two ticked boxes in a *tick one* group, or a value without backticks after editing. Fix it, tick **Done** again |
| "already has a `SIGNOFF.toml`" (or another file) | The file exists, e.g. in an own repository: skip the step, or change it with `@IMGAgent update SIGNOFF.toml` |
| A required check can't be found in the ruleset | It hasn't run in this repository yet, or the name differs: it's `pr-signoff / check`, `file-signoff / lint` |
| PR-signoff stays red after ticking | Two G boxes, G1–G3 without a model, no H ticked, A1–A3 without `AI-Review-Findings:`, or the page wasn't reloaded. **Details** says which |
| IMGAgent's review answers but opens no pull request | No `SIGNOFF.toml` on `main` yet, or aisignoff refused the record: the answer says why. The findings are still in the answer |
| A correction to a review is red | `reviews/` is add-only: a changed or deleted file there fails. Close it and record the corrected review in a new file |
| IMGAgent doesn't answer | Not installed on that repository (check *Settings → GitHub Apps*), the command is inside a code box or quote, or no folder was named. `@IMGAgent help` tests it |
| IMGAgent's signoff refuses | No `SIGNOFF.toml` on `main` yet (step D's pull request not merged), or a path that doesn't exist on `main` |
| Second signoff pull request shows "This branch has conflicts" | Two requests open at once. Merge one, then ask again with `@IMGAgent signoff` in the second issue, or **Resolve conflicts**: keep both entries, delete the `<<<<<<<`, `=======`, `>>>>>>>` lines |
| Pages: 404 | *Settings → Pages → Source* is not *GitHub Actions*, or the deploy job of Zensical docs hasn't finished; the report is under `/signoff/` |
| docs / build red on the workflow pull request | No `zensical.toml` on `main` yet: merge the `setup docs` pull request first, then update the workflow pull request's branch |
| The site has no report | No `SIGNOFF.toml` on `main`, or the report step warned (its summary says why); the site still deploys |
| Zenodo doesn't list the repository | Organisation access for Zenodo (Sandbox) not granted; **Sync now** after granting |
| Zenodo shows no new record | The release was saved as a draft, or the repository was switched on after the release. Publish a new release (`v0.1.1`) |

## Afterwards

- Participants can keep their `workshop-*` repositories as a reference, or delete them
  (*Settings → General → Danger Zone*). Remove the IMGAgent access for the deleted ones.
- Sandbox records can stay: they are test records, not real DOIs.
