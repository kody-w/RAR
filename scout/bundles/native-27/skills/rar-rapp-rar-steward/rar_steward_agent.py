"""RarStewardAgent — the autonomous steward of the public RAR.

A registry rots when it fills with noise: undocumented stubs, placeholders, and
"same but different" agents that do one thing five slightly-different ways. Left
alone it becomes unsearchable and low-trust. This agent trolls the RAR catalog
and reports — operator-mediated, it SUGGESTS, never auto-deletes — on:

  • health     overall quality (card coverage, placeholders, dup pressure) + a score
  • duplicates clusters of same-but-different agents that should be UNITED into one
               quality base.py (with a recommended unified name + the members + why)
  • junk       noise / low-quality candidates to review for removal (no card,
               stubs, version 0.0.0, placeholder/test names, exact dup ids)
  • agent name=…  a deep quality assessment of one agent (fetches its full card)
  • help

It reads the consolidated catalog (api/v1/index.json) in one request; deep
assessment fetches the per-agent card. Online by nature; degrades cleanly.
Steward, not executioner: it produces guidance for the operator to act on.

Generic + cover-safe. MIT © Kody Wildfeuer.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
from datetime import datetime, timezone

try:
    from agents.basic_agent import BasicAgent  # type: ignore
except ImportError:
    try:
        from basic_agent import BasicAgent  # type: ignore
    except ImportError:
        class BasicAgent:
            def __init__(self, name="Agent", metadata=None):
                self.name = name
                self.metadata = metadata or {}

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/rar_steward",
    "version": "1.0.1",
    "display_name": "RarStewardAgent",
    "description": ("Surveys the public RAR catalog over HTTP for health, duplicate clusters, and junk candidates, returning operator-mediated cleanup guidance."),
    "author": "Kody Wildfeuer",
    "tags": ["rar", "steward", "registry", "quality", "dedup", "merge", "curation"],
    "category": "core",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

RAR = os.environ.get("RAR_REPO", "kody-w/RAR")
_RAW = "https://raw.githubusercontent.com"
INDEX_URL = f"{_RAW}/{RAR}/main/api/v1/index.json"
AGENT_URL = f"{_RAW}/{RAR}/main/api/v1/agent/{{id}}.json"

# Where steward findings become traceable GitHub Issues (public canon only).
STEWARD_TRACKER = os.environ.get("STEWARD_TRACKER", "kody-w/RAR")
STEWARD_LABEL = os.environ.get("STEWARD_LABEL", "rar-steward")

# name tokens that carry no distinguishing meaning
_STOP = {"agent", "the", "a", "an", "of", "for", "to", "and", "or", "rapp",
         "generator", "helper", "tool", "assistant", "v1", "v2", "py"}
_PLACEHOLDER = re.compile(r"\b(test|tmp|temp|demo|foo|bar|baz|example|placeholder|untitled|copy|wip|draft|sample|hello[_-]?world)\b", re.IGNORECASE)
_DUP_THRESHOLD = 0.6   # name-token Jaccard at/above this = merge candidate


def _run(cmd, cwd=None):
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=120)
        return r.returncode, r.stdout.strip(), r.stderr.strip()
    except FileNotFoundError:
        return 127, "", f"{cmd[0]}: not found"
    except subprocess.TimeoutExpired:
        return 124, "", "timed out"


def _scrub(text):
    """Redact tokens/secrets before they enter a return envelope or issue."""
    if not text:
        return text
    text = re.sub(r"gh[pousr]_[A-Za-z0-9]{20,}", "[redacted-token]", text)
    text = re.sub(r"github_pat_[A-Za-z0-9_]{20,}", "[redacted-token]", text)
    text = re.sub(r"(?i)(authorization|token|bearer|secret|password)\s*[:=]\s*\S+",
                  r"\1=[redacted]", text)
    return text


def _now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _fetch(url, timeout=15):
    import urllib.request
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return r.read().decode("utf-8", "replace")
    except Exception:
        return None


def _tokens(text):
    return {t for t in re.split(r"[^a-z0-9]+", (text or "").lower()) if t and t not in _STOP and len(t) > 1}


def _jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


class _UF:
    def __init__(self, n): self.p = list(range(n))
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]; x = self.p[x]
        return x
    def union(self, a, b): self.p[self.find(a)] = self.find(b)


class RarStewardAgent(BasicAgent):
    def __init__(self):
        self.name = "RarStewardAgent"
        self.metadata = {
            "name": self.name,
            "description": ("Steward the public RAR: catalog health, "
                            "merge-candidate clusters of same-but-different "
                            "agents, and noise/junk to review. Guidance only — "
                            "never auto-deletes (operator-mediated)."),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string",
                               "enum": ["health", "duplicates", "junk", "agent",
                                        "file_issues", "help"]},
                    "name": {"type": "string", "description": "agent: rar_name or id to deep-assess"},
                    "publisher": {"type": "string", "description": "filter to one publisher (e.g. @kody-w)"},
                    "limit": {"type": "integer", "description": "max clusters/items to return (default 25)"},
                    "scope": {"type": "string", "enum": ["merge", "junk", "all"],
                              "description": "file_issues: which findings to file (default all)"},
                    "confirm": {"type": "boolean",
                                "description": "file_issues: actually create issues (default false = dry-run plan)"},
                    "tracker": {"type": "string",
                                "description": "file_issues: owner/repo to file into (default STEWARD_TRACKER)"},
                },
                "required": ["action"],
            },
        }
        super().__init__(self.name, self.metadata)

    def system_context(self):
        return ("RarStewardAgent can audit the public RAR for quality — "
                "duplicate/same-but-different agents to merge, and noise to "
                "prune. Use it when asked to keep the registry clean/usable. "
                "It only suggests; the operator acts.")

    def _env(self, action, status, **f):
        return json.dumps({"schema": "rapp-rar-steward/1.0", "action": action,
                           "status": status, **f}, indent=2, ensure_ascii=False)

    def _catalog(self, publisher=None):
        text = _fetch(INDEX_URL)
        if not text:
            return None
        try:
            d = json.loads(text)
        except ValueError:
            return None
        agents = d.get("agents", [])
        if publisher:
            agents = [a for a in agents if a.get("publisher") == publisher or a.get("publisher") == "@" + publisher.lstrip("@")]
        return agents

    def _clusters(self, agents):
        """Union-find clusters of same-but-different agents by name-token
        similarity (boosted when same category)."""
        toks = [_tokens(a.get("name", "") + " " + a.get("id", "").split("__")[-1]) for a in agents]
        uf = _UF(len(agents))
        pairs = []
        for i in range(len(agents)):
            for j in range(i + 1, len(agents)):
                if not toks[i] or not toks[j]:
                    continue
                sim = _jaccard(toks[i], toks[j])
                same_cat = agents[i].get("category") and agents[i].get("category") == agents[j].get("category")
                thresh = _DUP_THRESHOLD - (0.1 if same_cat else 0)
                if sim >= thresh:
                    uf.union(i, j); pairs.append((i, j, round(sim, 2)))
        groups = {}
        for idx in range(len(agents)):
            groups.setdefault(uf.find(idx), []).append(idx)
        clusters = []
        for members in groups.values():
            if len(members) < 2:
                continue
            ag = [agents[i] for i in members]
            common = set.intersection(*[toks[i] for i in members]) if all(toks[i] for i in members) else set()
            base = "_".join(sorted(common)) or "_".join(sorted(_tokens(ag[0].get("name", "")))[:2]) or "unified"
            clusters.append({
                "recommended_base": f"{base}_agent.py",
                "size": len(ag),
                "publishers": sorted({a.get("publisher") for a in ag}),
                "category": ag[0].get("category"),
                "members": [{"rar_name": a.get("rar_name"), "name": a.get("name"),
                             "publisher": a.get("publisher")} for a in ag],
                "why": ("these share the core name tokens " +
                        (", ".join(sorted(common)) if common else "(near-overlap)") +
                        " — same job, slightly different; unite into one quality base "
                        "covering the union of their inputs/outputs."),
            })
        clusters.sort(key=lambda c: -c["size"])
        return clusters

    def _junk(self, agents):
        out = []
        seen = {}
        for a in agents:
            reasons = []
            name = a.get("name", "")
            rid = a.get("id", "")
            if not a.get("has_card"):
                reasons.append("no card (undocumented — no summary/tags)")
            ver = str(a.get("version", ""))
            if ver in ("", "0.0.0") or ver.endswith("-stub") or ver.startswith("0.0"):
                reasons.append(f"pre-release/stub version ({ver or 'none'})")
            if _PLACEHOLDER.search(name) or _PLACEHOLDER.search(rid):
                reasons.append("placeholder/test name")
            key = (a.get("rar_name") or rid).lower()
            if key in seen:
                reasons.append(f"exact duplicate rar_name of {seen[key]}")
            else:
                seen[key] = a.get("rar_name") or rid
            if reasons:
                out.append({"rar_name": a.get("rar_name"), "name": name,
                            "publisher": a.get("publisher"), "reasons": reasons})
        return out

    # ── shared issue-filing contract (rapp-drift-issue/1.0) ──────────────────
    #   items: list of {title, fingerprint, body_md, machine}
    #   tracker: "owner/repo"  label: e.g. "rar-steward"  prefix: e.g. "drift"
    #   confirm: bool (default FALSE upstream — filing public issues is opt-in)
    # Idempotent: a stable fingerprint per finding means same drift => same fp =>
    # no duplicate issue. Cover-safe: only public canon ever lands in title/body.
    def _file_issues(self, items, tracker, label, prefix, confirm):
        """Idempotent Issue filer (same contract as the drift agent). Dedupe by
        ONE exhaustive label-scoped listing (search of a hex in a code fence is
        unreliable); the fp also rides the TITLE. Fail-safe: if we can't list,
        refuse to file. COVER: callers put only public canon in title/body."""
        filed, skipped_existing, planned = [], [], []
        rc, out, err = _run(["gh", "issue", "list", "--repo", tracker,
                             "--label", label, "--state", "all", "--limit", "500",
                             "--json", "number,title,body"])
        if rc != 0:
            return {"tracker": tracker, "label": label, "confirm": confirm,
                    "error": ("could not list existing issues to dedupe (" +
                              _scrub((err or "").strip())[:160] +
                              ") — refusing to file to avoid duplicates."),
                    "filed": [], "skipped_existing": [], "planned": []}
        existing = {}
        try:
            for it in json.loads(out or "[]"):
                blob = (it.get("title", "") or "") + "\n" + (it.get("body", "") or "")
                for fpm in re.findall(r"(?:fp:|\"fingerprint\"\s*:\s*\")([0-9a-f]{12})", blob):
                    existing.setdefault(fpm, it.get("number"))
        except ValueError:
            pass
        labelled = False
        for item in items:
            fp = item["fingerprint"]
            title = f"[{prefix}] {item['title']} (fp:{fp})"
            machine = {"schema": "rapp-drift-issue/1.0", "fingerprint": fp,
                       "prefix": prefix, **(item.get("machine") or {})}
            body = (item["body_md"] + "\n\n```json\n" +
                    json.dumps(machine, ensure_ascii=False) + "\n```\n")
            if fp in existing:
                skipped_existing.append({"fingerprint": fp, "title": title,
                                         "number": existing[fp]})
                continue
            if not confirm:
                planned.append({"title": title, "fingerprint": fp, "would_file": True})
                continue
            if not labelled:
                _run(["gh", "label", "create", label, "--repo", tracker, "--force"])
                labelled = True
            crc, cout, cerr = _run(["gh", "issue", "create", "--repo", tracker,
                                    "--title", title, "--body", body, "--label", label])
            if crc == 0 and cout:
                filed.append(cout.strip().splitlines()[-1])
            else:
                planned.append({"title": title, "fingerprint": fp,
                                "would_file": True, "error": _scrub(cerr) or "create failed"})
            existing[fp] = "just-filed"
        return {"tracker": tracker, "label": label, "confirm": confirm,
                "filed": filed, "skipped_existing": skipped_existing, "planned": planned}

    def _fp(self, *parts):
        key = "|".join(str(p) for p in parts)
        return hashlib.sha1(key.encode("utf-8")).hexdigest()[:12]

    def perform(self, **kwargs):
        action = (kwargs.get("action") or "health").lower()
        if action == "help" or action not in ("health", "duplicates", "junk",
                                               "agent", "file_issues"):
            return (
                "RarStewardAgent — keep the public RAR clean + usable.\n"
                "  action=health           catalog health + quality score\n"
                "  action=duplicates       same-but-different clusters to UNITE into one base\n"
                "  action=junk             noise/low-quality candidates to review (no auto-delete)\n"
                "  action=agent name=…     deep quality assessment of one agent\n"
                "  action=file_issues      turn merge-cluster + junk findings into GitHub Issues\n"
                "                          scope=merge|junk|all (default all); confirm=true to file\n"
                "                          (default dry-run — plans only; tracker=owner/repo override)\n"
                "  publisher=@kody-w       (optional) scope any action to one publisher\n"
                "Steward, not executioner: it suggests; the operator acts.")

        limit = kwargs.get("limit") or 25

        if action == "agent":
            nm = (kwargs.get("name") or "").strip()
            if not nm:
                return self._env(action, "error", error="pass name=<rar_name or id>")
            agents = self._catalog() or []
            hit = next((a for a in agents if nm in (a.get("rar_name", "") + " " + a.get("id", ""))), None)
            if not hit:
                return self._env(action, "not_found", name=nm)
            card = None
            cj = _fetch(AGENT_URL.format(id=hit["id"]))
            if cj:
                try: card = json.loads(cj)
                except ValueError: pass
            score, notes = 100, []
            if not hit.get("has_card"): score -= 40; notes.append("no card")
            summ = (card or {}).get("summary") or (card or {}).get("description") or ""
            if len(summ) < 40: score -= 20; notes.append("thin/absent summary")
            if not ((card or {}).get("tags")): score -= 15; notes.append("no tags")
            if _PLACEHOLDER.search(hit.get("name", "")): score -= 25; notes.append("placeholder name")
            return self._env(action, "success", rar_name=hit.get("rar_name"),
                             quality_score=max(0, score), notes=notes or ["looks healthy"],
                             summary=summ[:200], category=hit.get("category"))

        agents = self._catalog(kwargs.get("publisher"))
        if agents is None:
            return self._env(action, "offline",
                             note="could not reach the RAR catalog (api/v1/index.json). Try again online.")
        if not agents:
            return self._env(action, "empty", note="no agents matched.")

        if action == "file_issues":
            scope = (kwargs.get("scope") or "all").lower()
            if scope not in ("merge", "junk", "all"):
                scope = "all"
            confirm = bool(kwargs.get("confirm", False))   # dry-run default
            tracker = (kwargs.get("tracker") or STEWARD_TRACKER).strip()
            items = []

            if scope in ("merge", "all"):
                for c in self._clusters(agents):
                    members = [m["rar_name"] for m in c["members"]]
                    fp = self._fp("merge", *sorted(members))
                    body = (
                        f"**Merge candidate** — {c['size']} same-but-different agents.\n\n"
                        f"Recommended unified base: `{c['recommended_base']}`\n\n"
                        "Members:\n" +
                        "".join(f"- `{m}`\n" for m in sorted(members)) +
                        f"\nWhy: {c['why']}\n\n"
                        "Unite into one quality base (operator-mediated). Steward "
                        "suggests; the operator authors the base and retires the variants.")
                    items.append({
                        "title": f"merge {c['size']} same-but-different → {c['recommended_base']}",
                        "fingerprint": fp,
                        "body_md": body,
                        "machine": {"kind": "merge",
                                    "recommended_base": c["recommended_base"],
                                    "members": members},
                    })

            if scope in ("junk", "all"):
                _CONFIRMABLE = ("no card", "placeholder", "duplicate")
                for j in self._junk(agents):
                    reasons = j["reasons"]
                    joined = " ".join(reasons).lower()
                    if not any(k in joined for k in _CONFIRMABLE):
                        continue
                    fp = self._fp("junk", j["rar_name"], *reasons)
                    body = (
                        f"**Review candidate** — `{j['rar_name']}`\n\n"
                        "Reasons flagged:\n" +
                        "".join(f"- {r}\n" for r in reasons) +
                        "\nReview and either add a card or retire the noise "
                        "(operator-mediated). The steward never deletes.")
                    items.append({
                        "title": f"review: {j['rar_name']} ({', '.join(reasons)})",
                        "fingerprint": fp,
                        "body_md": body,
                        "machine": {"kind": "junk", "rar_name": j["rar_name"],
                                    "reasons": reasons},
                    })

            result = self._file_issues(items, tracker, STEWARD_LABEL,
                                       "rar-steward", confirm)
            return self._env(action, "success", scope=scope, scanned=len(agents),
                             candidates=len(items), result=result,
                             ruling=("Operator-mediated traceability: each finding becomes "
                                     "one idempotent GitHub Issue (same finding => same "
                                     "fingerprint => no dup). Dry-run by default — set "
                                     "confirm=true to actually file. Only public canon "
                                     "lands in issue titles/bodies."))

        if action == "duplicates":
            clusters = self._clusters(agents)
            dup_agents = sum(c["size"] for c in clusters)
            return self._env(action, "success",
                             scanned=len(agents), clusters=len(clusters),
                             agents_in_clusters=dup_agents,
                             merge_candidates=clusters[:limit],
                             ruling=("Operator-mediated: for each cluster, author ONE quality "
                                     "base agent covering the union of behaviors, publish it, "
                                     "and retire the redundant variants (keep lineage). Never "
                                     "auto-merge — these are suggestions for review."))

        if action == "junk":
            junk = self._junk(agents)
            by_reason = {}
            for j in junk:
                for r in j["reasons"]:
                    by_reason[r.split(" (")[0]] = by_reason.get(r.split(" (")[0], 0) + 1
            return self._env(action, "success", scanned=len(agents),
                             flagged=len(junk), by_reason=by_reason,
                             candidates=junk[:limit],
                             ruling=("Review candidates; remove true noise (placeholders, "
                                     "stubs, exact dups) and add cards to the undocumented. "
                                     "Operator decides — the steward never deletes."))

        # health (default)
        clusters = self._clusters(agents)
        junk = self._junk(agents)
        n = len(agents)
        carded = sum(1 for a in agents if a.get("has_card"))
        placeholders = sum(1 for a in agents if _PLACEHOLDER.search(a.get("name", "")))
        in_clusters = sum(c["size"] for c in clusters)
        publishers = {}
        for a in agents:
            publishers[a.get("publisher", "?")] = publishers.get(a.get("publisher", "?"), 0) + 1
        # 0-100 health: card coverage, low placeholder rate, low dup pressure
        card_cov = carded / n
        dup_pressure = in_clusters / n
        ph_rate = placeholders / n
        score = round(100 * (0.45 * card_cov + 0.35 * (1 - dup_pressure) + 0.20 * (1 - ph_rate)))
        grade = ("A" if score >= 85 else "B" if score >= 70 else "C" if score >= 55 else "D")
        return self._env(action, "success", surveyed_at=_now(),
                         total_agents=n,
                         by_publisher=dict(sorted(publishers.items(), key=lambda kv: -kv[1])),
                         card_coverage=f"{round(card_cov*100)}%",
                         merge_clusters=len(clusters),
                         agents_in_merge_clusters=in_clusters,
                         junk_candidates=len(junk),
                         placeholder_agents=placeholders,
                         health_score=score, grade=grade,
                         top_merge_clusters=[{"base": c["recommended_base"], "size": c["size"],
                                              "members": [m["rar_name"] for m in c["members"]]}
                                             for c in clusters[:8]],
                         guidance=("Raise the score by: (1) uniting the merge clusters into "
                                   "single quality bases, (2) adding cards to the undocumented, "
                                   "(3) pruning placeholders/stubs. action=duplicates and "
                                   "action=junk give the worklists. Steward suggests; you act."))


if __name__ == "__main__":
    print(RarStewardAgent().perform(action="help"))
