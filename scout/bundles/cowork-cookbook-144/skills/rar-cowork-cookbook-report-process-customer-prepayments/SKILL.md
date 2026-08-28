---
name: "rar-cowork-cookbook-report-process-customer-prepayments"
description: "Builds a structured summary report of process customer prepayments activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_process_customer_prepayments", "rar_sha256": "b7216a34d88e841fd8335b2802eca58a5405a11544ef70c60ea3c496f568b95a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_process_customer_prepayments`. The original RAPP
agent is preserved byte-for-byte in `report_process_customer_prepayments_agent.py` and in the RCI capsule.

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

Process customer prepayments Summary Report — Builds a structured summary report of process customer prepayments activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-process-customer-prepayments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_process_customer_prepayments_agent.py` and embedded as the fenced Python below (sha256 b7216a34d88e841f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_process_customer_prepayments_agent.py` first:

```bash
python3 report_process_customer_prepayments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_process_customer_prepayments_agent.py   # or on stdin
python3 report_process_customer_prepayments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process customer prepayments Summary Report — Builds a structured summary report of process customer prepayments activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-process-customer-prepayments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_process_customer_prepayments',
    "version": '2.0.1',
    "display_name": 'Process customer prepayments Summary Report',
    "description": 'Builds a structured summary report of process customer prepayments activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-process-customer-prepayments',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-process-customer-prepayments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2dc603b80437abe4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/process-customer-prepayments'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/report-process-customer-prepayments', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ReportProcessCustomerPrepayments(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportProcessCustomerPrepayments'
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
    print(ReportProcessCustomerPrepayments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
