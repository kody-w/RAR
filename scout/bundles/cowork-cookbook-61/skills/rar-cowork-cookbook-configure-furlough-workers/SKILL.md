---
name: "rar-cowork-cookbook-configure-furlough-workers"
description: "Bulk-applies furlough worker configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, pauses for your approval, then applies and emits before/after confir"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_furlough_workers", "rar_sha256": "97a44729755005620e0c539fcb30a821db4346751441170ada99242a9cd69a30", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
