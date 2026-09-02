---
name: "rar-cat-agent-skills-route-map-visualizer"
description: "Visualize routes and locations on a map. Accepts pre-ordered stops with coordinates from upstream connectors (Azure Maps, Bing Maps, Dataverse, CRM) plus optional road geometry, leg distances, and durations. Produces PNG, interactive HTML (Leaflet/OSM), GeoJSON, KML, deep links, and QR codes. Fully offline Python engine \u2014 road geometry rendered directly when provided, or OSRM used browser-side as\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/route_map_visualizer", "rar_sha256": "5c0cb3810b9ec755c91cad5a437f1fc98cd9de481f8e25c90d58dc0574b032dd", "source_kind": "rar-agent", "source_commit": "409a3c18c6511b9cbf68a9f6716c5be9715b10c4", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "route_map_visualizer_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/route-map-visualizer:25260c83e0b6bcbf7622aafc4ca0838d2e26d32e399504543f5c01a4405f11ec", "kind": "skill"}, "version": "2.0.0", "author": "Nazish Qasim", "tags": ["maps", "routing", "visualization", "openstreetmap", "python", "leaflet", "geojson", "kml"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/route_map_visualizer`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `route_map_visualizer_agent.py` is
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
