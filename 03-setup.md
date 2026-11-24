[← 2 AI signoff](02-ai-signoff.md) · **3 Set up your repository** · [4 IMGAgent →](04-imgagent.md)

# 3 · Set up your repository

You'll turn your empty `workshop-…` repository into one that is set up like the group's repositories. Each step
ends with ✅ **Check**: what you should see before you go on. Pascal does the same on this repository.

| Step | | Time |
|---|---|---|
| A | Put the example project in | 5 min |
| B | Repository settings | 5 min |
| C | Install the workflows | 10 min |
| D | `SIGNOFF.toml`: the setup pull request | 15 min |
| E | Protect `main` | 5 min |
| F | Your first declared pull request | 10 min |

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

**Settings → Actions → General**, scroll to **Workflow permissions**:

4. **Read and write permissions**, and tick **Allow GitHub Actions to create and approve pull requests**.
   **Save.** (If it's greyed out, the organisation already allows it.)

✅ **Check:** the settings stay after a page reload.

## C · Install the workflows

Workflows are the little robots. The group has ready-made ones. Install three of them, **File-signoff last**:

1. **Actions** tab. GitHub suggests workflows; scroll to **By Industrial Mathematics Group** (or search for
   `signoff`).
2. **PR-signoff → Configure.** Don't change anything. **Commit changes… → Commit changes** (directly to `main`
   is fine now: `main` isn't protected yet).
3. Back to **Actions → New workflow**: **Signoff-Badges → Configure → Commit changes.**
4. **Actions → New workflow**: **File-signoff → Configure → Commit changes.**

| Workflow | What it does |
|---|---|
| PR-signoff | Checks the ticked declaration of every pull request; sets the `ai:G*`, `human:H*`, `ai-review:A*` labels |
| File-signoff | Checks that every file (every line) is declared; writes the report and the file badges (and, switched on in part 5, publishes the report on GitHub Pages); without `SIGNOFF.toml` it opens a pull request to set it up |
| Signoff-Badges | Makes badges from the declarations of merged pull requests |

✅ **Check:** **Actions** lists runs for File-signoff and Signoff-Badges. File-signoff has a yellow warning
"aisignoff not set up". That's expected: step D.

## D · `SIGNOFF.toml`: the setup pull request

`SIGNOFF.toml` says how the files of the repository were made. File-signoff has just written one for you, with
`TODO` everywhere, and opened a pull request.

1. **Pull requests** tab → **Set up aisignoff (SIGNOFF.toml with TODOs to fill in)**. Read its description.
2. **Files changed** → on `SIGNOFF.toml` click **⋯ → Edit file**.
3. At the end, replace the `TODO`s with what is true for most of the files (see
   [HOW-THIS-WAS-MADE.md](sample-project/HOW-THIS-WAS-MADE.md); for your own repository, what is true for most
   of your files), with your name:

   ```toml
   # Default for everything
   [[annotations]]
   path = "**"
   AI-Generation = "G0"
   Human-Review = "H2"
   AI-Review = "A0"
   Reviewed-by = ["Jane Doe"]
   ```

   Leave the rest as it is. Look at `[history]` (every line is declared by the pull request that brought it)
   and the comment on review findings on the way. The commented `exclude` line mentions `reviews/**`: you don't
   need it, the review folder `reviews/` is left out by itself (part 4).
4. **Commit changes… → Commit directly to the `aisignoff-setup` branch → Commit changes.**
5. Back on the pull request's **Conversation** tab, wait for the checks (about a minute).
   **PR-signoff** is red: in the description **G0** and **A0** are already ticked (a tool wrote the file), and
   `Responsible person:` names you. **Tick your human review** (you just read the file: **H2**).
6. Both checks green: **Merge pull request → Confirm merge.**

✅ **Check:** `SIGNOFF.toml` is on `main`. **Actions → File-signoff →** the newest run on `main` is green, and its
summary shows a folder tree with the levels.

The other folders (`analysis/`, `results/`, `paper/`) are declared differently: that's part 4, with IMGAgent.

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

---

[← 2 AI signoff](02-ai-signoff.md) · [4 IMGAgent →](04-imgagent.md)
