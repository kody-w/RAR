---
name: "rar-cowork-cookbook-configure-conduct-business-performance-reviews"
description: "Applies bulk configuration changes for business performance review targets in Dynamics 365 F&SCM from an Excel file: validates all rows, emits a validation workbook, waits for approval, then applies and reports before/af"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_conduct_business_performance_reviews", "rar_sha256": "710aa04fd99469d666c123afd8599c5a74b7696daa2cab4e9f6964536f044ec1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
