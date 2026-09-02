---
name: "rar-cowork-cookbook-report-process-customer-rebates"
description: "Builds a structured summary report of process customer rebates activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_process_customer_rebates", "rar_sha256": "e239c3978bf582acd0d20453774b469b2b9967968087513fffdc923904ef5438", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_process_customer_rebates_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-process-customer-rebates:ad07ac29405b7bf5449024643eba55365d1a2074ca128a70d3368e19bc94064d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_process_customer_rebates`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_process_customer_rebates_agent.py` is
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
