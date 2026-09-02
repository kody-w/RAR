---
name: "rar-cowork-cookbook-configure-configure-monitor-and-send-emails"
description: "Applies a bulk configuration change to configure, monitor, and send emails from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_configure_monitor_and_send_emails", "rar_sha256": "f6e9fa79aa18988e00923e0e63ded63ae066138447485a809015e77222ab74cc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_configure_monitor_and_send_emails_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-configure-monitor-and-send-emails:8b140fbd97a48b05fa5260d4a6c81027b8907d82671078c4b8001f022314910a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_configure_monitor_and_send_emails`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_configure_monitor_and_send_emails_agent.py` is
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
