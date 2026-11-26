# Workshop: GitHub and AI signoff

**Friday, 27 November 2026 · Industrial Mathematics Group · everything in the web browser · aisignoff 0.24.0**

In this workshop you set up **your own repository** the way the group's repositories are set up (a fresh
workshop repository, or a real one of yours that you bring along): the AI signoff checks, the protection of `main`, the IMGAgent assistant, a documentation website with the report, and a DOI from Zenodo. IMGAgent writes the configuration files for you from forms: no manual setup.
Pascal does every step at the same time on this repository, on the projector.

| | Part | What you do |
|---|---|---|
| 0 | [Before the workshop](00-before-the-workshop.md) | Create an empty repository, or bring your own. **Please do this beforehand** |
| 1 | [GitHub in five words](01-git-and-github.md) | Repository, commit, branch, pull request, merge, as pictures |
| 2 | [AI signoff in plain words](02-ai-signoff.md) | Why we declare AI use, the G · H · A levels and the review findings, who is responsible |
| 3 | [Set up your repository](03-setup.md) | Add the example files, settings, workflows, `SIGNOFF.toml` with IMGAgent, protect `main`, first pull request |
| 4 | [IMGAgent](04-imgagent.md) | Ask your repository questions, sign off files in your own words, let it review a folder |
| 5 | [A website with the report](05-pages.md) | A documentation site on GitHub Pages, with the interactive aisignoff report of your repository |
| 6 | [Releases and DOIs](06-zenodo.md) | Connect Zenodo, add a citation with IMGAgent, publish a release |
| 7 | [Advanced: working with AI agents](07-advanced.md) | Demonstration: an agent opens a pull request, you inspect and merge it; and an advanced setup with sandboxes and the cluster |

**Take home:** the [cheat sheet](cheat-sheet.md) ([PDF](cheat-sheet.pdf)) for everyday work, and the
[maintainer cheat sheet](maintainer-cheat-sheet.md) ([PDF](maintainer-cheat-sheet.pdf)) for setting up a repository.

## What's in this repository

| Path | What it is |
|---|---|
| `00-…` to `07-…` | The workshop, one page per part |
| [`sample-project/`](sample-project/) and [`sample-project.zip`](sample-project.zip) | A tiny made-up research project (coffee cooling) that you put into your repository: something to declare and to ask about |
| [`templates/`](templates/) | A file to copy into your repository: the release workflow |
| `cheat-sheet.*`, `maintainer-cheat-sheet.*` | The two cheat sheets |
| [`facilitator-guide.md`](facilitator-guide.md) | For whoever runs the session |
| [`tools/walkthrough.py`](tools/walkthrough.py) | Replays the exercises of parts 3 to 7 in a local git repository with aisignoff, as PR-signoff and File-signoff would check them |

## Ground rules

- **Repositories here are public.** Don't put unpublished results, data about people, passwords or anything
  confidential into them, or into an AI tool.
- **Nothing can break.** A workshop repository is yours to try things in, and to delete afterwards. If you
  bring a real repository, you'll change its settings and add files through pull requests only.
- **You are responsible for what you merge**, whoever or whatever wrote it. That's the one idea behind AI signoff.
