---
name: "rar-cowork-cookbook-configure-manage-sales-order-holds"
description: "Reads an attached configuration Excel file of sales order hold changes for a D365 F&SCM legal entity, validates every row, emits a validation workbook, waits for approval, then applies changes and emits a before/after co"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_sales_order_holds", "rar_sha256": "e90a0834464de1f03e81a89262cd9448163ddf3f3b4ed95f38daef90cfcc3cf0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916eZOjVrbnV9Hkixjbj6oUYqc6OmIkQEhCLGKVcDnK7PsiFgHy+LvPRcqsKrfdr19PzF+jzCqx3Hv28zvnJPz24vRdXDUvn160wCkXvJPnSRw0C6f0F0w1VE0GvqrMBf8WXlV2TeL2XdW0Lx9e/KD1mqTukqoE29XA8VuwbeF0nePFgT8vD5Oob5x5xYIbvSBfhEkeLKpw0Tp50C6qxges4ioHi2OnjMClsAK8FyxK4Ivt/9QYcZEHkZMvgrJLuunD4ubkie90YGFwC5pp0VTDh0VQJB1g/X5z5jYLPsv8YTE4880H2bpuKrDmw6KLg3I+zRNA6J3zrPE7JTcAG4KlE3ZAPq8CygajU9RA5pdPP//y4SUBxy+ffnvxcqcFl16YN1UD0SmdKNBm7eRZuR3QbbZVDniAdfUEjF2C8zpoAIcCXPKDcPF29mMb5OGHxX/+ZzY4TdT+9OlzuXj7fH6Zf9S+nGVfdJXTdrOFndpxkxxY5nWxzgdnahdN0PVNOevQAl+V0etz5zdKVb34+3zvxyeT1yjofvz8UgERHpb7/PITcAvg1/Tz8etMpf7xp9e8GoLmx5++0Wl7Nw28biYGpH798nb+RhYs/LY0CRdfNIVj3ng1gZfUASD+nX7z5yn6G7k3k3x5Lv6xqj8s/pryrM/fgbzPaHQB3b8mC2wAdr68plVS/vjGA4RDUDqlF/z40z8jCyLZy/Kk7f5bdH9+Eo5BLgBrvZnkpw8P9/2ygN50+0rzn7OtQcD8O5qA5e/svhrqn9F+ePYfSOdJCVLg3Zd/Se6vNkB/X/z8T3X7rzZ8WISfX9ggT0AWO24efFr89giRn3/wv1384ZffAel/SUar+sZ7UPhSOGUSBm335cvPP7SPyz/88vMPfQ2iOHCKL32T/xXNv7Lrg88fLPi26sc/7gX8jTIrq6FcfM2hxW9V/T+a318X5gxI3663nxbfZ+L8gRazEu9Mnyb4LhtbIOt3dvzp5XeAPSXQpvcetwF+/Md/LMTEa6q2CruF5lV9twAO7pIimIXX46RdgN8ZNZoZMtsEGPZtHYj/2cOzxACSf/1f3gPvP3pveL98B/BgtiuAtS8P1P7yQO0vM2q3v74udEC5apIoKQFMq2tF+TwvLbuZa90EbdDcAFK5Uxd8BAn9cT5YJOXi139N/MuDzms9/frA5uSJfSqzn3Gv7fPgddbQmrH8qY8Hqk8wBl4PWOSV5zzLTfsBaN5W+Q3g5myNNkvyfOEnAFlAIZsetIHFPs3Efv31V9dp48/lE6jRxbPCtUuw4Ks4i48fgWJhnkRx97kMvLha/PDb7z8s/vfiv9r1ID7zUEDJePMHkPCgydIC5FdfgGXAVcC5ADwe/vjt9zfzAjIlqEPAe0k4V6x5M4jPLPDfba3t1h8RnHirWwtQnqqmA+i/SLrXxT5cfJUXMJ1vzfUhrtpu4Qd1UPpB6U2AqgPU+WrJsupAle6SNgRlt2+DB9df3cZ5iFiARHe6Xxcio4BqVOXgv1nMxyKwuSoTYP6vkfC8Dog0P7SLzTuJ14U0R+SidhqnjhvnjUfoPP0yV+y37YC4syiD4XM5F95gNtUjPZ7mAYuAZbw3l358tBheVYCw8tt33o81zlwz9UftbD6X7VvoO83sCq969BNRDzoIUBD+9hZSbVz1oDuZ7QcknSm9ecF/88ojBp9V/09NTbtg/tACbfo8W2gARurF5x6BV9ji/+emaTbMmudVjl/rHLvgJF29PB0295GzY5+tJxDxwemRnN86mnfUegfvz2WegOhrpr89Vz6M8rbmCYgAS3yAQOqDPogxIMVM95ECc0g3zSy587l8rxIfZvVnSAS6A7wA+TSH8TvD+e67pDEAhfn8W8fwCJnGnw0AwnxR924OQjAMAt91vAxI1cxp/OZmkA8PBw5x4sV/0Gr2EfAIoL8AQsx2BJXk9StyP+++i/6Hjc/GaN7yaBr7co6KmQCQI5gFnF0zJB0AMxBcj7Yd6PnpQQSoUdTdrLsLPF98eLsYNMG1T9qkmzHzadegBoj9cf5+ajpfDcYapA4wFkiQugfWfaTUjDYFaHuADABVQAgUSQnaAGCUNyM8CDrFjA8Af9/61CfFx+U3hZ4hOtev942zIvOeuSVYhEB0cGX6Hkb0vwoTQK+YVzz4/mOkfeU2056htAUJBTi+3332Dq/P8v/sLxbvdD/9aS768d8bnR4F3fhjAHxaxF1Xt5+Wy2cRfq/BrwDIlk9Z22/1+OOzZH58AMLHByB8fADOHyg/lf60+Pek+wOJt+z4tFi9wq/wfOv4Fl1vH2AM5uPm8hGb734u1eAb0AL2VQHCa3bdBBqAr1XxfQkojVEDgAosflbJdi6uA4CZR1kAfvhcfh/uc7q94c4H4KHvYODRHoDQf7rta/UCt8oO8PbnhjIKXuc5bBa/DV4+lX2ef3gpQeD9d8a3uUQVc1C389QH0gc0aF0SPM7eEXI+/uNIzI0ALD2QD3Pl+4qkiydAgm4sCYY5ax5V5a9Q+K2az9H+FW/n8wcG+7M63VTP8j9Hvbk5fIbIl3caf5Zp/V5ovistM0osZogChWGeRf9caDrQoQTdw86ztKAUg50BuAHk7oP2n4nSBWP3ZxHkx4GTvy7YAOB03n6fkG8Fd244vsONp/eB1z1g+Q+LZzEDuQrEn50yY47TZo+K9ZeyPOrhl2c9/LNAj8L5fcl872ac6IExix+D1+h1YWji9qe/PUQD0zWwhVuNYMMtaapybkmANE3b/SX/rw39n5lboI+a+fnVp5nnhzdwBt9gCPuw+DpPAa3fJtyZQ1D2xcunn+dZbg7Px5b5AOwBX183ff0rjRu8/PInuYBgD8QHdXOm9U3Ib0urxww4qwBId88/Wfz2AlLBAT5w3pLhbYgAywFAfmznxmkJAAMwB+fP1Ab3/i/GizcKbeyA5haQCGjYgSkUwwjMD1YhjAbUyqFohEA8n8YwakWgvh+iIepigU/jIUr5ThDSsBd6HuqFs0RPiPgy94fJLBVOkyFM00iIrRDY94MQwXyfIijCw0kEdmjXwV2cdtxvW7Ok9N9Ufao22/HrpPNAhKfGv724BAZW7rB2v35+mCW0AhdJdzqcoYYIKlHcCF6iC4WfH8TbgRDPDknqxinAxl4fHDbNmPN0OHLOpcko6dBV/na9Sw5KwYQ2iU9XLEd91/JLr+WcTV4lV5jw5Tq8nYUmk0WySi/33KxyT02qs6Y6lS5PmiCmW0093IYCsSftIF5uPJUy5LbXGsFU7t0RpUwbrpNkP22P66YmV6doKbkDjEFQ0p6K9KDupRRNhm55CPbdrphOutHcMar0w8QOl96ZnNRMvQqTHGPJvmVTaTw44pCtDf6a9ObO0KyzCHFI5W3z5nJz3HNzOHbegSpzfTsegzbP4Lt6FPlLkdSIQFitEdUb3/LsjWoVnchxHS5c1iGKTXy6ImmAALRk3WnCu41y6dKIt+zlI613nMyg68Lelm0WDSKVNttjpJqFV694ibuHosxU2f2+z6VJwRrG15z7MIp0xphJXGzWhOrnm573Fb1LqVQQh5OgsqfufGPwtSz2e1cvnemeetfjdIF928w7GaoobTnKQ3K1nbTDXaX0RpQ+oFnF720IrrOp8ixHEVOFWZ6NIDmm5nFj3a5nbJ0Z69y+laLW9nLnEzLtQNPOP23k6Oit15MG4WmHqgSLdnoD3ZVjUFwCYzB1daPavS3w8rSxK3kba6MaXXG2uvnMxjHjoNe2xy7j+82yHB2Y0M/GzYbseKp1BTfjXbun7MwJhBq5sahCTKs+i6E6vd4G5pQ1wj6B45USHO77dkCrK83uo5DTkipUl/xeJcnbri0Ot/DU74fEW2P+GBZVUFyRKoM1likCVbnrwbHg49SPeIOSsTLj84sQ33QnbnJrvaoxnjoc/J6orX13UPntsvA2RGt3y0KzS5xp9mesHpZM1q2YwMtLignjzYrVRcwsFcOE1h3KsaNKrrG4RXabwyqDNh56Q+Ia1IaVWiv51IYbHHRRRX8mpjMS8xRmbNf6ORSJu4iESkkq+T2ujeLiomBXBKN1ZaSM2I7W0h+B2W9Kkbaae2exPVboy+UlJMKAzQhj1W5p/JCxZgQASHY0Xty1OrFHxSXTidHZr6Kyo1vxstc30DpScR4nInYZSeolhy6Q02WrwAZZu2kNuDwgyAkFLdPJ0JNAzjg2D8aTZbGZcEJg4cg2GwzfldZdXynKxkD39JXLBimi6YPNJB6biohdnkyEFO8wNMZW4oapS6oFnl9WnV5RzYlQVgE/yulojXRyEvf7TMhpJt8uHRzmLzXOUcHOOegYZm01Pj9YgwWdA3mHukekGesOpwtsZ0N718PtHBKHe1RdrGp3hKlkbM+jvr+f7QseZYEXIIo+5jhe14Kq5IFbJ7SNZucI2kd7muFlRtlYXLZH6VtnaTWx3KyDSl76E3tmEbMOZBPz0h3EI9rOipVUz8zxDplZIUQmpgn0sKqQgzeWXbRhpczWt+zWJLWVaRn+1ThwyQ7ZFweMRHEmP9KXiUVRULUwGypuYxPVZXOLo0sNn+PtRqBOnLWGVplzcnso4vZemTLHaNpJoo5U4jmuRt5tx6psxQPF3hT4CG+duOaLXsNZhGHbQ5syesA5B+S83NwUx3GNrblJGByC7kaLXn30Sm0H2zEYdLcLw511ClteJNcTKxwdee07EuLZ8jnFTR5fOXdvA/EsDNEhHXDjpWQ2m2w/Iqy3806E6izzy21DY/pdZ3Q9yVjttKm3uIbSibzJiEY0WFTn/LhYuZtThsujIoabzUXN0KEUB3QSa3ZvJMmWu8CGfa30aFJBoDd3qEGa7I7o+6lYl0N5x+gxkxup9zLxkBq856e2jhsabRvwyWgjKQvw08CIJZfntRche4k9NkrF0SO8zcQ1XDUuS56NfXzFmd1Ubb0NFUfqSerS8eagxXHltUDTaLuyMAlOcBnE2t0y3ENgHIk7JCtNRssoTnicVOcCBw36VTng5j7n9zpVeO7xZqjJcEoY6CylI1lROCdDyOXkdwrDs9ANPU+3JYDIJbYMxNvtRiY+RqHnsSDFWvYYEMV4GzDHUzxsukJDMdnN70dh62yvvVRwYZxtWNunmT0R1W0FKWdmteUhNZYV6ZYMVbwrOciPLsfrOiDjRruurx0Os43s8Cs2OhkcObSRSu62nAwH4/lQ8sr6mvL8kI3LSTjeSqVMrqLcW4dtptuExAVSfhiuNk0Z8cGhr6PQCKMp2aQcmwXO77C1tcc3GzWMc56z0MLuR1agcujOcvz2ICX38y27cYcbOjQDVlza8ITTB27YI4Z4YvTJPyExQuIuShp3WDucalxFHEa5U/AURQUdk4wmJN3KH4kTx9E1vdlvvS2PWJa6IadCEe69mOZ5eKxgdHU38Yhe3dzGWx2jtY4IYh+qvLlPCcRZ4tl+r1nmxlZAvW+E07RPVG/fny/25eyNEFR5u7oeD/ZuY17ElVZJlXbTpnXt9dMFY6WzNqIiFdLEYWizeG9ub/xqn0Y1A+nWJO79cD/C5wY2solOQ/7cDPe1PkonOMXlslTVgkvM9BLzcHwvV9GR3JxyyinyI8TvdKFaZ9AQCTuu4Lr8tEKdBj8bgiZtWd0+t4gvyGeQIBTUOfvEu90VW9WMmx6lYcyeYETVGDFfHq+Io2bN2YWtiKuyPrginXr29jCXVCrZiZlAqffgpollNRjlWoxJDtbyw5YoxtONGzQenkY29RyjY45XxmsFaZBXnE3s+LheTbB6hg7acBdPgWcb3iW/KvWZgkfBUIXdsdKXUF5eog2diEh9QXdjoxHEfa/7VrG79IQ7TSfsLlDnI79RWGoJdzk66oeo2laM1wTnm2uORnZ2tXS5iVmuCSD3pmdDt2NR39KJTTYtIyoxd3Xn+2suZQs0KiQksTbXoI6zNqqMyGJWO2Kj5KhhXGobaaRAPbDYZQ8TPKtv/SK94BKsejBvYqu4mLZthxwqMRoqVisuK7ShG3uTHylPwDohOQpBrkcSg290r7oyKuNG8FjhmlBsCTdROO3YxvKdxg6pml7kNO9OsrxcXbKjU9BDlkDN3c4KnT67pwPOGuvjMbnGTH0r9HDddIMlXc+mIpStRF+W7pKdKO1GT3plt97F2em1aOyCW9c1WzyrZGNa7iSjulxZfC9zWXSAb752SUg7LFNRMJ1iMlWjZtTc7ck9y7WauU+kNQ+mkvMWueUXvBVridydzI4zbqQcInumuygMtj1ZdoCe8qAr3EpY6Ya9DVZjy+qWqeFo51SJvJULcU16fd/A5GZ0aLvoyLE1FbU1fDVW06Fru9UyJIZ0XXBLapQrRxzNgOA2wEwyl4wunt9aQSyPWwZHdxLZlRNvHu+i1l8hJ2giS90v+xOd3atttIMZCIvSw0REqbDEWWx9pEx/Y4sqvKtblFpZa9KMKq0E1gzJkdNwa+VT/pIs8PB0aKZpHO/x5TBSI6Y1YlYn4jpo41uTGYGA7NpOwFyCNVGQ5e3Oafqa3g6XqzSU8IUa8cq7E3DI5bSh4GtM3RZ6kUz11RZ7CtVIQWlTUkXsdn9jIOKCd3cIx7Byg5vrXQlKpAlmg7MZGZ7mWyAetgZyYg7ENrIiqxZWocKj0BJeo+3Am9YxupfH413yqtFsuzLqDZoC0bFTVzmOBrjvhZZTrfBVVzt5FvMxeTSsTeciAlSIFN8tTyGY/0A2VS0ahtolMOOw0d3AW7njgZb5K9kNWztaK2u8FUJuI56G8HC1t1s+cnrdKXuWlRR5TNeIse5KRVgb5om7JirpiTBaWPtspxkRN8GnZjNuLJ7brMdRLhyGdZJjq3G3Sh/awDbvORyEajDIFZPagVMQ94lSr17pSGfhWmmrS4gJpnhtLAWMiCtPtbah6iRhU23ixu2I7TkhXdM+atoyJG3Ev53dFWSXkrfe3fZAnMN9CEv9fFTbyOswN0mG/Rk6Cq3Euz5SXdZuL7E3IbCVTsrB1DHJO0U75afNvWBJ1+5pXB07c3Io0I8ur8d+oCCCGd224YyMQRW5F6NRkq7sPfDZbhVD6tYsDbsT1ppuWuvkTki7+9StTrJq7WjPPm9dMIXbRRTfdZY8suV6Ta68padiyws01NejcGhPnZHyNsqb5pnFB7Z1lxd8q66rezNEF1MblABJy+58VeGui2y0bxPM9VDO1K4I0/Vxd+WYDVO6Vt/aPKUKVWALFhROzRwOxo5pg3FrYihKuTQNxowopZEiU/Z7tT6ft/G4ddpIGTYXqZiEiYqZyUSdLGayyiMPBLyD8oI/MVvD2LpbwVg3PVEOiHpHzVs1KctywoIqvV7dY2loY2HSMXZbYoNWtOeqMdXagWJ/f5rgmwlGeY3EJGurq5UYnrLT2k+xdRqUNFOTOKUz61VGB5o+itr9yhZ825BlynuWXLCY4CCX85olLnIv1J2rF+i5wvdqqakVI6bs0T/4xsQNRLJsmHYXrQfFWU4KzTm6Mi0tReMsWhMIyQziqSoVxL1tlnefORjVQAhkJV0iisp1TFM0n4QOroidqb2Z2Kuc0mAlvu9kS9xhiM53KdOG/qlU7VVRiLdyqEQ6z2yl9nOF95cSco7hRqQnGGoYZKvkyU1rl259F7uB6l28uq3GlU06cpS2Og9BBEUmfe21ThD0RnOulfsJIw4cfWkpolWw/eTVYParmdFU0eUeYQWp8GEJC+k+p9dLbL+xD1FoIAoKKQnuQNjGTescYqjT6uRcrkp1P40jpQ8wddxUmQaGULNeVpWhbvfWipS6ZEn4adWmEQj5pUsGxRSwXUSTToFdlZUTSf4GuYk3YbWpWn2YfLXbX5Z8dHfWOhcUxBJBgae3S8qUVa2szfOSzpdpOIC2b5cNN2i5d8haRKmDw4A6TxjMFMr8pWWSfsfdl0SlIJIymTXB9v4y9cmdtj5rdVdhCcHr8GbSUjIGNeRMH3K5vgLhDVc5K7bRMFBNuEF6byVrLWXxEvMZ2sVEfEALeTNol2UlyUR6P08J7KLqsh9F1CT9bL8e6yW0glc0jPnxYQdLRrfbOyWqX2wx3tx16YDlGrcJmKo3M0WTVisUDQ+w2fZ9z6cXmAgSON+GXqNC/CG84rSloNXlCG39Udxvs9O+yQZPupVWfvbLmjrBA7fhkY49RU3VYtF0qeiWFlZwKFyPqxN9vzZreNOuuqu0625Bai4zKS93+4FbwqRg3bmGUrdjt0s2tzY5nLnJwYpWrfwiJOT0yrE200Yiy/DExUKbJolNyT2xoeUzwkUmZJ3yrIMY6VJwOtww11JYZF2GfSdr8tHxlXItHzaci49IHmKuAd+hczrSS+pybvpbxZpDFqt0cSJRpbqdd6HGRuwoVBB+53bevaWa47UYbgO68658UhCaI9qhLNKU3IcpQ+0IWUjifuhHLg2gzFVCj+VoOC+6IrPts3e+HhzNZpfSFUfdIu60q0sQaZeNvXVT+LulaRzvTys1j5rIjVH3lDYCxuzAVOMndl8eFCJJgxBm4Cb1DYB6rEwYk7ta+9LqovOIKbu4WcF0mGMWVoknDHh476QgQ2JzonZ3aWC4g5H4+y2J+NF43LMUHMIjE0gH1ToROx9Nhd1KvYGunfY5Q0KvW56OWP3YQ1PlSDThrI7jcLsipSQjNnpvFDQxzjvlpt+X3anHB9K/r6825I5og0MKLySrUfaOoWCeS3qAsFBDmjC8IvUVWxIC2hsgxTg53w36CbYBWnihKVNIHkAbprmCWc2Y4nJDwF5xds3O6iiOb4hE4nMHW4HpnJVrz5fXcig5ZORPpLSjkBTET6QPy0mK5PHk1YW9ljZOzFr9uDuz1UElDGB85XZKZSE8TtSw7i7mcN/hdnVKyLA9hCorH+NRinUW0gT3ZARhmOsbo9AUH5EZVhvzrXDtEjicAkU+7CFWbKUEr8Kt3fZZl63IlnORfrizp2uBSm5ClVRNIkKv7gIEFtG1XLk13I36xGRwfJ16EPQrPvMHKYZkSUjva/jCpFAPhbs9lROwC2AwD3e0yMDuBfUPUFUgOcYbgdNtrQPtO0wZoCyowXCG53ffQprLaEE3StZtwVGL1jst2Z1UnAfEtfjuBBdBDjv8LsNE4uSc5SBoCdQXc49cbV2u6l1S2EORYcerA3uAQw3Nwh7h6GWrSXtS2NhgBhc5Q7CskdDBJEG2e63AKXVvob6u1TfGu7FKJomkVVBxaqYOtHIzDBaQcrNii014Zq/7fjke/WvgJXQweBvpht+ndkAcjNjrG6k5SAI9rfkQZg/Vbqt4tyUkUXfEv0gbZQ3lMr5GqvMRTA1l47oJacqGRQZkIVHTtJSETNzltDWhZwXrcc+oIVsxmLGBiv6k6mOi321etXt+UyRqCVqZK4HgzBKAECoEMe/u8AQmRmJ1U2y6wLzDMmM0RBRh4xC1SBARHXoJnJ3E0pGGyhW+YUGLgh9sesMcN3LrczB7r255u/bk1MK2VuhKUo/2WVrBpRDDMWVIeuyQjVHuzr4LBtB0Mvy7arMrR8GkLUPbmLVsCNCwLlM+MLdh5Fybe2934/kGr8jG9A7UbUmVnn9NphBB16TdqhFoK0cP2a0FB4znpeXftrkumurKPVkSXBJX6G6dmeu1pBQFaXK5xavV+krtZKIjcItMrW6p6zp/4xRqAlmip3jOkRKfnuO6SGPoOAQ33RdufZGQ98KnCJjM9rspHAhHzE8nFtTuwamHglgnB+xaVZEEX3si1KPBMH0Ooh1H48q0Uza5SHPwzmaQLN6qA6VMWaBNvA3vEhU9MssrrHb9/XhRm54MWY1Csr0RYDgYm+pVT2mshMG7nM3qnUPeN7fLvWfqTDm5qVmq2nV/vfjrs4FLW3JF4Nfd6NNLthycTAc9vRCEsSGFYIwf6HRKJYWgCUgL+CHXV9iB6zxcJx1Sh0OKSVLSMKOcW6/Xf3/58DI/On17fvxvvMs2P0f6f/Y46/nk6f2VlMfzwMDxPz14ffp3hPrlw0vjJUCk52O7Nu+jt0dc//DQ7uO/fgdh3j89XxF7fwL8fNjeOdH8+vRLUvp92zXTl7bKHy+lgB0u6NzLoG3nd3I98P39Q82vLMHxU/qu+uI5bfwyvww5v2kS+InTBW+n0dtDzA8v/gT8k3jtF5TAvwRNPav59kYD0A59hV/Rl9//D3bqq5QCLwAA -->
