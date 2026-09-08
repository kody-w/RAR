---
name: "rar-cowork-cookbook-configure-create-and-track-service-level-agreements"
description: "Bulk-creates and updates service level agreement records in Dynamics 365 F&SCM from an attached configuration Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_create_and_track_service_level_agreements", "rar_sha256": "4f0481ab8c60fbdcb8fd28dfda2c8f4344c00f7feb007c52921f670de7f16b5a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
