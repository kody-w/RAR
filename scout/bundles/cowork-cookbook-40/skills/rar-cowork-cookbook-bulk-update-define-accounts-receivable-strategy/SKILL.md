---
name: "rar-cowork-cookbook-bulk-update-define-accounts-receivable-strategy"
description: "Applies a bulk field update to accounts receivable records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs, producing a dry-run preview workbook for approval before committing and a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_accounts_receivable_strategy", "rar_sha256": "92febba9850a5372b92937c2c7810d192117956fa7277ed28cefd30686fb6e60", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_accounts_receivable_strategy`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_accounts_receivable_strategy_agent.py` and in the RCI capsule.

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

Define accounts receivable strategy Bulk Field Update — Applies a bulk field update to accounts receivable records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs, producing a dry-run preview workbook for approval before committing and a

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-accounts-receivable-strategy
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
      "description": "Explicit approval after reviewing the dry-run preview workbook, before changes are committed.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to run against (defaults to USMF sandbox).",
      "type": "string"
    },
    "new_values": {
      "description": "The field(s) and new value(s) to apply to each record.",
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
    },
    "record_ids": {
      "description": "List of accounts receivable record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_accounts_receivable_strategy_agent.py` and embedded as the fenced Python below (sha256 92febba9850a5372…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_accounts_receivable_strategy_agent.py` first:

```bash
python3 bulk_update_define_accounts_receivable_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_accounts_receivable_strategy_agent.py   # or on stdin
python3 bulk_update_define_accounts_receivable_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define accounts receivable strategy Bulk Field Update — Applies a bulk field update to accounts receivable records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs, producing a dry-run preview workbook for approval before committing and a

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-accounts-receivable-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_accounts_receivable_strategy',
    "version": '3.0.3',
    "display_name": 'Define accounts receivable strategy Bulk Field Update',
    "description": 'Applies a bulk field update to accounts receivable records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs, producing a dry-run preview workbook for approval before committing and a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-define-accounts-receivable-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-accounts-receivable-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0e69a1c9d53f0ead',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/define-accounts-receivable-strategy'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/bulk-update-define-accounts-receivable-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against (defaults to USMF sandbox).', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of accounts receivable record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when define accounts receivable strategy records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to define accounts receivable strategy records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to accounts receivable records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a supplied list of record IDs, producing a dry-run preview workbook for approval before committing and a', 'example_request': 'Bulk-update these AR record IDs in USMF sandbox with the new credit limit - show me the dry-run first.', 'inputs': [{'description': 'List of accounts receivable record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against (defaults to USMF sandbox).', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across many accounts receivable records at once and want a reviewable before/after preview prior to writing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDefineAccountsReceivableStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineAccountsReceivableStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against (defaults to USMF sandbox).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of accounts receivable record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDefineAccountsReceivableStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abOjVrblX1HfF9G2H5kJAsSQLyqiEZOQhEAgJISzIs08z7Pc9d/7IN1M21Wu112v+1Nfh0MSnLPnvdY+Cb++2X0Xlc3b5zfdt4uVaGdZHPnNyi68FVuOZZOCjzJ1wP8rtyy6Jnb6rmzatw9vnt+6TVx1cVmA7UxVZbHfruyV02fpKoj9zFv1lWd3/qorV7brln3RtavGd/14sJ3MX76Wjdeu4mLFzYWdx267wojNSvjvOiuvfsz80M5WftHF3bwydFn4sGqBWU45/bQKmjIHqtr+qdVbZXHbrcrgXeRK4toPq6opvd6NixAs9Jr5Y9MX4Jo/xP64Whx7+hSUwNcKLB2ALscHP33gZ57HXffcCcJgA1/9yc6rzG/fPv/81w9vMfj+9vnXNzezW3DpbQs8Np6ucn4QFz7z7qz23Ve9a8DdcAaiMrsIwZ5qBnEvwO/Kb4DWHFzy/GD1/uvH1s+CD6t///d0tJuw/enzl2L1/vflbflPA8500RJau+1AAFy7sp04A6H6tGKy0Z6XSHd9UywZaUHaivDTa+dvkspq9Zfl3o8vJZ9Cv/vxy1sJTLCXpH55+2kFovPlDQQOfP+0SKl+/OlTVo5+8+NPv8lpeyfx3W4RBqz+9PX997tYsPC3pXGw+qqrPPuuC6Qrrnwg/Hf+LX8v09/FvYfk62vxj2X1YfXnkhd//gLsfRWmA+T+uVgQA7Dz7VNSxsWP7zpAAfiFXbj+jz/9M7Fu5LvpUmj/R3J/fgmOfNsD0XoPyU8fnun76wp69+27zH+utgIF8694ApZ/U/c9UP9M9jOzfyc6AwXcfs/ln4r7sw3QX1Y//1Pf/rMNH1bBlzfOz+IB1B1olc+rX58l8vMP3m8Xf/jr34Do/60Yvewb9ynha24XceC33devP//QPi//8Neff+grUMW+nX/tm+zPZP5ZXJ96/hDB91U//nEv0G8UaVGOxep7D61+Lav/1vzt0+pqZ7H32/X28+r3nbj8QavFiW9KXyH4XTe2wNbfxfGnt78BHCqAN737vA3w49/+bSXHblO2ZdCtdABB3QokuItzfzH+EsUAatsnagAU9Js2XkD4tQ7U/5LhxWKAor/8D/cJ/R/dd+iHF0z/+kLzr94T475+Q/SvvyH61/Yd5n75tLoANWUTh3EBgFVjVPVLYYcAzBcTAAq3fjMA2HLmzv8Iuvvj8mUhgl/+RU1fn0I/VfMvT6yOX6iosdKCiG2f+Z8W32+RX7x76gKW8yff7YG+rHSBcUEMgP0DiElbZgNA1CVObRpn2cqLgUbAdvNTNojl50XYL7/84tht9KV4QTi2etFgC4MF381ZffwIvAyyOIy6L4XvRuXqh1//9sPqf67+s11P4YsOFRDLe6aAhXtdOa1A5/W5v1DoknYAK89M/fq391gDMQXgbZDXOFh4eNkMKjf1vW+B13fMR3RDfGM5QGJl8yS5uPu0koLVd3uB0uXWwhxRCXjV8yu/8PzCnYFUG7jzPZJF2QFO7uI2mD+s+tZ/av3FaeyniTmAALv7ZSWzKuCpMlvmgOadt8DmsohB+L+Xxes6ENL80K6230R8Wp2WWl1VdmNXUWO/6wjsV14W9n7fvgwZq8IfvxQLPftLqJ6N8woPWAQi476n9OOS8yfPg8S233Q/19gLm16erNp8Kdr3prCb17gCTJlXYR97C1X8x3tJtVHZg2FniR+wdJH0ngXvPSvPGnyNBn86CH0r5tUySKyE5+j0midWX3oUWeOr/4+nqyU2jChqvMhceG7Fny7a/ZWzZd5ccvsaURc7F3nP/vxt3PkGad+Q/UuRxaAAm/k/XiufmX5f80LLvgEuaYz2lA/KDORskfvsgqWqm+YZ6S/FNwr5AFx84iUoBAAZoKWWmH9TuNz9ZmkEcGH5/ds48S1mwFVQ6auqdzJQhYHve47tpsCqZunk9yyDlvCXOI9R7EZ/8GpJFKg8IH8FjIhBpgHNfPoO66+730z/w8bX1LRseU6UPWjk5ikA2OEvBi5JGOMO4JndvcZ74OfnpxDgRl51i+8OaCXg6eui3/h1H7dxt8DmK65+BRD84/L58nS56k8V6B4QLNAjVQ+i++yqJe85mImADQBYQJPlcQHKCwTlPQhPgXa+QASA4Pch9iXxefndIf/Zigu5fdu4OLLseVb/q4SL+fdIcvmzMgHy8mXFU+/fV9p3bYvsBU1bgIhA47e7r8Hi02s2eA0fq29yP//D+enHf+2I9WR7448F8HkVdV3VfobhF0N/I+hPoKvgl63tk6w/vsDh44tCP34DiI+/AcTHb6jzBzWvCHxe/Wum/kHEe6t8Xq0/IZ+Q5dbxvdTe/0Bk2I/b+0d8uful0PzfgBeoL3NQa0seZzAdfGfJb0sAVYYNgC6w+MWa7UK2I+D3J02ApHwpfl/7S+8BFirCpVbb8neY8BwXQB+8cvidzcCtogO6vWX0DP1Py4ltMb/13z4XfZZ9eANY6v+rh76FvvKl2tvl3Aj6Cox1Xew/f30DyOX7H8/U/ATw1wWN8h1D7QDIWL1gdumkpQj/Gfp++I64L/+fJPaOvr63ONbN1eLJ63i4DJRPHJu6f7REeX6xs08rzgeYmbW/b453/lv4/3c9/Ao+CLoLnP2wWgLVLnwNgr/EYel/uwUNBUz8U1ueBPX1RVD/aNAfKO0PXPY+ZNjhs+9XP4IOsPsMJBrcWHjuO839qVYwQHwFge5fqfmjzgU/nsz7Y/vTs3zA4tVz8XJhoWHAl08DfBvg9ysAf6rl+1T/j0puYGRaRHjl58WPD+8gDD7BSezD6vuhCkT0/Zi7aPCLPn/7/PNyoFuq7bll+QL2gI/vm77/q43jv/31T+x6mfw19v7E++P7EPDPZ41lMHgx45LsP3H8qQFQByDgxdjfovCbLeXzpLnYAmzvXv8w8usbaB0byLTfm+f9qAKWA6T92C5DGAzABigEv1+wAO793x5i3sW1kQ2mZiCPRgPfcWya2iD2BiNRh0ZpjHRRl6TWiLem0fWapDdEYJMoSfoeSrl+4GEIQRGBQ/jEYt4La76+mhCI3NBkgNBAML5GEQ/YhOKeR4Ed7oZEEZt27I2zoW3nt61pXHjvfr/8XIL6/Tz1hJOX+7++OQQOVu7wVmJefywMrR34Rjrz0YRNhJqsO98crFvpHEFDyM1putQoPyV3i5FJlDJZQYsPOz5zjVk3z3SpccyJjrlNVEAX6FGlVlAWs0Y2lXPvGvG45R/VuHEfG3hDPe6u9djG10mINQ3iD1pmxLE2I1txDeNzlkrX/gpLtEFQh15uqEutu3oEzbxE8RgMEzTMG5YjpNcLKyAdMUBHrDI3QXVEDOqyO53nW6ztHy1fUM7WqCjY9YZJGeA+iaADYk+m2k8pn2rCZZhGynTWkxLBrOZWFSzeq1txm+dMz/C1sBNTthJ7js8mr5ZyqR0uLTPHloRu7w7hbPIba8ESkSZBvG/RIcvTg9qdXGibi2audJWrmYf7Hulx9BDmbl4GzC4kZMyhNio2TbTCIVoFUVChwmkcUo5Yucadh3Hg2t6FDnq9vTm6VDAPeMqEk/wI2Hbs5TE8K9mwxUTkoa4pGpFUkzfO0TZnmdv1nHEF6mIb5NFrtM2eijbbRXEjs5GquNPlcYfSHEnr+n7fDaaceVpehjhn46MIH9CZFpwZCsTrNBCXpr/GFsVfwxvyOIt+RrU422qHueCq7ToIWU1j1zmhj3EZYpvuJIiTDRIkbC59fHS3zJZBixOekuJuDjE/w7I+uJ0Oo2tZUj7vwjV/M/S5motwvO6b/a50iH0sw+xRKqEbqLsTqB8ROtH59rYmCM3VujoM5uwBGem9PtS6Le6Kg3Ns3IufDs6G9+cUsjimlA46emwk7awSOnTP1gNscThv8611JE58FRoVL5IWeoSEqMHwKXbPiL8XM019XO+peCr38uHshUNcULdHjWb4ReEpJbsfouZiR012Y9bVXaT2e68nqpvU7UFixqo18ikv0AZJJHUvnoeJucLC3qnN7VxY6hFP0ZrcrdeSOgnDKEBI6LP7e+FK+Rk5qi12FTkNtsWOOiaWkNrFxtk64yRzsgvxkEyhZZ7xba6Upcwgmy6duv0+uaW3bX1HuofgYGRvhnaJIIcpHnI8HrA+aF2HxB9VfoWkvZkQdh9UBczMlLgx+QHPUygPbfNyNObj+uhe5s36fNY2WWQ1lmQRsNm70mWK5WTD7txG9gpGGVo9rO40g3i7w3RX5MIm93J2uVMFaXFaTV+3WLdPm/OZrSGdSfsdD+aS8irtWhPMFp5TqAZECUeXQ0s9CcN1O1XpcY+4Yf6QSBl63HM/wdjDqDt4ENjJ9dRYm/tpQ94S21vja3AqOV579dA7pS0UFV+mA265A+moIxJlrQM/yF0dZEZZ37PDEWMfyG4zuaRErHvvBFLjjF5BRs10zc2RSPbsGOF7tEAqgFYFE0dtp5+17ODfmHwUaKJqlTLIOospMGGfm71gp6Yk7s7hHEcxm3AzM4ck2pfIllETc6Tnk3/xL5Yr7nEWKQ4A4CMzuaTXBwkZan2VGjxMyc2UGrOF30Nv1GQoo3Jtvlidc1VsTdd1eS9tNWSnFjfySKPe3jRsxkMSgQvmwb/ShSJo9OkwXFj2uLkH0jkb9eJxlGDJb5oNa+7x0cBPwsPku5oTUPum9YNMuDkrENoFEoV5221hIe/tORHZfpY20a5GDmsy7PzHfF+jROvY7OFQJJCkw1m1I4oJ67SaMa9ub0ZwkjSRhl0ILbM2CX8aWP9+mj0LMsP62LkIiafaUAW3cZ4oKyEr00a0kQunE+NOkLC13eSO0cexECMxNiTID7cbibIv91JDTzlL7NgTVyjF2lEZx1Eu+A10pn7jdXktO6pnHMfzBI9Rw6q2yAatcTfA9CTSsNOGRKeVoWAioTsiqGQfQkXbZ2tD4yNJthCFOzTM+kTM+1zQCuaqlL0mkbFxJjf6dr/btOsC2eoIzN6U8srLTOY19P7gIFe43sxHz9s+jmwc+vWO825Da9Yba280kSyu4/vhgYNfj7019dWoGfuK9jCLgnoyzuT9+djIBoToFHSZa+2gjipx3fcdmiCiore8AFutT6rzwI9NL+6cc8JpheHCxU6Fs2BrUocBzghaezBoF19zXzNcqyuCuLmHEVdKQn9gFS7vNKrRAx691WhcSqO2hwJyvORiHjckLXNX8zhygPUd55qFiXqQKIKfzMN5q+z2fEmUuJoabrGW3DWSs1R5MyuaS1JVOlq4V6UGvlHm0b7PoUCeIStyt7xrVafsDAMN9+rKQFxxwcRA89trI3UPyNbvlyHnlFabdDw5okPauU0mk/AdObToHaGUfc2WEkevBdeYyEBDRX6bEaYj1eciRdDjnkkSWpCj+0xZBxreowTju7JR6IjE7rbGSZUm7gTB2KHf95KqSeJw4bVZPUdsOJxFsbmwXHhh6MdGszPcU4iBzYftAJnxdsf2jOhYdUOwDcxsL5JAMh49X42Ry/cYCq3pQ8bzac/ktVa1WIZeFZ0t43R/rhXPtYQjhYkkdW71qZWFbLdh5LAScSaIJoi7nttHemkzJB/lQAtpNtdvkSOEcmtqWibWVmQV3Pki0Ns4vLDJvL5ezI5ujdYW1Gy8slN02Mm4NHhBRmdHYns7ndg2bp3jqRgLeQtJ7lWk+XN/2yZGUWZHyoqcWbbzGj9EFXq7Ukgs2To53himLBS/nsWiic/2gbd4dH6cWFg87CJMS3GRt3WeHBiTSpQb2e3Ckz+uVWqaMz5T9bgOi8ehP2+3slmUPiH0JqcLgRdtpfxe9obm35GmDXRuXE/2Wau5oH7A9F6ZGI7krUGfcvWiecg+v8fEmO5PtL++ij2Rnx7yrT34uw3WOE0S6vtU5CUxaIjRd9iroYsQUjzmcLv34Rj2i6mylZ2Ct6Zx3GfBvswPx8S2Zxbmmjw42zKAtbB2rDBNCyM/W1tb6tginqurnHbOumwlZGRbwDtgMLCaMXYGrgqPh54Vg5AYbUW56d5mNAz7rFQ65MyX0b9SWYjHAgqA9ZS4p/qEM+XB1A9SsOVJBOV9Odsjl4RWZxrZ8txt9gvuVlD0VF5K5izu0cp3XBwx6wpiZoaPtP39ms7CoUWC+iIiWxyqPAPBb65A87ADJ7NXGSK5R3iMKG4pLw+d5JC0uuFT5RbjuwuZpIf4cL/A0vZaq+51ptYboakKirK2QSWj2UHMmPO4ZomSZ3JdrwRDLQ7WxJmd0dcUrgTQtXfPt3mnBykOW9bZj8mq1QRN1E+H695LL45PnwFOVHH68JztFjJNNla2WZ1qB7w83qANfLST9XoqE6FpKYPHBEtP7HW6Pu8ugrYb7xLXXUYt2yXR7pJJfIxXtkUShFGfebOsjs5eDe0jeqMcp3YobUZLAt50xF1kBTCQMVicbc7Olbhu0hFLL66/F06HR9YaNhkGjLqe4VZoRhuumIuxM2TzwUf36D4pfXjG8FiqD4Q5FfHw4IbzuYZ31yZznN5ID6jadvWG2fsiojeR6NFXQIgtcj/uMrS47ctMRLjiSuvVhqHPzpT3teXi5YCl4OgXT7XE95ka8gMxilBPnHYTn1AGeo72e3yL5aFIa+NgDw9Dk2+3DR1FZsmyLHo72fAYeok5xSQ/tWWxX3cTvJb5Ou8OyaMD6djt8uohO8LozFY+oIih2zP8wOcHh1xumoYkBvOAysNIdmureRxVqD35zbkRy935ODNBQjxMML6rExNA497qD4cW12KVKpQj5MQOE9EGG7E7xtnAV+tuXbrTgCkVMR1ua9mAse2aixVRqoYh3/NIOFJlqVGOYcV39lFexBqUQ0WC042zr090FqrJA39ws3ZNuNYC9GwMOVndwkyRd2etL8aJO+ZxBKmPDvIGs0uMQw2G9qS9ClI13qPCzhVdOo3j3ZYceFOinNhLUDDzbciY/XpCW1SgC0poEqso3Qq3+pMrs0ciJzCj7e8ej9JoZp1xvqrj0+g5UNFuLzOFSBeMNEx66iCB56wKul75ba0qnXvA9XytbQooFAkO5h9z1HrkLNRJzOTJZSLptG40qrO8xwkUj71jx8yr+ElG+vJ4VIiHBY2n7cXM2U5D1zjnbg4NV6dc9EgaZ8DWSndndtS2zpXhEJS4davCDTgNXoa7QtVzkhHpFi5NDhx8iJ4QrvSZU68nZ8qCrnVuFuceUXSrOpFG6AiYMk9Vdjh41bVuqhOl1qf7rSh10qsnB6U4iI4MVMNoOm+Dc5nyddeuvbVvYGzktn5xCdaRiKxTrPVubSYxUKiyZZi43bmaxpqh9vfO9aeHd6Hsfd0hqYdoEK1elJiXr1wrpteeH09XLIKd4jxC5JlRDzSLjfXM5+16PKaB0UGyGVXQLR2bCROY+/mWmy6xVni3D1MmFAOw+QLpbbLDNSa5xePdkqd6UO+32HObg6KcbzHxoIQzcjCvqXNS93CVT4/p4KB1vr/tsESeVJ11spQJtgQYuUtQ+Z2eHhQRkwniyEQMpQQqFPDnTboVjD4YbZ4W97BtTKwwz56EsZf9xna36y1tXFTB4/CzF2hWmRCMyu0JlYCNIOfDBxH1aZUoESTjG2i6+pxeKVGSkwJpVA/FM6vkWJEKfbQsUSdM6xKloM6GCBe44wZMS+lxVwwnY05hp3kMQkvNj007rGfEwiylHLqLOFMERSZ8FfRGndwO12BdDKXvibPXtrY3B7g0luf5CJ8jk+jOcO/tjl2fITfEowebyLpNskEGc51gric33XFjyX5l9Vdfh+9V097sBoRV72hWWW/qxNd9HymRjOaYe6pGwvWE3mOHpcUrsd73AeaqKa7GBAqNNcXpx7rBVAOPH2nDwSk1bPeX9dw6MgTXs7CPITFpu/RgcvERHBNkPz+QGwyG0Ss8H5L7+JBTmKY9OO4msbzY+DQEbCOuz3odiePBP7mzhkXrvZBM9cF2p6hDQs/zB7Y4SS1b0TJsTaddITm6VtV4DPFJup0v9mNQUPZKW/Vpstc1giRq4c/NTaBgBEV2xV1vOefKWGdbIEzceWwLxb3h6QTfnSRR1QCQXO+ZEJXiZ9NbGx51oRWPRq/32ZuUjHRHX9ugGXqRNLnikNRusEMYW0HsdnwReMp6Pa8v1mM3xGUvDuZYHSKs03Fwrtzs9SAraEJEcVZ0Z9bwzxwfa+ouwYuL2s8poTp4vB/TtWM/MDauc1U/7uMHMSGOo1PoFhwMcu96V8KT2A2aRA8kYg8U17a4pXA7f3Dcm81SQzZuzt0Ua2Ay0vVG329tjqHVABmz6abc9e2uEeUjVj6iGxZJ7QkzouCKcjV7YmQtDURhG0ISqe+bqXSmlMSpar5Nh11HMoGy6/XJ7fBLluipORBZoJIUTdKYefXgUmGp5Jh0QiBcWRLBLrnJErpwO11aVbESB7/ttJNm5gOUnU+xsDbsuxVAKWO4dYvzPQQlcVU63bHVWCy0BHCgZibV21vHfSXePDRAUwUBEXvY4YkFQFG1N6gPSUt2suERpQivR0LhnRDrLpIdfkJxiZh7BnCHwbWXK7WZghvqXOAkz1ynTh/luMH0PPFrrs4rFofm+mFKXT5U1KCvBS5VTgh6VrQNQDyC9ukq3nDG1phpNiN3WTKRDEOlAbZ5aActummUmYzhQW1jqGxZ3yiMCauE2ybiHlwHDbh1anCsMdG9L2xONo0LPeb7g3ZvlcGOCgCcpHnskcOtiveZ6WPBGrLmLZRF1CwzmAube3LsROKG0tdHcJhkxewolPZ5MJHN5AahxQglzF1zZm0d88nIgXhsLchlcM9tNnvE5DQh5GDWwz3RQtMUw6DiLayhqzm6TI1JJK2Jn+EYpJjbQNkei6VzTpxbqe/A6XMdDVY3kTpzzwLSeBxrVdMusN8kDCsk5v4epDkgfhsgDcrALGTfkvrKyirOGErfUNG45bC74OepfFfxTWb2ALTPMo6nHCHPI3osIuqaE8QFPWP5pA0EyloEEbWXIusuyh0mr6as+QStmudLecRlJXLVPX+seX6LdhC7U5o7LZt3eOdn2ia8nyoNNmFelWBZKFGqoeQ6QO4HrSNZ8lTkEakYsdWta56+5PusP3amp6BIOU/Dcad3JWbdeneIr8JhRtmTPyX5fMTdU6PeyoOzT2SPZkeFUzA0f1ySdRjD57RJofJ4R3gn2FgmIifuoZRAM1JHfxt4A3N6UIxfDMI9jeAiZGp7l0lsualoQToWQyUanihkkcPKWFKkJxm/i7S4a5SZsjGFvAu96iEXyyBLjD6WqsgqDm3O6W7ApHDfwvxweBxtnisjmUdbhnAwmbHgs5yHrs/NFLwxH9IGFYwDaOfs4odtlRFUlDr0cKou1c4b3KHDDspDSMmCqryr2605mOzNqxSsuTXb3jwEfqAKdGcDkhmPJ3yUb7pC7LaVmcOKaVVed3dQ6XGmZbQw1FtGkl5LJtsjlei3KRLjSN7kE1JcWigh9Y1a9OxtQpXznZZERb9Bkyhtldbl093DU9cQ47LRDZdNCNUdbzj5xQM6yQmh4ZlScBmc9L7dEphNMwFyJsQYFQ+lP3kKS4RyA4vylQ4wHvT5PjhDdZPUTjchASLAzaG9csMwFS51i88DDOBjMGWzNNVtiO0meXz4GigQ69hEUp3UYJB2olNLwylyQgP4Eh4IKBjbh3Ozr/ZD67n1XfS0BsyGptKRQ1Tkgn8MqlzoqH24vbeQT7r86GIbixYIuKq79QneKGhAB1XfRsH+wUwb/7ZlbqHTmxeFx86CxgoVUUpuryIR4NZdhhkn/+Sx0312tw/snBCXs9czHSMIWxycDEOPsTiZpDcSGUkDSqgGZnWt1vRkQOvwLUQklXIRGkcIrN8HOW5rM0fcuNMVgEDoYJX72GnHRBg0vZZq22NMY3MSHu36cVNnEobFQajOCsncrAfUTwNRpmsx9l2rCni4vhO+e1xH5KlmDBvbGM3Q+yoLuxABC/3EMQzzl7cPb8vj7PeH0v/Vt+eWB0z/z55zvR5JfXsD5vlY0re9z09dn//LFv71w1vjxsC+15O+NuvD9wdhf/ec7+O/+P7DImx+va727fH360F/Z4fLC99vceH1YPH8tS2z59sxYIfTt8troe3y5rALPn//1PV3LoJfZeP5zdeu/OrabfS2vLS5vPTie/Hr9vIzfH8M+uHNe3+s/RUjNl/9plq8fn+fAjiLfUI+YW9/+18jw41ZtS8AAA== -->
