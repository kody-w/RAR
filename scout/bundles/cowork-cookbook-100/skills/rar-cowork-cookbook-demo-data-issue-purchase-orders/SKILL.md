---
name: "rar-cowork-cookbook-demo-data-issue-purchase-orders"
description: "Generates 25 realistic demo purchase order records for a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_issue_purchase_orders", "rar_sha256": "b854002a52b43bae80553610ab8338db97b75f3b1b2b85cef93199cfe59452ff", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_issue_purchase_orders`. The original RAPP
agent is preserved byte-for-byte in `demo_data_issue_purchase_orders_agent.py` and in the RCI capsule.

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

Issue purchase orders Demo Data Generator — Generates 25 realistic demo purchase order records for a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-issue-purchase-orders
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Sandbox D365 legal entity to target (default USMF); must not be production.",
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
    "record_count": {
      "description": "Number of demo purchase order records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-issue-purchase-orders-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_issue_purchase_orders_agent.py` and embedded as the fenced Python below (sha256 b854002a52b43bae…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_issue_purchase_orders_agent.py` first:

```bash
python3 demo_data_issue_purchase_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_issue_purchase_orders_agent.py   # or on stdin
python3 demo_data_issue_purchase_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue purchase orders Demo Data Generator — Generates 25 realistic demo purchase order records for a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-issue-purchase-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_issue_purchase_orders',
    "version": '3.0.3',
    "display_name": 'Issue purchase orders Demo Data Generator',
    "description": "Generates 25 realistic demo purchase order records for a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-issue-purchase-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-issue-purchase-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '189c6c354beae435',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/issue-purchase-orders'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/demo-data-issue-purchase-orders', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'Number of demo purchase order records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-issue-purchase-orders-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic issue purchase orders data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for issue purchase orders. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-issue-purchase-orders-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic issue purchase orders records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo purchase order records for a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo purchase orders in the USMF sandbox, stage them in Excel first, then create them and list the keys.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo purchase order records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-issue-purchase-orders-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo/training purchase order data created in a D365 F&SCM sandbox legal entity — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataIssuePurchaseOrders(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataIssuePurchaseOrders'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo purchase order records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-issue-purchase-orders-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataIssuePurchaseOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
