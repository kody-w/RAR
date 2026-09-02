---
name: "rar-rapp-store-navigator"
description: "Help the user navigate the kody-w/RAPP_Store catalog. Call this whenever the user asks what's in the store, what they should install, what categories exist, how to install a rapplication, or how two rapplications compare. Actions: list (browse all, optional category/tag filter), search (keyword match), describe (full details by id), recommend (natural-language goal \u2192 top 3 with rationale), install (curl one-liner), compare (side-by-side two ids), categories (facet counts), spec (explain the spec)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/store_navigator_agent", "rar_sha256": "d66b3003e0a562b0af69dfa070eae0a4ca6dc97cb53438b9e636c2ffa55214ef", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "store_navigator_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapp/store-navigator:9898dce14de8837f7e6813cbe4368793f00c8dac3fa7b76eeb4e7e35ebdf20ec", "kind": "skill"}, "version": "0.1.4", "author": "RAPP", "tags": ["meta", "navigator", "store", "discovery", "rapplication"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapp/store_navigator_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `store_navigator_agent.py` is
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

store_navigator_agent.py — help users navigate the RAPP store catalog.

Drop into any RAPP brainstem's agents/ dir, or load into the rapp_store
vBrainstem. The navigator is the entry point a new user should reach for
when they ask "what should I install?" or "what can this store do?".

Stdlib only. Uses utils.llm.call_llm (host-provided) when available for the
'recommend' action; falls back to keyword scoring offline.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "Which navigator action to run.",
      "enum": [
        "list",
        "search",
        "describe",
        "recommend",
        "install",
        "compare",
        "categories",
        "spec"
      ],
      "type": "string"
    },
    "category": {
      "description": "Filter 'list' results to this category. One of: productivity, creative, analysis, data, integration, platform, workspace.",
      "type": "string"
    },
    "id": {
      "description": "Rapp id (e.g. 'bookfactoryagent') for describe / install.",
      "type": "string"
    },
    "ids": {
      "description": "Exactly two ids for 'compare'.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "limit": {
      "description": "Cap on results (default 10).",
      "type": "integer"
    },
    "query": {
      "description": "Keywords for 'search' OR a natural-language goal for 'recommend'.",
      "type": "string"
    },
    "tag": {
      "description": "Filter 'list' results to rapps carrying this tag.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `store_navigator_agent.py` and embedded as the fenced Python below (sha256 d66b3003e0a562b0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `store_navigator_agent.py` first:

```bash
python3 store_navigator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 store_navigator_agent.py   # or on stdin
python3 store_navigator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""store_navigator_agent.py — help users navigate the RAPP store catalog.

Drop into any RAPP brainstem's agents/ dir, or load into the rapp_store
vBrainstem. The navigator is the entry point a new user should reach for
when they ask "what should I install?" or "what can this store do?".

Stdlib only. Uses utils.llm.call_llm (host-provided) when available for the
'recommend' action; falls back to keyword scoring offline.
"""
from __future__ import annotations

import json
import re
import urllib.error
import urllib.request

try:
    from agents.basic_agent import BasicAgent
except ImportError:  # pragma: no cover - cloud / openrappter / fallback
    try:
        from basic_agent import BasicAgent  # type: ignore
    except ImportError:
        from openrappter.agents.basic_agent import BasicAgent  # type: ignore


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/store_navigator_agent",
    "display_name": "StoreNavigator",
    "description": (
        "Lists, searches, compares, and recommends rapplications from the RAPP_Store catalog over HTTP, with keyword scoring when no LLM is available."
    ),
    "author": "RAPP",
    "version": "0.1.4",
    "tags": ["meta", "navigator", "store", "discovery", "rapplication"],
    "category": "platform",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "example_call": {
        "args": {
            "action": "recommend",
            "query": "I want to turn raw meeting notes into a publishable chapter",
        }
    },
}


_CATALOG_URL = "https://raw.githubusercontent.com/kody-w/rapp_store/main/index.json"
_SPEC_URL_HUMAN = "https://github.com/kody-w/RAPP_Store/blob/main/SPEC.md"
_CONSTITUTION_XXVII = (
    "https://github.com/kody-w/RAPP/blob/main/CONSTITUTION.md"
    "#article-xxvii--rar-holds-files-the-rapp-store-holds-bundles"
)


def _fetch_json(url: str, timeout: int = 15):
    req = urllib.request.Request(url, headers={
        "User-Agent": "store-navigator/0.1",
        "Accept": "application/json",
    })
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())


def _haystack(rapp: dict) -> str:
    parts = [
        str(rapp.get("name", "")),
        str(rapp.get("id", "")),
        str(rapp.get("summary", "")),
        str(rapp.get("tagline", "")),
        str(rapp.get("category", "")),
        " ".join(str(t) for t in rapp.get("tags", []) or []),
    ]
    return " ".join(parts).lower()


def _score(rapp: dict, terms: list) -> int:
    hay = _haystack(rapp)
    name = str(rapp.get("name", "")).lower()
    score = 0
    for t in terms:
        t = t.strip().lower()
        if not t:
            continue
        if t in name:
            score += 5
        score += hay.count(t)
    return score


class StoreNavigatorAgent(BasicAgent):
    def __init__(self):
        self.name = "StoreNavigator"
        self.metadata = {
            "name": self.name,
            "description": (
                "Help the user navigate the kody-w/RAPP_Store catalog. Call "
                "this whenever the user asks what's in the store, what they "
                "should install, what categories exist, how to install a "
                "rapplication, or how two rapplications compare. Actions: "
                "list (browse all, optional category/tag filter), search "
                "(keyword match), describe (full details by id), recommend "
                "(natural-language goal → top 3 with rationale), install "
                "(curl one-liner), compare (side-by-side two ids), "
                "categories (facet counts), spec (explain the spec)."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": [
                            "list", "search", "describe", "recommend",
                            "install", "compare", "categories", "spec",
                        ],
                        "description": "Which navigator action to run.",
                    },
                    "query": {
                        "type": "string",
                        "description": (
                            "Keywords for 'search' OR a natural-language "
                            "goal for 'recommend'."
                        ),
                    },
                    "id": {
                        "type": "string",
                        "description": "Rapp id (e.g. 'bookfactoryagent') for describe / install.",
                    },
                    "ids": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Exactly two ids for 'compare'.",
                    },
                    "category": {
                        "type": "string",
                        "description": (
                            "Filter 'list' results to this category. One of: "
                            "productivity, creative, analysis, data, "
                            "integration, platform, workspace."
                        ),
                    },
                    "tag": {
                        "type": "string",
                        "description": "Filter 'list' results to rapps carrying this tag.",
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Cap on results (default 10).",
                    },
                },
                "required": ["action"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)
        self._catalog = None

    def _load_catalog(self):
        if self._catalog is None:
            try:
                self._catalog = _fetch_json(_CATALOG_URL)
            except urllib.error.HTTPError as e:
                return None, f"catalog HTTP {e.code}"
            except Exception as e:
                return None, f"catalog fetch failed: {e}"
        return self._catalog, None

    def perform(self, **kwargs):
        action = kwargs.get("action", "list")
        cat, err = self._load_catalog()
        if err and action != "spec":
            return json.dumps({"error": err})
        rapps = (cat or {}).get("rapplications", [])
        try:
            if action == "list":
                return self._list(rapps, kwargs)
            if action == "search":
                return self._search(rapps, kwargs)
            if action == "describe":
                return self._describe(rapps, kwargs)
            if action == "recommend":
                return self._recommend(rapps, kwargs)
            if action == "install":
                return self._install(rapps, kwargs)
            if action == "compare":
                return self._compare(rapps, kwargs)
            if action == "categories":
                return self._categories(rapps)
            if action == "spec":
                return self._spec(cat)
            return json.dumps({"error": f"unknown action: {action}"})
        except Exception as e:
            return json.dumps({"error": f"navigator error: {e}"})

    # ── action handlers ──────────────────────────────────────────────────

    def _list(self, rapps, kw):
        category = (kw.get("category") or "").lower()
        tag = (kw.get("tag") or "").lower()
        out = []
        for r in rapps:
            if category and (r.get("category") or "").lower() != category:
                continue
            if tag and tag not in [str(t).lower() for t in r.get("tags", []) or []]:
                continue
            out.append({
                "id": r.get("id"),
                "name": r.get("name"),
                "version": r.get("version"),
                "category": r.get("category"),
                "summary": (r.get("summary") or "")[:200],
                "tagline": r.get("tagline"),
                "has_ui": bool(r.get("ui_url")),
                "has_service": bool(r.get("service_url")),
                "has_eggs": bool(r.get("egg_url")),
                "publisher": r.get("publisher"),
                "quality_tier": r.get("quality_tier"),
            })
        limit = max(1, int(kw.get("limit") or 25))
        return json.dumps({
            "filter": {"category": category or None, "tag": tag or None},
            "count": len(out),
            "rapps": out[:limit],
        })

    def _search(self, rapps, kw):
        q = (kw.get("query") or "").strip()
        if not q:
            return json.dumps({"error": "query is required for action=search"})
        terms = [t for t in re.split(r"\s+", q) if len(t) > 1]
        scored = [(r, _score(r, terms)) for r in rapps]
        scored = [(r, s) for r, s in scored if s > 0]
        scored.sort(key=lambda x: -x[1])
        limit = max(1, int(kw.get("limit") or 10))
        return json.dumps({
            "query": q,
            "method": "keyword",
            "matches": [{
                "id": r.get("id"),
                "name": r.get("name"),
                "score": s,
                "category": r.get("category"),
                "summary": (r.get("summary") or "")[:200],
            } for r, s in scored[:limit]],
        })

    def _describe(self, rapps, kw):
        rid = kw.get("id")
        if not rid:
            return json.dumps({"error": "id is required for action=describe"})
        r = next((x for x in rapps if x.get("id") == rid), None)
        if not r:
            return json.dumps({
                "error": f"rapp '{rid}' is not in the catalog",
                "hint": "use action='search' to find the right id",
            })
        return json.dumps(r)

    def _install(self, rapps, kw):
        rid = kw.get("id")
        if not rid:
            return json.dumps({"error": "id is required for action=install"})
        r = next((x for x in rapps if x.get("id") == rid), None)
        if not r:
            return json.dumps({"error": f"rapp '{rid}' not in catalog"})
        out = {
            "id": rid,
            "name": r.get("name"),
            "version": r.get("version"),
            "agent_install_curl": None,
            "ui_url": r.get("ui_url"),
            "egg_url": r.get("egg_url"),
            "service_url": r.get("service_url"),
            "install": (
                f"Use install_agent(id='{rid}') — "
                f"the installer fetches singleton, service, ui, and registers "
                f"the rapp in .brainstem_data/agents.json."
            ),
        }
        if r.get("singleton_url") and r.get("singleton_filename"):
            out["agent_install_curl"] = (
                f"curl -fsSL {r['singleton_url']} "
                f"-o ~/.brainstem/src/rapp_brainstem/agents/{r['singleton_filename']}"
            )
        if r.get("singleton_sha256"):
            out["singleton_sha256"] = r["singleton_sha256"]
        return json.dumps(out)

    def _compare(self, rapps, kw):
        ids = kw.get("ids") or []
        if not isinstance(ids, list) or len(ids) != 2:
            return json.dumps({"error": "ids must be a list of exactly 2 rapp ids"})
        by_id = {r.get("id"): r for r in rapps}
        missing = [i for i in ids if i not in by_id]
        if missing:
            return json.dumps({
                "error": f"not in catalog: {missing}",
                "hint": "use action='search' or action='list' to find valid ids",
            })
        keys = [
            "name", "version", "category", "publisher", "quality_tier",
            "tagline", "summary", "tags", "singleton_lines", "singleton_bytes",
            "singleton_url", "ui_url",
        ]
        a = by_id[ids[0]]
        b = by_id[ids[1]]
        return json.dumps({
            "a": {k: a.get(k) for k in keys},
            "b": {k: b.get(k) for k in keys},
        })

    def _categories(self, rapps):
        counts = {}
        for r in rapps:
            c = r.get("category") or "?"
            counts[c] = counts.get(c, 0) + 1
        ordered = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
        return json.dumps({
            "categories": [{"name": k, "count": v} for k, v in ordered],
            "locked_enum": [
                "productivity", "creative", "analysis", "data",
                "integration", "platform", "workspace",
            ],
        })

    def _recommend(self, rapps, kw):
        q = (kw.get("query") or "").strip()
        if not q:
            return json.dumps({"error": "query is required for action=recommend"})
        # Try LLM-augmented ranking via the host's call_llm shim.
        try:
            from utils.llm import call_llm  # type: ignore
            catalog_brief = "\n".join(
                f"- {r.get('id')}: {r.get('name')} ({r.get('category', '?')}) — "
                f"{(r.get('summary') or '')[:160]}"
                for r in rapps
            )
            prompt = (
                f"User goal: {q}\n\n"
                f"Catalog of available rapplications:\n{catalog_brief}\n\n"
                f"Pick the 1-3 rapplications that best fit the user's goal. "
                f'Respond as a JSON array: [{{"id": "<exact-id>", '
                f'"why": "one concrete sentence"}}, ...]. '
                f"If nothing in the catalog fits, return [] and explain why "
                f"in a separate JSON field 'note'. Quote the user's goal "
                f"verbatim in your reasoning."
            )
            messages = [
                {"role": "system", "content": (
                    "You match a user's stated goal to the right rapplication "
                    "from the kody-w/RAPP_Store catalog. Be concrete. Don't "
                    "recommend rapplications that aren't in the catalog."
                )},
                {"role": "user", "content": prompt},
            ]
            resp = call_llm(messages)
            picks = []
            note = None
            m = re.search(r"\[\s*(?:\{[^}]*\}\s*,?\s*)*\]", resp, re.DOTALL)
            if m:
                try:
                    picks = json.loads(m.group(0))
                except Exception:
                    picks = []
            if not picks:
                nm = re.search(r'"note"\s*:\s*"([^"]+)"', resp)
                if nm:
                    note = nm.group(1)
            valid_ids = {r.get("id") for r in rapps}
            picks = [p for p in picks if isinstance(p, dict) and p.get("id") in valid_ids]
            return json.dumps({
                "query": q,
                "method": "llm",
                "recommendations": picks,
                "note": note,
                "raw_llm_response_preview": resp[:280] if resp else None,
            })
        except Exception:
            # Offline fallback — keyword scoring.
            terms = [t for t in re.split(r"\s+", q.lower()) if len(t) > 2]
            scored = [(r, _score(r, terms)) for r in rapps]
            scored = [(r, s) for r, s in scored if s > 0]
            scored.sort(key=lambda x: -x[1])
            return json.dumps({
                "query": q,
                "method": "keyword-fallback",
                "recommendations": [{
                    "id": r.get("id"),
                    "why": f"keyword match across name/summary/tags (score {s})",
                } for r, s in scored[:3]],
            })

    def _spec(self, cat):
        return json.dumps({
            "what_is_a_rapplication": (
                "A packaged directory containing one Python agent plus AT "
                "LEAST ONE of: a UI (manifest.ui), an HTTP service "
                "(manifest.service), or a state cartridge (eggs/*.egg). Per "
                "Constitution Article XXVII, bare agent.py files belong in "
                "kody-w/RAR, not the rapp store."
            ),
            "categories_locked": [
                "productivity", "creative", "analysis", "data",
                "integration", "platform", "workspace",
            ],
            "quality_tiers": [
                "featured (≤7 hand-curated)",
                "official",
                "verified",
                "community (default for federation submissions)",
                "experimental",
                "deprecated",
            ],
            "submission_paths": [
                "publish_to_rapp_store agent: validate locally + open issue",
                "[RAPP] issue template",
                "Direct PR (bundle mode only)",
            ],
            "spec_url": _SPEC_URL_HUMAN,
            "constitution_article_xxvii": _CONSTITUTION_XXVII,
            "rar_for_bare_agents": "https://github.com/kody-w/RAR",
            "catalog_count": len((cat or {}).get("rapplications", [])),
            "catalog_generated_at": (cat or {}).get("generated_at"),
        })
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
