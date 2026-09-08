---
name: "rar-cowork-cookbook-report-monitor-product-feedback"
description: "Builds a read-only monitor product feedback summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_monitor_product_feedback", "rar_sha256": "ca42571951be922162c44b6dda7b533502aff96f68fb13483cfe07a3d2eb2f45", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_monitor_product_feedback`. The original RAPP
agent is preserved byte-for-byte in `report_monitor_product_feedback_agent.py` and in the RCI capsule.

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

Monitor product feedback Summary Report — Builds a read-only monitor product feedback summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-monitor-product-feedback
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
      "description": "Dynamics 365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-monitor-product-feedback-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to cover; defaults to the most recent posted period available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_monitor_product_feedback_agent.py` and embedded as the fenced Python below (sha256 ca42571951be9221…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_monitor_product_feedback_agent.py` first:

```bash
python3 report_monitor_product_feedback_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_monitor_product_feedback_agent.py   # or on stdin
python3 report_monitor_product_feedback_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor product feedback Summary Report — Builds a read-only monitor product feedback summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-monitor-product-feedback
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_monitor_product_feedback',
    "version": '3.0.3',
    "display_name": 'Monitor product feedback Summary Report',
    "description": 'Builds a read-only monitor product feedback summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-monitor-product-feedback',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-monitor-product-feedback',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b9349610a42ae9cb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/analyze-product-performance/monitor-product-feedback'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/report-monitor-product-feedback', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-monitor-product-feedback-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where monitor product feedback stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of monitor product feedback for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-monitor-product-feedback-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads monitor product feedback records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only monitor product feedback summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a monitor product feedback summary report from D365 USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available in the tenant.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-monitor-product-feedback-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary report of monitor product feedback from D365 ERP with totals, by-dimension breakdowns, and a Top 10 by value section.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportMonitorProductFeedback(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportMonitorProductFeedback'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-monitor-product-feedback-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportMonitorProductFeedback().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
