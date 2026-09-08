---
name: "rar-cowork-cookbook-configure-define-learning-paths"
description: "Bulk-applies define-learning-paths configuration changes in Dynamics 365 F&SCM from an attached Excel file, validating every row first, pausing for approval, then emitting validation and before/after confirmation workboo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_learning_paths", "rar_sha256": "9e348aef8dbca2d7241f1d911da43b1e35ba68e61902c8a2b3e0c163d9662fe7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
