---
name: "rar-cowork-cookbook-configure-recognize-project-revenue"
description: "Reads an attached Excel file of recognize-project-revenue configuration rows against a Dynamics 365 legal entity, returns a validation workbook of pass/fail rows, and after your approval applies the changes and returns a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_recognize_project_revenue", "rar_sha256": "0835d197b34cd9da0a50bde802b11374a1601bbb841d8831b2b7df3a48fdff36", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
