---
name: "rar-cowork-cookbook-demo-data-analyze-customer-risk"
description: "Generates 25 realistic demo customer-risk records against a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them in D365, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_customer_risk", "rar_sha256": "2b123f77088f2569fd944d968e26c8655ddaa28ddefdff4ecd3486abc3024766", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
