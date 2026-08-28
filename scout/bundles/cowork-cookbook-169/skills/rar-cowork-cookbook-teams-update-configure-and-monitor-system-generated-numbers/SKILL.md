---
name: "rar-cowork-cookbook-teams-update-configure-and-monitor-system-generated-numbers"
description: "Drafts a Teams channel post on configure and monitor system generated numbers status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_configure_and_monitor_system_generated_numbers", "rar_sha256": "05c3ad74b65863bf75d2bfb829141ae98fba3cfae4212a8ae86a0ee4966ceecf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_configure_and_monitor_system_generated_numbers`. The original RAPP
agent is preserved byte-for-byte in `teams_update_configure_and_monitor_system_generated_numbers_agent.py` and in the RCI capsule.

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

Configure and monitor system generated numbers Teams Channel Update — Drafts a Teams channel post on configure and monitor system generated numbers status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-configure-and-monitor-system-generated-numbers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_configure_and_monitor_system_generated_numbers_agent.py` and embedded as the fenced Python below (sha256 05c3ad74b65863bf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_configure_and_monitor_system_generated_numbers_agent.py` first:

```bash
python3 teams_update_configure_and_monitor_system_generated_numbers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_configure_and_monitor_system_generated_numbers_agent.py   # or on stdin
python3 teams_update_configure_and_monitor_system_generated_numbers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and monitor system generated numbers Teams Channel Update — Drafts a Teams channel post on configure and monitor system generated numbers status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-configure-and-monitor-system-generated-numbers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_configure_and_monitor_system_generated_numbers',
    "version": '2.0.0',
    "display_name": 'Configure and monitor system generated numbers Teams Channel Update',
    "description": 'Drafts a Teams channel post on configure and monitor system generated numbers status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-configure-and-monitor-system-generated-numbers',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-configure-and-monitor-system-generated-numbers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0be395dd115b50ae',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-monitor-system-generated-numbers'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-configure-and-monitor-system-generated-numbers', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateConfigureAndMonitorSystemGeneratedNumbers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateConfigureAndMonitorSystemGeneratedNumbers'
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
    print(TeamsUpdateConfigureAndMonitorSystemGeneratedNumbers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
