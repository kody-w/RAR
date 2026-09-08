---
name: "rar-cowork-cookbook-configure-allocate-or-assign-software-licenses"
description: "Bulk-applies software license allocation/assignment changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies and emits before/after c"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_allocate_or_assign_software_licenses", "rar_sha256": "934e6550551f49f26f32ce5f94791d6331d7594b5e3d38cdbec5014eb0645261", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_allocate_or_assign_software_licenses`. The original RAPP
agent is preserved byte-for-byte in `configure_allocate_or_assign_software_licenses_agent.py` and in the RCI capsule.

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

Allocate or assign software licenses Configuration Bulk Setup — Bulk-applies software license allocation/assignment changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies and emits before/after c

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-allocate-or-assign-software-licenses
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
      "description": "Explicit user approval after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_excel": {
      "description": "Attached Excel file with one row per license allocation/assignment target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF); sandbox environment first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_allocate_or_assign_software_licenses_agent.py` and embedded as the fenced Python below (sha256 934e6550551f49f2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_allocate_or_assign_software_licenses_agent.py` first:

```bash
python3 configure_allocate_or_assign_software_licenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_allocate_or_assign_software_licenses_agent.py   # or on stdin
python3 configure_allocate_or_assign_software_licenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate or assign software licenses Configuration Bulk Setup — Bulk-applies software license allocation/assignment changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies and emits before/after c

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-allocate-or-assign-software-licenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_allocate_or_assign_software_licenses',
    "version": '3.0.3',
    "display_name": 'Allocate or assign software licenses Configuration Bulk Setup',
    "description": 'Bulk-applies software license allocation/assignment changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies and emits before/after c',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-allocate-or-assign-software-licenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-allocate-or-assign-software-licenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '22251dda2f9bd2fc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/allocate-or-assign-software-licenses'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-allocate-or-assign-software-licenses', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, before changes are applied.', 'configuration_excel': 'Attached Excel file with one row per license allocation/assignment target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for allocate or assign software licenses, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per allocate or assign software licenses target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-applies software license allocation/assignment changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies and emits before/after c', 'example_request': 'Bulk-assign software licenses in USMF sandbox from this Excel file - validate first and show me before I approve.', 'inputs': [{'description': 'Attached Excel file with one row per license allocation/assignment target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against (e.g. USMF); sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit user approval after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user has an Excel file of license allocation/assignment rows to bulk-apply in D365 F&SCM and wants validation plus approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureAllocateOrAssignSoftwareLicenses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAllocateOrAssignSoftwareLicenses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Attached Excel file with one row per license allocation/assignment target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureAllocateOrAssignSoftwareLicenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
