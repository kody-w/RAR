---
name: "rar-cowork-cookbook-bulk-update-send-case-close-notification"
description: "Applies a bulk field update to send case close notification records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, returning a dry-run preview workbook for approval before committing a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_send_case_close_notification", "rar_sha256": "43f203b33ac7816b955b8b5a90a3b039ceaa8467b0cb8dc89016b6e7bd7295f1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
