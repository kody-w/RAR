---
name: "rar-cowork-cookbook-demo-data-define-credit-and-collections-strategy"
description: "Generates 25 realistic demo records for credit and collections strategy in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_credit_and_collections_strategy", "rar_sha256": "2e5d83b026afebfa37ac4492d5b0adad8702c27842faefc92ec2032f7b350ee5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_define_credit_and_collections_strategy`. The original RAPP
agent is preserved byte-for-byte in `demo_data_define_credit_and_collections_strategy_agent.py` and in the RCI capsule.

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

Define credit and collections strategy Demo Data Generator — Generates 25 realistic demo records for credit and collections strategy in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-credit-and-collections-strategy
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
      "description": "Sandbox D365 legal entity to write into (default USMF).",
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
      "description": "How many demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-define-credit-and-collections-strategy-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_credit_and_collections_strategy_agent.py` and embedded as the fenced Python below (sha256 2e5d83b026afebfa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_credit_and_collections_strategy_agent.py` first:

```bash
python3 demo_data_define_credit_and_collections_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_credit_and_collections_strategy_agent.py   # or on stdin
python3 demo_data_define_credit_and_collections_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define credit and collections strategy Demo Data Generator — Generates 25 realistic demo records for credit and collections strategy in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-credit-and-collections-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_credit_and_collections_strategy',
    "version": '3.0.3',
    "display_name": 'Define credit and collections strategy Demo Data Generator',
    "description": "Generates 25 realistic demo records for credit and collections strategy in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-define-credit-and-collections-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-credit-and-collections-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0b8666eec36ab65f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/define-credit-and-collections-strategy'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/demo-data-define-credit-and-collections-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write into (default USMF).', 'record_count': 'How many demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-define-credit-and-collections-strategy-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic define credit and collections strategy data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for define credit and collections strategy. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-define-credit-and-collections-strategy-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic define credit and collections strategy records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo records for credit and collections strategy in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo credit and collections strategy records in the USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to write into (default USMF).', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-define-credit-and-collections-strategy-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training data for credit and collections strategy in a D365 F&SCM sandbox tenant. Sandbox only — never production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataDefineCreditAndCollectionsStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefineCreditAndCollectionsStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write into (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-define-credit-and-collections-strategy-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataDefineCreditAndCollectionsStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
