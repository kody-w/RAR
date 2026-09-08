---
name: "rar-cowork-cookbook-configure-create-and-track-service-level-agreements"
description: "Bulk-creates and updates service level agreement records in Dynamics 365 F&SCM from an attached configuration Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_create_and_track_service_level_agreements", "rar_sha256": "4f0481ab8c60fbdcb8fd28dfda2c8f4344c00f7feb007c52921f670de7f16b5a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_create_and_track_service_level_agreements`. The original RAPP
agent is preserved byte-for-byte in `configure_create_and_track_service_level_agreements_agent.py` and in the RCI capsule.

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

Create and track service level agreements Configuration Bulk Setup — Bulk-creates and updates service level agreement records in Dynamics 365 F&SCM from an attached configuration Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-create-and-track-service-level-agreements
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
      "description": "Excel file with one row per service level agreement target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment; run sandbox first before production.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_create_and_track_service_level_agreements_agent.py` and embedded as the fenced Python below (sha256 4f0481ab8c60fbdc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_create_and_track_service_level_agreements_agent.py` first:

```bash
python3 configure_create_and_track_service_level_agreements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_create_and_track_service_level_agreements_agent.py   # or on stdin
python3 configure_create_and_track_service_level_agreements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create and track service level agreements Configuration Bulk Setup — Bulk-creates and updates service level agreement records in Dynamics 365 F&SCM from an attached configuration Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-create-and-track-service-level-agreements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_create_and_track_service_level_agreements',
    "version": '3.0.3',
    "display_name": 'Create and track service level agreements Configuration Bulk Setup',
    "description": 'Bulk-creates and updates service level agreement records in Dynamics 365 F&SCM from an attached configuration Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-create-and-track-service-level-agreements',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-create-and-track-service-level-agreements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '26f8979f25ffea1b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/create-and-track-service-level-agreements'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/configure-create-and-track-service-level-agreements', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit confirmation after reviewing the validation workbook, before changes are applied.', 'configuration_file': 'Excel file with one row per service level agreement target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; run sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for create and track service level agreements, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per create and track service level agreements target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-creates and updates service level agreement records in Dynamics 365 F&SCM from an attached configuration Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes', 'example_request': 'Run the SLA bulk setup on USMF sandbox using my attached config Excel — validate first and wait for my approval.', 'inputs': [{'description': 'Excel file with one row per service level agreement target and the new field values.', 'name': 'configuration_file'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; run sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit confirmation after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you have an Excel file of SLA rows to apply in bulk to a D365 legal entity and want row-level validation plus an approval gate before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureCreateAndTrackServiceLevelAgreements(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureCreateAndTrackServiceLevelAgreements'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit confirmation after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_file': {'description': 'Excel file with one row per service level agreement target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; run sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureCreateAndTrackServiceLevelAgreements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
