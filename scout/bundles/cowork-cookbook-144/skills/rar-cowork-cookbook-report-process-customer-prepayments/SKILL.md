---
name: "rar-cowork-cookbook-report-process-customer-prepayments"
description: "Builds a structured summary report of process customer prepayments activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_process_customer_prepayments", "rar_sha256": "6ac8c2551879841a67efdead33c8e4bcdf43ce3b4073a6afbeaa005289309e81", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_process_customer_prepayments_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-process-customer-prepayments:94f074bbe3fa2067c9f0a3853576250318577b217970dc042422ca24d6500030", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_process_customer_prepayments`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_process_customer_prepayments_agent.py` is
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
