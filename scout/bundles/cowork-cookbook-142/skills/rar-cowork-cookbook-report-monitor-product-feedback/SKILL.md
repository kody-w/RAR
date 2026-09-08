---
name: "rar-cowork-cookbook-report-monitor-product-feedback"
description: "Builds a read-only monitor product feedback summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_monitor_product_feedback", "rar_sha256": "ca42571951be922162c44b6dda7b533502aff96f68fb13483cfe07a3d2eb2f45", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
