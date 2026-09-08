---
name: "rar-cowork-cookbook-configure-receive-goods"
description: "Reads an attached Excel file of receive-goods configuration rows against Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies changes and returns a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_receive_goods", "rar_sha256": "85aa9015fa9fbc2359cf20d35d54597e7bf9975b98f48caa2b8f0bb4b28c8254", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
