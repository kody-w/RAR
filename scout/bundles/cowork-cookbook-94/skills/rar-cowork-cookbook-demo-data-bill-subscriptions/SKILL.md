---
name: "rar-cowork-cookbook-demo-data-bill-subscriptions"
description: "Generates 25 realistic demo bill subscription records for a D365 F&SCM sandbox legal entity, stages them in an Excel workbook first, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_bill_subscriptions", "rar_sha256": "face1ad7fc323b4f9a059a3c211ff7ecc08f527af34a2c737169fa38ccd31f3f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
