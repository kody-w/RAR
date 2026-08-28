---
name: "rar-cowork-cookbook-report-define-trade-allowances"
description: "Builds a structured summary report of define trade allowances activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_trade_allowances", "rar_sha256": "d059a0c0cc7d7ea330b6c1315e681fe8e862b36cfc86a790a2ba4d0f8362a333", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_trade_allowances_agent.py` and embedded as the fenced Python below (sha256 d059a0c0cc7d7ea3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_trade_allowances_agent.py` first:

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
    "version": '2.0.1',
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
