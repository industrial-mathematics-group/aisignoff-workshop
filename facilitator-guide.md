[← Overview](README.md)

# Facilitator guide

For Pascal (or whoever runs the session). Participants don't need this page.

**Format:** a short introduction, then everyone sets up their own repository in parallel while you do the same
steps on this repository on the projector. Then IMGAgent, Pages and Zenodo, then the advanced part.

## Before the workshop

### A week ahead: participants

- [ ] Send the link to [Before the workshop](00-before-the-workshop.md): account, user name to you, accept the
      invitation, create `workshop-<name>` (public, empty) in the organisation, Zenodo Sandbox login.
- [ ] Invite everyone to **industrial-mathematics-group** as members.

### Organisation settings (admin)

- [ ] *Organisation settings → Member privileges → Repository creation:* members may create **public**
      repositories (or create the `workshop-<name>` repositories yourself and make each person admin).
- [ ] *Organisation settings → Actions → General:* allow the actions the workflows use (`actions/*`), and under
      *Workflow permissions* **Read and write** with **Allow GitHub Actions to create and approve pull
      requests**. Without it the File-signoff setup pull request can't be opened (step 3 D).
- [ ] The `.github` repository is public and its *Settings → Actions → General → Access* is **Accessible from
      repositories in the organization**.
- [ ] *Organisation settings → Third-party access → OAuth app policy:* if it is restricted, approve **Zenodo**
      and **Zenodo Sandbox** (they are separate apps), or participants can't see their organisation repositories
      on Zenodo (part 6). The first participant who requests access triggers an approval request you can grant.

### The day before: IMGAgent and the repositories

- [ ] *Organisation settings → GitHub Apps → IMGAgent → Configure → Repository access:* add every
      `workshop-<name>` repository and `aisignoff-workshop` (or choose **All repositories**).
- [ ] Check the list of `workshop-*` repositories against the participants; chase the missing ones.
- [ ] Dry run: create `workshop-test`, go through parts 3 to 6 end to end with the pages open, then delete it.
      It shows how long each step takes with the current GitHub UI.
- [ ] Print the [cheat sheet](cheat-sheet.pdf) for everyone, and the [maintainer cheat sheet](maintainer-cheat-sheet.pdf)
      for those who will maintain repositories.

### This repository as your demo repository

This repository starts plain on purpose: no workflows, no `SIGNOFF.toml`, no rules. You set it up live,
step by step with the participants. Differences from their repositories:

- **Step A:** nothing to upload; the example is already in `sample-project/`. Show the zip and the upload page
  anyway.
- **Step D:** be honest about this repository: everything in it, the guide and the example, was written by
  Claude (Claude Opus 5.5) and checked by you. A fitting `**` default is **G3 · H1 (or what you did) · A0**,
  with `Assisted-by = ["Claude Opus 5.5 (Anthropic)"]` added to the annotation. A good moment to mention
  `exclude` too (files that need no declaration, such as committed AI review reports). The participants'
  example story (G0/G1/G2/G3 by folder) is made up; their repositories role-play it.
- **Part 4:** for the signoff demo, use something true, e.g. *"The cheat sheet PDFs were made by Claude Opus 5.5
  on its own; I checked them against the Markdown (H1)"*, or an attestation of a page you read line by line.

## Timing

| Time | Part | Notes |
|---|---|---|
| 0:00 | [1 GitHub in five words](01-git-and-github.md) | Pictures only. Show the history of an existing repository |
| 0:10 | [2 AI signoff](02-ai-signoff.md) | The levels table and "who is responsible" are the core |
| 0:20 | [3 Set up](03-setup.md) A–C | Everyone in step, wait at each ✅ check. Hands up when done |
| 0:40 | [3 Set up](03-setup.md) D | The longest step. Explain `[history]` and `[review]` while the checks run |
| 0:55 | [3 Set up](03-setup.md) E–F | The red→green moment in F is the payoff: give it time |
| 1:10 | Break | |
| 1:20 | [4 IMGAgent](04-imgagent.md) | Ask first (instant gratification), then signoff one folder at a time |
| 1:40 | [5 Pages](05-pages.md) | While the Pages run builds: explain the review gap |
| 1:55 | [6 Zenodo](06-zenodo.md) | Sandbox only. Archiving takes a few minutes: start the release, then talk |
| 2:15 | [7 Advanced](07-advanced.md) | |

Short on time: skip step F's "break it on purpose", the optional parts of 4, and step 4 of part 6.

## What to say at each step (talking points)

- **3 B, merge settings:** "The declaration is in the pull request's description. Only a merge commit with the
  description as its message carries it into history. Squash or rebase would drop it."
- **3 C, File-signoff last:** it reacts to the push of its own file by opening the setup pull request.
- **3 D:** the pull request was opened by a bot, so its checks start only with the first push to the branch
  (the edit). `Responsible person:` makes the human who triggered it responsible.
- **3 E:** checks can only be required once they have run, which is why protection comes after D.
- **4:** IMGAgent writes declarations, it doesn't decide them: the person checks the diff and ticks. Each
  request costs the group a few cents.
- **5:** the report is public with the text of each file. One Pages site per repository.
- **6:** version DOI for a paper, concept DOI for the badge. Real DOIs are forever.

## What tends to go wrong

| Symptom | Cause and fix |
|---|---|
| No "By Industrial Mathematics Group" section under *Actions* | The repository isn't in the organisation, or the `.github` repository's templates aren't visible. Copy the workflow from `industrial-mathematics-group/.github/workflow-templates/` by hand (replace `$default-branch` with `main`) |
| File-signoff ran, but no setup pull request | *Allow GitHub Actions to create … pull requests* is off (organisation or repository); the branch `aisignoff-setup` exists and the job summary links to a prefilled pull request. Turn the setting on, delete the branch, *Run workflow* |
| The setup pull request has no checks | Nothing was pushed to `aisignoff-setup` yet: the edit of step D starts them |
| File-signoff red on the setup pull request | A `TODO` left, a typo in a level (`"G 0"`), or `Reviewed-by` not in `[" "]` |
| A required check can't be found in the ruleset | It hasn't run in this repository yet, or the name differs: it's `pr-signoff / check`, `file-signoff / lint` |
| PR-signoff stays red after ticking | Two G boxes, G1–G3 without a model, no H ticked, or the page wasn't reloaded. **Details** says which |
| IMGAgent doesn't answer | Not installed on that repository (check *Settings → GitHub Apps*), the command is inside a code box or quote, or no folder was named. `@IMGAgent help` tests it |
| IMGAgent's signoff refuses | No `SIGNOFF.toml` on `main` yet (step D not merged), or a path that doesn't exist on `main` |
| Second signoff pull request shows "This branch has conflicts" | Two requests open at once. Merge one, then ask again with `@IMGAgent signoff` in the second issue, or **Resolve conflicts**: keep both entries, delete the `<<<<<<<`, `=======`, `>>>>>>>` lines |
| Pages: 404 | *Settings → Pages → Source* is not *GitHub Actions*, or the Pages run hasn't finished |
| Zenodo doesn't list the repository | Organisation access for Zenodo (Sandbox) not granted; **Sync now** after granting |
| Zenodo shows no new record | The release was saved as a draft, or the repository was switched on after the release. Publish a new release (`v0.1.1`) |

## Afterwards

- Participants can keep their `workshop-*` repositories as a reference, or delete them
  (*Settings → General → Danger Zone*). Remove the IMGAgent access for the deleted ones.
- Sandbox records can stay: they are test records, not real DOIs.
