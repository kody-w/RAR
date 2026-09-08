---
name: "rar-cowork-cookbook-demo-data-evaluate-supplier-bids"
description: "Generates 25 realistic supplier-bid evaluation demo records against a sandbox D365 legal entity, stages them in an Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_evaluate_supplier_bids", "rar_sha256": "896e895fd90dc1ab671c525ac534f612777bf986b274dad42000617be2b17eeb", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
