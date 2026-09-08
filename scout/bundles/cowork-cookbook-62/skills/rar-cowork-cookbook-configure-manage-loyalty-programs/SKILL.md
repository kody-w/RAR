---
name: "rar-cowork-cookbook-configure-manage-loyalty-programs"
description: "Bulk-updates loyalty program configuration in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and emits a before/after confirma"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_loyalty_programs", "rar_sha256": "577dc432d821005a4835393be218ae1f89ceb738cdf40be36a56d9cf74490e82", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
