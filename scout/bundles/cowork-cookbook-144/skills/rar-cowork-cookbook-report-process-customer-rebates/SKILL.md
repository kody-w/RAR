---
name: "rar-cowork-cookbook-report-process-customer-rebates"
description: "Builds a structured summary report of process customer rebates activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_process_customer_rebates", "rar_sha256": "e239c3978bf582acd0d20453774b469b2b9967968087513fffdc923904ef5438", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_process_customer_rebates`. The original RAPP
agent is preserved byte-for-byte in `report_process_customer_rebates_agent.py` and in the RCI capsule.

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

Process customer rebates Summary Report — Builds a structured summary report of process customer rebates activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-process-customer-rebates
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_process_customer_rebates_agent.py` and embedded as the fenced Python below (sha256 e239c3978bf582ac…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_process_customer_rebates_agent.py` first:

```bash
python3 report_process_customer_rebates_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_process_customer_rebates_agent.py   # or on stdin
python3 report_process_customer_rebates_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process customer rebates Summary Report — Builds a structured summary report of process customer rebates activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-process-customer-rebates
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_process_customer_rebates',
    "version": '2.0.0',
    "display_name": 'Process customer rebates Summary Report',
    "description": 'Builds a structured summary report of process customer rebates activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-process-customer-rebates',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-process-customer-rebates',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ac3370e129780c93',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/process-customer-rebates'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/report-process-customer-rebates', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportProcessCustomerRebates(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportProcessCustomerRebates'
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
    print(ReportProcessCustomerRebates().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
