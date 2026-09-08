---
name: "rar-cowork-cookbook-configure-define-learning-paths"
description: "Bulk-applies define-learning-paths configuration changes in Dynamics 365 F&SCM from an attached Excel file, validating every row first, pausing for approval, then emitting validation and before/after confirmation workboo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_learning_paths", "rar_sha256": "9e348aef8dbca2d7241f1d911da43b1e35ba68e61902c8a2b3e0c163d9662fe7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_define_learning_paths`. The original RAPP
agent is preserved byte-for-byte in `configure_define_learning_paths_agent.py` and in the RCI capsule.

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

Define learning paths Configuration Bulk Setup — Bulk-applies define-learning-paths configuration changes in Dynamics 365 F&SCM from an attached Excel file, validating every row first, pausing for approval, then emitting validation and before/after confirmation workboo

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-learning-paths
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
      "description": "Explicit user approval after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_excel": {
      "description": "Attached Excel file with one row per define learning paths target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; sandbox environment first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_learning_paths_agent.py` and embedded as the fenced Python below (sha256 9e348aef8dbca2d7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_learning_paths_agent.py` first:

```bash
python3 configure_define_learning_paths_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_define_learning_paths_agent.py   # or on stdin
python3 configure_define_learning_paths_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define learning paths Configuration Bulk Setup — Bulk-applies define-learning-paths configuration changes in Dynamics 365 F&SCM from an attached Excel file, validating every row first, pausing for approval, then emitting validation and before/after confirmation workboo

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-learning-paths
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_define_learning_paths',
    "version": '3.0.3',
    "display_name": 'Define learning paths Configuration Bulk Setup',
    "description": 'Bulk-applies define-learning-paths configuration changes in Dynamics 365 F&SCM from an attached Excel file, validating every row first, pausing for approval, then emitting validation and before/after confirmation workboo',
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
        "upstream_slug": 'configure-define-learning-paths',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-define-learning-paths',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '50e26a6a745f2acf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/define-learning-paths'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/configure-define-learning-paths', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, before changes are applied.', 'configuration_excel': 'Attached Excel file with one row per define learning paths target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for define learning paths, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per define learning paths target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-applies define-learning-paths configuration changes in Dynamics 365 F&SCM from an attached Excel file, validating every row first, pausing for approval, then emitting validation and before/after confirmation workboo', 'example_request': 'Validate and bulk-apply the attached learning paths config file in USMF sandbox, show me the dry run first.', 'inputs': [{'description': 'Attached Excel file with one row per define learning paths target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against, e.g. USMF; sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit user approval after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have an Excel file of learning path configuration rows to validate and apply in bulk to D365 F&SCM, with dry-run review and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureDefineLearningPaths(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDefineLearningPaths'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Attached Excel file with one row per define learning paths target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureDefineLearningPaths().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
