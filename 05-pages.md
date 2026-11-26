[← 4 IMGAgent](04-imgagent.md) · **5 A website with the report** · [6 Releases and DOIs →](06-zenodo.md)

# 5 · A website with the report

aisignoff can draw an **interactive report** of a repository, like a coverage report for AI use: a sunburst
of the folders, a table per folder, and every file line by line, coloured by its levels. It belongs on the
repository's **documentation website**, next to the docs: GitHub Pages publishes the site at
`https://www.industrial-mathematics.org/<your repository>/`, and the report at `…/signoff/`. IMGAgent sets the
site up, and the group's *Zensical docs* workflow builds it with the report on every change to `main`.

## Step 1 · Turn Pages on (1 min)

**Settings → Pages → Build and deployment → Source:** **GitHub Actions**.

## Step 2 · Set up the site with IMGAgent (5 min)

1. **Issues → New issue.** Title: `Documentation site`. Text: `@IMGAgent setup docs`. **Create.**
2. IMGAgent answers with a form: the site's name and description (from your repository) and its address.
   Set the address to `https://www.industrial-mathematics.org/workshop-jane-doe/` with your repository's name
   (**⋯ → Edit**, change the text between the backticks, **Update comment**).
3. Tick **Done**. The pull request **Set up zensical.toml** adds the site's settings, `zensical.toml`, and a
   first page, `docs/index.md`. Written from the form, without AI: **G0** is ticked. Tick your human review,
   merge.

Want real pages instead of the placeholder? `@IMGAgent make docs` has Claude write `docs/` from your files,
as a pull request declared G3. Optional, and it takes a few minutes.

## Step 3 · Add the Zensical docs workflow (5 min)

1. **Actions → New workflow → Zensical docs → Configure.** Don't change anything.
2. **Commit changes… → Create a new branch for this commit and start a pull request → Propose changes →
   Create pull request.** (`main` is protected since part 3, so even a workflow comes as a pull request.)
3. Declare it like the REUSE workflow: a file copied from the group's templates, which were written with Claude:
   **G3**, **Claude Opus**, **H1** (you read it), **A0**. The check **docs / build** builds the site once as a
   test: wait for it to turn green.
4. **Merge pull request → Confirm merge.**

✅ **Check:** **Actions → Zensical docs →** the run on `main` has two jobs, **build** and **deploy** (about a
minute). The summary of **build** says *AI signoff report: added to the site at `signoff/index.html`*, and
**deploy** shows the address of the site.

## Step 4 · Look at your report (5 min)

Open `https://www.industrial-mathematics.org/workshop-jane-doe/signoff/` (with your repository's name; without
`signoff/` you get the site's front page). To have the link on your repository's front page: the **⚙** next to
*About* → tick **Use your GitHub Pages website** → **Save**.

- **The header:** the mix of each axis, and two flags: the share of lines **without independent AI review**
  (F-) and the share with an **open major or critical finding** (F2, F3).
- **Sunburst:** click a folder to zoom in, the centre to go back.
- **Axis buttons:** colour by **Generation**, **Human review**, **AI review** or **Findings** (F0 to F3, and
  F- in grey for lines no independent AI review has seen since they last changed). **Folder colour** chooses
  how a folder sums up its files: the average, the majority, or the weakest link.
- **A file:** its levels, who reviewed it, where the declaration comes from, and every line with its level
  in the margin, with syntax colours as on GitHub. Hover the margin.
- **Find:** type part of a path to jump to it. The address keeps the view, so you can send a link to one file.

Things to try: switch to **Generation**, then **Human review**: where did AI do a lot and people check little?
Then **Findings**: which of those has never had an independent review (F-)? IMGAgent's review in part 4 changed that
for `analysis/`: its files show their own findings colour. Review another folder and watch it change.

The workflow rebuilds the site on every push to `main`, so the report stays current. On a pull request it builds
the site with the report too, marks the lines the pull request changes, and keeps the built site as the
artifact **site** of the run (*Actions →* the run *→ Artifacts*).

> The report is public, with the text of every file, like the repository itself. Repositories with a Julia
> package put it into their Documenter docs instead (see the [maintainer cheat sheet](maintainer-cheat-sheet.md#6-documentation)).

---

[← 4 IMGAgent](04-imgagent.md) · [6 Releases and DOIs →](06-zenodo.md)
