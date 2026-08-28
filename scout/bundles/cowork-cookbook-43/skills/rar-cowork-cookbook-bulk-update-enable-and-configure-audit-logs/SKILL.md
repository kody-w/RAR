---
name: "rar-cowork-cookbook-bulk-update-enable-and-configure-audit-logs"
description: "Applies a bulk field update across enable and configure audit logs records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_enable_and_configure_audit_logs", "rar_sha256": "2baf92db0c6466ca5e60867532f2c2334b7f8e0bb4986309a6112e18788575ba", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_enable_and_configure_audit_logs_agent.py` and embedded as the fenced Python below (sha256 2baf92db0c6466ca…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_enable_and_configure_audit_logs_agent.py` first:

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
    "version": '2.0.1',
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
