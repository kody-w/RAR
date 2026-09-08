---
name: "rar-cowork-cookbook-configure-analyze-account-payable"
description: "Reads an attached Excel file of accounts payable configuration rows for a D365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after confi"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_account_payable", "rar_sha256": "394c0bf9edd1b580559b775950303e69ae02c8b7e34b6217c1cc458c485b443f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_analyze_account_payable`. The original RAPP
agent is preserved byte-for-byte in `configure_analyze_account_payable_agent.py` and in the RCI capsule.

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

Analyze account payable Configuration Bulk Setup — Reads an attached Excel file of accounts payable configuration rows for a D365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after confi

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-account-payable
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
      "description": "Attached Excel file with one row per accounts payable target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; use a sandbox environment first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_account_payable_agent.py` and embedded as the fenced Python below (sha256 394c0bf9edd1b580…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_account_payable_agent.py` first:

```bash
python3 configure_analyze_account_payable_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_account_payable_agent.py   # or on stdin
python3 configure_analyze_account_payable_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze account payable Configuration Bulk Setup — Reads an attached Excel file of accounts payable configuration rows for a D365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after confi

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-account-payable
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_account_payable',
    "version": '3.0.3',
    "display_name": 'Analyze account payable Configuration Bulk Setup',
    "description": 'Reads an attached Excel file of accounts payable configuration rows for a D365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after confi',
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
        "upstream_slug": 'configure-analyze-account-payable',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-account-payable',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3ce30c3202b9584f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/analyze-account-payable'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-analyze-account-payable', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per accounts payable target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for analyze account payable, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per analyze account payable target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached Excel file of accounts payable configuration rows for a D365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after confi', 'example_request': 'Bulk-update accounts payable config in USMF sandbox from this Excel file — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per accounts payable target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-apply accounts payable configuration changes in Dynamics 365 F&SCM from a spreadsheet, with dry-run validation and explicit approval before writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureAnalyzeAccountPayable(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeAccountPayable'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per accounts payable target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureAnalyzeAccountPayable().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
