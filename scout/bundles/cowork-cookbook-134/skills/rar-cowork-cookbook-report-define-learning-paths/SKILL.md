---
name: "rar-cowork-cookbook-report-define-learning-paths"
description: "Builds a structured summary report of define learning paths activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_learning_paths", "rar_sha256": "bb98f6b1615b2be9dcf8c89ad2e9f12c77c5c7907128dd1dea5b95f169825836", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_learning_paths`. The original RAPP
agent is preserved byte-for-byte in `report_define_learning_paths_agent.py` and in the RCI capsule.

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
