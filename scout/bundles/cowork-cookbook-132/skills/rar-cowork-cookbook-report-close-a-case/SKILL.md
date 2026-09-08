---
name: "rar-cowork-cookbook-report-close-a-case"
description: "Builds a read-only close-a-case summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_close_a_case", "rar_sha256": "538692d49ee85db75af1f4a29c45f1399713d256d95fc2154ee52d3b34970f16", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
