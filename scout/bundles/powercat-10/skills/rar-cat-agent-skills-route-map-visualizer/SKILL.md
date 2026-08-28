---
name: "rar-cat-agent-skills-route-map-visualizer"
description: "Visualize routes and locations on a map. Accepts pre-ordered stops with coordinates from upstream connectors (Azure Maps, Bing Maps, Dataverse, CRM) plus optional road geometry, leg distances, and durations. Produces PNG, interactive HTML (Leaflet/OSM), GeoJSON, KML, deep links, and QR codes. Fully offline Python engine \u2014 road geometry rendered directly when provided, or OSRM used browser-side as\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/route_map_visualizer", "rar_sha256": "5c0cb3810b9ec755c91cad5a437f1fc98cd9de481f8e25c90d58dc0574b032dd", "source_kind": "rar-agent", "source_commit": "409a3c18c6511b9cbf68a9f6716c5be9715b10c4", "version": "2.0.0", "author": "Nazish Qasim", "tags": ["maps", "routing", "visualization", "openstreetmap", "python", "leaflet", "geojson", "kml"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `route_map_visualizer_agent.py` and embedded as the fenced Python below (sha256 5c0cb3810b9ec755…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `route_map_visualizer_agent.py` first:

```bash
python3 route_map_visualizer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 route_map_visualizer_agent.py   # or on stdin
python3 route_map_visualizer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
    "version": '2.0.0',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
