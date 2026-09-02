---
name: "rar-cowork-cookbook-teams-update-configure-and-monitor-system-generated-numbers"
description: "Drafts a Teams channel post on configure and monitor system generated numbers status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_configure_and_monitor_system_generated_numbers", "rar_sha256": "05c3ad74b65863bf75d2bfb829141ae98fba3cfae4212a8ae86a0ee4966ceecf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_configure_and_monitor_system_generated_numbers_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-configure-and-monitor-system-generated-numbers:1383da8331ad41214c22549630227369e0305c22914b047f5104f0f0f41343c3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_configure_and_monitor_system_generated_numbers`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_configure_and_monitor_system_generated_numbers_agent.py` is
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
