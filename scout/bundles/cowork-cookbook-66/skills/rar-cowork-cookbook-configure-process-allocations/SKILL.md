---
name: "rar-cowork-cookbook-configure-process-allocations"
description: "Reads an attached configuration Excel file of process allocation targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies changes and return"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_process_allocations", "rar_sha256": "8ad63334ad8ce082abce0d3b49352539279898951f72d6265c74012836e4acb8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_process_allocations`. The original RAPP
agent is preserved byte-for-byte in `configure_process_allocations_agent.py` and in the RCI capsule.

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

Process allocations Configuration Bulk Setup — Reads an attached configuration Excel file of process allocation targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies changes and return

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-process-allocations
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
      "description": "Explicit user approval after reviewing the validation workbook, required before changes are applied.",
      "type": "string"
    },
    "configuration_file": {
      "description": "Excel file with one row per process allocations target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment \u2014 sandbox first before production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; defaults to USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_process_allocations_agent.py` and embedded as the fenced Python below (sha256 8ad63334ad8ce082…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_process_allocations_agent.py` first:

```bash
python3 configure_process_allocations_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_process_allocations_agent.py   # or on stdin
python3 configure_process_allocations_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process allocations Configuration Bulk Setup — Reads an attached configuration Excel file of process allocation targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies changes and return

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-process-allocations
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_process_allocations',
    "version": '3.0.3',
    "display_name": 'Process allocations Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of process allocation targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies changes and return',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-process-allocations',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-process-allocations',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '133b1d3257617d6e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/process-allocations'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-process-allocations', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, required before changes are applied.', 'configuration_file': 'Excel file with one row per process allocations target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment — sandbox first before production.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for process allocations, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per process allocations target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of process allocation targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies changes and return', 'example_request': 'Bulk-update our process allocations in USMF sandbox from this config spreadsheet — validate first and show me before/after.', 'inputs': [{'description': 'Excel file with one row per process allocations target and the new field values.', 'name': 'configuration_file'}, {'description': 'D365 legal entity to run against; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Target environment — sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit user approval after reviewing the validation workbook, required before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to bulk-update process allocation configuration in D365 F&SCM from a spreadsheet, with row validation and an approval gate before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureProcessAllocations(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureProcessAllocations'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, required before changes are applied.', 'type': 'string'}, 'configuration_file': {'description': 'Excel file with one row per process allocations target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment — sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureProcessAllocations().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
