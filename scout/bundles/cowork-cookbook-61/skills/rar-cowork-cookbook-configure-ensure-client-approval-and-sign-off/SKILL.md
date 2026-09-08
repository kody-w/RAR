---
name: "rar-cowork-cookbook-configure-ensure-client-approval-and-sign-off"
description: "Validates an attached Excel file of client approval/sign-off configuration rows against Dynamics 365 F&SCM (legal entity USMF), returns a validation workbook, then after your approval applies the changes and returns a be"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_ensure_client_approval_and_sign_off", "rar_sha256": "6ee04721ce0b155fb87a5130f26f9d169101cb38fe05411c75c235f82219f3d4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
