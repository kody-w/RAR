---
name: "rar-cowork-cookbook-configure-enable-and-configure-audit-logs"
description: "Applies a bulk configuration change to enable and configure audit logs from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_enable_and_configure_audit_logs", "rar_sha256": "6729964054860328722c3b1dbf63230868f9f83651c9956790da39a5f6fd602f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_enable_and_configure_audit_logs_agent.py` and embedded as the fenced Python below (sha256 6729964054860328…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_enable_and_configure_audit_logs_agent.py` first:

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
    "version": '2.0.0',
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
