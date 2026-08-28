---
name: "rar-cowork-cookbook-adaptive-card-create-and-track-tasks-for-a-case"
description: "Produces a reusable Adaptive Card JSON snapshot of create and track tasks for a case status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_create_and_track_tasks_for_a_case", "rar_sha256": "485d2dd87b805de268c059642e63f0a3bc405c04559ba914864620ed24749128", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_create_and_track_tasks_for_a_case_agent.py` and embedded as the fenced Python below (sha256 485d2dd87b805de2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_create_and_track_tasks_for_a_case_agent.py` first:

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
    "version": '2.0.0',
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
