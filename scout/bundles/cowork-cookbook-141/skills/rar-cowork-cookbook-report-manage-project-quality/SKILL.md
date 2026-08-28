---
name: "rar-cowork-cookbook-report-manage-project-quality"
description: "Builds a structured summary report of manage project quality activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_project_quality", "rar_sha256": "dea936c74280c19918d044bf8e2c1d530b8fc6f7e0e61e7e8ccbb25763e967d2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_project_quality_agent.py` and embedded as the fenced Python below (sha256 dea936c74280c199…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_project_quality_agent.py` first:

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
    "version": '2.0.0',
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
