---
name: "rar-cowork-cookbook-ppt-exec-implement-the-disaster-recovery-plan"
description: "Builds a read-only executive PowerPoint deck on disaster recovery plan implementation from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, risk, action, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_implement_the_disaster_recovery_plan", "rar_sha256": "4a9c13b36953b349da23d54a70b3bc9ebe39426f844404a6bda0f0967c9fe6dd", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_implement_the_disaster_recovery_plan`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_implement_the_disaster_recovery_plan_agent.py` and in the RCI capsule.

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

Implement the disaster recovery plan Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on disaster recovery plan implementation from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, risk, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-implement-the-disaster-recovery-plan
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
      "description": "Prior period to compare against in the trend chart.",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-implement-the-disaster-recovery-plan-2026-05-24.pptx.",
      "type": "string"
    },
    "review_date": {
      "description": "Date/period of the monthly review used for the report and filename.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_implement_the_disaster_recovery_plan_agent.py` and embedded as the fenced Python below (sha256 4a9c13b36953b349…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_implement_the_disaster_recovery_plan_agent.py` first:

```bash
python3 ppt_exec_implement_the_disaster_recovery_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_implement_the_disaster_recovery_plan_agent.py   # or on stdin
python3 ppt_exec_implement_the_disaster_recovery_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement the disaster recovery plan Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on disaster recovery plan implementation from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, risk, action, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-implement-the-disaster-recovery-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_implement_the_disaster_recovery_plan',
    "version": '3.0.3',
    "display_name": 'Implement the disaster recovery plan Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on disaster recovery plan implementation from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, risk, action, and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-implement-the-disaster-recovery-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-implement-the-disaster-recovery-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1a49392ebb920ed9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/implement-the-disaster-recovery-plan'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-implement-the-disaster-recovery-plan', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare against in the trend chart.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-implement-the-disaster-recovery-plan-2026-05-24.pptx.', 'review_date': 'Date/period of the monthly review used for the report and filename.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for implement the disaster recovery plan reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on implement the disaster recovery plan for a 15-minute monthly review. Produce 'ppt-exec-implement-the-disaster-recovery-plan-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads implement the disaster recovery plan data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on disaster recovery plan implementation from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, risk, action, and appendix slides plus speaker notes.', 'example_request': "Build the exec PowerPoint on our disaster recovery plan rollout from D365 USMF for this month's review.", 'inputs': [{'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-implement-the-disaster-recovery-plan-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Date/period of the monthly review used for the report and filename.', 'name': 'review_date'}, {'description': 'Prior period to compare against in the trend chart.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready PPTX status deck on disaster recovery implementation for a 15-minute monthly review, sourced from D365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecImplementTheDisasterRecoveryPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecImplementTheDisasterRecoveryPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare against in the trend chart.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-implement-the-disaster-recovery-plan-2026-05-24.pptx.', 'type': 'string'}, 'review_date': {'description': 'Date/period of the monthly review used for the report and filename.', 'type': 'string'}},
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
    print(PptExecImplementTheDisasterRecoveryPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916aZObyLrmX9HUjZjuvrILEJvkGydikITYN4GERPuEmx3Evgro6f8+iVRlu8/xuTN9Zz6N7FJJkPnmuz7Pm5X8/mJ3bVTUL59edN/OF4ydpnHk1ws79xa74l7UCfhVJA74WbhF3tax07VF3bx8ePH8xq3jso2LHEzfdnHqNQt7Ufu297HI03HhD77btXHvL9Ti7tdqEeftwvPdZFHkCy9u7KYFK9W+W/R+PS7KFCgQZ2XqZ37e2rPcRVAX2WI/5nYWu80CJfDF4b/rO2nh2a29CAqg5yIEC+SL1A/tdAHmxe34YXGP22gBPqb+h4Wgch8Wbe3n3odFHTfJh4XtzrI/PGy0yxLciYdFk8bAIKBE1yya0rcToFpetH7zCkz1B3vWq3n59OvfP7zMOr58+v3FTe0GXHpRy5YGpnLvqhuRv3+z7vhmnApsA3LAewgmlCPw+fy99GtgRAYueX6wePv2c+OnwYfFv/97crfrsPnl0+d88fb6/DL/O3b5oo38RVvMa3gL1y5tJ06B5a8LKr3bYwOc2nZ1PoejASHLw9fnzG+SinLxt/nez89FXkO//fnzSwFUeDj+88svC+Ddzy91N39+naWUP//yms6B/PmXb3Kazrn5bjsLA1q/fnn7/iYWDPw2NA4WX3SV3r2tBeIelz4Q/p198+up+pu4N5d8eQ7+uSg/LH4sebbnb0DfZ1I6QO6PxQIfgJkvrzeQjD+/rVGDEOV27vo///KvxLoRSNs0btr/I7m/PgVHoBKAt95c8suHR/j+vli+2fZV5r9edi6Jv2IJGP6+3FdH/SvZj8j+g+g0zkENvMfyh+J+NGH5t8Wv/9K2/2zCh0Xw+WXvp6CEa9tJ/U+L3x8p8utP3reLP/39DyD6fytGL7rafUj4ktl5HPhN++XLrz81j8s//f3Xn7oSZLFvZ1+6Ov2RzB/59bHOnzz4NurnP88F65/yJC/u+eJrDS1+L8r/Vv/xujjbAFu+XW8+Lb6vxPm1XMxGvC/6dMF31dgAXb/z4y8vfwAQyoE13QPJZgz6t39bSLFbF00RtAvdLbp2AQLcxpk/K29EcbMA/2fUqH3g1yYGjn0bB/J/jvCscREsfvsf7gP2P7pvsA+VZftlhvIvX7H5C5Dz5R3Av7wD+CNffntdAPgD2BGHcQ4Q+Uip6ufcDsGsWYGy9hu/7gFoOWPrfwS1/XH+sIjzxW9/aZ0vD5Gv5fjbA8bjJyIed9yMhk2X+q+z3WYEqOFppQvI5UlI/iItXKBaEANEB5zgN0UKOKqdfdQkcZoCbgJrAZYbH7KBHz/Nwn777TfHbqLP+RO+0cWT/hoIDPiqzuLjR2BjkMZh1H7OfTcqFj/9/sdPi/+5+M9mPYTPa6iAUd6iBDTkdUVegKrrZmeAAIKQA0h5ROn3P948DcTkgKqAY+Ig9p+TQdYmvvfudp2lPq5wYuH4wN3+zLBF3QJOWMTt64ILFl/1BYvOt2bWiIpmpuqZG/3cHYFUG5jz1ZOAGBcNSM0mAGTbNf5j1d+c2n6omIHyt9vfFtJOBRxVpOBtVvMxCEwu8hi4/2tSPK8DIfVPzWL7LuJ1Ic95uijt2i6j2n5bI7CfcZmZ/206EG4vcv/+Of9z7/B0DxgEPOO+hfTjHHPQx2QAIbzmfe3HGHtmUuPBqPXnvHkrCLv2vzUoYRd7M038x1tKNVHRpd7Df0DTWdJbFLy3qDxy8Gtb8BjxL9oe+ket0n5ulT53KxjBFv//tlezjyiGOdIMZdD7BS0bx+szdnO/Ofvt2aKClR8qPer0W8vzDmvv6P45T2OQiPX4H8+Rj4i/jXkiZleDAB2p40M+SDegySz3UQ1zdtf1XEf25/ydRoApiwdmAo8B6AClNWf0+4Lz3XdNI4AP8/dvLcXD/7U3OwNk/KLsnBRkY+D7nmODSLXRHM/3IIPS8OfqvkexG/3Jqtn1IIZA/hzcGNQooJrXr9D+vPuu+p8mPjunecqjq+xAQdcPAUAPf1ZwDtMcUKBe+2zvgZ2fHkKAGVnZzrY7IF+Apc+Lfu1XXdzE7QyfT7/6JcDxj/Pvp6XzVX8oQRUBZ4FaKTvg3Ud1zcCTgb4I6ACSFWRoFuegTwBOeXPCQ6CdzVABoPitkX1KfFx+M8h/JPVMcO8TZ0PmOXPP8MxsOx+/RxTjR2kC5GXziMe6/5hpX1ebZc+o2gBkBCu+3302F6/P/uDZgCze5X76p/3Tz39ti/Vg/NOfE+DTImrbsvkEQU+WfifpV4Bp0FPXZibsjzM4fPxa7R+Bsh/fIeHjOyR8fLSX3y/ytP/T4q8p+icRb4XyaYG8wq/wfEt8S7S3F/DL7uP2+hGb737Oj/43+AXLFxnItDmKI+gQvnLl+xBAmGENoAgMfnJnM1PuHbD8gyyAlZ/z7zN/rjzARXk4Z2pTfIcIj6YBVMEzgl85DdzKW7C2NzefoT/v/R510vgvn/IuTT+8AKz0/9Keb2awbE70Zt4zgpICXV0b+49vIGrgdtwU+bzTiQtvvvjnfbUKLteL590Zdp5TgAHhI6/fOeyBwLOtdTsr3Y7lrOVz8ze3iw+EGtp/lq88PtjpK6AbgIZp833avzHczPDfVefTscChLrDlw0wWAHSAksCxs5lzZdsNKBVQJT/U5UEmX55k8s8K/YmOvued2fqym9uzBzvNBf6z/xq+Lk66dPjlhyt97aD/eRkTtCizRK/4NLP1hzew+/DgyQ+LrxsYYN/blvLxh4C8A7v1X+fN0xzax5T5wzPUXyd9/euI47/8/Ud6PRDxy5yJz3z6R+3kGekAE8zufgX1PDyzdvZAXXidC9z+MP0vlfrHFbwiPsL4xxX2kPlDl4HtQezfv8xB/UFswFXoLRfftMtAYkXpDKPzvDlVvO/Ac+4nH7X2buoP1nwsCggF0PLs2m8x++a54rEHndUDdrTPP5n8/gKqyp5z4a2u3jYxYDjA34/N3KJBAITAguD7Ey7Avf+77c2bsCayQUcNpGH2xkVQByU2OHjHNp69Qj0cs0nYQR134zs+usFWRLDGMAzGbMLxbDiANwTpbgKf8Dwg74lAX+amNJ4VnLUDfvkIKtr/dhtc8t4se1oyu+3rbmr2wJuBv784BAZGsljDUc/XDtog4CLpHEtnWRN+gWtUbZ/smN03itzzBO10JHsMSS+qVhIpb2/w1rDoNM5izjp02QpmopDNBN/l8aRHlSqOS/3MBg6gCf3O0UnT1afqouJTZVaqu3Z6+W5W3iTUW/F8LArsZDOVtUsFxj8FlpgYx2OZYd14uylFtdT3B/+CpSMkre9BZDDnldBDEOIseTy39YGO6SwKaHjaCF7Cwsa1rDRr7Zq6fs+v1jlEhFpqlzycYheHP4gxfPbV4dpDAduPenOMDtfyfMmEjXx0uOOuvlz14i4S6YpGmfN5221rInNjdb0JpuR41rPJ34nC8YAox214dC5D1mixSGVL/QYLKVjznAnx+cSdJHF9ACzl6curum1WSyi4qCvSkVGLCGJSNUl5gjAsQumDcraOOicSq8pIkfjC2MUqPvJHkzNEXjjnS/o01lpzYBux5eiVaZ1vXd7F22rUz14YMsjhcE4nznRwYnMN+CgpaJkr21OfR1Z42Vp8Rk0sM+3FQ8qfTdqhOt7gBRi+jdjQrSsH9+MWv0hGFaIbMak55d5Nuig2Ix7Skruf/DLJknPEM/pmLwi5nexKqztnvm4x/SCfstiwW8jac4XRa3x1yg4G0UnFrWF9ROlJad0SVoTbuibTTFZhWdEgsalu4UZnBDml5Yrljuez7ohZqq2soQ4DpD21SpLeqKODUJtUuCwrGj9T1lG6GUgqpWRTBgFnEja7NqW4CMv92MVltVPP3v4mSw0IYXRjB+quHM4mYYgSe4vZQB0krpW3RCYYMXu7cYjNE3Z9ClfXG5X4R3EwluqeNwzJioZMgZh1RNdb+GA7J9mtNKYVKfTG1ymMCANbylICaO+WmNJqeb6k3jESxsOSa4PBNIl0dPGDh/vXTIVYgYfWl6K+6lOg9cskhGlj0EltHTXACXjl2uHygjgYqgyVXe4m05/incdYJRbgXmdZqSHHlWDTYSkxpO+HrVJughX4gculQ5BRS5IX9m5nI3bABnlaXy/QnV1SMrqGo+yyDOFBKZsNlLEEn2IS6sZoZOu0tS0dpZ2o5tTiish6u6N51s9MmUV30Kak8M65UdcLSef40SU7yvKvyEEfXApxUeFub+XMJnkxNdqlsWmiZOMLIXlOqO0YrXdV3bCadN31l5MQstEWo8PggnHbrToEJiV3TGlTirj2nZ2AHZLTysqjCCFpCPbvu3zw+lg+t+LJLhKYxrdZmFwn6hiqNXPdVXhGyXsJRrhBin3qpqvmMbjiFiNeRZIpIBG/w2fBNPtDPrRDG5KcjcCe7KtrtCGDe3XZ9VIfhZl5nvYU62/HVGKm7kDveR/RbsejEG6Xxz5OrKEUllY3bKHCH6J6eaWsM9tpB3NabUI23N4MXsllqJZqrR5oW6Jc7TqK3FUMhxvt2v0a5VkTVTOZm6Az554ETKoSZ9hoUrya+j29z7aFSJwES7W3Xh0VBqfTO9JjAoHN0VuQbGs5rXieWxLANz2u5HsvmoagN04j3btSW0HB/QhFuWkZIXnbaverEjQstDfvq0E0QfKyh9gXE5a27/fc5ZAC7rR9KZ9gZNS3jlymTVatC5htIGXv++hxFVF2KLGTtzq1PNSifj5qw6HURHvtswUxiW025Dhx9Kxcvx9aDbWQBD8qRXsgjZ5e7pYpLniTejdNJvVGmB2NcNlxEkYhB9u+WfRGvOdMk1SEJx1PYaQrcYrYtG9U9+UWXm3gvejxjD9lOK2tIfgQ0sZBz8j9ydUZSVtq2H4vK9TNMO3TyW/WzMbvcwUhsnh0tkmsDNJulRUGj8GEbTEphQG2VvnIqiQi21o06SZS0uiSGN6QgU8dgzvHew0hJmKbmt4g9CeBYnc8am7GOOfPHdO7Y+9TB+QKn9RJOwV3u9p44rkOd/sKA+mHK2Z4HUzCwd3EseBuVEUYUi71esPdw8qyDrd8vbMnQhZkob5fcTJd3SVB1Sz+ZPLZADWQ0O3DmymxjnWMrvcOgtT6iNyh1O1z5H53R6itr6mVJ7K7l6VpYzo0TSlubMLU3u2pyOC1tE42pyr2ixOzT6Ctcj3ZWd1I9+3FhWhbMCbfYRpaDanS9QlNQ442P+kNFdClxg4CJ5D7LW1KhTRG4+5wyNgVlx0cHOFsLjKAeS07FI58pXIxRSg7FUwYG80yVG99Sx4Ivzd3crJJDnKjSawe2mS6uXSwOFajE8rnrRbJJnPpL9PymmoUWQhwal50q9Y31ZKlj7rtYK7bSppGpeN4Vq/8DoaJ5XDjz1yvCp0Y+9XN2B2uQrs9U1eWCelht8k3PeLdpGOLb7lY6gK4bguR3qYVBZdYGXp3blWbPVtI6XBGWhwaoJMUHajI9qqqj6phV7IylyamiPOANCXuWJVHDIAvVWmEfeL4RGfQmjqUI7ee7jc6xafaxFrozFejdjufTL+98r5254RTdPJVkBPOERM84T5VglxoHo/fI+hocfGA4g5yYfQYT+Vq5cSOpmnb3a3ctd4JP/iOypzhcCWJYrrj6EIKymAidzlc3rFSh8fLVh77gOSTcaRu64pIznuAbnLsYDIkxq2CnLVEnc7uGa+U87mBYxyRkFCi9kfFBbrap07Fh3UEiU4vTLSL1vCNxySeu4uNfzyzrV8GPHIRUS7cHFKrqPFYT4vj8p5P22YfljuOw7ZmoZxsgE7e+hoLqx27TU6KujHVSo36EKbCkxAcx2W7lYY7Sx7K2hhWym50cFwaRKzRRnY1mSefJKyLNFj3gvMvftst/Z0lKVy6nUon8aBrkJUUqoQjomuWcPf6qcEl0bhD6CFZhpbUYdUJYMdI2XsyOWiVtPLNUXDxMNHyJtKsHSHIu/y24U0paR2k6Lj1PW5OurIr24jZ4d1aXVFdpRROFF90vWgzvjX2RyO/IGxEkoVB+udNScNXGgbUWhj4ntI2eyJshnjgGAMy7CM3XvKtIDdTkGuxxLQJrjAbFSNRjQmdwsqFCG+m3KhWqX2gQ2xHl6Gpp+d2OkKl5GjsbcjqVS9UoCTllQoF6NI+TqeonsStXzlT6qWk37cen2xEWOUstWP0CtMEquRU6dYJqdqlUTrYkC/h3HKf+xJ/2I8JX52VHLqJUTiYFtUKWKFwgs8kOxuJGXOQDWnX0pWWYNs2Scq1RglJdz9AK8cstgQt6yReXg3X1Up2a1YITxXCypFAM0BjRte1rno6Dqkvn01xfdQS1zCrA6ajZexn+igl0XBYyQSjMw633Q+Uzh7kozQipxQrk4luh50Jx4yAXppkhfaxs4qHaocgJ4zzEG6ZtUGgQivk2g1p7IpKvN2ALlXrPJdWWaq/NgiLqkQhTEp8dkWWq/fccQ+wnF4Han7DkMDYYst8L+JZVuOKsMeydRGNwmEi0yNNi2g1QtFZQ4XgMtm7Iy9ebMLnJs2iFTOwlnF7OedwDZp5M3Js47RfbXX71OP7THake5LJS0nx9ktdiHx817RjKJvhTkq24wmXlx2frnOIkKwSjcVTchwPxaS0jFTLWGe6rF3SQx7iSBDCejpiJpfwCW3FnawJfZsvY1buOH1HBowJWUqJbuPz5Z5lLbHNsWZDV1sKOuCW5Himu7Ss24rA92LODKJ2LUTEMVcqCtebLsjRwReKtlyputqfjVFIlk0g9stW0XjDvRQjxHTlMqvNJD6GEHuN1b3CmekJa+TU7wvYiw8ixGzt9r4hGJZKh1g73GOrKix8onSvtAf9vOOxDXqTmM3QVaZ0ygbM64Oo6hlIN4xLQvA2NyWAJiTICER0Gtym0bv2ugodP922GH/gut5Kkeu9jPwkJUT6dh/ZFGz3ylbwwrwa4GDrbXcXypo0l8w2xxXWSAfzAFWclYSWM0mMnl6mjVGdARDEpY9Sqsi1Rw1W2j6d4EQVV1pooV0TQDdrWePq7cToVBVW2uSovq3EsX3pIAmHd6jNYrRtytscCtWdJY4Hk8Wuhe0cTaEJN9xNys9RAlv3EzK1KUSCzFpRuzTLReVy9en7ufen0/lqSqak5bl4rwkHso5GBAhkZ9mpem3i6hK4dzy7UxlX68ohGn2a9/cH80ZX03mjMnf/BK/3l7OH9noekYCSblrk07G01XQuyS/5+mof1FQ3Eqc9rGl45e/GO84kgjLxTjHCR6+DVWNIi6gpq6GTGYkYFMKuMA6ygwRscyeBOWfs3kMPecLinm3yNrE8wcGZ3NBoRzeEeUUCt91YBV+Ox3VWGy59OG3pLLAJBr24hEbtsiV1iu540GkN4FRc2EaAXrpr2Xmg7+SX0HJaRstBR/1Df4FNTPYGyaAzkbXDjGZczVIQfTx2ZdPkrYIrDknKGLVbqTdn2HdnB13TQeolnCUWcOudWU2pE1gz9yJX3HdxUFidWt4vhyMMasRnyMkZkd2tuXnsRTGGrGU2eiYRexzNwlJtwoSw91eOdIYAc0sP7CH6lGud4IA5GoyyDrPmMcBiAbuM0EttEpxqpS1SxvAF9ZWzjBoo1q9G+IxaXX9t9+rR93wP9AkpekG02lUK/AYjrB+Hiul5Pq7uacvAxlrULZTdnP2i3+rViiJ4h+9GagmLqyt/CDpy32K2ZRAQEV/tNu9sewOLgZkTObQV+UGt3Clb50uLChllOMjjnSZlDWbZgD/iOdI1hKAOV0WArPXVynvMHgKkR+w7qeNreCmzeK2ReKS2x1r2IvScoWBbUq6dO+xFvWbVTDpdw5vmZxmEoj0EnyFkW5WaabU9iTsQq1IXygjpUV32XCXKgUBdeH2sLi4AKEndS6ZtX1hbP2/gk2tAO7hPmlu9EU180jgu2vBMVscqpisau5UaXyavPAqbBXqoTeAXaemyQmuho2o4mu9FwsQft9p4IHLYmiI0UxRKv0KFfMUNFEWSrs4vQRcp1mECKUGbAtcNUK8QhLDeKFgUbzqONtai5qQjs28aN7md3TQplBzLxCOPoobh+a3BrAcSq8TohmyEqPDYU63kW1W4IC7kR92yLhAmoQYuMQZsycEo2ZTKDQ3oo7Q3kLRSGyFG7g4fT6sBdhx9rYCgspl3viqhnCtokfjohjiAfTNzWks9ZaiXvhNdLRiki0AvOVtZcal+Fo58TV9ZPl0ajU+6Z0SgldC6Q7rOIBv3hJc1sXMIODwYRxh4guUTg2Om62nnLCXRAp3/Tl4yMM/hLT5QmI8LAPY8ZWdfo02g9ZurxO4HiOirJXRiIotPs2a3hnZkgtz9bkJopreTtetOCnRvlNje9WqvlLpceGgDOnVozeMHjyXZDUhs6bq8dfduoGX/mFzUpONDn9Bhs05pwOWUIrXwGOYZ4sLnSTJBwyEQ+zYZOxNSGCfnhXivEvA2DcmWDFEnvNUCtiPx5dqL7a7n1Q3YdC59q0GZtgsKjsbrSW7b/Yay4ytmwWWb9n68sjZkS1w4SdHd9Y1zL44m9Zfcui6vZijcmEInb6icDCK3X8PBejBI/qittDXbTpHA+bFf5gddsGDEPl467rq5iwYqr+P7+iqXZNBT65Vt+zhUI3m+ulVQseK8ZXCLkZFM2TO+1q0U8y5inyd3xmH1amlVjdOd1phq9nXvJBe+I5bRatV1oGU0unip3swjpGObuhtKMUWNQ0frQeJfqaynwB7aaoY8h3O7Px/h+FgqnaIF7s5aoZtyaA387qxLmCRPwSSwnYW3yr6XEMrhdyNzTtVEqQ4bk6Tbqxye1coBONxnCLsGwH04Njsi3RcZivOgQUN7bLujx3urnkZGUnGu9GQDbwaB4XMlyYZo3W39rNJHx9zrGw5bY3SPSfGaPMTrpWA4Pk8ylYEtYV+kO3nsbA4xuTEgjxcp8Ic95Gj7657QQQOGbmmuchpqdV7t2VXVb7J9czVuerGe5ENYQH2fO7c+82y5EyBRSNbMLnH8eydO5HGTVJqULZGd6rJcWgnI5HeOfzrgkMjobbOyss7rV0dG0Fd72cejbKeS6/YmmYXsJkOmLgeL2XckkhlOXpkQzsSjRQxINU7ycDmTzR7Dj2CPOypWvVTqtFcgur2N+qY3uaHcb1SKRir/dBfQXOLZ2EQSIRki+WYaOtLuGohXYEVxR6Pjio21CiITJ0fIhCG0kO4ldD1ZXhDkS/nU7MkUre8kNeQbOfOSDomYIyBUhcthTfEpwwwdZe1evCWywQPCNvZBLapOXfsUXB0IeJ9wctvBLbLvvO6yIlP1rFz48rLF1m3W+dgRJRCRiBTcH28r3kNiA5GrTBS8q8my45ZCkqKLXOeEQ+iedMK+PprD8ioLnb8xxlXq3cg4wNhTGu82MnU1+LxYtm4jZvkUXCx6M1UK5XjcaqeZAxbTVG4q43W3maaNF7JUce72B8xLLk6DI2uPLzBOzdRQq1z14gsYTpClJxJUoE+1e0hUo4BC+CQit8jaXE7eRgkAIZLZuiPtVtkMTswGZX2xCGzEA8ja4WdZziC5Ay31dfK3VyjGc5iC4bvvmR1J7oUbVkWlWYBaU2OVrmvyhIfZOsBwSBg9gryd6y2LBfUOXQmQ65ynekl66+nkrFeT3hgGntE1G0AQFu4NNc/SS9+aMbFn3TNZGpvTSjvu8pV7l3w7DbXtSQxG94QZHnWm17J20i64cJ5iN2Gty8kPwG6waXHpOKB8P2bazTaSGPQlxztEbNc8l8IFKvWdKeOwxmygxmqYJbuCnH45XKoRZuS1u15i8Ih25SVZV/KwI8xYRsjucjfhaD1hXEvGZy1V6XanhGLhM/FaIfCcHDbIep/fnWQfTQfitEQKHbItnjuEZ9qG8LwkRBxlG3t5vLbZ3Q5sZ+3vobtvwJF/6mmJoqi//e3lw8u348CX/9qzcPNx0f+zk6nnAdP7cyyPQ0/f9j491vr0X9Tv7x9eajcG2j3P5Zq0C98Otf7hVO7jXzrYnEWNzwfP3o+5n4f1rR3Oz2y/xLnXNS1QpynSx/MtYIbTNfPDnc38/K8Lfv/pPPfNPPDR9p4PqACj2uLL83ByPpeL8/nZFR9Q5dev4du55YcX7+0M+wtK4F/8upwNf3swAtiLvsKv6Msf/wsHM5ZZfC8AAA== -->
