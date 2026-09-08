---
name: "rar-cowork-cookbook-configure-develop-training-materials"
description: "Reads an attached configuration Excel file of develop-training-materials targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, and applies changes only after your approval"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_training_materials", "rar_sha256": "e1aa09a363b698c29f50b8979b11085aaf7f6f7f9e560305b2648559690ecfdf", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_develop_training_materials`. The original RAPP
agent is preserved byte-for-byte in `configure_develop_training_materials_agent.py` and in the RCI capsule.

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

Develop training materials Configuration Bulk Setup — Reads an attached configuration Excel file of develop-training-materials targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, and applies changes only after your approval

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-training-materials
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
      "description": "Explicit go-ahead after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel": {
      "description": "Excel file with one row per develop training materials target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment; sandbox first before production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (default USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_training_materials_agent.py` and embedded as the fenced Python below (sha256 e1aa09a363b698c2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_training_materials_agent.py` first:

```bash
python3 configure_develop_training_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_develop_training_materials_agent.py   # or on stdin
python3 configure_develop_training_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop training materials Configuration Bulk Setup — Reads an attached configuration Excel file of develop-training-materials targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, and applies changes only after your approval

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-training-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_develop_training_materials',
    "version": '3.0.3',
    "display_name": 'Develop training materials Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of develop-training-materials targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, and applies changes only after your approval',
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
        "upstream_slug": 'configure-develop-training-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-develop-training-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0819485f0a738e91',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/develop-training-materials'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-develop-training-materials', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel': 'Excel file with one row per develop training materials target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox first before production.', 'legal_entity': 'D365 legal entity to run against (default USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for develop training materials, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per develop training materials target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of develop-training-materials targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, and applies changes only after your approval', 'example_request': 'Bulk-update our develop training materials config in USMF sandbox from this Excel file — validate first and show me before applying.', 'inputs': [{'description': 'Excel file with one row per develop training materials target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against (default USMF).', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-apply develop training materials configuration changes in D365 F&SCM from a spreadsheet, with dry-run validation and approval before write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureDevelopTrainingMaterials(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDevelopTrainingMaterials'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Excel file with one row per develop training materials target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureDevelopTrainingMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
