---
name: "rar-cowork-cookbook-configure-configure-and-maintain-electronically-generated-documents"
description: "Bulk-updates electronic document configuration records in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes and emits a before"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_configure_and_maintain_electronically_generated_documents", "rar_sha256": "b27bcab462227a2c4361c37ef472aec823c65dcc19d5eeb19c5c0246b5d9177b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
