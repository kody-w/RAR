---
name: "rar-cowork-cookbook-report-pay-taxes"
description: "Builds a structured summary report of pay taxes activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_pay_taxes", "rar_sha256": "ba4485fd5f255529d038853e151158f1b37214f599aebcc4b645210289aae64d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_pay_taxes`. The original RAPP
agent is preserved byte-for-byte in `report_pay_taxes_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_pay_taxes_agent.py` and embedded as the fenced Python below (sha256 ba4485fd5f255529…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_pay_taxes_agent.py` first:

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
    "version": '2.0.1',
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
