---
name: "rar-cowork-cookbook-configure-analyze-fixed-assets"
description: "Reads an attached Excel file of fixed asset configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies changes with a before/after confirmatio"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_fixed_assets", "rar_sha256": "5849424ecd5f576261b9c4eb547fb43dd76259c183a8cd315624c304cda34439", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
