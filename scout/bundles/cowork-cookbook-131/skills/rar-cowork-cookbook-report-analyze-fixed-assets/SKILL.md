---
name: "rar-cowork-cookbook-report-analyze-fixed-assets"
description: "Builds a read-only fixed assets summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_analyze_fixed_assets", "rar_sha256": "4e187bbb3aa1be2b403abc32daa421a069b974e0662e9805084a3704d84f580c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_analyze_fixed_assets`. The original RAPP
agent is preserved byte-for-byte in `report_analyze_fixed_assets_agent.py` and in the RCI capsule.

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

Analyze fixed assets Summary Report — Builds a read-only fixed assets summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-analyze-fixed-assets
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
      "description": "Dimensions for breakdowns, such as department, category, or responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report against (e.g. USMF).",
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
      "description": "Name of the Excel workbook to produce, e.g. report-analyze-fixed-assets-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_analyze_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 4e187bbb3aa1be2b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_analyze_fixed_assets_agent.py` first:

```bash
python3 report_analyze_fixed_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_analyze_fixed_assets_agent.py   # or on stdin
python3 report_analyze_fixed_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze fixed assets Summary Report — Builds a read-only fixed assets summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-analyze-fixed-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_analyze_fixed_assets',
    "version": '3.0.3',
    "display_name": 'Analyze fixed assets Summary Report',
    "description": 'Builds a read-only fixed assets summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'report-analyze-fixed-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-analyze-fixed-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd7cc6140f6934424',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/analyze-fixed-assets'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/report-analyze-fixed-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against (e.g. USMF).', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-analyze-fixed-assets-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where analyze fixed assets stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of analyze fixed assets for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-analyze-fixed-assets-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads analyze fixed assets records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only fixed assets summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a fixed assets summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-analyze-fixed-assets-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a fixed assets summary report from D365 ERP with totals, dimension breakdowns, and a Top 10 by value list, without modifying data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportAnalyzeFixedAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportAnalyzeFixedAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-analyze-fixed-assets-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportAnalyzeFixedAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
