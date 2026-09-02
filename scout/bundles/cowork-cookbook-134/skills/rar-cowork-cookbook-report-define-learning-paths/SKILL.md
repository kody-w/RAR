---
name: "rar-cowork-cookbook-report-define-learning-paths"
description: "Builds a structured summary report of define learning paths activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_learning_paths", "rar_sha256": "bb98f6b1615b2be9dcf8c89ad2e9f12c77c5c7907128dd1dea5b95f169825836", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_define_learning_paths_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-define-learning-paths:56735d7ba37ae28036c227556ca3c0ac9bae0587739694ca1092be6a4b62b47e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_define_learning_paths`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_define_learning_paths_agent.py` is
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

Define learning paths Summary Report — Builds a structured summary report of define learning paths activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-learning-paths
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_learning_paths_agent.py` and embedded as the fenced Python below (sha256 bb98f6b1615b2be9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_learning_paths_agent.py` first:

```bash
python3 report_define_learning_paths_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_learning_paths_agent.py   # or on stdin
python3 report_define_learning_paths_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define learning paths Summary Report — Builds a structured summary report of define learning paths activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-learning-paths
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_learning_paths',
    "version": '2.0.0',
    "display_name": 'Define learning paths Summary Report',
    "description": 'Builds a structured summary report of define learning paths activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-define-learning-paths',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-learning-paths',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '08c05872a00354ef',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/define-learning-paths'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-define-learning-paths', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportDefineLearningPaths(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineLearningPaths'
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
    print(ReportDefineLearningPaths().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
