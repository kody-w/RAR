---
name: "rar-cowork-cookbook-configure-ensure-client-approval-and-sign-off"
description: "Validates an attached Excel file of client approval/sign-off configuration rows against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then after your approval applies the changes and returns a be"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_ensure_client_approval_and_sign_off", "rar_sha256": "6ee04721ce0b155fb87a5130f26f9d169101cb38fe05411c75c235f82219f3d4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_ensure_client_approval_and_sign_off`. The original RAPP
agent is preserved byte-for-byte in `configure_ensure_client_approval_and_sign_off_agent.py` and in the RCI capsule.

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

Ensure client approval and sign-off Configuration Bulk Setup — Validates an attached Excel file of client approval/sign-off configuration rows against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then after your approval applies the changes and returns a be

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-ensure-client-approval-and-sign-off
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
    "approval_confirmation": {
      "description": "Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per approval/sign-off target and the new field values.",
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
      "description": "D365 legal entity to run against (default USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_ensure_client_approval_and_sign_off_agent.py` and embedded as the fenced Python below (sha256 6ee04721ce0b155f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_ensure_client_approval_and_sign_off_agent.py` first:

```bash
python3 configure_ensure_client_approval_and_sign_off_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_ensure_client_approval_and_sign_off_agent.py   # or on stdin
python3 configure_ensure_client_approval_and_sign_off_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Ensure client approval and sign-off Configuration Bulk Setup — Validates an attached Excel file of client approval/sign-off configuration rows against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then after your approval applies the changes and returns a be

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-ensure-client-approval-and-sign-off
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_ensure_client_approval_and_sign_off',
    "version": '3.0.3',
    "display_name": 'Ensure client approval and sign-off Configuration Bulk Setup',
    "description": 'Validates an attached Excel file of client approval/sign-off configuration rows against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then after your approval applies the changes and returns a be',
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
        "upstream_slug": 'configure-ensure-client-approval-and-sign-off',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-ensure-client-approval-and-sign-off',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8f53458923555f26',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/ensure-client-approval-and-sign-off'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/configure-ensure-client-approval-and-sign-off', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval_confirmation': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per approval/sign-off target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox first before production.', 'legal_entity': 'D365 legal entity to run against (default USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for ensure client approval and sign-off, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per ensure client approval and sign-off target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Validates an attached Excel file of client approval/sign-off configuration rows against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then after your approval applies the changes and returns a be', 'example_request': 'Run the bulk client approval sign-off config setup on this Excel in USMF sandbox — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per approval/sign-off target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against (default USMF).', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox first before production.', 'name': 'environment'}, {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval_confirmation'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to bulk-apply client approval and sign-off configuration changes in D365 F&SCM from a spreadsheet, with dry-run validation and explicit approval first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureEnsureClientApprovalAndSignOff(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureEnsureClientApprovalAndSignOff'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval_confirmation': {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per approval/sign-off target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureEnsureClientApprovalAndSignOff().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
