---
name: "rar-cowork-cookbook-configure-use-similar-cases-to-find-a-solution"
description: "Runs a bulk 'use similar cases to find a solution' configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_use_similar_cases_to_find_a_solution", "rar_sha256": "aee4a8a9cae26e87a5cb30a386d48ef09eeef7f25b92951ba786999a86381494", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
