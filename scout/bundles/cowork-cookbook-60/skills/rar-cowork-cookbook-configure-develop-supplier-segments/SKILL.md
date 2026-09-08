---
name: "rar-cowork-cookbook-configure-develop-supplier-segments"
description: "Bulk-applies supplier segment configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a befor"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_supplier_segments", "rar_sha256": "836e406d4652da2614df9028ff5227d3b10c655592ba38257bd1dddc272f5943", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_develop_supplier_segments`. The original RAPP
agent is preserved byte-for-byte in `configure_develop_supplier_segments_agent.py` and in the RCI capsule.

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

Develop supplier segments Configuration Bulk Setup — Bulk-applies supplier segment configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a befor

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-supplier-segments
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
      "description": "Explicit go-ahead after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per supplier segment target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Which environment to target; sandbox first before production.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_supplier_segments_agent.py` and embedded as the fenced Python below (sha256 836e406d4652da26…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_supplier_segments_agent.py` first:

```bash
python3 configure_develop_supplier_segments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_develop_supplier_segments_agent.py   # or on stdin
python3 configure_develop_supplier_segments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop supplier segments Configuration Bulk Setup — Bulk-applies supplier segment configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a befor

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-supplier-segments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_develop_supplier_segments',
    "version": '3.0.3',
    "display_name": 'Develop supplier segments Configuration Bulk Setup',
    "description": 'Bulk-applies supplier segment configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a befor',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-develop-supplier-segments',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-develop-supplier-segments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '87421a63e87bc422',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/develop-supplier-segments'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-develop-supplier-segments', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per supplier segment target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Which environment to target; sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for develop supplier segments, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per develop supplier segments target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-applies supplier segment configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a befor', 'example_request': 'Run the supplier segment bulk config setup on USMF sandbox using my attached Excel file — validate first.', 'inputs': [{'description': 'Attached Excel file with one row per supplier segment target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Which environment to target; sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you have an Excel file of supplier segment config changes to apply in bulk to a D365 legal entity and need row-level validation plus an approval gate.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureDevelopSupplierSegments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDevelopSupplierSegments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per supplier segment target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Which environment to target; sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureDevelopSupplierSegments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
