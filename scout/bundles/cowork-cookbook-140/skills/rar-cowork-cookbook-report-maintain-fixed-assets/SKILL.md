---
name: "rar-cowork-cookbook-report-maintain-fixed-assets"
description: "Builds a read-only fixed asset summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_maintain_fixed_assets", "rar_sha256": "8bbadcdb9483765dd275b70ec147291066421794f0f5dee5eb520275d70d17bc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
