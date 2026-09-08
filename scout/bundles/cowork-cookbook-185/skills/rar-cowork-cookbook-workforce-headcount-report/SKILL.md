---
name: "rar-cowork-cookbook-workforce-headcount-report"
description: "Builds a workforce headcount report as of today from the configured HR data source, aggregated by department, location, and worker type, with year-over-year trend if available, delivered as an Excel workbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/workforce_headcount_report", "rar_sha256": "7b593899954da2ff4c804bf7249b135859f72bc4bb8056a66eed2d9adbd021e7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
