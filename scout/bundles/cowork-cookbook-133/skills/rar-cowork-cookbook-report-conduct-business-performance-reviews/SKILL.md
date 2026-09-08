---
name: "rar-cowork-cookbook-report-conduct-business-performance-reviews"
description: "Builds a read-only business performance review summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_conduct_business_performance_reviews", "rar_sha256": "a9058af45ad2b448b5492041c52b009ffff0b33a7867cbfb203ee24457deb242", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_conduct_business_performance_reviews`. The original RAPP
agent is preserved byte-for-byte in `report_conduct_business_performance_reviews_agent.py` and in the RCI capsule.

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

Conduct business performance reviews Summary Report — Builds a read-only business performance review summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-conduct-business-performance-reviews
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
    "legal_entity": {
      "description": "D365 legal entity to report against (defaults to USMF).",
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
      "description": "Name of the Excel workbook to produce, e.g. report-conduct-business-performance-reviews-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to summarize; defaults to the most recent posted period available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_conduct_business_performance_reviews_agent.py` and embedded as the fenced Python below (sha256 a9058af45ad2b448…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_conduct_business_performance_reviews_agent.py` first:

```bash
python3 report_conduct_business_performance_reviews_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_conduct_business_performance_reviews_agent.py   # or on stdin
python3 report_conduct_business_performance_reviews_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct business performance reviews Summary Report — Builds a read-only business performance review summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-conduct-business-performance-reviews
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_conduct_business_performance_reviews',
    "version": '3.0.3',
    "display_name": 'Conduct business performance reviews Summary Report',
    "description": 'Builds a read-only business performance review summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'report-conduct-business-performance-reviews',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-conduct-business-performance-reviews',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1ee2aa96f01e1a96',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/conduct-business-performance-reviews'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/report-conduct-business-performance-reviews', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against (defaults to USMF).', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-conduct-business-performance-reviews-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where conduct business performance reviews stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of conduct business performance reviews for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-conduct-business-performance-reviews-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads conduct business performance reviews records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only business performance review summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a business performance review summary report for USMF from D365 for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against (defaults to USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available in the tenant.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-conduct-business-performance-reviews-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-change summary report of business performance review activity from D365 ERP with totals, dimension breakdowns, and top 10 by value.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportConductBusinessPerformanceReviews(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportConductBusinessPerformanceReviews'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against (defaults to USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-conduct-business-performance-reviews-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportConductBusinessPerformanceReviews().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
