---
name: "rar-rapp-store-navigator"
description: "Help the user navigate the kody-w/RAPP_Store catalog. Call this whenever the user asks what's in the store, what they should install, what categories exist, how to install a rapplication, or how two rapplications compare. Actions: list (browse all, optional category/tag filter), search (keyword match), describe (full details by id), recommend (natural-language goal \u2192 top 3 with rationale), install (curl one-liner), compare (side-by-side two ids), categories (facet counts), spec (explain the spec)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/store_navigator_agent", "rar_sha256": "909f0778d6d9066e668adffc72f75be4d55de9552ab781df337afe6fd54e0d03", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "0.1.4", "author": "RAPP", "tags": ["meta", "navigator", "store", "discovery", "rapplication"]}
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
