---
name: "rar-cowork-cookbook-ppt-exec-create-background-job-schedule"
description: "Builds a read-only executive PowerPoint deck on create background job schedule status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_create_background_job_schedule", "rar_sha256": "1a2b9b00baf5a6b7f1ea8855cebbe4817e7e6b0766253ac4f705523468582285", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_create_background_job_schedule`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_create_background_job_schedule_agent.py` and in the RCI capsule.

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

Create background job schedule Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on create background job schedule status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-create-background-job-schedule
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
    "comparison_period": {
      "description": "Prior period to chart the trend against.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-create-background-job-schedule-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/cadence of the review the deck is sized for, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_create_background_job_schedule_agent.py` and embedded as the fenced Python below (sha256 1a2b9b00baf5a6b7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_create_background_job_schedule_agent.py` first:

```bash
python3 ppt_exec_create_background_job_schedule_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_create_background_job_schedule_agent.py   # or on stdin
python3 ppt_exec_create_background_job_schedule_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create background job schedule Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on create background job schedule status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-create-background-job-schedule
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_create_background_job_schedule',
    "version": '3.0.3',
    "display_name": 'Create background job schedule Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on create background job schedule status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-create-background-job-schedule',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-create-background-job-schedule',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4be59d2fa8815e93',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/create-background-job-schedule'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-create-background-job-schedule', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to chart the trend against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-create-background-job-schedule-2026-05-24.pptx.', 'review_length': 'Length/cadence of the review the deck is sized for, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for create background job schedule reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on create background job schedule for a 15-minute monthly review. Produce 'ppt-exec-create-background-job-schedule-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads create background job schedule data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on create background job schedule status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': 'Make an exec PowerPoint on create background job schedule for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-create-background-job-schedule-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/cadence of the review the deck is sized for, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to chart the trend against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready deck on create background job schedule status for a short periodic review, sourced from D365 ERP without modifying data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecCreateBackgroundJobSchedule(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecCreateBackgroundJobSchedule'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to chart the trend against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-create-background-job-schedule-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/cadence of the review the deck is sized for, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecCreateBackgroundJobSchedule().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
