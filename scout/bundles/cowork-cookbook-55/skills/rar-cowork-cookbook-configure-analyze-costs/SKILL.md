---
name: "rar-cowork-cookbook-configure-analyze-costs"
description: "Applies bulk analyze-costs configuration changes in Dynamics 365 F&SCM from an input Excel file: validates every row, emits a validation workbook, pauses for your approval, then applies changes with a before/after confir"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_costs", "rar_sha256": "f710c0f0251218eb9ef8998294514c6ef4ccdd5fa86dd2ff6cbfb505f3778b35", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
