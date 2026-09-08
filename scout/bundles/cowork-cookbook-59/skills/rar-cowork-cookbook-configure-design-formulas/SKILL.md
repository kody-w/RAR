---
name: "rar-cowork-cookbook-configure-design-formulas"
description: "Bulk-updates design formulas in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for your approval, then applies changes and returns a before/after confirmation w"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_design_formulas", "rar_sha256": "2d3c178d08a52933d0c1aaa1a14ba00600f990a2b3cede34494d45a3d7db9ef3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_design_formulas`. The original RAPP
agent is preserved byte-for-byte in `configure_design_formulas_agent.py` and in the RCI capsule.

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

Design formulas Configuration Bulk Setup — Bulk-updates design formulas in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for your approval, then applies changes and returns a before/after confirmation w

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-design-formulas
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
      "description": "Attached Excel file with one row per design formulas target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF); use a sandbox first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_design_formulas_agent.py` and embedded as the fenced Python below (sha256 2d3c178d08a52933…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_design_formulas_agent.py` first:

```bash
python3 configure_design_formulas_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_design_formulas_agent.py   # or on stdin
python3 configure_design_formulas_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Design formulas Configuration Bulk Setup — Bulk-updates design formulas in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for your approval, then applies changes and returns a before/after confirmation w

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-design-formulas
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_design_formulas',
    "version": '3.0.3',
    "display_name": 'Design formulas Configuration Bulk Setup',
    "description": 'Bulk-updates design formulas in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for your approval, then applies changes and returns a before/after confirmation w',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-design-formulas',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-design-formulas',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8a9dde4c603f23e7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/design-formulas'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/configure-design-formulas', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per design formulas target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for design formulas, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per design formulas target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-updates design formulas in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for your approval, then applies changes and returns a before/after confirmation w', 'example_request': "Here's my design formula update spreadsheet — validate it against USMF sandbox and show me what would change before applying.", 'inputs': [{'description': 'Attached Excel file with one row per design formulas target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to apply many design formula field changes at once from a spreadsheet, with row-level validation and an approval gate before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureDesignFormulas(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDesignFormulas'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per design formulas target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureDesignFormulas().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
