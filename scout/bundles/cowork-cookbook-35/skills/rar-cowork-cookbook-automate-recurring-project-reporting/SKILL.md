---
name: "rar-cowork-cookbook-automate-recurring-project-reporting"
description: "Replace the manual \"pull the board, write the update, send it out\" Monday-morning cycle with a status update that writes and sends itself."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/automate_recurring_project_reporting", "rar_sha256": "8ee6baf76060e5b0b1a34acc7a0d672246f08d5acef6c6391a02455bea1ee05e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "work_management", "advanced", "integration", "monday_com"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/automate_recurring_project_reporting`. The original RAPP
agent is preserved byte-for-byte in `automate_recurring_project_reporting_agent.py` and in the RCI capsule.

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

Automate recurring project reporting — Replace the manual "pull the board, write the update, send it out" Monday-morning cycle with a status update that writes and sends itself.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/automate-recurring-project-reporting
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `automate_recurring_project_reporting_agent.py` and embedded as the fenced Python below (sha256 8ee6baf76060e5b0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `automate_recurring_project_reporting_agent.py` first:

```bash
python3 automate_recurring_project_reporting_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 automate_recurring_project_reporting_agent.py   # or on stdin
python3 automate_recurring_project_reporting_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Automate recurring project reporting — Replace the manual "pull the board, write the update, send it out" Monday-morning cycle with a status update that writes and sends itself.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/automate-recurring-project-reporting
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/automate_recurring_project_reporting',
    "version": '2.0.0',
    "display_name": 'Automate recurring project reporting',
    "description": 'Replace the manual "pull the board, write the update, send it out" Monday-morning cycle with a status update that writes and sends itself.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'work_management', 'advanced', 'integration', 'monday_com'],
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
        "upstream_slug": 'automate-recurring-project-reporting',
        "upstream_url": 'https://coworkcookbook.com/recipes/automate-recurring-project-reporting',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '604027779498dc7b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'monday-com', 'process_roots': ['work-management'], 'process_tags': ['work-management/coordinate-team-work/automate-recurring-reporting'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'work-management/automate-recurring-project-reporting', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Scheduling', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.375, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report', 'word:write'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class AutomateRecurringProjectReporting(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AutomateRecurringProjectReporting'
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
    print(AutomateRecurringProjectReporting().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
