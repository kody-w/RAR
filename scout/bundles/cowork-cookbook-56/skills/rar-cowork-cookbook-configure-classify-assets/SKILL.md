---
name: "rar-cowork-cookbook-configure-classify-assets"
description: "Validates an attached Excel file of classify-assets configuration rows against Dynamics 365 F&SCM via the ERP plugin, returns a validation workbook, then after your approval applies the changes and emits a before/after c"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_classify_assets", "rar_sha256": "00dc49fe8f2d962c39cd8bbfba4f9adbae26f00e3636adbfe6240c63533731dc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_classify_assets`. The original RAPP
agent is preserved byte-for-byte in `configure_classify_assets_agent.py` and in the RCI capsule.

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

Classify assets Configuration Bulk Setup — Validates an attached Excel file of classify-assets configuration rows against Dynamics 365 F&SCM via the ERP plugin, returns a validation workbook, then after your approval applies the changes and emits a before/after c

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-classify-assets
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
      "description": "Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel": {
      "description": "Attached Excel file with one row per classify assets target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_classify_assets_agent.py` and embedded as the fenced Python below (sha256 00dc49fe8f2d962c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_classify_assets_agent.py` first:

```bash
python3 configure_classify_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_classify_assets_agent.py   # or on stdin
python3 configure_classify_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Classify assets Configuration Bulk Setup — Validates an attached Excel file of classify-assets configuration rows against Dynamics 365 F&SCM via the ERP plugin, returns a validation workbook, then after your approval applies the changes and emits a before/after c

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-classify-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_classify_assets',
    "version": '3.0.3',
    "display_name": 'Classify assets Configuration Bulk Setup',
    "description": 'Validates an attached Excel file of classify-assets configuration rows against Dynamics 365 F&SCM via the ERP plugin, returns a validation workbook, then after your approval applies the changes and emits a before/after c',
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
        "upstream_slug": 'configure-classify-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-classify-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '93d277b281ed0913',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/define-asset-strategy/classify-assets'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/configure-classify-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel': 'Attached Excel file with one row per classify assets target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for classify assets, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per classify assets target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Validates an attached Excel file of classify-assets configuration rows against Dynamics 365 F&SCM via the ERP plugin, returns a validation workbook, then after your approval applies the changes and emits a before/after c', 'example_request': 'Run the classify assets bulk config from this Excel against USMF sandbox — validate first and show me the dry run before applying.', 'inputs': [{'description': 'Attached Excel file with one row per classify assets target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when bulk-applying classify assets configuration changes in D365 F&SCM from a spreadsheet, with dry-run validation and explicit approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureClassifyAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureClassifyAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Attached Excel file with one row per classify assets target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureClassifyAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
