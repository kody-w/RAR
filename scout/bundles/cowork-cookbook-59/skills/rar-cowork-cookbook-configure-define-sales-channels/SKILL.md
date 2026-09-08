---
name: "rar-cowork-cookbook-configure-define-sales-channels"
description: "Reads an attached Excel file of sales channel configuration rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a be"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_sales_channels", "rar_sha256": "f250c4e4f77b044964361601a0e61bc10eee266b93dc2a683b8fefc310966e56", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
