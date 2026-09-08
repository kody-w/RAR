---
name: "rar-cowork-cookbook-ppt-exec-create-and-schedule-services"
description: "Builds a read-only executive PowerPoint deck on create-and-schedule-services status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_create_and_schedule_services", "rar_sha256": "1b1e7095ea9a4b951ca7760070cb0ede2d9a4cc8b62bed08dea4f08eb8a9e730", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_create_and_schedule_services`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_create_and_schedule_services_agent.py` and in the RCI capsule.

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

Create and schedule services Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on create-and-schedule-services status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-create-and-schedule-services
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-create-and-schedule-services-2026-05-24.pptx.",
      "type": "string"
    },
    "reporting_period": {
      "description": "Current period and prior period used for the trend comparison.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the review the deck must fit, e.g. 15-minute monthly review.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_create_and_schedule_services_agent.py` and embedded as the fenced Python below (sha256 1b1e7095ea9a4b95…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_create_and_schedule_services_agent.py` first:

```bash
python3 ppt_exec_create_and_schedule_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_create_and_schedule_services_agent.py   # or on stdin
python3 ppt_exec_create_and_schedule_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create and schedule services Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on create-and-schedule-services status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-create-and-schedule-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_create_and_schedule_services',
    "version": '3.0.3',
    "display_name": 'Create and schedule services Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on create-and-schedule-services status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-create-and-schedule-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-create-and-schedule-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e1fe1217aa05bf8f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/create-and-schedule-services'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/ppt-exec-create-and-schedule-services', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-create-and-schedule-services-2026-05-24.pptx.', 'reporting_period': 'Current period and prior period used for the trend comparison.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for create and schedule services reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on create and schedule services for a 15-minute monthly review. Produce 'ppt-exec-create-and-schedule-services-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads create and schedule services data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on create-and-schedule-services status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': 'Build the exec PowerPoint deck on create and schedule services for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-create-and-schedule-services-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Current period and prior period used for the trend comparison.', 'name': 'reporting_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready .pptx summarizing create-and-schedule-services status from D365 ERP data for a short monthly review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecCreateAndScheduleServices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecCreateAndScheduleServices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-create-and-schedule-services-2026-05-24.pptx.', 'type': 'string'}, 'reporting_period': {'description': 'Current period and prior period used for the trend comparison.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecCreateAndScheduleServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
