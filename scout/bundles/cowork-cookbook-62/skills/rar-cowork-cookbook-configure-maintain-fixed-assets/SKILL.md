---
name: "rar-cowork-cookbook-configure-maintain-fixed-assets"
description: "Reads an attached Excel file of fixed-asset configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, then applies approved changes with a before/after confirmation workbook"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_maintain_fixed_assets", "rar_sha256": "450bbfeb2f55c144bb012c91fc16d13ffd536368e6ed8c5f7362c99dce4d5227", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_maintain_fixed_assets`. The original RAPP
agent is preserved byte-for-byte in `configure_maintain_fixed_assets_agent.py` and in the RCI capsule.

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

Maintain fixed assets Configuration Bulk Setup — Reads an attached Excel file of fixed-asset configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, then applies approved changes with a before/after confirmation workbook

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-maintain-fixed-assets
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
      "description": "Explicit user approval after reviewing the validation/dry-run workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_file": {
      "description": "Excel file with one row per maintain fixed assets target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment; sandbox first before production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_maintain_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 450bbfeb2f55c144…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_maintain_fixed_assets_agent.py` first:

```bash
python3 configure_maintain_fixed_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_maintain_fixed_assets_agent.py   # or on stdin
python3 configure_maintain_fixed_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain fixed assets Configuration Bulk Setup — Reads an attached Excel file of fixed-asset configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, then applies approved changes with a before/after confirmation workbook

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-maintain-fixed-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_maintain_fixed_assets',
    "version": '3.0.3',
    "display_name": 'Maintain fixed assets Configuration Bulk Setup',
    "description": 'Reads an attached Excel file of fixed-asset configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, then applies approved changes with a before/after confirmation workbook',
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
        "upstream_slug": 'configure-maintain-fixed-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-maintain-fixed-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8bace6c9d02a7655',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/maintain-fixed-assets'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/configure-maintain-fixed-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation/dry-run workbook, before any changes are applied.', 'configuration_file': 'Excel file with one row per maintain fixed assets target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for maintain fixed assets, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per maintain fixed assets target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached Excel file of fixed-asset configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, then applies approved changes with a before/after confirmation workbook', 'example_request': 'Bulk update our fixed assets in USMF sandbox from this config spreadsheet — validate the rows first and show me the preview.', 'inputs': [{'description': 'Excel file with one row per maintain fixed assets target and the new field values.', 'name': 'configuration_file'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit user approval after reviewing the validation/dry-run workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-update maintain fixed assets records in Dynamics 365 F&SCM from a spreadsheet, with row-level validation and an approval gate before writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureMaintainFixedAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureMaintainFixedAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation/dry-run workbook, before any changes are applied.', 'type': 'string'}, 'configuration_file': {'description': 'Excel file with one row per maintain fixed assets target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureMaintainFixedAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
