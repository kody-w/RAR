---
name: "rar-cowork-cookbook-report-conduct-business-performance-reviews"
description: "Builds a read-only business performance review summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_conduct_business_performance_reviews", "rar_sha256": "a9058af45ad2b448b5492041c52b009ffff0b33a7867cbfb203ee24457deb242", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
