---
name: "rar-cowork-cookbook-configure-configure-monitor-and-send-emails"
description: "Applies a bulk configuration change to configure, monitor, and send emails from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_configure_monitor_and_send_emails", "rar_sha256": "f6e9fa79aa18988e00923e0e63ded63ae066138447485a809015e77222ab74cc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_configure_monitor_and_send_emails_agent.py` and embedded as the fenced Python below (sha256 f6e9fa79aa18988e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_configure_monitor_and_send_emails_agent.py` first:

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
    "version": '2.0.0',
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
