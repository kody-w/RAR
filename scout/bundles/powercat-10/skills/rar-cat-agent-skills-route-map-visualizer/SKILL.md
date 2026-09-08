---
name: "rar-cat-agent-skills-route-map-visualizer"
description: "Visualize routes and locations on a map. Accepts pre-ordered stops with coordinates from upstream connectors (Azure Maps, Bing Maps, Dataverse, CRM) plus optional road geometry, leg distances, and durations. Produces PNG, interactive HTML (Leaflet/OSM), GeoJSON, KML, deep links, and QR codes. Fully offline Python engine \u2014 road geometry rendered directly when provided, or OSRM used browser-side as\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/route_map_visualizer", "rar_sha256": "1b02f419c31f24a0b8e108a23abe9a6c0007030ef20d5d10c1833c293035080c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Nazish Qasim", "tags": ["maps", "routing", "visualization", "openstreetmap", "python", "leaflet", "geojson", "kml"]}
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
