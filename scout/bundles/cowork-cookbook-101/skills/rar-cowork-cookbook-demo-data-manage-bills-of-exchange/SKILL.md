---
name: "rar-cowork-cookbook-demo-data-manage-bills-of-exchange"
description: "Generates 25 realistic bills-of-exchange demo records for a D365 F&SCM sandbox legal entity (default USMF), stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_bills_of_exchange", "rar_sha256": "d551cff45f2889759fb103f13da8bae1313258c115bbc6f1527c4964fcb8a2ec", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
