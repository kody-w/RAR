---
name: "rar-cowork-cookbook-configure-scrap-defective-production"
description: "Reads an attached Excel file of scrap-defective-production\u914d\u7f6e rows against Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, waits for your approval, then applies changes and emit"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_scrap_defective_production", "rar_sha256": "228255831c9487fe4de5b6ce75074cd122eaf9bcff5aea9083297ac666271937", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
