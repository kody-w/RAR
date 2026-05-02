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
        "Navigate the kody-w/RAPP_Store catalog. List, search, describe, "
        "recommend, get install commands, compare rapplications, browse "
        "categories, and explain the spec. Use this whenever the user asks "
        "what's in the store, what to install, or how to find a rapp that "
        "fits their goal."
    ),
    "author": "RAPP",
    "version": "0.1.0",
    "tags": ["meta", "navigator", "store", "discovery", "rapplication"],
    "category": "platform",
    "quality_tier": "community",
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
            "name": "navigate_rapp_store",
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
            "binder_install": (
                f"Use the binder agent: action='install', id='{rid}' — "
                f"the binder fetches singleton, service, ui, and registers "
                f"the rapp in .brainstem_data/binder.json."
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