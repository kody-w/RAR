---
name: "rar-cowork-cookbook-configure-scrap-defective-production"
description: "Reads an attached Excel file of scrap-defective-production\u914d\u7f6e rows against Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies changes and emit"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_scrap_defective_production", "rar_sha256": "228255831c9487fe4de5b6ce75074cd122eaf9bcff5aea9083297ac666271937", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_scrap_defective_production`. The original RAPP
agent is preserved byte-for-byte in `configure_scrap_defective_production_agent.py` and in the RCI capsule.

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

Scrap defective production Configuration Bulk Setup — Reads an attached Excel file of scrap-defective-production配置 rows against Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies changes and emit

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-scrap-defective-production
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
      "description": "Attached Excel file with one row per scrap defective production target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; USMF, sandbox first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_scrap_defective_production_agent.py` and embedded as the fenced Python below (sha256 228255831c9487fe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_scrap_defective_production_agent.py` first:

```bash
python3 configure_scrap_defective_production_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_scrap_defective_production_agent.py   # or on stdin
python3 configure_scrap_defective_production_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Scrap defective production Configuration Bulk Setup — Reads an attached Excel file of scrap-defective-production配置 rows against Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies changes and emit

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-scrap-defective-production
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_scrap_defective_production',
    "version": '3.0.3',
    "display_name": 'Scrap defective production Configuration Bulk Setup',
    "description": 'Reads an attached Excel file of scrap-defective-production配置 rows against Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies changes and emit',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-scrap-defective-production',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-scrap-defective-production',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a20a7ac72210cbde',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/scrap-defective-production'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/configure-scrap-defective-production', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per scrap defective production target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; USMF, sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for scrap defective production, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per scrap defective production target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached Excel file of scrap-defective-production配置 rows against Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies changes and emit', 'example_request': 'Bulk-update scrap defective production in USMF sandbox from this Excel file — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per scrap defective production target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against; USMF, sandbox first.', 'name': 'legal_entity'}, {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to bulk-update scrap defective production settings in D365 F&SCM from a spreadsheet, with dry-run validation and explicit approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureScrapDefectiveProduction(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureScrapDefectiveProduction'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per scrap defective production target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; USMF, sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureScrapDefectiveProduction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
