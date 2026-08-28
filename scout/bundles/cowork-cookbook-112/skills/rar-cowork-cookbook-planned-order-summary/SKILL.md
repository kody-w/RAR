---
name: "rar-cowork-cookbook-planned-order-summary"
description: "Summarizes planned production orders by resource for the next four weeks, including load vs capacity."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/planned_order_summary", "rar_sha256": "a96f9bd059fa1a5b1ec9e6f88a8049daf82de5b4d3a63df7594a94542a1244ac", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/planned_order_summary`. The original RAPP
agent is preserved byte-for-byte in `planned_order_summary_agent.py` and in the RCI capsule.

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

Planned Order Summary by Resource — Summarizes planned production orders by resource for the next four weeks, including load vs capacity.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/planned-order-summary
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `planned_order_summary_agent.py` and embedded as the fenced Python below (sha256 a96f9bd059fa1a5b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `planned_order_summary_agent.py` first:

```bash
python3 planned_order_summary_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 planned_order_summary_agent.py   # or on stdin
python3 planned_order_summary_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Planned Order Summary by Resource — Summarizes planned production orders by resource for the next four weeks, including load vs capacity.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/planned-order-summary
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/planned_order_summary',
    "version": '2.0.0',
    "display_name": 'Planned Order Summary by Resource',
    "description": 'Summarizes planned production orders by resource for the next four weeks, including load vs capacity.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'planned-order-summary',
        "upstream_url": 'https://coworkcookbook.com/recipes/planned-order-summary',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0eb3dd922e7ca635',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/planned-order-summary', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class PlannedOrderSummary(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PlannedOrderSummary'
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
    print(PlannedOrderSummary().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
