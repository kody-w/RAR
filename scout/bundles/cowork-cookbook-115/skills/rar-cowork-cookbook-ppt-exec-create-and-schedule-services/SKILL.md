---
name: "rar-cowork-cookbook-ppt-exec-create-and-schedule-services"
description: "Builds a read-only executive PowerPoint deck on create-and-schedule-services status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_create_and_schedule_services", "rar_sha256": "1b1e7095ea9a4b951ca7760070cb0ede2d9a4cc8b62bed08dea4f08eb8a9e730", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
