"""
M365 Template Factory — RAR-publishable thin client.

The full factory is ~340 KB (it bundles the Copilot Studio solution template
zip + the inlined generator), which exceeds GitHub's 65,536-char issue body
limit that the RAR `submit` action uses. So the published-to-RAR client is
this small file: on first call it downloads the full factory once, caches
it under ~/.rapp/m365_factory_cache/, imports the runtime class, and
delegates every subsequent call to it.

Behaviour after the one-time fetch is identical to the bundled factory —
same params, same outputs, same self-contained 15-slide WAF deck.
"""

from __future__ import annotations

import importlib.util
import json
import os
import sys
import urllib.request
from pathlib import Path

from agents.basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody/m365_template_factory_agent",
    "version": "1.0.0",
    "display_name": "M365 Template Factory",
    "description": (
        "Generate a 15-slide WAF-themed M365-agent-templates customer "
        "delivery bundle for any agent use case. Self-contained — fetches "
        "the full generator + Copilot Studio solution zip on first use."
    ),
    "author": "Kody",
    "tags": ["m365", "copilot-studio", "factory", "agent-template", "deliverable"],
    "category": "industry",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "external_prereqs": ["python-pptx", "reportlab", "Pillow"],
    "example_call": {
        "args": {
            "name": "Predictive Asset Maintenance Intelligence",
            "industry": "energy_utilities",
            "description": "Continuously monitors transmission and distribution asset health and predicts failures.",
        }
    },
}


# Stable URL where the full factory file lives. Update when a new version
# of the full factory is published.
FULL_FACTORY_URL = (
    "https://raw.githubusercontent.com/kody-w/RAPP/main/"
    "rapp_brainstem/agents/m365_template_factory_agent.py"
)
CACHE_DIR = Path.home() / ".rapp" / "m365_factory_cache"
CACHE_FILE = CACHE_DIR / "m365_template_factory_agent.py"
CACHE_TTL_SECONDS = 7 * 24 * 3600  # refetch weekly


def _fetch_full_factory() -> Path:
    """Download (or refresh) the full factory file into the local cache."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    needs_fetch = (
        not CACHE_FILE.exists()
        or (CACHE_FILE.stat().st_size < 50_000)  # truncated download
        or (CACHE_FILE.stat().st_mtime < (os.path.getmtime(__file__) - CACHE_TTL_SECONDS))
    )
    if needs_fetch:
        with urllib.request.urlopen(FULL_FACTORY_URL, timeout=60) as resp:
            data = resp.read()
        CACHE_FILE.write_bytes(data)
    return CACHE_FILE


_runtime_instance = None


def _get_runtime():
    """Import and instantiate the full factory once, then cache for the session."""
    global _runtime_instance
    if _runtime_instance is not None:
        return _runtime_instance

    factory_path = _fetch_full_factory()
    spec = importlib.util.spec_from_file_location(
        "m365_template_factory_full", factory_path
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    _runtime_instance = mod.M365TemplateFactoryAgent()
    return _runtime_instance


class M365TemplateFactoryClientAgent(BasicAgent):
    """RAR-publishable thin client; delegates to the full factory on call."""

    def __init__(self):
        self.name = "M365TemplateFactory"
        self.metadata = {
            "name": self.name,
            "description": (
                "Generate a complete m365-agent-templates customer delivery bundle "
                "(README, Setup Guide PDF, 15-slide WAF-themed Overview Deck, "
                "Eval PDF + CSV, Icon PNG, Copilot Studio solution ZIP, agent "
                "scaffold, architecture diagrams, CUSTOM_ACTION_SETUP.md). "
                "Returns the bundle path."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "name":              {"type": "string"},
                    "industry":          {"type": "string"},
                    "description":       {"type": "string"},
                    "agent_class":       {"type": "string"},
                    "agent_file":        {"type": "string"},
                    "features":          {"type": "array", "items": {"type": "string"}},
                    "capability_categories": {"type": "array", "items": {"type": "string"}},
                    "pipeline_steps":    {"type": "array", "items": {"type": "array", "items": {"type": "string"}}},
                    "audience":          {"type": "array", "items": {"type": "string"}},
                    "benefits":          {"type": "array", "items": {"type": "string"}},
                    "outcome_subtitles": {"type": "array", "items": {"type": "string"}},
                    "integrations":      {"type": "array", "items": {"type": "string"}},
                    "integration_roles": {"type": "object", "additionalProperties": {"type": "string"}},
                    "starters":          {"type": "array", "items": {"type": "string"}},
                    "key_challenges":    {"type": "array", "items": {"type": "string"}},
                    "output_dir":        {"type": "string"},
                },
                "required": ["name", "description", "industry"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        try:
            runtime = _get_runtime()
        except Exception as exc:
            return json.dumps({
                "status": "error",
                "message": (
                    f"Failed to fetch full factory from {FULL_FACTORY_URL}: "
                    f"{type(exc).__name__}: {exc}"
                ),
            })
        return runtime.perform(**kwargs)
