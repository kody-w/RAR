---
name: "rar-cowork-cookbook-ppt-exec-create-background-job-schedule"
description: "Builds a read-only executive PowerPoint deck on create background job schedule status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_create_background_job_schedule", "rar_sha256": "1a2b9b00baf5a6b7f1ea8855cebbe4817e7e6b0766253ac4f705523468582285", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adObWLLmX9G8N2Kq6mK/7Is80RGD2IQQAoEkEOUOFzuIfZNANf3f5yDJdlW3+073xHwaOWwhOCf3fDLTh9/f3KFPqvbt05sZuuVCcvM8TcJ24ZbBgqtuVZuBryrzwN+FX5V9m3pDX7Xd24e3IOz8Nq37tCrB9tWQ5kG3cBdt6AYfqzKfFuEY+kOfXsOFXt3CVq/Ssl8EoZ8tqnLhg3V9uPBcP4vbagDsLpW36PwkDIY8XHS92w/dImqrYsFPpVukfrfAKXIh/neTUxeB27uLqAJyLmLAoFzkYezmi7Ds0376sLilfbJQdPnDom/DMviwSLtuCLsPC9efxe0e6rl1DZ6l46LLU6DLos4Bw64O3QzoX1Z92L0DLcPRLeo87N4+/frXD28puH779Pubn7sduPWm170AtOQeyqy+6bKpPPOlCSCRu2UM1tYTsHQJftdhC0QvwK0gjBavXz93YR59WPznf2Y3t427Xz59Lhevz+e3+Y8xlIs+CRd95XZ9GCx8t3a9NAf6vi/Y/OZOHTB9P7SzdsB8bVrG78+d3ylV9eIv87Ofn0ze47D/+fNbBURwZ7t8fvtlAWz6+a0d5uv3mUr98y/v+ey+n3/5TqcbvEvo9zMxIPX7l9fvF1mw8PvSNFp8MXWBe/FqQz+tQ0D8D/rNn6foL3Ivk3x5Lv65qj8sfkx51ucvQN5nKHqA7o/JAhuAnW/vFxCCP794tBWIG7f0w59/+WdkgQv9LE+7/l+i++uTcALiH1jrZZJfPjzc99cF9NLtG81/zrYGAfPvaAKWf2X3zVD/jPbDs39HOk9LEP5ffflDcj/aAP1l8es/1e2/2vBhEX1+48McJG7renn4afH7I0R+/Sn4fvOnv/4NkP4/kjGrofUfFL4UbplGYdd/+fLrT93j9k9//fWnoQZRHLrFl6HNf0TzR3Z98PmTBV+rfv7zXsD/WGZldSsX33Jo8XtV/7f2b++Lkwtg5fv97tPij5k4f6DFrMRXpk8T/CEbOyDrH+z4y9vfAP6UQJvhCWIAP/7jPxZq6rdVV0X9wvSroV8AB/dpEc7CH5K0A8j3QI02BHbtUmDY1zoQ/7OHZ4mraPHb//QfYP/Rf4E9XNf9lxnAvzyB+st3oP4CgPrLV6D+7X1xAOSrNo3TEiCwwer659KNARLPrOs27ML2CuDKm/rwI8jqj/PFIi0Xv/2LHL48iL3X028P1E6fKGhw8oyAHVjwPutqJaAIPDXzQR17lp5wkVc+ECpK8xn8gSxVDqpRP9uly9I8XwQpwBhQz6YHbWC7TzOx3377zXO75HP5hGx88Sx0HQwWfBNn8fEj0C7K0zjpP5ehn1SLn37/20+L/7X4r3Y9iM88dFBAXp4BEm5MbbcAmTYUYBlwGnAzgJGHZ37/28vGgEwJKhPwYxql4XMziNQsDL4a3FyzHzGSWnghMDQwclFXbQ/qwCLt3xdytPgmL2A6P5orRVJ1c1GeS2FY+hOg6gJ1vlkS1MFFB8Kxi0BZHbrwwfU3r3UfIhYg5d3+t4XK6aAuVTn4ZxbzsQhsrsoUmP9bODzvAyLtT91i9ZXE+2I3x+aidlu3Tlr3xSNyn36Za/xrOyDuLsrw9rmcy3A4m+qRKE/zgEXAMv7LpR9nn4OOpQCoEHRfeT/WuHP1PDyqaPu57F5J4LazK3xQFADTeEiDuTT8j1dIdUk15MHDfkDSmdLLC8HLK48Y5P7rlkb4UTvEz+3Q5wFDUGLx/2ULNRuGlSRDkNiDwC+E3cE4Px02t5OzY58dKGD6kOaRnN97m6/49RXGP5d5CqKvnf7Hc+XDza81T2gcWuAVgzUe9EGMAUlmuo8UmEO6befkcT+XX+sFUGnxAEdgUoAXIJ/mMP7KcH76VdIEgML8+3vv8AiZNpiNAcJ8UQ9eDkIwCsNg9gqQanblV/+CfAjnlL4lqZ/8SavZ6iDsAP3ZrylITFBT3r9h+PPpV9H/tPHZIs1bHu0jCIKwfRAAcoSzgLObZl8C8fpn9w70/PQgAtQo6n7W3QN5BDR93gzbsBnSLu1nbz/tGtYAtj/O309N57vhWIPUAcYCCVIPwLqPlJrRpgANEJABxCnIsCItQUMAjPIywoOgW8z4APD31bE+KT5uvxQKH3k4V7KvG2dF5j1zc/AMarec/ggjhx+FCaBXzCsefP8+0r5xm2nPUNoBOAQcvz59dhHvz0bg2WksvtL99A/j0c//3gT1KO3HPwfAp0XS93X3CYaf5fhrNX4HQAY/Ze3myvxxxoWPz/z/+D3/P4L8//g1//9E/qn5p8W/J+KfSLxS5NMCfUfekfnR9hVirw+wCPdxdf5IzE8/l0b4HW0B+6oAMTb7bwKtwLfS+HUJqI9xC/AHLH6Wym6usDdQ1B+1ATjjc/nHmJ9zDpSeMp5jtKv+gAWPHgHE/9N330oYeFT2gHcw95dxOE92jwzpwrdP5ZDnH94AQIb/6kQ316piju5uHgZBHoGerU/Dxy/gKvA47apynmPSKphv/nlW1sHtdvF8OmMN0KTtn8PdjLWg4D2Cehayn+pZquc8N3eADywa+38kqj0u3Pwd1BSAe3n3xwB/FbC5gP8hD5+GBAb0gQIf5ooA4AVIBgw56zbnsNuBpAD58ENZHhXjy7Ni/KNA/Fxr/lhUHt3Bo/GYUe7n8D1+XxxNVfzlh8S/9cH/SNkCTcdMLKg+zfX3wwvJwDeYXT4svo0hQKXXYPiY5MsBzNy/ziPQ7MLHlvkC7AFf3zZ9+58NL3z764/kesDdlznYniHz99LtZhgDMD9b+B0k6/gMTCAv4BkMPrD0Q/V/MY8/YghGfUTIjxjxoPZDY4H2Pg1vX4BIcZ/8o0jbx33Yd4NHwr6Ee256XD5airkrTu8gXYG/XzKi5EcA4HMnXYC4S/LptekHQjykAIUDlN/Zyt/d992I1WOonOUFRu+f/wfy+xtIJHduRl6p9JpKwHKAs8AKwN4wgBzAEPx+ggN49n87r7zIdIkLGmVAB3Uxb+khiOdGpEt5dISGLsOQpB96XkgwKB3SIeUhNEVhJO76REQjJInhBMWQDIYxJKD3RJovc6+ZzqLNcgGLfAS5HH5/DG4FL52eOswG+zYezbq/VPv9zaMIsHJNdDL7/HDwEvUggvbG3oZthBmds6i4qa0EgxyD0SZdDkAgPRLv3bbt2RRjL0hqjMpSVPObqcCncb9ZpjyZlJQJ+5hDiN7RlpDSW7Gk1ZAZ6UOOHw3+1BH0hZeJaWOred4rsCUFG2EfpZEnH7Eeqio5PWp6UcGcrOtTMhb51ND8fkOgN1+BlxysdRE8HvT0zir9huUMeVMLmU9XUWWttvs4PZ9gBjtTOV4ko1lv+2FDiEzfU9J1HE+hPp6vUWlgS6Faq/UpzqXI8c7E7mxIVS9T61RXR1zABYdMriNM+dfNtNVPq1E1lAStIkMweUbPxqQ7XyCnTuKtfquC5Lw25Qq7VUfqdBU5J93sfNf2b6Hu9T221K4lji0H41xuRwiCnPWJvgeKJpT+mVom3H06OJvEhM45ThguxCun6c6lNLzyLl0uNp0k4iyV+pty4+mRcBAnUVPcII4LsRxDh+tMz8Gg85UdL50gZrfl7bTF1f29lfee2q5OnZeYQ+aPoxCdFGeUEyGH45NFIgW6PmNWJFEZ3vNX13FYi99iYnDINmjOxsklhjDZSTzyrBjWft+xB9dZo1IajkKXK7ZEctFSpXgko7FR7JEiPBNMkPMbaVkHmtM52xK9bLu14ipik1Q7Q9xf/ZrQTsl+XFV1ct8T2boIE3/gTrxTSsMKLiAHoRRb3Y93I1KyaXlSDerClqLRk01pUsAx9WaEjGu+j46QXQrixiSlbFV55K5WaT7kMExNV9B5M5BT6yRrbdOWCKyP2t6S6sBYqVRSobHeFHB/NPZnLM5u9To2mCN8Jw3ZdeLBYo4Ec6dWprrdo5veRLmed5H4EHZFb6NHUtDi9sJNCMbZ59bAT6azpThaPhIEAaU1X9kGk+dZjscGroyjvkwDxcm2W0KMIEGK01DBzTzbpXdis9tdEBDgbSSRmGaQzRDeC5/ZRt5VWzp6f+e5xsEK93DL2LrzjJq2LgdoXSHLrVEsD7smBDkT3zDllFwLeVjTsY6zRxfqJieHCRW5NCBayBFK/fVKok8Ww4ubTSX12YSqaW9iAtMFMRdvEfSuT6AHthXmfmZvBTHpWbVDkRUVsSp/zjf7yV1l1EBay+zKuVtUKHkCyghHGyXH4w6SyF52speuxW693+46/nSkWM1ckaQF0WWZNl7sIpzgZz1qaaWeOCp3Uzz1fiOKIDWytZU2Kt8yI1UXFpRKQajsD3foIjS4ne7NIGwcLaktLTddE4r5CVa2jL6vUckfwhOEjw2uXCrF3PXDMryqtXJ07kfs0IVMSVo2hWskmidLPb5fKplb0ocpMORpfyOy8zYedp0ioSsQwYyjQSp52ZTUnaI8VeVVqr6r3WGLlM4kZWwWH6UmXXXwlpaqHZJ0qy0iC6LuhPntbJR31YYCh+8oq9jtxijRE9eMKc1KiEHlFdoRLxKscOd7UgRKmF7gPWeEp8BZ3Qj/KG90c8ncUAe2bnUQxt4JP3ToDlKQqYGGUAl4mwwFVd4yeHDT6eSSF17sXZj0ZklRx195zcTGrZWMupQJFHWXeO12K/2tDLPDPi/EzOXoTahmTTyNPumSqKU7qCoxPrZKuMSMCLhArUbIls7g0GeLFVB7mxIRxUwx7C179d4xcVqUMR/xvp1H2zEQzc4NkED1MHscUA+/76alRpsxd9NYH92UIlnJVDZxV1MVAGiLkVevomylONVRM8cywzud9U/Xg8wO6kSfp14yQp263ABs1rw/qUv2yhKZkORSngWYevCp/UoasxaloOCIhO5OLTeOSEmRoPZHjNv0GJPgcsAiYWAogZLDLta74ka2UGGTGUm2GzeOfNrtJ96cNJpebc7BihQm7cZdxSMFm2a6J+2NPTjbluV2CnLk8xvhKegyXVpbpdl5q6vniteg309JkE1mfb6b1anAaYTRynwZZMotozLkdihWW3Ip5dYlYwrV3Cy7JXfBClMQk1NH4jjWxzhu83wPgDn2UPIkL+FCv7mcBcPXNjnD9lrND65xJES0vU9nhrBWEsd7bLa6qchWsnIRWjXDqREjQ+VF6ECcDXR1cBwmHDbNFmUuuurJvaCd2bIzyHi8pcihyVzjdDvc1v7xthmEsarMMnHY7AhKSHs8W5K7WarTlru5/pSxa4dQRrCyqmid6rO+bcdYdLQgtI6+dPBuTh7rJN0fmRN7Qs02OmAWVLkiNA6UqjRcJR+TpXAEGREZDSXs8Mn2ZPWYqbLb5Ry10gzrYkzHIDKOjln7d70lzoWJ8eT+LoT7nI+L4MCVmlGIJ1QfWSTbD9uphmJMivu9ZDQec8iycDpfiL5wbM3K3QiyqHGTBZfSrFx8aODTlAa3Y+MuCcE6UyXc3IybKuujVcXKJSxOHHRmsp6jWLvrsbMsDO2wL3JoHZLZoZza7SgU9km+xyInJfKJj5mLapyvhmlusd3yHNYrJB5SK0mEiWw1hlM3wl1tOtf0tEhjA0YNjk3rTtf+lgl71YlWsWcJjeqTBxYlbUzInZUZhma2aU4es1QHV9Dhq4WILGYwdx/r82gimnt3OiaHDLU1yfI2DSYZx8ZubxbLVuUudJGaPyI3BEkyw+vVbGJOd2ionOiw26scJVxO/qYIL+1mvVwF5WA6bmoVm41hbNHYBpatRI9jIFZvuJVUD1wRSELaV0nuiPwlTOmlge78ohKnGKc7njxvVXfNpILqEFN5MXeIUJxTahI2ztJHRWGYivyuWp0UFg7kndsyLjxtL+8VomstuJfRg+F5++jkq+d8O90RUrv4TKAGo6NXmmn6pz7odYclVuikELvCc7as2Gc383gYT7IQB0ctPoyh2BSK1Tc3WzD3kKVoEpsitTQ5HTNQ7OCyrpfG97OAbc53t7khRzI/HPZh38i0rkFVZlOJeizKUoNl2VrLnpZrabLl5QZNT/FVM8/uBvRoyVFQ1xvM3zU8iZN9xp6ON223vlMlh5Gogkr1yhM2B7ZLleZklUtThhLdTtTW6pWCt/0d5sERHvqQaln8DpdIJ98cLO/q6gfaWqFlpR2nSJXz07TOoWkfbdbCUdQGMPDcSDhSfCFa3Tea5Ca1KWyV/GBXYlH7sZypHir0IWaOPe+YLr5rnDj3R67ayOuuEDltvzqKg9yRZdCQUS5LuHaoxPXIuSCKk839fFc31vW8zBli8nPxRKLH/NwjvHlqVmm8H1urrgpbXk8OpMsIVrGVw3a8kLEYfETZ4gBlyuG8ztq2SnpM2S4xOXWdw3Y0k8wtWFu51CYddEfdoZbhRcZ9S2HDyUH2iZkymwoE2Sjg23R7B3EVxyDRJWMPDZIM0vTuIoivr0sEjaIVAQ3Jth5cN9FEvuGIpbetsNAXcVgqC/PuDn7Z3S+HJSje66HpNFjBHXpibH5Ed5konLRLQpcFlpQinR0rodM3jeUSPXU2qIFxINQeo2wNMqlLGpWTzwFumO65iM/p6mZX/LphNXWCsNhNJBjMcamvtKmh3KTL6ijs1ylx7bPk6EmIP9r7FgtkVR7MjI/kTZLlqLO3EymAl6t6uoJ6L97O+Co/YbejoUzCgThoFrOajh6oBy0TBVxZoAW1CwKnxyaShy/SSO8352kIkEG441TDnY55KERaqy3tq12ez13rZWfduPPGVZetfiVcVtRuPHobWd4ER1JVT+GlSmlBVG67cE0lYXsSdgJNCwlnotHBzDz7UHfnen+y+I5xLivXG/JLttwv+/jG7CzCaze7gw9rPW+oUJGloEnKKRJp7c6BTqzZeOpqN+zF9XnYg4QvcKqOjFWYDRtLuDQHVFPWRe6uqCHop3tNYESt2WmR4U2Irwwj3x16bufLZshMe7YSEdyikGR0iMux3+t3U/GRnXk93zOmFrCKlLQ1q8HadrjhYRGOdlpfWO7Kq82SBpXRposGpw4eaLKsymbhAxtwo5Upw6a7Z+hUbo/WuIw5yAhvVK0RKwLHsDupu3a2LreyLK31W3eekG3kbNxhg225+DCU6AmMaO2+coOG2qp8aG+sA8jdoGIntFnTIP85TshXgWKUuU1p5eV8OKkNLyOobZ9OKxoK66uy2p2mAvEUGTIORiFdVeV4PMO7LkBUk009aM85lKYbozsmWJ1hCTaucf2kCWq6rByj9mHbq+BE2eyZXN1hcE1AQTlxmbveGodiSy9pUh3z/IAfmWV7i3W2rGpKP19dojS28Woyu9GluOFkDa6JqMXuiJgYXDqKTYd0e9Bu10kMRrZTz0hcXeIK9BLMirLl4koKyeZ4lLHzIbvsOpB8fSSnFjbcL6V7VenT1jnfBJ1QuhNiT3AgE9tR3jaodvDs/XCksHS7zAzBJ/dLZIMgFXGwNaq/qHjIMO01QqPuMt2t5HrC96ASlKy/Qgx1j+3Mfr/tYC+s6HtHHUzL9u41HY7WDs/M+/YuMaV3TQiR14mmPSHm5Wqm1ymDnRtJNffQWNJ4QvqBGGLby5Hmxv6C2ydfXsr0aodRW6qVGltkTzSzcZepQ6tQHIlOPnjZQFEMot/69QSaRMq2bu3SFqkVnZd0R9ChVBypJeSVfIO5YrOKTAOermiasaOpOUh+UOotNu5hZBRQg2YJa7zfWGM6SUWE5ZfqjEtX6krpq50a3ttGhEzmeNoOvq2HxKXFeP6ahsNpM6GI7ynUsi257BYdDMy6rQpZsXb7UFt5xy1MkTB845njURSVpEAh2IEJlFi1EpZ3Llymx8Jp8fOqTy++7WZBDvvpCMqxrjk3ComDe8Vw0VGF6UPjBwBlzYp3j7vLVrCPtygOzfNeFccxpWt1xHYWc+XyU0biqDaG/iY34jDYov2YarWr7Ex/wrfhWSYuyl0sjCRNSh4WUy+e6NDROJH0MwIMHqDr0e/XIDoF2nBOeSaUXb1bb9u6U63zbbmRMtXxY66s2rvhwIhn6H7AccHo3dpt3WJLpaiC7f6qBVV0b06QfcXOZzotoFW+AvO8yAx8jTIUody7+3USCrYbMLRsBGOPbPPkRDvNqW0gW7zm/O4qymLeU7Fv3O4djoQd00WdjPKrksxOHRQkUcprIkPu83sCED4zzGrarFyeZXqd2suYwstgokXvhUgS9Llqp8Lv8YBlOAyUJQ7yDZnqFJt3OSw+8GO3HrOS0JzGGJX1hWZ35WGkJmCUOqPNrLxSfajzMWLqduAj6/Sy3YKhRLRJLiODTCAZUeNpqUHsi3wLbhpPDENz4OHD2W9uWIaj9OF+J9FSzzGasXeOf78ekB1GWnLc4kzreHR6LsKsEzPs0u6InA4ttNjDoAsK1yC69ud+6a8wzLG3tsU7V1Lh1hroy8u4RIKYFkcDTYJVQCxtCOlsPl8v97vqeuG809i0W5pmy93O2TUgjd1KvLhDvOsG1NXalmrPR+l8dnNaVQ3I7/cUIwF0Z1Yc17hKgmsS5Esrh4WHFDowG+K0EpzLLcQ1tYEakZbYSG6Ok+asXTLm73wP5YjNtxTe6ogfoETv0hQ6lGIABSsr0O58tIXgXh3IPQEd9oUT0jRKkSMB965J3Pzl1T6i9DIuS6/AlqcJwkcNB/0lsvURSeR4zK4RysEoe705TH19isx9SicBsa871mFAz0BflxtCXaLtKRrko3tqL/a1zhRyE1JUtiGQNVUjJbkHoalv0QnG+GhTrHJBau5qQsX5/tqu/Yt3yTZGcYR2rj7YB02BaYq5se35JFprctMZaWtGHDTx/tobJK4RmL0/JWeC0qc+afjNOsz4FYrvpzQ3rNHd1lu7FOJoVVrWxORwmmFr8zBxBM4dnbZTb6rS9y2SKAfoGNAi3CvhwKj4flWtc1wbTWyVratttkNOkCIUbgxLdOVfVKaDTGV9I5YV3DqXKG3dflKYiYuXFtZ7Q3Y1w74OQdYhqNzcrhpxO7YU5fW1lZVq7ykY7lli2cIchplF5rTroz6NdydndgVat8fdphwHaXkhtZVWYvm9LFuJR8FwLS2BUsq2gSbmGm+kc2DuJ3+N9OSa7hM9ogXexKbOMuH2sBK5PK/CjOBHmxBFoyUTypATkIPmdNAEMrQi2T2Nw45cr+liXDb4DjRNWBmifFHoNJsuW9KHR8vbQ2QwMmB2duBDXZx4F+Hliy5IVYnYg8kextjZaUTrXWAA8VlrW/Z+zdCGwBzbI59fcfvSAVeRpzDC6NDrTx1xjyzxINnj8mjh9tXXaP/Y3yn8vB49KgsgxzA01OxBFcV5djJk/BZJSeD5FLzb9bd0qWwx/c462/K69/tWxyASABy+kbP+wGri5Ey79rqTyYrAUCzQfeXKS2tzHQviMJyX7Ea8lBmbuj20x7kbq+FOw2Bc5PWb/uBjDGJesyK1oK1WTjuScO9tf0XZa5PUiu6cm4QSdZ9HTz0GbScFKrxUgUIiqnbHE4nvRkLDKQVGN5qM2TC1jczacCJYindXXSkrXJdTL7iJ6oBfjm2IpymZKhVV11uXMpe87wBpbel8WsEHgEobvN0pvaPAK6prtSqACKztsLtlE4wMk6XUn7E1rW0wbQlfyVDCTlf1qvuoekdbkOG0HRGgAUJtBj9yNqZYGzZlh/qkE3dvdRJY4YAeDVLwELNRDaQgWiAGgSLVVrMFf0k5zK5SMAFUHOXSECHKQmAQxypcvQ7HHYkY1BLunE6C1g2c47BzQR2Kk6DBinzK8HDkcvNPEhUHW16i7viWUNx9aISCtRzlyqxTLFnvc0EHkUkGPh0R0BJaHW67aUXQ6VKPTGTlB2p1W96nZgfDyT2QozVvafhKrpuWiiTHD/nopl/YXLEURGVZ9i9/efvw9v2c7+3ffWFtPvz5f3bO9Dwu+vreyeMcM3SDTw9en/5tyf764a3101mux8lalw/x63Dq787VPv6Lp5Qzken5RtjXA+rnsXrvxvO7029pGQxd305fuip/vIMCdnhDN79p2c0v4/rg+0/Hsi+VwKUbPF8iCdsvffXlebA4M0zL+f2SMEi//4xfZ44f3oLXG09fcIr8Erb1rPLrFQagKf6OvONvf/vfY+zKaP8uAAA= -->
