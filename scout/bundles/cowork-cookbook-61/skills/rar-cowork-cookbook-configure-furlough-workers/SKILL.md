---
name: "rar-cowork-cookbook-configure-furlough-workers"
description: "Bulk-applies furlough worker configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, pauses for your approval, then applies and emits before/after confir"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_furlough_workers", "rar_sha256": "97a44729755005620e0c539fcb30a821db4346751441170ada99242a9cd69a30", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_furlough_workers`. The original RAPP
agent is preserved byte-for-byte in `configure_furlough_workers_agent.py` and in the RCI capsule.

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

Furlough workers Configuration Bulk Setup — Bulk-applies furlough worker configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, pauses for your approval, then applies and emits before/after confir

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-furlough-workers
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
      "description": "Explicit approval after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_excel": {
      "description": "Attached Excel file with one row per furlough worker target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF); use a sandbox environment first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_furlough_workers_agent.py` and embedded as the fenced Python below (sha256 97a4472975500562…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_furlough_workers_agent.py` first:

```bash
python3 configure_furlough_workers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_furlough_workers_agent.py   # or on stdin
python3 configure_furlough_workers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Furlough workers Configuration Bulk Setup — Bulk-applies furlough worker configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, pauses for your approval, then applies and emits before/after confir

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-furlough-workers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_furlough_workers',
    "version": '3.0.3',
    "display_name": 'Furlough workers Configuration Bulk Setup',
    "description": 'Bulk-applies furlough worker configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, pauses for your approval, then applies and emits before/after confir',
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
        "upstream_slug": 'configure-furlough-workers',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-furlough-workers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '19b174df72eb59e3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/offboard-talent/furlough-workers'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/configure-furlough-workers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the validation workbook, before changes are applied.', 'configuration_excel': 'Attached Excel file with one row per furlough worker target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for furlough workers, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per furlough workers target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-applies furlough worker configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, pauses for your approval, then applies and emits before/after confir', 'example_request': 'Run the furlough worker bulk config setup in USMF sandbox using this Excel file - validate first and let me approve.', 'inputs': [{'description': 'Attached Excel file with one row per furlough worker target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to update furlough worker configuration in bulk from a spreadsheet in D365 F&SCM, with dry-run validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureFurloughWorkers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureFurloughWorkers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Attached Excel file with one row per furlough worker target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureFurloughWorkers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
