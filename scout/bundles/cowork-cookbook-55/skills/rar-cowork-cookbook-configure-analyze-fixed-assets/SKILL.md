---
name: "rar-cowork-cookbook-configure-analyze-fixed-assets"
description: "Reads an attached Excel file of fixed asset configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies changes with a before/after confirmatio"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_fixed_assets", "rar_sha256": "5849424ecd5f576261b9c4eb547fb43dd76259c183a8cd315624c304cda34439", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_analyze_fixed_assets`. The original RAPP
agent is preserved byte-for-byte in `configure_analyze_fixed_assets_agent.py` and in the RCI capsule.

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

Analyze fixed assets Configuration Bulk Setup — Reads an attached Excel file of fixed asset configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies changes with a before/after confirmatio

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-fixed-assets
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
    "configuration_file": {
      "description": "Excel file with one row per fixed asset target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 5849424ecd5f5762…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_fixed_assets_agent.py` first:

```bash
python3 configure_analyze_fixed_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_fixed_assets_agent.py   # or on stdin
python3 configure_analyze_fixed_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze fixed assets Configuration Bulk Setup — Reads an attached Excel file of fixed asset configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies changes with a before/after confirmatio

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-fixed-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_fixed_assets',
    "version": '3.0.3',
    "display_name": 'Analyze fixed assets Configuration Bulk Setup',
    "description": 'Reads an attached Excel file of fixed asset configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies changes with a before/after confirmatio',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-analyze-fixed-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-fixed-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '634fd710233cbb5d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/analyze-fixed-assets'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/configure-analyze-fixed-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_file': 'Excel file with one row per fixed asset target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for analyze fixed assets, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per analyze fixed assets target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached Excel file of fixed asset configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies changes with a before/after confirmatio', 'example_request': 'Bulk-update fixed asset config in USMF sandbox from this Excel file — validate first and show me the dry run.', 'inputs': [{'description': 'Excel file with one row per fixed asset target and the new field values.', 'name': 'configuration_file'}, {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-update fixed asset configuration in Dynamics 365 F&SCM from a spreadsheet, with dry-run validation and explicit approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureAnalyzeFixedAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeFixedAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_file': {'description': 'Excel file with one row per fixed asset target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureAnalyzeFixedAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
