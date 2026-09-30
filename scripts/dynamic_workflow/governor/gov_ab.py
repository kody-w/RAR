"""Governor's A/B for one proven branch: the tests the branch ADDED must pass on the branch and fail on the base
SOURCE. The base tree is the branch's own export with every changed non-test file put back as the base had it
(files the branch added outside tests/ removed) - the branch's test code, helpers included, runs against the base's
code. Both run in clean exports (git archive), never in a builder's worktree. Prints one line; exit 0 iff it holds.
Usage: python3 gov_ab.py <repo> <base> <branch-or-commit> [scratch_dir]"""
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile

repo, base, ref = sys.argv[1], sys.argv[2], sys.argv[3]
scratch = sys.argv[4] if len(sys.argv) > 4 else os.path.join(os.environ.get("RAPP_WORKFLOWS_HOME") or os.path.expanduser("~/.rapp/workflows"), "governor", "ab")
os.makedirs(scratch, exist_ok=True)


def git(*a):
    return subprocess.run(["git", "-C", repo] + list(a), capture_output=True, text=True, check=True).stdout


def export(rev, into):
    shutil.rmtree(into, ignore_errors=True)
    os.makedirs(into)
    data = subprocess.run(["git", "-C", repo, "archive", rev], capture_output=True, check=True).stdout
    with tempfile.TemporaryFile() as f:
        f.write(data)
        f.seek(0)
        with tarfile.open(fileobj=f) as t:
            t.extractall(into)


def run(tree, modules):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    r = subprocess.run(["/usr/bin/python3", "-m", "unittest"] + modules, cwd=tree, capture_output=True, text=True, env=env, timeout=3600)
    tail = [l for l in r.stderr.strip().splitlines() if l.strip()]
    ran = next((l for l in reversed(tail) if l.startswith("Ran ")), "Ran ? tests")
    return r.returncode == 0, ran.split(" in ")[0] + " -> " + (tail[-1] if tail else "?")


added = [p for p in git("diff", "--name-only", "--diff-filter=A", base + ".." + ref, "--", "tests").split() if re.match(r"tests/test_[^/]+\.py$", p)]
if not added:
    print("%s: NO NEW TEST MODULE - nothing to A/B" % ref)
    sys.exit(1)
modules = [p[:-3].replace("/", ".") for p in added]
name = re.sub(r"[^A-Za-z0-9_.-]+", "-", ref)
fix_dir, base_dir = os.path.join(scratch, name + "-fix"), os.path.join(scratch, name + "-base")
export(ref, fix_dir)
export(ref, base_dir)
put_back = 0
for row in git("diff", "--name-status", "--no-renames", base + ".." + ref).splitlines():
    st, path = row.split("\t", 1)
    if path.startswith("tests/"):
        continue
    target = os.path.join(base_dir, path)
    if st == "A":
        os.remove(target)
    else:
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "wb") as f:
            f.write(subprocess.run(["git", "-C", repo, "show", "%s:%s" % (base, path)], capture_output=True, check=True).stdout)
    put_back += 1
fix_ok, fix_line = run(fix_dir, modules)
base_ok, base_line = run(base_dir, modules)
holds = fix_ok and not base_ok
print("%s  %s  | fix: %s | base %s (%d source files put back): %s | %s" % (
    "A/B HOLDS" if holds else "A/B DOES NOT HOLD", ref, fix_line, base, put_back, base_line, " ".join(modules)))
shutil.rmtree(fix_dir, ignore_errors=True)
shutil.rmtree(base_dir, ignore_errors=True)
sys.exit(0 if holds else 1)
