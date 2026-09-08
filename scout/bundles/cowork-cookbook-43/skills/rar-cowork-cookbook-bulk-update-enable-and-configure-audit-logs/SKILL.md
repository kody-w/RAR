---
name: "rar-cowork-cookbook-bulk-update-enable-and-configure-audit-logs"
description: "Runs a bulk field update on audit log configuration records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, waits for approval, then applies changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_enable_and_configure_audit_logs", "rar_sha256": "9512b80a548f8763630549a43a8053ba4bee5130870dd99ddc0f123c8caa1856", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

Enable and configure audit logs Bulk Field Update — Runs a bulk field update on audit log configuration records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, waits for approval, then applies changes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

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
    "approval": {
      "description": "Explicit go-ahead after reviewing the dry-run preview workbook.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Target D365 legal entity; defaults to USMF sandbox.",
      "type": "string"
    },
    "new_values": {
      "description": "The field(s) and new value(s) to apply to each record.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "record_ids": {
      "description": "List of audit log record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_enable_and_configure_audit_logs_agent.py` and embedded as the fenced Python below (sha256 9512b80a548f8763…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_enable_and_configure_audit_logs_agent.py` first:

```bash
python3 bulk_update_enable_and_configure_audit_logs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_enable_and_configure_audit_logs_agent.py   # or on stdin
python3 bulk_update_enable_and_configure_audit_logs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Enable and configure audit logs Bulk Field Update — Runs a bulk field update on audit log configuration records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, waits for approval, then applies changes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

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
    "version": '3.0.3',
    "display_name": 'Enable and configure audit logs Bulk Field Update',
    "description": 'Runs a bulk field update on audit log configuration records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, waits for approval, then applies changes.',
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
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5a3fbe45a5c78ffb',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Target D365 legal entity; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of audit log record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when enable and configure audit logs records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to enable and configure audit logs records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a bulk field update on audit log configuration records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin: returns a dry-run preview workbook, waits for approval, then applies changes.', 'example_request': 'Bulk update the audit log settings for these record IDs in USMF sandbox — show me a dry-run first.', 'inputs': [{'description': 'List of audit log record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Target D365 legal entity; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to change the same field(s) across many audit-log records at once and want a before/after preview and approval gate before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateEnableAndConfigureAuditLogs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateEnableAndConfigureAuditLogs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Target D365 legal entity; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of audit log record IDs to update.', 'type': 'string'}},
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
