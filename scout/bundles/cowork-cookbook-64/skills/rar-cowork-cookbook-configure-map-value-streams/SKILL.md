---
name: "rar-cowork-cookbook-configure-map-value-streams"
description: "Runs a bulk value-stream mapping configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then applies changes and returns a before/"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_map_value_streams", "rar_sha256": "157b80b47311d0a5d84ff3fd29bdf9c2a5c1ef92281d9a67e3024bab6ab325e0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_map_value_streams`. The original RAPP
agent is preserved byte-for-byte in `configure_map_value_streams_agent.py` and in the RCI capsule.

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

Map value streams Configuration Bulk Setup — Runs a bulk value-stream mapping configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then applies changes and returns a before/

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-map-value-streams
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
      "description": "Explicit confirmation after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_file": {
      "description": "Attached Excel file with one row per map value streams target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF); use a sandbox environment first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_map_value_streams_agent.py` and embedded as the fenced Python below (sha256 157b80b47311d0a5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_map_value_streams_agent.py` first:

```bash
python3 configure_map_value_streams_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_map_value_streams_agent.py   # or on stdin
python3 configure_map_value_streams_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Map value streams Configuration Bulk Setup — Runs a bulk value-stream mapping configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then applies changes and returns a before/

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-map-value-streams
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_map_value_streams',
    "version": '3.0.3',
    "display_name": 'Map value streams Configuration Bulk Setup',
    "description": 'Runs a bulk value-stream mapping configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then applies changes and returns a before/',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-map-value-streams',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-map-value-streams',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '46646cdca1066baa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies/map-value-streams'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/configure-map-value-streams', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit confirmation after reviewing the validation workbook, before any changes are applied.', 'configuration_file': 'Attached Excel file with one row per map value streams target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for map value streams, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per map value streams target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a bulk value-stream mapping configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then applies changes and returns a before/', 'example_request': 'Bulk-update map value streams in USMF sandbox from this config Excel — validate rows first and let me approve before applying.', 'inputs': [{'description': 'Attached Excel file with one row per map value streams target and the new field values.', 'name': 'configuration_file'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit confirmation after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when applying bulk map-value-stream configuration updates in D365 F&SCM from a spreadsheet, with row validation and an approval gate before any writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureMapValueStreams(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureMapValueStreams'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit confirmation after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_file': {'description': 'Attached Excel file with one row per map value streams target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureMapValueStreams().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
