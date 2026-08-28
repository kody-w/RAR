---
name: "rar-cowork-cookbook-configure-enable-and-configure-audit-logs"
description: "Applies a bulk configuration change to enable and configure audit logs from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_enable_and_configure_audit_logs", "rar_sha256": "049ba7ac09436baa602888a29edb07302b7550dea17217afe7fc84545c700b60", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_enable_and_configure_audit_logs`. The original RAPP
agent is preserved byte-for-byte in `configure_enable_and_configure_audit_logs_agent.py` and in the RCI capsule.

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

Enable and configure audit logs Configuration Bulk Setup — Applies a bulk configuration change to enable and configure audit logs from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-enable-and-configure-audit-logs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_enable_and_configure_audit_logs_agent.py` and embedded as the fenced Python below (sha256 049ba7ac09436baa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_enable_and_configure_audit_logs_agent.py` first:

```bash
python3 configure_enable_and_configure_audit_logs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_enable_and_configure_audit_logs_agent.py   # or on stdin
python3 configure_enable_and_configure_audit_logs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Enable and configure audit logs Configuration Bulk Setup — Applies a bulk configuration change to enable and configure audit logs from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-enable-and-configure-audit-logs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_enable_and_configure_audit_logs',
    "version": '2.0.1',
    "display_name": 'Enable and configure audit logs Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to enable and configure audit logs from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-enable-and-configure-audit-logs',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-enable-and-configure-audit-logs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1146594f207ecefc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/enable-and-configure-audit-logs'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-enable-and-configure-audit-logs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureEnableAndConfigureAuditLogs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureEnableAndConfigureAuditLogs'
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
    print(ConfigureEnableAndConfigureAuditLogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
