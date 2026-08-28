---
name: "rar-cowork-cookbook-configure-configure-monitor-and-send-emails"
description: "Applies a bulk configuration change to configure, monitor, and send emails from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_configure_monitor_and_send_emails", "rar_sha256": "e683cc63ba3e5ae48b07264c74f8073deb3bf3f2818b5c1bcd679a45c2458f4a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_configure_monitor_and_send_emails`. The original RAPP
agent is preserved byte-for-byte in `configure_configure_monitor_and_send_emails_agent.py` and in the RCI capsule.

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

Configure, monitor, and send emails Configuration Bulk Setup — Applies a bulk configuration change to configure, monitor, and send emails from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-configure-monitor-and-send-emails
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_configure_monitor_and_send_emails_agent.py` and embedded as the fenced Python below (sha256 e683cc63ba3e5ae4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_configure_monitor_and_send_emails_agent.py` first:

```bash
python3 configure_configure_monitor_and_send_emails_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_configure_monitor_and_send_emails_agent.py   # or on stdin
python3 configure_configure_monitor_and_send_emails_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure, monitor, and send emails Configuration Bulk Setup — Applies a bulk configuration change to configure, monitor, and send emails from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-configure-monitor-and-send-emails
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_configure_monitor_and_send_emails',
    "version": '2.0.1',
    "display_name": 'Configure, monitor, and send emails Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to configure, monitor, and send emails from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-configure-monitor-and-send-emails',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-configure-monitor-and-send-emails',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '74d85e7de8259d5c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-monitor-and-send-emails'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-configure-monitor-and-send-emails', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureConfigureMonitorAndSendEmails(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureConfigureMonitorAndSendEmails'
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
    print(ConfigureConfigureMonitorAndSendEmails().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
