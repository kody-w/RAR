---
name: "rar-cowork-cookbook-report-manage-supplier-contracts"
description: "Builds a structured summary report of manage supplier contracts activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_supplier_contracts", "rar_sha256": "b4a5e89cbcc4862cc062115e2da82622164317cf1ed350aee1e8d336015aeaa2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_manage_supplier_contracts_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-manage-supplier-contracts:ffec7f90274bc7ac6b92a7864d547ac080290122963962af0f8d4985a76f64f2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_manage_supplier_contracts`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_manage_supplier_contracts_agent.py` is
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
