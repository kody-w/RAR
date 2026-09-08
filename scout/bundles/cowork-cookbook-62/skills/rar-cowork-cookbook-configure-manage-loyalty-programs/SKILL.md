---
name: "rar-cowork-cookbook-configure-manage-loyalty-programs"
description: "Bulk-updates loyalty program configuration in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and emits a before/after confirma"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_loyalty_programs", "rar_sha256": "577dc432d821005a4835393be218ae1f89ceb738cdf40be36a56d9cf74490e82", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_loyalty_programs`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_loyalty_programs_agent.py` and in the RCI capsule.

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

Manage loyalty programs Configuration Bulk Setup — Bulk-updates loyalty program configuration in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and emits a before/after confirma

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-loyalty-programs
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
      "description": "Explicit go-ahead after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel": {
      "description": "Excel file with one row per loyalty program target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Sandbox or production target; sandbox first is required.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_loyalty_programs_agent.py` and embedded as the fenced Python below (sha256 577dc432d821005a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_loyalty_programs_agent.py` first:

```bash
python3 configure_manage_loyalty_programs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_loyalty_programs_agent.py   # or on stdin
python3 configure_manage_loyalty_programs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage loyalty programs Configuration Bulk Setup — Bulk-updates loyalty program configuration in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and emits a before/after confirma

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-loyalty-programs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_loyalty_programs',
    "version": '3.0.3',
    "display_name": 'Manage loyalty programs Configuration Bulk Setup',
    "description": 'Bulk-updates loyalty program configuration in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and emits a before/after confirma',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-manage-loyalty-programs',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-loyalty-programs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ee4ca4f029776892',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/manage-loyalty-programs'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/configure-manage-loyalty-programs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel': 'Excel file with one row per loyalty program target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Sandbox or production target; sandbox first is required.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for manage loyalty programs, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per manage loyalty programs target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-updates loyalty program configuration in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and emits a before/after confirma', 'example_request': 'Bulk-update our loyalty programs in USMF sandbox from this Excel file - validate first and show me before I approve.', 'inputs': [{'description': 'Excel file with one row per loyalty program target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Sandbox or production target; sandbox first is required.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to apply many loyalty program config changes at once from a spreadsheet, with pre-validation, an approval pause, and before/after evidence.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureManageLoyaltyPrograms(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageLoyaltyPrograms'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Excel file with one row per loyalty program target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Sandbox or production target; sandbox first is required.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureManageLoyaltyPrograms().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
