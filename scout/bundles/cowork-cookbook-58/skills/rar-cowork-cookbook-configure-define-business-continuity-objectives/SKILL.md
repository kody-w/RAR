---
name: "rar-cowork-cookbook-configure-define-business-continuity-objectives"
description: "Runs a bulk business continuity objectives configuration update in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes with a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_business_continuity_objectives", "rar_sha256": "86a98e7fc513625ac0d94226e60f83414ea1a55e89862e214899dc97cf04f3a1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
