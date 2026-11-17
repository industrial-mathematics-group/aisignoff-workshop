[← 4 IMGAgent](04-imgagent.md) · **5 The report on GitHub Pages** · [6 Releases and DOIs →](06-zenodo.md)

# 5 · The report on GitHub Pages

aisignoff can draw an **interactive report** of a repository, like a coverage report for AI use: a sunburst
of the folders, a table per folder, and every file line by line, coloured by its levels. GitHub Pages
publishes it as a website at `https://industrial-mathematics-group.github.io/<your repository>/`.

## Step 1 · Turn Pages on (1 min)

**Settings → Pages → Build and deployment → Source:** **GitHub Actions**.

## Step 2 · Add the Pages workflow, as a pull request (5 min)

1. Open [`templates/signoff-pages.yml`](templates/signoff-pages.yml) in this workshop repository and copy its
   text (the copy icon at the top right of the file view).
2. In your repository: **Add file → Create new file.** As the name, type
   `.github/workflows/signoff-pages.yml` (the slashes make the folders). Paste the text.
3. **Commit changes… → Create a new branch … and start a pull request → Propose changes → Create pull request.**
4. Declare it. You didn't write this file; it comes from the
   [aisignoff examples](https://github.com/industrial-mathematics-group/aisignoff/tree/main/examples/workflows),
   which declare it as made by Claude Opus and checked by a new session. So: **G3**, **Claude Opus**, **A1**,
   and your human review of what you read (**H0** if you only skimmed it, **H1** if you read the important
   parts). A copied file keeps its origin.
5. Green: **Merge pull request → Confirm merge.**

✅ **Check:** **Actions → aisignoff report on Pages** runs on `main` (about a minute). Its summary shows the
address of the site.

## Step 3 · Look at your report (5 min)

Open `https://industrial-mathematics-group.github.io/workshop-jane-doe/` (with your repository's name). To have
the link on your front page: the **⚙** next to *About* → tick **Use your GitHub Pages website** → **Save**.

- **Sunburst:** click a folder to zoom in, the centre to go back.
- **Axis buttons:** colour by **Generation**, **Human review**, **AI review**, or the **Review gap**
  (generation minus human review: where AI did a lot and people checked little).
- **A file:** its levels, who reviewed it, where the declaration comes from, and every line with its level
  in the margin. Hover the margin.
- **Find:** type part of a path to jump to it. The address keeps the view, so you can send a link to one file.

Things to try: find the folder with the biggest review gap. Make it smaller (part 4's attestation, or a review by
a colleague) and watch the report change after the next merge.

> The report is public, with the text of every file, like the repository itself. A repository has one Pages
> site: one with a documentation site writes the report into that site instead (see the
> [maintainer cheat sheet](maintainer-cheat-sheet.md#6-documentation)).

---

[← 4 IMGAgent](04-imgagent.md) · [6 Releases and DOIs →](06-zenodo.md)
