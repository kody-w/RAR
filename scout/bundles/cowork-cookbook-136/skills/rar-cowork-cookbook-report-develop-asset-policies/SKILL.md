---
name: "rar-cowork-cookbook-report-develop-asset-policies"
description: "Builds a read-only summary report of develop asset policies from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_asset_policies", "rar_sha256": "9f6102d621953717e8524fc34cd342dc89f0f28d0c506958f06ed230591be0fc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_develop_asset_policies`. The original RAPP
agent is preserved byte-for-byte in `report_develop_asset_policies_agent.py` and in the RCI capsule.

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

Develop asset policies Summary Report — Builds a read-only summary report of develop asset policies from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-asset-policies
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
      "description": "Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-develop-asset-policies-2026-05-24.xlsx.",
      "type": "string"
    },
    "posted_period": {
      "description": "The posted period to summarize; defaults to the most recent posted period available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_asset_policies_agent.py` and embedded as the fenced Python below (sha256 9f6102d621953717…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_asset_policies_agent.py` first:

```bash
python3 report_develop_asset_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_develop_asset_policies_agent.py   # or on stdin
python3 report_develop_asset_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop asset policies Summary Report — Builds a read-only summary report of develop asset policies from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-asset-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_develop_asset_policies',
    "version": '3.0.3',
    "display_name": 'Develop asset policies Summary Report',
    "description": 'Builds a read-only summary report of develop asset policies from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-develop-asset-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-develop-asset-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '34fe9c32c6ea9791',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-asset-policies'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/report-develop-asset-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-develop-asset-policies-2026-05-24.xlsx.', 'posted_period': 'The posted period to summarize; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where develop asset policies stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of develop asset policies for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-develop-asset-policies-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads develop asset policies records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of develop asset policies from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a develop asset policies summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'The posted period to summarize; defaults to the most recent posted period available in the tenant.', 'name': 'posted_period'}, {'description': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-develop-asset-policies-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write D365 ERP summary of develop asset policies with totals, by-dimension breakdowns, and a Top 10 by value list in Excel.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDevelopAssetPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDevelopAssetPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-develop-asset-policies-2026-05-24.xlsx.', 'type': 'string'}, 'posted_period': {'description': 'The posted period to summarize; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportDevelopAssetPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
