---
name: "rar-cowork-cookbook-configure-enable-and-configure-audit-logs"
description: "Applies a bulk configuration change to enable and configure audit logs from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_enable_and_configure_audit_logs", "rar_sha256": "6729964054860328722c3b1dbf63230868f9f83651c9956790da39a5f6fd602f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_enable_and_configure_audit_logs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-enable-and-configure-audit-logs:9c27c3bf8896690674ef69abec917f0dd31894e22a6611036f1519808d5432ab", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_enable_and_configure_audit_logs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_enable_and_configure_audit_logs_agent.py` is
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
