---
name: "rar-cowork-cookbook-configure-use-similar-cases-to-find-a-solution"
description: "Runs a bulk 'use similar cases to find a solution' configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_use_similar_cases_to_find_a_solution", "rar_sha256": "aee4a8a9cae26e87a5cb30a386d48ef09eeef7f25b92951ba786999a86381494", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_use_similar_cases_to_find_a_solution`. The original RAPP
agent is preserved byte-for-byte in `configure_use_similar_cases_to_find_a_solution_agent.py` and in the RCI capsule.

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

Use similar cases to find a solution Configuration Bulk Setup — Runs a bulk 'use similar cases to find a solution' configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-use-similar-cases-to-find-a-solution
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
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF); use a sandbox first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_use_similar_cases_to_find_a_solution_agent.py` and embedded as the fenced Python below (sha256 aee4a8a9cae26e87…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_use_similar_cases_to_find_a_solution_agent.py` first:

```bash
python3 configure_use_similar_cases_to_find_a_solution_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_use_similar_cases_to_find_a_solution_agent.py   # or on stdin
python3 configure_use_similar_cases_to_find_a_solution_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Use similar cases to find a solution Configuration Bulk Setup — Runs a bulk 'use similar cases to find a solution' configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-use-similar-cases-to-find-a-solution
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_use_similar_cases_to_find_a_solution',
    "version": '3.0.3',
    "display_name": 'Use similar cases to find a solution Configuration Bulk Setup',
    "description": "Runs a bulk 'use similar cases to find a solution' configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes",
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
        "upstream_slug": 'configure-use-similar-cases-to-find-a-solution',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-use-similar-cases-to-find-a-solution',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7a8c460a54512fc8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/use-similar-cases-to-find-a-solution'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/configure-use-similar-cases-to-find-a-solution', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for use similar cases to find a solution, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per use similar cases to find a solution target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Runs a bulk 'use similar cases to find a solution' configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes", 'example_request': 'Bulk-apply the config changes in this Excel to USMF sandbox — validate first and show me the results before writing.', 'inputs': [{'description': 'Attached Excel file with one row per target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.', 'name': 'legal_entity'}, {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to apply bulk configuration updates to Dynamics 365 F&SCM from a spreadsheet with a dry-run validation pass and approval gate before writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureUseSimilarCasesToFindASolution(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureUseSimilarCasesToFindASolution'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureUseSimilarCasesToFindASolution().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
