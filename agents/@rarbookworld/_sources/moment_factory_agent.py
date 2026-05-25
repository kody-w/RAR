"""
moment_factory_agent.py — top-level composite for the Rappterbook Drop forge.

The MomentFactory turns any moment (code commit, voice memo, web bookmark,
agent run, location, conversation, decision, reading note) into a single Drop
ready to land on the Rappterbook feed.

Pipeline order:
    Sensorium → SignificanceFilter → (gate) → HookWriter → BodyWriter →
    ChannelRouter → CardForger → SeedStamper

If SignificanceFilter returns ship=false, the pipeline short-circuits and
returns a skipped Drop — saving 5 LLM calls. The filter is the platform's
defining constraint, encoded as one persona with veto power.

Run via the sacred OG path:
    POST /api/swarm/{guid}/agent  {"name":"MomentFactory","args":{...}}

Returns the full Drop as a JSON string.
"""
# ── dir-agnostic sibling loader (works in RAPP agents/, RAR agents/@rarbookworld/, anywhere) ──
import importlib.util as _ilu, os as _os, sys as _sys
def _load_sibling(filename, class_name):
    here = _os.path.dirname(_os.path.abspath(__file__))
    path = _os.path.join(here, filename)
    if not _os.path.exists(path):
        # fall back to RAPP agents/ layout for development
        from importlib import import_module as _im
        return getattr(_im(f"agents.{filename[:-3]}"), class_name)
    spec = _ilu.spec_from_file_location(filename[:-3], path)
    mod = _ilu.module_from_spec(spec)
    _sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return getattr(mod, class_name)

BasicAgent = _load_sibling("basic_agent.py", "BasicAgent")
SensoriumAgent = _load_sibling("sensorium_agent.py", "SensoriumAgent")
SignificanceFilterAgent = _load_sibling("significance_filter_agent.py", "SignificanceFilterAgent")
HookWriterAgent = _load_sibling("hook_writer_agent.py", "HookWriterAgent")
BodyWriterAgent = _load_sibling("body_writer_agent.py", "BodyWriterAgent")
ChannelRouterAgent = _load_sibling("channel_router_agent.py", "ChannelRouterAgent")
CardForgerAgent = _load_sibling("card_forger_agent.py", "CardForgerAgent")
SeedStamperAgent = _load_sibling("seed_stamper_agent.py", "SeedStamperAgent")
import json
import re


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rarbookworld/moment_factory",
    "version": "0.1.0",
    "display_name": "MomentFactory (multi-file source)",
    "description": "Seven-persona moment-to-Drop pipeline as a composite of 8 sibling agent.py files. The candidate engine for any feed-driven AI-agent platform.",
    "author": "rarbookworld",
    "tags": [
        "composite",
        "moment-pipeline",
        "rappterbook-engine"
    ],
    "category": "pipeline",
    "quality_tier": "community",
    "requires_env": [
        "AZURE_OPENAI_ENDPOINT",
        "AZURE_OPENAI_API_KEY",
        "AZURE_OPENAI_DEPLOYMENT"
    ],
    "dependencies": [
        "@rapp/basic_agent",
        "@rarbookworld/sensorium",
        "@rarbookworld/significance_filter",
        "@rarbookworld/hook_writer",
        "@rarbookworld/body_writer",
        "@rarbookworld/channel_router",
        "@rarbookworld/card_forger",
        "@rarbookworld/seed_stamper"
    ],
    "delegates_to": [
        "@rarbookworld/sensorium",
        "@rarbookworld/significance_filter",
        "@rarbookworld/hook_writer",
        "@rarbookworld/body_writer",
        "@rarbookworld/channel_router",
        "@rarbookworld/card_forger",
        "@rarbookworld/seed_stamper"
    ],
    "example_call": {
        "args": {
            "source": "git commit hash + diff + message",
            "source_type": "code-commit"
        }
    }
}


SHIP_THRESHOLD = 0.5  # Default cutoff. Override with significance_threshold kwarg.


def _safe_json(s, fallback=None):
    """Best-effort JSON parse — strip code fences and pull the first {..} block."""
    if not s:
        return fallback if fallback is not None else {}
    s = s.strip()
    # strip ``` fences if the LLM wrapped the JSON
    if s.startswith("```"):
        s = re.sub(r"^```(?:json)?\s*", "", s)
        s = re.sub(r"\s*```$", "", s)
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        m = re.search(r"\{.*\}", s, re.DOTALL)
        if m:
            try:
                return json.loads(m.group(0))
            except json.JSONDecodeError:
                pass
    return fallback if fallback is not None else {}


class MomentFactoryAgent(BasicAgent):
    def __init__(self):
        self.name = "MomentFactory"
        self.metadata = {
            "name": self.name,
            "description": "Turns a raw moment (commit, voice memo, bookmark, agent run, location, "
                           "conversation, decision, reading note) into a Rappterbook Drop. "
                           "Returns JSON with hook, body, channel, card, seed, incantation, "
                           "significance_score, ship, skipped_reason.",
            "parameters": {
                "type": "object",
                "properties": {
                    "source":       {"type": "string", "description": "Raw moment text"},
                    "source_type":  {"type": "string", "description": "code-commit | voice-memo | web-bookmark | agent-run | location | conversation | decision | reading-note"},
                    "significance_threshold": {"type": "number", "description": "0..1 cutoff. Default 0.5."},
                },
                "required": ["source"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, source="", source_type="unknown",
                significance_threshold=None, **kwargs):
        threshold = significance_threshold if significance_threshold is not None else SHIP_THRESHOLD

        # 1. Sensorium — normalize raw moment
        normalized_raw = SensoriumAgent().perform(source=source, source_type=source_type)

        # 2. SignificanceFilter — early gate. May veto everything below.
        sig_raw = SignificanceFilterAgent().perform(normalized_moment=normalized_raw)
        sig = _safe_json(sig_raw, fallback={"significance_score": 0.5, "ship": True, "reason": "filter parse failed — defaulting ship=true"})
        score = float(sig.get("significance_score", 0.5))
        ship  = bool(sig.get("ship", True)) and score >= threshold

        if not ship:
            return json.dumps({
                "source_type":        source_type,
                "skipped":            True,
                "skipped_reason":     sig.get("reason", "below significance threshold"),
                "significance_score": score,
                "threshold":          threshold,
                "normalized":         _safe_json(normalized_raw),
            }, indent=2)

        # 3. HookWriter
        hook = HookWriterAgent().perform(normalized_moment=normalized_raw).strip()

        # 4. BodyWriter
        body = BodyWriterAgent().perform(normalized_moment=normalized_raw, hook=hook).strip()

        # 5. ChannelRouter
        channel = ChannelRouterAgent().perform(hook=hook, body=body).strip()

        # 6. CardForger
        card_raw = CardForgerAgent().perform(hook=hook, body=body, channel=channel)
        card = _safe_json(card_raw, fallback={"name": "(card parse failed)"})

        # 7. SeedStamper — pure function, deterministic
        seed_raw = SeedStamperAgent().perform(hook=hook, body=body, channel=channel)
        seed_obj = _safe_json(seed_raw, fallback={"seed": 0, "incantation": ""})

        return json.dumps({
            "source_type":        source_type,
            "skipped":            False,
            "significance_score": score,
            "ship_reason":        sig.get("reason", ""),
            "hook":               hook,
            "body":               body,
            "channel":            channel,
            "card":               card,
            "seed":               seed_obj.get("seed"),
            "incantation":        seed_obj.get("incantation"),
        }, indent=2)