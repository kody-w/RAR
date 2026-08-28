---
name: "rar-cowork-cookbook-configure-prioritize-notifications"
description: "Applies a bulk configuration change to prioritize notifications from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_prioritize_notifications", "rar_sha256": "0a5704b4bf701a5f8984355fdee7d22c81752a70d1bbf7e89b89d5991fe10969", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_prioritize_notifications`. The original RAPP
agent is preserved byte-for-byte in `configure_prioritize_notifications_agent.py` and in the RCI capsule.

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

Prioritize notifications Configuration Bulk Setup — Applies a bulk configuration change to prioritize notifications from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-prioritize-notifications
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_prioritize_notifications_agent.py` and embedded as the fenced Python below (sha256 0a5704b4bf701a5f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_prioritize_notifications_agent.py` first:

```bash
python3 configure_prioritize_notifications_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_prioritize_notifications_agent.py   # or on stdin
python3 configure_prioritize_notifications_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prioritize notifications Configuration Bulk Setup — Applies a bulk configuration change to prioritize notifications from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-prioritize-notifications
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_prioritize_notifications',
    "version": '2.0.1',
    "display_name": 'Prioritize notifications Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to prioritize notifications from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-prioritize-notifications',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-prioritize-notifications',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '526041cd3f860787',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/prioritize-notifications'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-prioritize-notifications', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigurePrioritizeNotifications(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePrioritizeNotifications'
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
    print(ConfigurePrioritizeNotifications().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
