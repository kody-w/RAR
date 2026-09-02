---
name: "rar-cowork-cookbook-report-define-quality-procedures-and-tools"
description: "Builds a structured summary report of define quality procedures and tools activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_quality_procedures_and_tools", "rar_sha256": "913966a38a3ae27b7ab969fb0afbca23fec01c736ae3fd9e1205be818173ed22", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_define_quality_procedures_and_tools_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-define-quality-procedures-and-tools:c20be88026ddd3ece80a741fa99d02c14c68cce1f04473af3d45cc2827bf9d24", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_define_quality_procedures_and_tools`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_define_quality_procedures_and_tools_agent.py` is
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

Define quality procedures and tools Summary Report — Builds a structured summary report of define quality procedures and tools activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-quality-procedures-and-tools
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_quality_procedures_and_tools_agent.py` and embedded as the fenced Python below (sha256 913966a38a3ae27b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_quality_procedures_and_tools_agent.py` first:

```bash
python3 report_define_quality_procedures_and_tools_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_quality_procedures_and_tools_agent.py   # or on stdin
python3 report_define_quality_procedures_and_tools_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define quality procedures and tools Summary Report — Builds a structured summary report of define quality procedures and tools activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-quality-procedures-and-tools
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_quality_procedures_and_tools',
    "version": '2.0.0',
    "display_name": 'Define quality procedures and tools Summary Report',
    "description": 'Builds a structured summary report of define quality procedures and tools activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-define-quality-procedures-and-tools',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-quality-procedures-and-tools',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fe25930fdd707ef5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/define-quality-procedures-and-tools'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/report-define-quality-procedures-and-tools', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportDefineQualityProceduresAndTools(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineQualityProceduresAndTools'
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
    print(ReportDefineQualityProceduresAndTools().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
