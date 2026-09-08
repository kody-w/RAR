---
name: "rar-cowork-cookbook-configure-track-fronline-worker-location"
description: "Reads an attached Excel file of frontline-worker-location configuration rows against a Dynamics 365 F&SCM legal entity, validates every row, returns a validation workbook, waits for approval, then applies changes and emi"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_track_fronline_worker_location", "rar_sha256": "c9533a7663dbc3b2d3c10c173b04ecf4a72aac189d35a592bf7e10afa20138b1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
