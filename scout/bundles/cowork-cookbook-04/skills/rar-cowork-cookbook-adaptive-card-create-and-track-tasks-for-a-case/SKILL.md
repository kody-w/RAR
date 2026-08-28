---
name: "rar-cowork-cookbook-adaptive-card-create-and-track-tasks-for-a-case"
description: "Produces a reusable Adaptive Card JSON snapshot of create and track tasks for a case status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_create_and_track_tasks_for_a_case", "rar_sha256": "89cfb84cce704a95606b7a06aa371a8595f8ec0c583ec2fa25c96f29ee2e5899", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_create_and_track_tasks_for_a_case`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_create_and_track_tasks_for_a_case_agent.py` and in the RCI capsule.

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

Create and track tasks for a case Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of create and track tasks for a case status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-create-and-track-tasks-for-a-case
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_create_and_track_tasks_for_a_case_agent.py` and embedded as the fenced Python below (sha256 89cfb84cce704a95…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_create_and_track_tasks_for_a_case_agent.py` first:

```bash
python3 adaptive_card_create_and_track_tasks_for_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_create_and_track_tasks_for_a_case_agent.py   # or on stdin
python3 adaptive_card_create_and_track_tasks_for_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create and track tasks for a case Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of create and track tasks for a case status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-create-and-track-tasks-for-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_create_and_track_tasks_for_a_case',
    "version": '2.0.1',
    "display_name": 'Create and track tasks for a case Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of create and track tasks for a case status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-create-and-track-tasks-for-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-create-and-track-tasks-for-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e4b5ef57665501c8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/create-and-track-tasks-for-a-case'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/adaptive-card-create-and-track-tasks-for-a-case', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardCreateAndTrackTasksForACase(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardCreateAndTrackTasksForACase'
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
    print(AdaptiveCardCreateAndTrackTasksForACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
