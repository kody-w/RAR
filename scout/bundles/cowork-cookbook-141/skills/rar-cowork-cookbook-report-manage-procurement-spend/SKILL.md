---
name: "rar-cowork-cookbook-report-manage-procurement-spend"
description: "Builds a structured summary report of manage procurement spend activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_procurement_spend", "rar_sha256": "75279a07273c869ab4d38cc9a30a3010b6941d5f3d94e91c546229d0af6de3e4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_procurement_spend_agent.py` and embedded as the fenced Python below (sha256 75279a07273c869a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_procurement_spend_agent.py` first:

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
    "version": '2.0.0',
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
