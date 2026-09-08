---
name: "rar-cowork-cookbook-bulk-update-define-notification-channels"
description: "Applies a bulk field update to define-notification-channels records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval before committing c"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_notification_channels", "rar_sha256": "c26c55b966ea70dac4b15aef91781096a272e9f490b28873fc0103f6a2072585", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_notification_channels`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_notification_channels_agent.py` and in the RCI capsule.

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

Define notification channels Bulk Field Update — Applies a bulk field update to define-notification-channels records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval before committing c

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-notification-channels
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
      "description": "Explicit approval after reviewing the dry-run preview workbook, before changes are committed.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to run against; defaults to USMF sandbox.",
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
      "description": "List of define notification channels record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_notification_channels_agent.py` and embedded as the fenced Python below (sha256 c26c55b966ea70da…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_notification_channels_agent.py` first:

```bash
python3 bulk_update_define_notification_channels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_notification_channels_agent.py   # or on stdin
python3 bulk_update_define_notification_channels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define notification channels Bulk Field Update — Applies a bulk field update to define-notification-channels records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval before committing c

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-notification-channels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_notification_channels',
    "version": '3.0.3',
    "display_name": 'Define notification channels Bulk Field Update',
    "description": 'Applies a bulk field update to define-notification-channels records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval before committing c',
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
        "upstream_slug": 'bulk-update-define-notification-channels',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-notification-channels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '886b95576ec78df8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/define-notification-channels'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-define-notification-channels', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of define notification channels record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when define notification channels records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to define notification channels records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to define-notification-channels records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval before committing c', 'example_request': 'Bulk update these notification channel record IDs to the new value in USMF sandbox — show me the dry-run first.', 'inputs': [{'description': 'List of define notification channels record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change one or more fields across many define notification channels records at once and want a before/after dry-run preview and approval gate first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDefineNotificationChannels(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineNotificationChannels'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of define notification channels record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDefineNotificationChannels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
