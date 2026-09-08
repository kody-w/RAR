---
name: "rar-cowork-cookbook-configure-model-service-capacity"
description: "Bulk-updates model service capacity records in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, pauses for your approval, then applies changes and emits a before/after con"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_model_service_capacity", "rar_sha256": "5b8aa79e426af6b71fd4f00f3107c1373736d82f2cb99ae90af13cceac4d155c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_model_service_capacity`. The original RAPP
agent is preserved byte-for-byte in `configure_model_service_capacity_agent.py` and in the RCI capsule.

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

Model service capacity Configuration Bulk Setup — Bulk-updates model service capacity records in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, pauses for your approval, then applies changes and emits a before/after con

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-model-service-capacity
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
    "config_excel_file": {
      "description": "Attached Excel file with one row per model service capacity target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF); use a sandbox environment first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_model_service_capacity_agent.py` and embedded as the fenced Python below (sha256 5b8aa79e426af6b7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_model_service_capacity_agent.py` first:

```bash
python3 configure_model_service_capacity_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_model_service_capacity_agent.py   # or on stdin
python3 configure_model_service_capacity_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Model service capacity Configuration Bulk Setup — Bulk-updates model service capacity records in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, pauses for your approval, then applies changes and emits a before/after con

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-model-service-capacity
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_model_service_capacity',
    "version": '3.0.3',
    "display_name": 'Model service capacity Configuration Bulk Setup',
    "description": 'Bulk-updates model service capacity records in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, pauses for your approval, then applies changes and emits a before/after con',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-model-service-capacity',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-model-service-capacity',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e71f21a240ed19b5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/plan-service-work/model-service-capacity'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/configure-model-service-capacity', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'config_excel_file': 'Attached Excel file with one row per model service capacity target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for model service capacity, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per model service capacity target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-updates model service capacity records in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, pauses for your approval, then applies changes and emits a before/after con', 'example_request': 'Bulk update model service capacity in USMF sandbox from this Excel file — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per model service capacity target and the new field values.', 'name': 'config_excel_file'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to apply bulk field changes to model service capacity records in D365 from a spreadsheet, with dry-run validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureModelServiceCapacity(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureModelServiceCapacity'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'config_excel_file': {'description': 'Attached Excel file with one row per model service capacity target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureModelServiceCapacity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
