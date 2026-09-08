---
name: "rar-cowork-cookbook-ppt-exec-define-service-scheduling-approach"
description: "Builds a read-only executive PowerPoint deck on service scheduling approach from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_service_scheduling_approach", "rar_sha256": "65255f4839196565abd05d978ac15dd955fdc1cc83d970061dcc7044fc8d5192", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_service_scheduling_approach`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_service_scheduling_approach_agent.py` and in the RCI capsule.

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

Define service scheduling approach Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on service scheduling approach from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-service-scheduling-approach
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
      "description": "Prior period to trend the KPIs against.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to pull data from (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-define-service-scheduling-approach-2026-05-24.pptx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_service_scheduling_approach_agent.py` and embedded as the fenced Python below (sha256 65255f4839196565…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_service_scheduling_approach_agent.py` first:

```bash
python3 ppt_exec_define_service_scheduling_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_service_scheduling_approach_agent.py   # or on stdin
python3 ppt_exec_define_service_scheduling_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define service scheduling approach Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on service scheduling approach from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-service-scheduling-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_service_scheduling_approach',
    "version": '3.0.3',
    "display_name": 'Define service scheduling approach Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on service scheduling approach from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-define-service-scheduling-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-service-scheduling-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aabce3ca8d823403',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/define-service-scheduling-approach'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/ppt-exec-define-service-scheduling-approach', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to trend the KPIs against.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to pull data from (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-define-service-scheduling-approach-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for define service scheduling approach reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on define service scheduling approach for a 15-minute monthly review. Produce 'ppt-exec-define-service-scheduling-approach-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define service scheduling approach data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on service scheduling approach from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on our service scheduling approach for USMF for the 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to pull data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-define-service-scheduling-approach-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to trend the KPIs against.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX on service scheduling status for a short monthly review, sourced from D365 ERP data without modifying it.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDefineServiceSchedulingApproach(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineServiceSchedulingApproach'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to trend the KPIs against.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-define-service-scheduling-approach-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecDefineServiceSchedulingApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
