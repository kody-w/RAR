---
name: "rar-cowork-cookbook-configure-analyze-costs"
description: "Applies bulk analyze-costs configuration changes in Dynamics 365 F&SCM from an input Excel file: validates every row, emits a validation workbook, pauses for your approval, then applies changes with a before/after confir"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_costs", "rar_sha256": "f710c0f0251218eb9ef8998294514c6ef4ccdd5fa86dd2ff6cbfb505f3778b35", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_analyze_costs`. The original RAPP
agent is preserved byte-for-byte in `configure_analyze_costs_agent.py` and in the RCI capsule.

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

Analyze costs Configuration Bulk Setup — Applies bulk analyze-costs configuration changes in Dynamics 365 F&SCM from an input Excel file: validates every row, emits a validation workbook, pauses for your approval, then applies changes with a before/after confir

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-costs
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
    "configuration_excel": {
      "description": "Excel file with one row per analyze costs target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF); use a sandbox first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_costs_agent.py` and embedded as the fenced Python below (sha256 f710c0f0251218eb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_costs_agent.py` first:

```bash
python3 configure_analyze_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_costs_agent.py   # or on stdin
python3 configure_analyze_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze costs Configuration Bulk Setup — Applies bulk analyze-costs configuration changes in Dynamics 365 F&SCM from an input Excel file: validates every row, emits a validation workbook, pauses for your approval, then applies changes with a before/after confir

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_costs',
    "version": '3.0.3',
    "display_name": 'Analyze costs Configuration Bulk Setup',
    "description": 'Applies bulk analyze-costs configuration changes in Dynamics 365 F&SCM from an input Excel file: validates every row, emits a validation workbook, pauses for your approval, then applies changes with a before/after confir',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-analyze-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '504dd220d3ae2901',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/analyze-costs'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-analyze-costs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_excel': 'Excel file with one row per analyze costs target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for analyze costs, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per analyze costs target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies bulk analyze-costs configuration changes in Dynamics 365 F&SCM from an input Excel file: validates every row, emits a validation workbook, pauses for your approval, then applies changes with a before/after confir', 'example_request': 'Run the analyze costs bulk config update in USMF sandbox from this Excel file — validate first and let me approve.', 'inputs': [{'description': 'Excel file with one row per analyze costs target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to bulk-update analyze costs configuration in D365 F&SCM from a spreadsheet, with row-level validation and an approval gate before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureAnalyzeCosts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeCosts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Excel file with one row per analyze costs target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureAnalyzeCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
