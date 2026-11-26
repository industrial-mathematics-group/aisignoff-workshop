[← 2 AI signoff](02-ai-signoff.md) · **3 Set up your repository** · [4 IMGAgent →](04-imgagent.md)

# 3 · Set up your repository

You'll turn your empty `workshop-…` repository into one that is set up like the group's repositories. Each step
ends with ✅ **Check**: what you should see before you go on. Pascal does the same on this repository.

| Step | | Time |
|---|---|---|
| A | Put the example project in | 5 min |
| B | Repository settings | 5 min |
| C | Install the workflows | 10 min |
| D | `SIGNOFF.toml`, set up by IMGAgent | 15 min |
| E | Protect `main` | 5 min |
| F | Your first declared pull request | 10 min |
| G | Optional: licences with REUSE | 10 min |

## A · Put the example project in

**Brought your own repository?** Skip this step: you'll work with your own files. Where the steps below
say *the example*, think of your files and declare what really happened.

1. In this workshop repository, open [`sample-project.zip`](sample-project.zip) and click the **download**
   icon (top right of the file view). Unzip it on your computer.
2. Open your repository. On the empty "Quick setup" page click **uploading an existing file**.
3. Open the unzipped folder, select **everything inside it** (the folders `analysis`, `data`, `notes`, `paper`,
   `results` and the two `.md` files), and drag it onto the browser window. The folders are kept.
4. Commit message: `Add the coffee cooling project`. **Commit changes.**

✅ **Check:** your repository's front page shows the folders and the README "How fast does coffee cool?".

## B · Repository settings

**Settings** (the tab at the top of your repository) → **General**, scroll to **Pull Requests**:

1. Keep **Allow merge commits** ticked. Under it, set **Default commit message** to
   **Pull request title and description**.
2. Untick **Allow squash merging** and **Allow rebase merging**.
3. Tick **Automatically delete head branches**.

*Why:* the ticked declaration is in the pull request's description. Only a merge commit with the description
as its message carries it into the history of `main`.

✅ **Check:** the settings stay after a page reload.

## C · Install the workflows

Workflows are the little robots. The group has ready-made ones. Install three of them:

1. **Actions** tab. GitHub suggests workflows; scroll to **By Industrial Mathematics Group** (or search for
   `signoff`).
2. **PR-signoff → Configure.** Don't change anything. **Commit changes… → Commit changes** (directly to `main`
   is fine now: `main` isn't protected yet).
3. Back to **Actions → New workflow**: **Signoff-Badges → Configure → Commit changes.**
4. **Actions → New workflow**: **File-signoff → Configure → Commit changes.**

| Workflow | What it does |
|---|---|
| PR-signoff | Checks the ticked declaration of every pull request; sets the `ai:G*`, `human:H*`, `ai-review:A*` labels |
| File-signoff | Checks that every file (every line) is declared; writes the report and the file badges |
| Signoff-Badges | Makes badges from the declarations of merged pull requests |

✅ **Check:** **Actions** lists runs for File-signoff and Signoff-Badges. File-signoff has a yellow warning
"aisignoff not set up". That's expected: step D sets it up.

## D · `SIGNOFF.toml`, set up by IMGAgent

`SIGNOFF.toml` says how the files of the repository were made. You don't write it by hand: **IMGAgent**, the
group's assistant on GitHub (more of it in part 4), gives you a form with everything filled in, and turns it into
a pull request. No AI is involved in this step.

1. **Issues → New issue** (choose **Blank issue** if GitHub offers forms). Title: `Set up AI signoff`. Text:

   ```text
   @IMGAgent setup aisignoff
   ```

   **Create.**
2. After a few seconds IMGAgent answers with a form: the default declaration for every file (`**`), the git
   history, and a few more settings. The defaults are what is true for most of the example's files
   (see [HOW-THIS-WAS-MADE.md](sample-project/HOW-THIS-WAS-MADE.md)): **G0** (written by a person), **H2**
   (read line by line), **A0** (no independent AI review), and you as `Reviewed-by`. For your own repository,
   choose what is true for most of *your* files.
   - **Boxes:** tick or untick them right in the comment.
   - **Values** between backticks (such as your name): open the comment's **⋯ → Edit**, change the text
     between the backticks, **Update comment**. Your full name is nicer than your GitHub login.
3. Leave the rest as it is. Look at **History** on the way: every line is declared by the pull request that
   brought it.
4. Tick **Done: create the pull request** at the bottom of the form. A moment later IMGAgent replies with a link
   to the pull request **Set up SIGNOFF.toml**. (If something in the form can't be used, it unticks **Done** and
   says why at the top: fix it and tick **Done** again.)
5. Open the pull request. **Files changed** shows the new `SIGNOFF.toml`: check that it says what you chose.
6. Wait for the checks (about a minute). **PR-signoff** is red: in the description **G0** is already ticked
   (IMGAgent filled in a form, no AI), and `Responsible person:` names you. **Tick your human review** (you just
   read the file: **H2**).
7. Both checks green: **Merge pull request → Confirm merge.**

✅ **Check:** `SIGNOFF.toml` is on `main`. **Actions → File-signoff →** the newest run on `main` is green, and its
summary shows a folder tree with the levels.

The other folders (`analysis/`, `results/`, `paper/`) were made differently: you declare them in part 4, with
IMGAgent too.

## E · Protect `main`

From now on, changes reach `main` only through checked pull requests.

**Settings → Rules → Rulesets → New ruleset → New branch ruleset:**

1. **Ruleset name:** `main`. **Enforcement status:** Active.
2. **Bypass list: leave it empty.** (Why, below.)
3. **Target branches → Add target → Include default branch.**
4. Rules (keep **Restrict deletions** and **Block force pushes** ticked):
   - **Require a pull request before merging.** Required approvals: **0** (you're alone in your repository).
     Under *Allowed merge methods* keep only **Merge**.
   - **Require status checks to pass → Add checks:** type `check` and choose **pr-signoff / check**, then type
     `lint` and choose **file-signoff / lint**.
5. **Create.**

✅ **Check:** on the front page, try the pencil on any file: the commit dialog no longer offers to commit to
`main` directly.

> **Why no bypass, not even for yourself?** Whoever is on the bypass list can push straight to `main`, without a
> pull request and without checks. That includes every tool and AI agent that works **with your account**: in
> a test on the playground, Claude, acting with an admin's login, pushed directly to `main` because the
> *Repository admin* role was on the bypass list. And a bypass covers **every rule of its ruleset**, so it also
> switches off *Block force pushes* and *Restrict deletions* for you.
>
> If you really want a way out (a pull request whose checks can't pass, such as a change to `[policy]`): add
> *Repository admin* with the mode **For pull requests only** instead of *Always*. Then you can merge such a pull
> request anyway, but never push to `main` directly. Better still, keep *Block force pushes* and
> *Restrict deletions* in a second ruleset with no bypass at all.

## F · Your first declared pull request

Add the badges to your README, as a real pull request.

1. Open `README.md` → pencil. At the very top, paste this and replace `workshop-jane-doe` (twice in each line)
   with the name of your repository:

   ```markdown
   [![AI generation](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/industrial-mathematics-group/workshop-jane-doe/badges/aisignoff-generation.json)](https://github.com/industrial-mathematics-group/workshop-jane-doe/actions/workflows/file-signoff.yml)
   [![Human review](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/industrial-mathematics-group/workshop-jane-doe/badges/aisignoff-human-review.json)](https://github.com/industrial-mathematics-group/workshop-jane-doe/actions/workflows/file-signoff.yml)
   [![AI review](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/industrial-mathematics-group/workshop-jane-doe/badges/aisignoff-ai-review.json)](https://github.com/industrial-mathematics-group/workshop-jane-doe/actions/workflows/file-signoff.yml)
   [![AI review findings](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/industrial-mathematics-group/workshop-jane-doe/badges/aisignoff-findings.json)](https://github.com/industrial-mathematics-group/workshop-jane-doe/actions/workflows/file-signoff.yml)
   ```

2. **Commit changes… → Create a new branch for this commit and start a pull request → Propose changes →
   Create pull request.** The description is the group's template, ending in the **AI declaration**.
3. Watch the checks go **red**. Then **break it on purpose** once: tick **G0** and **G1** together and read
   **Details** on the PR-signoff check.
4. Tick it properly: **G0** (you pasted it), no model, **H2**, **A0**. Leave `AI-Review-Findings:` empty (it is
   only for A1 to A3).
5. Checks green, labels `ai:G0`, `human:H2`, `ai-review:A0` on the right: **Merge pull request → Confirm merge.**

✅ **Check:** the front page shows four badges (they may need a minute and a reload; the findings badge says
F- for now, since nothing has had an independent AI review yet), and the newest commit
on `main` carries your ticked declaration in its message.

**Your repository is now set up like the group's.** The [maintainer cheat sheet](maintainer-cheat-sheet.md) has
all of this on two pages, for the next repository.

## G · Optional: licences with REUSE (10 min)

[REUSE](https://reuse.software) checks that every file says who holds the copyright and under which licence it
may be used, so that others know what they may reuse. Again IMGAgent writes the files from a form.

1. In a new issue, write `@IMGAgent setup reuse`. The form has the copyright line (year and owner) and the common
   licences as boxes, each with the folders it applies to (`.` is everything). For the example, tick **MIT** for
   `.`. For real data or texts, CC BY 4.0 for their folders is a common choice.
2. Tick **Done**. The pull request **Set up REUSE.toml** adds `REUSE.toml` and the licence texts in
   `LICENSES/`. Tick your human review, merge.
3. **Actions → New workflow → REUSE → Configure → Commit changes… → Create a new branch … and start a pull
   request.** Declare it like any file you copied from the group's templates (they were written with Claude):
   **G3**, **Claude Opus**, **H1** (you read it), **A0**. Merge once green.

✅ **Check:** the REUSE run on `main` is green ("Congratulations! Your project is compliant").

---

[← 2 AI signoff](02-ai-signoff.md) · [4 IMGAgent →](04-imgagent.md)
