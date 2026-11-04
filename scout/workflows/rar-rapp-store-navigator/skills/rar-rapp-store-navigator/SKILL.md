---
name: "rar-rapp-store-navigator"
description: "Help the user navigate the kody-w/RAPP_Store catalog. Call this whenever the user asks what's in the store, what they should install, what categories exist, how to install a rapplication, or how two rapplications compare. Actions: list (browse all, optional category/tag filter), search (keyword match), describe (full details by id), recommend (natural-language goal \u2192 top 3 with rationale), install (curl one-liner), compare (side-by-side two ids), categories (facet counts), spec (explain the spec)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/store_navigator_agent", "rar_sha256": "909f0778d6d9066e668adffc72f75be4d55de9552ab781df337afe6fd54e0d03", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "0.1.4", "author": "RAPP", "tags": ["meta", "navigator", "store", "discovery", "rapplication"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `store_navigator_agent.py` and embedded as the fenced Python below (sha256 909f0778d6d9066e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `store_navigator_agent.py` first:

```bash
python3 store_navigator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 store_navigator_agent.py   # or on stdin
python3 store_navigator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@rapp/store_navigator_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/store_navigator_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@rapp/store_navigator_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
