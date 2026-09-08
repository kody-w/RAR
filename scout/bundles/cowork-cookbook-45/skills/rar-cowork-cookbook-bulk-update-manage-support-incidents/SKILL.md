---
name: "rar-cowork-cookbook-bulk-update-manage-support-incidents"
description: "Applies a bulk field update to support incident records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval befor"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_support_incidents", "rar_sha256": "4c17049e845d2e9cb88c350e625393f12aaf40e5d7fbc7116bf10f96befc70d6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_manage_support_incidents`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_manage_support_incidents_agent.py` and in the RCI capsule.

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

Manage support incidents Bulk Field Update — Applies a bulk field update to support incident records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval befor

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-support-incidents
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
    "field_values": {
      "description": "The field(s) and new value(s) to apply to each record.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to run against (default USMF, sandbox).",
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
      "description": "List of support incident record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_support_incidents_agent.py` and embedded as the fenced Python below (sha256 4c17049e845d2e9c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_support_incidents_agent.py` first:

```bash
python3 bulk_update_manage_support_incidents_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_manage_support_incidents_agent.py   # or on stdin
python3 bulk_update_manage_support_incidents_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage support incidents Bulk Field Update — Applies a bulk field update to support incident records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval befor

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-support-incidents
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_manage_support_incidents',
    "version": '3.0.3',
    "display_name": 'Manage support incidents Bulk Field Update',
    "description": 'Applies a bulk field update to support incident records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval befor',
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
        "upstream_slug": 'bulk-update-manage-support-incidents',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-manage-support-incidents',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '773b9af7aa579070',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/manage-support-incidents'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-manage-support-incidents', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'field_values': 'The field(s) and new value(s) to apply to each record.', 'legal_entity': 'Dynamics 365 legal entity to run against (default USMF, sandbox).', 'record_ids': 'List of support incident record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when manage support incidents records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to manage support incidents records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to support incident records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval befor', 'example_request': 'Bulk-update these support incident IDs in USMF sandbox with the new priority value — show me the dry-run first.', 'inputs': [{'description': 'List of support incident record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'field_values'}, {'description': 'Dynamics 365 legal entity to run against (default USMF, sandbox).', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to change the same field(s) across many support incident records at once and want a reviewable dry-run preview before any data is written.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateManageSupportIncidents(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateManageSupportIncidents'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'field_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against (default USMF, sandbox).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of support incident record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateManageSupportIncidents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
