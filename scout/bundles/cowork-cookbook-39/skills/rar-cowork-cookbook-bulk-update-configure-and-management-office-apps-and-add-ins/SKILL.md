---
name: "rar-cowork-cookbook-bulk-update-configure-and-management-office-apps-and-add-ins"
description: "Runs a bulk field update on Office apps and add-ins configuration records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, the"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_configure_and_management_office_apps_and_add_ins", "rar_sha256": "df3f9cfb81d8e4267b213fa0520c7180e06b4c9f7657c48bd9d266cb9206db46", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_configure_and_management_office_apps_and_add_ins`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_configure_and_management_office_apps_and_add_ins_agent.py` and in the RCI capsule.

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

Configure and management office apps and add-ins Bulk Field Update — Runs a bulk field update on Office apps and add-ins configuration records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, the

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-configure-and-management-office-apps-and-add-ins
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
      "description": "Explicit approval after reviewing the dry-run preview workbook, before any write.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; defaults to USMF sandbox.",
      "type": "string"
    },
    "new_values": {
      "description": "The new field value(s) to apply to each listed record.",
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
      "description": "List of record IDs for the office apps and add-ins records to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_configure_and_management_office_apps_and_add_ins_agent.py` and embedded as the fenced Python below (sha256 df3f9cfb81d8e426…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_configure_and_management_office_apps_and_add_ins_agent.py` first:

```bash
python3 bulk_update_configure_and_management_office_apps_and_add_ins_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_configure_and_management_office_apps_and_add_ins_agent.py   # or on stdin
python3 bulk_update_configure_and_management_office_apps_and_add_ins_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and management office apps and add-ins Bulk Field Update — Runs a bulk field update on Office apps and add-ins configuration records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, the

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-configure-and-management-office-apps-and-add-ins
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_configure_and_management_office_apps_and_add_ins',
    "version": '3.0.3',
    "display_name": 'Configure and management office apps and add-ins Bulk Field Update',
    "description": 'Runs a bulk field update on Office apps and add-ins configuration records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, the',
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
        "upstream_slug": 'bulk-update-configure-and-management-office-apps-and-add-ins',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-configure-and-management-office-apps-and-add-ins',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ee63c7995ef28fd8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-management-office-apps-and-add-ins'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-configure-and-management-office-apps-and-add-ins', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before any write.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The new field value(s) to apply to each listed record.', 'record_ids': 'List of record IDs for the office apps and add-ins records to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when configure and management office apps and add-ins records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to configure and management office apps and add-ins records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a bulk field update on Office apps and add-ins configuration records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, the', 'example_request': 'Bulk update these office add-in records in USMF sandbox to the new value — show me the dry-run preview first.', 'inputs': [{'description': 'List of record IDs for the office apps and add-ins records to update.', 'name': 'record_ids'}, {'description': 'The new field value(s) to apply to each listed record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before any write.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across a supplied list of D365 office apps/add-ins records and want a reviewable before/after preview before committing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateConfigureAndManagementOfficeAppsAndAddIns(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateConfigureAndManagementOfficeAppsAndAddIns'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before any write.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The new field value(s) to apply to each listed record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of record IDs for the office apps and add-ins records to update.', 'type': 'string'}},
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
    print(BulkUpdateConfigureAndManagementOfficeAppsAndAddIns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
