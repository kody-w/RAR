---
name: "rar-cowork-cookbook-demo-data-define-credit-and-collections-strategy"
description: "Generates 25 realistic demo records for credit and collections strategy in a Dynamics 365 sandbox legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_credit_and_collections_strategy", "rar_sha256": "2e5d83b026afebfa37ac4492d5b0adad8702c27842faefc92ec2032f7b350ee5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
