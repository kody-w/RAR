---
name: "rar-rapp-rar-steward"
description: "Steward the public RAR: catalog health, merge-candidate clusters of same-but-different agents, and noise/junk to review. Guidance only \u2014 never auto-deletes (operator-mediated)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/rar_steward", "rar_sha256": "e02083e45e0704bddd5a681e08490a92c9ef06c44277d09000aba99f65cacd57", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["rar", "steward", "registry", "quality", "dedup", "merge", "curation"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rar_steward_agent.py` and embedded as the fenced Python below (sha256 e02083e45e0704bd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rar_steward_agent.py` first:

```bash
python3 rar_steward_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rar_steward_agent.py   # or on stdin
python3 rar_steward_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@rapp/rar_steward_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/rar_steward_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@rapp/rar_steward/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
