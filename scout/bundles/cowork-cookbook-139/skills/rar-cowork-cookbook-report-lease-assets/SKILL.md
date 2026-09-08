---
name: "rar-cowork-cookbook-report-lease-assets"
description: "Builds a read-only lease assets summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_lease_assets", "rar_sha256": "9bd65520605cd6f0771087c4074d606fbad774d2e1737bfb8f83ed43f9fbea76", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_lease_assets`. The original RAPP
agent is preserved byte-for-byte in `report_lease_assets_agent.py` and in the RCI capsule.

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

Lease assets Summary Report — Builds a read-only lease assets summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-lease-assets
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
      "description": "D365 legal entity to report against, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-lease-assets-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_lease_assets_agent.py` and embedded as the fenced Python below (sha256 9bd65520605cd6f0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_lease_assets_agent.py` first:

```bash
python3 report_lease_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_lease_assets_agent.py   # or on stdin
python3 report_lease_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Lease assets Summary Report — Builds a read-only lease assets summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-lease-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_lease_assets',
    "version": '3.0.3',
    "display_name": 'Lease assets Summary Report',
    "description": 'Builds a read-only lease assets summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
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
        "upstream_slug": 'report-lease-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-lease-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '57369fa34be25878',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/lease-assets'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/report-lease-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-lease-assets-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where lease assets stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of lease assets for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-lease-assets-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads lease assets records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only lease assets summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build a lease assets summary report for USMF for the latest posted period as an Excel workbook with a Top 10 sheet.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-lease-assets-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a lease assets summary report from D365 ERP with totals, by-dimension breakdowns, and a Top 10 by value list, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportLeaseAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportLeaseAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-lease-assets-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportLeaseAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
