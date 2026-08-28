---
name: "rar-cowork-cookbook-report-process-customer-prepayments"
description: "Builds a structured summary report of process customer prepayments activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_process_customer_prepayments", "rar_sha256": "6ac8c2551879841a67efdead33c8e4bcdf43ce3b4073a6afbeaa005289309e81", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_process_customer_prepayments_agent.py` and embedded as the fenced Python below (sha256 6ac8c2551879841a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_process_customer_prepayments_agent.py` first:

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
    "version": '2.0.0',
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
