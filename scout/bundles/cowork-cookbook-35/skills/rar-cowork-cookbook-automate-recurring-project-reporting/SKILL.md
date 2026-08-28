---
name: "rar-cowork-cookbook-automate-recurring-project-reporting"
description: "Replace the manual \"pull the board, write the update, send it out\" Monday-morning cycle with a status update that writes and sends itself."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/automate_recurring_project_reporting", "rar_sha256": "e6a745820c852ce105a16c82ae0736190304a7cfa935d368ca77ca601dd64dfa", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "work_management", "advanced", "integration", "monday_com"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `automate_recurring_project_reporting_agent.py` and embedded as the fenced Python below (sha256 e6a745820c852ce1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `automate_recurring_project_reporting_agent.py` first:

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
    "version": '2.0.1',
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
