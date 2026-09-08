---
name: "rar-cowork-cookbook-configure-develop-asset-policies"
description: "Reads an attached configuration Excel file of develop asset policies changes in Dynamics 365 F&SCM, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after conf"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_asset_policies", "rar_sha256": "847f4b834e96f36dc7a0592a1deb01535962c9aeb95ad4c8ce504aa30f644884", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_develop_asset_policies`. The original RAPP
agent is preserved byte-for-byte in `configure_develop_asset_policies_agent.py` and in the RCI capsule.

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

Develop asset policies Configuration Bulk Setup — Reads an attached configuration Excel file of develop asset policies changes in Dynamics 365 F&SCM, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after conf

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-asset-policies
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
    "configuration_excel": {
      "description": "Excel file with one row per develop asset policies target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF); use a sandbox first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_asset_policies_agent.py` and embedded as the fenced Python below (sha256 847f4b834e96f36d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_asset_policies_agent.py` first:

```bash
python3 configure_develop_asset_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_develop_asset_policies_agent.py   # or on stdin
python3 configure_develop_asset_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop asset policies Configuration Bulk Setup — Reads an attached configuration Excel file of develop asset policies changes in Dynamics 365 F&SCM, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after conf

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-asset-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_develop_asset_policies',
    "version": '3.0.3',
    "display_name": 'Develop asset policies Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of develop asset policies changes in Dynamics 365 F&SCM, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after conf',
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
        "upstream_slug": 'configure-develop-asset-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-develop-asset-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6537fabaf2f2dbfb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-asset-policies'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-develop-asset-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_excel': 'Excel file with one row per develop asset policies target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for develop asset policies, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per develop asset policies target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of develop asset policies changes in Dynamics 365 F&SCM, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after conf', 'example_request': 'Bulk-update develop asset policies in USMF sandbox from this Excel file — validate first and show me the preview.', 'inputs': [{'description': 'Excel file with one row per develop asset policies target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to bulk-update develop asset policies in D365 F&SCM from a spreadsheet, with row-level validation and an approval gate before any writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureDevelopAssetPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDevelopAssetPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Excel file with one row per develop asset policies target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureDevelopAssetPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
