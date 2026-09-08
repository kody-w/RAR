---
name: "rar-cowork-cookbook-scheduled-brief-modify-production-plan"
description: "Builds a morning brief on modify production plan from Dynamics 365 ERP for legal entity USMF: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, drafted as an unsent email plus a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_modify_production_plan", "rar_sha256": "590bb65c5a12aff290828fa1e18afdb1c76ff5b38f653b89e322429c7b2fc36e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_modify_production_plan`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_modify_production_plan_agent.py` and in the RCI capsule.

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

Modify production plan Scheduled Email Brief — Builds a morning brief on modify production plan from Dynamics 365 ERP for legal entity USMF: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, drafted as an unsent email plus a

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-modify-production-plan
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
      "description": "D365 legal entity to query; defaults to USMF.",
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
    "owner": {
      "description": "Responsible owner who receives the drafted email.",
      "type": "string"
    },
    "schedule": {
      "description": "Optional cadence for the scheduled task, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_modify_production_plan_agent.py` and embedded as the fenced Python below (sha256 590bb65c5a12aff2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_modify_production_plan_agent.py` first:

```bash
python3 scheduled_brief_modify_production_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_modify_production_plan_agent.py   # or on stdin
python3 scheduled_brief_modify_production_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Modify production plan Scheduled Email Brief — Builds a morning brief on modify production plan from Dynamics 365 ERP for legal entity USMF: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, drafted as an unsent email plus a

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-modify-production-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_modify_production_plan',
    "version": '3.0.3',
    "display_name": 'Modify production plan Scheduled Email Brief',
    "description": 'Builds a morning brief on modify production plan from Dynamics 365 ERP for legal entity USMF: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, drafted as an unsent email plus a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-modify-production-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-modify-production-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3311ce6c4ee310ca',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/modify-production-plan'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/scheduled-brief-modify-production-plan', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email.', 'schedule': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where modify production plan stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on modify production plan for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads modify production plan, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on modify production plan from Dynamics 365 ERP for legal entity USMF: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, drafted as an unsent email plus a', 'example_request': 'Give me the 7am morning brief on the modify production plan for USMF and draft the email to the owner.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email.', 'name': 'owner'}, {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when the responsible owner wants a daily or weekly (weekday 7am) production-plan brief with an email draft and Teams-ready summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefModifyProductionPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefModifyProductionPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefModifyProductionPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/91615LbWLblr3DyPlTVpZQwJEhQNzpi4GkAwpGEKVWo4L0HCFNT/z4HZKak6lbf6Z6Yp6FCmSRwzj7brrV3gn+8WF0bFvXLpxfVs/IFZ6VpFHr1wsrdBVX0RZ2AX0Vig/8Lp8jbOrK7tqiblw8vrtc4dVS2UZGD7WQXpW6zsBZZUedRHizsOvL8RZGDC27kj4uyLtzOmVcvyhQc5ddFtqDH3Moip1msNtiCUaSFX9SL1AusdOHlbdSOi6sqsJ8WbVEusEXUelmzsMdFlJWW034AWhaZlUZes7g3izb0FtuPrjUu6gJYAVSw7l5tBd6HhzW15xRZ5uWu5y5yb2gX1kOZ5sPCrS2/BVctoH6+6PIGHL3wMitKgaYduAiM9QYrK1Ovefn0628fXsD56cunP16c1Gqa2XdO6Lld6rnkbLTwMFj6aq8EzAUiwM8ArC1H4PD5c+nVwNoMXHKBo94+/dx4qf9h8Z//mfRWHTS/fPqcL95en1/mf0qXPyxtC6uZlXas0rKjFLjqdUGkvTU2wNK2q/M5Fg2IVx68Pnd+kwSc+bf53s/PQ14Dr/3580sBVLBmfT+//LIAYfj8Unfz+9dZSvnzL69p0Xv1z798k9N0duw57SwMaP365e3zm1iw8NvSyF98USWGejsLBCMqPSD8O/vm11P1N3FvLvnyXPxzUX5Y/FjybM/fgL7PjLSB3B+LBT4AO19e4yLKf347oy7uXm7ljvfzL/9MLAiuk6RR0/5Lcn99Cg49ywXeenPJLx8e4fttsXyz7avMf37sXCX/jiVg+ftxXx31z2Q/Ivt3okHJgEJ6j+UPxf1ow/Jvi1//qW3/3YYPC//zC+2l0Vyldup9WvzxSJFff3K/Xfzptz+B6P+jGLXoauch4Utm5ZHvNe2XL7/+1Dwu//Tbrz91Jchiz8q+dHX6I5k/8uvjnL948G3Vz3/dC86/5kle9Pniaw0t/ijK/1H/+bq4AXxyv11vPi2+r8T5tVzMRrwf+nTBd9XYAF2/8+MvL38C/MmBNU9wmeHnP/5jIUROXTSF3y5Up+jaBQhwG2XerPwljJpF9MTH2gN+bSLg2Ld1IP/nCM8aF/7i9//pPDD/o/OG+VDzjmxfHnj+5QnmX76B+SNRfn9dXID0oo6CKAfYrRCS9DkH0AuAFJxc1l7j1XeAVvbYeh9BUX+c3yyifPH7v3bAl4es13L8/YHl0RMDFeow418Dtr/Olmqhl7/Z5QAk9wbP6cAxaeEAnfwIwPcH4IGmSO8AP2evNEmUpgs3AggDSG188kSXf5qF/f7777bVhJ/zJ2CvFk+2ayCw4Ks6i48fgXF+GgVh+zn3nLBY/PTHnz8t/tfiv9v1ED6fIQH6eIsL0PCoiucFqLMOsFQLQgaCDEDkEZc//nxzMRCTA3oGUYz8mffmzSBPE89997e6Jz6i2GZhe8DP3kyVRd3ObBi1r4uDv/iqLzh0vjXzRFg07cL1ypkdc2cEUi1gzldP5kW7aEAyNv74YdE13uPU3+3aeqiYgYK32t8XAiUBVipS8GNW87EIbC7yCLj/azY8rwMh9U/NgnwX8bo4z5m5KK3aKsPaejvDt55xAWz0vh0ItwB/95/zmYS92VWPMnm6BywCnnHeQvpxjvlipn0Q2Ob97Mcaa+bOy4ND68+A8Z8lYNXeo08AqoyLoIvcmRj+6y2lmrDoUvfhP6DpLOktCu5bVB45KPy42/naISyYR2PxaBQWnzsURtaL/597p9knBMcpDEdcGHrBnC+K8YzV3E7Oq58d6KzvbMCjLr81Ne/A9Y7fn/M0AolXj//1XPmI8NuaJyZ2NVBHIZSHfJBeIFaz3Ef2z9lc17PNQK93ogAmLh6oCLwLoAKU0pzB7wfOd981DQEezJ+/NQ0Pz9Tu7CSQ4Yuys1OQfb7nubblJECreq7gtzCDUvDmau7DyAn/YtUcMJBxQP4c9AjUJCCT16/g/bz7rvpfNj57o3nLo2/sQIjqhwCghzcrOIevj1qAY1b77N6BnZ8eQoAZWdnOttughIClz4te7VVd1ICEaT68+dUrAWB/nH8/LZ2vekMJqgY4C9RG2QHvPqppTp0MdD5ABwAooLiyKAedAHDKmxMeAq1shgYAvW+t6lPi4/KbQd6jBGcKe984GzLvmbuCZwFY+fg9glx+lCZAXjaveJz795n29bRZ9oyiDUBCcOL73Wf78PrsAJ4txuJd7qd/GI9+/vcmqAenX/+aAJ8WYduWzScIevLwOw2/gvKDnro23yj54wMmPj4x4uM3jPj46By/l/40/NPi39PwLyLeKuTTAnmFX+H5Fv+WYW8v4BDqI2l8XM93P+eK9w1nwfEAa9qZB9JxxqB3UnxfApgxqAFygcVPkmxmbu0BnT9YAcTic/59ys8lB0gnD+YUbYrvoODRHYD0f4buK3mBW3kLznbnvjLwXudxbFa/8V4+5V2afngBWOr9q5PczFLZnNzNPAQCx4NerY28x6cHVgzt/PavA7L4eGOlrwvaA7iUNt8n4Bu3zNz6XZ08LQUWOuAEgLXAP83MhcDS+fC5xqwGJC3I19midixnE55D39wmPsjgy5MM/lEheuaNv/AFgL2q82ZsBROp1aXAj+DSzCI/FP+1Rf1H2RroCOa9bvFpJscPb1jz4UFfHxZfJwRg1NvMNp/g5R0Yh3+dp5PZy48t85un179u+vq3B9t7+e1HevUgq/5RJ8VrSsBZj+b3sQQkWDH72ANJ8YzGO5s9COyHNr8X3z+PL8g591EXX1HkK/W3IFofFt5r8LroPS+Z6faN8QEhtYutlf3gTHDoA5ABrc2++eb0b6YXjyltVg+4qn3+UeGPF5ChFkgZ6y1H39p8sBzg18dmbmkgUMvgQPD5WXXg3v/lAPAmpQkt0HoCMdgOtu0N5mAWglq+j+5gHMV9C/EQ3PJdG3G2G9/H7BXub7CVje+8FYqu0Z2ztVHfWW08IO9ZwV/mxiOaNZvVAg75CEDgu9vgkvtm0tOE2V9f543Z9DfL/nixN2uwcr9uDsTzRUE7xIa0rT3yOqTD+JD2WleyVpRUtk0k5dQYeUwSnKU7ktim0TqID5Ey8Dor5GmyZ5geJnzgIuO4zO/5MQ/TMYRMvtttZUPkj8xk4htn2uGYABm4DRFL2pIQPVMwrjRJxtKOI3cyo0MbVPhhvFXMeuUkBVtBo3pasRK0RV2Iq2LxKFNjilomxoxXq1mS12x7L4+1f4aPyPbObDOeiFAP8te1o5fLY2uWfHZCEpuVVYW5edDeHfxm5SBckvnhSTnolmXvrQiN9NGiDOqYJeKQ7tWilbRQsY/+uqe9m4dxicP09zHB61RpufVVlCt172xTQwmklPOpkTO5C6wY6lYnTezUHJcHoWUNLYo9fbB0jw6M+37a7u4TvHUaqdxA7Obi+FMNrQbZa9hKOcraOdW06ZLzQborAPMx10DYZicjLzTOtU8X0sOSuiX3J2TMvKWfrff1iTU7ijAJObuKeoP5eXzGOPVamdujsjbaFSnHuaghBp0bY+Sap2QImHNVHpucsXSORZObzcO3+x5D7IrX0f0p3pQKZZFGlScHOS0C0U9PxZpqbkalC3lAxSMpN3F1cY9MpMttXbtKw63acFBv23WCni5NhYvNBpc9mt7KWxzfDqtjxaXWWYBl+VaPjuxtwjEP1hrLs5xad2LUIQSbXL36WqtIOZSBtHNvLZXdtqdDw+gTsKwaJl5tyMOu8Y9XVFeRfHe8r6LD7nbEJ9akNvCWP6hBjMhjicieNSbjfjjAx1u17/WjwnjkdtgeI3MF85FgrAhxr942VxpFNIQNLAoiEvF4HOjlOR0BN58Q95i3a5qVT2FucyFfasSt2HINybsdWmlFeujx0709R5kmoDtEy0yyr0Z2eaKkvty7KibCXQPfwZodV7EQeoQLjW5snPXbgx5E2nFFHZMzNW3POyWA72hb+9QGVcx9udR6DRcuxHSXQnOS6OqIlexEZXtimR3DUNigRF9qtHzk1qikeNJ6szv2l5rW6QnJoVDCRVNCKr6R+jg2pbpaglrE98e+jo0THxkYcaCvdGiyWtte8jNL7jONzeskVLe5iR1CkTuMEnOQ0GZCcKJaDicxDWBeuePVEJww4cxZisj1mISOrH0eKjpTlaMWROcbnJGlIxww2pbLgytLbNDlVnNPlye2I3P5GI/qlsE2znKfCk2XTcJaECEjw2KYqnDeXrsuJyJinqdFqiL2Ea7CRLPaRFULU4uPWsZcSs65YBMNS4c1Ei43NxuLmWOxOYXxgWih226kcqBTa567Fer49h0L3aGY+LWjJKnRtzyqYituT1Z7ZmKdVKkxOWtVs6D9ndAzKlRfr5cRCslIV7TqVi9DJWVp+IoyzGnl++eJXHawUgw2ynRHp5rWBj8iGYGbDbzaSR6XC9WU483R0mlTYcpVvDw2ydQPxCrYHOH6frscj7s6KuqTGjOqR7KEKvne8liIfm2pItGJbB6uNgDqNPNi+j6vlPaQco5AR4epl/IyzEU72E6M3iOe34wXQlHRfq+Vw5HLkk2NC+ytDMWDywdUpYbW9TwpV1M4h/cMtuu+tpZjtj5j6+2dY6pSDjrHx9PjeZO7GUQfTrFFWlDc4HvRxRvuTEiqxEsni3T7S4dFcp5vNHHsV2cPCeDteBsgvJLUIdtFk0qxjr/EIopj3fowGjqU313mgJR7/1aQfEQgyVDt7fhCgaY7IsulPYijzEZTijEqvkyxgLnsVQ3L7Iza0ZRHUhVjwFdhZRiHK2yS5y203NA2RPnhFTkR+cHcyCNCXpYXvl2H8Uk0L4Ef3Gi6NNjMTgaFOgyErKi78VhyOptjRMmz7m7KGzFIY/NmEghrG9DFSmnWCLS4YJfkOgpJ4XymscbajzTiNDcLKeIdhzTYsXNbagjBAHBBjD6AxUHawph43ybr0qIu1TixUsi696KvYDVOsEEdoIIEMKlxTUlM590WklVpXF3spiARXaSFpQcV8JXHJb/yr83GlYjQb7eqeo/aK46vJJIt1J5sMxVai/Z54rWoOtYti+1lJYlPzVqSV4xwvuloJyu6AzFnh869rVBQBqSqIreU5eXWVGi1oUCNhyJchhp64dTwyEvCNQJAfY32+yy0S+Sk0YomXE1zs5Qv0nJ1p8UzCwBNWIqduKFu1xJtdcU0VoGhGzZScSc/MR3ESfMUL5OmvY9Vv7vRRR8eLDkUdfg2XKRuy8m2fLML2wkMVcbDbHDbDGL4+AJPEZUNG0Bxqb9PpvMxIkwZS/kjC/fVlTxkhu1u7qkb8d2BZJRygrjdDgRJqGX0kIdOkNz5a30u+qwU99KSdZ2AYWQS5i8XX7+5B5llAl1iszHWh4tK0GYR4Jx4tAq3yvrsJGPOeBs1htYi+3qMVSvbqMfVpmu3B+IUtY55ThmMJILytCT9eFjSitysitRIk6xv/UtAqPmoKTYbCI6uKClXmQFW0DLdJaog4/1ws7K2qJYry5lIarWuO94I1HCyqdNKv/m302jwYEMVCUNHrC5COBI0vtkkF9pk+Da27Bt0jA6SsSyqfdllBLHJA4QnD+suhAUyIjbYNstoWr3JvUQwZHnG4RNeJM5946SEL6+v1+AWnI1pnW2VdTIeiHxpYGokAnJSlAsW6riaMGa67q72JtLJyFyXBdEnlybhoUMh2IgmlXt51VuBW4FiQ5cuKQz9fsWUxTR050E5T31WVJuC4FXontQ05CubITh6WcdhqG3c9aCy+etJdlAdvl9Q+lSJZzo+l+mBVvGOb3biRRVwcTfoYnVSpxieFDJwbx6Bp+jIwTxX384y0sr9qCrdRWCD9oIFNLa7nbST5laDnqgGmVFnKtAsoHtsS/wy4LMgyODCgeWYxZXmWHg8aFNg2deaxFnlW7POJn/n5fywr66sgopKvw2QBKfJQDMiMwq1DBlNMPKoSLVuhUGgtVFLae6+bAk5KDyHO+apZzcQeqsqmJAYLiSPxu2Ksiccdje0uCINtHQZ+KI55yUD+VC8meTCRS/FOfQlmhxN31JXq9GuXBmzpMKVOlHeHApFwgO2L0DLyE96YnS5Pw0JC43VrTFPRHwubum1CWshMA4GXB9PWHWbzO2YTp3NrofRXKL4uNLvNI8OWkefzPt57wHojK4MnPI3b+IRyict4oDJ9u3UsRhBngMzh1sVTu7lKUFGwx4xyHatcOcGnBZfhz4q9rjoXPlIJsKNub9RmR3fdrQbXyZdTAR0vSxC/Cqd7F6V+mIUsnGLlj6v2zvToq0Vlbkx7XqbaipoUo98Srzd/T3XIqR2W20NOhBDJ6Jx4oYcPRd0Ck2spO2ZPVUYmRU3N8UpxwTA0hCb4kTxGKAChuqZdVYxbiifLyHCdulabGT6POnhUU3swDbPgdoLQUNIURyfMNFMWIPcXg6hMZ4mFrRxXrIiif0tqQsM4fVINRMGq/g1zN5jyBKTrhwY3kUNuAWdGuYw1VI4rt3rktFadUlWmyU8KuYh12Xc3k/YwbSrtX/O11k7RjrGtnwTQC1/cz1k3atL7+gwoNmIxmKbdPwSCU9ejx0So3Zs0PYgRYEm1/iAo1lI3MdzfpAYZKouBJtLeyGRDTCQy556Q8vbnrQZ42JcM5piQ4xmOdgQpytXC3c3vtdsV/QneOtx1OmyDkTQQZuaWbFRwFYiujRt+2BZx8t6wyrHMDrA5GBcZWVsNoiabbYdFmo0PGWSaK9YBi2a7DotJ/MSWef8BOiTNqipW4+UzHEb1KWpyt0XUoRMI6NcyjWhi9T5AOeHjZwl/qS4ELtaA1TfhFF2z/LMcysYV3zHg9H7rhk15AQpO1k9RvJFX5EKlRXwqOJBXl7BgOFf1lRgnieaqsnJxPIWpeHc5nsmI9rLLjaa+BAiAyfniZCI+z2VCLgtKtl6m/LVuD9Lss9fPJ0iwbhzbBVm3cknviePyq40seXZGrzrrjez5LTa3A+iD7GuXtSlU/qslSThNUzae6JdSVuGqV7i9t3kHJoyFowIHSrQtk3TBpaQHbwZWby+lgrdjv4kc2AgJY61DYrJy/dAWEgyjmsI8LKJlxFG0sYGPqW7UWVgPjh1a8TgCvqKOA5zmLx8R4V7EDcPE0icIVVEiCklPuNcnHm94BouXUi3eyLaSrgLYwtMSXbUFuKIX2DXVolLBDvYssFqiSvcBJUEfiKbTc4jBESrQmnU1ZTQ1eW+LybLqNsAJdysJGI/dfKrNTgAfcDcVp95nnPlsYraShvNbR44UZlF/k3UOsnBb67iQfAEyM+LunbA7sgZOqNgFpJWPt3b3AY6mbfWvtP3dY2XErpxVrEucRRu8zvH5Tw07voNM9zv3V1cg+Flcl14Q1q5d12xgoklpbWL7P1hHSxP8diHPXW2urJY72NsU3U6xd5POYSOyZbcuSJt47h1u+ytFif9im1JmFq61/4MXUP8wrGXgEqVZsKsvAzI49iielqbO/5cjfhteTmAmdliVU1CxeWGwnAUFcVdLY8YKR3V+AbGOEi4n5Bdi1962A3vpKzHZYZC+2DX4NDB9yHc9htFG5TELKV8o0P7C3VgUK/tNOysIRPtbRi5PGqIW10wvRz5c3yXEzfPLs4auglHrIAKVT7fmbWdoO1OYQ6FramH5RAsiSYZRFvKY32lmpNhtRuTtabz5Fdk5OCr/Z1E4H1tRsvBNLmgQJbbk3PG4thmNAGIdzS7h45Vtha01emSlvbqeCJNgqrX/g5b6bqel3eG0rCBmqDAst0z6MAaiTLLu1Ap2m15GGHN33GrCdmr3V3Q8NO4tnbdia32CnyiU0uCy9POl6oBneh0SF16AN1xRLJ4R4ftbrM+Tc10j5gMzFtgcL0eThtTZJrsJNmS2rr6uE6pwiyHS2BdVxY37WNuug+baeTGKU4Mzs/O6WSDafkwbvU8JFYoydSqyZ3oQ86uhRgWpmqk8NYJrrTEnQx95ddRGFNRqXTmAVWzGIBmzw3JxeDCI3OyvXNtCHubmuRrHGmSLcqjI9npbmvCiliLiX4fEV/ik3YLIb67wwteRaOAOHc253U2fBxK06O3XHVb2ULv9yK97rrqQkMXwx1Vm+JXy2mtLnepLDiIf9JVV7raXd1cqRVz0ehkTyvOdNiu2CLLroiMasRmNMiJup87dWThRguXxsYS7kkZ3+6ooKzZPcvlgCO3DHy6k+0qPN9ua0EYgGsiUEAlj+ej7HQ4nIY7g+Czu7CBrzriXRmk2FMcrFkYex12U1vpB8MKh0rwww1/TDdnnd/H5xVhRBXJF5SIQg0HMgPqYihh7GNFHcZ9AHUOmA6uNsLLd91EQiQLlbtBwOP2HnBMrOwEC4HMnPUvWeuO23LK7Uw8xTlqYGsXDIPD1j0yqdHZSO8ghZ2wSrNWtsi+D+FwIiTNd5DW3LpOu1/tdzekxSi2VbgRvuviciWvtycDa49nLWL1SgO4F9b9+ayjU7aN9Qy93xSEi4mqOzvr6TCV3mbKTzktd4LudXsFYq/eNhtE8XJnhIBPEkw5W5dyX9Ne7MddwvSnu1hm+tWPoniJryiStakyNLZg0HUKOMYyKZiopXXLK5YSpPXhKnY1rhpUKBfb63JUpgK7C6dqN8K+7O33TALdEo1b+o2OqfY2PJipIdy5hhnPyN7M7yKWCSOEVneD2l733jLI5P2ZtMdtpxqXK7OmGxu0JjtV2RrdEIrxKd4yV06Nl8u7vobuk2+18Qkao2Sncandwd0E2MujUx6tFTZcGfDqWo+Y7ZZaFnNai9hgPatvoB5prmXJWQNC442Dmv7ebA0LoVUTt8O7oZF9jS9hznI9/HTjhNbdIkcjW0cWVDP4cFUCxNwfrlBs9fZwX2OJS9ibncGLyZ2BCZY3dsde79L+JEZQ1CJuSdtdS6uyHnDbYRi5zpsmJ4xvW2uJXFJ829oX6bbPzj6sMLROYVCo8fISc/HlYHgCVOKDwy2rw0iMA1kSy5GcekoVaaXyIeiO3u821B+u5Gl1ldbnKnTaZn2ia9vVT+XE55eVk93vpb0Zr4Ql1Zs67SqXd0esvBSCB5rslUs5WFzl51G3uFBpubDqFV3etBW+wtSthLQ56Q2isT+26EYZ0bt/gWLD4P1kVFCBgK/HXEC7Zt3GvW/pR3zXW6g4bIj9kRjGERcOyoFH4iILPCvctj0dwKcVGcHiCEZ6TECdoVgPkgkFTNlIuset15tt6dowAZFxZfGGVSkQty72tUTFy7aoN/byXG712xLcBQlUaZMHXXSx4aAJ8yGbgVDQNIG2PtxRGxJMY+cBHxkShteeq3Xb8LQue+3owkjtlOccws60m6NXJ/Rv05JN7M2k1pp6772aWlWs352r7dl1GgHv60HfiX2bxwJRs8DxBRG22aW3+BUbTW67zTRvuVpqreK0h0ilFVwQw8M14KvbZSnA/U0h2OOmOjSRBKPNRtLD/up6gjsixiiQw4q4YzZhtsTuwLEkjEtU4hPm/rw9D/w2DDqxovUVFrbKNtqAcQzSCPwkOcZqt+63Kw/MkI13GUP0Grfm+q435up4HfcDH7K5q1aHynADA8ZcsnduoN8AxAZlPlP2HEag7rCsztbm0KCcqvPl7WpBWB5sCEYnG2tJDZebFi2Fcb3eQ70MkxjTgTGYIIi//e3lw8v8kPTtUee/+c2r+ZnL/7PHO8+nNO/fong88/Ms99PjrE//rmK/fXipnQio9Xyc1aRd8PZI6O8eZn381x6dzzLG5xeb3h/mPp8Rt1YwfwH4Jcrdrmnr8UtTpI/vU4AddtfMXxdsZjUd8Pv7B5h/Z9DbI80vbfFm0/w8K8rnL0t4bmS17x+Dtwd9H17ct6/6fFltsC9eXc4mvz2QB5auXuHX1cuf/xvf4nlqzC0AAA== -->
