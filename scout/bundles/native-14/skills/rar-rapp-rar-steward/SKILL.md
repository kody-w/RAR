---
name: "rar-rapp-rar-steward"
description: "Steward the public RAR: catalog health, merge-candidate clusters of same-but-different agents, and noise/junk to review. Guidance only \u2014 never auto-deletes (operator-mediated)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/rar_steward", "rar_sha256": "e8cb15fe4f51fefb7c9f05fe3722dc7eccd67ab22beca8398591479d8fcc9e3e", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["rar", "steward", "registry", "quality", "dedup", "merge", "curation"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapp/rar_steward`. The original RAPP
agent is preserved byte-for-byte in `rar_steward_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

RarStewardAgent — the autonomous steward of the public RAR.

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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "enum": [
        "health",
        "duplicates",
        "junk",
        "agent",
        "file_issues",
        "help"
      ],
      "type": "string"
    },
    "confirm": {
      "description": "file_issues: actually create issues (default false = dry-run plan)",
      "type": "boolean"
    },
    "limit": {
      "description": "max clusters/items to return (default 25)",
      "type": "integer"
    },
    "name": {
      "description": "agent: rar_name or id to deep-assess",
      "type": "string"
    },
    "publisher": {
      "description": "filter to one publisher (e.g. @kody-w)",
      "type": "string"
    },
    "scope": {
      "description": "file_issues: which findings to file (default all)",
      "enum": [
        "merge",
        "junk",
        "all"
      ],
      "type": "string"
    },
    "tracker": {
      "description": "file_issues: owner/repo to file into (default STEWARD_TRACKER)",
      "type": "string"
    }
  },
  "required": [
    "action"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rar_steward_agent.py` and embedded as the fenced Python below (sha256 e8cb15fe4f51fefb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rar_steward_agent.py` first:

```bash
python3 rar_steward_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rar_steward_agent.py   # or on stdin
python3 rar_steward_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
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
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
