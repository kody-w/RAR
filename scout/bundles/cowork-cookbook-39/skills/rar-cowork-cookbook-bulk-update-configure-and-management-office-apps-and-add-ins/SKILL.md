---
name: "rar-cowork-cookbook-bulk-update-configure-and-management-office-apps-and-add-ins"
description: "Runs a bulk field update on Office apps and add-ins configuration records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, the"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_configure_and_management_office_apps_and_add_ins", "rar_sha256": "df3f9cfb81d8e4267b213fa0520c7180e06b4c9f7657c48bd9d266cb9206db46", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
