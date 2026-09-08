---
name: "rar-cowork-cookbook-demo-data-bill-subscriptions"
description: "Generates 25 realistic demo bill subscription records for a D365 F&SCM sandbox legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_bill_subscriptions", "rar_sha256": "face1ad7fc323b4f9a059a3c211ff7ecc08f527af34a2c737169fa38ccd31f3f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_bill_subscriptions`. The original RAPP
agent is preserved byte-for-byte in `demo_data_bill_subscriptions_agent.py` and in the RCI capsule.

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

Bill subscriptions Demo Data Generator — Generates 25 realistic demo bill subscription records for a D365 F&SCM sandbox legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-bill-subscriptions
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
      "description": "How many demo bill subscription records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-bill-subscriptions-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_bill_subscriptions_agent.py` and embedded as the fenced Python below (sha256 face1ad7fc323b4f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_bill_subscriptions_agent.py` first:

```bash
python3 demo_data_bill_subscriptions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_bill_subscriptions_agent.py   # or on stdin
python3 demo_data_bill_subscriptions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Bill subscriptions Demo Data Generator — Generates 25 realistic demo bill subscription records for a D365 F&SCM sandbox legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-bill-subscriptions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_bill_subscriptions',
    "version": '3.0.3',
    "display_name": 'Bill subscriptions Demo Data Generator',
    "description": "Generates 25 realistic demo bill subscription records for a D365 F&SCM sandbox legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-bill-subscriptions',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-bill-subscriptions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '85a1b016a0bc1c76',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/bill-subscriptions'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/demo-data-bill-subscriptions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'How many demo bill subscription records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-bill-subscriptions-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic bill subscriptions data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for bill subscriptions. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-bill-subscriptions-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic bill subscriptions records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo bill subscription records for a D365 F&SCM sandbox legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo bill subscription records in USMF sandbox, stage them in Excel, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'How many demo bill subscription records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-bill-subscriptions-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training bill subscription data created in a D365 sandbox tenant (never production).'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataBillSubscriptions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataBillSubscriptions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo bill subscription records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-bill-subscriptions-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataBillSubscriptions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
