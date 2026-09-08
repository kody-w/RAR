---
name: "rar-cowork-cookbook-configure-release-goods-for-picking"
description: "Applies a bulk release-goods-for-picking configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes and returns"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_release_goods_for_picking", "rar_sha256": "67e0aea5147dfeb00dbb59ed5444132583fc2d2c72b77183aa6dffcc50b30e5f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
