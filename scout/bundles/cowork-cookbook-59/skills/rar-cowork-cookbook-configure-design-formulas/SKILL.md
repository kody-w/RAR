---
name: "rar-cowork-cookbook-configure-design-formulas"
description: "Bulk-updates design formulas in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for your approval, then applies changes and returns a before/after confirmation w"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_design_formulas", "rar_sha256": "2d3c178d08a52933d0c1aaa1a14ba00600f990a2b3cede34494d45a3d7db9ef3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
