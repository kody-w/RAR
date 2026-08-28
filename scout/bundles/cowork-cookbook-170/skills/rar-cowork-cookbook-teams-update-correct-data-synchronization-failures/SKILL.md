---
name: "rar-cowork-cookbook-teams-update-correct-data-synchronization-failures"
description: "Drafts a Teams channel post on correct data synchronization failures status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_correct_data_synchronization_failures", "rar_sha256": "a0f4c4db1aaaf5723f46a9f8c2f712f7e81de708155cb9ddcad380a28097756c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_correct_data_synchronization_failures`. The original RAPP
agent is preserved byte-for-byte in `teams_update_correct_data_synchronization_failures_agent.py` and in the RCI capsule.

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

Correct data synchronization failures Teams Channel Update — Drafts a Teams channel post on correct data synchronization failures status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-correct-data-synchronization-failures
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_correct_data_synchronization_failures_agent.py` and embedded as the fenced Python below (sha256 a0f4c4db1aaaf572…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_correct_data_synchronization_failures_agent.py` first:

```bash
python3 teams_update_correct_data_synchronization_failures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_correct_data_synchronization_failures_agent.py   # or on stdin
python3 teams_update_correct_data_synchronization_failures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct data synchronization failures Teams Channel Update — Drafts a Teams channel post on correct data synchronization failures status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-correct-data-synchronization-failures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_correct_data_synchronization_failures',
    "version": '2.0.1',
    "display_name": 'Correct data synchronization failures Teams Channel Update',
    "description": 'Drafts a Teams channel post on correct data synchronization failures status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-correct-data-synchronization-failures',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-correct-data-synchronization-failures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '36a44957bc2a06e4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-data/correct-data-synchronization-failures'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-correct-data-synchronization-failures', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateCorrectDataSynchronizationFailures(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateCorrectDataSynchronizationFailures'
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
    print(TeamsUpdateCorrectDataSynchronizationFailures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
