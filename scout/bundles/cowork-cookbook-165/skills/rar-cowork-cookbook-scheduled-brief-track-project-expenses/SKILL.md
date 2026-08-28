---
name: "rar-cowork-cookbook-scheduled-brief-track-project-expenses"
description: "Schedulable morning-brief email summarizing track project expenses for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_track_project_expenses", "rar_sha256": "9509f008acab9b9fadf41a2fdba09c3c5bf0f2dd707feec827c55160b9e9666a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_track_project_expenses`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_track_project_expenses_agent.py` and in the RCI capsule.

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

Track project expenses Scheduled Email Brief — Schedulable morning-brief email summarizing track project expenses for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-track-project-expenses
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
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_track_project_expenses_agent.py` and embedded as the fenced Python below (sha256 9509f008acab9b9f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_track_project_expenses_agent.py` first:

```bash
python3 scheduled_brief_track_project_expenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_track_project_expenses_agent.py   # or on stdin
python3 scheduled_brief_track_project_expenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track project expenses Scheduled Email Brief — Schedulable morning-brief email summarizing track project expenses for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-track-project-expenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_track_project_expenses',
    "version": '2.0.1',
    "display_name": 'Track project expenses Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing track project expenses for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-track-project-expenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-track-project-expenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd7fcf107e421f4a6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/track-project-expenses'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/scheduled-brief-track-project-expenses', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefTrackProjectExpenses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefTrackProjectExpenses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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
    print(ScheduledBriefTrackProjectExpenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
