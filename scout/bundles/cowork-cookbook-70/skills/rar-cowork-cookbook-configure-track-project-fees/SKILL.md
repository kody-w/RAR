---
name: "rar-cowork-cookbook-configure-track-project-fees"
description: "Reads an attached configuration Excel file of track project fees changes for a Dynamics 365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies the changes with a befor"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_track_project_fees", "rar_sha256": "881f4ced0bfc2f4de0fbb22f46566277b111e55b215ff39660e56bb676c99202", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_track_project_fees`. The original RAPP
agent is preserved byte-for-byte in `configure_track_project_fees_agent.py` and in the RCI capsule.

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

Track project fees Configuration Bulk Setup — Reads an attached configuration Excel file of track project fees changes for a Dynamics 365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies the changes with a befor

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-track-project-fees
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
      "description": "Explicit confirmation after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_file": {
      "description": "Excel file with one row per track project fees target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; use a sandbox first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_track_project_fees_agent.py` and embedded as the fenced Python below (sha256 881f4ced0bfc2f4d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_track_project_fees_agent.py` first:

```bash
python3 configure_track_project_fees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_track_project_fees_agent.py   # or on stdin
python3 configure_track_project_fees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track project fees Configuration Bulk Setup — Reads an attached configuration Excel file of track project fees changes for a Dynamics 365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies the changes with a befor

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-track-project-fees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_track_project_fees',
    "version": '3.0.3',
    "display_name": 'Track project fees Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of track project fees changes for a Dynamics 365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies the changes with a befor',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-track-project-fees',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-track-project-fees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c1b8deecbcdb1a85',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/track-project-fees'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/configure-track-project-fees', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit confirmation after reviewing the validation workbook, before changes are applied.', 'configuration_file': 'Excel file with one row per track project fees target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for track project fees, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per track project fees target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of track project fees changes for a Dynamics 365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies the changes with a befor', 'example_request': 'Run the track project fees bulk config update in USMF sandbox from my attached Excel file — validate first.', 'inputs': [{'description': 'Excel file with one row per track project fees target and the new field values.', 'name': 'configuration_file'}, {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.', 'name': 'legal_entity'}, {'description': 'Explicit confirmation after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-apply track project fees configuration changes in D365 F&SCM from a spreadsheet, with row validation and an approval gate before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureTrackProjectFees(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureTrackProjectFees'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit confirmation after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_file': {'description': 'Excel file with one row per track project fees target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureTrackProjectFees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
