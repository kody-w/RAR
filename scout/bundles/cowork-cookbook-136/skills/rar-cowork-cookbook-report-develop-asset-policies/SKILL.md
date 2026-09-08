---
name: "rar-cowork-cookbook-report-develop-asset-policies"
description: "Builds a read-only summary report of develop asset policies from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_asset_policies", "rar_sha256": "9f6102d621953717e8524fc34cd342dc89f0f28d0c506958f06ed230591be0fc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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
