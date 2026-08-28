---
name: "rar-cowork-cookbook-report-define-trade-allowances"
description: "Builds a structured summary report of define trade allowances activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_trade_allowances", "rar_sha256": "62be54f712e2ddb2f3f09ec2942a05095a7709204f40dbac431b0f7a55f1921c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_trade_allowances`. The original RAPP
agent is preserved byte-for-byte in `report_define_trade_allowances_agent.py` and in the RCI capsule.

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
