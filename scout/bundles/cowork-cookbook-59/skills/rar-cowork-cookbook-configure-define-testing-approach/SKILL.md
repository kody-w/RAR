---
name: "rar-cowork-cookbook-configure-define-testing-approach"
description: "Applies a bulk 'define testing approach' configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and emits"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_testing_approach", "rar_sha256": "cb5e146d6969281bd4a9371bde0d723c68b6ebd8dcf02fd2e31544571c572edd", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
