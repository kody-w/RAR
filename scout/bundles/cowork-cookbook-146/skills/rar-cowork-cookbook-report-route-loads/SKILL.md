---
name: "rar-cowork-cookbook-report-route-loads"
description: "Builds a structured summary report of route loads activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_route_loads", "rar_sha256": "fd13f9b62fc549c4f63fc3fe995b2e2cac74d5fcae66edb10ef16ad169584a2c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_route_loads`. The original RAPP
agent is preserved byte-for-byte in `report_route_loads_agent.py` and in the RCI capsule.

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

Route loads Summary Report — Builds a structured summary report of route loads activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-route-loads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
      "type": "string"
    },
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_route_loads_agent.py` and embedded as the fenced Python below (sha256 fd13f9b62fc549c4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_route_loads_agent.py` first:

```bash
python3 report_route_loads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_route_loads_agent.py   # or on stdin
python3 report_route_loads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Route loads Summary Report — Builds a structured summary report of route loads activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-route-loads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_route_loads',
    "version": '2.0.1',
    "display_name": 'Route loads Summary Report',
    "description": 'Builds a structured summary report of route loads activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'report-route-loads',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-route-loads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dd14cf61ee848cbf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/route-loads'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/report-route-loads', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.333, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportRouteLoads(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportRouteLoads'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(ReportRouteLoads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
