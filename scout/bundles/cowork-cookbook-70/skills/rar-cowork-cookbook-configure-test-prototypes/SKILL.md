---
name: "rar-cowork-cookbook-configure-test-prototypes"
description: "Reads an attached configuration Excel file of test prototype targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies changes and return"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_test_prototypes", "rar_sha256": "e557ecafa5d9da0f51cb69a90c9ab7be0523d5f11634dc5e4baca0b1b3b4740c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_test_prototypes`. The original RAPP
agent is preserved byte-for-byte in `configure_test_prototypes_agent.py` and in the RCI capsule.

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

Test prototypes Configuration Bulk Setup — Reads an attached configuration Excel file of test prototype targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies changes and return

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-test-prototypes
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
      "description": "Explicit user approval after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per test prototype target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment; sandbox first before production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_test_prototypes_agent.py` and embedded as the fenced Python below (sha256 e557ecafa5d9da0f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_test_prototypes_agent.py` first:

```bash
python3 configure_test_prototypes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_test_prototypes_agent.py   # or on stdin
python3 configure_test_prototypes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Test prototypes Configuration Bulk Setup — Reads an attached configuration Excel file of test prototype targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies changes and return

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-test-prototypes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_test_prototypes',
    "version": '3.0.3',
    "display_name": 'Test prototypes Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of test prototype targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies changes and return',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-test-prototypes',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-test-prototypes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f26e68093cbf2d1e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/test-prototypes'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/configure-test-prototypes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, before changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per test prototype target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox first before production.', 'legal_entity': 'D365 legal entity to run against (USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for test prototypes, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per test prototypes target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of test prototype targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies changes and return', 'example_request': 'Bulk-update test prototype config in USMF sandbox from this Excel file — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per test prototype target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against (USMF).', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit user approval after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-update test prototype configuration fields in D365 F&SCM from a spreadsheet, with row validation and an approval gate before any writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureTestPrototypes(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureTestPrototypes'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per test prototype target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureTestPrototypes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
