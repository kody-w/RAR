---
name: "rar-cowork-cookbook-report-close-a-case"
description: "Builds a read-only close-a-case summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_close_a_case", "rar_sha256": "538692d49ee85db75af1f4a29c45f1399713d256d95fc2154ee52d3b34970f16", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_close_a_case`. The original RAPP
agent is preserved byte-for-byte in `report_close_a_case_agent.py` and in the RCI capsule.

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

Close a case Summary Report — Builds a read-only close-a-case summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-close-a-case
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
      "description": "Dimensions for breakdowns, e.g. department, category, responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on (default USMF).",
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
      "description": "Excel workbook name, e.g. report-close-a-case-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to summarize; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_close_a_case_agent.py` and embedded as the fenced Python below (sha256 538692d49ee85db7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_close_a_case_agent.py` first:

```bash
python3 report_close_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_close_a_case_agent.py   # or on stdin
python3 report_close_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Close a case Summary Report — Builds a read-only close-a-case summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-close-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_close_a_case',
    "version": '3.0.3',
    "display_name": 'Close a case Summary Report',
    "description": 'Builds a read-only close-a-case summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-close-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-close-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6a2fb842ff6faefd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/close-a-case'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/report-close-a-case', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (default USMF).', 'output_filename': 'Excel workbook name, e.g. report-close-a-case-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where close a case stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of close a case for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-close-a-case-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads close a case records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only close-a-case summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': "Build a close-a-case summary report for USMF's latest posted period as an Excel workbook with a Top 10 sheet.", 'inputs': [{'description': 'D365 legal entity to report on (default USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Excel workbook name, e.g. report-close-a-case-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a close-a-case summary report from D365 ERP with totals, by-dimension breakdowns, and a Top 10 by value list, exported to Excel.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportCloseACase(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportCloseACase'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. report-close-a-case-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportCloseACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
