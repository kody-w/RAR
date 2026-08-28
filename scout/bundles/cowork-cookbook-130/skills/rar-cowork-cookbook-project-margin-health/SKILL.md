---
name: "rar-cowork-cookbook-project-margin-health"
description: "Compares project budget to actuals by cost category, flags projects with margin erosion, and drafts emails to the project managers of red projects."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/project_margin_health", "rar_sha256": "cec496cab5bf24f829348c6d5d3bbe968eda6cc0e20ae6da245c2d07efdc9051", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/project_margin_health`. The original RAPP
agent is preserved byte-for-byte in `project_margin_health_agent.py` and in the RCI capsule.

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

Project Margin Health Report — Compares project budget to actuals by cost category, flags projects with margin erosion, and drafts emails to the project managers of red projects.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/project-margin-health
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `project_margin_health_agent.py` and embedded as the fenced Python below (sha256 cec496cab5bf24f8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `project_margin_health_agent.py` first:

```bash
python3 project_margin_health_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 project_margin_health_agent.py   # or on stdin
python3 project_margin_health_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Project Margin Health Report — Compares project budget to actuals by cost category, flags projects with margin erosion, and drafts emails to the project managers of red projects.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/project-margin-health
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/project_margin_health',
    "version": '2.0.0',
    "display_name": 'Project Margin Health Report',
    "description": 'Compares project budget to actuals by cost category, flags projects with margin erosion, and drafts emails to the project managers of red projects.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'project-margin-health',
        "upstream_url": 'https://coworkcookbook.com/recipes/project-margin-health',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e8787a0e5d49d105',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/analyze-project-performance'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/project-margin-health', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Email'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ProjectMarginHealth(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ProjectMarginHealth'
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
    print(ProjectMarginHealth().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
