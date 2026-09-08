---
name: "rar-cowork-cookbook-configure-maintain-and-update-the-business-continuity-plan"
description: "Applies bulk business continuity plan configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns before/"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_maintain_and_update_the_business_continuity_plan", "rar_sha256": "a3f3830e592be38e45769d3d4518a7d3568ca9beb6f767563edae902c925886c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_maintain_and_update_the_business_continuity_plan`. The original RAPP
agent is preserved byte-for-byte in `configure_maintain_and_update_the_business_continuity_plan_agent.py` and in the RCI capsule.

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

Maintain and update the business continuity plan Configuration Bulk Setup — Applies bulk business continuity plan configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns before/

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-maintain-and-update-the-business-continuity-plan
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
      "description": "Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel": {
      "description": "Attached Excel file with one row per business continuity plan target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF); sandbox first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_maintain_and_update_the_business_continuity_plan_agent.py` and embedded as the fenced Python below (sha256 a3f3830e592be38e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_maintain_and_update_the_business_continuity_plan_agent.py` first:

```bash
python3 configure_maintain_and_update_the_business_continuity_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_maintain_and_update_the_business_continuity_plan_agent.py   # or on stdin
python3 configure_maintain_and_update_the_business_continuity_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain and update the business continuity plan Configuration Bulk Setup — Applies bulk business continuity plan configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns before/

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-maintain-and-update-the-business-continuity-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_maintain_and_update_the_business_continuity_plan',
    "version": '3.0.3',
    "display_name": 'Maintain and update the business continuity plan Configuration Bulk Setup',
    "description": 'Applies bulk business continuity plan configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns before/',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-maintain-and-update-the-business-continuity-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-maintain-and-update-the-business-continuity-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '77500dbfd56b250e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/maintain-and-update-the-business-continuity-plan'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-maintain-and-update-the-business-continuity-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel': 'Attached Excel file with one row per business continuity plan target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for maintain and update the business continuity plan, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per maintain and update the business continuity plan target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies bulk business continuity plan configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns before/', 'example_request': 'Bulk-update our business continuity plan config in USMF sandbox from this Excel file - validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per business continuity plan target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against (e.g. USMF); sandbox first.', 'name': 'legal_entity'}, {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have an Excel file of business continuity plan config updates to validate and bulk-apply in D365 F&SCM, with dry-run review and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureMaintainAndUpdateTheBusinessContinuityPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureMaintainAndUpdateTheBusinessContinuityPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Attached Excel file with one row per business continuity plan target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureMaintainAndUpdateTheBusinessContinuityPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
