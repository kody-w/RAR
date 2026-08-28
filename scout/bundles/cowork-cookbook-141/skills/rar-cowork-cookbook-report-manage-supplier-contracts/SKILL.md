---
name: "rar-cowork-cookbook-report-manage-supplier-contracts"
description: "Builds a structured summary report of manage supplier contracts activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_supplier_contracts", "rar_sha256": "b4a5e89cbcc4862cc062115e2da82622164317cf1ed350aee1e8d336015aeaa2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_supplier_contracts_agent.py` and embedded as the fenced Python below (sha256 b4a5e89cbcc4862c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_supplier_contracts_agent.py` first:

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
    "version": '2.0.0',
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
