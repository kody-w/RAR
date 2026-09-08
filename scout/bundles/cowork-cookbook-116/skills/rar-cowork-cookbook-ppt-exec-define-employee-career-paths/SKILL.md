---
name: "rar-cowork-cookbook-ppt-exec-define-employee-career-paths"
description: "Builds a read-only executive PowerPoint deck on employee career paths from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_employee_career_paths", "rar_sha256": "35b01b0bb3ba0197c9cd84857ac26e8c56f380d136d5f068e7c82fe04e7c05cb", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_employee_career_paths`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_employee_career_paths_agent.py` and in the RCI capsule.

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

Define employee career paths Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on employee career paths from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-employee-career-paths
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
      "description": "Dynamics 365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-define-employee-career-paths-2026-05-24.pptx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_employee_career_paths_agent.py` and embedded as the fenced Python below (sha256 35b01b0bb3ba0197…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_employee_career_paths_agent.py` first:

```bash
python3 ppt_exec_define_employee_career_paths_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_employee_career_paths_agent.py   # or on stdin
python3 ppt_exec_define_employee_career_paths_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define employee career paths Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on employee career paths from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-employee-career-paths
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_employee_career_paths',
    "version": '3.0.3',
    "display_name": 'Define employee career paths Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on employee career paths from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-define-employee-career-paths',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-employee-career-paths',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b46b929ac2cb951d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/define-employee-career-paths'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/ppt-exec-define-employee-career-paths', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-define-employee-career-paths-2026-05-24.pptx.', 'reporting_period': 'Current period and prior period used for the trend comparison.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for define employee career paths reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on define employee career paths for a 15-minute monthly review. Produce 'ppt-exec-define-employee-career-paths-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define employee career paths data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on employee career paths from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes.', 'example_request': 'Build an executive deck on employee career paths from D365 USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-define-employee-career-paths-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Current period and prior period used for the trend comparison.', 'name': 'reporting_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready career-paths deck from D365 ERP data for a monthly or periodic review, without modifying any source data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDefineEmployeeCareerPaths(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineEmployeeCareerPaths'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-define-employee-career-paths-2026-05-24.pptx.', 'type': 'string'}, 'reporting_period': {'description': 'Current period and prior period used for the trend comparison.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}},
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
    print(PptExecDefineEmployeeCareerPaths().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
