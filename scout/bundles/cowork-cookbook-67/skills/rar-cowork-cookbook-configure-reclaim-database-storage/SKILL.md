---
name: "rar-cowork-cookbook-configure-reclaim-database-storage"
description: "Reads an attached Excel file of reclaim-database-storage configuration rows for a D365 F&SCM legal entity, validates each row, returns a validation workbook, waits for approval, then applies changes and emits a before/af"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_reclaim_database_storage", "rar_sha256": "4c90e1de9974af83931ab49d8c47209aefe42e9d441afd51e4fa360df35976df", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
