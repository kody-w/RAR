---
name: "rar-cowork-cookbook-bulk-update-adjust-notifications-and-alerts"
description: "Applies a bulk field update to adjust notifications and alerts records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs and new values, with a dry-run preview workbook and approval pa"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_adjust_notifications_and_alerts", "rar_sha256": "c5e409912afa18603cbc95085a34cb4b8820e1bcfcd1e446a8f4d8b8c651f410", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_adjust_notifications_and_alerts`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_adjust_notifications_and_alerts_agent.py` and in the RCI capsule.

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

Adjust notifications and alerts Bulk Field Update — Applies a bulk field update to adjust notifications and alerts records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs and new values, with a dry-run preview workbook and approval pa

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-adjust-notifications-and-alerts
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
      "description": "D365 legal entity to run against (defaults to USMF sandbox).",
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
      "description": "List of adjust notifications and alerts record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_adjust_notifications_and_alerts_agent.py` and embedded as the fenced Python below (sha256 c5e409912afa1860…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_adjust_notifications_and_alerts_agent.py` first:

```bash
python3 bulk_update_adjust_notifications_and_alerts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_adjust_notifications_and_alerts_agent.py   # or on stdin
python3 bulk_update_adjust_notifications_and_alerts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Adjust notifications and alerts Bulk Field Update — Applies a bulk field update to adjust notifications and alerts records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs and new values, with a dry-run preview workbook and approval pa

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-adjust-notifications-and-alerts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_adjust_notifications_and_alerts',
    "version": '3.0.3',
    "display_name": 'Adjust notifications and alerts Bulk Field Update',
    "description": 'Applies a bulk field update to adjust notifications and alerts records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs and new values, with a dry-run preview workbook and approval pa',
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
        "upstream_slug": 'bulk-update-adjust-notifications-and-alerts',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-adjust-notifications-and-alerts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '931fc0c8150ed98b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/adjust-notifications-and-alerts'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-adjust-notifications-and-alerts', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (defaults to USMF sandbox).', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of adjust notifications and alerts record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when adjust notifications and alerts records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to adjust notifications and alerts records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to adjust notifications and alerts records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs and new values, with a dry-run preview workbook and approval pa', 'example_request': 'Bulk-update these alert record IDs to the new value in USMF sandbox — show me a dry-run preview first.', 'inputs': [{'description': 'List of adjust notifications and alerts record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against (defaults to USMF sandbox).', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many adjust notifications and alerts records at once in a D365 sandbox and want a reviewable preview before writing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateAdjustNotificationsAndAlerts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAdjustNotificationsAndAlerts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (defaults to USMF sandbox).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of adjust notifications and alerts record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateAdjustNotificationsAndAlerts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
