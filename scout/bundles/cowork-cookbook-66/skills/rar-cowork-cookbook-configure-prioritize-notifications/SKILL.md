---
name: "rar-cowork-cookbook-configure-prioritize-notifications"
description: "Applies a bulk configuration change to prioritize notifications from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_prioritize_notifications", "rar_sha256": "443f1af4bd6bae13af2b7e9d3abe34374857699deef7f4dbd6d9eed1757d91ac", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_prioritize_notifications_agent.py` and embedded as the fenced Python below (sha256 443f1af4bd6bae13…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_prioritize_notifications_agent.py` first:

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
    "version": '2.0.0',
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
