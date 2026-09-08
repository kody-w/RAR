---
name: "rar-cowork-cookbook-configure-analyze-account-payable"
description: "Reads an attached Excel file of accounts payable configuration rows for a D365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after confi"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_account_payable", "rar_sha256": "394c0bf9edd1b580559b775950303e69ae02c8b7e34b6217c1cc458c485b443f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
