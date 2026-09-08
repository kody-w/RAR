---
name: "rar-cowork-cookbook-configure-depreciate-assets"
description: "Reads an attached Excel file of depreciate-assets configuration changes for a D365 F&SCM legal entity, validates every row, emits a validation workbook, waits for approval, then applies changes with a before/after confir"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_depreciate_assets", "rar_sha256": "9cd3ac03ec9762e3126ac9bdc2a93ff4f79cdf1f04efa16e25c921ceac3ce037", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_depreciate_assets`. The original RAPP
agent is preserved byte-for-byte in `configure_depreciate_assets_agent.py` and in the RCI capsule.

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

Depreciate assets Configuration Bulk Setup — Reads an attached Excel file of depreciate-assets configuration changes for a D365 F&SCM legal entity, validates every row, emits a validation workbook, waits for approval, then applies changes with a before/after confir

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-depreciate-assets
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
      "description": "Explicit user approval after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per depreciate assets target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; use a sandbox environment first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_depreciate_assets_agent.py` and embedded as the fenced Python below (sha256 9cd3ac03ec9762e3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_depreciate_assets_agent.py` first:

```bash
python3 configure_depreciate_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_depreciate_assets_agent.py   # or on stdin
python3 configure_depreciate_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Depreciate assets Configuration Bulk Setup — Reads an attached Excel file of depreciate-assets configuration changes for a D365 F&SCM legal entity, validates every row, emits a validation workbook, waits for approval, then applies changes with a before/after confir

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-depreciate-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_depreciate_assets',
    "version": '3.0.3',
    "display_name": 'Depreciate assets Configuration Bulk Setup',
    "description": 'Reads an attached Excel file of depreciate-assets configuration changes for a D365 F&SCM legal entity, validates every row, emits a validation workbook, waits for approval, then applies changes with a before/after confir',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-depreciate-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-depreciate-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f8814a0be76e3761',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/depreciate-assets'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/configure-depreciate-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per depreciate assets target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for depreciate assets, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per depreciate assets target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached Excel file of depreciate-assets configuration changes for a D365 F&SCM legal entity, validates every row, emits a validation workbook, waits for approval, then applies changes with a before/after confir', 'example_request': "Here's my depreciation config spreadsheet — validate it against USMF sandbox and show me what would fail before applying.", 'inputs': [{'description': 'Attached Excel file with one row per depreciate assets target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to bulk-apply depreciate assets configuration changes from a spreadsheet in Dynamics 365 F&SCM with dry-run validation and approval before writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureDepreciateAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDepreciateAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per depreciate assets target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureDepreciateAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
