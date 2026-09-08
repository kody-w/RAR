---
name: "rar-cowork-cookbook-configure-create-a-case-manually"
description: "Bulk-creates cases in Dynamics 365 F&SCM from an attached configuration Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after confirmatio"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_create_a_case_manually", "rar_sha256": "4731130f8e8ffc172ef31632c3621462cfc7f7a413900da631fedefbb2086ccd", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_create_a_case_manually`. The original RAPP
agent is preserved byte-for-byte in `configure_create_a_case_manually_agent.py` and in the RCI capsule.

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

Create a case manually Configuration Bulk Setup — Bulk-creates cases in Dynamics 365 F&SCM from an attached configuration Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after confirmatio

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-create-a-case-manually
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
      "description": "Explicit confirmation after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per case-creation target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment; run sandbox first before production.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_create_a_case_manually_agent.py` and embedded as the fenced Python below (sha256 4731130f8e8ffc17…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_create_a_case_manually_agent.py` first:

```bash
python3 configure_create_a_case_manually_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_create_a_case_manually_agent.py   # or on stdin
python3 configure_create_a_case_manually_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create a case manually Configuration Bulk Setup — Bulk-creates cases in Dynamics 365 F&SCM from an attached configuration Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after confirmatio

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-create-a-case-manually
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_create_a_case_manually',
    "version": '3.0.3',
    "display_name": 'Create a case manually Configuration Bulk Setup',
    "description": 'Bulk-creates cases in Dynamics 365 F&SCM from an attached configuration Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after confirmatio',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-create-a-case-manually',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-create-a-case-manually',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5ebd9b3897cabd96',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/intake-cases/create-a-case-manually'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/configure-create-a-case-manually', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit confirmation after reviewing the validation workbook, before changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per case-creation target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; run sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for create a case manually, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per create a case manually target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-creates cases in Dynamics 365 F&SCM from an attached configuration Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after confirmatio', 'example_request': 'Run the bulk case-creation setup on USMF sandbox using my attached config Excel, and show me the validation results first.', 'inputs': [{'description': 'Attached Excel file with one row per case-creation target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; run sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit confirmation after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to apply a bulk case-creation configuration change in D365 F&SCM from a spreadsheet, with row validation and an approval gate before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureCreateACaseManually(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureCreateACaseManually'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit confirmation after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per case-creation target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; run sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureCreateACaseManually().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
