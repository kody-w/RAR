---
name: "rar-cowork-cookbook-report-manage-procurement-spend"
description: "Builds a structured summary report of manage procurement spend activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_procurement_spend", "rar_sha256": "1a6d5552b79184e2c9c3c7661bf9d6a782a0ca84e93ffeff7e29d2eff222c7fb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_procurement_spend`. The original RAPP
agent is preserved byte-for-byte in `report_manage_procurement_spend_agent.py` and in the RCI capsule.

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

Manage procurement spend Summary Report — Builds a structured summary report of manage procurement spend activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-procurement-spend
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_procurement_spend_agent.py` and embedded as the fenced Python below (sha256 1a6d5552b79184e2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_procurement_spend_agent.py` first:

```bash
python3 report_manage_procurement_spend_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_procurement_spend_agent.py   # or on stdin
python3 report_manage_procurement_spend_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage procurement spend Summary Report — Builds a structured summary report of manage procurement spend activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-procurement-spend
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_procurement_spend',
    "version": '2.0.1',
    "display_name": 'Manage procurement spend Summary Report',
    "description": 'Builds a structured summary report of manage procurement spend activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-manage-procurement-spend',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-procurement-spend',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '27098e13b13153e1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/manage-procurement-spend'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/report-manage-procurement-spend', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportManageProcurementSpend(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageProcurementSpend'
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
    print(ReportManageProcurementSpend().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
