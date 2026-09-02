---
name: "rar-cowork-cookbook-report-pay-taxes"
description: "Builds a structured summary report of pay taxes activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_pay_taxes", "rar_sha256": "a558ecc9fb748bbd99d67f066f291d1ea0dba1eb1624da65f8ac37009d7b5466", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_pay_taxes_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-pay-taxes:911ba6594425887edda671a6013978d2f771f959adf1441d6181cfb7591b169e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_pay_taxes`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_pay_taxes_agent.py` is
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

Pay taxes Summary Report — Builds a structured summary report of pay taxes activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-pay-taxes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_pay_taxes_agent.py` and embedded as the fenced Python below (sha256 a558ecc9fb748bbd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_pay_taxes_agent.py` first:

```bash
python3 report_pay_taxes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_pay_taxes_agent.py   # or on stdin
python3 report_pay_taxes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pay taxes Summary Report — Builds a structured summary report of pay taxes activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-pay-taxes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_pay_taxes',
    "version": '2.0.0',
    "display_name": 'Pay taxes Summary Report',
    "description": 'Builds a structured summary report of pay taxes activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-pay-taxes',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-pay-taxes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '36c45a0e8165da3d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/pay-taxes'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/report-pay-taxes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ReportPayTaxes(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportPayTaxes'
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
    print(ReportPayTaxes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
