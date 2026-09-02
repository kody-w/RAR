---
name: "rar-rapp-rar-steward"
description: "Steward the public RAR: catalog health, merge-candidate clusters of same-but-different agents, and noise/junk to review. Guidance only \u2014 never auto-deletes (operator-mediated)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/rar_steward", "rar_sha256": "e8cb15fe4f51fefb7c9f05fe3722dc7eccd67ab22beca8398591479d8fcc9e3e", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "rar_steward_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapp/rar-steward:40ca915bea4fffbc44d567be9489b8b46cc3c67750800e78911f7c570f6b80f3", "kind": "skill"}, "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["rar", "steward", "registry", "quality", "dedup", "merge", "curation"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapp/rar_steward`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `rar_steward_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
