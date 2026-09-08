---
name: "rar-cowork-cookbook-configure-review-case-loads-and-rebalance-case-loads"
description: "Runs a validated bulk case-load rebalancing update in Dynamics 365 F&SCM from an attached Excel file: returns a validation workbook of pass/fail rows, waits for approval, then applies changes and returns a before/after c"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_review_case_loads_and_rebalance_case_loads", "rar_sha256": "11ca4f70201db30510f53351a3bc09421341630dae39161bb69f037a4e655a0c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
