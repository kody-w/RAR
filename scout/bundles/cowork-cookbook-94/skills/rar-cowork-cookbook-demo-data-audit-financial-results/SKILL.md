---
name: "rar-cowork-cookbook-demo-data-audit-financial-results"
description: "Generates 25 realistic demo audit financial results records in a sandbox D365 F&SCM legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_audit_financial_results", "rar_sha256": "63bea45e4c5dc276b7bfc2141f85f654dbb0c85daf175191252dac56cf7d9d30", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
