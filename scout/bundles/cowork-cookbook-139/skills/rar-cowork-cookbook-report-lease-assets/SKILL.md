---
name: "rar-cowork-cookbook-report-lease-assets"
description: "Builds a read-only lease assets summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_lease_assets", "rar_sha256": "9bd65520605cd6f0771087c4074d606fbad774d2e1737bfb8f83ed43f9fbea76", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
