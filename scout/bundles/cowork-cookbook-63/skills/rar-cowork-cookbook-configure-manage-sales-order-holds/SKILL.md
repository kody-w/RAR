---
name: "rar-cowork-cookbook-configure-manage-sales-order-holds"
description: "Reads an attached configuration Excel file of sales order hold changes for a D365 F&SCM legal entity, validates every row, emits a validation workbook, waits for approval, then applies changes and emits a before/after co"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_sales_order_holds", "rar_sha256": "e90a0834464de1f03e81a89262cd9448163ddf3f3b4ed95f38daef90cfcc3cf0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_sales_order_holds`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_sales_order_holds_agent.py` and in the RCI capsule.

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

Manage sales order holds Configuration Bulk Setup — Reads an attached configuration Excel file of sales order hold changes for a D365 F&SCM legal entity, validates every row, emits a validation workbook, waits for approval, then applies changes and emits a before/after co

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-sales-order-holds
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
    "config_workbook": {
      "description": "Attached Excel file with one row per sales order hold target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_sales_order_holds_agent.py` and embedded as the fenced Python below (sha256 e90a0834464de1f0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_sales_order_holds_agent.py` first:

```bash
python3 configure_manage_sales_order_holds_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_sales_order_holds_agent.py   # or on stdin
python3 configure_manage_sales_order_holds_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage sales order holds Configuration Bulk Setup — Reads an attached configuration Excel file of sales order hold changes for a D365 F&SCM legal entity, validates every row, emits a validation workbook, waits for approval, then applies changes and emits a before/after co

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-sales-order-holds
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_sales_order_holds',
    "version": '3.0.3',
    "display_name": 'Manage sales order holds Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of sales order hold changes for a D365 F&SCM legal entity, validates every row, emits a validation workbook, waits for approval, then applies changes and emits a before/after co',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-manage-sales-order-holds',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-sales-order-holds',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '79ec9887029260f5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/manage-sales-order-holds'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/configure-manage-sales-order-holds', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'config_workbook': 'Attached Excel file with one row per sales order hold target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for manage sales order holds, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per manage sales order holds target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of sales order hold changes for a D365 F&SCM legal entity, validates every row, emits a validation workbook, waits for approval, then applies changes and emits a before/after co', 'example_request': 'Bulk update sales order holds in USMF sandbox from this Excel file — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per sales order hold target and the new field values.', 'name': 'config_workbook'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to bulk-apply sales order hold configuration changes from an Excel file in Dynamics 365 F&SCM with a validation pass and approval gate.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureManageSalesOrderHolds(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageSalesOrderHolds'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'config_workbook': {'description': 'Attached Excel file with one row per sales order hold target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureManageSalesOrderHolds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebOjVrLnV9HcFzG2H1UXxCaojo4YCRCSEItYJVyOMvu+iEWAPP7uc5DurSq33a9fT8xfoypbgnNO7vnLzILfXpy+i6vm5dOLFjjlgnfyPImDZuGU/oKphqrJwFeVueC/hVeVXZO4fVc17cuHFz9ovSapu6QqwXE1cPwWHFs4Xed4ceDP28Mk6htn3rHgRi/IF2GSB4sqXLROHrSLqvEBq7jKwebYKSNwK6wA7wWLkcRi+z81RlzkQeTki6Dskm76sLg5eeI7HdgY3IJmWjTV8GERFEkHWL8vztxmwWeZPywGZ158kK3rpgJ7Piy6OCjnyzwBhN45zxq/U3IDcCCAnbAD8nkVUDYYnaIGMr98+vmXDy8J+P3y6bcXL3dacOuFeVM1EJ3SiQJt1k6eldsB3WZb5YAH2FdPwNgluK6DBnAowC0/CBdvVz+2QR5+WPznf2aD00TtT58+l4u3z+eX+Y/al7Psi65y2m62sFM7bpIDy7wu1vngTO2iCbq+KWcdWuCrMnp9nvxGqaoXf5/XfnwyeY2C7sfPLxUQ4WG5zy8/AbcAfk0//36dqdQ//vSaV0PQ/PjTNzpt76aB183EgNSvX96u38iCjd+2JuHii6ZwzBuvJvCSOgDEv9Nv/jxFfyP3ZpIvz80/VvWHxV9TnvX5O5D3GY0uoPvXZIENwMmX17RKyh/feIBwCEqn9IIff/pnZEEke1metN1/i+7PT8IxyAVgrTeT/PTh4b5fFtCbbl9p/nO2NQiYf0cTsP2d3VdD/TPaD8/+A+k8KUEKvPvyL8n91QHo74uf/6lu/9WBD4vw8wsb5AnIYsfNg0+L3x4h8vMP/rebP/zyOyD9L8loVd94DwpfCqdMwqDtvnz5+Yf2cfuHX37+oa9BFAdO8aVv8r+i+Vd2ffD5gwXfdv34x7OAv1FmZTWUi685tPitqv9H8/vrwpwB6dv99tPi+0ycP9BiVuKd6dME32VjC2T9zo4/vfwOsKcE2vTeYxngx3/8x0JMvKZqq7BbaF7Vdwvg4C4pgll4PU7aBfg7o0YzQ2abAMO+7QPxP3t4lhhA8q//y3vg/UfvDe/hdwAPZrsCWPvyQO0vD9T+MqN2++vrQgeUqyaJkhLAtLpWlM/z1rKbudZN0AbNDSCVO3XBR5DQH+cfi6Rc/PqviX950Hmtp18f2Jw8sU9l9jPutX0evM4aWjOWP/XxQPUJxsDrAYu88pxnuWk/AM3bKr8B3Jyt0WZJni/8BCALKGTTgzaw2KeZ2K+//uo6bfy5fAI1tnhWuBYGG76Ks/j4ESgW5kkUd5/LwIurxQ+//f7D4n8v/qtTD+IzDwWUjDd/AAkPmiwtQH71BdgGXAWcC8Dj4Y/ffn8zLyBTgjoEvJeEc8WaD4P4zAL/3dbabv0RJci3urUA5alqOoD+i6R7XezDxVd5AdN5aa4PcdV2Cz+og9IPSm8CVB2gzldLllUHqnSXtCEou30bPLj+6jbOQ8QCJLrT/boQGQVUoyoH/5vFfGwCh6syAeb/GgnP+4BI80O72LyTeF1Ic0Quaqdx6rhx3niEztMvc8V+Ow6IO4syGD6Xc+ENZlM90uNpHrAJWMZ7c+nHR4vhVQUIK7995/3Y48w1U3/UzuZz2b6FvtPMrvCqRz8R9aCDAAXhb28h1cZVD7qT2X5A0pnSmxf8N688YvBZ9f/U1LQL5g8t0KbPs4UGYKRefO5RZIkv/n9ummbDrHle5fi1zrELTtLVy9Nhcx85O/bZegIRH5weyfmto3lHrXfw/lzmCYi+Zvrbc+fDKG97noAIsMQHCKQ+6IMYA1LMdB8pMId008ySO5/L9yrxYVZ/hkSgO8ALkE9zGL8znFffJY0BKMzX3zqGR8g0/mwAEOaLundzEIJhEPiu42VAqmZO4zc3g3x4OHCIEy/+g1azj4BHAP0FEGK2I6gkr1+R+7n6LvofDj4bo/nIo2nsyzkqZgJAjmAWcHbNkHQAzEBwPdp2oOenBxGgRlF3s+4u8Hzx4e1m0ATXPmmTbsbMp12DGiD2x/n7qel8NxhrkDrAWCBB6h5Y95FSM9oUoO0BMgBUASFQJCVoA4BR3ozwIOgUMz4A/H3rU58UH7ffFHqG6Fy/3g/Oisxn5pZgEQLRwZ3pexjR/ypMAL1i3vHg+4+R9pXbTHuG0hYkFOD4vvrsHV6f5f/ZXyze6X7601z04783Oj0KuvHHAPi0iLuubj/B8LMIv9fgVwBk8FPW9ls9/vgsmR8fgPDxAQgfH4DzB8pPpT8t/j3p/kDiLTs+LZavyCsyLx3fouvtA4zBfNxcPuLz6udSDb4BLWBfFSC8ZtdNoAH4WhXft4DSGDUAqMDmZ5Vs5+I6AJh5lAXgh8/l9+E+p9sb7nwAHvoOBh7tAQj9p9u+Vi+wVHaAtz83lFHwOs9hs/ht8PKp7PP8w0sJAu+/M77NJaqYg7qdpz6QPqBB65LgcfWOkPPvP47E3AjA0gP5MFe+r0i6eAIk6MaSYJiz5lFV/gqF36r5HO1f8Xa+fmCwP6vTTfUs/3PUm5vDZ4h8eafxZ5nW74Xmu9Iyo8RihihQGOZZ9M+FpgMdStA97DxLC0oxOBmABSB3H7T/TJQuGLs/iyA/fjj564INAE7n7fcJ+VZw54bjO9x4eh943QOW/7B4FjOQq0D82Skz5jht9qhYfynLox5+edbDPwv0KJzfl8z3bsaJHhiz+DF4jV4XhiZuf/rbQzQwXQNbuNUIDtySpirnlgRI07TdX/L/2tD/mbkF+qiZn199mnl+eANn8A2GsA+Lr/MU0Pptwp05BGVfvHz6eZ7l5vB8HJl/gDPg6+uhr/9K4wYvv/xJLiDYA/FB3ZxpfRPy29bqMQPOKgDS3fOfLH57AangAB84b8nwNkSA7QAgP7Zz4wQDwADMwfUztcHa/8V48UahjR3Q3AISAY04CIXhOIn7wTJEsIBaOhSNkqjn0zhOLUnM90MsxFw88GkixCjfCUIa8ULPw7xwlugJEV/m/jCZpZpFAsb4CFAm+LYMbvlv6jzFn231dZp5ZP1Tq99eXBIHO3d4u18/PwwMLcHNlTsdzlBDBpUobgQv0YXCzw/i7UCKZ2e10o1TgI+9PjhsmjHn6XDknEuTUdKhq/ztepcclIIJ7RUxXfEc813LL72WczZ5lVwR0pfr8HYWmkwWV1V6uedmlXtqUp011al0edIEMd1q6uE2FKg9aQfxcuOplFlte60RTOXeHTHKtJE6SfbT9rhu6tXyFMGSOyA4BCXtqUgP6l5KsWTo4EOw73bFdNKN5o5TpR8mdgh759WkZupVmOQYT/Ytm0rjwRGHbG3w16Q3d4ZmnUWIQytvmzeXm+Oem8Ox8w5Umevb8Ri0eYbc1aPIX4qkRgXSao2o3viWZ29Uq+hEjusI4bIOMXzi0+WKBllOS9adJr3bKJcujXpwLx9pveNkBlsX9rZss2gQqbTZHiPVLLx6yUvcPRRlpsru930uTQreML7m3IdRpDPGTOJisyZVP9/0vK/oXUqlgjicBJU9decbQ6xlsd+7eulM99S7HqcL4ttm3slQRWnwKA/J1XbSjnCV0hsx+oBlFb+3IaTOpsqzHEVMFQY+G0FyTM3jxrpdz/g6M9a5fStFre3lzidl2oGmnX/ayNHRW68nDSLSDlNJFuv0Brorx6C4BMZg6upGtXtb4OVpY1fyNtZGNboSbHXzmY1jxkGvbY9dxvcbuBwdhNTPxs2G7HiqdYUw4127p+zMCYQavbGYQk7LPouhOr3eBuaUNcI+QeKlEhzu+3bAqivN7qOQ05IqVGF+r65Wt11bHG7hqd8PibfG/TEsqqC4olWGaCxTBKpy14NjwcepH/EGJeNlxucXIb7pTtzk1npZ4zx1OPg9WVv77qDyW7jwNmRrd3Ch2SXBNPszXg8wk3VLJvDykmLCeLNkdRE3S8UwoXWHceyortZ43KK7zWGZQRsPu6FxDfB/qdZKPrXhhgCdUtGfyemMxjyFG9u1fg5F8i6ioVKulPwe10ZxcTFwKkKwujJSRmxHC/ZHYPabUqSt5t5ZfI8XOgxfQjIM2Iw0lu2WJg4Za0YAZGRH48Vdq5N7TISZTozOfhWVHd2Kl72+gdaRSvAEGbFwJKmXHLpATpctAxtk7aY1kPKAoicMtEUnQ08COePYPBhPlsVmwglFhCPbbHBiV1p3fakoGwPb01cuG6SIpg82k3hsKqJ2eTLRlXhHoDG2EjdM3ZVaEPll2ekV1ZxIZRnwo5yO1kgnJ3G/z4ScZvIt7BAIf6kJjgp2zkHHcWur8fnBGizoHMg7zD2izVh3BF3gOxvaux5h55A43KPqYlW7I0IlY3se9f39bF+IKAu8AFX0MSeIuhZUJQ/cOqFtLDtH0D7a0wwvM8rG4rI9Rt86S6tJeLMOKhn2J/bMomYdyCbupTuIR7WdFSupnpnjHTKzQohMXBPoYVmhB28su2jDSpmtb9mtudKWpmX4V+PAJTt0XxzwFUYw+ZG+TCyGgcqE21BxG5uoLptbHF1q5BxvNwJ14qw1tMyck9tDEbf3ypQ5RtNOEnW0Es9xNfJuO1ZlKx4o9qYgR2TrxDVf9BrBogzbHtqU0QPOOaBneHNTHMc1tuYmYQgIuhstdvWxK7UdbMdgsN0uDHfWKWx5cbWeWOHoyGvfkVDPls8pYfLE0rl7G4hnEYgO6YAbLyWz2WT7EWW9nXciVQfOL7cNjet3ndH1JGO106beEhpGJ/ImIxvRYDGd8+Ni6W5OGSGPihhuNhc1w4ZSHLBJrNm9kSRb7oIY9rXSo0kFgd7coQZtsjuq76diXQ7lHafHTG6k3svEQ2rwnp/aOmFotG0gJ6ONpCwgTgMjllye116E7iX22CgVR4/INhPXSNW47Ops7OMrweymauttqDhST1KXjjcHK45LrwWaRtulhUtIQsgg1u6W4R4C40jeIVlpMlrGCNLjpDoXOGjQr8qBMPc5v9epwnOPN0NNhlPCQGcpHVcVRXAyhF5OfqcwPAvdsPN0gwFEwjgciLfbbZX4OIWdx2Il1rLHgCgm2oA5nuJh0xUahstufj8KW2d77aWCC+Nsw9o+zezJqG4rSDkzyy0PqbGsSLdkqOJdyUF+dDle18EqbrTr+toRCNvIDr9ko5PBrYY2Ule7LScjwXg+lLyyvqY8P2QjPAnHW6mUyVWUe+uwzXSblLhAyg/D1aYpIz449HUUGmE0JXslx2ZB8Dt8be2JzUYN45znLKyw+5EVqBy6sxy/PUjJ/XzLbtzhhg3NgBeXNjwR9IEb9qghnhh98k9ojK4IF1sZd0Q7nGpCRR1GuVPIFEUFHa8YTUi6pT+SJ46ja3qz33pbHrUsdbOaCkW492Ka5+GxQrDl3SQienlzG295jNY6Koh9qPLmPiVRByay/V6zzI2tgHrfCKdpn6jevj9f7MvZGyGo8nZ1PR7s3ca8iEutkirtpk3r2uunC85KZ23ERCqkycPQZvHe3N745T6NagbSrUnc++F+RM4NYmQTnYb8uRnua32UTkhKyGWpqgWXmOkl5pH4Xi6j42pzyimnyI8Qv9OFap1BQyTsuILr8tMScxribAiatGV1+9yiviCfQYJQUOfsE+92V2xVM256lIYxe0JQVWPEHD5eUUfNmrOLWBFXZX1wRTv17O0RLqnUVSdmAqXeg5smltVglGsxXnGIlh+2ZDGebtyg8cg0sqnnGB1zvDJeK0iDvORscsfH9XJC1DN00Ia7eAo82/Au+VWpzxQyCoYq7I6VDkN5eYk2dCKi9QXbjY1Gkve97lvF7tKT7jSd8LtAnY/8RmEpGOlybNQPUbWtGK8JzjfXHI3s7GopvIlZrgkg96ZnQ7djMd/SyU02wRGVmLu68/01l7IFFhUSmliba1DHWRtVRmQxyx25UXLMMC61jTZSoB5Y/LJHSJ7Vt36RXggJUT2EN/FlXEzbtkMPlRgNFasVlyXW0I29yY+UJ+CdkByFINcjiSE2ulddGZVxI2SsCE0otqSbKJx2bGP5TuOHVE0vcpp3J1mGl5fs6BT0kCVQc7ezQqfP7ulAsMb6eEyuMVPfCj1cN91gSdezqQhlK9EX2IXZidJu9KRXdutdnJ1ei8YuuHVdsyWySjYmeCcZ1eXKEnuZy6IDcvO1S7KywzIVBdMpJlM1akbN3X61Z7lWM/eJtObB5HHeorf8QrRiLa12J7PjjNtKDtE9010UBt+eLDvATnnQFW4lLHXD3gbLsWV1y9QIrHOqRN7KhbheeX3fIKvN6NB20a3G1lTU1vDVWE2Hru2WcEgO6brgYGqUK0cczYDkNsBMMpeMLpHfWkEsj1uGwHbSqisn3jzeRa2/Qk7QRJa6h/sTnd2rbbRDGAiP0sNERqkAEyy+PlKmv7FFFdnVLUYtrfXKjCqtBNYMVyOnEdbSp3x4VRDh6dBM0zje48thpEZca8SsTsR10Ma3JjMCAd21nYC7JGtiIMvbndP0Nb0dLldpKJELNRKVdyeRkMtpQyHWuLot9CKZ6qst9hSmrQSlTVcqarf7GwORF6K7QwSOlxvCXO9KUCJNMBuczcjwNN8C8bA10BNzILeRFVm1sAwVHoNgZI21A29ax+heHo93yatGs+3KqDdoCkTHTl3mBBYQvhdaTrUkll3t5FnMx6ujYW06FxWgQqT4Dj6FSxQB2VS1WBhql8CMw0Z3A2/pjgda5q+rbtja0VpZE60QchvxNISHq73d8pHT607Zs6ykyGO6Ro11VyrC2jBP3DVRV56IYIW1z3aaEXETcmo248biuc16HOXCYVgnObYad6v0oQ1s854jQagGg1wxqR04BXmfKPXqlY50Fq6VtryEuGCK18ZSwIi49FRrG6pOEjbVJm7cjtyek5Vr2kdNg8OVjfq3s7uE7FLy1rvbHohzuA9hqZ+Paht5He4mybA/Q0ehlXjXR6vL2u0l9iYEttJJOZg6JnmnaKf8tLkX7Mq1e5pQx86cHAr0o/D12A8URDKj2zackTGYIvdiNErSlb0HPtstY0jdmqVhd8Ja001rndxJaXefuuVJVq0d7dnnrQsmbbuI4rvOro5suV6vlh7sqTh8gYb6ehQO7akzUt7GeNM8s8TAti58Ibbquro3Q3QxtUEJ0LTszlcV6brIxvo2wV0P40ztijJdH3dXjtkwpWv1rc1TqlAFtmBB4dTM4WDsmDYYtyaOYZRL02DMiFIaLTJlv1fr83kbj1unjZRhc5GKSZiomJlMzMliJqu81YFEdlBe8CdmaxhbdysY66YnywFV75h5qyYFLic8qNLr1T2WhjYWJh3jNxgftKI9V42p1g4U+/vThNxMMMprK1yytrpaieEpO639FF+nQUkz9YqgdGa9zOhA00dRu1/Zgm+bVZnyniUXLC446OW8ZsmL3At15+oFdq6IvVpqasWIKXv0D74xcQOZwA3T7qL1oDjwpNCcoysTbCkaZ9GaQEpmEE9VqaDubQPffeZgVAMprCrpElFUruOaovkr6OCK+Jnam4m9zCkNUeL7TrbEHY7qfJcybeifStVeFoV4K4dKpPPMVmo/V3gfltBzjDQiPSFQw6BbJU9uWgu79V3sBqp3ieq2HJf2ypGjtNV5CCKpVdLXXusEQW8051q5n3DywNGXliJbBd9PXg1mv5oZTRWD9ygrSIWPSHhI9zm9hvH9xj5EoYEqGKQkhAPhGzetc4ihTsuTc7kq1f00jpQ+INRxU2UaGELNGq4qQ93ureVK6hKY9NOqTSMQ8rC7CoopYLuIXjkFflWWTiT5G/Qm3oTlpmr1YfLVbn+B+ejurHUuKEgYxYCntzBlyqpW1uYZpnM4DQfQ9u2y4QbBe2dVixh1cBhQ50mDmUKZv7RM0u+4O0xWCiopk1mTbO/Dqb/aaeuzVncVnpC8jmwmLV3FoIac6UMu11cgvOEqZ8U2GgaqSTdI761kraUshnGfoV1cJAaskDeDdoErSSbT+3lKEBdT4X4UMXPlZ/v1WMPQElnSCO7Hhx0iGd1u75SYfrHFeHPXpQOea9wmYKrezBRNWi4xLDwgZtv3PZ9eEDJIkHwbeo0K8YfwStCWglWXI7T1R3G/zU77Jhs86VZa+dkva+qEDNyGRzv2FDVVi0fTpaJbWlgioXA9Lk/0/dqskU277K7SrrsFqQlnUl7u9gMHIyvBunMNpW7Hbpdsbm1yOHOTgxetWvlFSMrplWNtpo1EluHJi4U1TRKbkntiQ8tnhItMyjrlWQcx0qXgdLjhrqWw6LoM+07W5KPjK+VaPmw4lxjRPMRdA7lD53SkYepybvpbxZpDFqt0cVphSnU770KNjdhRqCDizu28e0s1x2sx3AZs5135pCA1R7RDWaQpuQ9ThtqRspDE/dCPXBpAmauEHsvRSF50RWbbZ+98PTiazcLSlcDcIu60q0uSaZeNvXVT+LulaRzvT0s1j5rIjTH3lDYCzuzAVOMndl8eFDJJgxBhkCb1DYB6rEwak7tc+9LyovOoKbuEWSF0mOMWXoknHHh476QgQ2JzonZ3aWC4g5H4++0K9aPxuGcpJERGJpAOqnUidz6WCrulegNdO+1zhoRdtzwdsfqxh6bKkWjSWR7H4XZFS0lGbezeKFhinHfKTb/D3aknhpV/X19tyB2xhoAUXkiWo+wdQ8E8l/QA4aGGNmF4ResrDpMC1hsgxTg53w36CbEBWnihKVNoHkAbprmCWc2Y4nJDIl5xds3O6iiOb8hE4nMHX4LpnJVrz5fXcig5q8ifVtKOQlMQP5E+wJMUyePJqwt7LW2cmLX6cXdmq4NKGsD4yu2UykJ4nKhh3V3M4b4j7OqUrML2EKqsfIxHKdZZSBPckxGEYa5vjEJTfFRmWG3Mt8K1S5BwChT5sIdYsZUSogq3dttnXbZctZyL9sOdPV0LTHITqqTqFSr06i5AERFby5VbI92oT0yGxNepB0G/5DN/kGJIloT0vkYuTAr1ULjbUzmJuAAG83BHiwziXjD/AFUFmuO8ETjd1jrQvsOUAcaCGoxkRH73LbS5jBZ0o2TdFhy1aL0TzO6k4jygrsV3J6QIcsThdxkukifnLAdBS2K+mHur5dblqt5dCXsoMux4eWAPSKhhWdijHA23mrRfCRsbzOAiZwiWNZI6mCRW7V4rCErdW5iva/WN8W6skkniyiqoODVTB1q6GY4IaLlZssUmPLPXfQ+PR/8aeAkdDN5GuhH3qR1QByf3+kZqDpJAT2s+RNhDtdsq3g2GJOqO+hdpo6yhXCbWaHU+gqmhbFw3WZmyYa2CVSFR0wRLQibuctqasLOC94Rn1JCtGMzYQEV/UvUx0e82r9o9vykStQStzJVECQYGIIQJQcy7OyJByJFc3hSbLnDvAGeMhooiYhyiFg0issMugbOTWDrSMLkiNixoUYiDTW+Y40ZufQ5h79Utb9eenFr41gpdSeqxPksrpBRiJKYMSY+dVWOUu7PvggE0nQz/rtrs0lFwacvQNm7BDQkaVjjlA3MbRs61ufd2N55vyHLVmN6BusFU6fnXZApRbL2yWzUCbeXoobu14IDxvLT82zbXRVNduidLQkryCt2tM3O9lpSioE0ut0S1XF+pnUx2JGGtUquDdV3nb5xCTSBL9JTIuZXEp+e4LtIYOg7BTfeFW18kq3vhUySyyva7KRxIR8xPJxbU7sGph4JcJwf8WlWRhFx7MtSjwTB9DqIdR+PKtFM2uUhzyM5m0CzeqgOlTFmgTbyN7BIVOzLwFVG7/n68qE2/ClmNQrO9EeAEGJvqZU9prIQju5zN6p2zum9ul3vP1JlyclOzVLXr/nrx12eDkLarJUlcd6NPw2w5OJkOenohCGNDCsEYP9DplEoKSZOQFvBDri/xA9d5hL5yVjoSUkySrgwzyrn1ev33lw8v8+PRt2fE/8b7avNzpP9nj6yeT57eXzt5PPMLHP/Tg9enf0eoXz68NF4CRHo+mmvzPnp7xPUPD+Y+/uv3DObz0/M1sPenvM8H6p0Tza9IvySl37ddM31pq/zx4gk44YLOvQzadn7v1gPf3z+4/MoS/H5K31VfPKeNX+YXHue3SQI/cbrg7TJ6e1D54cWfgH8Sr/2CkcSXoKlnNd/eWgDaYa/IK/by+/8Bt91H+eYuAAA= -->
