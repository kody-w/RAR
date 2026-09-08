---
name: "rar-cowork-cookbook-configure-allocate-or-assign-software-licenses"
description: "Bulk-applies software license allocation/assignment changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies and emits before/after c"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_allocate_or_assign_software_licenses", "rar_sha256": "934e6550551f49f26f32ce5f94791d6331d7594b5e3d38cdbec5014eb0645261", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
