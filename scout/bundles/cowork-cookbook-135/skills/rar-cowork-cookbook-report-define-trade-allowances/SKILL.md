---
name: "rar-cowork-cookbook-report-define-trade-allowances"
description: "Builds a structured summary report of define trade allowances activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_trade_allowances", "rar_sha256": "62be54f712e2ddb2f3f09ec2942a05095a7709204f40dbac431b0f7a55f1921c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_define_trade_allowances_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-define-trade-allowances:cc9ca376eef5b1af5fd5bcc90fc9aa07a3f33c464ea972add635425728875389", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_define_trade_allowances`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_define_trade_allowances_agent.py` is
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

Define trade allowances Summary Report — Builds a structured summary report of define trade allowances activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-trade-allowances
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_trade_allowances_agent.py` and embedded as the fenced Python below (sha256 62be54f712e2ddb2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_trade_allowances_agent.py` first:

```bash
python3 report_define_trade_allowances_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_trade_allowances_agent.py   # or on stdin
python3 report_define_trade_allowances_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define trade allowances Summary Report — Builds a structured summary report of define trade allowances activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-trade-allowances
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_trade_allowances',
    "version": '2.0.0',
    "display_name": 'Define trade allowances Summary Report',
    "description": 'Builds a structured summary report of define trade allowances activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-define-trade-allowances',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-trade-allowances',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5aeae58a97dca940',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/define-trade-allowances'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/report-define-trade-allowances', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.286, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportDefineTradeAllowances(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineTradeAllowances'
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
    print(ReportDefineTradeAllowances().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
