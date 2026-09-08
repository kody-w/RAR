---
name: "rar-cowork-cookbook-configure-configure-and-maintain-electronically-generated-documents"
description: "Bulk-updates electronic document configuration records in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes and emits a before"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_configure_and_maintain_electronically_generated_documents", "rar_sha256": "b27bcab462227a2c4361c37ef472aec823c65dcc19d5eeb19c5c0246b5d9177b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_configure_and_maintain_electronically_generated_documents`. The original RAPP
agent is preserved byte-for-byte in `configure_configure_and_maintain_electronically_generated_documents_agent.py` and in the RCI capsule.

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

Configure and maintain electronically generated documents Configuration Bulk Setup — Bulk-updates electronic document configuration records in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes and emits a before

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-configure-and-maintain-electronically-generated-documents
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
      "description": "Explicit user approval after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per electronic document configuration target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; use a sandbox environment first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_configure_and_maintain_electronically_generated_documents_agent.py` and embedded as the fenced Python below (sha256 b27bcab462227a2c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_configure_and_maintain_electronically_generated_documents_agent.py` first:

```bash
python3 configure_configure_and_maintain_electronically_generated_documents_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_configure_and_maintain_electronically_generated_documents_agent.py   # or on stdin
python3 configure_configure_and_maintain_electronically_generated_documents_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and maintain electronically generated documents Configuration Bulk Setup — Bulk-updates electronic document configuration records in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes and emits a before

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-configure-and-maintain-electronically-generated-documents
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_configure_and_maintain_electronically_generated_documents',
    "version": '3.0.3',
    "display_name": 'Configure and maintain electronically generated documents Configuration Bulk Setup',
    "description": 'Bulk-updates electronic document configuration records in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes and emits a before',
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
        "upstream_slug": 'configure-configure-and-maintain-electronically-generated-documents',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-configure-and-maintain-electronically-generated-documents',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ae2d97a11ee1842b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-maintain-electronically-generated-documents'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-configure-and-maintain-electronically-generated-documents', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per electronic document configuration target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for configure and maintain electronically generated documents, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per configure and maintain electronically generated documents target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-updates electronic document configuration records in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes and emits a before', 'example_request': "Here's my config spreadsheet — bulk update the electronic document setup in USMF sandbox, validate first and show me before applying.", 'inputs': [{'description': 'Attached Excel file with one row per electronic document configuration target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to apply many electronic-document configuration changes at once from a spreadsheet, with row-level validation and an approval gate before writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureConfigureAndMaintainElectronicallyGeneratedDocuments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureConfigureAndMaintainElectronicallyGeneratedDocuments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per electronic document configuration target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureConfigureAndMaintainElectronicallyGeneratedDocuments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
