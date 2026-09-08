---
name: "rar-cowork-cookbook-configure-create-a-case-manually"
description: "Bulk-creates cases in Dynamics 365 F&SCM from an attached configuration Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after confirmatio"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_create_a_case_manually", "rar_sha256": "4731130f8e8ffc172ef31632c3621462cfc7f7a413900da631fedefbb2086ccd", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
