---
name: "rar-cowork-cookbook-configure-classify-assets"
description: "Validates an attached Excel file of classify-assets configuration rows against Dynamics 365 F&SCM via the ERP plugin, returns a validation workbook, then after your approval applies the changes and emits a before/after c"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_classify_assets", "rar_sha256": "00dc49fe8f2d962c39cd8bbfba4f9adbae26f00e3636adbfe6240c63533731dc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
