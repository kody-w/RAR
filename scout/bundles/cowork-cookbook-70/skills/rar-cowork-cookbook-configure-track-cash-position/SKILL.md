---
name: "rar-cowork-cookbook-configure-track-cash-position"
description: "Applies bulk cash-position configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies and returns a before/after confirma"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_track_cash_position", "rar_sha256": "206ac8e14febbd54b02aff19e33be1807bf2417d27b91da566aae8f3bfff2244", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
