---
name: "rar-cowork-cookbook-demo-data-issue-purchase-orders"
description: "Generates 25 realistic demo purchase order records for a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_issue_purchase_orders", "rar_sha256": "b854002a52b43bae80553610ab8338db97b75f3b1b2b85cef93199cfe59452ff", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
