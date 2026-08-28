---
name: "rar-cowork-cookbook-teams-update-correct-data-synchronization-failures"
description: "Drafts a Teams channel post on correct data synchronization failures status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_correct_data_synchronization_failures", "rar_sha256": "59578c4e397988f81e3b60acc95b2d9d9efc0516ca6df03df8b5323decb95e35", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_correct_data_synchronization_failures_agent.py` and embedded as the fenced Python below (sha256 59578c4e397988f8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_correct_data_synchronization_failures_agent.py` first:

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
    "version": '2.0.0',
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
