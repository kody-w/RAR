---
name: "rar-cowork-cookbook-configure-release-goods-for-picking"
description: "Applies a bulk release-goods-for-picking configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes and returns"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_release_goods_for_picking", "rar_sha256": "67e0aea5147dfeb00dbb59ed5444132583fc2d2c72b77183aa6dffcc50b30e5f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_release_goods_for_picking`. The original RAPP
agent is preserved byte-for-byte in `configure_release_goods_for_picking_agent.py` and in the RCI capsule.

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

Release goods for picking Configuration Bulk Setup — Applies a bulk release-goods-for-picking configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes and returns

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-release-goods-for-picking
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
      "description": "Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per release goods for picking target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_release_goods_for_picking_agent.py` and embedded as the fenced Python below (sha256 67e0aea5147dfeb0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_release_goods_for_picking_agent.py` first:

```bash
python3 configure_release_goods_for_picking_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_release_goods_for_picking_agent.py   # or on stdin
python3 configure_release_goods_for_picking_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Release goods for picking Configuration Bulk Setup — Applies a bulk release-goods-for-picking configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes and returns

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-release-goods-for-picking
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_release_goods_for_picking',
    "version": '3.0.3',
    "display_name": 'Release goods for picking Configuration Bulk Setup',
    "description": 'Applies a bulk release-goods-for-picking configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes and returns',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-release-goods-for-picking',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-release-goods-for-picking',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '13c12e383d231597',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/release-goods-for-picking'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/configure-release-goods-for-picking', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per release goods for picking target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for release goods for picking, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per release goods for picking target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk release-goods-for-picking configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes and returns', 'example_request': 'Run the release goods for picking bulk setup on USMF sandbox using this attached config spreadsheet.', 'inputs': [{'description': 'Attached Excel file with one row per release goods for picking target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-update release goods for picking settings in D365 F&SCM from a spreadsheet, with dry-run validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureReleaseGoodsForPicking(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReleaseGoodsForPicking'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per release goods for picking target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureReleaseGoodsForPicking().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
