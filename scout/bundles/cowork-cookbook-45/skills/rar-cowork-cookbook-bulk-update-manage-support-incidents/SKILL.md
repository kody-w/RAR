---
name: "rar-cowork-cookbook-bulk-update-manage-support-incidents"
description: "Applies a bulk field update to support incident records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval befor"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_support_incidents", "rar_sha256": "4c17049e845d2e9cb88c350e625393f12aaf40e5d7fbc7116bf10f96befc70d6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
