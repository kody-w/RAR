---
name: "rar-cowork-cookbook-configure-receive-goods"
description: "Reads an attached Excel file of receive-goods configuration rows against Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies changes and returns a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_receive_goods", "rar_sha256": "85aa9015fa9fbc2359cf20d35d54597e7bf9975b98f48caa2b8f0bb4b28c8254", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_receive_goods`. The original RAPP
agent is preserved byte-for-byte in `configure_receive_goods_agent.py` and in the RCI capsule.

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

Receive goods Configuration Bulk Setup — Reads an attached Excel file of receive-goods configuration rows against Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies changes and returns a

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-receive-goods
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
      "description": "Explicit user confirmation after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_workbook": {
      "description": "Excel file with one row per receive goods target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; defaults to USMF sandbox.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_receive_goods_agent.py` and embedded as the fenced Python below (sha256 85aa9015fa9fbc23…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_receive_goods_agent.py` first:

```bash
python3 configure_receive_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_receive_goods_agent.py   # or on stdin
python3 configure_receive_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Receive goods Configuration Bulk Setup — Reads an attached Excel file of receive-goods configuration rows against Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies changes and returns a

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-receive-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_receive_goods',
    "version": '3.0.3',
    "display_name": 'Receive goods Configuration Bulk Setup',
    "description": 'Reads an attached Excel file of receive-goods configuration rows against Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies changes and returns a',
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
        "upstream_slug": 'configure-receive-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-receive-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1faebd3176bbb5d1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-inbound-goods/receive-goods'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/configure-receive-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user confirmation after reviewing the validation workbook, before changes are applied.', 'configuration_workbook': 'Excel file with one row per receive goods target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for receive goods, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per receive goods target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached Excel file of receive-goods configuration rows against Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies changes and returns a', 'example_request': 'Bulk update our receive goods config in USMF sandbox from this Excel file — validate first and show me before I approve.', 'inputs': [{'description': 'Excel file with one row per receive goods target and the new field values.', 'name': 'configuration_workbook'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit user confirmation after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to bulk-update receive goods configuration in D365 from a spreadsheet, with dry-run validation and approval before any data is written.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureReceiveGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReceiveGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user confirmation after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_workbook': {'description': 'Excel file with one row per receive goods target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureReceiveGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
