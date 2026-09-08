---
name: "rar-cowork-cookbook-configure-develop-supplier-segments"
description: "Bulk-applies supplier segment configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a befor"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_supplier_segments", "rar_sha256": "836e406d4652da2614df9028ff5227d3b10c655592ba38257bd1dddc272f5943", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
