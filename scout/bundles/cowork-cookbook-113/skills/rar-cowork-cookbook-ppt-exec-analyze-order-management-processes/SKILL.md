---
name: "rar-cowork-cookbook-ppt-exec-analyze-order-management-processes"
description: "Builds a read-only executive PowerPoint deck analyzing order management processes from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_analyze_order_management_processes", "rar_sha256": "610c1f3c9439f2eaba3a377a24b2b28b58f3d3ab6485bba655c282090ccd0aa7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_analyze_order_management_processes`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_analyze_order_management_processes_agent.py` and in the RCI capsule.

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

Analyze order management processes Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck analyzing order management processes from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-analyze-order-management-processes
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
      "description": "D365 legal entity to analyze, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-analyze-order-management-processes-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length of the review the deck must fit, e.g. 15 minutes.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend chart (e.g. monthly review as of 2026-05-24).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_analyze_order_management_processes_agent.py` and embedded as the fenced Python below (sha256 610c1f3c9439f2ea…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_analyze_order_management_processes_agent.py` first:

```bash
python3 ppt_exec_analyze_order_management_processes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_analyze_order_management_processes_agent.py   # or on stdin
python3 ppt_exec_analyze_order_management_processes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze order management processes Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck analyzing order management processes from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-analyze-order-management-processes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_analyze_order_management_processes',
    "version": '3.0.3',
    "display_name": 'Analyze order management processes Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck analyzing order management processes from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-analyze-order-management-processes',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-analyze-order-management-processes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'da8c93e1015e7358',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/analyze-order-management-processes'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/ppt-exec-analyze-order-management-processes', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to analyze, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-analyze-order-management-processes-2026-05-24.pptx.', 'review_length': 'Length of the review the deck must fit, e.g. 15 minutes.', 'review_period': 'Reporting period and prior period used for the trend chart (e.g. monthly review as of 2026-05-24).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for analyze order management processes reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on analyze order management processes for a 15-minute monthly review. Produce 'ppt-exec-analyze-order-management-processes-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads analyze order management processes data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck analyzing order management processes from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on order management processes for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to analyze, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-analyze-order-management-processes-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend chart (e.g. monthly review as of 2026-05-24).', 'name': 'review_period'}, {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'name': 'review_length'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX on order management process status from D365 ERP data for a short monthly review meeting.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecAnalyzeOrderManagementProcesses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecAnalyzeOrderManagementProcesses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to analyze, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-analyze-order-management-processes-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length of the review the deck must fit, e.g. 15 minutes.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend chart (e.g. monthly review as of 2026-05-24).', 'type': 'string'}},
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
    print(PptExecAnalyzeOrderManagementProcesses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
