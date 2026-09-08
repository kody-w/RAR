---
name: "rar-cowork-cookbook-configure-reclaim-database-storage"
description: "Reads an attached Excel file of reclaim-database-storage configuration rows for a D365 F&SCM legal entity, validates each row, returns a validation workbook, waits for approval, then applies changes and emits a before/af"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_reclaim_database_storage", "rar_sha256": "4c90e1de9974af83931ab49d8c47209aefe42e9d441afd51e4fa360df35976df", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_reclaim_database_storage`. The original RAPP
agent is preserved byte-for-byte in `configure_reclaim_database_storage_agent.py` and in the RCI capsule.

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

Reclaim database storage Configuration Bulk Setup — Reads an attached Excel file of reclaim-database-storage configuration rows for a D365 F&SCM legal entity, validates each row, returns a validation workbook, waits for approval, then applies changes and emits a before/af

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-reclaim-database-storage
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
    "configuration_excel": {
      "description": "Attached Excel file with one row per reclaim database storage target and the new field values.",
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
      "description": "D365 legal entity to run against, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_reclaim_database_storage_agent.py` and embedded as the fenced Python below (sha256 4c90e1de9974af83…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_reclaim_database_storage_agent.py` first:

```bash
python3 configure_reclaim_database_storage_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_reclaim_database_storage_agent.py   # or on stdin
python3 configure_reclaim_database_storage_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reclaim database storage Configuration Bulk Setup — Reads an attached Excel file of reclaim-database-storage configuration rows for a D365 F&SCM legal entity, validates each row, returns a validation workbook, waits for approval, then applies changes and emits a before/af

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-reclaim-database-storage
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_reclaim_database_storage',
    "version": '3.0.3',
    "display_name": 'Reclaim database storage Configuration Bulk Setup',
    "description": 'Reads an attached Excel file of reclaim-database-storage configuration rows for a D365 F&SCM legal entity, validates each row, returns a validation workbook, waits for approval, then applies changes and emits a before/af',
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
        "upstream_slug": 'configure-reclaim-database-storage',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-reclaim-database-storage',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a9b36e619436f736',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/reclaim-database-storage'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-reclaim-database-storage', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'configuration_excel': 'Attached Excel file with one row per reclaim database storage target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for reclaim database storage, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per reclaim database storage target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached Excel file of reclaim-database-storage configuration rows for a D365 F&SCM legal entity, validates each row, returns a validation workbook, waits for approval, then applies changes and emits a before/af', 'example_request': 'Bulk-apply the reclaim database storage config in this Excel to USMF sandbox — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per reclaim database storage target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to bulk-apply reclaim database storage configuration changes in Dynamics 365 F&SCM from a spreadsheet, with dry-run validation and approval before writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureReclaimDatabaseStorage(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReclaimDatabaseStorage'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Attached Excel file with one row per reclaim database storage target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureReclaimDatabaseStorage().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
