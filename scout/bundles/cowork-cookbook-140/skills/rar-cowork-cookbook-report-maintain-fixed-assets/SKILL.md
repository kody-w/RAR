---
name: "rar-cowork-cookbook-report-maintain-fixed-assets"
description: "Builds a read-only fixed asset summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_maintain_fixed_assets", "rar_sha256": "8bbadcdb9483765dd275b70ec147291066421794f0f5dee5eb520275d70d17bc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_maintain_fixed_assets`. The original RAPP
agent is preserved byte-for-byte in `report_maintain_fixed_assets_agent.py` and in the RCI capsule.

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

Maintain fixed assets Summary Report — Builds a read-only fixed asset summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-maintain-fixed-assets
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
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-maintain-fixed-assets-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_maintain_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 8bbadcdb9483765d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_maintain_fixed_assets_agent.py` first:

```bash
python3 report_maintain_fixed_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_maintain_fixed_assets_agent.py   # or on stdin
python3 report_maintain_fixed_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain fixed assets Summary Report — Builds a read-only fixed asset summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-maintain-fixed-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_maintain_fixed_assets',
    "version": '3.0.3',
    "display_name": 'Maintain fixed assets Summary Report',
    "description": 'Builds a read-only fixed asset summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
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
        "upstream_slug": 'report-maintain-fixed-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-maintain-fixed-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '81eba0b8d3fc2b58',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/maintain-fixed-assets'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/report-maintain-fixed-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-maintain-fixed-assets-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where maintain fixed assets stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of maintain fixed assets for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-maintain-fixed-assets-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads maintain fixed assets records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only fixed asset summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build a fixed assets summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-maintain-fixed-assets-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a fixed assets summary with totals, by-dimension breakdowns, and a Top 10 by value list exported to Excel from D365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportMaintainFixedAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportMaintainFixedAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-maintain-fixed-assets-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportMaintainFixedAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
