---
name: "rar-cowork-cookbook-report-route-loads"
description: "Builds a structured summary report of route loads activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_route_loads", "rar_sha256": "1a6f99532348de5cfd827f1ade3f1b0e4f9942f46af60714da0e5ba498b49312", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_route_loads_agent.py` and embedded as the fenced Python below (sha256 1a6f99532348de5c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_route_loads_agent.py` first:

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
    "version": '2.0.0',
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
