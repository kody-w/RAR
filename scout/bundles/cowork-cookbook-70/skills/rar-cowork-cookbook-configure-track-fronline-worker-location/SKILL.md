---
name: "rar-cowork-cookbook-configure-track-fronline-worker-location"
description: "Reads an attached Excel file of frontline-worker-location configuration rows against a Dynamics 365 F&SCM legal entity, validates every row, returns a validation workbook, waits for approval, then applies changes and emi"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_track_fronline_worker_location", "rar_sha256": "c9533a7663dbc3b2d3c10c173b04ecf4a72aac189d35a592bf7e10afa20138b1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_track_fronline_worker_location`. The original RAPP
agent is preserved byte-for-byte in `configure_track_fronline_worker_location_agent.py` and in the RCI capsule.

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

Track fronline worker location Configuration Bulk Setup — Reads an attached Excel file of frontline-worker-location configuration rows against a Dynamics 365 F&SCM legal entity, validates every row, returns a validation workbook, waits for approval, then applies changes and emi

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-track-fronline-worker-location
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
    "configuration_file": {
      "description": "Excel file with one row per frontline worker location target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; sandbox first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_track_fronline_worker_location_agent.py` and embedded as the fenced Python below (sha256 c9533a7663dbc3b2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_track_fronline_worker_location_agent.py` first:

```bash
python3 configure_track_fronline_worker_location_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_track_fronline_worker_location_agent.py   # or on stdin
python3 configure_track_fronline_worker_location_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track fronline worker location Configuration Bulk Setup — Reads an attached Excel file of frontline-worker-location configuration rows against a Dynamics 365 F&SCM legal entity, validates every row, returns a validation workbook, waits for approval, then applies changes and emi

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-track-fronline-worker-location
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_track_fronline_worker_location',
    "version": '3.0.3',
    "display_name": 'Track fronline worker location Configuration Bulk Setup',
    "description": 'Reads an attached Excel file of frontline-worker-location configuration rows against a Dynamics 365 F&SCM legal entity, validates every row, returns a validation workbook, waits for approval, then applies changes and emi',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-track-fronline-worker-location',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-track-fronline-worker-location',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4399a50f1dc185b7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/track-fronline-worker-location'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/configure-track-fronline-worker-location', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'configuration_file': 'Excel file with one row per frontline worker location target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for track fronline worker location, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per track fronline worker location target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached Excel file of frontline-worker-location configuration rows against a Dynamics 365 F&SCM legal entity, validates every row, returns a validation workbook, waits for approval, then applies changes and emi', 'example_request': 'Bulk update frontline worker location config in USMF sandbox from this Excel file — validate first and show me the dry run.', 'inputs': [{'description': 'Excel file with one row per frontline worker location target and the new field values.', 'name': 'configuration_file'}, {'description': 'D365 legal entity to run against, e.g. USMF; sandbox first.', 'name': 'legal_entity'}, {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to bulk-apply frontline worker location configuration changes in Dynamics 365 F&SCM from a spreadsheet, with dry-run validation and approval before writing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureTrackFronlineWorkerLocation(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureTrackFronlineWorkerLocation'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_file': {'description': 'Excel file with one row per frontline worker location target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureTrackFronlineWorkerLocation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
