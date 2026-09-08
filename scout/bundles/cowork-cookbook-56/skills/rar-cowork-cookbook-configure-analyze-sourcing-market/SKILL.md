---
name: "rar-cowork-cookbook-configure-analyze-sourcing-market"
description: "Applies a bulk analyze-sourcing-market configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a be"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_sourcing_market", "rar_sha256": "0cac817944228857c9bece93b2e9e3f99957243c8ae546af219a80f6ef16f74c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_analyze_sourcing_market`. The original RAPP
agent is preserved byte-for-byte in `configure_analyze_sourcing_market_agent.py` and in the RCI capsule.

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

Analyze sourcing market Configuration Bulk Setup — Applies a bulk analyze-sourcing-market configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a be

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-sourcing-market
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
      "description": "Explicit user approval after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per analyze sourcing market target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_sourcing_market_agent.py` and embedded as the fenced Python below (sha256 0cac817944228857…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_sourcing_market_agent.py` first:

```bash
python3 configure_analyze_sourcing_market_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_sourcing_market_agent.py   # or on stdin
python3 configure_analyze_sourcing_market_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze sourcing market Configuration Bulk Setup — Applies a bulk analyze-sourcing-market configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a be

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-sourcing-market
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_sourcing_market',
    "version": '3.0.3',
    "display_name": 'Analyze sourcing market Configuration Bulk Setup',
    "description": 'Applies a bulk analyze-sourcing-market configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a be',
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
        "upstream_slug": 'configure-analyze-sourcing-market',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-sourcing-market',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '478ec18d29c0078e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/develop-procurement-and-sourcing-strategy/analyze-sourcing-market'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-analyze-sourcing-market', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per analyze sourcing market target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for analyze sourcing market, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per analyze sourcing market target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk analyze-sourcing-market configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a be', 'example_request': "Here's my sourcing config spreadsheet — validate it against USMF sandbox and show me what would change before applying.", 'inputs': [{'description': 'Attached Excel file with one row per analyze sourcing market target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user has an Excel file of analyze sourcing market configuration rows to validate and bulk-apply in D365 F&SCM, with approval and before/after output.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureAnalyzeSourcingMarket(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeSourcingMarket'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per analyze sourcing market target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureAnalyzeSourcingMarket().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
