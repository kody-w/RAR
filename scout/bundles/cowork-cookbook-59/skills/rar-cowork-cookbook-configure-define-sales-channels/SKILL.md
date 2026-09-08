---
name: "rar-cowork-cookbook-configure-define-sales-channels"
description: "Reads an attached Excel file of sales channel configuration rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a be"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_sales_channels", "rar_sha256": "f250c4e4f77b044964361601a0e61bc10eee266b93dc2a683b8fefc310966e56", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_define_sales_channels`. The original RAPP
agent is preserved byte-for-byte in `configure_define_sales_channels_agent.py` and in the RCI capsule.

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

Define sales channels Configuration Bulk Setup — Reads an attached Excel file of sales channel configuration rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a be

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-sales-channels
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
      "description": "Your explicit go-ahead after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached workbook with one row per sales channel target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; the recipe uses USMF, sandbox first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_sales_channels_agent.py` and embedded as the fenced Python below (sha256 f250c4e4f77b0449…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_sales_channels_agent.py` first:

```bash
python3 configure_define_sales_channels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_define_sales_channels_agent.py   # or on stdin
python3 configure_define_sales_channels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define sales channels Configuration Bulk Setup — Reads an attached Excel file of sales channel configuration rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a be

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-sales-channels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_define_sales_channels',
    "version": '3.0.3',
    "display_name": 'Define sales channels Configuration Bulk Setup',
    "description": 'Reads an attached Excel file of sales channel configuration rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a be',
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
        "upstream_slug": 'configure-define-sales-channels',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-define-sales-channels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4d5ad80b07aa5e36',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/define-sales-channels'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/configure-define-sales-channels', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Your explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_excel_file': 'Attached workbook with one row per sales channel target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; the recipe uses USMF, sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for define sales channels, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per define sales channels target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached Excel file of sales channel configuration rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a be', 'example_request': 'Bulk-define sales channels in USMF sandbox from this Excel file — validate first and show me the dry run before applying.', 'inputs': [{'description': 'Attached workbook with one row per sales channel target and the new field values.', 'name': 'configuration Excel file'}, {'description': 'D365 legal entity to run against; the recipe uses USMF, sandbox first.', 'name': 'legal entity'}, {'description': 'Your explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to bulk-define or update sales channels in D365 from a spreadsheet, with dry-run validation and explicit approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureDefineSalesChannels(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDefineSalesChannels'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Your explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached workbook with one row per sales channel target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; the recipe uses USMF, sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureDefineSalesChannels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
