---
name: "rar-cowork-cookbook-configure-conduct-business-performance-reviews"
description: "Applies bulk configuration changes for business performance review targets in Dynamics 365 F&SCM from an Excel file: validates all rows, emits a validation workbook, waits for approval, then applies and reports before/af"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_conduct_business_performance_reviews", "rar_sha256": "710aa04fd99469d666c123afd8599c5a74b7696daa2cab4e9f6964536f044ec1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_conduct_business_performance_reviews`. The original RAPP
agent is preserved byte-for-byte in `configure_conduct_business_performance_reviews_agent.py` and in the RCI capsule.

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

Conduct business performance reviews Configuration Bulk Setup — Applies bulk configuration changes for business performance review targets in Dynamics 365 F&SCM from an Excel file: validates all rows, emits a validation workbook, waits for approval, then applies and reports before/af

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-conduct-business-performance-reviews
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
      "description": "Explicit user approval after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Excel file with one row per business performance review target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_conduct_business_performance_reviews_agent.py` and embedded as the fenced Python below (sha256 710aa04fd99469d6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_conduct_business_performance_reviews_agent.py` first:

```bash
python3 configure_conduct_business_performance_reviews_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_conduct_business_performance_reviews_agent.py   # or on stdin
python3 configure_conduct_business_performance_reviews_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct business performance reviews Configuration Bulk Setup — Applies bulk configuration changes for business performance review targets in Dynamics 365 F&SCM from an Excel file: validates all rows, emits a validation workbook, waits for approval, then applies and reports before/af

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-conduct-business-performance-reviews
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_conduct_business_performance_reviews',
    "version": '3.0.3',
    "display_name": 'Conduct business performance reviews Configuration Bulk Setup',
    "description": 'Applies bulk configuration changes for business performance review targets in Dynamics 365 F&SCM from an Excel file: validates all rows, emits a validation workbook, waits for approval, then applies and reports before/af',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-conduct-business-performance-reviews',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-conduct-business-performance-reviews',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c049280ab21cefc7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/conduct-business-performance-reviews'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/configure-conduct-business-performance-reviews', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, before changes are applied.', 'configuration_excel_file': 'Excel file with one row per business performance review target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for conduct business performance reviews, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per conduct business performance reviews target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies bulk configuration changes for business performance review targets in Dynamics 365 F&SCM from an Excel file: validates all rows, emits a validation workbook, waits for approval, then applies and reports before/af', 'example_request': 'Run the bulk performance review config update in USMF sandbox from this Excel file — validate first and show me the dry run.', 'inputs': [{'description': 'Excel file with one row per business performance review target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.', 'name': 'legal_entity'}, {'description': 'Explicit user approval after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-update conduct business performance review configuration in D365 from a spreadsheet, with dry-run validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureConductBusinessPerformanceReviews(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureConductBusinessPerformanceReviews'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Excel file with one row per business performance review target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureConductBusinessPerformanceReviews().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
