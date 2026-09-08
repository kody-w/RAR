---
name: "rar-cowork-cookbook-report-conduct-root-cause-analysis"
description: "Builds a read-only conduct root cause analysis summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_conduct_root_cause_analysis", "rar_sha256": "fb3efa4e28633837034c7247cbfe6a414a9c4ab6c5f333ff87027f4a184cc8c9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_conduct_root_cause_analysis`. The original RAPP
agent is preserved byte-for-byte in `report_conduct_root_cause_analysis_agent.py` and in the RCI capsule.

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

Conduct root cause analysis Summary Report — Builds a read-only conduct root cause analysis summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-conduct-root-cause-analysis
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
      "description": "D365 legal entity to report on (e.g. USMF).",
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
      "description": "Name of the Excel workbook to produce, e.g. report-conduct-root-cause-analysis-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to cover; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_conduct_root_cause_analysis_agent.py` and embedded as the fenced Python below (sha256 fb3efa4e28633837…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_conduct_root_cause_analysis_agent.py` first:

```bash
python3 report_conduct_root_cause_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_conduct_root_cause_analysis_agent.py   # or on stdin
python3 report_conduct_root_cause_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct root cause analysis Summary Report — Builds a read-only conduct root cause analysis summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-conduct-root-cause-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_conduct_root_cause_analysis',
    "version": '3.0.3',
    "display_name": 'Conduct root cause analysis Summary Report',
    "description": 'Builds a read-only conduct root cause analysis summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-conduct-root-cause-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-conduct-root-cause-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2fa167651fc9b95c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/conduct-root-cause-analysis'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-conduct-root-cause-analysis', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-conduct-root-cause-analysis-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where conduct root cause analysis stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of conduct root cause analysis for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-conduct-root-cause-analysis-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads conduct root cause analysis records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only conduct root cause analysis summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build a conduct root cause analysis summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-conduct-root-cause-analysis-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a conduct root cause analysis summary with totals, by-dimension breakdowns, and a Top 10 by value list from D365 ERP data, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportConductRootCauseAnalysis(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportConductRootCauseAnalysis'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-conduct-root-cause-analysis-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportConductRootCauseAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adOjRrbmX9G8N2JsX1W9rAJRNzpiWAVICAQCSbg6yuwgVrEJ8Pi/TyKpquxud/ftifk0qrIlIPPkWZ/nZCW/vjldG5f126c3I3CKxcbJsiQO6oVT+Au2vJd1Cr7K1AX/LbyyaOvE7dqybt4+vPlB49VJ1SZlAaYzXZL5zcJZ1IHjfyyLbJzH+53XLuqybBee0zUBEOtkY5M0i6bLc6ceweiqrNtFWJf5ghsLJ0+8ZoERq4XwPw1WWYQlUGURJX1QLLIgcrJFULRJOz70q8qmDcBXUCel/wGIaru6SIoIPFzwgxdki1n/h+r3pI0XxnPNDwsuaJ0k+/AQciyrBQIv3HHRO1kXLJo4CNrmHdgXDE5eZUHz9unnv354S8Dvt0+/vnmZ04Bbb/pDcfZpog4sZGcD6Zd9YHrmFBEYV43AvwW4BmoCa3Jwyw/CxevqxybIwg+L//zP9O7UUfPTp8/F4vX5/Db/0bti0cbBoi2dh7GeUzlukgEXvC/o7O6Mzcvu2fUNCE8RvT9nfpcELPzL/OzH5yLvUdD++PmtBCo4c/A+v/20AG7+/FZ38+/3WUr140/vWXkP6h9/+i6n6dxrAOIJhAGt37+8rl9iwcDvQ5Nw8cXQePa1Vh14SRUA4b+zb/48VX+Je7nky3Pwj2X1YfHnkmd7/gL0fSagC+T+uVjgAzDz7f1aJsWPrzXqEqSSU3jBjz/9I7FeHHhpljTtf0vuz0/BMch64K2XS3768AjfXxfLl23fZP7jZSuQMP+OJWD41+W+OeofyX5E9m9EZ0kRNN9i+afi/mzC8i+Ln/+hbf9swodF+PmNCzJQy7XjZsGnxa+PFPn5B//7zR/++hsQ/S/FGGVXew8JX3KnSMKgab98+fmH5nH7h7/+/ENXgSwOnPxLV2d/JvPP/PpY5w8efI368Y9zwfpmkRblvVh8q6HFr2X1P+rf3heWkyX+9/vNp8XvK3H+LBezEV8Xfbrgd9XYAF1/58ef3n4D2FMAawDMzI8BfvzHfyyUxKvLpgzbheGVHYDYDsBiHszKH2MAr+DvjBp1APzaJMCxr3Eg/+cIzxqX4eKX/+U9IP6j94J46AnHX17I/WVG7i8P5P7yFbl/eV8cgeSyTqIE3FrotKZ9LpwI4PK8alUHTVD3AKncsQ0+goL+OP9YJMXil38t/MtDzns1/vLA5uSJfTorzbjXdFnwPlt4igEbPO3xANQHQ+B1YIms9IA+YQIgeyaDpsx6gJuzN5o0ybKFnwBkAdz1JA/gsU+zsF9++cV1mvhz8QRqbPEktQYCA76ps/j4ERgWZkkUt5+LwIvLxQ+//vbD4n8v/tmsh/B5DQ1QxiseQEPZUPcLUF9dDoaBUIHgAvB4xOPX317uBWIKwMIgekmYBM/JID/TwP/qa0OkP6IrYuEGwMfAv/ns25n8kvZ9IYWLb/q+KHbmhxgQ5sIPqqDwg8IbgVQHmPPNkwWg6QYkYRMCjpzZel71F7d2HirmoNCd9peFwmqAjcoM/G9W8zEITC6LBLj/WyY87wMh9Q/Ngvkq4n2xnzNyUTm1U8W181ojdJ5xmcn+NR0IdxZFcP9czMQbzK56lMfTPWAQ8Iz3CunHOeag2wDsXvjN17UfY5yZM48P7qw/F80r9Z16DoUHqAAsGnWJPxPCf71SqonLLvMf/gOazpJeUfBfUXnkIPtPeptXn7F4tgiLzx0KI/ji/7MGaXYCvdno/IY+8tyC3x/1yzM4c5s4B/HZWc66zEo+CvF79/IVob4C9eciS0Cm1eN/PUc+Qvoa8wS/rgam6LT+kA/yCQRnlvtI99l7dT0XivO5+MoIQP3FA/5AxAE2gNqZU/brgvPTr5rGAADm6+/dwSM9an92AEjpRdW5GUi3MAh81/FSoNUcxK+RBbkfzOV7jxMv/oNVczBADIH8BVAiAUUIWOP9G0o/n35V/Q8Tn03QPOXRIHagYuuHAKBHMCs4h2YOGlCvfXblwM5PDyHAjLxqZ9tdUDPA0ufNoA5uXdIk7YyPT78GFUDnj/P309L5bjBUoEyAs0AxVB3w7qN85qzJQYsDdAAIAqopTwpA+cApLyc8BDr5jAUAa1896VPi4/bLoOBRczNXfZ04GzLPmen/meZOMf4eMo5/liZAXj6PeKz7t5n2bbVZ9gybDYA+sOLXp88+4f1J9c9eYvFV7qe/2/b8+O/tjB7kbf4xAT4t4ratmk8Q9CTcr3z7DkALeuravLj34wsUPs6g8PEBCh+/gsIfJD+N/rT497T7g4hXdXxaIO/wOzw/2r2y6/UBzmA/MpeP+Pz0c6EH30EVLF/mIL3m0I0zOnxlwK9DAA1GNUAkMPjJiM1MpHfA3Q8KAHH4XPw+3edyAwxTRHN6NuXvYODRCoDUf4btG1OBR0UL1vbn5jEK5i3bozia4O1T0WXZhzeAlsF/Z6s201E+J3Uz7/BA+QDEbJPgceUC/VIflO0XHyRt0Tx7sF//ZvfLfXv2SLJvk2ZTOgAKAAAA7zp1OxPZB2BCG0TljLRgMGhVKjDx0aWBKUH9YfYSoCinqoBBc13MtrVjNRvz3OPNXeEDvYb275VRHz+c7P2F483vS+JFbzPX/K5yn/4HynrA9g8LH+jXzLoB/89umaveadKHcX+qy4N6vjyp50+8M/PVH9hp7h2exAZw8cfgPXpfmIYi/PSnwr/1xn8v+QRaklmYX36a2fnDC/vAN9jPAD9/3ZoAk16bxcfOvujAPvzneVs0R/8xZf4B5oCvb5O+/RuHG7z99c/0egDklzlHn5n2t9rtZ+ADxDB7+G/4FugM1gUJCbz9MP9fV/9HFEaJj/DqI4q/D1kz/Kmvnlz/96pov28F5tUf3c9/AbeETpeB4mrLh5r53CKCbJhp8Q/tw8LpQSr9g2QECz/IBVD07NfvAfvutvKxtXyomDnt819Cfn0DVeeAZHNedffam4DhAIs/NnM/BgFsAguC6yeKgGf/F7uWl4QmdkDPDESELgYMxwN0TWDYGiNhDPdIFCc9NwwIB0dwh/JwxyW8VYhhWBiuSRglQ9xB1rjnrT0KyHui0Ze57UxmrVYUGcIUhYY4gsI+8CuK+/6aWAMZJAo7lOus3BXluN+npknhv0x9mjb78dsGanbJy2KAQgQORop4I9HPDwtRiAvhpDvU5+UZXg/Z/dRVgpugKeGX/Q7Rg8FHJ+agrp0OHncXtjckkS8UMzlykgufhKiHpfDGh/aOLI7KJPCZjtbWlJKHgeOjxAaKq8flco3uc81bu8XGrizplG1320bYbpqWkcbMy04DUnmW3O13Ozc5q5ZtXioICtQQL1JLXvEnM9a3eqs0R/eSaLzMnO43oXTppilhHCXskcd9J9TOyAUSx36kVAyPM6vk0m1PlGa1KTNz5I2mwzFJPsiarGT3MryVyeTQsmFbp9Rza9aAxMQkIsOzYcvCm6YbdmfPzdAzD/G5UWUFP15GrWmE+zpMFOsUyrpcXfRgi1i3cGJwqqut5aU9TxQBqYzSYzUOQRR+JqlgS2UGyxib2qtga6Dz4bQlhsrici/mC4oeISMaOy9DWFFuGT5Zb2tt4jlh2iRnmVNoOrlFdYNDk63a6tlzyq0cd+e+iPdl0m1P/AaNcETBibMhW9FZRE4xfh+S0ZPqiSWm4JoRBBR7BonmGJbrh8tl5PRzKmxsQZebEBdzxFDlw04+bYXrdk2ny1Sj7DK/WVubb4f+QnL+qYEq+lhy9UHYSPEuFMaC32ckWiGrFRZ3R0/bes6qjNLbiUc2WWpUuJrFh4Epq1g4IOnGsgepuw20XRxpbe1CW2Nfowf7cm/zMriZHHVqLqtdZfinIrmFu9o+LrtDC6casrW8ODerUwZULl1Sq1hSNq+XUSpWfMVXlqtK8NCpB38N8Sv64mQw6MLMRiNuPrq9l4p7MC/mdZSX23DwIn7fwNjOZ7tAQOhqsy8v/LJymFPcOjTdo+6pDhIzKbxjleluzW27VTvd6iRjGCqVvbUQxjeF5B3TRa84pKiKWB4afjqXGyigMYZfnzseVIZQDCeCE8qwDU9LfmzGaXduVuoxZYONX+GhXTXHOxEtFQOnWh+H5GAZNr2vFaGHsXazn9bHYu076YVBYjkmCQ66i4GmnB0YQ8W7PqgFtoRCQwu4FLfGRqBWcspZEYGuWcfY7N1DRPtCIQRErGCyzNbWQTTvJ2YdHxK4QKGYw5K9bhbLiLDbFAkEZ5V3IxMjSMGgaETanc+fjqy+py+pU1OSYcAh3aKSsDvXNGbyB5XzNLoXTIweSn6Fq8hEH93RWR86d5Xt09X9QlDJOdUIQcdVaNo4G/dmbTSLt2KE2RpqtDd1VTSV3SGtje1uFMzjKjs3wXCstBVn3w3qDintwcyYTVuFuJsMVpetHdO5qKG9HjrAludNrfTxJKS0qznMtdptaFXkJ8GzmBtzCBraZK5JusJta6v3sX3CNkot4XJ0i67SrqlA3lkkvz1tvKTbbcjBCk79Tc9OEZ0cnNso+dOIOBKAvQbd7zabYn9ri2Uj0yeqlO6WO6wuzTYzNJHnNltlVx1UK7wdqenU1SNjsQemTMw9M5FDM5K2KiCiUEIKOh2wdYG152EcvNAV6V0ZJ51VEPR1LRZJfad9qNEZhFzFInwS80R2TXaHw+Z1w3jkRaG38Fh4O/cOgnwNYWE8wNZ2neAVfgrr05bK47s7DWaubPana7QMu8SsNF+dlGXCKteb7BRcH4rkcezsI0xJBGg1L4KI79LV6KUFzOdIWWTYBXN7atee+zN1IAQ0ooFAskGYgtNLaViLaw7rE9NZX7UO5l2hT5eYz+2Rkt4pDp2ftaMfI4F+aFaabmoaFVwYfoDz1t4Ixjk1dedecfooFBs51iTp6rR7AgqXo0M2cK6naVJeN8YGvV3QFMXRw5Ar9vXmU1tLjXrn1FqCKOm5yYlho2+3pStKTGrYKGYE99WkbzMhZYjteF9i1kZxbiZK3ZiQhiScP3DuYe2i2SqmTjVzal26W52EbqUds/jk7WS58UxJnposPFfLZSD2w73hLSrKzOVxe9O3qlmQEowuB53Yiawhu+MgAU6nGLrfdxvRPQ4xPd1gS1pCWqUBElh29AT12nXCKc7JbCxFDtxemZaWy29oZZ2cIIb0ehlAdmnc1mfJjhGT3ctTe8Bodu+f0c2FrfNzsquZtt9nJ1k5ltEU96nXx/VR2d86GWfrm8cj48UzN8dos12KgH9RUOeOnSlnTnX2ja7DXLSmYOusXm8dlincLUUVVduEQlqYwi6/KPYaO9jC8oSuBq9mNpRTQJrt5rkFYQpG+/yBHzi3L2/HeOegCnyPt7dxsmnuOsTJVO6wEREBH0oyFcr5llfVeNQjg1vRtpSyKXy5tCVU4+IluVaslDjrMCXbcuKFzJHuyYqPQDafd0avlYdktbPJDgIkzd6sXEY2wXUJ32Az2fa6VCbnxhHimok8xb2GxHDoBNZW0o2/Wu6SMpLWkrXfs7YK51UqJSF0dpA0qcbSv26HpCnwA9yGEiiP5dXRTz3jyPVevrtBwWCcwtfHQU33up8Jpmkvd3xlSgWeSHxJC9FREip2uat9QFZmI8jNhc0GntmMYdAdBLw8WZLaGXRpF2dXs5RgI8mQdj4l0nkXo6XbnDLCc2pUdk4JuuNy3d/dHSFJuS6GFSahCZzM8/KqCgd2v+PDzYantIJSI1vT03LDhMm9appbvEP2SRvaKecK8IkxSq/amOdGboabItWmGR2YKwPZ0PpqjvZBOCqHzf1SKk59dw2IKhMePGDrwwCtdvuB5zDBb8Y40djBILHG4km6TOVdHZ43Z90vKuoeSeqkcay7b84Tfthzuih1lxqf+i3EZcsr5NJ2RdDmeTeQ3rmu8kAMIDo3SSbCBlMmOfN4ks5e5OwPRIIOLSfv+VzBLVaQjjRUw+bpcLPzggtiQRdKCblFMmhl2qlRCpJeOixxW8Y7mVbUlh0vetONcZ7cvRV29WmKINq9zceRc5fQDEpXGn2Xt2tDSRM/DnI4QdJeTRRnt8ZCVqId9JjiLhzG/fHo0GzseISQU6rf3G7HhjcYXDJyxmb9k70Xl+lA0YG2Af3++sbt/TtmhxDkyY6AXC4KdnADfrUnC3GMWmqZE7c7vbOhmB+J1ZXN9zKURgahli3S3kb1fNit1/bhiIqcsbIMPpMiqkRAgxLV+smm91ucU2XQ7Wy4ip3SITV0xpzwbbm1JLOn1+3NEG3S6rE4pI7cFlT6JaWOFxFA+qDt+U6hcV5PlDy5ioOcELqdJGwjs5bLrO67vSTWdz1HzwevpUDjCx+xwcm7Nr0eIvlcmk6MtznS8HeGEVassVESKS1vziaVhAvR3EIvo/TzNKXtgJ/uVzFfauSWso4HzXANXo0YvAqXpx05kkHP3N3UVTo6k+xIF/SA7y8MvU7d683apzGzwa8ZLt1lTMeiCl8HmlYRy44bqD0fQuZShhqjzm+3QCj6805T5bCMjRqL2Rt70+NNRtg0Q2fjwT101MmBOem6Ym9pOLSFu70z9nXE2hiAJ1OYRLHzUHzPs8v+IgX302heWbH0Vzg7VM4x2J0dGVVM6l4uh+56oaxsR8KGLbGHIOLiHco37gZnr6N38I55FiWkSVsJNMoqso+Oy9AEXV3AnFzxykjNLvM1hrfdntiKXRYrO2bcD+qIXcOtlIWsoIqN2DQrbCPx45pr9/hFkFrLridZqcmOQIvLYX3JZZepAZNL2+UVLRw2XAf7tGRX55t2StRss9+M8N7M+WG6H0CrKwFwhzRSj3Afijo5qFDB0PUjbqxAcyvyZB1uGtpaJfE+ge4jnDp3Al+Lptb29sFBJ8K2JEUd0UmyJONYUtTF085hT7VLLS0VbgpaWuHazCym627rjymTyL5LNsSx2l2V1WXrckHvnrdmR8stK8a86gSHQSE4eG91Ld+YlNTu4v2t2bpCcHT2hYMhIqAFaRoTD8oZaCn3VcTnl8osGZa1rvkpCLaHyzYnj/fOW2+vXHPQtiKt3AUVhOW0tTY625D8DrB4SB+vqa2oRKuyp33WdQG8skOJhZV1felJ+g6ralnZNWjcWvZ6QFBkC+ptMHcFcbo4+d6yBVPVKXkjnypuChlnDbshl1P6Dt9gjOmFlZLerVaHMhtfiq3Tj4YhVp3RLdc1h6FymLuM4/Yyzxx0auwAi5ona6JSp224C76js/I4RBziwlobLAld5zqqNEcG1UPUXuLylrWqmgH0K5I9VUubdeMKqtAnFhSZR8HzhX0K1ZelYRrG2tdcTCaNe8SWYGdWj61hrBB1s2OqoKC2A3H07CowI1bKR/lYr6HucrsU5wFWDXbMfJsQeSy8dRFqsBSdHmOH26f6uJJZhSrxUbVQjsmik4d7qKOPqXI4jFG/3lzKbS9w+JWhzxPntLYprGDOHppKiO+yyWW6tNbhnTfpxRXmNck/HQHDTsSg6mSXxx1iBjIu0je7V24pyfU2fFYH1Zhu1Ha11g5Y60olfDJ2GqUcJxU9M/cbi4wwenO6rWbmvZFCbjWJ+3Jd10jTrwbMJh31cGyOm+WSWJORUunNtivOhrVbFlhk+NwmaE6n5ajh2/EinMzVjWsvnEjeUPbgEOPlGI3kiiADLNDKFbGCAvJaZcoB2gMwrgUa2/a1BOEwcXLoi31UiNEumqlsDx4v5nWRM5NfnGIz9eC8nqoTqmmxi7E9aB4wElUE9wxdKZJtBR/aueIE+kF/fRRR13K6O+nnYk7ShLm9w/61xy2YKSAn4swA3bp4D5ErsI87O6szyOc6X2EQD92dDsWY9EQhZ4SUL8TBWfLLwbsZsNUlmnZNT8OqELZGBinswYdG0MpSXN16tnLVthbpJ3sOU8I7byYqe7is3eV41HpN7zizPVc3u5lgK79PYc8gsFhfWKQqXQ2wWtYrG28YlslRnOKrKC9Xa5ifghzyURmG9q4S03SF10tk2XUddPRkibyskRan4SXpHuXUDE+HStvcaBmHBDuctK5wK+CuRKynk+V7e3WqTESsHYEaW5HwrK4ukAtkx+U6Kim5ZJScFpSciymKwAmymbRkk9NRgCJ1zVs22x8JQzi3eQ32U6swX5oKjFd3eedS3OUaFzZWUvbqQF2GROG06TTZ1MqDeMHbXeHYremrFctYFIE9f8DRlOjDeNxa8WHLFFdB2ZEkMhzgrLftzlXxWBFNXlBwWKcuJtjXblopFwGOXGXQ2U7mNYFFF41cpXCsjCDHq99ujQCqEWKtcrpEQdik+ywJn5Sz7GmuuMX2a1FuWp+r1VUmFtK9X2tcv2lukwgdS+tOk4aT+f2YUeOYXmB26Z9aNRluRDfok6fvHfXi7YVJufZhvnbsI0I5AcXsIulike15vwuMqu7zZRftbNVF6gHs8NNsYDKKpMc7gol3t73rVhYwFEx1oBTPWFd04tUMcQW5XQNYxRvWQ1YpilYIh+iKoyP7NiuCBNXRsCXOkrI/4LvNBe/yux306Dis7z4tiNWBDFIbh/37fSeJEBw218hHzOMGX/P+tZb6W+tXFUfal+bWePSejDZFX5dUjGM9KDyfsKETvKrRroQ0r7IwvTlAUyhStwxTNTfVhGk3Bd00acP9alKqNDE7HHPuK7TAWAJpbTK0LAUDlQb2cKZAHeFK6DFrH+LncwU6Q3W341c6YUCRjx+qhr6sJ9egkBbFgxaprbCTTMevr2dtzKVVG+CkJOMISVaoSxzCaSuGw6pXuV5p6bPMjBsr01L1JlAnkvcv+8hSbVdZ1sGe0HBq3exqidmLZ0vqo1NsaD1xv+KSsAqC0pQu4cgcie11kkdT8QNbOh6VcU/W97osCSHF+pFV1JiDdpdOWw5xKFS5knTIqgh2DTeut1FzRWXfviriErFI4dz0RwSmCXa1OqZH/66zRGLT/jWMYuSGaHpCijipbMWWiZut5kIUe8EuBVpfkn4sS02IqxPZ79bNEu4P25QUmuu9RZikEpPphB3beut5WFZXJ9j1yLOKIWqdgdbk1Af3SRao4DTktQk4asiBsvaG60gkP7rFDaCesnIV6kAgtpPjW2OFVet7eWXKUbWvy32xC/1OdkU+JoK1lRjnpU2rtbmuaLNXva3GVretsD+zuw3oRG+EIBNHH3e8oc9WPFY0Y+tgauVxXW/B3Prmwf5SNgMfijMIWVcMSa1wxtWmIpOz+qLDh9wQT8b2iEmRv743SeS5+kBBxBlroRKRtCVUEt1xT9Bjfq69jd6jazRTO58cVr4bNBCcmUi21pLb+bYijSKGjbPq+HdI6G/OjjQzlrO2qDJOnsLJ/DWMR7AjaIfr0uHcZLUeJVSbuAq5ImUQwO5e846QfEmbi1CVHGs3voCQnejBS5cg6azz9YQjY/4+shjGXyKeGGDjECoSBFoYfM+293BPNSlKBidPzeDLSpzCIbW2Yg2Jire3EZArtLbS4b3QKP4FStYwh1xja3lKLarQroZKtb5HVVbhYburGJY1dg7xZBVCt46KEaGA1g6NYh4axN46kXuMNu9k4Bst6W/rTLpduzxt3Xq37kHGkrf1mDia70GxrVJ+ZdX7E77rGawYMa/2B9cBLqzic9IvL3F93g/oPaH6PiQJK6bqZCJ3iH88hkXdWaduWpdV08ahPNHVClUZWji0kFwVrHNhy2t0MwgWYg2yalUuGHzk6A51dQFOkFYk2Bq5B7+RHUOxRBCYLUNJUtXrnR16pTuUV2QFXUhn7+365TmkEs0qSsklVjY1AZgIDY0ZzGtGEydVQ8jcuu82x4BZirk+FqYO7KeranS4a1ijfSdgEKSFTHVQSdq0pyUV10SZYhtHZy5VKIa5RHYdzQ/AmRKiNut9gBNifw+Xgc8TQsXRNP2Xtw9v3w/03v6NV9bmc53/Z8dLz5Ogr2+jPM4qA8f/9Fjr07+j1F8/vNVeAlR6HqM1WRe9jpz+5hDt478+gJznj883wb4ePT/P2Vsnmt+SfkvA1Katxy9NmT3eRwEz3K6Z36ts5ldvPfD9+wPX55Lgh+M/XycJ6i9t+eV5fBi8zS8+zm+aBH7y/TJ6nSx+ePNfb0N9wYjVl6CuZltfbzQAE7F3+B17++3/APqOBPDhLgAA -->
