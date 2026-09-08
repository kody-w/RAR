---
name: "rar-cowork-cookbook-configure-develop-training-materials"
description: "Reads an attached configuration Excel file of develop-training-materials targets in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, and applies changes only after your approval"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_training_materials", "rar_sha256": "e1aa09a363b698c29f50b8979b11085aaf7f6f7f9e560305b2648559690ecfdf", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
