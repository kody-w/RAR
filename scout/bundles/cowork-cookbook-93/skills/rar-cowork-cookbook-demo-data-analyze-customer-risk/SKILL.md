---
name: "rar-cowork-cookbook-demo-data-analyze-customer-risk"
description: "Generates 25 realistic demo customer-risk records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_customer_risk", "rar_sha256": "2b123f77088f2569fd944d968e26c8655ddaa28ddefdff4ecd3486abc3024766", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_analyze_customer_risk`. The original RAPP
agent is preserved byte-for-byte in `demo_data_analyze_customer_risk_agent.py` and in the RCI capsule.

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

Analyze customer risk Demo Data Generator — Generates 25 realistic demo customer-risk records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-customer-risk
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
      "description": "Excel staging file name, e.g. demo-data-analyze-customer-risk-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_analyze_customer_risk_agent.py` and embedded as the fenced Python below (sha256 2b123f77088f2569…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_analyze_customer_risk_agent.py` first:

```bash
python3 demo_data_analyze_customer_risk_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_analyze_customer_risk_agent.py   # or on stdin
python3 demo_data_analyze_customer_risk_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze customer risk Demo Data Generator — Generates 25 realistic demo customer-risk records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-customer-risk
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_analyze_customer_risk',
    "version": '3.0.3',
    "display_name": 'Analyze customer risk Demo Data Generator',
    "description": "Generates 25 realistic demo customer-risk records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-analyze-customer-risk',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-analyze-customer-risk',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b0cc84cdaa026d3d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/analyze-customer-risk'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/demo-data-analyze-customer-risk', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'record_count': 'Number of demo records to generate; defaults to 25.', 'workbook_name': 'Excel staging file name, e.g. demo-data-analyze-customer-risk-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic analyze customer risk data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for analyze customer risk. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-analyze-customer-risk-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic analyze customer risk records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo customer-risk records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key.", 'example_request': 'Generate 25 demo customer risk records in the USMF sandbox, stage them in Excel first, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate; defaults to 25.', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-analyze-customer-risk-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need synthetic customer-risk demo data created in a D365 F&SCM sandbox for training or pilot scenarios. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataAnalyzeCustomerRisk(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAnalyzeCustomerRisk'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target; defaults to USMF. Must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate; defaults to 25.', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-analyze-customer-risk-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataAnalyzeCustomerRisk().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
