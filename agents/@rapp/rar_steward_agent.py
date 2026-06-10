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

import json
import os
import re
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
    "version": "1.0.0",
    "display_name": "RarStewardAgent",
    "description": ("Autonomous steward of the public RAR: surveys catalog "
                    "health, clusters same-but-different agents that should be "
                    "merged into one quality base, and flags noise/junk for "
                    "review — operator-mediated guidance, never auto-deletes."),
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

# name tokens that carry no distinguishing meaning
_STOP = {"agent", "the", "a", "an", "of", "for", "to", "and", "or", "rapp",
         "generator", "helper", "tool", "assistant", "v1", "v2", "py"}
_PLACEHOLDER = re.compile(r"\b(test|tmp|temp|demo|foo|bar|baz|example|placeholder|untitled|copy|wip|draft|sample|hello[_-]?world)\b", re.IGNORECASE)
_DUP_THRESHOLD = 0.6   # name-token Jaccard at/above this = merge candidate


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
                               "enum": ["health", "duplicates", "junk", "agent", "help"]},
                    "name": {"type": "string", "description": "agent: rar_name or id to deep-assess"},
                    "publisher": {"type": "string", "description": "filter to one publisher (e.g. @kody-w)"},
                    "limit": {"type": "integer", "description": "max clusters/items to return (default 25)"},
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

    def perform(self, **kwargs):
        action = (kwargs.get("action") or "health").lower()
        if action == "help" or action not in ("health", "duplicates", "junk", "agent"):
            return (
                "RarStewardAgent — keep the public RAR clean + usable.\n"
                "  action=health           catalog health + quality score\n"
                "  action=duplicates       same-but-different clusters to UNITE into one base\n"
                "  action=junk             noise/low-quality candidates to review (no auto-delete)\n"
                "  action=agent name=…     deep quality assessment of one agent\n"
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
