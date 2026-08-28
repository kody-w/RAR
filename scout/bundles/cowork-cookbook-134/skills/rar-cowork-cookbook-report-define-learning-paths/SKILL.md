---
name: "rar-cowork-cookbook-report-define-learning-paths"
description: "Builds a structured summary report of define learning paths activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_learning_paths", "rar_sha256": "7d7dabf3d7096e5d902197610a1c65d5a46cd5a7782bb61ace6723928961c934", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_learning_paths_agent.py` and embedded as the fenced Python below (sha256 7d7dabf3d7096e5d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_learning_paths_agent.py` first:

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
    "version": '2.0.1',
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
