---
name: "rar-cowork-cookbook-bulk-update-enable-and-configure-audit-logs"
description: "Applies a bulk field update across enable and configure audit logs records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_enable_and_configure_audit_logs", "rar_sha256": "982eb71d2203795c3beb4cd32a28fbe3f4de1a2e389104f45186d2559ae33f19", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_enable_and_configure_audit_logs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-enable-and-configure-audit-logs:f36c61ef71a90661f6153bf89c7e834ccd11ea11d63ea2b92e121b1c49e71f1e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_enable_and_configure_audit_logs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_enable_and_configure_audit_logs_agent.py` is
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
