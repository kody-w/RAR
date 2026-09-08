---
name: "rar-cowork-cookbook-bulk-update-send-case-close-notification"
description: "Applies a bulk field update to send case close notification records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval before committing a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_send_case_close_notification", "rar_sha256": "43f203b33ac7816b955b8b5a90a3b039ceaa8467b0cb8dc89016b6e7bd7295f1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_send_case_close_notification`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_send_case_close_notification_agent.py` and in the RCI capsule.

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

Send case close notification Bulk Field Update — Applies a bulk field update to send case close notification records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval before committing a

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-send-case-close-notification
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
    "environment": {
      "description": "Target environment; sandbox only for this recipe.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; recipe default is USMF.",
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
      "description": "List of send case close notification record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_send_case_close_notification_agent.py` and embedded as the fenced Python below (sha256 43f203b33ac7816b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_send_case_close_notification_agent.py` first:

```bash
python3 bulk_update_send_case_close_notification_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_send_case_close_notification_agent.py   # or on stdin
python3 bulk_update_send_case_close_notification_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Send case close notification Bulk Field Update — Applies a bulk field update to send case close notification records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval before committing a

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-send-case-close-notification
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_send_case_close_notification',
    "version": '3.0.3',
    "display_name": 'Send case close notification Bulk Field Update',
    "description": 'Applies a bulk field update to send case close notification records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval before committing a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-send-case-close-notification',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-send-case-close-notification',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8bdfd0c77387bca0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/send-case-close-notification'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/bulk-update-send-case-close-notification', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox only for this recipe.', 'legal_entity': 'D365 legal entity to run against; recipe default is USMF.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of send case close notification record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when send case close notification records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to send case close notification records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to send case close notification records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval before committing a', 'example_request': 'Bulk update these send case close notification record IDs in USMF sandbox — show me the dry-run preview first.', 'inputs': [{'description': 'List of send case close notification record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; recipe default is USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox only for this recipe.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across a known list of send case close notification record IDs in a D365 sandbox, with preview-then-approve safety.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateSendCaseCloseNotification(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateSendCaseCloseNotification'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox only for this recipe.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; recipe default is USMF.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of send case close notification record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateSendCaseCloseNotification().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
