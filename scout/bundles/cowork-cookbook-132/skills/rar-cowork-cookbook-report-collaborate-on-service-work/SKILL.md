---
name: "rar-cowork-cookbook-report-collaborate-on-service-work"
description: "Builds a read-only Excel summary report of collaborate-on-service-work activity from Dynamics 365 F&SCM for a given legal entity and posted period, with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_collaborate_on_service_work", "rar_sha256": "ca9152f7739fcb3053ebae229c61510d9fd5ad80e0289c988eb187eccc964318", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_collaborate_on_service_work`. The original RAPP
agent is preserved byte-for-byte in `report_collaborate_on_service_work_agent.py` and in the RCI capsule.

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

Collaborate on service work Summary Report — Builds a read-only Excel summary report of collaborate-on-service-work activity from Dynamics 365 F&SCM for a given legal entity and posted period, with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-collaborate-on-service-work
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
      "description": "Dimensions for breakdowns where applicable: department, category, responsible owner.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-collaborate-on-service-work-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to report on; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_collaborate_on_service_work_agent.py` and embedded as the fenced Python below (sha256 ca9152f7739fcb30…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_collaborate_on_service_work_agent.py` first:

```bash
python3 report_collaborate_on_service_work_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_collaborate_on_service_work_agent.py   # or on stdin
python3 report_collaborate_on_service_work_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Collaborate on service work Summary Report — Builds a read-only Excel summary report of collaborate-on-service-work activity from Dynamics 365 F&SCM for a given legal entity and posted period, with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-collaborate-on-service-work
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_collaborate_on_service_work',
    "version": '3.0.3',
    "display_name": 'Collaborate on service work Summary Report',
    "description": 'Builds a read-only Excel summary report of collaborate-on-service-work activity from Dynamics 365 F&SCM for a given legal entity and posted period, with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-collaborate-on-service-work',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-collaborate-on-service-work',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8f971a20dc38fdac',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/collaborate-on-service-work'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/report-collaborate-on-service-work', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-collaborate-on-service-work-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where collaborate on service work stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of collaborate on service work for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-collaborate-on-service-work-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads collaborate on service work records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only Excel summary report of collaborate-on-service-work activity from Dynamics 365 F&SCM for a given legal entity and posted period, with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a collaborate on service work summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-collaborate-on-service-work-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary report of service work collaboration activity from D365 ERP, broken out by dimension with a Top 10 by value section.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportCollaborateOnServiceWork(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportCollaborateOnServiceWork'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-collaborate-on-service-work-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportCollaborateOnServiceWork().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
