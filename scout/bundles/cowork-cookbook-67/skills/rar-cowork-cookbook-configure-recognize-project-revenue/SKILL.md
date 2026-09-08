---
name: "rar-cowork-cookbook-configure-recognize-project-revenue"
description: "Reads an attached Excel file of recognize-project-revenue configuration rows against a Dynamics 365 legal entity, returns a validation workbook of pass/fail rows, and after your approval applies the changes and returns a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_recognize_project_revenue", "rar_sha256": "0835d197b34cd9da0a50bde802b11374a1601bbb841d8831b2b7df3a48fdff36", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_recognize_project_revenue`. The original RAPP
agent is preserved byte-for-byte in `configure_recognize_project_revenue_agent.py` and in the RCI capsule.

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

Recognize project revenue Configuration Bulk Setup — Reads an attached Excel file of recognize-project-revenue configuration rows against a Dynamics 365 legal entity, returns a validation workbook of pass/fail rows, and after your approval applies the changes and returns a

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-recognize-project-revenue
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
    "configuration_file": {
      "description": "Excel file with one row per recognize project revenue target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; use a sandbox first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_recognize_project_revenue_agent.py` and embedded as the fenced Python below (sha256 0835d197b34cd9da…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_recognize_project_revenue_agent.py` first:

```bash
python3 configure_recognize_project_revenue_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_recognize_project_revenue_agent.py   # or on stdin
python3 configure_recognize_project_revenue_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Recognize project revenue Configuration Bulk Setup — Reads an attached Excel file of recognize-project-revenue configuration rows against a Dynamics 365 legal entity, returns a validation workbook of pass/fail rows, and after your approval applies the changes and returns a

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-recognize-project-revenue
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_recognize_project_revenue',
    "version": '3.0.3',
    "display_name": 'Recognize project revenue Configuration Bulk Setup',
    "description": 'Reads an attached Excel file of recognize-project-revenue configuration rows against a Dynamics 365 legal entity, returns a validation workbook of pass/fail rows, and after your approval applies the changes and returns a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-recognize-project-revenue',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-recognize-project-revenue',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '03a88cd9e4926e13',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-financials/recognize-project-revenue'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/configure-recognize-project-revenue', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_file': 'Excel file with one row per recognize project revenue target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for recognize project revenue, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per recognize project revenue target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached Excel file of recognize-project-revenue configuration rows against a Dynamics 365 legal entity, returns a validation workbook of pass/fail rows, and after your approval applies the changes and returns a', 'example_request': 'Bulk update recognize project revenue config in USMF sandbox from this Excel file - validate first and show me before I approve.', 'inputs': [{'description': 'Excel file with one row per recognize project revenue target and the new field values.', 'name': 'configuration_file'}, {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.', 'name': 'legal_entity'}, {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to bulk-update recognize project revenue configuration in Dynamics 365 F&SCM from a spreadsheet, with dry-run validation and explicit approval before writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureRecognizeProjectRevenue(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureRecognizeProjectRevenue'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_file': {'description': 'Excel file with one row per recognize project revenue target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureRecognizeProjectRevenue().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
