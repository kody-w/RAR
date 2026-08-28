---
name: "rar-cowork-cookbook-report-manage-project-quality"
description: "Builds a structured summary report of manage project quality activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_project_quality", "rar_sha256": "e505b227d6a41d64951aae4e524a671eace9008b52133092eb02d80bbe9dd444", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_project_quality`. The original RAPP
agent is preserved byte-for-byte in `report_manage_project_quality_agent.py` and in the RCI capsule.

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

Manage project quality Summary Report — Builds a structured summary report of manage project quality activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-project-quality
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_project_quality_agent.py` and embedded as the fenced Python below (sha256 e505b227d6a41d64…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_project_quality_agent.py` first:

```bash
python3 report_manage_project_quality_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_project_quality_agent.py   # or on stdin
python3 report_manage_project_quality_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage project quality Summary Report — Builds a structured summary report of manage project quality activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-project-quality
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_project_quality',
    "version": '2.0.1',
    "display_name": 'Manage project quality Summary Report',
    "description": 'Builds a structured summary report of manage project quality activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-manage-project-quality',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-project-quality',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1850fa7c01635f05',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/analyze-project-performance/manage-project-quality'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-manage-project-quality', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportManageProjectQuality(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageProjectQuality'
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
    print(ReportManageProjectQuality().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
