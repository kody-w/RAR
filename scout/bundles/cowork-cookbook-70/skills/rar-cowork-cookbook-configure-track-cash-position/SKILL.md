---
name: "rar-cowork-cookbook-configure-track-cash-position"
description: "Applies bulk cash-position configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies and returns a before/after confirma"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_track_cash_position", "rar_sha256": "206ac8e14febbd54b02aff19e33be1807bf2417d27b91da566aae8f3bfff2244", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_track_cash_position`. The original RAPP
agent is preserved byte-for-byte in `configure_track_cash_position_agent.py` and in the RCI capsule.

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

Track cash position Configuration Bulk Setup — Applies bulk cash-position configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies and returns a before/after confirma

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-track-cash-position
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
      "description": "Explicit go-ahead after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per track cash position target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment; use sandbox first before production.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_track_cash_position_agent.py` and embedded as the fenced Python below (sha256 206ac8e14febbd54…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_track_cash_position_agent.py` first:

```bash
python3 configure_track_cash_position_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_track_cash_position_agent.py   # or on stdin
python3 configure_track_cash_position_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track cash position Configuration Bulk Setup — Applies bulk cash-position configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies and returns a before/after confirma

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-track-cash-position
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_track_cash_position',
    "version": '3.0.3',
    "display_name": 'Track cash position Configuration Bulk Setup',
    "description": 'Applies bulk cash-position configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies and returns a before/after confirma',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-track-cash-position',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-track-cash-position',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f1cbea5c65b862fa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/track-cash-position'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-track-cash-position', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per track cash position target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; use sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for track cash position, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per track cash position target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies bulk cash-position configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies and returns a before/after confirma', 'example_request': 'Bulk-update track cash position config in USMF sandbox from this Excel file - validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per track cash position target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; use sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-update track cash position configuration in D365 F&SCM from a spreadsheet, with dry-run validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureTrackCashPosition(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureTrackCashPosition'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per track cash position target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; use sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureTrackCashPosition().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
