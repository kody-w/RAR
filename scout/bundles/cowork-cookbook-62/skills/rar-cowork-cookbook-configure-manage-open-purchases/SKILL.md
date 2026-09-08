---
name: "rar-cowork-cookbook-configure-manage-open-purchases"
description: "Reads an attached configuration Excel file of open-purchase changes in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for approval, then applies changes with a before/af"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_open_purchases", "rar_sha256": "d8f79da03c2b620218d304f655f9fc98a933bf36355e67b41374d33c1ed08f60", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
