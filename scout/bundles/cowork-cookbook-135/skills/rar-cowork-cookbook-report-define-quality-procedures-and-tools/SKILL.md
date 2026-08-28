---
name: "rar-cowork-cookbook-report-define-quality-procedures-and-tools"
description: "Builds a structured summary report of define quality procedures and tools activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_quality_procedures_and_tools", "rar_sha256": "913966a38a3ae27b7ab969fb0afbca23fec01c736ae3fd9e1205be818173ed22", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
