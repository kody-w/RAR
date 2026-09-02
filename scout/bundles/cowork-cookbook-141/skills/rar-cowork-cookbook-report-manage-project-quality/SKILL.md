---
name: "rar-cowork-cookbook-report-manage-project-quality"
description: "Builds a structured summary report of manage project quality activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_project_quality", "rar_sha256": "dea936c74280c19918d044bf8e2c1d530b8fc6f7e0e61e7e8ccbb25763e967d2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_manage_project_quality_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-manage-project-quality:fc1f77868ece3a590e82315e59884d4e53755685fd9cb0dc57b9593577211e9a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_manage_project_quality`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_manage_project_quality_agent.py` is
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
