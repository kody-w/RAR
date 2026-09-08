---
name: "rar-cowork-cookbook-bulk-update-adjust-notifications-and-alerts"
description: "Applies a bulk field update to adjust notifications and alerts records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs and new values, with a dry-run preview workbook and approval pa"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_adjust_notifications_and_alerts", "rar_sha256": "c5e409912afa18603cbc95085a34cb4b8820e1bcfcd1e446a8f4d8b8c651f410", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
