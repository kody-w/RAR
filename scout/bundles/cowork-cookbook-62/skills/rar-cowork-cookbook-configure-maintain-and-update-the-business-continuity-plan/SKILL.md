---
name: "rar-cowork-cookbook-configure-maintain-and-update-the-business-continuity-plan"
description: "Applies bulk business continuity plan configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns before/"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_maintain_and_update_the_business_continuity_plan", "rar_sha256": "a3f3830e592be38e45769d3d4518a7d3568ca9beb6f767563edae902c925886c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
