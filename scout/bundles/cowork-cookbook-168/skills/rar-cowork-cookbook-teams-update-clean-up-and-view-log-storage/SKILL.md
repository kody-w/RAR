---
name: "rar-cowork-cookbook-teams-update-clean-up-and-view-log-storage"
description: "Drafts a Teams channel post on clean up and view log storage status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_clean_up_and_view_log_storage", "rar_sha256": "2cea4f72c64db9c57663d2b9c9503d754f7ea32ab57122687d65ac812206c05f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_clean_up_and_view_log_storage`. The original RAPP
agent is preserved byte-for-byte in `teams_update_clean_up_and_view_log_storage_agent.py` and in the RCI capsule.

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

Clean up and view log storage Teams Channel Update — Drafts a Teams channel post on clean up and view log storage status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-clean-up-and-view-log-storage
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_clean_up_and_view_log_storage_agent.py` and embedded as the fenced Python below (sha256 2cea4f72c64db9c5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_clean_up_and_view_log_storage_agent.py` first:

```bash
python3 teams_update_clean_up_and_view_log_storage_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_clean_up_and_view_log_storage_agent.py   # or on stdin
python3 teams_update_clean_up_and_view_log_storage_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Clean up and view log storage Teams Channel Update — Drafts a Teams channel post on clean up and view log storage status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-clean-up-and-view-log-storage
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_clean_up_and_view_log_storage',
    "version": '2.0.1',
    "display_name": 'Clean up and view log storage Teams Channel Update',
    "description": 'Drafts a Teams channel post on clean up and view log storage status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-clean-up-and-view-log-storage',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-clean-up-and-view-log-storage',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '47c55292fdae5131',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/clean-up-and-view-log-storage'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-clean-up-and-view-log-storage', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateCleanUpAndViewLogStorage(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateCleanUpAndViewLogStorage'
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
    print(TeamsUpdateCleanUpAndViewLogStorage().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
