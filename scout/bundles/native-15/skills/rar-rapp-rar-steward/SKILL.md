---
name: "rar-rapp-rar-steward"
description: "Steward the public RAR: catalog health, merge-candidate clusters of same-but-different agents, and noise/junk to review. Guidance only \u2014 never auto-deletes (operator-mediated)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/rar_steward", "rar_sha256": "e02083e45e0704bddd5a681e08490a92c9ef06c44277d09000aba99f65cacd57", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["rar", "steward", "registry", "quality", "dedup", "merge", "curation"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/829ebebyJIv+lW03OutYx9sgxBI4L7udwEhIYlBIAahqlouZhCjGASour77SyTtyd4equ/94+1zVu0tyIyMjOEXEZmhqr/eWE0d5uWbT282uduPjChxfa/xyjfv37he5ZRRUUd5Bl7vaq+1SndUh96oaOwkckYKpXwaOVZtJXkwCj0rqcP3o9QrA++DY2Vu5Fq1N3KSpqq9shrl/qiyUu+D3dQf3Mj3vdLL6pEVgH9W70dg/CjLo8qDj00Wj+p8VHrnyGs/jpYNIJQ53ijPkn70e4MiY2yUeWevHAHe8w+ul3i1V43e5oVXWnVefkg9NwJLu+8+gl14nZUWiVe9+fTbH+/fRODvN5/+euMkVgUevVGs8r4xamAEjE+sLAAvih6IJQOfAVE/L1PwyPX80f3T28pL/Pejf/87BlOD6t2n37PR/cdyBoGNPo/e3t59DLz67e9vbo9/f/NulJej39/cpAU+fkzy1ivfvnsiEPmPND5fRybF72+GWfenWV6Pomz09onIezDMbQqgErDr6vZ5kCL464nsL/4ATgdB3Ij4UeJ9iaqqGag+3+TwU3p1Uw58ZN/S+EqsD1qLPa/4yoCAfXhWNoJGTWXZiffx99+BkF4j+SDZz7ddP3v30gIBqVNjJVHdjyonL72fE3wS3f3dK2b6aMXAMDVxpbJABeDPPPNGtlX9wiJXq37+czN2oP0PD+w++kz1ZP6jt1n+3Mzf/Xylq/5GGdjD50Hs6PQ6wB1E/7ASsH2vqtJhHPDKYRM3pf+U9jODuL27msDd5W8iAvK/7tWPwG6yoLoJahnVXGOPVjdb+v463/sBqiy8z9eF/nsg/99WkozeAo+0mgSASJK8+8+Rk2d+VKaf67LxBgkOzP4Plnqk6pb9h7LJHoy3AMhQXUHoP0d1aTmxV37O28wr4dIrgCkAQCoj94caupp9FYKJ/zsGaPuhfVgyv6Kslby7bRSgYf/g7ncre5z6XfJ3h3t/BQiv85xmmO+Vn0ZRPaqaIPCquvrPq/s9IOWwRvURuDag+UgxiVIw4fPoBXxdH97RC8WfD/8Kru7o8RVWZOk3gDgY6CMcDkBY1SDYPAfCO/VhO1n66dst3wFogOKPX7zs/PbGxwBcQBV5OWDY9Y/Pv78pgMnffOJ/lVb5ZfhrWDly/+u6++dkbxEJ8HsjfEeXt1dOf/vj5djwKqnM6+q3b62RP0h0wOY7iYH59IrV1n3TD2vf4HXYPjQYBvg/NHoYE7mPb9+9ez8SgQ5fFwpY/J9JBUz64udNdl3gKows/Yq0M4T4z9dFv3pxBI+/+F7thG+pJSuqXzSF/zjEQqt+G7mfATO/3Xj/49237DrHVzity/7Tw4LHKs9AKLTc6q1zfPftWK9zvKIe6VbSeOyg00+jQaUvB17x/mr/3qC/MYK8/0ZjT7K7izu0qi8DE0OAu1EYffg8wpD/vNH5aBWFl7mDweaj+7ivVm3Sq3VfdwIs4K+/391JD2+ssr9b+SsDnmVYz1zhG4YTL3s70Ho3+l+AsWdcot9yWYdRBlt2NWD70/qvyuDtKxzVVjCE+ueiGOOvieI+8BvCX7Y8xbCcxM9Z5WPlWSWwlydhv7D954ug3y4C8NbxwjxxQUy5g8WrCchrll41jgMi3LDUg8t9fuLiyQvf/SxBukfML1dGP6dW9xbY1PXDu7uhfb6Z2wAOACbzPK7uiQiQ+x8/I3/X0Ofh92+fUAT54/2QznhBDh4+MfzwaBDac+z9DlS9wNmnwPHm3VdZ5h2lqqu7f/pl4ea+n0SZ9/PscpAMwF4nbxL3anGlZznhNQJdM7973vbWKiL4PIZBwuB1HwckePdxpJYgAgYWAE8QccFqH1+o/27Btx38OudeWtT9FfxunA251U0IAMWc0HO/joVfBbcX+fCnb8AHBO6vo9z16aNvgzzl1ZT/vtSNxFN+f013XqTzjzRegdMHBu5DvoLvW24EXtt5nrzk8f5uIL+wksp79w5M+I/H9OeeDr2kd0+Avtnv/fl9xzuVNShl/kVVKGbDKt+L8bWXDkY8QPV3ZPKNPL4rhSEGO8P4u0vc8/a3Nz2/NmP4Sb3UHrJ7wET623OA+ONK8BrEnd8GDq7jwPM/XifkF4/e6BfPWf53lZegJH17p/Du3evz7aEI//xaUfW4wu9v/v1vYSD7VDD8+98PSepfzm//qqKL968//v5+tX0tsl5PI5+tonhOnoIawfXcUZNFfgR+D7XOp9Gfwyrl0+svw2Ow4p8/p/v7G+EmgE/XgSPoR0N/f/PxmEfZW8DMB7BoelvgzZNKvpbpj8gBImC2EYKcY2C/DXvA8a8wrGXAQJ/KvYcaatjzq2cOo4eTkh+T/V5Gfj2Oqa4Pr0sMByMA0qLSuz08W2VkZQ9p+2u0r/70EEf/+hEPdVSDEunNp0E4V0v9mf0AKxuT6Og7+v9hRBjQMwu8siija4EAXOWHowdP+JK6w8jhzx+OTUFYuUYkoNvf38RRdp325H2/dgoC/P6rPQ1UBrf/9vkfv0zzETI+PaDM39+Z+/e7n+DfLwSBL4wkLlaKQNE8e8WRp7R1mPcsp/rq2OhVaxoc7fgEpsP6PwFSEOFB/B6A9HiV2/UTENfrowfv9txrzBo9OPt9znei5NcJQNa/jQcG75QGhq+fn8vhe7ze42IdZY33a2j+oIDjyxgB0P2B6/8jVFduRz6vwPqffx2Bx91X/FWkVe668BMLQI37jxH3r/LvJ7wtB6k+7PInRH7P7jsZsMuLAGoBXHNdUBs/FBw3QLvi2fUc7CdY+SrMqmBydYfa23Hw/ST4/zYy3k7iALS81MHo7V//ej/610urBT78/zcQfEKNJ5P99I0J/zpE3l3604M1/DqcgRA2nKs9utRTNv32qpn3D2nl+8fMkadolv/1U+zrnj7crWLY9D23/R9Vjrczx+s/hw9WBhDm81CL3yHwZ2w9nedeZ123CKrGmxQ+3379jEbZgOIn+AywR/raBa7C8iw7GtKRT6NraXU/dB3ZQ8ACCcOP3OorwQ25TeSCCgmURiDSPz+wHb0dUoFH4p//65oa/BPiz6x+mA5iEgg8wIfn9xrD7h/KjAfEq7z6nyzw9dkvUCjI05L+egj8cSQNV0f3SwegFlDP/QPaCdDjcIw9utrq6AoNFQz8MbphzY8qxufXMl+Foccrhc/fqVVeDgeUvjzV+036dkhMhlTtoUi5Vj0PNP4nBv+zs4pXPOBxvevTx8V/Ruo2/UuUPe7589P2fjb5mtR9eeZcDzR++3Q9pf7j/8CnPl0leXWlO9X394x8JInsY+7/D4znlsNfr2Sc4YpgcKAh7IGKCthI7gNXDa1zBFL+9w9n/CBMvf8nSzxVCFfKpec2mQtKhMdSAdTow+3PcIwCOAFuJ17D5T9ZYriBulUId/8EKw0bA2veC5nommpcY/v13vYnjnGLSl+5xPXi6PMr2ebLYXb/5RZ7wNi//n757jFlHaZ/53zgmsu8zE+/kyI+rvRb+bECnjwccQxJ9bvfkD/+GA5THt5fjz++HfN+hAxH/OP/Wfj5xxHnnuldpwz7Bw76yOHnx7/+QdwaiPxzt/o6jwU1bumlwPpHV3i+ZXxvn9Ui1T+y96pubDDD64DYBlgE+ejgAkOGOeSX19vTm4u5udMMt5ye+/GfLPAACyAmOSAkVs9s/vsZ5wtj/4+Hy+iHy8RnFvwPcP8X/GHwgWcW8mwZwOW1thpixfi1uynr2xuQZ/Ofq+dHVF478LdePe5/fn77hPz/MJo9HmdXXzn/V6x95dBP036zvj0YHzj8fwGLg0s/jbyO+8Hob537P0bIhzGC3JV/v9y6wj5g6v0IVLTPxToCRnZ/Cqx4VICMsGpK76UKv4DpgKu7NuHRMyMbQubDJDDkuUxfjCvCL8NKw96e6/TFmNtFzOdROVwPvh328O/RW+QjhoPfj2xAI+TjZHgCLOHDi+XfXd+hyMO7+5IvdB6UluvdziQogJC3sw2w6H99HhH4yEuuVSD91ZsZ8vCG+eoN/jhn/qLe+0Vwbcqz13vuF6v+/CXL27c/xNY6r63knp58/iF+ApB9uuR3I6d+ez+jfGZW10IALDiKvf5zYqW2a43i86fRh/j82/iPdz/k5EEXV4v6DIrTv24ae3j+b6C6d3//Pz/O5u4Z1D9O3Z7Stq8oPDO9H80fEOzLV1XRLUz9YNIzm33QwIvI8YOpNze8393dL4evVvj5+s8fa7z4epO//XXL5n50KDh6ALHbkDug/eMurBenhr98I/H3P1zmG5j97RPxxw+ZDe6teNcgbw1R/BoSry5pgxr07fjdkNjWD0nuLWN8RKXrGfovxuFBeFmQvDxvB1H/LfpuiPTDCt8N9u9/fZG3k3cAeAHPgN5zs4KvScbHV1rEhlTjl8k/b/4KovNNXm1exgAL6urpquDpMqDPm2HRa0bx5v2bqgeiS78Mx5ReV9+bEF8+vPYiPj/jfGzM+6YND/geKGfcqP66CW8whcfi5pbsvN5k9CgI+Lu3S4NGrop/1tQ5+o7iQVwFwgcFugbGALba0AMcVvFwupE/tQuWXgDkVfa3ZkH43ir4HYqr+tYp+pOWpzd/v38TZYBqc9XR0Az6H/8xEiKnzKvcr0c7J29qkNRmdQTcDoRKNYyul+U3hgACVxHg4j6uKPOjdytvQE335/8uraKAB6e954t/3s4r8zIKosxKgNC329+zW10IaA5x1AMRyQVuVHsfgDo+DH8MzvnnMyo3APxY9H9eRQveXu/SmRXQbFE1Q/tkNtxxASHe2BoUfmsF80Ce4YCFh/OQ6noIlSdXewSrV3GUJCMXFJAOkFB/u3Jqsk8DsT///BN4Xvh7dmuInYxuHSsVDAY8sjP68AHswE+iIKx/zzwnzEf/+uvvf43+e/SjWVfiwxrboTnrJlbA4XoniaCwDK7OPIAG2LzlXsX61993OQIyGUighnraj+4XY6D6AHbzINQdR31A8Skor/0BnaK0AHF48PKo/jha+aNHfkdD914JFrJGYV6BgsIbToe9zOkBVQts51GSw4VDZdVR5ffvR80d/P60S+vKIvBHMPzPkcBsge3mybWHs7lp6HrkBNwmeVT57TkgUv6rGtEPJB4q88IC9hOW1n0N37rpZbDe+/ThiAvUIO3v2dDR7A2isgbru4kHDAKSce4q/TDofDQEq4eDrPphzPUcUc2tAZ9/z6q7BQ9V/RDdACv9I+b/592kqvDazjHID3B6vZG8acG9a+Vqg99pAB6GD2cJWZ7mTfVYTAHdvgSkKw3qye/LHCjoCg4AJMB2EvApAuXVFVw+vQD/0b08fFlegp0PVxnXc0sAWqNH0AJZ5QNsAfWN3Nsl79BFFYCFgIdUVytJ+mc411o9wG7e84F1WMn14LR+PHJtslsRNEDU1ZOGFl+AMlU96AZ4202FdZkPu/iqFwbQux7m3CzyLrRvLj/eD+vttOWS3am796/1wj/MvPnw6PoZRUfPWqevKSTw+gfUf/tVrfJSfM/rkyHXt+691U+kn0XIX+r4v4n7bky2d2uqnj9es38D7M/TgAFx3l71b43KV7oUrt2d0D0DuTV2QMB6+nfP+H3Wj32LUPDop73Yt9OtND8DlHp7v1f9Nl262981QABnQj6C/72QJwyo3hq0n59ijCK3es7gK23c1i91cY/eXrs0AecRELPfACUPjL57YQdJMRjG6tqS5d7MEKQTICZcN+3+qDdrdO3JGhDi1ICN/OeVKWC4T9w8rH/1aa/8cD/+BExcT+KjoWm+B1sDaYo3TL9m49UtuCc98P0ftjKDUOs2oI57RKarXl7E+NsFAODyiiPLOxpCN/P+UFk+SB6ElQrEgSAWOXr5zZfhSyPAlD3gx28+ZUB876/nGK9+WWQA6tQbjH34UgngDHBQR9710y33G/7ysiZ98+m3+/c1hm/WPDoL+DBYIvhl3Uk+uxUDnwZNgQLiTd0XAwdD/1QWDKnL/cJjIP/yezrP5n96ugZxgJ6HfOLWuv/Y4u4P/V6gJn/o9Rp63Ie0877c0CsGdDKsdz0D/Ha11Ooe/R2+NXJd/eWWgT4sg+LPiAIX9wKvHIje5Po1zaskPo1e9mkPZAdD+3CzszeviOSxxH5VKMNXE77upR+99T4GH0f3Zvx3rxG9Xv/9RMptGD3dvVUPXz14+fWE4ZtIdzO4JsfPFJ8kr2r4fhf6k7WffQPhYd0rhj4u/nUP3rebBGsNvgxyBXdg7263Tyzl9pDaXiWcWPXty1B/gV3UFsAK62749+wXDL/ewA6pAjz+iIDVBj3ejPvTm2/y4vv7KrRAsgYGeAiKEBMPwz1khmC267q4NSXGHkJgJHBV1CE9H5k6GIbOZi5CIsB/bYsk/SnuWI6Lz4aSKW9KB9TtICwMFvvGdhB/PCXHhO95pI2ikylCeIg/Iacz35p6E9RzCUDHfpo63J3fN3JjfBDRY4p+9e3bfv56Y08xMJLDqhV1+2FgSCPRiW3vOP4Mr3IJPwbLA72Ja0ly9/scr7rCJo/HstojsbdzD2mzpOS1xNLU2twzSreR7Eq7YMFhRgTzS5yd8cU23ZFrfa9NED6S88he94546rrVOt805QmqvbEbnFGBhGH5THQEvt1O8Dj1SI9AOrcvDlDfHKCWzgjXkdVLvuHQA71YGd6kb8Mms/Fkams+LbTbqVdyrm0JclikO4TawrWPByXqVhNDW/eXdCeX88zfWd4kWhwUll9V7tGvD4laHpeQ0622htON23QmcQaqzsPMcuyjSx2DYzpBbY/HVnpnCntBImc51WUGwycVPss9Hj5W8EUivYqGCWRVN0jPzTBv4x52gtH3PR/CCLS1ewFJL9jYY0oMnu4kZIkeFjNW6w7LpcHsJucVe5iufBEhmHHRZAuIzH0qp8pIPE/sZryYTNHL0kM5WFPXGD6L1qxKzy9Fj5Bok6oTW7LiHUaPzXJ7zk89N4UmjMhcQoJtGZydusspflbaUOsPFrGXtqoutcKWphaTSOikC0HOsLMCu8QxyemTEBh5jcwi1UuXnEUeeJSHkdIFMfIApWWEFGmC7+R1sexnbSPvHHky3Qt7vzgsLwukUxusm/bblZ4cVJMgo8b2rdW5XWrdnKwmhdBQ9AWHGj6MfXkzFmSaEs77uSRAIKSJFXqxUB4Ll4wJzcX9qnVWMVA2ehQkbXk5qzvmQKa8kMzx2CoTRZxuVMF1qzqjyolak+ZktkK2iejgLMKkcb2oyJCTuQtOocxBhC7zSXDguxpO/O7CCE7v4awkTxXlEG1hOClnO1ct8IVp7zZEoaydcp2rIE75tI3xp6hwZmdVMnVyD4dFcuoObL4wJ8yUTvxWwHceZc8Aq0saYspmH7SHluj2AqXk2cVfH9BU7zA+JHaHjZbXZSfF9qmcRzauZBd4mzprmMFyTW5kdNatkjW82qghlZp0Gcdzf8YJQWacl8KiyVS9vagVdLkUUrAi5gqQzIRyT2vZQ12aD850spLYdg01JzTpdTyt40CcYZqzNhPWwqhF25a0G9O8sqqlY0BJ8/GGool4YYYSlioKktTdZeIGlo46U4hX04ubLXBnny8m2FyDVukc3dKXy9FJAmzGyaa/7SbrRPPgWG15KTiRje8wflddtHbfe7MdLhvnmDjzZmfN842Ot9EEnTMdN43NdYLOQ77pd0EnTaldK4UNtVxlyUxeTEVjXowR1NDobiZH2XgKw3Y/W+tyoM3p+ekMbWiFzie8ZkSHupYlRFZAgSt7drbyocnKg1fGrBB6PolOZBoJ8cVc78ZrfUn2lVgyhwMW+nqhkrKW8yYxmUr6YROV9qSDGCifBCZUTgVznVLxiWMyvdwJRSNfVgl8CrTAROENyXQqRl3kAPZWF18y8KW+NUhdYtOUWvrL7YRIYDKo2M2WmIXmuZDSiuJWYzZ08LnctevL5UJpIl21VBFtuK2msaXB88HsqHpyNY3VxsPm7L5eahoyX5Gd0QdrQ4L9iSCI1eXowqa+NNYFHG4hvOtaH+Fydy4jwJnik3opmH3XukVNMpQANDEzqg0FvO7A8R3PrbpZONRxMxPX6ATpz3AvNZN4WVMiH05ad40v9w08x1aBq8m4r24bWtsFQG04I2jycYPJKBdY1CkLYm922kvcutdnJMC+MzxVYZNDJD5YtKqXSQ5R6ezeVcvLenHqpvudt5qU6sYX95tlHhQ5IwZYFGfmlKgDxebOwYVUjCK/4NzJz1ksouDCj4WK8h3twq61Y3kJVC7xfYPs4flEJY4959InGVoVy4iLO8qSyPE4tMm9acPLnbaGKwa3anNMT2AAlqanTPicuJCF6W3ZZrehWZkhqQUk+HRnLGfmWoDZgN5aFLNcuFkL0X0+W7mQWKDWRobTvcNF9HFcBtvtUmidHMsvHtUvK1NH2+Vq2u0snBN5nqRkbcFFOUSBkr8uJpJLnaRgTnCL/OByJStSKr0zRVQPMGzh7RfscTvttirDWnSFLVy8TrlyHNDK2KesJer4p6bxstXWLk/yWq4m5cK8dGP2Aks0dVQbIVKXM1yyUOscs2RsnW0X93SODaSw55sEjxCNx2M09w6bg2su8EBu5uRSEq1+FbOurGilbAvSTlqtakMz1/xpdZKNXExtcYV5mLmjjvtgA7bfRDqjS2I21ZYtBgUnWDAB21jVzDHK7g7x8XBc5RzIIk3luFIKxInyfrfTLO9wkaPUukwme7ddjznS0OaXw6mvBFtZFjt2XiyX3XK6Df1VFE70A8Vk9BGnnZyk8iVCYYwX6IpJCC2KSUcEhuCAdpS9t9qeqLA2DlkBQ5RA2H2iC5ykgWqL2OyOh7nYJUIiLnAInumoSkpbHIUDyM+64MDZ58qm+G1dAuicHV2kJFnc329R+MyHK3Ndi93ZR9FZstvSrD+OmGY3Jk5qRoWH8bbQKwYKGIEFoGzDl6qZXJaTfO3SCICI0pyf80QmWrdkJiqCu/G2gLxzUfhZ0cOwIx6WuZirc/VUQBApnS/jWY06xGTnG45Gkztk2jvzOIYXCXLRtoWUM2sKhFZ1zq0MELR6GNV8XtaFOU/MtPbMH0lCWbATbpPEc5oqYWkrlx0NK5MtMXfXbN2LXTAJ93t21QiqPLP7i9xt5jm2QJHTuJWO8srKNhZ13Elpc0nTSe9j0hizUQIkriDOJajv+/vjJMoj05F2wpJZwcKFhS5Ih8yb6UXft1tBd4kZtpw4KrTNz80hJhg4g2b0fnxcUDa8h1fZbCtcCF6ae2flvJjCtc1hZnI59jOVMEBmSclHyyN71ZtoyhobN94hMErKP59T2PQvFe5lC9Sn2hMB+YfO8zMXcvPlitLzOUQ6AqmSuzPraAcYDhpJtqQk81NNOx1irU6xAFOhyFRP7jwNcYYnRTfQxhP7MnbzsSdoFH/c9WKhEzZIFI9Bt9zp+aWfT5ckknpKzjPcRqdh2q42JOJz65Y5hXGOH6MdAjVrllN7ENKzrN1sW9o2aosIii2b6Ysahc6mtvUUMisZZrNKC0NFViRIylY1rW8YsK6EEYtY6lX4YOLHOY2adbXmAw8+7OXW6tOKhk4aZTVzBtg5HS0cZbHp2OO56xIk2ZjRfLHdK0TIHhENwhiOVs7m0na4GZ4ut3mMM1uVZuh2S83FY28rCppOEFlnrO3UqVgfm9tqm9cBcZSgtWUsxJZneFyNlhaDHlTBy84qgZ8PxPLskpIYefNZaO8FFlttPWw9L3LTbJrKTZhYsLwuRtO2KAk53aaijWdgjRiOdQMvxtxEaI9zeSmzhYcf2YUmMwWzJpcBwbGT4AJ5/AGx5wXibpZraKu0mjR2k/GmykTmJNoaOlXPm5rYKvV5s/e3l+N2L5+nNtbtVW+73p53XjkJt2eiSiZt7/tznHRgKtazll6rpXVYY9wSPEk4cT0J8HOQueVORaHNktD5selW0OpUpEwRQK7HGCsh0TVSYHuQZPUTG+tDvygWGUHi51BgM9xQNFxKBfgcmEFtUmDts953CsFzEgZvQnVnOX7esc56S6MgKUoJH+aBesn8ogiSUrYzuookHVh9blSZvswSejmjJsdQQ4MV3Rtz40yk4fi8kIH6q/SgFr64WKILc03tI4VMjzudCjfOMUIplzw7FLUSNxCICHuU2mA7erudIcZKzAkzrfKJCJKTeUwJ6CoFNU1wSMNDp1AIBvOdRIzFczKOoIQSuJoUURES0cV4PCWK2Qo28Gau4K032/QTT4XC8hw1cdjmOCPZRKC1mml6rtkpF2Sv1+RFrtB+Aiw3ZnXbHE8Zcd4Wl2aG5bQYyuUm35GB7hjk1CT52TQ7HVuCD8c9jrEWP67nVFxk1cKw+1xW1xRJs3smJHyh8EkhU/nJShez5pine2TSH2Gina+SU6+gZqCUzCrdCPZCDfgcA2nrfn1eciBOxtIuvUynWDrTcr2VhBXRq4wNymI08SummhwWIA3nBZdPTmN3r1VzWNAlv4tO/ZHYzNc6RI0LBZ/ai8JxiVQMugzfuEdFP5+oDrXNucZdAI4yLt52h0hYmDEeuEfb4FKsWSc4vjrT0ayIWE89ONqyQ9pF39Jbeac4xnZhLg+9hy4vk7baTuocNyDmDG/aPm4Jr0PWWMcbIKzgbusfSK7rnFRvj7QhMZN5jcf8UsVndbYD6cNE28/NwuMjnjfHES3LnuGdjctOMSY1yxll01+Oa4KxrKO2uBznc/skh1RxmfXWiSGDLqLNWdhhElGHzjmm8lUYL6H2MKYBSZ5iZ6G495gFZyTJtJsZVEX33aVRQvXYepXrbwW4vUjT0IyK4yWrgszScAaRS8eQSjVC9wCgzrFj8xOdta0GuNh5p0hyBwUu2rnUyhpTY25sZSBwFsugDrW2zGezzdTS19WECRuT2gu9isAn1EWQjahI7hiF9f508qcex+WxfJyLS4ka58hkizd03wcn57Q+rYyoJfwcORySxS6eanof2GOik1WaM+2G9w4VqKTPSUSt8RQ6MYfEVN0dSs7zEI5NXPVlNViCGsHnW7N1OduQ2VIw68I7Y7XqjHkRMdKCwqUcYfolPYNEU0Z6YR8z61ax+Isyk11O3YUatd51nbqe6KQPy1anhX5kq6RzNBbIqcv4VDdXyWSyOieqcjrVsu670m4aTC2MyOVNG2mhqa8PjQMvKZe/wFNKxkvEaJvekufU/iRHStxxXjDbhzvZTky702Nhf6nYJTGbLid8dJlvWI3mCXTXIVpwkeZRRCrckWwPM/2I53S/9kKiNloE0REonq09VDSP/bREESXkIR/ZcHW+X8HVsljUcq8vQDLFJEemZdM8DOzT1jGETRWbuuLqQi2cqHRmIU1kMSAScUhMEaHcsiaViPk2JBrNnXTb/UEOY3XjLUUPc9VpO+208wZkx3GrQWdVLhbdtuRnQObbntX6gF31lruKkNXW18NxC3P0CV7THEkRs5J3L1DlzNvKhzoBwDS3PxFpqxsHBfOLcFLwZ3LsYSINHOEQurQzPs0DZpo3FxB52XDLzHKj2Vm8u4kaCJKi02J/PDQiZNPdWkeiY70njBw6UHBlWvoi6MSFPJ+2qNew/bnD16aExH3joYxwJnjgYfs8dGttoThBBE2Xm/36EO2FYGEm+NhcBk4F8E3g+flBTzKquTQs4yitBBmHWtJTPhcgaskos4RZYZRRG4yyKJ3F7JRgfIycA3F6ZLVSQAWcWiKHzdaAuslso6wz3U4dxYoLV06TrgW5BTLVFabUFWW3XZ8PUxFJNztHNbupuFCIyWoxTym9vTikow7f4g+WieF2aIl2R08NAMnzKkRybKcxRtoKm34jiEoz9vIjoWPCJi1ZobLmCJGaRV8dE09s3Hxda6gtHr3yxNNbViXajBOPAQ6hiuLKBrrbQ0c4rLA1UJctq2gyrio9Eg+VIUzpokYRm9uMjYJehgsBNVb7FShXt86SKUEWu4hsjl14YpRPis2enJ3ZRI2qxtrU59POwIQdtrewAt7Rs7iwpF4K+nKl6Ey0CLj9ITKjFV/zglJt3NiW1vO2bXFooZh7uXdQluerTjrJHnZKbaO0RLNOU25DFvE+ZfYbT+TWmpG56FpaCZswPXaas2dOhSjGNL7aIiYlmmjoJQG/UyIxQF2zEaOLdYb2uSZtmgN+oSc9VzYGP0+KBdtqgoCQ7WLeL9CG6umdrmMFji7UI1osG2/KSB5DjBU5EK3dil7486UVSWQ56ZeeZriLQij3XTy1FDXpi0LdaYWgs5t2zZC801ckC4dFJbniAqqzpep2+OmsH6qdgETBeiaCwLM5iRGGaApC+uKFS6nsrE09Qd7nm7JuqN2qBJXwNje1WvTMrbVutHp55gKvMWXIp702Wga73XJHpeHCw6Z4oywbnBRkdKsW47QEtgKboAoWe0ImV6Zq2RUvcez8OM6nAdpcqEajpWq6VJylBUzVwKf98ShtqJJoBLpjkmm8lDn5kKBpKYhtGMzPQoqGYX062qY39xOsP1RiLZ3NXb6zWp62CvSyC5TTNHVIslhMUyqwQ2rmJwU6nmstncpxmh9iKMznqBKsFuYqptywxLmglMcbwx6zGeSRXrA+LtJ6TwbZpnEWSMoubS3UqTo/nYL1RNCaMcbGgnFUyyrJ4tJyTU1HQLhdbSHbNPmDQKbroI6PwtLE2AtGLGXN35y1nM7QrTMhIVjb6idRMxmQAmJhS3RG6rq475cNlvf0HHdoXvdigN/dgVmzh1NHMHwSrVg835nheWtPNzl26XMKX07dKM0ZRISITpPz2Qa24na3ko3lBKnP1fgIMUFoFi7VelJEVom3iMaRjHP8iZMhjV0RuYiHM3bNEWdLyblDwc3kKrnIas3UruJOm9Uy3LMnqJwudqIsAKcLTaEvqORC75QcWkUKLLORYoD4sqjIoJxZPEOW+XyC+ciB3pI8jbYH91Tu4Pl4k3Elu0GCVpsGpwPdcLwa41BKuasWSvEkQAgRRNSgox24AI5ex96KyVXg/Bvh1IOCvJ95xkzAG9I9dxRAaBYqLIsq8FRcJvt4SuP8ca1h4ZHuWxLebsQTk9lSMaNowwEoKqRnhaRWtBjMzv6B1vah6keusaPRvekEZHXCXcgi2bZBoznnHFSSDjR7y6CLULZMGmUvRDA5R5NxvwUI6yOU453HvWQtib3XdrogTJZ6NDXLVcZKHE5s6cqerzZpQsO6c0zwUieCqVZJOZ6au0VbwwF5iC+IzRO0TVgg5oWt0R/swvLrk8J7lqkzq/3Y2kN7Xx7vaK/Y6kyv7jUeS9aXbEqc/HRnB1hsr9AGr44ISKKPx31LpHNkRUmYeArPkbBl04MjmClyqFbnjdWTKah7mlXhQegaPy5XJnCqwsL5xUk6G/2kWxeuT8iy3avNhp7GQWntW2SzZ3WTyGxjJvKrMJ1SMJaqtN1Rcq/2Sh56aXTpuTTCTlzEAqV3RcAeRPy83oxdd1cseTdiCb3lAvi87RoLPY8rn51uwzrITP2YeuJ8VrqSrV5sbg1RmCvH8OkypnMzivA2CdRkt0eqKjnXB7KjnF0qRjNNb4NJMF6hUbI3kHGMzeNwi6toVeZrY2lzU1QkY83WuZ3Ta7APKrWtBnE2Ix7V08Ydz6Q67g1h3AoYRM8Lo0OabseM8zrUxxd6GnCqI9CrpsOKcd7S9KyN+VWpIE5qRrvVxnB0YzY7GHV9CoKFLa1S0REnO/lCpUHmQOEFhiBG7Nf8QpnCnbVPcGm8zpsFTFHLmD55m5DyxEDpFK32U0XE2RyuWPa4bvRgAzJvQjrV2slstRgB2bKnlnvdZON0qRNlZ8n9Dj1x7HmVp9b4vAbp/86JyoDJLGyrrA5r2RVtJk/VOs5kXBY3uHU6NOeWDYCHYuneIGQptsZp4s6XTarEk/3YqON5WO0ttF6NN/O+ZMis2E29pW9XQqB2pcPwYWRmLtXoMNtoMSwE4Ykfo/VxTMfYeQmA/rTRty1tuvzR87YhlDZzF2Qmx8PBWKguk1KLA49js4PknvabA0+hZlQSjD6jUh7dprATxZuor9zmaB3RidqLtFBtUXSMCwiRHGe4ZrYFRSBI5MytZuHh1a7tTHwRr3kk5k7QWVdmUMVwmkRYcVyN52d/L1bppS3miG9N2VSKqizuVvtoYVJQXIbORBYFV2c6JNB4na2jcdNTkXtKU3572LobASo5lRecbbEWNyA0m9ulZXPVhYNCSNK7ehqNV2160lWVNk6QWIilN5vJYQAGGsfLOFgohRBZ3Tzox0Wb8NoSzTj0JO9OZyWnlEgPp4pqwQ1tmf6hbwql3NHmYs5RjaXOLXS/ZC+SC/W+fDzRBU1y03mHz9upmBlFY9R7yIBStjeriFPxbU1Pi7rxQa24rpMIbwJGYewFwNGLQiebwBHdqu+mmBuh9EJ0ciiYwZxpnrQFju13/FQQyDXcwzSBq/JCER0ksKZrdLeLW9/ikAk7NOGxCJXb8wa2ohnNyHNdP5X5cXo4XCj21Bw1mN7ZTeUaFhqQ+NSRpnIXEC0WnjaBl6niilir2rHNLpdqpq/GMqUbynzsjte6mcIzJS+r8YzR3RrVioj3ynUum7uxmke20iyIBdsLR8pjlxeoQUt/Ijrj2UzMtY5q9V3FrfSQ7xhozXMg/1MV2+sKholai3FPZLE/89OEt5VdtTYFm0MoZqkKOk5NUpNPOr3VV5Y/VmpiOi91VPd3Gcf0rKnixi6dYQh1vCyi7TJOZy4KmDLNiXXCa25unI1yehTQtgzLzU5LttKWRToMmXJBPyUtpJi6Wm5jx7Ccu9G+xT2GmY/72BLXNhMHesdvOiqMMepkdSjj4c2EPJiT3qPrhXFig2Zf8K1j2RFAky2NeS50KKxoE2GZvUgRVLDYube2ILLZZrxR7Y/deIftgtWpM3au19oIr0+VpCrMCzDdWcor6LbV1hstG7Ndc7CjCQT5p7lEhxKd425/aOc80h3WhEjzTsiuG5rm0IkcZeZ2DOzg6EQdB3EyuaVzcV2jx2wDfMUiUOtQo6E1UWuQvXincOrq81XBeHArL9dL4pIuVwGEO0jExwdrEqBHau/avkTS6ELslz21qsYgYV5BLJYYCILWmRXhyIz0g1MRSSEV+YjtqBtZkfAdFikuW+uiCk0xgITiol80IbK7OCKjHlmxmYnEOjb3fiaW2wlnQ4aMb1z07B4YWW/5STUvdrJ2WigJqjT8qjolWj5GpOmq1pGEo+DpCRTqSlSXJC6hKD4+yZJ9quB6Aco9v/JOyO40zetixW9m05lSJgQoIlTexlppVzq7LMnjZmlv8hkf5si6EI3lejdjcZHJF37ggWyI03f20dWmhrSn3LxcT+bBFCrxaXXm8mhxoY9qDUUBwqbbvY3uxNzsbRGltuRZAim9EvRzMd1K7JLEZDOFJiy8k8RZ5c3DWbVzT3NrHXNuQy6ZdKGtxrtTubdsh0PEC8Ztpy3NS9upiIEkdR5SbQihtbBDMnsXblJVnNTBLFt3Uy/yNyym+Ft2k8j9NnS3i2Xvd5k+x1oDpXbqARWRnc77Qm9fhD28dWQHvhAlDC/d9HLmij0ZLTs5dgDANOp+Frj6MYxs2CLplhTo+W4xD6G9a2QlIy8DW+8dLojOduUBb7Mcra5NyPYNKiqmELydQyCpu8wQCPb33hJLYCzoN3pB9yCvx2OF2MenWsHHzA7RSUgvVXyPTTdwvkDrfK/slFqXM/3cQ/vDRVc9EnNPRHHa7KiVZCKZS+JqI0/EukSn624NMhCX0iQo8UKIOI9nZbZySFmfYZC9wSlHcjWaOS8cNkM8UIfEZ9bJuxjtdSPvWEPrKksh2wvEselYE93LttrsXUJtqxNSZ3sv8LUjHCWC6U0W5/HKxkPVnvDy4WIAVB3DZw+UEkEXaNM8Lk6HdOq6ZKlujuPjBYLhvaGVUe1Pg03seKdqclJViDspRLtZB+WmUZhp6xUuttYmKdk5/HSM5IpK5gQhlcEOVbfTo07khjrboWXuy5ujoIirwAgbSMaWxrZbwxyIELh4xITLRpxjyGRIaWP/mLNUe6B3IPFAPFKuEOy4pJbnfVrPNr7CYtM+1w60Ho+ZEOGNBgNZvhRkbWg6U+uyHVeFv4DRbjuvTHc+ro3DpWQvSM91uSiYIH0oT/uIcRdA7Qs+PPm1YEsIeypZqrNTYs+nPPi1cLcbad/Vqx5EI/0gipDhmAJDLCPDj+iTjXKdGU2nRnwhKEbuvObEdXrB4XbuLdnKG+uyygV6tN3IwhSS9z3Ryxs2ilbpAi3cmueM+aa5TDXN3O15Cqvq8yG4wMdd47NHn19q6iKTrXG1DXViim03Wn7wOC47BuHOkZBdb6xVJqGWEWXwSMZMnNZn+hVDk845RnZjTAB57UoJYsijFkkohRAcwv46T3Z4FuWHvDtMSrIwqwO2wcaLGrYS7DiPsK0ZpCoiTuZkQ9bLzc6xVlJgsr6FIRw7veiLzCmGS6S8qpbp2oTgYL/EZhwqHwtXpPj9XFjvsbl52objxqXnSxM10lnsMgkLnIyQJ6By2DCqVPKzgEhEOLa6KT9pEo0LL5ftlp+cFliGb/wq551teJrGnNxvdmPUAFV50ZAtfDyksCbqku6Ep+0eBIXtGkqlpdKrOjqVAp3GCl8TEX92iVdGale1K63QZFZR5BJEJ8uicXJD7cgxiQqCBqqzqcJxUlXQGHKYSd58fNS4sxKlfp666FaMZZSBzZxziKUQ1MnR2BOpUbMMdxKXKqVsNye44Y0+wUVTVYPVzKsvRD4vjWM8pukqJsX8NCcMfupgcwtfTy4TktVZdCnEx2h1hNkDqFq2Kxxmxq0nmEvyBLdM2uHlZYMrvivRzcnL+MU0ErluIy3KjM77tUxd/OM4Ok/i5nJxSWM2gcYa7fnjlIQTUGASRS6u5pWOcwga2416GFfrxQyuWVc86FxKi5v5UpqowYkqevLU4bPmIFVeQsgwjp1DRoDQAIH3Yrw1GpuwORatfC4vsW4+PTY2q4BcquGIhWG4VQaN23rqUcT4BOo+K7eo1YQng447qrs63KlM37RePllmedYtSI/wNqYijotDbB9Wph3vYBLCL/sFHHjLbXU5mHrYm/zc35vj8EIeJCFE/X2NQdSElHQMWp/X20jVp4iqrI5nxA1y5MAooFY6opelxKtBdTqOJUgdM8WyyvfAIidz4zKZn07rgzpX8DxdHIpYwqW+v1C+5TtbInH2La8USMDqR+5YaEmd16W2zRd0uzQgYmOcQTkX9xNtvxFVXy9SGTlr5AzzpyyVYyo+m9KHYjVZJuQ5gjy2OIckIhVGwwtGfThPagO3aqnexuRmTc6pOSSSXOibCGkGFHVvK763Mb/2haKh+fH/Wg/mrV0yP4MFM8cbekqHLvNPt77eV1f/4/2b0onA2reW0SppgnsD5tAw+uHZv9Tnle/E3Xq0h38h7XUpa/hvFzxrL71/hwT8eW+cv/6nDdymAL8fWnGdprQeul7vjfs3Zj6O3/z9/wFx/25YJGEAAA== -->
