---
name: "rar-cowork-cookbook-configure-maintain-fixed-assets"
description: "Reads an attached Excel file of fixed-asset configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, then applies approved changes with a before/after confirmation workbook"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_maintain_fixed_assets", "rar_sha256": "450bbfeb2f55c144bb012c91fc16d13ffd536368e6ed8c5f7362c99dce4d5227", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
