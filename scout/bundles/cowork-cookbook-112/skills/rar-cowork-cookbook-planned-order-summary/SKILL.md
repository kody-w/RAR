---
name: "rar-cowork-cookbook-planned-order-summary"
description: "Summarizes planned production orders by resource for the next four weeks, including load vs capacity."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/planned_order_summary", "rar_sha256": "4e424c94407e95646923ad2885b11ceb0e5dc0b85d1086359ef7ee0259fd9b91", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `planned_order_summary_agent.py` and embedded as the fenced Python below (sha256 4e424c94407e9564…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `planned_order_summary_agent.py` first:

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
    "version": '2.0.1',
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
