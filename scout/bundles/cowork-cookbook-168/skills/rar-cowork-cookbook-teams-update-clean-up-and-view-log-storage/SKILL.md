---
name: "rar-cowork-cookbook-teams-update-clean-up-and-view-log-storage"
description: "Drafts a Teams channel post on clean up and view log storage status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_clean_up_and_view_log_storage", "rar_sha256": "fbd380c70f5d0b9f574af5433ca8326043179511492645036d670f1ebbfbbfff", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_clean_up_and_view_log_storage_agent.py` and embedded as the fenced Python below (sha256 fbd380c70f5d0b9f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_clean_up_and_view_log_storage_agent.py` first:

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
    "version": '2.0.0',
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
