---
name: "rar-cowork-cookbook-configure-review-case-loads-and-rebalance-case-loads"
description: "Runs a validated bulk case-load rebalancing update in Dynamics 365 F&SCM from an attached Excel file: returns a validation workbook of pass/fail rows, waits for approval, then applies changes and returns a before/after c"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_review_case_loads_and_rebalance_case_loads", "rar_sha256": "11ca4f70201db30510f53351a3bc09421341630dae39161bb69f037a4e655a0c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_review_case_loads_and_rebalance_case_loads`. The original RAPP
agent is preserved byte-for-byte in `configure_review_case_loads_and_rebalance_case_loads_agent.py` and in the RCI capsule.

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

Review case loads and rebalance case loads Configuration Bulk Setup — Runs a validated bulk case-load rebalancing update in Dynamics 365 F&SCM from an attached Excel file: returns a validation workbook of pass/fail rows, waits for approval, then applies changes and returns a before/after c

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-review-case-loads-and-rebalance-case-loads
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
      "description": "Explicit go-ahead after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel": {
      "description": "Excel file with one row per case-load rebalance target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment; use sandbox before production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_review_case_loads_and_rebalance_case_loads_agent.py` and embedded as the fenced Python below (sha256 11ca4f70201db305…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_review_case_loads_and_rebalance_case_loads_agent.py` first:

```bash
python3 configure_review_case_loads_and_rebalance_case_loads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_review_case_loads_and_rebalance_case_loads_agent.py   # or on stdin
python3 configure_review_case_loads_and_rebalance_case_loads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Review case loads and rebalance case loads Configuration Bulk Setup — Runs a validated bulk case-load rebalancing update in Dynamics 365 F&SCM from an attached Excel file: returns a validation workbook of pass/fail rows, waits for approval, then applies changes and returns a before/after c

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-review-case-loads-and-rebalance-case-loads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_review_case_loads_and_rebalance_case_loads',
    "version": '3.0.3',
    "display_name": 'Review case loads and rebalance case loads Configuration Bulk Setup',
    "description": 'Runs a validated bulk case-load rebalancing update in Dynamics 365 F&SCM from an attached Excel file: returns a validation workbook of pass/fail rows, waits for approval, then applies changes and returns a before/after c',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-review-case-loads-and-rebalance-case-loads',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-review-case-loads-and-rebalance-case-loads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '335511bfef3dec61',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/analyze-case-performance/review-case-loads-and-rebalance-case-loads'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/configure-review-case-loads-and-rebalance-case-loads', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel': 'Excel file with one row per case-load rebalance target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; use sandbox before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for review case loads and rebalance case loads, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per review case loads and rebalance case loads target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a validated bulk case-load rebalancing update in Dynamics 365 F&SCM from an attached Excel file: returns a validation workbook of pass/fail rows, waits for approval, then applies changes and returns a before/after c', 'example_request': 'Bulk-rebalance case loads in USMF sandbox from my attached Excel — validate first and show me the preview.', 'inputs': [{'description': 'Excel file with one row per case-load rebalance target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; use sandbox before production.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you have an Excel file of case-load rebalance target rows and need them validated, approved, then bulk-applied in D365 F&SCM (sandbox first).'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureReviewCaseLoadsAndRebalanceCaseLoads(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReviewCaseLoadsAndRebalanceCaseLoads'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Excel file with one row per case-load rebalance target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; use sandbox before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureReviewCaseLoadsAndRebalanceCaseLoads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
