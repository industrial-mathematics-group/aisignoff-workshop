# Maintainer cheat sheet: preparing a repository for AI signoff

For repositories in **industrial-mathematics-group**, as of aisignoff **0.20.1** and the organisation's
`.github` repository (24 November 2026). Reference setups: **aisignoff-playground** (Python, Zensical) and
**HyperCloudCore.jl** (Julia, Documenter). Full text: `SETUP.md` in `industrial-mathematics-group/.github`.

## 0. Organisation, once (admins)

- *Organisation settings → Actions → General*: allow `actions/*` and the actions the packages use
  (julia-actions, codecov, TagBot).
- *Workflow permissions*: **Read and write permissions**, and tick **Allow GitHub Actions to create and approve
  pull requests** (the File-signoff setup PR, CompatHelper and Documenter need it).
- The `.github` repository stays **public**, with *Settings → Actions → General → Access*: **Accessible from
  repositories in the organization** (else no repository can call the reusable workflows).
- **IMGAgent** (GitHub App, replaces the old `@signoff` workflows): installed per repository under
  *Organisation settings → GitHub Apps → IMGAgent → Configure*.

## 1. Merge settings (*Settings → General → Pull Requests*)

- Allow **merge commits** only (org default). Default message: **Pull request title and description**.
  Without this the ticked declaration never reaches git, and every merged line falls back to the file-level
  declaration.
- If you also allow squash: set its default message to the same, and `merge-method = "squash"` in `[history]`
  (`"merge"` is the default). Rebase merging drops the description: avoid it.
- Merge on GitHub, not locally: a local merge doesn't carry the description.
- Tick **Automatically delete head branches** (optional, keeps the branch list clean).

## 2. Workflows (*Actions → New workflow → "By Industrial Mathematics Group"*)

The templates are thin callers of the reusable workflows in `.github`; copying by hand works too
(replace `$default-branch` with `main`).

| Workflow file | What it does | Check name to require |
|---|---|---|
| `pr-signoff.yml` | Checks the ticked AI declaration of every PR into `main` (with `SIGNOFF.toml`: also every file/line of the merge preview, under the base branch's `[policy]`); sets `ai:G*`, `human:H*`, `ai-review:A*` labels | **`pr-signoff / check`** |
| `file-signoff.yml` | `aisignoff lint` on push, PR, merge queue; folder tree in the job summary, HTML report as artifact; file badges (generation, human review, AI review, findings) on `main`; **opens a setup PR if there is no `SIGNOFF.toml`**; optionally the report on Pages | **`file-signoff / lint`** |
| `signoff-badges.yml` | Badges of the declarations of merged PRs | none |
| `zensical-docs.yml` | Builds `docs/` + `zensical.toml` on PRs that touch them, deploys to Pages from `main` | none (path-filtered, see §4) |

Useful inputs (`with:` in the caller): `weight: lines` (File-signoff badges by lines; the Julia repos and the
playground use it), `aisignoff-version` (pin a different release than the org default, §10),
`setup: false`, `setup-history: false`, `pages: true` and `pages-path` (File-signoff, below),
`allow-policy-change: admin,maintain` (PR-signoff),
`zensical-version`, `deploy: false`.

The File-signoff template's caller has `pull-requests: write`; keep it, or the setup PR can't be opened (the
branch is still pushed and the job summary links to a prefilled PR).

**The report on Pages.** `pages: true` makes File-signoff deploy the HTML report to GitHub Pages on pushes to
`main`, at `https://industrial-mathematics-group.github.io/<repo>/signoff/` (`pages-path`, default `/signoff/`;
`/` for the root, which otherwise redirects to it). Needs *Settings → Pages → Source: GitHub Actions* and
`pages: write` + `id-token: write` in the caller (commented out in the template). A deployment replaces the whole
site: repositories with a docs site keep it off and use §6.

## 3. `SIGNOFF.toml`

**Easiest: let File-signoff set it up.** Add the workflow and push to `main` (or *Run workflow*). Without a
`SIGNOFF.toml` it skips the check with a warning and opens the PR *"Set up aisignoff (SIGNOFF.toml with TODOs to
fill in)"* from the branch `aisignoff-setup`, with the org defaults: `[history]` on, and a `**` annotation with
every level and `Reviewed-by` set to `TODO`.

1. Check out `aisignoff-setup`, fill in the `TODO`s with what is true for most of the repository, add
   annotations for folders that differ (`aisignoff annotate`), put files that need no declaration into `exclude`
   (e.g. `docs/build/**`). The review folder `reviews/` is left out by itself: no `exclude` for it.
2. Push. Checks only start with that push (GitHub doesn't run workflows on PRs opened by the workflow token);
   File-signoff stays red until no `TODO` is left.
3. Tick the human review box you did, merge. To get a fresh setup PR later, delete the `aisignoff-setup` branch.

**By hand:** `pipx install aisignoff==0.20.1`, then `aisignoff init -g … -H … -a … --reviewed-by … --history`
and `aisignoff annotate …`, then `aisignoff lint`. `init` also adds a section to `AGENTS.md` (and `CLAUDE.md`)
that points agents to `aisignoff guide`; `--no-agents-md` skips it, `aisignoff guide --agents-md` adds it later.

Typical content (see the playground):

```toml
version = 4
# exclude = ["docs/build/**"]   # reviews/ needs no entry: the review folder is left out by itself

[history]               # line-level declarations from git history
enabled = true
merge-method = "merge"  # must match how PRs land
# undeclared = "error"  # every commit landing on main must declare itself

[policy]                # minimum levels, read from the base branch
"*" = { human = "H1" }
G3  = { human = "H2", ai = "A1" }

[[annotations]]         # the LAST matching annotation wins
path = "**"
AI-Generation = "G0"
Human-Review = "H2"
AI-Review = "A0"
Reviewed-by = ["Jane Doe"]
```

A PR can't change `version`, `[policy]`, `exclude`, `[history]`, `[review] dir`, `.git-blame-ignore-revs` (or
delete `SIGNOFF.toml`): commit such changes to `main` directly (with `undeclared = "error"`, give the commit
"Key: value" lines), or set `allow-policy-change` on PR-signoff. `[review] recheck` is gone (findings block
nothing): `lint` warns until you delete it.

**Who writes what.** `SIGNOFF.toml` is the file a **person** signs off: rules, annotations, a person's reviews
(`attest -H`), corrections of a commit (`aisignoff correct REV`, a `[[commits]]` entry). AI reviews go into the
**review folder** `reviews/`: reports, A3 evidence (in a subfolder), and record files (`.toml` directly in the
folder, `[[attestations]]` with `AI-Review`, `AI-Reviewed-by`, `AI-Review-Findings` only). Agents never write
`SIGNOFF.toml`. To make that hold, give it a code owner and require their review:

```text
# .github/CODEOWNERS (with "Require review from Code Owners" in the ruleset)
/SIGNOFF.toml  @your-login
```

**Housekeeping.** Records that cover no line any more (deleted file, rewritten content) are no error; `lint`
counts them, `aisignoff gc --dry-run` lists them, `aisignoff gc` in a PR deletes them (the one deletion the
add-only review folder allows). There is no `freeze` or `SIGNOFF.snapshot.json` any more: every line is worked
out from the history, and a blame cache in `.git/aisignoff` keeps it fast (in CI: `actions/cache` on that path,
see aisignoff's docs, *The blame cache*).

## 4. Protect `main` (*Settings → Rules → Rulesets → New branch ruleset*)

- **Enforcement:** Active. **Target:** default branch (only; don't target `badges` or `aisignoff-setup`, the
  workflows push to them as `github-actions[bot]`).
- **Require a pull request before merging.** Approvals: 0 for one-maintainer repositories (you can't approve
  your own PR); allowed merge methods: Merge.
- **Require status checks to pass:** `pr-signoff / check`, and `file-signoff / lint` if the repository has
  `SIGNOFF.toml`. Add the CI/test jobs as usual. Checks appear in the picker only after they ran once.
- **Don't require `docs / build`** (or any other path-filtered check): it doesn't run on PRs that don't touch
  `docs/`, and those PRs would wait forever.
- **Block force pushes**, **Restrict deletions**.
- **Bypass list: empty** if `main` must really be protected. A bypass actor can push to `main` directly, and so
  can every tool or AI agent acting with that person's account (seen in a test: Claude with an admin's login
  pushed straight to `main`). A bypass also lifts **every** rule of its ruleset, force-push and deletion
  protection included.
- Need a way out for PRs whose checks can't pass (policy changes)? Add *Repository admin* in the mode **For pull
  requests only**, not *Always*: merging such a PR then works, direct pushes don't. Keep *Block force pushes* and
  *Restrict deletions* in a second ruleset without bypass. For policy changes, `allow-policy-change:
  admin,maintain` on PR-signoff is the alternative to any bypass.
- Agents that work as their own **GitHub App** (IMGAgent, or the agent-sandbox `github-app` add-on) have their
  own identity: they aren't on the bypass list, so they can't skip the rules.

## 5. README badges

Replace `<repo>` (e.g. `HyperCloudCore.jl`). File badges come from File-signoff, PR badges from Signoff-Badges;
both write to the `badges` branch, which the first run on `main` creates (*Run workflow* once to create it
now). The PR badges say "no declarations yet" until a declared PR is merged.

```markdown
[![AI policy](https://img.shields.io/badge/AI_policy-declared-9558B2.svg)](https://github.com/industrial-mathematics-group/.github/blob/main/.github/CONTRIBUTING.md#ai-assisted-contributions)
[![AI generation (files)](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/industrial-mathematics-group/<repo>/badges/aisignoff-generation.json)](<link>)
[![Human review (files)](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/industrial-mathematics-group/<repo>/badges/aisignoff-human-review.json)](<link>)
[![AI review (files)](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/industrial-mathematics-group/<repo>/badges/aisignoff-ai-review.json)](<link>)
[![AI review findings (files)](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/industrial-mathematics-group/<repo>/badges/aisignoff-findings.json)](<link>)
```

PR badges: the same with `ai-generation.json`, `ai-human-review.json`, `ai-review.json`. Link the file badges to
the published report (Julia: `https://industrial-mathematics-group.github.io/<repo>/dev/aisignoff/`) or to the
File-signoff workflow page.

## 6. Documentation

**Zensical (Python and other repositories).** *Settings → Pages → Source:* **GitHub Actions**; add
`zensical-docs.yml`; set `site_url = "https://industrial-mathematics-group.github.io/<repo>/"` in
`zensical.toml`. No site yet? Write `@IMGAgent make docs` in an issue: it opens a PR with `docs/` and a complete
`zensical.toml`. Later: `@IMGAgent update docs with src`, `@IMGAgent ask docs`.

**Documenter (Julia).** The report is a page of the docs, as in the four Julia repositories:

1. In the docs job of `CI.yml`: `fetch-depth: 0` on checkout, then before `make.jl`
   ```yaml
   - name: AI signoff report
     continue-on-error: true
     env:
       AISIGNOFF_VERSION: "0.20.1"   # keep at File-signoff's
       SINCE: ${{ github.event_name == 'pull_request' && 'origin/main' || '' }}
     run: |
       pipx run --spec "aisignoff==${AISIGNOFF_VERSION}" aisignoff report \
         --html docs/src/assets/aisignoff.html --title "<Package>.jl" --with-source ${SINCE:+--since "$SINCE"}
   ```
2. Copy `docs/src/aisignoff.md` (iframe on `assets/aisignoff.html`) from HyperCloudCore.jl and add
   `"AI Signoff Report" => "aisignoff.md"` to `pages` in `docs/make.jl`. `deploydocs` publishes it.
3. Add `docs/src/assets/aisignoff.html` to `.gitignore`.

## 7. IMGAgent

Install the App on the repository (it needs a `SIGNOFF.toml`). Then group members can write
`@IMGAgent signoff …` in an issue, in their own words, or use the issue form *Signoff: declare or attest files*;
IMGAgent opens a PR that changes `SIGNOFF.toml`, which they review, tick and merge. An AI review recorded this
way is one a person records, so it goes into `SIGNOFF.toml` (`attest --signoff`), and it needs its findings, A1
included. Repositories with their own
`.github/ISSUE_TEMPLATE/` must copy `signoff-request.yml` into it; optionally create the label
`signoff-request`.

Commands are action, then folders, then text (the old order `docs ask` gets a reminder): `@IMGAgent ask notes,
analysis` and a question (answers from those folders), `@IMGAgent update docs with src` and a task (a PR),
`@IMGAgent make docs` (a PR with a Zensical site), `@IMGAgent signoff` and your words, `@IMGAgent help`. Only
people with write access are answered; commands in code blocks or quotes are ignored.

## 8. Releases and Zenodo

- Add `CITATION.cff` (*Cite this repository*, and Zenodo's metadata).
- Once per repository: log in at zenodo.org with GitHub → *GitHub* → switch the repository **On**. Every
  published GitHub release is then archived with a **version DOI**; put the **concept DOI** badge in the README.
  Practise on sandbox.zenodo.org (real DOIs can't be deleted).
- **Julia:** TagBot creates the releases after a registration; `citation.yml` fails a PR whose `CITATION.cff`
  version differs from `Project.toml`, so bump `version` and `date-released` in the same PR.
- **Optional:** `signoff-release.yml` (from aisignoff's `examples/workflows/`, used in the playground) attaches
  `aisignoff-report.txt/.json/.html` to every published release.

## 9. PR messages: what maintainers check

- **Use the org template** (`.github/PULL_REQUEST_TEMPLATE.md`); repositories with their own template copy its
  "AI declaration" section unchanged. Tick, don't type: exactly one **G**; the model(s) for G1–G3; the highest
  **H** done (H0 at least); the highest **A** (none = A0).
- **A1–A3:** `AI-Review-Findings:` gives the review's highest finding in the change
  (`none`/`trivial`/`minor`/`major`/`critical`); any value passes, it is recorded (F0–F3 in the reports). A
  major or critical finding should be fixed and re-reviewed before the merge; the check doesn't enforce it.
- **A2/A3:** after *Model and report:* the reviewing model (not one that wrote it) and the report path, e.g.
  `GPT Sol (OpenAI), reviews/pull12.md`. The report must be added or changed **in this PR** (or be a link).
- **Review PRs** (a review of something already on `main`): only **add** files to `reviews/` (report, record
  file); the description needs no declaration. A PR that adds a record file and changes anything else fails, and
  so does any PR that modifies, deletes or renames a file in `reviews/` (except `gc`). A fix's re-review attests
  the reviewed commit and the fix in one new record file; the author never clears a finding.
- **PRs opened by bots or apps:** a line `Responsible person: @login` under the template comment.
- **No old trailer lines** (`AI-Generation: …`) next to ticked boxes: that's an error. Editing the description
  reruns the check; no new push needed.
- **Title:** the repo's commit style (e.g. `Area: what changed` in the HyperCloud repos); title and description
  become the merge commit message, so they're permanent.
- **Direct commits to `main`:** declare with "Key: value" lines in the message: `AI-Generation: G1`,
  `Assisted-by: …`, `Human-Review: H2`, `Reviewed-by: …`, `AI-Review: A0`.
- **Reviewer of record:** for a merge commit it's whoever clicked *Merge*; correct with a `[[commits]]` entry if
  that wasn't the reviewer.
- Dependabot and CompatHelper PRs skip PR-signoff; other bots and AI agents don't.
- **Agents:** `aisignoff guide --role dev` (writing) and `--role review` (reviewing) are their one-page briefs;
  `guide --skills` writes them as Claude skills.

## 10. Updating aisignoff

The org pins aisignoff in the reusable workflows (`aisignoff-version` in `file-signoff.yml` and
`pr-signoff.yml`). On 24 November 2026 the default is **0.18.0**; raise both to **0.20.1** to get 0.19's rules
(below), and the fixes and syntax colours of 0.19.1–0.20.1. Raising it there updates every repository at once:
read the changelog for **Breaking** first ([Upgrading](https://industrial-mathematics-group.github.io/aisignoff/migrating/)).
Keep the Julia docs step (`AISIGNOFF_VERSION`, already 0.20.1 in the four Julia repositories) and the
playground's own workflows on the same release. (aisignoff went back to 0.x: 0.15.0 follows 1.0.0rc10.)

| From | What changed for a repository |
|---|---|
| 1.0.0rc8 → rc10 | Findings are recorded, not a threshold (`[review] recheck` gone); a fourth axis F0–F3/F-; **A1 gives its findings** too |
| 0.16 | The review folder `reviews/`: needs no declaration, add-only, record files of AI reviews |
| 0.17 | `freeze` and `SIGNOFF.snapshot.json` removed (`unfreeze.py` converts); blame cache instead |
| 0.18 | `attest -a` writes a record file in `reviews/` (`--signoff`: into `SIGNOFF.toml`); `correct`, `gc` |
| 0.19 | AI reviews count in the order recorded; `[review] dir` protected; only top-level `.toml` in `reviews/` are records; a record file comes in a PR of its own, with a report the PR adds |

## Red check? Quick fixes

| Symptom | Fix |
|---|---|
| File-signoff yellow "aisignoff not set up" | Merge the `aisignoff-setup` PR (or `aisignoff init`) |
| "A1 needs a line 'AI-Review-Findings:'" | Fill in the line below the A boxes (`none` if nothing was found) |
| "the change modifies reviews/…" | The review folder is add-only: record the new review in a new file |
| "adds the review record … and also changes …" | Put the record file into a PR of its own; the change's own review goes into its description |
| `lint` fails on `SIGNOFF.snapshot.json` | Run `unfreeze.py` from aisignoff's examples (with 0.17 or later) and commit the result |
| `lint` warns about `[review] recheck` | Delete it on `main` directly (it is no longer read) |
| No setup PR, only a branch | Org/repo setting *Allow GitHub Actions to create … pull requests*, and `pull-requests: write` in the caller |
| Setup PR has no checks | Push a commit to `aisignoff-setup` |
| PR-signoff fails on a `SIGNOFF.toml` change | Policy-type change: commit to `main` directly, or `allow-policy-change` |
| Badges show "no declarations yet" forever | Merge message not set to *title and description*, or `badges` branch protected |
| Docs build fails "No zensical.toml" | `@IMGAgent make docs`, or `zensical new` |
| Pages 404 | *Settings → Pages → Source: GitHub Actions*; File-signoff's report is under `/signoff/` (default `pages-path`) |
| File-signoff `pages` job: "Couldn't deploy" | Pages source, or `pages: write` / `id-token: write` missing in the caller |
| Required check never starts | It's path-filtered or renamed: required names are `<caller job> / <job>` |
