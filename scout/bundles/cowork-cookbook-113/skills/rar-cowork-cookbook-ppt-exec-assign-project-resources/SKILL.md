---
name: "rar-cowork-cookbook-ppt-exec-assign-project-resources"
description: "Builds a read-only executive PowerPoint deck on assign project resources status from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_assign_project_resources", "rar_sha256": "6e18f8b17233fbc57f3ce012e012aef5cbe0df696ee06dad1ff22c7acb66593a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_assign_project_resources`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_assign_project_resources_agent.py` and in the RCI capsule.

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

Assign project resources Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on assign project resources status from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-assign-project-resources
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
      "description": "Prior period to trend against for the trend chart.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Target .pptx filename, e.g. ppt-exec-assign-project-resources-2026-05-24.pptx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_assign_project_resources_agent.py` and embedded as the fenced Python below (sha256 6e18f8b17233fbc5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_assign_project_resources_agent.py` first:

```bash
python3 ppt_exec_assign_project_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_assign_project_resources_agent.py   # or on stdin
python3 ppt_exec_assign_project_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Assign project resources Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on assign project resources status from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-assign-project-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_assign_project_resources',
    "version": '3.0.3',
    "display_name": 'Assign project resources Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on assign project resources status from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-assign-project-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-assign-project-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '73c3138fec3caf39',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/assign-project-resources'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/ppt-exec-assign-project-resources', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to trend against for the trend chart.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Target .pptx filename, e.g. ppt-exec-assign-project-resources-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for assign project resources reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on assign project resources for a 15-minute monthly review. Produce 'ppt-exec-assign-project-resources-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads assign project resources data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on assign project resources status from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Make an exec PowerPoint on assign project resources for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target .pptx filename, e.g. ppt-exec-assign-project-resources-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to trend against for the trend chart.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX on assign project resources for a short monthly review, sourced from D365 ERP without modifying data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecAssignProjectResources(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecAssignProjectResources'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to trend against for the trend chart.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target .pptx filename, e.g. ppt-exec-assign-project-resources-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecAssignProjectResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
