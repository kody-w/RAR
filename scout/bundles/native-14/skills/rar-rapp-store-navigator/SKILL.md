---
name: "rar-rapp-store-navigator"
description: "Help the user navigate the kody-w/RAPP_Store catalog. Call this whenever the user asks what's in the store, what they should install, what categories exist, how to install a rapplication, or how two rapplications compare. Actions: list (browse all, optional category/tag filter), search (keyword match), describe (full details by id), recommend (natural-language goal \u2192 top 3 with rationale), install (curl one-liner), compare (side-by-side two ids), categories (facet counts), spec (explain the spec)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/store_navigator_agent", "rar_sha256": "d66b3003e0a562b0af69dfa070eae0a4ca6dc97cb53438b9e636c2ffa55214ef", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "0.1.4", "author": "RAPP", "tags": ["meta", "navigator", "store", "discovery", "rapplication"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapp/store_navigator_agent`. The original RAPP
agent is preserved byte-for-byte in `store_navigator_agent.py` and in the RCI capsule.

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
