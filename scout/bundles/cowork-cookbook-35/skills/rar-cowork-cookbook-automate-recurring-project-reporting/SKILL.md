---
name: "rar-cowork-cookbook-automate-recurring-project-reporting"
description: "Replace the manual \"pull the board, write the update, send it out\" Monday-morning cycle with a status update that writes and sends itself."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/automate_recurring_project_reporting", "rar_sha256": "8ee6baf76060e5b0b1a34acc7a0d672246f08d5acef6c6391a02455bea1ee05e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "automate_recurring_project_reporting_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/automate-recurring-project-reporting:922464754c4906c949b493523d2d288cad338b509460f7adadfd9e60fbc94b9e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "work_management", "advanced", "integration", "monday_com"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/automate_recurring_project_reporting`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `automate_recurring_project_reporting_agent.py` is
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
