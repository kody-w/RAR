---
name: "rar-cat-agent-skills-route-map-visualizer"
description: "Visualize routes and locations on a map. Accepts pre-ordered stops with coordinates from upstream connectors (Azure Maps, Bing Maps, Dataverse, CRM) plus optional road geometry, leg distances, and durations. Produces PNG, interactive HTML (Leaflet/OSM), GeoJSON, KML, deep links, and QR codes. Fully offline Python engine \u2014 road geometry rendered directly when provided, or OSRM used browser-side as\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/route_map_visualizer", "rar_sha256": "1b02f419c31f24a0b8e108a23abe9a6c0007030ef20d5d10c1833c293035080c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Nazish Qasim", "tags": ["maps", "routing", "visualization", "openstreetmap", "python", "leaflet", "geojson", "kml"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `route_map_visualizer_agent.py` and embedded as the fenced Python below (sha256 1b02f419c31f24a0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `route_map_visualizer_agent.py` first:

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
