---
name: "rar-cowork-cookbook-demo-data-audit-financial-results"
description: "Generates 25 realistic demo audit financial results records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_audit_financial_results", "rar_sha256": "63bea45e4c5dc276b7bfc2141f85f654dbb0c85daf175191252dac56cf7d9d30", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_audit_financial_results`. The original RAPP
agent is preserved byte-for-byte in `demo_data_audit_financial_results_agent.py` and in the RCI capsule.

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

Audit financial results Demo Data Generator — Generates 25 realistic demo audit financial results records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-audit-financial-results
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
      "description": "Sandbox D365 legal entity to write to (default USMF); must not be production.",
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
      "description": "Excel staging file name, e.g. demo-data-audit-financial-results-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_audit_financial_results_agent.py` and embedded as the fenced Python below (sha256 63bea45e4c5dc276…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_audit_financial_results_agent.py` first:

```bash
python3 demo_data_audit_financial_results_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_audit_financial_results_agent.py   # or on stdin
python3 demo_data_audit_financial_results_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Audit financial results Demo Data Generator — Generates 25 realistic demo audit financial results records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-audit-financial-results
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_audit_financial_results',
    "version": '3.0.3',
    "display_name": 'Audit financial results Demo Data Generator',
    "description": "Generates 25 realistic demo audit financial results records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-audit-financial-results',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-audit-financial-results',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6470db15328391ad',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/audit-financial-results'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-audit-financial-results', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-audit-financial-results-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic audit financial results data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for audit financial results. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-audit-financial-results-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic audit financial results records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo audit financial results records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo audit financial results records in the USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-audit-financial-results-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo/training data for audit financial results in a D365 sandbox legal entity. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataAuditFinancialResults(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAuditFinancialResults'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-audit-financial-results-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataAuditFinancialResults().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
