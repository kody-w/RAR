---
name: "rar-cowork-cookbook-demo-data-evaluate-supplier-bids"
description: "Generates 25 realistic supplier-bid evaluation demo records against a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_evaluate_supplier_bids", "rar_sha256": "896e895fd90dc1ab671c525ac534f612777bf986b274dad42000617be2b17eeb", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_evaluate_supplier_bids`. The original RAPP
agent is preserved byte-for-byte in `demo_data_evaluate_supplier_bids_agent.py` and in the RCI capsule.

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

Evaluate supplier bids Demo Data Generator — Generates 25 realistic supplier-bid evaluation demo records against a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-evaluate-supplier-bids
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
      "description": "Sandbox D365 legal entity to target (default USMF).",
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
      "description": "Number of demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-evaluate-supplier-bids-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_evaluate_supplier_bids_agent.py` and embedded as the fenced Python below (sha256 896e895fd90dc1ab…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_evaluate_supplier_bids_agent.py` first:

```bash
python3 demo_data_evaluate_supplier_bids_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_evaluate_supplier_bids_agent.py   # or on stdin
python3 demo_data_evaluate_supplier_bids_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Evaluate supplier bids Demo Data Generator — Generates 25 realistic supplier-bid evaluation demo records against a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-evaluate-supplier-bids
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_evaluate_supplier_bids',
    "version": '3.0.3',
    "display_name": 'Evaluate supplier bids Demo Data Generator',
    "description": "Generates 25 realistic supplier-bid evaluation demo records against a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-evaluate-supplier-bids',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-evaluate-supplier-bids',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f90872901f9bd91a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/source-and-contract-goods-and-services/evaluate-supplier-bids'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/demo-data-evaluate-supplier-bids', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF).', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-evaluate-supplier-bids-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic evaluate supplier bids data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for evaluate supplier bids. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-evaluate-supplier-bids-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic evaluate supplier bids records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic supplier-bid evaluation demo records against a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo supplier bid evaluation records in sandbox USMF and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF).', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-evaluate-supplier-bids-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo or pilot data for evaluate supplier bids in a sandbox D365 F&SCM tenant. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataEvaluateSupplierBids(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataEvaluateSupplierBids'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-evaluate-supplier-bids-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataEvaluateSupplierBids().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
