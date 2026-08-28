---
name: "rar-cowork-cookbook-report-manage-supplier-contracts"
description: "Builds a structured summary report of manage supplier contracts activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_supplier_contracts", "rar_sha256": "e7c0f9076050279469cf5c00a7442c1e800c43184d71770e0f181664e786b8c8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_supplier_contracts`. The original RAPP
agent is preserved byte-for-byte in `report_manage_supplier_contracts_agent.py` and in the RCI capsule.

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

Manage supplier contracts Summary Report — Builds a structured summary report of manage supplier contracts activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-supplier-contracts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_supplier_contracts_agent.py` and embedded as the fenced Python below (sha256 e7c0f90760502794…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_supplier_contracts_agent.py` first:

```bash
python3 report_manage_supplier_contracts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_supplier_contracts_agent.py   # or on stdin
python3 report_manage_supplier_contracts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage supplier contracts Summary Report — Builds a structured summary report of manage supplier contracts activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-supplier-contracts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_supplier_contracts',
    "version": '2.0.1',
    "display_name": 'Manage supplier contracts Summary Report',
    "description": 'Builds a structured summary report of manage supplier contracts activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-manage-supplier-contracts',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-supplier-contracts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fff74c2f41dff7a2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/manage-supplier-contracts'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/report-manage-supplier-contracts', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportManageSupplierContracts(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageSupplierContracts'
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
    print(ReportManageSupplierContracts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
