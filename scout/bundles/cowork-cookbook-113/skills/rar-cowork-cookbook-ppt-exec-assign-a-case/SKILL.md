---
name: "rar-cowork-cookbook-ppt-exec-assign-a-case"
description: "Builds a read-only executive PowerPoint deck on assign-a-case status from Dynamics 365 ERP data, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_assign_a_case", "rar_sha256": "88c7240b220f6864ac8426c22b3d57d7021a06e5f2184042b8e5b0e8836073d3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
