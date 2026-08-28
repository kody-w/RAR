---
name: "rar-cowork-cookbook-bulk-update-enable-and-configure-audit-logs"
description: "Applies a bulk field update across enable and configure audit logs records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_enable_and_configure_audit_logs", "rar_sha256": "982eb71d2203795c3beb4cd32a28fbe3f4de1a2e389104f45186d2559ae33f19", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_enable_and_configure_audit_logs`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_enable_and_configure_audit_logs_agent.py` and in the RCI capsule.

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

Enable and configure audit logs Bulk Field Update — Applies a bulk field update across enable and configure audit logs records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-enable-and-configure-audit-logs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_enable_and_configure_audit_logs_agent.py` and embedded as the fenced Python below (sha256 982eb71d2203795c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_enable_and_configure_audit_logs_agent.py` first:

```bash
python3 bulk_update_enable_and_configure_audit_logs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_enable_and_configure_audit_logs_agent.py   # or on stdin
python3 bulk_update_enable_and_configure_audit_logs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Enable and configure audit logs Bulk Field Update — Applies a bulk field update across enable and configure audit logs records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-enable-and-configure-audit-logs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_enable_and_configure_audit_logs',
    "version": '2.0.0',
    "display_name": 'Enable and configure audit logs Bulk Field Update',
    "description": 'Applies a bulk field update across enable and configure audit logs records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-enable-and-configure-audit-logs',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-enable-and-configure-audit-logs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '94f1d9b43a1aa1b0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/enable-and-configure-audit-logs'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-enable-and-configure-audit-logs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateEnableAndConfigureAuditLogs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateEnableAndConfigureAuditLogs'
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
    print(BulkUpdateEnableAndConfigureAuditLogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
