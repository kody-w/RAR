---
name: "rar-cowork-cookbook-bulk-update-define-notification-channels"
description: "Applies a bulk field update to define-notification-channels records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval before committing c"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_notification_channels", "rar_sha256": "c26c55b966ea70dac4b15aef91781096a272e9f490b28873fc0103f6a2072585", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
