---
name: "rar-cowork-cookbook-ppt-exec-define-service-scheduling-approach"
description: "Builds a read-only executive PowerPoint deck on service scheduling approach from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_service_scheduling_approach", "rar_sha256": "65255f4839196565abd05d978ac15dd955fdc1cc83d970061dcc7044fc8d5192", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
