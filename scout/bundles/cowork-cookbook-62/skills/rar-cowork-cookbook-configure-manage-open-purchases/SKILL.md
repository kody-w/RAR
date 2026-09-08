---
name: "rar-cowork-cookbook-configure-manage-open-purchases"
description: "Reads an attached configuration Excel file of open-purchase changes in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for approval, then applies changes with a before/af"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_open_purchases", "rar_sha256": "d8f79da03c2b620218d304f655f9fc98a933bf36355e67b41374d33c1ed08f60", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_open_purchases`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_open_purchases_agent.py` and in the RCI capsule.

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

Manage open purchases Configuration Bulk Setup — Reads an attached configuration Excel file of open-purchase changes in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for approval, then applies changes with a before/af

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-open-purchases
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
      "description": "Explicit go-ahead after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_file": {
      "description": "Excel file with one row per manage-open-purchases target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF); use sandbox first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_open_purchases_agent.py` and embedded as the fenced Python below (sha256 d8f79da03c2b6202…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_open_purchases_agent.py` first:

```bash
python3 configure_manage_open_purchases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_open_purchases_agent.py   # or on stdin
python3 configure_manage_open_purchases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage open purchases Configuration Bulk Setup — Reads an attached configuration Excel file of open-purchase changes in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for approval, then applies changes with a before/af

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-open-purchases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_open_purchases',
    "version": '3.0.3',
    "display_name": 'Manage open purchases Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of open-purchase changes in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for approval, then applies changes with a before/af',
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
        "upstream_slug": 'configure-manage-open-purchases',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-open-purchases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b55aadcc4bc90773',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/manage-open-purchases'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-manage-open-purchases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_file': 'Excel file with one row per manage-open-purchases target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for manage open purchases, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per manage open purchases target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of open-purchase changes in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for approval, then applies changes with a before/af', 'example_request': 'Bulk-update our open purchases in USMF sandbox from this config spreadsheet — validate first and show me before I approve.', 'inputs': [{'description': 'Excel file with one row per manage-open-purchases target and the new field values.', 'name': 'configuration_file'}, {'description': 'D365 legal entity to run against (e.g. USMF); use sandbox first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to bulk-update open purchase records in D365 F&SCM from a spreadsheet, with row-level validation and an approval gate before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureManageOpenPurchases(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageOpenPurchases'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_file': {'description': 'Excel file with one row per manage-open-purchases target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureManageOpenPurchases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
