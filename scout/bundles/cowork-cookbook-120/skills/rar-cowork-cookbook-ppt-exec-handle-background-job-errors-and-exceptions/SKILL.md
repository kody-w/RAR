---
name: "rar-cowork-cookbook-ppt-exec-handle-background-job-errors-and-exceptions"
description: "Builds a read-only executive PowerPoint deck on background job errors and exceptions from Dynamics 365 F&SCM data, with title, KPI, trend, red-flag, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_handle_background_job_errors_and_exceptions", "rar_sha256": "d704d58606bdd19699be1f1f6541bea5ea5c4b32ca0cf782fbe4266e6610714b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
