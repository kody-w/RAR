---
name: "rar-cowork-cookbook-demo-data-manage-bills-of-exchange"
description: "Generates 25 realistic bills-of-exchange demo records for a D365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_bills_of_exchange", "rar_sha256": "d551cff45f2889759fb103f13da8bae1313258c115bbc6f1527c4964fcb8a2ec", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_bills_of_exchange`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_bills_of_exchange_agent.py` and in the RCI capsule.

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

Manage bills of exchange Demo Data Generator — Generates 25 realistic bills-of-exchange demo records for a D365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-bills-of-exchange
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
      "description": "Sandbox D365 legal entity to target; defaults to USMF. Must not be production.",
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
      "description": "Number of demo records to generate; defaults to 25.",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-manage-bills-of-exchange-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_bills_of_exchange_agent.py` and embedded as the fenced Python below (sha256 d551cff45f288975…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_bills_of_exchange_agent.py` first:

```bash
python3 demo_data_manage_bills_of_exchange_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_bills_of_exchange_agent.py   # or on stdin
python3 demo_data_manage_bills_of_exchange_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage bills of exchange Demo Data Generator — Generates 25 realistic bills-of-exchange demo records for a D365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-bills-of-exchange
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_bills_of_exchange',
    "version": '3.0.3',
    "display_name": 'Manage bills of exchange Demo Data Generator',
    "description": "Generates 25 realistic bills-of-exchange demo records for a D365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-manage-bills-of-exchange',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-bills-of-exchange',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c05f5bf34c2ae323',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/manage-bills-of-exchange'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/demo-data-manage-bills-of-exchange', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'record_count': 'Number of demo records to generate; defaults to 25.', 'workbook_name': 'Excel staging file name, e.g. demo-data-manage-bills-of-exchange-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic manage bills of exchange data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for manage bills of exchange. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-manage-bills-of-exchange-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic manage bills of exchange records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic bills-of-exchange demo records for a D365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo bills of exchange in the USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate; defaults to 25.', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-manage-bills-of-exchange-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo or training data for manage bills of exchange in a D365 sandbox tenant. Sandbox only — never run against a production legal entity.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataManageBillsOfExchange(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageBillsOfExchange'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate; defaults to 25.', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-manage-bills-of-exchange-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataManageBillsOfExchange().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
