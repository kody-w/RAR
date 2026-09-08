---
name: "rar-cowork-cookbook-report-analyze-fixed-assets"
description: "Builds a read-only fixed assets summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_analyze_fixed_assets", "rar_sha256": "4e187bbb3aa1be2b403abc32daa421a069b974e0662e9805084a3704d84f580c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
