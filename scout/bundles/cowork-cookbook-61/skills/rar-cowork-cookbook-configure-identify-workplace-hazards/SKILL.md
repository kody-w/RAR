---
name: "rar-cowork-cookbook-configure-identify-workplace-hazards"
description: "Bulk-applies workplace hazard configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a befor"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_identify_workplace_hazards", "rar_sha256": "bf76c8402a5a19e399377126a26a8413fce1847be9c11f7939ef60798eaa0044", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_identify_workplace_hazards`. The original RAPP
agent is preserved byte-for-byte in `configure_identify_workplace_hazards_agent.py` and in the RCI capsule.

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

Identify workplace hazards Configuration Bulk Setup — Bulk-applies workplace hazard configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a befor

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-identify-workplace-hazards
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
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per workplace hazard target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_identify_workplace_hazards_agent.py` and embedded as the fenced Python below (sha256 bf76c8402a5a19e3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_identify_workplace_hazards_agent.py` first:

```bash
python3 configure_identify_workplace_hazards_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_identify_workplace_hazards_agent.py   # or on stdin
python3 configure_identify_workplace_hazards_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify workplace hazards Configuration Bulk Setup — Bulk-applies workplace hazard configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a befor

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-identify-workplace-hazards
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_identify_workplace_hazards',
    "version": '3.0.3',
    "display_name": 'Identify workplace hazards Configuration Bulk Setup',
    "description": 'Bulk-applies workplace hazard configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a befor',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-identify-workplace-hazards',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-identify-workplace-hazards',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '48b661773878bf48',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/identify-workplace-hazards'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/configure-identify-workplace-hazards', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per workplace hazard target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for identify workplace hazards, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per identify workplace hazards target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-applies workplace hazard configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a befor', 'example_request': 'Run the bulk workplace hazard config update in USMF sandbox from this Excel file — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per workplace hazard target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against (e.g. USMF); sandbox first.', 'name': 'legal_entity'}, {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to update many workplace-hazard configuration records at once in D365 F&SCM from a spreadsheet, with dry-run validation and explicit approval before writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureIdentifyWorkplaceHazards(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureIdentifyWorkplaceHazards'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per workplace hazard target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureIdentifyWorkplaceHazards().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
