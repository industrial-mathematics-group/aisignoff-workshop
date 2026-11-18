[← 4 IMGAgent](04-imgagent.md) · **5 The report on GitHub Pages** · [6 Releases and DOIs →](06-zenodo.md)

# 5 · The report on GitHub Pages

aisignoff can draw an **interactive report** of a repository, like a coverage report for AI use: a sunburst
of the folders, a table per folder, and every file line by line, coloured by its levels. GitHub Pages
publishes it as a website at `https://industrial-mathematics-group.github.io/<your repository>/aisignoff/`.
File-signoff writes the report on every run already; one switch makes it publish it too.

## Step 1 · Turn Pages on (1 min)

**Settings → Pages → Build and deployment → Source:** **GitHub Actions**.

## Step 2 · Switch it on in File-signoff, as a pull request (5 min)

1. In your repository, open `.github/workflows/file-signoff.yml` and click the **pencil** (*Edit this file*).
2. Under `permissions:`, remove the `# ` in front of the two lines `pages: write` and `id-token: write`.
3. At the bottom, remove the `# ` in front of `with:` and of `pages: true`. Keep the indentation: `with:` lines
   up with `uses:`, and `pages: true` is two spaces further in. The changed parts then look like this:

   ```yaml
   permissions:
     contents: write
     pull-requests: write   # only for the setup pull request in a repository without SIGNOFF.toml
     pages: write          # with "pages: true" below: publish the report on GitHub Pages
     id-token: write       # (both lines, and Settings → Pages → Source: "GitHub Actions")

   jobs:
     file-signoff:
       uses: industrial-mathematics-group/.github/.github/workflows/file-signoff.yml@main
       with:
       #   weight: lines                 # weight the badges by lines instead of files
       #   ...
         pages: true                   # publish the folder report on GitHub Pages (replaces the Pages site)
       #   pages-path: /aisignoff/       # where in the site: https://<owner>.github.io/<repo>/aisignoff/ ("/": the root)
   ```

   The other lines stay commented out. `pages-path` moves the report elsewhere in the site, for example
   `pages-path: /` for the front page; the default `/aisignoff/` is what we use today.
4. **Commit changes… → Create a new branch … and start a pull request → Propose changes → Create pull request.**
5. Declare it: you changed the lines yourself, following this page, so **G0**, **A0**, and **H1** (you read what
   you changed).
6. Green: **Merge pull request → Confirm merge.**

✅ **Check:** **Actions → File-signoff →** the run on `main` now has a fourth job, **pages** (about a minute
after lint). Its summary shows the address of the report.

## Step 3 · Look at your report (5 min)

Open `https://industrial-mathematics-group.github.io/workshop-jane-doe/aisignoff/` (with your repository's name; the
address without `aisignoff/` leads there too). To have the link on your front page: the **⚙** next to *About* →
tick **Use your GitHub Pages website** → **Save**.

- **Sunburst:** click a folder to zoom in, the centre to go back.
- **Axis buttons:** colour by **Generation**, **Human review**, **AI review**, or the **Review gap**
  (generation minus human review: where AI did a lot and people checked little).
- **A file:** its levels, who reviewed it, where the declaration comes from, and every line with its level
  in the margin. Hover the margin.
- **Find:** type part of a path to jump to it. The address keeps the view, so you can send a link to one file.

Things to try: find the folder with the biggest review gap. Make it smaller (part 4's attestation, or a review by
a colleague) and watch the report change after the next merge.

> The report is public, with the text of every file, like the repository itself. A repository has one Pages
> site, and each deployment replaces all of it: a repository with a documentation site leaves `pages` off and
> writes the report into that site instead (see the [maintainer cheat sheet](maintainer-cheat-sheet.md#6-documentation)).

---

[← 4 IMGAgent](04-imgagent.md) · [6 Releases and DOIs →](06-zenodo.md)
