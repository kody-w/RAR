---
name: "rar-cowork-cookbook-ppt-exec-define-employee-career-paths"
description: "Builds a read-only executive PowerPoint deck on employee career paths from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_employee_career_paths", "rar_sha256": "35b01b0bb3ba0197c9cd84857ac26e8c56f380d136d5f068e7c82fe04e7c05cb", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebObWLLnV9HcFzFV9bANErsnOmIQCMS+SIBQucPFKpDYxCagpr/7HKRrV1V39ZvuiflrdK8tlnNyz19mXvj1ze+7tGrePr8dYr9cCX6eZ2ncrPwyWrHVo2pu4Ku6BeDfKqzKrsmCvqua9u3DWxS3YZPVXVaVYPu2z/KoXfmrJvajj1WZT6t4jMO+y4Z4ZVSPuDGqrOxWURzeVlW5ios6r6Y4XoV+EwOGtd+l7SppqmLFTaVfZGG7Qgl8xf/3A6uuIr/zV0kF5FpdAMFylccXP1/FZZd104fVI+vSFTjM4w8r2RA/rLomLqMPQJboY5L7lw8rP1zkbJ96+XUN7mbjqs0zoMSqzvt21daxfwNylFUXt5+AevHoAxHj9u3zz3/98JaB47fPv76Fud+CS29G3e2AelycZGW8e9eFfapiLJoAArlfXsDKegIGLsF5HTdAgwJciuJk9X72YxvnyYfVf/7n7eE3l/anz1/K1fvny9vyY/XlqkvjVVf5bRdHwFy1H2Q5UPvTiskf/tQCLbu+WXRbtcA/5eXTa+dvlKp69Zfl3o8vJp8ucffjl7cKiOAvVvny9tMKmPbLW9Mvx58WKvWPP33KF6/9+NNvdNo+uMZhtxADUn/6+n7+ThYs/G1plqy+Howd+86ricOsjgHx3+m3fF6iv5N7N8nX1+Ifq/rD6s8pL/r8Bcj7isAA0P1zssAGYOfbpyuIvB/feTQVCB+/DOMff/pnZMMUxGietd2/RPfnF+EUhD2w1rtJfvrwdN9fV9C7bt9p/nO2NQiYf0cTsPwbu++G+me0n579O9I5iNz2uy//lNyfbYD+svr5n+r2X234sEq+vHFxDvK38YM8/rz69RkiP/8Q/Xbxh7/+DZD+P5I5VH0TPil8LfwyS+K2+/r15x/a5+Uf/vrzD30Nojj2i699k/8ZzT+z65PPHyz4vurHP+4F/O3yVlaPcvU9h1a/VvV/a/72aeX4AFR+u95+Xv0+E5cPtFqU+Mb0ZYLfZWMLZP2dHX96+xtAnxJo078gDODHf/zHSs3CpmqrpFsdwqrvVsDBXVbEi/DHNGtX4HdBjSYGdm0zYNj3dSD+Fw8vElfJ6pf/GT4x/mP4jvFwXXdfF9z+Gj2R7es3mP76gumvT5j+5dPqCIhXTXbJSgDDFmMYX0r/AuB4YVw3cRs3AwCrYOrijyCnPy4Hq6xc/fIv0f/6JPWpnn554nX2QkCLFRf0a/s8/rTo6aagDry0CkHpelWbeJVXIRApyQB0LwWgrXJQgLrFJu0ty/NVlAF8ASVsetIGdvu8EPvll18Cv02/lC+4Rlev2tbCYMF3cVYfPwLdkjy7pN2XMg7TavXDr3/7YfW/Vv/VrifxhYcBSse7V4CE0kHXViDL+gIsAw4DLgYQ8vTKr397tzAgU4KaBHyYJVn82gyi9BZH38x92DMfNzixCmJgZmDioq6aDtSAVdZ9WonJ6ru8gOlya6kSadUudXgpgnEZToCqD9T5bklQAVctCMU2AZW1b+Mn11+Cxn+KWIB097tfViprgJpU5eC/RcznIrC5KjNg/u/B8LoOiDQ/tKvtNxKfVtoSl6DmN36dNv47j8R/+WUp8+/bAXF/VcaPL+VSgOPFVM8keZkHLAKWCd9d+nHxOWhSCoAIUfuN93ONv1TO47OCNl/K9j0BQMQBq4SgIACmlz6LlrLwP95Dqk2rPo+e9gOSLpTevRC9e+UZg6/6/0+amd2f9T/c0v986TfIGlv9/9UzLfZgBMHaCcxxx6122tHyXn5aGsfFn69eE3B/ivXMyd/amW+Q9Q25v5R5BoKumf7Ha+XTu+9rXmjYA1EB9lhP+iC0gCQL3WfkL5HcNEvO+F/KbyUCqLR64iGwJYAJkEZL9H5juNz9JmkKsGA5/61deEZKEy3GANG9qvsgB5GXxHEU+MA7Xbr48JtjQRrESyY/0ixM/6DVYn4QbYD+4tAM5CMoI5++w/br7jfR/7Dx1RUtW54dYw+St3kSAHLEi4CLmxanAvG6V58O9Pz8JALUKOpu0T0A6QM0fV2Mm/jeZ23WLVD5smtcA6z+uHy/NF2uxmMNMgYYC+RF3QPrPjNpAZkC9DxABhCgILGKrAQ9ADDKuxGeBP1iiVYAu+9N6ovi8/K7QvEz/Zbi9W3josiyZ+kHXtHtl9Pv0eP4Z2EC6BXLiiffv4+079wW2guCtgAFAcdvd1+Nw6dX7X81F6tvdD//wyD04783Kz2ruf3HAPi8Sruubj/D8KsCfyvAnwB+wS9Z26UYf1wA4eOrWH78lv8fX/n/8Zn/fyD+0vvz6t8T8A8k3hPk82r9CfmELLeU9wB7/wB7sB+33kdsufultOLfIBawrwoQYYv3JlD9v9fDb0tAUbw0AIbA4ld9bJey+gCV/FkQgCu+lL+P+CXjQL0pL0uEttXvkODZGIDof3nue90Ct8oO8I6WhvISL4PcMz/a+O1z2ef5hzeAk/G/NsAt5alYIrtdJj+QQ6BF67L4efYEirFbDv84B+vPAz//BJAegFLe/j763ovKUlR/lyQvPYF+IeDwYcFtkPsgMIGeC/MlwfwWRCwI1kWfbqoXBV6z3tIdPnH96wvX/1GgP1SG35eAZ+V+NgUAij6s4k+XTyv7oPJ/yuN7e/qPDFzQDyy0ourzUho/vKMN+AYjxYfV9+kAaPY+rz3H67IHo/DPy2SymPq5ZTkAe8DX903f/84QxG9//TO5npD0dQmJl2P/XjptgRoAxYuhP4GEGl/hA+QFPKM+jN81/5dy7eMG2RAfEfzjBnvS+lNTvWwKTpaBNquif5SJ7ZtmqTKv+89QrsFR8+0CiI/oOzQ9y/LS1oBwzFrQ+vw5zyGLH1+BES5d+o8Mled1eJmuga/erfHa8zx8NhhFD9rCJOveDbLGPwJEXzrqAsR6mk/vG/6E/1MAUElAPV5c+lus/Oax6jlYLqICD3evv4P8+gayy1/alPf8ep9MwHIAvB/bpQ+DAQoBhuD8hRfg3v/dzPJOpE190C4DKigeIOsACQI08JE1TYZ0GFEYhZN+uCFiKsSJBKWQaI0SEZ4gBBWTIbVJYgQDBwgeBoDeC3q+Lh1ntgiG02SC0PQmwdYbJALCbLAoogiKCHFyg/h04OMBTvu/23rLyuhd25d2iym/j0+LVd6V/vUtIDCwco+1IvP6sDC9DmCXDCblBJ8Qaswfbl/zfnbrH0UvD+FJGDP90V8LYrLOfNueRCGdpP1Os51Jd83wceTMFLoc6VtJ6JuogFhHjhpFC4J+yyDDbZZuMw5pqFEEra6SF0cmMou543MsIRJhizA/yyfBglpnn5Gyqk6ZQoiqw8cZOmezJbPl7n6ZhpEmYegYPKpqTm2A9DitanXRmqSYtEUKRDiaRAuC9dgcr5GUYBu2PmJEm1+pRIZRnKB2dz6BBNnB7yy8bfnduFe6ERELyzm2Ui8S8tVj9xsV350gSpcgUawjSWd2A3YyHQjqJUpUs0NqPHLsyM6zTF2PmMzbceqwsnKYHFsakIaShFvqHHvP4KgeguNyj6Kwhp7vx5SEY1I7EjjWPYTZd6SLHQun8RBo7dGbHfeRpaf1Db7KMmEVEG+l4flSU5DWbffsejZoil6b2sk+zN2OeVQXQtyVkKJRc6SiVSiEmRfwPoYpSMrEprmBw717JGTHYdyNOJPiSeD34o3gZOrRI0WFx8WAo0Z6N2loNsSTDbMH87YrTDzbSV7FlfhR1plGOKj5TNi7aRQTdzRr1c5rth8Nu2CvfgefOY8aUUu6OcL2hEfSyJ11+h4lRYQHN5Sb8l3he7LqjJol3fdqfKy9m2r6shfZesIqYgW5kp+38/XIwLPX+JqmDFj2sJK1iQ/ySc1Fy+G8kaqP50gpAqSAY/G6sfezeua324Obns+sL0AHdO1YKujyjI0JibzFX5XEuhW78bEfQAONu7Ni6ExQIryQbTvg7NGW0tJ7GNyUHkITvibxCeHYoK3hdhTbUL44nLtZsye/ZZoDomGsS0a521ny8Sor+cGrtUxLOrd27figpnGmJJTtZPcQFQ6ne4LzJyJ3kIHiCR1FbvAugphhc+MelrIjU3UStme48C+Tb5De2kjjoGqvdsJ5SixIF7zJt329rq3ObicMAGCCIWeOPbu3OAEjUtLeVdSPW3qm3LKN4pu3H1MlJQiOfuxjQ6fVw3XmSBErAhLzk2p9upDxpLi7FM5vO/5CoEC7g3Aj2+gh8bFlOffsvI8VnEBt/a7yl0Q07VwaOmwrYVfbkbaeXsRn7bq1Wtg9q/S9AYFMmpFaup3KpxJzZyz2Dh2YW79nFIfibJswdWGLr3ODnufxqD1Uf6vrIF4evBD25fYhaoWzOXfZqNL7gTlXhwBLEr931OZ0FsURr0dN9Sl/FAwZsa6zPWn8QVXE0nRwrnDgMy7It5Yu4/gUn2bz5vBHt5YK3IFcas8FuRhoPTogyBzMGUx1odJOG8FOWVcN9LjWhLO535G7kL/d5R1Tc/TFw7iQRmZOKrFZJxK1mO7Oqd7iJifBFeua0iBp6VbVNygdPyJEJTROQcSdZuBd/vCOF1ndA2i/Dr690fQx2Q21TW0Rts2mpBWUYla2O7hl1KA5sbUhpXTlY4O8v2V3ir/tuFPTJ7t2Y+QDIV/uCDbnBaHDO8s6KSdjH2+5arjq23k8tZiAP4YZlR7dSNOYhBubU5lmVeDxjYlFV5MN19h1y/vesefRh+WI0Fpo/QMpndSb/phHn/fx8QifW1WGI8fpmNTCMTjDBty3oJqKSNu/8OuTcsYSDAOBEj2g29mNvZE7Pth1uJacKxFnbbueg/aUDNGh3w/pEauswW0RTCy3w7UQkUeW1+5xHHpgUy917TOt3wAi3W6FZM69n+wrEdlvrgy51xqBKaUpyUabYjMsszbVdryaUHpFDrzqu9bojeugZoVAYIe5g3C9o2b/rCA3V6oxc3IOJ69Ak0kI07tmnje7+nZX6Npbm/YlM+yjYD4E47Qrb7V9Q0VN8RqjtZ16s2sjs2EkJI8aWpJd04Hv+CTS4dbIr5ap77m0VU6usg7bu+gwAt1RAr5BrvJuc5T0fNbk2A2SEofC4YSTVs0ep2nmjWrXlUjs+NsjNM6W1KGtHV8my2wV9VpGsNOy9Abzoo4XeE5ocPps5BoGQZSn7R+JHIwPmvPWUXHL1VRTYcpVGJ6JzIsLS1BoGIcrbt8Cce3ep0vlbbgs2UKiR2R1e6OMk4ryPgRmWUXtWGy09uU+FsXk0WJ45TIn38a4Tb7bAh6qzDlEbNY8x2a2zRJnXr+6o6ftPEsXivNjtPNw29Z1qe5sHU2V7lioKVL6yWl0z5u1qJ4a/jYpFCRcix3nVcGa2Minwwl3rICTce9m30lDW1+RcQtwZJT9vrpmBQmShtlc7qiJ4VB1SSXFuJ2iqN7eEAIar6IrDvvDcJ3O98uROXubtb5N0Yg7gkiOH3uBR0G+7izRCpNcSbaxtvUvaufZu/3+QUNCZMkpEUHEwAqDMvRazcy5b25yK9k6CTZxhYVU95PtE7Jvcg0CkfABK4j0fvdY30bSbpq2vJdmCCJW0iEkCFYqoV47TWwpZ1PRsNq0tbaHm5w+IM4+nMpd7zW0eqk26RYpykzQzjyrHpO8t73zQS7sjXrupY7Zm9ymvxIIfVTWeIsAvGPHjbg1sdy6Wsrcl3h8aKBLupekXp1lDe0Lg2MYeFPfLdu4AfoSVruUbvAEH+3NiHceWpHj68N4sEuTFJiRiVR8jkKhzDBLwDI5C85BkZ7S7RUnjzdM2IUHXhx2DafW/oBAUs72F3pCNRt4RpIJOVZlyGQDrzcYiJezO3c7EFf5KHgZi2T8WNr9FlfgTSYeJs20OnaAz9FGvATelc5sLcUCLW7c8Xa0R8uQaxcakJJBhzMxXjiENrQkiFpn9mJpx+7ljacQs77m+LbjIU5EDrahxKd6ik5cTfQKKLGZE4w3NEf4ivNOgciZld/ZOWfPDSdthVl9FOxa1xkjR+xKks6bRoot6SJ4IupvuSPf3fYeriHbEBHWm4gzbhbtA0bjniXlg28ICNYJewlG+UMKmcy2ZdP9nSmOD1U/PHaKIXrJdtcg6C5WbzUCSlw47RCv4BpcMdNrQm/rh18FrSAVeRyo+Ma+VwJzFOXLVvIc+7GWQYd/53R0623qyN7cW0zBJAiGSWQ2q25zrKRLY0SsOMUIPSTI9eabuK+0annai47tng3qtpetTHicikYcoz1sbMIdLBXI2mwBwuRWjYnsbN8t9cBq8qT3Lh4WoXHHhxmY34voTYsZJ+1EtF7PdkQqbwsjmuRUzhlMPDju6RCFOXAjG3KH1EtP5MWcHuoxO1agbDUEZk/eCcd7xbG2a7/ZOMYc3t24km3nwpPyVrfJrnIMEqdpRxnK9pTdElPksavpYyLokdURP8hE0pn8zk8ZWdidDzvjeqp4FOqv22pKjlsMKq8kXrh3XKNK6T7sCzM5Wwf3alJyooc2L8JYfOEmKoFmUxfl+9hesm6ujIdbVZTJXGaHwwWKbljQGmH20EeGSuEu27RXw6vgMI3SbHowwjSrdQqYFcS1ZmcRwrVsB8HqVoqzrnQapDF7ojlpnVoTWlXcZQO+jMTJhhA1xFLX4gSfcCgwntQeQ9oyEedrt2UyI3JsxBqt4XCgmXWtWFng27nW5gLSZ4mdoFJ3xTX7YvcX4Cgpl3zF31EgdmBmoJHdOfR6vhqE0xDw1q4RFcPSVJLaa5b42N2HEXL4k9Z0oUclFNKhTUDefFo7yhQTlTJSnRybJOt1FG3Z+4FnybI0kAZtClt31/yk7it8zSNjMCMHcIzy1lCnR2mmqVgMpfha3cn92rQOlMyNzrS+jZjQqgdO3x34E7sXAtvaGrYlG9KVCtWoa7vuVLOb9YkDDcy1vyObdYyAdmAwN/5FR4UibMq413cQ2zNTHgS51scnwbCFe3XO1xVawUMm0+eDVeFKVoJiOfHadF17WECRprkmtdAFGQSbTB/sOdC89Rm/VnYedS/XnBU1G0NSDvxhfSFVkewOazm/CCR0GeVrfhJNhoTtUzT20JoqHsoos7LK0DNaH8110J2J4AYKklA+yp2+Zy5WwU4pP6437KYy1/6FGECzKqWhv84cLprlc9mv5ynnaHx7SLOc5K1gY6KnUMpzSbjPZ4i9npKrQu8JnUkrt1GzBonN9BxGqra5bBUfO8W3G+hVc6iKpbqozxW0z/2BtSGhb9i+bxMO3XBooXHnLQYfRJI9ujdqoMv9zRj6NLEYkwLjq8JQe73HuAcJcrG0SXMgKE01Cv6+uaXxcOGG21Cio+c09/NxpFCYfqhVw2P6OqlduDnhiLF263VL4D7DJJcSW2NlRXnY3tIuW9ffcVcCd2PyWF1LLtvUZ0wywyCL/aqLs7u7MUJFSU3HQ9YnwnQ22dnf0fIBG8ythuyQPmCuiuBXtsT7m+NJKspyEMZYghDBGi9sgulV0zb5jFyDQUsTITvd+7s2u8X0SNrcuzZ3YZMeiBplLf5kbuoHPMzVPJQKByk30AyTTe1xlXTtgY11vDnKd/3ClSE/2FuLiFHckLbnAlaqTsh8xSvTMhm19BH6+Rx2WuXToFiJV7weICIE46jhTnCgjElU+OvjRJG7sRl6g8Vswrtv/RQxnBiqY4Qr+yxv1njZXglGdXqfN9J1k9cdCRlCPiFwQERst0sC8Xg7EcdHFRlm50inIZFLqChBjqd9EXLXS0Efd3JWy9JdrTFS29nUsbGr8kigzJnZYx0ZJS4sasc1pTnHuIS2iKaTYCQhYFgeu3bYBR4FFyejuqmQL5PGXS/wK14gmpG5wpU69yytInNz2PrHx4OMCxiGNgO023W8m9zspGkSyjIYitcIjtdwomuMNdRsa/noOrO0d06oSMWq5ZZ5uDtLe9g6MyjNuhaFlba3ppGWwR3OP2w1VD09drdCY0UqPPfE0Qg4qz96nRv3Z+pInYipPkM6dKEC0S7kUkhtBRkeaMHpJrEepRQC7WsFg1E8S4co08kdrtqdYF/cimoIg4hJsr2Pt/lCKBsy5a5z17WFySQRd2v9Zi+UWxUVcELSId+DG/R+mIt9wluhHhuW7lwHL7eggevjw2ntwXF6b5Uq3d2YtXjjRhwisIlsO+MqbMQsFvCmsSNvrXQXN+AB4lcbNydbdu0a7VQ9aMbXyDizyAStnIRgztZjorYqHUNYO27hHR5WFnbxSC9zJLveFa11CYs9vsVJPi3s1iS2JUfLUuDQo3kpBjD81ATDa3tT19uwsNRLol1MqcM22uURteIJUcwbV6zL/ZySt1p3QH9S14f9mmTh/PKIjX1T9PeZNk98J7Bbh4ok5TyYuX6VkNjLXZg6s1xvITGfr49eQgRcYXMxl9Carg5lHG734XWknZQOOsNEfcfLpIGZuLzqpUtMHB7u0ddbMgu6OqhxxtDuODYXU7fN0PVjH5zLsNM9rUBudzEkK3MTM/3B5SIIKKNU8rCnDhu8wMIbeWcpmso5f9B4L8m8HV7PGkgISnQsFaSV1eXFYK2Z5BwcbhPHuXpgFbqS98KpQVv1pComf7zZ225Eu8uoiByFJAh+PUuW5ZrUvptT2egz/Uaz571MBJrYoCoTe1qzRg94mwigl4ObbpAad9jz60giaDdrCfouJCQCd2FPmpLvioUTkR094Wub7uSenClo7aJ+Tk9lHrgQ7HAHfKRJpwwJLbTF/tC00ZGm5g7pdb/sg0PjXlMF4tGULR7b66jlx/zmR5NFNu49CQ8V0pwAvDm7LXGhUxoMudUJmdPTdEELezDJmbD38TljNgetUBs2AiOlRGiQ4ptH5g77t3MUQ4GdzCRuOsJDuev6dExKnr0lZ/6yx47zAYmOoveAb2yOrI2i2VXePSQODX8afZyKx1nuPE1Brtf5YsKXSbmeW7sc3eBalW1cG1lgbtzePufh+nxXzzncOeHoEEeU7hjtYjQT7szhzszqu7k/ox6TEHd04+kjpGvydeZth71CPeToMnReVxusoaDyHt4Cf+znI2lpg2KGd2p9kNvjTCC8QPcF6TvnelaEqes2eNZFCXEQZBfhNB9LN4JOql2qblrNrxs11iZU3UuPmoIQ3abpaYzcyZkHm+99ELNUe8Ukq9jbN7Xc0kpsQaR3ROGRQboWjJwGQT0ssz77+1pnqZu+texB9/pcFoMItZF78CiVx4xzR72XBtFbe5uhs/GHDrvIjFQhUsPIztbgYwE5YceR3YZkFG5Uptu8QURS5CStkXiRRGwdEg+uGRs7rCfpBn/AyGYnwP4uPDkExZxPyrou92jjBwfU0XERGzpUju9Tf5x60FwFTkiv54GQFELVsTi7bkoIOo/H/drvrmqLcsxkiWgVFmkYhHhSpBssTexMu1IPPwppf192+kSiO3jSJUXgfZ95FIFhRS4po5pRQP1DCgBwXyDMUtVLR4+CuAWws7vt54cxYYzOmU0oKEkgaT1ZmmA+vV5FyIWMDABfhDXXsulzZKi2tKzXVZfe6z3lFpe4DeWBIDLjhlP4eXYdfH+/NxreJIwOB05v0XM+odTUTf6d5KkgNHrBiiF2i+5no9rWUgURnbOecmc7OpzbjfbGh51QR0FbfCX0R3LBYB8KidltXFZ5xCQ73/Og13x0k+Y9bGUG5KXNSRqRR0YPQ0ISTooX7EwoaHkE2jTDJmpLGJfRKb2OBnbS9IPIcHfnSmjIw4oYa0eBIcoUaG2d785iT/SVD0mRPKG3cb8PC1g+s1qtH7Z9TegcZCY5s+sKdW7QG9c7fAwfCYHUulQeyAjeKLR7SFP4CjodoXTpUaHQranbSg1mzVOPJ9v2vMX3mBXsZQfA2r5j5atSxXwGbIif4JmmKbZkghtnoXuC3ZRVNntn6YyXuXqGgdgERQbcRrEfto8iR25oY4Mxaji7INstxzDMX94+vP32GPLt33vRbXkk9P/sydTrIdK3F1eeD1ljP/r85PX535Trrx/emjADUr2ew7V5f3l/YPV3T+E+/ksPUBcS0+stsm8P0F9P5Tv/srxp/ZaVUd92zfS1rfLnCyxgR9C3y5uZ7fLybgi+//C8+F0dcJhmTfy1q742cQeO3pa3Jpe3UuIo87tvp5f3B5Mf3qL3x+JfUQL/Gjf1oun7qw+LDz4hn9C3v/1viYsm/B8vAAA= -->
