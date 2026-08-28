---
name: "rar-cowork-cookbook-teams-update-configure-and-monitor-system-generated-numbers"
description: "Drafts a Teams channel post on configure and monitor system generated numbers status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_configure_and_monitor_system_generated_numbers", "rar_sha256": "4755670ddd08f773bc0b09e3df6383b17281bcdbe7625af9f8f5f8f2dc9e4057", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_configure_and_monitor_system_generated_numbers_agent.py` and embedded as the fenced Python below (sha256 4755670ddd08f773…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_configure_and_monitor_system_generated_numbers_agent.py` first:

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
    "version": '2.0.1',
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
