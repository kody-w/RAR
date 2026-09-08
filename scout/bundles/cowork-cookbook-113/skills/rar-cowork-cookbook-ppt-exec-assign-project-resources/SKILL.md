---
name: "rar-cowork-cookbook-ppt-exec-assign-project-resources"
description: "Builds a read-only executive PowerPoint deck on assign project resources status from Dynamics 365 F&SCM data for a legal entity, with title, KPI, trend, red-flag, actions and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_assign_project_resources", "rar_sha256": "6e18f8b17233fbc57f3ce012e012aef5cbe0df696ee06dad1ff22c7acb66593a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916eZOjWJLnV9HGmG1VjTKDG4kca7MFIRBIICQECCrbsrhB3Jc4auq770NSZlV1Z093m+1fq8wIwTv8+flz94Bf3+yujYr67dOb6tv5grfTNI78emHn3mJT9EWdgK8iccDPwi3yto6dri3q5u3Dm+c3bh2XbVzkYDvTxanXLOxF7dvexyJPx4U/+G7Xxnd/oRS9XytFnLcLz3eTRZEv7KaJw3xR1sXNd1uwqym62vWbRdPabdcsgrrIFuyY21nsNguMJBbc/1Y30sKzW3sRFIDDReqHdrrw8zZuxw+LPm6jBbhM/Q+LvSJ8WLS1n3sfAGXvY5Da4YeF7c68Ng/Z7LIEs/GwaNIYCLIoU3BmU/p2AoTPi9Zv3oGI/mBnZeo3b59+/uuHtxhcv3369c1NAfNAZKVst0BE+iGJ8hTk/FUOsDu18xAsK0eg4Rzcl34NGM/AkOcHi9fdj42fBh8W//mfSW/XYfPTp8/54vX5/Db/O3f5oo38RVvYTet7C9cubSdOgczvCzrt7bEBIrZdPQsGlFfHefj+3Pk7paJc/GWe+/F5yHvotz9+fisAC/asks9vPy2ARj+/1d18/T5TKX/86T2dzfbjT7/TaTrnYS1ADHD9/uV1/yILFv6+NA4WX1Rlu3mdVftuXPqA+B/kmz9P1l/kXir58lz8Y1F+WHyf8izPXwC/Txd0AN3vkwU6ADvf3m/A9X58nVEXdz+3c9f/8ad/RNaNgJOmcdP+S3R/fhKOgN8Dbb1U8tOHh/n+uli+ZPtG8x8fWwKH+XckAcu/HvdNUf+I9sOyf0M6jXPg+V9t+V1y39uw/Mvi538o2/+04cMi+PzG+ilAhNp2Uv/T4teHi/z8g/f74A9//Q2Q/qdk1EeUzRS+ZHYeB37Tfvny8w/P4Pvhrz//0JXAi307+9LV6fdofk+vj3P+pMHXqh//vBecr+VJXvT54lsMLX4tyv9V//a+0G2AKL+PN58Wf4zE+bNczEJ8PfSpgj9EYwN4/YMef3r7DUBPDqTpnvgF8OM//mMhxW5dNEXQLlS36ACAdgAHM39m/hLFzQL8n1Gj9oFemxgo9rXuBbgzx0Ww+OX/uA+Q/+i+QB4qy/bLDNxfngD95bX+yzeA/uV9cQGEizoO4xzg75lWlM+5HQIcng8twUK/vgOgcsbW/wji+eN8sYjzxS//lPaXB5n3cvzlAdLxE/nOG2FGvaZL/fdZPiPy85c0LshZzzTjL9LCBewEMcDrD498koLM0866aJI4TRdeDHAF5K7xQRvo69NM7JdffnHsJvqcP2EaWzyTWgOBBd/YWXz8COQK0jiM2s+570bF4odff/th8d+L/2nXg/h8hgLkfVkDcCiqR3kBoqvLwDJgKGBaAB0Pa/z620u7gEwOEhGwXRzE/nMz8M7E976qWt3RH1GCXDg+UDFQb1YWdQuwfxG37wshWHzjFxw6T83ZISqaOQHPmc/P3RFQtYE43zQJ0t6iAS7YBCCddo3/OPUXp7YfLGYgzO32l4W0UUAuKlLwa2bzsQhsLvIYqP+bIzzHAZH6h2bBfCXxvpBnf1yUdm2XUW2/zgjsp13mrP7aDojbi9zvP+dz1vVnVT2C46kesAhoxn2Z9ONsc1CdZAAJvObr2Y819pwxL4/MWX/Om5fj2/VsChckAnBo2MXenA7+6+VSTVR0qffQH+B0pvSygveyysMH6X9Uvmy/V/Swc9HzuUNhBF/8/1coPfTB8+ctT1+27GIrX87m005zxTjb81lkgtMfDD1i8vcy5itUfUXsz3kaA6erx/96rnxY97XmiYIdYBXgzvlBH7gW4GSm+/D82ZPreo4Z+3P+NTUAkRYPHAT6BDABwmj23q8HzrNfOY0AFsz3v5cJD0+pvVkZwLsXZeekwPMC3/ccG1iojWY7fjUuCAN/juQ+it3oT1LN6gfeBujPRo1BPIL08f4Nrp+zX1n/08ZnNTRveVSKHQje+kEA8OHPDM5mmo0K2GufBTqQ89ODCBAjK9tZdgeED5D0OejXftXFTdzOUPnUq18CnP44fz8lnUf9oQQuB5QF4qLsgHYfkTSDTAZqHcADcFIQWFmcg9wPlPJSwoOgnc2wAGD3VZw+KT6GXwL5j/Cbk9bXjbMg8565Dnj6tZ2Pf0SPy/fcBNDL5hWPc//W076dNtOeEbQBKAhO/Dr7DKb3Z85/FhWLr3Q//V0H9OO/1yQ9srj2Zwf4tIjatmw+QdAz835NvO8Av6Anr82chD/OoPDxGfwfX8H/8Vvw/4nwU+ZPi3+PuT+ReAXHpwXyDr/D89Th5VyvD9DF5iNjfsTn2c/52f8dXsHxRQa8a7bcCLL+t1z4dQlIiGENIAgsfubGZk6pPcjij2QAzPA5/6O3z9EGck0ezt7ZFH9AgUdRADz/qYVvOQtM5S0425uLyNCfO7dHbDT+26e8S9MPbwAd/X+hY5vzUja7dDP3eUDroCZrY/9xB+wDpuOmyOc+JS68efDPPbAChuvFc3YGmAewgpT28N9vLvccBQLW7cxpO5Yza8/Oba71HlA0tH9P/vi4sNN3kE8A7KXNH/37lbbmtP2HMHxqE2jRBaJ8mHMCQBfAB9DmLOUcwnYDYgLw9l1eHpnjyzNz/D1D7Jxt/phcHjXBo9wAIPdh4b+H7wtNlbjv0v5W8P49YQNUGjMtr/g0J90PLxwD36BJ+bD41m8AiV4d4KNbzzvQXP889zqzLR9b5guwB3x92/TtTxeO//bX7/H1ALsvs8M93eZvubuA4s1vF+8gSofF12Uvaf9p5H5EYZT8CBMfUfxB4LuqAVV77PdfAOWwjf6egcNjHJp7ZaAnkG5elT7Y87h8lA5ZN/tc3L4YQ4iPAKfnOjkD/hWl42vDd85/MADyA8iyszp/t9Pv2ioebeLMKtBu+/yrxq9vIHTsuex4Bc+rzwDLAZx+bObqCgL4Ag4E908kAHP/fgfyItBENiiAAQXSR9bB2kFWKIYFjkusAsz1YQSdf2w/IFzHh72ApEjfh0nP9pAgQFF3ZbsOSRIUZgN6T8pf5hoynpmaOQK6+Ahi1f99Ggx5L2me3M+q+tbwzFK/hPr1zSFxsHKHNwL9/GwgCnFI7OCcS2c5kUEx6Kd2PCcqtbkep/ZQ116s5juxzfdhYqHWhY9MmU7QURgYGhaYNE1KfT2wU6RIyZLALphK02F1aMSDNLnAs7dduAyC0r3nCqjRPOJueXaFaHFzmyjNtLlxrx/HadSMcqBSnrMqmlLzvYtJN0rR9b2gDakfryCIMqBYB3WTKjT0FheLfOMMehN3mzMnq4x03nElz8Hc2a53EozDOKY6zLnQbUXBxux6o1aEmzuwpnECZ5a31Ig7rYoFXdqkenNeijxndMxttXXjYE0Ek6SeVfJi05c9fA0thuzOG0nclKcUv2yEs8XkflVQm2GsN1WaSfJVy0K0s+Lx1JaKtQIyBgGGDNT9evBQP8e7yfEGF1oeD55RFP3lVDT7Yj8ae5dAMguN66sqhONo7rnYL6w7c7Kv2ckMetu8VrDmE/I9tzpGHTxB7k16PGzrfq8S/vXGEqeNHobruOoj776J2KPba2hI4ZkqAwnCg7M9U0ldb29bO4hkw7zajuber/q6Do9U2a1P1Mm3mG1SCJbUTyqQm4aUETaaU81rUlpstS05iJExaqUEJ6roxWWHbFpfhizWXI/YWcyMiq6pblvcmp2PHe87aS2TVmRZupjF7I3QYk1Vz1Me4oZ44Pgx5nSq2MejbMSiqMvZycEx9MQ51+LM0aUj01R6yNdVqlsn1L3tNdS5DVdLumPZgeKY5cQz2ZYTbS5NxMIhDjSCFtZGQ0/aZd2z9CEzKK240zghw1Nj0Ozt5A2sREYFfMGqykP3gyA5Bof72/0l3q3t3TiG5sWJBTnb61OqbQoTHYqLrYeczQ81ra6ctkorUZXcqvOsODcEhKJMnM1O92GjQ5ywqnRxTGQ0Xd50qKROB2jwGZUpcpy/j6V8Oiuc3LIjP5hrPusikiUCXblpq20XJ4MiEseTiFtoHi2zDE8jfbscaya+UPhSTvFlm+Lr+kBCFznovDihbrW2YpYNpymKGSxNqCeitr6Aa2JHj8H9yi7pbr3iMCE1zxhjnCSDrb1ejART7waULjwC1AKUdAJ692v9RJq9wawjWoVzFIvYPJbPWr6+O2WZIEeOHBkrUbGqPTp1y8Cju5IhYxtuEmZr14SwUWGPHq89J15LGpeJ9aoe1krk3gceVeRuV7o0XK9tZzPinG+iVh5GyEqAJF/b5EN7X+qaO5m2acOS6rWTAKNEajpruHAC7c6MJS8ogpbkqzpPPNHa8VPuFLrCDltdNJLE4QJiddLkFuFuyOGyu0xyLa/Wgh5VUw0VVawBQ+7sDiZuTMOuVQggzFblYTHV4yVR+fz1llwQJ6DivO6SqFxxh4EWQk3buDfGaVEMcXsPbqgm3LsnnJkyI6AyQ6sGJdKzjCqNlUZwngSlpx13z7NI5NdecqDL7TQM9BBXhWMQF3Z1WmW2blhMiDt7gYMu7hIvpeAgCC1dyRiWouQR2vrnKx8oO3+oI6I8MuNwveN83t8nTOzbgcJxEVPQaxDFlmMy9Ql35HPs1ji72ff9rlHaPutObHpu7M1KAHWTWyB9u6EoUkSaOGMD3y7GkA7X6wBAhlufV9baUXTjtEUC1oTuOE5gRYsuE9PwzYF1+l3pd5d8N2XHmLjKx3Xh7YKjUq+KEJZZEYJt6bbjkd4biGoje8wkeas+57Oq7HKVgbfQXvSvCGZEIzGRPdUcttfSk/oLcbw0ar3rT8b2dKTYfM+utK0msF503CfpITle2Op05inHkZfUOlkerGkb8uO+kkyltombf/OSkrXNkckR86ih+sZf3210czxv1YNYXKLdIb6McGaaWz5tEAw+2jAZG2Kh0xKudsgyZzSlanMhwHqpO8ocjQao3aSeedfHPrkZvZMZkZMfVEk4iEKCX7frchTb5fp4yVfUfS8VG/tqmCVFp9LyNtbnvbBXbEvsqDiC+c2OC83EWUHLIrx6mHxpiwKkTGS3XrPWehnc6115GoOo2Y3klbK71f5ypyvX951dGMOCSTtW0vpsRnlMvQFenBadrt/4XjqUSsjuNE5Oc0zu5fM1EO5XPoNRcaQdWpSImmAYQi8qXjdoikljZWP3MsnJWnZ0S07O8v1xvwYpYCeHk2R3UoHuTko2sp0+kZXYe5TX2KQoHO1uZM81zokB5JMob6tX5BpV+WE8bG4GlRpOvDyGNGi23fZw3RdEKa0CarsvRRnoWiIFRVMH/Lbq4DC2veA0pI5wic67EkEnj8nX2qFz12fd3hPqOZEgyKtxHk9WMR/FUhfgmQRbFavKo3l2S9XLhnF3XgZMk2+M5dR1+/0mp8P8eM493dYMGmP2ZYXFrZui0omInXXgB2p76vR9Ju136EAwZtrTubUHoG0khOxJF2W6gEKOXetscjbirA8i9pTsb8Py5p6NO8MN2saJ0HbPlpy0rbcTN+7CezyJamXFuMiH8SFRaN5nOUSMUbEmrHLa3dK93RxWvMZLZkF7kD7SjcWJZ/oQxoIRpOhEXEDtywQ3AilibsTbjieTyM0NA/ChoVfG96VbGrBCpkHeCvFZWM0V2dU82zQrXitOGTrKG2i7x2o4KVewKPQHzedavjQGiDXbaxXQaC2tz6srmwp9DKIp485nzo3zzB3UW0XTfJmqGcvTiRxGusWxLKbfyDMsr/mCG8Prqr1jp4vkMtSwt6W1E/aN0QY3Se3UrWhRso7wGbaTB8lYy700rVE0CDgVlehTaPWgp6RQel+HshcqWVwwZZCnSy8XU8Pn/ZWSawfxhnHm/nbRTjp0d6M9cyYndSQuQMnJlkxGRghOUwHDfrS3shT0kNyZTwSkCvUTJ7sVLstYtx44RGUpU3Jjm2EPQwfj9t7dnWtY2a+5VZZe+fN+yxx8lNwzewU/7gQ947KtdgxHj7yoB0OFSXFoc64DBVxooxcYNmHoBu7IzZ5RPdLIsKOXdJUYciqDC6rBWVKrOvJuGUYt7Suon9luRssUjJkQtQzKjCcE7YiZVy+WCkj0sXp1VUXFpUCqv6yiJGm5/WUSmSmxB2fytBzuImU15Myut6i9vrdPibjlWztMYFBk8iF76kInOl618MKbwhqVYzNMU6YuGFAlMvre1PFqO0SHpbmSfR6PwvPGlbocrTyCj8XbQQzv2SScQn+JCzQR71b6qFmahaT86WZphTywXlXZWmUYJ8K8mpgQVwYO8BVm+PW2lTF7oK9oa2dlEGety0tcpUx26m8Y5ZoKBXOPo1WqrPYcRQX3HGkZCfQFlrTZcJXQs81xL4m7q4IXGN2sVmjc7G4UQR0vh7Ut5/joBRK9CyzaDdLDaIXUYS+C+/XeFc3Lec0fiFpOyNtyc8QY1kxBSat7HchAa9NJrRPXXS21Ph7b3Gcu6s5cqmgBI04yxFuLmu5VV3WNctKnMUioPcOk/tZOPassqR1th/w6dOAbSCCtnBxlNZXk4STsdXVLMJbUTSevFMcGZXXRNcuLcGTuXokH6HZclnSY9hfg0jyhuRBU4EdC2xYNxrQC6iNVe0IP0CRH6zDsp9zsblHd+Utsi3FxKzdrwl5L5UjLfNtWu9t18K11CecnwhZrbSpAWcuO8RrFVherT+XBZwf4oPY32ZCGIytq+yHdSkZvdmVVmKGrMJhBa9G62IlThBTmmtb4EgB9Hq8YygRFnCCQJnshUIuOrNUxEhMsMTIRX/t6jwySk42kg06BlZj51rbGrq0JPMHPA6/l18PQTnd82A6I1jcooe+ay7XcLyVGGBPqoqaEqMatXnad1R43GMeNtTZkFIfhksipiDwJQx8Rq1YhrXNdVq1+OGTWCa/tMM8SlShJ1pgcgriUsjju7wpJLX3xXtzdrOuR7ammt/ARQNLUmeg9A81SKTdLZkfHJO8g4VFM7gLiXs5hXjqMXRXsOmpG+0rqZ4xWjBjVIN/VOpxwm1NhGdCmD3kgBWQJcSfwUizB+i6Gjlf8hji4bN+NUq0BalmWQ2Fwhm/2VWhJh0tcCGLG+Y1X6l09NNgKyW6bxFnXcXW/OhAO8C7M9BCGjXHKmJw9k37RRJfCQW5nmGU1IYASGvUv8egGjRFVukx4lbquPM6PAp+Hko2+ktqmptbQzju0xFGuWx1CPTVs83Da+Km9vMuqonmQAoBOINxd02SggzUKQ0NbfzxDueCcjuoJa2hlz2ASz7ZID7M8ASO2m6+gFdb7W9FXDd/j1VGKNj5/9sZimy211j5GfRbypmnFang2D6bYxq6VINjGsbmNZmPYyISg/2fEcRiaA2PLQkqBdsPo7/HGPBfI5qBpFwWB8kiHncw8Ii4plzHpFqG9WhV0u7xgSo9Nl5CJ9NJpKPtsrwTcM7brW56sr0cs2bcpwt4F6HK37Ck4Ume/42F4R42DtdUJZDd5x7Rrdhjiyzp0RG+SY+FZGzs6trqm7tRy0R0lXSS93CvXzjXK1ii/kqnEOx3jeuqjwfDOPncfmLHbkaytb/p6iVVDDSNBB5NNcXT0LCekXj4NvagvPYKDXEjD+h2zFzGVdK3Cw+3NMTOTqhR8fyVxdzNXq4O5bIf8NPiiHwa9shFDLzica5JbQ+7Btrpj23P5PeMhnnCqq9ymgWG1qzbZg7JR2p0ccqPT1jYjwwEMKmtqBVHcZVkE3V5iAWxAVoBXBj/d1BhdYS1FU/ezbPZZfYgNg6xZhsC9GD0I+KSelDJCFYza0GeCrHV88CaDhhHW7hkWk649nSTyGDRrZ1ldFIdlmgsnHyTsSJaoOEnrar1yNF8uhCNn66dKzq6EM/G7rXcym3FtqpcRiltxsLGScbzNyh+P7EY9aOeAainP95YZqNcG2MK8niEIVEcDwQQNkwqsdctu0Cmd5K4634+Umin+TS4zZIAd+nqA1bTAMBEOyv5wz2uy8Zp+ctOJ3qi0mqlMv4TWuNWCtnCQL9vz/mYjSLxtyJvd16BQ3SOIc3AhNDJq/njWTb/GbK+ZBCJfSfscoqUIt5ZCZimBnuEhFNtdAiAcHGIJSeXGp0zRQEOxzGlqU0wbTfCEIfK7+sitfK1FKnKMJlHCrtuthhsARLXjAeZaId+1J+QmYtN1hG8xvHPQ0JFuayQiCeI0GKlwh1Jh6d8vSexDKyKUub7QN1CzyTkid7Ils0aWTajnGs9OmYktxQi5mTpRQ522Ibo2kg9HaLX3h1zNzrfgdNMBol+9q5lZHY22uXS0YyI7Y9lgyOu62rWMvy27nbSnslMW34n1hE7O9ZpKaWsiJJQXWxUP+2VLO2Y2priM9mJFYnSE+kVtpocVesZqIlIa0taHHMROxoKeCHZWNJFWYYa4RJGN0/28kkg1Q8SE31dezgru9aJJ92ttmb55DPcg77hO0B6sm0GzRAFRt6oUmbNxwlcMMqQ75HzXkljkjpnACjUmCb4pVysfuZhLmYSJGLvaF1BQNkqJ5XnHVW2Bmh5xvy2RyUl3HC5pEglhh1KeNAK3VWo8E3iXlHVA5soRLVuyNhAFtB5I7GOcozHcpqU2JbY0MPLKl5dcKUFzI3B3etVH57295Q6gqT6h6TW5VHf7jPfV1W48Pm7Iftnjh2Glr3IUc7IimPaKG1lnhYWEjsY4Zsz0ZKfx1Rb0oFvPlcOUty6QUSypjYSX6/thRW/k7noRAtDwbw5yAw3UViLvyvbISQpBly2jEmtqz+9rKTFwbH1I7a3kjjV6OC+3oe+q7No4W3U6JMv95Hjiau94ZoUdV6zEqrWzhdHdGIx1Z1ZU4oxYhJm0zLh+uRQFYX/yaeAaG4wsNK9imuAejcI4trBWQMoNPQx2dqZ4dBuk6aXbMWp7t69WSRUdlgr8NeCjXTfFncTx0J2sbR00LwdjbFu0jGsvIFVjr8GsbJMRahxBurpJaCNV5V1y5RiRdmJfrzv4qC0pYtvF1p7YIaKZ4TcbQkvMKm6bavTP4TK9HwKrEx0MD0kf1uLxSvmnfaE1LavdGV8N6KJSPWlS2W2bWxWpi/ilxS03q3L4ek0atXUwtPBaJ6jJE6kdbQPKSJGHzpeg6rSIguxSMaY1QqgWifTeVkwiPekSahR2gXQQip2putcJUpeQ4m0jJsApnuq9+8k3Kteyh3aJkVoFT63SXQ2suFOOLlsBi3dp1QVnEVsRh4w5wkycI6y3mm6ZXMUO75kdbyUxU1cVaM4dtwyAkvAskGL5tu5Jz6TsXS5nY6hsodEQDzxj23SfOYdz65OTIrNZ1/Wik2tmOOAnSQpbauAF5th422RHxUq7pN1NxONyvkQvtZfL3VS4PG+tzbWdnmISipAda3h1ezyxS82Tzw7LGQreyjTlhnuFXMb3EsLh2927nmfDYkiGITtK9vEJY6UUopLVlGqosx7wow2aFZxjl4fs1LOXS0TC9uqeHKtdXPGlHVMNvFy5bndvL9t9W1DDsESaASFbo+GCqGvYwKm9obuKzaq+TtM5mA7yfmiVzLw0HgQF8VpuYN84+55urqqdF8kNCHxQAlYG0UlbpeZgkY5ptNSV1eXC6Ft6e0G0MyF5MEIKBlzgunc11japcjkbHo+ItORh3tkYoJnyYUrZhIG6OdSgELlge35tC5TvoUc0vm5WUIphZoRY5IZfdkbgkpGFwbfe1Y9k5B1YnqSGw2pFnpbnzTajkEOhlnEW7U7pVqHQK+GtVyy+XC+Zy4SMDL6KKSkQYMZrtfg6dbpmQ6tdiivEgd0qgampyETfb7Wr+FDPNcWwt7zt/EjlL395+/D2+yO6t3/91bL5cc7/sydHzwdAX18VeTx89G3v0+OsT/8GT3/98Fa7MeDo+XysSbvw9aDpb56OffynDxjn7ePzfa2vD5Kfz8BBBzy/yPwW517XtPX4pSnSx6siYIfTNfO7j83MI6DR/On56UuM59hDgraYFwbxPB3n8ysgvhfbrf+6DV/PCz+8ea/3kr5gJPHFr8tZ0Ne7BkA+7B1+x95++7+z9ndhhS4AAA== -->
