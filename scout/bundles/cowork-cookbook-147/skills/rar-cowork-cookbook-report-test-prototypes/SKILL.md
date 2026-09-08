---
name: "rar-cowork-cookbook-report-test-prototypes"
description: "Generates a read-only test prototypes summary report from Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets. Call when you need that report."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_test_prototypes", "rar_sha256": "d2a50067f2fd2f1cf64f9c8618b9d1c64eb9355e2d8d347b773b66d4239b2734", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_test_prototypes`. The original RAPP
agent is preserved byte-for-byte in `report_test_prototypes_agent.py` and in the RCI capsule.

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

Test prototypes Summary Report — Generates a read-only test prototypes summary report from Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets. Call when you need that report.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-test-prototypes
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
    "breakdown_dimensions": {
      "description": "Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to report on, e.g. USMF.",
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
    "output_filename": {
      "description": "Name of the Excel workbook to produce, e.g. report-test-prototypes-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to report on; defaults to the most recent posted period available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_test_prototypes_agent.py` and embedded as the fenced Python below (sha256 d2a50067f2fd2f1c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_test_prototypes_agent.py` first:

```bash
python3 report_test_prototypes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_test_prototypes_agent.py   # or on stdin
python3 report_test_prototypes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Test prototypes Summary Report — Generates a read-only test prototypes summary report from Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets. Call when you need that report.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-test-prototypes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_test_prototypes',
    "version": '3.0.3',
    "display_name": 'Test prototypes Summary Report',
    "description": 'Generates a read-only test prototypes summary report from Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets. Call when you need that report.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-test-prototypes',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-test-prototypes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3954cb6e14522ff5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/test-prototypes'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/report-test-prototypes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-test-prototypes-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where test prototypes stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of test prototypes for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-test-prototypes-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads test prototypes records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only test prototypes summary report from Dynamics 365 F&SCM via the Cowork ERP plugin, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets. Call when you need that report.', 'example_request': 'Build a test prototypes summary report for USMF from the latest posted period as an Excel workbook with a Top 10 sheet.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available in the tenant.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-test-prototypes-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when a user wants a read-only summary report of test prototypes activity from Dynamics 365 F&SCM, with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportTestPrototypes(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportTestPrototypes'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-test-prototypes-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportTestPrototypes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
