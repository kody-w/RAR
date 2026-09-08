---
name: "rar-cowork-cookbook-configure-define-testing-approach"
description: "Applies a bulk 'define testing approach' configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_testing_approach", "rar_sha256": "cb5e146d6969281bd4a9371bde0d723c68b6ebd8dcf02fd2e31544571c572edd", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_define_testing_approach`. The original RAPP
agent is preserved byte-for-byte in `configure_define_testing_approach_agent.py` and in the RCI capsule.

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

Define testing approach Configuration Bulk Setup — Applies a bulk 'define testing approach' configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-testing-approach
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
    "configuration_excel_file": {
      "description": "Attached workbook with one row per define testing approach target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_testing_approach_agent.py` and embedded as the fenced Python below (sha256 cb5e146d6969281b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_testing_approach_agent.py` first:

```bash
python3 configure_define_testing_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_define_testing_approach_agent.py   # or on stdin
python3 configure_define_testing_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define testing approach Configuration Bulk Setup — Applies a bulk 'define testing approach' configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-testing-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_define_testing_approach',
    "version": '3.0.3',
    "display_name": 'Define testing approach Configuration Bulk Setup',
    "description": "Applies a bulk 'define testing approach' configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits",
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
        "upstream_slug": 'configure-define-testing-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-define-testing-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b2e227c947a2c594',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-testing-approach'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-define-testing-approach', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached workbook with one row per define testing approach target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for define testing approach, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per define testing approach target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Applies a bulk 'define testing approach' configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits", 'example_request': 'Run the bulk define testing approach config update in USMF sandbox from this Excel file - validate first and wait for my approval.', 'inputs': [{'description': 'Attached workbook with one row per define testing approach target and the new field values.', 'name': 'configuration Excel file'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'name': 'legal entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to bulk-update define testing approach configuration rows in D365 F&SCM from a spreadsheet, with dry-run validation and explicit approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureDefineTestingApproach(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDefineTestingApproach'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached workbook with one row per define testing approach target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureDefineTestingApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
