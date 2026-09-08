---
name: "rar-cowork-cookbook-configure-identify-workplace-hazards"
description: "Bulk-applies workplace hazard configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a befor"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_identify_workplace_hazards", "rar_sha256": "bf76c8402a5a19e399377126a26a8413fce1847be9c11f7939ef60798eaa0044", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
