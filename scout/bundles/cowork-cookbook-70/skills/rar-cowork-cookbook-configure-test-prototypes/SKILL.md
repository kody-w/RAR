---
name: "rar-cowork-cookbook-configure-test-prototypes"
description: "Reads an attached configuration Excel file of test prototype targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies changes and return"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_test_prototypes", "rar_sha256": "e557ecafa5d9da0f51cb69a90c9ab7be0523d5f11634dc5e4baca0b1b3b4740c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
