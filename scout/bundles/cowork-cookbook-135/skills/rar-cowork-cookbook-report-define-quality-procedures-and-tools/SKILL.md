---
name: "rar-cowork-cookbook-report-define-quality-procedures-and-tools"
description: "Builds a structured summary report of define quality procedures and tools activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_quality_procedures_and_tools", "rar_sha256": "aadde320ea463f8aef218a3352b80c4e47ef7b409d4f22d8ac7c409d63f671ef", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_quality_procedures_and_tools`. The original RAPP
agent is preserved byte-for-byte in `report_define_quality_procedures_and_tools_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_quality_procedures_and_tools_agent.py` and embedded as the fenced Python below (sha256 aadde320ea463f8a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_quality_procedures_and_tools_agent.py` first:

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
    "version": '2.0.1',
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
