---
name: "rar-cowork-cookbook-report-define-project-stakeholders"
description: "Builds a structured summary report of define project stakeholders activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_project_stakeholders", "rar_sha256": "a25880a486953ad3c35031a1050abbe5e8c28688c997375e6cd8370b56d570d6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_project_stakeholders`. The original RAPP
agent is preserved byte-for-byte in `report_define_project_stakeholders_agent.py` and in the RCI capsule.

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

Define project stakeholders Summary Report — Builds a structured summary report of define project stakeholders activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-project-stakeholders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_project_stakeholders_agent.py` and embedded as the fenced Python below (sha256 a25880a486953ad3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_project_stakeholders_agent.py` first:

```bash
python3 report_define_project_stakeholders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_project_stakeholders_agent.py   # or on stdin
python3 report_define_project_stakeholders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define project stakeholders Summary Report — Builds a structured summary report of define project stakeholders activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-project-stakeholders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_project_stakeholders',
    "version": '2.0.0',
    "display_name": 'Define project stakeholders Summary Report',
    "description": 'Builds a structured summary report of define project stakeholders activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-define-project-stakeholders',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-project-stakeholders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a6e0e31b02135889',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/define-project-stakeholders'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-define-project-stakeholders', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportDefineProjectStakeholders(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineProjectStakeholders'
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
    print(ReportDefineProjectStakeholders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
