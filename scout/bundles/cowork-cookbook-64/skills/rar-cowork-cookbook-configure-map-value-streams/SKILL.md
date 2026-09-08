---
name: "rar-cowork-cookbook-configure-map-value-streams"
description: "Runs a bulk value-stream mapping configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then applies changes and returns a before/"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_map_value_streams", "rar_sha256": "157b80b47311d0a5d84ff3fd29bdf9c2a5c1ef92281d9a67e3024bab6ab325e0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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
