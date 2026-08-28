---
name: "rar-cowork-cookbook-project-margin-health"
description: "Compares project budget to actuals by cost category, flags projects with margin erosion, and drafts emails to the project managers of red projects."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/project_margin_health", "rar_sha256": "d9c739dab5bcc81b1fc9827b2b29a507119ce9b1dfec5b1ca5dd679a126c4abb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `project_margin_health_agent.py` and embedded as the fenced Python below (sha256 d9c739dab5bcc81b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `project_margin_health_agent.py` first:

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
    "version": '2.0.1',
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
