---
name: "rar-cowork-cookbook-configure-model-service-capacity"
description: "Bulk-updates model service capacity records in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, pauses for your approval, then applies changes and emits a before/after con"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_model_service_capacity", "rar_sha256": "5b8aa79e426af6b71fd4f00f3107c1373736d82f2cb99ae90af13cceac4d155c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
