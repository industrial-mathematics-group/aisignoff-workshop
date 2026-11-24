"""Walk through the workshop's exercises (parts 3-7) in a local git repository, the way GitHub and the
organisation's workflows would: every pull request is checked like PR-signoff does it
(aisignoff lint --declare-from on the merge preview, --base HEAD^1), merged with a merge commit whose message
is the title and description, and main is linted like File-signoff does it.

Usage (from the repository root, with the aisignoff release under test installed):

    curl -sO https://raw.githubusercontent.com/industrial-mathematics-group/.github/main/.github/PULL_REQUEST_TEMPLATE.md
    python tools/walkthrough.py /tmp/walkthrough sample-project PULL_REQUEST_TEMPLATE.md \
        templates/CITATION.cff templates/signoff-release.yml

It prints one line per check (OK or BAD, with the labels PR-signoff would set), the folder tree at the end,
and exits non-zero if a check didn't come out as the workshop says.
"""
import os, re, shutil, subprocess, sys, textwrap
from pathlib import Path

work, sample, template = map(Path, sys.argv[1:4])
TEMPLATE = template.read_text()
TEMPLATE = TEMPLATE[TEMPLATE.index("## AI declaration"):]  # the part the participants tick
if work.exists():
    shutil.rmtree(work)
work.mkdir(parents=True)
origin, repo = work / "origin.git", work / "repo"
ENV = dict(os.environ, GIT_AUTHOR_NAME="Jane Doe", GIT_AUTHOR_EMAIL="jane@example.org",
           GIT_COMMITTER_NAME="Jane Doe", GIT_COMMITTER_EMAIL="jane@example.org", AISIGNOFF_NO_CACHE="")
results = []


def sh(*cmd, check=True, cwd=None):
    p = subprocess.run(cmd, cwd=cwd or repo, env=ENV, text=True, capture_output=True)
    if check and p.returncode:
        raise SystemExit(f"FAILED {' '.join(cmd)}\n{p.stdout}\n{p.stderr}")
    return p


def git(*a, **k):
    return sh("git", *a, **k)


def desc(ticks=(), other="", a1_model="", model_report="", findings="", responsible=None, what="", template=TEMPLATE):
    """The organisation's PR template's AI declaration, ticked like a participant would."""
    d = template
    for t in ticks:
        d, n = re.subn(r"^- \[ \] (\*\*" + re.escape(t) + r"\*\*)", r"- [x] \1", d, count=1, flags=re.M)
        assert n, t
    if other:
        d = d.replace("- [ ] **Other:** ", f"- [x] **Other:** {other}")
    if a1_model:
        d = re.sub(r"(\*\*A1\*\*.*Model, if not one of the above: )", r"\g<1>" + a1_model, d)
    if model_report:
        d = re.sub(r"(- \[x\] \*\*A[23]\*\*.*Model and report: )", r"\g<1>" + model_report, d)
    d = d.replace("AI-Review-Findings: ", "AI-Review-Findings: " + findings)
    if responsible:
        end = d.index("-->") + 3
        d = d[:end] + f"\n\nResponsible person: @{responsible}\n" + d[end:]
    return f"## What does this PR change?\n\n{what}\n\n" + d


def write(path, text):
    p = repo / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)


def direct(msg, files):
    """A commit straight to main (before main is protected), as the browser makes it."""
    git("checkout", "-q", "main", check=False)
    for path, text in files.items():
        write(path, text)
    git("add", "-A")
    git("commit", "-q", "-m", msg)
    git("push", "-q", "origin", "main")


PR = [0]


def pull_request(name, title, change, description, author="jane-doe", expect=0, merge=True):
    """change(): edits on the branch. Runs PR-signoff's check on the merge preview, then merges."""
    PR[0] += 1
    n = PR[0]
    branch = f"pr{n}"
    git("checkout", "-q", "-B", branch, "origin/main")
    change()
    git("add", "-A")
    git("commit", "-q", "-m", f"Update for {title}")
    # GitHub's merge preview
    git("checkout", "-q", "--detach", "origin/main")
    git("merge", "-q", "--no-ff", branch, "-m", f"Merge {branch} into main")
    dfile = work / f"pr{n}.md"
    dfile.write_text(description)
    args = ["--declare-from", str(dfile), "--author", author, "--base", "HEAD^1"]
    p = sh("aisignoff", "lint", *args, check=False)
    rep = sh("aisignoff", "report", "--json", *args, check=False)
    labels = ""
    try:
        import json
        pr = json.loads(rep.stdout).get("pull_request") or {}
        if pr.get("applies"):
            labels = f"{pr.get('AI-Generation')} {pr.get('Human-Review')} {pr.get('AI-Review')}"
            if pr.get("AI-Review-Findings"):
                labels += f" findings {pr['AI-Review-Findings']}"
    except Exception:
        pass
    ok = (p.returncode == 0) == (expect == 0)
    results.append((f"PR #{n} {name}", p.returncode, expect, ok, labels, (p.stdout + p.stderr).strip()))
    if merge and p.returncode == 0:
        git("checkout", "-q", "main")
        git("merge", "-q", "--no-ff", branch, "-m", f"{title} (#{n})\n\n{description}")
        git("push", "-q", "origin", "main")
        main_lint(f"main after PR #{n}")
    git("checkout", "-q", "main")
    return p


def main_lint(name, expect=0):
    git("checkout", "-q", "main")
    p = sh("aisignoff", "lint", check=False)
    ok = (p.returncode == 0) == (expect == 0)
    results.append((f"File-signoff on {name}", p.returncode, expect, ok, "", (p.stdout + p.stderr).strip()))
    return p


# ---- setup: an empty repository in the organisation
sh("git", "init", "-q", "--bare", "-b", "main", str(origin), cwd=work)
sh("git", "clone", "-q", str(origin), str(repo), cwd=work)
git("symbolic-ref", "HEAD", "refs/heads/main")

# 3 A: upload the example project (browser commit, no declaration)
files = {str(p.relative_to(sample)): p.read_text() for p in sample.rglob("*") if p.is_file()}
direct("Add the coffee cooling project", files)

# 3 C: the three workflow callers, committed to main directly (stubs: their content doesn't matter here)
for wf in ("pr-signoff", "signoff-badges", "file-signoff"):
    direct(f"Create {wf}.yml", {f".github/workflows/{wf}.yml": f"# {wf} caller\nname: {wf}\n"})

# 3 D: the setup pull request, as File-signoff opens it: SIGNOFF.toml from aisignoff init with TODOs
git("checkout", "-q", "-B", "aisignoff-setup", "origin/main")
sh("aisignoff", "init", "-g", "TODO", "-H", "TODO", "-a", "TODO", "--history", "--no-agents-md")
git("add", "SIGNOFF.toml")
git("commit", "-q", "-m", "Set up aisignoff with the organisation's defaults")
git("push", "-q", "origin", "aisignoff-setup")
p = sh("aisignoff", "lint", check=False)
results.append(("setup branch with TODOs (File-signoff red)", p.returncode, 1, p.returncode != 0, "", (p.stdout + p.stderr).strip()))


def fill_todos():
    sh("aisignoff", "init", "-g", "TODO", "-H", "TODO", "-a", "TODO", "--history", "--no-agents-md")
    s = (repo / "SIGNOFF.toml").read_text()
    s = s.replace('AI-Generation = "TODO"', 'AI-Generation = "G0"').replace('Human-Review = "TODO"', 'Human-Review = "H2"')
    s = s.replace('AI-Review = "TODO"', 'AI-Review = "A0"').replace('Reviewed-by = ["TODO"]', 'Reviewed-by = ["Jane Doe"]')
    (repo / "SIGNOFF.toml").write_text(s)


setup_desc = desc(["G0", "A0"], responsible="jane-doe", what="Set up aisignoff")
git("checkout", "-q", "main")
git("branch", "-q", "-D", "aisignoff-setup")
pull_request("setup PR, only G0 and A0 ticked (step D.5: red)", "Set up aisignoff",
             fill_todos, setup_desc, author="github-actions[bot]", expect=1, merge=False)
PR[0] -= 1
pull_request("setup PR, H2 ticked (step D.6)", "Set up aisignoff (SIGNOFF.toml with TODOs to fill in)",
             fill_todos, desc(["G0", "H2", "A0"], responsible="jane-doe", what="Set up aisignoff"),
             author="github-actions[bot]")

# 3 F: badges in the README
BADGES = "[![AI generation](https://img.shields.io/endpoint?url=...)](...)\n" * 4


def add_badges():
    write("README.md", BADGES + (repo / "README.md").read_text())


pull_request("README badges, G0 and G1 ticked (F.3: break it)", "Add badges", add_badges,
             desc(["G0", "G1", "H2", "A0"]), expect=1, merge=False)
PR[0] -= 1
pull_request("README badges, nothing ticked (F.2: red)", "Add badges", add_badges, desc([]), expect=1, merge=False)
PR[0] -= 1
pull_request("README badges, G0 H2 A0 (F.4)", "Add the badges to the README", add_badges, desc(["G0", "H2", "A0"]))


# 4 exercise 2: three IMGAgent signoff pull requests (aisignoff annotate, as IMGAgent runs it)
def annotate(*args):
    return lambda: sh("aisignoff", "annotate", *args)


imgagent = desc(["G1", "H2", "A0"], other="IMGAgent", responsible="jane-doe", what="Declare a folder (signoff request)")
pull_request("IMGAgent: Declare analysis/", "Declare analysis/ (signoff request #3)",
             annotate("analysis/", "-g", "G2", "-H", "H1", "-a", "A0", "--assisted-by", "Claude Opus 5.5 (Anthropic)",
                      "--reviewed-by", "Jane Doe"), imgagent, author="imgagent[bot]")
pull_request("IMGAgent: Declare results/", "Declare results/ (signoff request #5)",
             annotate("results/", "-g", "G3", "-H", "H1", "-a", "A0", "--assisted-by", "Claude Opus 5.5 (Anthropic)",
                      "--reviewed-by", "Jane Doe"), imgagent, author="imgagent[bot]")
pull_request("IMGAgent: Declare paper/", "Declare paper/ (signoff request #7)",
             annotate("paper/", "-g", "G1", "-H", "H2", "-a", "A0", "--assisted-by", "GPT Sol (OpenAI)",
                      "--reviewed-by", "Jane Doe"), imgagent, author="imgagent[bot]")

# 4 optional: an A1 attestation recorded by IMGAgent into SIGNOFF.toml (attest --signoff)
git("checkout", "-q", "main")
p = sh("aisignoff", "attest", "analysis/fit_cooling.py", "-a", "A1", "--signoff",
       "--ai-reviewed-by", "Claude Opus 5.5 (Anthropic), new session", check=False)
results.append(("attest -a A1 without --findings is refused", p.returncode, 1, p.returncode != 0, "", (p.stdout + p.stderr).strip()))
git("checkout", "-q", "--", ".")
pull_request("IMGAgent: A1 attestation, findings none", "Attest analysis/fit_cooling.py (signoff request #9)",
             lambda: sh("aisignoff", "attest", "analysis/fit_cooling.py", "-a", "A1", "--findings", "none", "--signoff",
                        "--ai-reviewed-by", "Claude Opus 5.5 (Anthropic), new session without the generating conversation"),
             imgagent, author="imgagent[bot]")


# 4 optional (new): an independent AI review as a review pull request: report + record file, nothing else
def upload_sha():
    return git("log", "--format=%H", "--grep", "Add the coffee cooling project", "origin/main").stdout.strip()


REPORT = "# Review of analysis/fit_cooling.py\n\nModel: GPT Sol (OpenAI)\n\n## Findings\n\n- minor: the fit ignores ...\n"


def review_pr(record_extra="", findings='"minor"', also=None, report=True):
    def change():
        if report:
            write("reviews/fit-cooling.md", REPORT)
        write("reviews/fit-cooling.toml", textwrap.dedent(f"""\
            [[attestations]]
            commit = "{upload_sha()}"
            path = "analysis/fit_cooling.py"
            AI-Review = "A2"
            AI-Reviewed-by = "GPT Sol (OpenAI), reviews/fit-cooling.md"
            AI-Review-Findings = {findings}
            """) + record_extra)
        if also:
            also()
    return change


pull_request("review PR: record file without findings (red)", "Review of fit_cooling.py",
             review_pr(findings='""'.replace('""', '"TODO"')), desc([]), expect=1, merge=False)
PR[0] -= 1
pull_request("review PR: record file without its report (red)", "Review of fit_cooling.py",
             review_pr(report=False), desc([]), expect=1, merge=False)
PR[0] -= 1
pull_request("review PR: record file + an edit elsewhere (red)", "Review of fit_cooling.py",
             review_pr(also=lambda: write("notes/lab-notes.md", (repo / "notes/lab-notes.md").read_text() + "\nmore\n")),
             desc(["G0", "H2", "A0"]), expect=1, merge=False)
PR[0] -= 1
pull_request("review PR: report + record file, description untouched", "Review of analysis/fit_cooling.py (A2, findings: minor)",
             review_pr(), desc([]))


def edit_review():
    write("reviews/fit-cooling.md", REPORT + "\nedited\n")


pull_request("edit of an earlier review (add-only: red)", "Fix the review", edit_review, desc(["G0", "H2", "A0"]),
             expect=1, merge=False)
PR[0] -= 1

# 5: switch pages on in file-signoff.yml
pull_request("Pages switch (G0 H1 A0)", "Publish the report on GitHub Pages",
             lambda: write(".github/workflows/file-signoff.yml", "# file-signoff caller\nname: file-signoff\n# pages: true\n"),
             desc(["G0", "H1", "A0"]))

# 6: CITATION.cff and signoff-release.yml
pull_request("CITATION.cff (G1 Claude Opus H2 A0)", "Add a citation file",
             lambda: write("CITATION.cff", Path(sys.argv[4]).read_text()), desc(["G1", "Claude Opus", "H2", "A0"]))
pull_request("signoff-release.yml, A1 without findings (red)", "Attach the report to releases",
             lambda: write(".github/workflows/signoff-release.yml", Path(sys.argv[5]).read_text()),
             desc(["G3", "Claude Opus", "H1", "A1"], a1_model="GPT Sol (OpenAI)"), expect=1, merge=False)
PR[0] -= 1
pull_request("signoff-release.yml (G3 Claude Opus H1 A1, findings none)", "Attach the report to releases",
             lambda: write(".github/workflows/signoff-release.yml", Path(sys.argv[5]).read_text()),
             desc(["G3", "Claude Opus", "H1", "A1"], a1_model="GPT Sol (OpenAI)", findings="none"))

# 7.1: an agent's pull request (G3, its model; the person ticks H1)
pull_request("agent PR, human review not ticked yet (red)", "Abstract: the main limitation",
             lambda: write("paper/abstract.md", (repo / "paper/abstract.md").read_text() + "\nOne limitation ...\n"),
             desc(["G3", "Claude Opus", "A0"]), expect=1, merge=False)
PR[0] -= 1
pull_request("agent PR, H1 ticked", "Abstract: the main limitation",
             lambda: write("paper/abstract.md", (repo / "paper/abstract.md").read_text() + "\nOne limitation ...\n"),
             desc(["G3", "Claude Opus", "H1", "A0"]))

# the report at the end
git("checkout", "-q", "main")
tree = sh("aisignoff", "report", "--tree", check=False).stdout
gc = sh("aisignoff", "gc", "--dry-run", check=False)
sh("aisignoff", "report", "--html", str(work / "report.html"), "--with-source", check=False)

bad = 0
for name, rc, exp, ok, labels, out in results:
    bad += not ok
    print(f"{'OK ' if ok else 'BAD'} exit {rc} (expected {'0' if exp == 0 else 'non-zero'})  {name}  {labels}")
    if not ok or rc:
        print(textwrap.indent(out[-1500:], "      | "))
print("\n--- aisignoff report --tree on main ---\n" + tree)
print("--- gc --dry-run ---\n" + gc.stdout + gc.stderr)
print(f"\n{len(results) - bad} of {len(results)} as expected")
sys.exit(1 if bad else 0)
