---
name: "rar-cat-agent-skills-route-map-visualizer"
description: "Visualize routes and locations on a map. Accepts pre-ordered stops with coordinates from upstream connectors (Azure Maps, Bing Maps, Dataverse, CRM) plus optional road geometry, leg distances, and durations. Produces PNG, interactive HTML (Leaflet/OSM), GeoJSON, KML, deep links, and QR codes. Fully offline Python engine \u2014 road geometry rendered directly when provided, or OSRM used browser-side as\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/route_map_visualizer", "rar_sha256": "2f00ce5f28aaef338a2dcf9c25b34c562518cbee5d91d999961a8254e22a5115", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Nazish Qasim", "tags": ["maps", "routing", "visualization", "openstreetmap", "python", "leaflet", "geojson", "kml"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/route_map_visualizer`. The original RAPP
agent is preserved byte-for-byte in `route_map_visualizer_agent.py` and in the RCI capsule.

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

Route Map Visualizer — Visualize routes and locations on a map. Accepts pre-ordered stops with coordinates from upstream connectors (Azure Maps, Bing Maps, Dataverse, CRM) plus optional road geometry, leg distances, and durations. Produces PNG, interactive HTML (Leaflet/OSM), GeoJSON, KML, deep links, and QR codes. Fully offline Python engine — road geometry rendered directly when provided, or OSRM used browser-side as…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#route-map-visualizer
  Upstream author: Nazish Qasim
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "What to apply this capability to.",
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `route_map_visualizer_agent.py` and embedded as the fenced Python below (sha256 2f00ce5f28aaef33…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `route_map_visualizer_agent.py` first:

```bash
python3 route_map_visualizer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 route_map_visualizer_agent.py   # or on stdin
python3 route_map_visualizer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/route_map_visualizer_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/route_map_visualizer_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/route_map_visualizer/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Route Map Visualizer — Visualize routes and locations on a map. Accepts pre-ordered stops with coordinates from upstream connectors (Azure Maps, Bing Maps, Dataverse, CRM) plus optional road geometry, leg distances, and durations. Produces PNG, interactive HTML (Leaflet/OSM), GeoJSON, KML, deep links, and QR codes. Fully offline Python engine — road geometry rendered directly when provided, or OSRM used browser-side as…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#route-map-visualizer
  Upstream author: Nazish Qasim
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/route_map_visualizer',
    "version": '3.0.2',
    "display_name": 'Route Map Visualizer',
    "description": 'Visualize routes and locations on a map. Accepts pre-ordered stops with coordinates from upstream connectors (Azure Maps, Bing Maps, Dataverse, CRM) plus optional road geometry, leg distances, and durations. Produces PNG, interactive HTML (Leaflet/OSM), GeoJSON, KML, deep links, and QR codes. Fully offline Python engine — road geometry rendered directly when provided, or OSRM used browser-side as…',
    "author": 'Nazish Qasim',
    "tags": ['maps', 'routing', 'visualization', 'openstreetmap', 'python', 'leaflet', 'geojson', 'kml'],
    "category": 'devtools',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'route-map-visualizer',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#route-map-visualizer',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'f6e86f5cfd0f8994',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'general', 'checks': ['The outcome is independently verifiable.', 'Assumptions are written down.', 'The result was checked against the original goal.'], 'confidence': 0.0, 'deliverable': 'A completed pass with the goal, the method, the result, and the assumptions it rests on.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'What to apply this capability to.'}, 'refined_by': 'rules', 'signals': [], 'steps': ['State the goal as an outcome someone else could verify without you.', 'List what you have and what is missing before starting.', 'Do the smallest version end to end, so unknowns surface while they are cheap.', 'Check the result against the goal as stated, not against what turned out to be convenient.', 'Record what would have to be true for this to be wrong.'], 'subject_label': 'task', 'verb': 'Run'}


class RouteMapVisualizer(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'RouteMapVisualizer'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to apply this capability to.', 'type': 'string'}},
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\u0022...\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

        if op == "describe":
            return "\n".join(self._provenance())

        if op == "checklist":
            return "\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(RouteMapVisualizer().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
