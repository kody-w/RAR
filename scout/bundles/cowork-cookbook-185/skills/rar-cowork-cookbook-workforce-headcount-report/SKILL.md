---
name: "rar-cowork-cookbook-workforce-headcount-report"
description: "Builds a workforce headcount report as of today from the configured HR data source, aggregated by department, location, and worker type, with year-over-year trend if available, delivered as an Excel workbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/workforce_headcount_report", "rar_sha256": "7b593899954da2ff4c804bf7249b135859f72bc4bb8056a66eed2d9adbd021e7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/workforce_headcount_report`. The original RAPP
agent is preserved byte-for-byte in `workforce_headcount_report_agent.py` and in the RCI capsule.

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

Workforce Headcount Report — Builds a workforce headcount report as of today from the configured HR data source, aggregated by department, location, and worker type, with year-over-year trend if available, delivered as an Excel workbook.

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
  Upstream entry : https://coworkcookbook.com/recipes/workforce-headcount-report
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `workforce_headcount_report_agent.py` and embedded as the fenced Python below (sha256 7b593899954da2ff…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `workforce_headcount_report_agent.py` first:

```bash
python3 workforce_headcount_report_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 workforce_headcount_report_agent.py   # or on stdin
python3 workforce_headcount_report_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Workforce Headcount Report — Builds a workforce headcount report as of today from the configured HR data source, aggregated by department, location, and worker type, with year-over-year trend if available, delivered as an Excel workbook.

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
  Upstream entry : https://coworkcookbook.com/recipes/workforce-headcount-report
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/workforce_headcount_report',
    "version": '3.0.3',
    "display_name": 'Workforce Headcount Report',
    "description": 'Builds a workforce headcount report as of today from the configured HR data source, aggregated by department, location, and worker type, with year-over-year trend if available, delivered as an Excel workbook.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'workforce-headcount-report',
        "upstream_url": 'https://coworkcookbook.com/recipes/workforce-headcount-report',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '375123a970962e45',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/workforce-headcount-report', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': []}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Read access to the configured HR data source via Cowork', 'Output matches: Workbook with headcount by dimension and YoY trend.'], 'confidence': 1.0, 'deliverable': 'Workbook with headcount by dimension and YoY trend.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives HR and finance a unified headcount source-of-truth that reconciles to payroll without spreadsheet stitching.', 'expected_output': 'Workbook with headcount by dimension and YoY trend.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Read access to the configured HR data source via Cowork'], 'prompt': 'Build a workforce headcount report as of today. Aggregate by department, by location, and by worker type (employee, contractor, intern). Include trend vs same date last year if data is available. Output as an Excel workbook.', 'steps': ['Paste the prompt.', 'Validate the trend figures with HR.'], 'tenant_caveat': "Validated end-to-end against a live Cowork tenant on 2026-05-23 with USMF. Cowork pulled 97 active workers (92 employees + 5 contractors + 0 interns) and produced Headcount-2026-05-23.xlsx with 6 sheets: Summary, By Department, By Location, By Worker Type, YoY Trend, and Detail (full roster of all 97). Honesty notes surfaced by the agent: (a) D365's worker type enum only has Employee/Contractor - the Intern row in the summary is structurally zero, not an empirical zero; (b) YoY change is zero because the demo source shows the same 97 personnel records active on both 2026-05-24 and 2025-05-24; (c) 9 recent hires (personnel #000763-000771) are unassigned department/position and roll up under 'Unassigned'.", 'verified_against': 'm365.cloud.microsoft 2026-05-23', 'what_it_does': 'HR snapshot of current headcount with year-over-year trend.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a workforce headcount report as of today from the configured HR data source, aggregated by department, location, and worker type, with year-over-year trend if available, delivered as an Excel workbook.', 'example_request': 'Build a headcount report as of today by department, location, and worker type with YoY trend, in Excel.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a current headcount report broken down by department, location, and worker type, with optional YoY trend, as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt.', 'Validate the trend figures with HR.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class WorkforceHeadcountReport(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WorkforceHeadcountReport'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(WorkforceHeadcountReport().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
