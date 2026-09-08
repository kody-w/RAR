---
name: "rar-cowork-cookbook-ppt-exec-handle-background-job-errors-and-exceptions"
description: "Builds a read-only executive PowerPoint deck on background job errors and exceptions from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_handle_background_job_errors_and_exceptions", "rar_sha256": "d704d58606bdd19699be1f1f6541bea5ea5c4b32ca0cf782fbe4266e6610714b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_handle_background_job_errors_and_exceptions`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_handle_background_job_errors_and_exceptions_agent.py` and in the RCI capsule.

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

Handle background job errors and exceptions Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on background job errors and exceptions from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-handle-background-job-errors-and-exceptions
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
      "description": "Dynamics 365 legal entity to report on (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-handle-background-job-errors-and-exceptions-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend chart (e.g. monthly, dated 2026-05-24).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_handle_background_job_errors_and_exceptions_agent.py` and embedded as the fenced Python below (sha256 d704d58606bdd196…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_handle_background_job_errors_and_exceptions_agent.py` first:

```bash
python3 ppt_exec_handle_background_job_errors_and_exceptions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_handle_background_job_errors_and_exceptions_agent.py   # or on stdin
python3 ppt_exec_handle_background_job_errors_and_exceptions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Handle background job errors and exceptions Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on background job errors and exceptions from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-handle-background-job-errors-and-exceptions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_handle_background_job_errors_and_exceptions',
    "version": '3.0.3',
    "display_name": 'Handle background job errors and exceptions Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on background job errors and exceptions from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-handle-background-job-errors-and-exceptions',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-handle-background-job-errors-and-exceptions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9189ca013a3b2d99',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/handle-background-job-errors-and-exceptions'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-handle-background-job-errors-and-exceptions', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-handle-background-job-errors-and-exceptions-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend chart (e.g. monthly, dated 2026-05-24).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for handle background job errors and exceptions reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on handle background job errors and exceptions for a 15-minute monthly review. Produce 'ppt-exec-handle-background-job-errors-and-exceptions-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads handle background job errors and exceptions data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on background job errors and exceptions from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes.', 'example_request': "Build an executive PowerPoint on background job errors and exceptions for USMF for this month's 15-minute review.", 'inputs': [{'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-handle-background-job-errors-and-exceptions-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend chart (e.g. monthly, dated 2026-05-24).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a 15-minute monthly review deck on background job errors and exceptions built from D365 ERP data, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecHandleBackgroundJobErrorsAndExceptions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecHandleBackgroundJobErrorsAndExceptions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-handle-background-job-errors-and-exceptions-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend chart (e.g. monthly, dated 2026-05-24).', 'type': 'string'}},
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
    print(PptExecHandleBackgroundJobErrorsAndExceptions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
