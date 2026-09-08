---
name: "rar-cowork-cookbook-ppt-exec-assign-a-case"
description: "Builds a read-only executive PowerPoint deck on assign-a-case status from Dynamics 365 ERP data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_assign_a_case", "rar_sha256": "88c7240b220f6864ac8426c22b3d57d7021a06e5f2184042b8e5b0e8836073d3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_assign_a_case`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_assign_a_case_agent.py` and in the RCI capsule.

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

Assign a case Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on assign-a-case status from Dynamics 365 ERP data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-assign-a-case
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
      "description": "Prior period to compare against for the trend chart.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to pull data from (e.g. USMF).",
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
      "description": "Target file name, e.g. ppt-exec-assign-a-case-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the review the deck must fit, e.g. 15-minute monthly review.",
      "type": "string"
    },
    "topic": {
      "description": "Subject of the deck, e.g. 'assign a case' status.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_assign_a_case_agent.py` and embedded as the fenced Python below (sha256 88c7240b220f6864…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_assign_a_case_agent.py` first:

```bash
python3 ppt_exec_assign_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_assign_a_case_agent.py   # or on stdin
python3 ppt_exec_assign_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Assign a case Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on assign-a-case status from Dynamics 365 ERP data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-assign-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_assign_a_case',
    "version": '3.0.3',
    "display_name": 'Assign a case Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on assign-a-case status from Dynamics 365 ERP data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-assign-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-assign-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '51fa69a126bdc492',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/intake-cases/assign-a-case'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/ppt-exec-assign-a-case', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare against for the trend chart.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'output_filename': 'Target file name, e.g. ppt-exec-assign-a-case-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'topic': "Subject of the deck, e.g. 'assign a case' status."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for assign a case reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on assign a case for a 15-minute monthly review. Produce 'ppt-exec-assign-a-case-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads assign a case data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on assign-a-case status from Dynamics 365 ERP data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on assign-a-case status for USMF for our 15-minute monthly review, with speaker notes.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': "Subject of the deck, e.g. 'assign a case' status.", 'name': 'topic'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Target file name, e.g. ppt-exec-assign-a-case-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Prior period to compare against for the trend chart.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready .pptx on assign-a-case status for a short monthly review, sourced from Dynamics 365 F&SCM via the Cowork ERP plugin.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecAssignACase(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecAssignACase'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare against for the trend chart.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Target file name, e.g. ppt-exec-assign-a-case-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}, 'topic': {'description': "Subject of the deck, e.g. 'assign a case' status.", 'type': 'string'}},
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
    print(PptExecAssignACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
