---
name: "rar-cowork-cookbook-configure-define-business-continuity-objectives"
description: "Runs a bulk business continuity objectives configuration update in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes with a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_business_continuity_objectives", "rar_sha256": "86a98e7fc513625ac0d94226e60f83414ea1a55e89862e214899dc97cf04f3a1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_define_business_continuity_objectives`. The original RAPP
agent is preserved byte-for-byte in `configure_define_business_continuity_objectives_agent.py` and in the RCI capsule.

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

Define business continuity objectives Configuration Bulk Setup — Runs a bulk business continuity objectives configuration update in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes with a

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-business-continuity-objectives
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
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per business continuity objectives target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment; run sandbox first before production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_business_continuity_objectives_agent.py` and embedded as the fenced Python below (sha256 86a98e7fc513625a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_business_continuity_objectives_agent.py` first:

```bash
python3 configure_define_business_continuity_objectives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_define_business_continuity_objectives_agent.py   # or on stdin
python3 configure_define_business_continuity_objectives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define business continuity objectives Configuration Bulk Setup — Runs a bulk business continuity objectives configuration update in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes with a

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-business-continuity-objectives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_define_business_continuity_objectives',
    "version": '3.0.3',
    "display_name": 'Define business continuity objectives Configuration Bulk Setup',
    "description": 'Runs a bulk business continuity objectives configuration update in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes with a',
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
        "upstream_slug": 'configure-define-business-continuity-objectives',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-define-business-continuity-objectives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '162434268a5bec6e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/define-business-continuity-objectives'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-define-business-continuity-objectives', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per business continuity objectives target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; run sandbox first before production.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for define business continuity objectives, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per define business continuity objectives target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a bulk business continuity objectives configuration update in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes with a', 'example_request': 'Bulk-update business continuity objectives in USMF sandbox from this Excel file — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per business continuity objectives target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Target environment; run sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to bulk-update define business continuity objectives config in D365 F&SCM from a spreadsheet, with dry-run validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureDefineBusinessContinuityObjectives(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDefineBusinessContinuityObjectives'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per business continuity objectives target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; run sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureDefineBusinessContinuityObjectives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
