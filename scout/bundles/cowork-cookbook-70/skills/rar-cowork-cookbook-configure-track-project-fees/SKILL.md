---
name: "rar-cowork-cookbook-configure-track-project-fees"
description: "Reads an attached configuration Excel file of track project fees changes for a Dynamics 365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies the changes with a befor"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_track_project_fees", "rar_sha256": "881f4ced0bfc2f4de0fbb22f46566277b111e55b215ff39660e56bb676c99202", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
