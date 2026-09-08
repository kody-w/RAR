---
name: "rar-cowork-cookbook-scheduled-brief-plan-budgets"
description: "Builds a morning brief on plan budgets from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Teams-re"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_budgets", "rar_sha256": "16f029116eb5b6aba86f2e9114dc4fc1a9540919e31be4144b72f79f7e98545e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_plan_budgets`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_plan_budgets_agent.py` and in the RCI capsule.

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

Plan budgets Scheduled Email Brief — Builds a morning brief on plan budgets from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Teams-re

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-budgets
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
      "description": "Dynamics 365 legal entity to query; defaults to USMF.",
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
      "description": "Responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "When to run, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_plan_budgets_agent.py` and embedded as the fenced Python below (sha256 16f029116eb5b6ab…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_plan_budgets_agent.py` first:

```bash
python3 scheduled_brief_plan_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_plan_budgets_agent.py   # or on stdin
python3 scheduled_brief_plan_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan budgets Scheduled Email Brief — Builds a morning brief on plan budgets from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Teams-re

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_plan_budgets',
    "version": '3.0.3',
    "display_name": 'Plan budgets Scheduled Email Brief',
    "description": 'Builds a morning brief on plan budgets from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Teams-re',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'scheduled-brief-plan-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-plan-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0e46c6cf1cf197b1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/plan-budgets'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/scheduled-brief-plan-budgets', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where plan budgets stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on plan budgets for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads plan budgets, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on plan budgets from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Teams-re', 'example_request': 'Give me the plan budgets morning brief for USMF and draft it to the owner, weekdays at 7am.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a recurring daily or weekly plan-budget brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefPlanBudgets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPlanBudgets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefPlanBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adOjRrbmX9G894PtS9ULiL1udMQghEBIIECIRS5HmR3EKjYJPP7vk0iqst1d3fd2xHwaVVRIQObJsz7PyTf57c3tu6Rq3j69HUO3XAhunqdJ2CzcMlhw1a1qMvBVZR74v/CrsmtSr++qpn378BaErd+kdZdWJZi+6tM8aBfuoqiaMi3jhdekYbSoykWdA8FeH8Rh1y6ipioW67F0i9RvFxhJLHhdXfyYh7GbL8KyS7txcTrKm58Wt7RLFl1VL4hF2oVFu/DGRVrUrt99ANpVhZunYbsY2kWXhAvqY+COi6YC2oOl3SFs3Dj88LCiDO/dAswCarYf5sHlogUDZlWDxo26RVi4aQ5WegiqbiWwvs77+bkRukX7sQmBseHdLeo8bN8+/fzLhzegR/726bc3P3fbdvadn4RBn4fBajZaBQavnvaCmeAiBkPqEfi5BNd12ERVU4BbAfDP6+rHNsyjD4v//M/s5jZx+9Onz+Xi9fn8Nv/T+/KhX1e5bRcGC9+tXS/NgbveF2x+c8d20YRd35Sz3i0IUxm/P2f+IQn48m/zsx+fi7wDBX/8/FYBFdzZO5/fflpUDViv6eff77OU+sef3vPqFjY//vSHnLb3LqHfzcKA1u9fXtcvsWDgH0PTaPHlqPLca60m9NM6BML/ZN/8ear+EvdyyZfn4B+r+sPi+5Jne/4G9H0mogfkfl8s8AGY+fZ+qdLyx9caTTWEpVv64Y8//TOxIKZ+lqdt9z+S+/NTcBK6AfDWyyU/fXiE75cF9LLtm8x/vuxcLv+OJWD41+W+OeqfyX5E9u9Eg4oBxfA1lt8V970J0N8WP/9T2/7VhA+L6PPbOszTuUi9PPy0+O2RIj//EPxx84dffgei/1sxx6pv/IeEL4VbplHYdl++/PxD+7j9wy8//9DXIItBFX/pm/x7Mr/n18c6f/Hga9SPf50L1j+VWQkQY/Gthha/VfX/an5/X5gAnoI/7refFn+uxPkDLWYjvi76dMGfqrEFuv7Jjz+9/Q5gpwTW9E8oA/jxH/+xkFO/qdoKoNjRr/puAQLcpUU4K28kabtIn/DYhMCvbQoc+xoH8n+O8KxxFS1+/d/+A+o/+i+oh9uvgPblAeOPtPjywvBf3xfGjJRNGqclQG2dVdXPJcDbspvXq5uwDZsBYJQ3duFHUMof5x+LtFz8+q/EfnlIeK/HXx+wnT7xTue2M9a1YNL7bJU14/fTBh/QSngP/R4IzysfaBKlAKE/AGvbKh8AVs4eaLM0zxdBCtAE8Nb4kA289GkW9uuvv3pum3wun+CMLZ6E1sJgwDd1Fh8/ApOiPI2T7nMZ+km1+OG3339Y/J/Fv5r1ED6voQKGeMUAaCgdD8oC1FRfgGEgPCCgADAeMfjt95djgZiZg0DE0mimuHkyyMksDL56+SiyH5cEufBC4N1wZsWq6WbiS7v3xTZafNMXLDo/mjkhqdpuEYR1WAZh6Y9AqgvM+ebJsuoALXZpG40fFn0bPlb91Wvch4oFKG63+3UhcypgoOrBls2LkcDkqkyB+7/lwPM+ENL80C5WX0W8L5Q5Cxe127h10rivNSL3GRfAPF+nA+EuoO3b53Lm2XB21aMknu4Bg4Bn/FdIP84xB51JAeo/aL+u/RjjzjxpPPiy+Vy2r3R3mzkUPoB/sGjcp8FMAv/1Sqk2qfo8ePgPaDpLekUheEXlkYPqnxuab9S/4B99xKMDWHzulwiKL/5/bopmT7CCoPMCa/DrBa8YuvOM0NwnzpF8tpaz8iBNn9X4R9vyFZq+IvTnMk9BujXjfz1HPuL6GvNEvb4BTtZZ/SEfJBVQaZb7yPk5h5tmtt39XH6lAmDq4oF7wN8AIEABzQZ9XXB++lXTBKDAfP1HW/DIkSaYnQXyelH3Xg5yLgrDwHP9DGjVzHX7CjMogHCu4VuS+slfrJqjB/IMyJ+DnoJYA1++f4Pn59Ovqv9l4rP7mac8OsMelG3zEAD0CGcF5zDO6QDU655tObDz00MIMKOou9l2DxRO8eF1M2zCa5+2IHGeMQd+DWsAzh/n76el893wXoNaAc4CFVH3wLuPGppTqAC9DdABwAgoqSItAdcDp7yc8BDoFjMgAMB9NaNPiY/bL4PCR+HNJPV14mzIPGfm/WcpuOX4Z9wwvpcmQF4xj3is+/eZ9m21WfaMnS3AP7Di16fPBuH9yfHPJmLxVe6nf9j3/PjvbY0erH36awJ8WiRdV7efYPjJtF+J9h0gF/zUtf2DdD8+YOLjjBEfXxjxF5lPcz8t/j29/iLiVRefFug78o7Mj/avvHp9gBu4jyvnIz4//Vzq4R+YCpYHSNPNmJ+PMwJ9JcCvQwALxg0ALzD4SYjtzKM3gDIPBgAR+Fz+OdHnQgMEU8ZzYrbVnwDg0QmApH8G7BtRgUdlB9YO5n4xDt/nbdasfhu+fSr7PP/wBrA0/G82ZjMRFXMmt/NWDtQMaL26NHxcPYDh3s0//7rNPTx+uPn7Yh0CEMrbP2fbiz5m+vxTUTwNBIb5YIUPiwC4pZ3pDhg4Lz4XlNuCDAXJORvSjfWs+XMPN3d9Dxr48qSBf1ToL7TxF8YAWHftwxlQwUbT7XPgRnBr5pHvLvOt8/zHNSxA/vPcoPo08+CHF8B8eLDYh8W3xh8Y99qKzSuEZQ92uT/Pm47Z248p8w8wB3x9m/TtLwle+PbL9/SayecfddLDtgbk9ehpn/x0A50Z8HWYDi8sfTAZyNcnlz1q6ruWf6277xkOiPHZ63xYhO/x++IWhtnMqi9CB3zTLSi3+I5cIPiBt4C1Zi/84d4/jKwe26xZBeCU7vlXgd/eQE66IEncV1a++nQwHMDTx3buU2BQtGBBcP0sL/Ds3+rgX3PbxAVdJJiMkhGyZFCUDD3CI13PpcloGYIbeODjkY+6DIEjDMqEGOqFOIrjHrWMKCaiQoYmcGL++8izQL/MjVg66zMrA9zwEdT4nx6DW8HLkKfis5e+bRhmg1/2/PbmkTgYKeLtln1+OJiZV4e9e2PDNsGkY9z5Rxfjg/ONvJ2tIWUuTWcJsRFPnqtv2tW5SnVGyiDtKmJ762bt2KiqoVtJHmF/ed6uj/k1gBAkOuo3fIMdJimbCJinLvecKi8BmeHHs6XYdz0/u8O2X8pX3BCcflI2RyncONdeP8MwNET3veJKHm9Vp8sk5+pZv97xnczwuC45OZZdyx4a5Y2lb3IGYk6pP9jIRapKP9kWmuVa1zK6QFjY2idMyK/XZUVnW5q/Xo9X3W1Kc1XzJ880tvq5rFwpy2uAupuujhJSrHzqFJ4lLe/FnNrKCrEv7sedIY79yjw2KrO9FWdEurAN7+aQQPK1pJ56U97t4d2ZLSz3XsN7WjlNSEsIF5SBon239PuSoqEwpZQBo2DmpkeDbJS79lbRKcX1XZlLzQ6e+OJ42uQbJ+F6E1kHubW77e3zKT7wzekaT3vMkiffRY7L07RK1tcrmezTKBqQ/VlWN9Fmfd7YeYr6Jif5uWjc/NoSCjTfGQdWOzTihs1CQ1+Z3kWW0aWiNLdew9C8xIdxuB/PBW8dTXG345gL32lbDOrMKt3d84sUJgG/CdndplAsj9ALvr2fbetudgfIT5rziaoybGd27P18SFW9h+tAcFvcK6b1um+0bssV7r2sWiK1ImlsOU5SzG0o+HzV7OpjYzVHfCvVsQoh18NFu1KrI+nfoXxn01fTcdFie1rb5c5pKHcK80FNJSZf0XvBPGmnnLB1bZkMLbO2z+K5FjYyvE0cs5Fk0/Vuh3BvyBR/S3xvLbFiiWyEQodQO7xrUlI63JrPQ12dDFhkN2tPDRImO4jxwYyv4qnYrKNdxja1VtDnAOqX9XKrcBOjVV136Zbu6YzZ56OWhKMY0g6UVl6l1XBu2jkVN/A9TSJ4Q0hL3qJwPlpW+5uubuBEG4X7mbb7qnZFKkKjhPN2/RXZ9kaGx7ZeuoEI2XVqbU4lFAvywZVXmMzFVLZhiTA7hDUXrWp7H9sNGw93sAYb4ZyuohXVDsxqtYum8wTLEQ6vELMnMptrs8ONtW6KUglN26eHE2IKdZpdI2Vz4Py9XLMm51xWzD08IPYBi7mk4eujTWXWxSZOlKa0t+W58vFAIaNLtj15qs/jbToOiXzWzEJsrK3or4ZmYvf9ZSvEvspeeB7jmSpTcEmmEWblcTv6kBZrmZKm9K5M6oXduBIS8ZieRpOe5pSuHdt0y554M9lcDmi6QyQXHi0eEuxJBTmAYMFKg6c+U7g+510n76/D4RQj+uRaxi5ilE3Xo3mU6IWKQmaS+9qyWcYn0rhf6PtFvtvdyeVPYsOuYge3YPLcc1oEYlAY+Dm+jVeVS/Ls7NOGdeL9tWTJh7JgbkiLhbhu0ZmYibd4XO7obnffFHtYGu9IMOWl0Q6EIZp7nhur3NI4rd1UjWBEl4sM5ehWlPd9sR2Z846LS3wat1VKERRGrO4leeea4/7in8kAusCpofdUpIqrVePEZsktyfhArzeEvUkt54DflrysXJj86qSpZcWJ1yxvJU/ouNvKCr2uN8JmZBVY793dJAHqz5ya7GiSiFqkWIfQrrgnK2dJqyhj+cM5aid5fdeUi91Dhwvpo1gSTjgrnLtzriXKEFtn7HQ8RBoXoUnnBUkXrjkIDqmJTByJQ1gklMkQz4xkh2SnbE3e1ItmHbjkXrM5F5pZ2wiTNbGtfltbDOTKypAZIAUQVL1TbLgyfJ33aPXoiJmTIMla2B58UTCv25IO26lgosEOFabwDUfKUtbYjcKx9Y7VRC79Id9vqrpT9iZzzYjlyhOWbaaxDbGWT6if3HX04p5jPjZ6iLksRdaSmH3Lbo/WQUWWNZ2c2CPvraI4vO1YfR1pdDAc6VtIoelgNawteym2Les7xpTkeIxEk+N8TBJRKChLjKLaO3uqxUvJcseJVHbKrrk5N4JWSfbmiMzd2p7KyZ5g/bbUekxsq22bnDesShwgOG3IHZrD8QQzzBA13LI2A2Jv4RPXwmZxX8Xr9TYvbwG2v235EZGOikk27pa82t7lfhSvUr4yXIJe9fLOT250GF1MmBYuEL0SleOh3fmYyUrYersdVu2GZ4ZMrA61hBunuqu0LZ/sRLkK+HF1F9aAeJpSibW2tLKTF59LzULOxu5yR6TDoR8J5bzlu9UJ1YQVlN6xGL4ylUls8kMjNMHAps1eQwJZZClny3FJMSHJqQIqiOhhK7l0acjxyZL96GaK+GTwdQ0X16Auj6IqI5uGdJoRFuv2doH2m2h74PkhvXGalwyDJ9n0xFOhdpKN2qDzQJHc2LkeCtzYsRrqoKJFR4YAuSf+grJL/biNUJUxV4pZnfLRr+w9eqyvWMank9zD6EE5VvY1S7JdPzpOU9RbQcuv+pXLCH/H69FILCvXPAqGicuJkEXFOtsTnN2rd1mUzvSpypwzurGQVmVq/HJKTlftvKeaa33Jnd6QALZoAb7VWZUrts3RbFf2cron1+3OdmJln54F2e8JRvfGo3Oyzyh+vRUCxpZ1fq20C01i2UVIt7ZnLX2vtze74NzopjIRYng6r11aSEAJU9n5cnLivufQutImyIOMIucgzmrNCboYJ7gas4S+pP76dkijBjbcwe6P7JI6jPpWXOfbW8rErbXXm824ddfs7lRmAyntnFvNgD4qLZINAIFgIm3Y3daqjLIJsoHEmEY5Q0ig+06QaeOoOx3UFtucsR39BNX9XlUopUEI57YVznZdXyBoV7d7Plk1RbHakxNWwBcU0m7etZLzrYR5NHGYJmTCzBaqi2YlXyhVJnQJMxDNaiPfv67Oy2lc3o2VzJcCmXGrra0NFYIE3e5c5Ll6SvHLjXNRDdDCrmh9vqBwyOHGK3UveEkQmnikz13IFWWiOQQGOCZkhM5CKZqiBgMd45YTwD76JKGRxqsa4exkUyZuw5HUd6OtCsxVvMnuYV0R3mmahkmtWba2/d3WpsJN65F6xx1XFGhsV+ejebK7PZmeCS6EOWdw8RoKzBuGTwxMq5O6qw251LzwxMh0KY7xCdAYZEx8o9N6zuHEptapjBo10Kk4FgSj58u+EmnmjBtwYk07/kYMAdik5MfU7ba1zAq5D5Uc09fb4rDV8uOlNaxsBO22Qt8Zsy3US9r7WYz5jtxeY/eu8emJaTG54JWlmfGXwknrKu63rOyvZTK7hvyJjDvFLwSo969o7ERLkkmM+qYJw3qnqaPncNKmcNWaTzxeZzdWrR+EDmVtvtrF6vlU2zduukuBlTPmtvfTTXeCzmOv2kFc77ewlO+k5Y09+iTPAOrppf0YZ/XVopH1BTSZSiQJXOUqV2KNGHzeMgpbp3kpe6ecEo4uqrD39eEs1EPLq0ocT7nk3ISwFsnr8kQLJNizEI3GGZ6CbdrjTSDkFW3aiV9sRsfanp00OHZ8seLOpXfZ0mCzHjFHvg7vy62YXs8Jj3B2Eu8PWOQqG4XitpZXob53CA6qL3Awcvf7+CDlZR+xeRS5xLbMjKbCugTFHc8roV2cT4cpsM2tWum3MAvF62EpMtnkbUho3O3yi3OIs5IlsWRgTRPEKmOsk0XtMU/XlQr0OT5RHzty7yns1vUlequyJJKm3snYSSolhBUFSb5/aNVEiSFnR2pOfjeWaIfQzJGQzXNQjznql1a36xQ9iZOWwYGl51xeHaqrWyRD76DJsh8ynU2mg0ZyIodayZpZNqbZFUvnYjOa7XQEJIvivdjSxiHnzLH1UFvbtK2qy4zTV7FiNEp+iHMOjjwhuVylaLnsTZQ759V1qIl4Ck++qPsXe3dbQ46t4ggM0O5QOVVD1IQ9nC07LSmxbTB7Ge3P+QGBKwBGMTu1gCSl4FzfzHwzXE+S7uMZnyF3UlX6EqsE1B6uIX7Rofygo9Qu7IDn9gpylQHej76P99weZ+0Eocpso+2CJL2uleUEOxDYbByLWq1PgLjlpM30dMOpJ+EgITGE69Q07C4orAi4eHS2AAp2XYGdLyWM7s2eYya245NMs7LrZVn7rC0cjXtP+Rp23mjirtxOPHbOOjOIXE8JKIPWr6YWqi4q3RjHBr7dRX55S5As9vuj3VLw9u5XSrkmVub6vqYTDVtXnVEKayMDyXE4rxXQwlhkfcGxLG3PKnkEWURlpDGagYGSGyEI+QOPBn4hDW0c7p3hIpFHFj8mN1naK9a6F8O1htLrLd8fCLDDG4+CZ7QbaD84BDFY3D3Po8pmr+FgXujUiFPdt6LlOd/nWGCVSSBby1Q6+qAtNNZNhB3FcaVvAnnCJ8+I3E17RSHVh9dWfthPTHVFc/Kelpg3BL5KR3noeWs5aOtrR2qhuDSv6rq2ziaDucO60K5kfujbA0NSFsb3MA1RcdtAo0/ZlgWlMhMEd/MkY9i+nixGOJzIfM/gLUEyB0/0yVjaCFbuAYi3+guLrPHa6vM6vWGBMVHOjqGhPlhR8ir0nIzoFCG6asFqZ0KQvF073VAnOuBWIygkh7mmCKF51hmFvJYn77ttxw7QObZWsUAGB4BTenWC6XPLspSBppMYbhp9T+Y92Q5KTrk4VmdkGdE2dSk2qFpWREvD4hDBbQNXaWew1ahFahPRp2gFte2h6y28NU1LIJEYK3hED0b9bpf3vTINeh4EuuFXsClLRA5r1+wceshS2kT9bY1XnrXbQkQMsX5W9y5cGjZ2PE8CKHa37syCOGy4e2hJFz0LGdCladi4K5Nsr/THqVyXsn9x4rtMSw4+oHBedQ2y9NrExfK1nm9j7QaKT7UxLOoUp8VjDh2cQ09T8jkfd/tEPuWXK29kEbc/5Ih67GhURbByzKse6oWLm41higZCQggJnAf2mDOWenCcaFPqdxXfZNq2yW6BMgxCHgWFC21Hh2tB7FcVIMoNtD3LVrgMG9ctc2K30aYGFVa1EYyXQimClrkEQxZ0g7i98bBCVha22dMGsezUVADUIp2y48kS7qKEnNXM6/NwT6I77iazfn0N+kjcKAeXy6/0uNmjsgiLaqp4QnHbZWnFozSu3xwJEpfxWeTbUPbZPmCVDUN544Vqr8cQBolDH9aJxsDYpEH8cuw36Jb2cMSclFYgqilgm8NyJdrybaCjdVvQ12kPNyd+iZNjcA0GkmCmY0rez9BUpCRdUf3UmkebD6wJ7BOcwi06dATdQwHtjXzLte2W6Eyl7UfjAllJ75AkaMX7ZtVTlo4kU38cFVqAQhrkMhe2Q7wfSthGN1eSQWBkbXp4ZXmau0QZPF4XQ7ccRwoOMY64NTFH7UMGQO5YUKdCc/yUyoUtdTjgXriOSSfUFNZkKY1mDht/KTmsWlzgJajULN+f11WAhXyVkBKZ+/ZYjchtYim7ZUOHGYhuHRNQu5soW9zr+/IQTd1INoAZd3azdDw82vfoRHXCxNO2TOKKPQZ3tWpxkSEownJ3hCYOcm8yNgUtPVEUMRm1KTZPtAofQ5kYendLhzm1RPIHznBmATsVGlpxHaKUFQYKSa5M8SgJBYkTDCHsmtYXmlQqp1hNsVqNKiw/0ZCXILhCZziPaG4jjazLoRzXMqPSy7ccNKrEWEEEI+MNPOwnluuSk+pHmXXf7YIdJK0RAVdVX974e3xL5JxBIPBuualkJLi60o5A7C61PPfuioQolnwGbzKrtIdxwmulwwuZa+hynafWqra7xlyux+huB/eIQlU7XqsI60qUsfe1ID5zJCutAyVKEwp0ZfeEFLaTulezY0wfVK+GoP2BEZY8nOfHUFwdu8G1TYKu+qW5FUzxol2wxj5d7iEgbZDJcakQLmkGwrK7lh6TmWkWxJTdO+fsAsF7Z1pfDVs6nI3KX+ox1a/P2ZIgywFis7QI28Bt28k3lyG1pMuTHhPypXDhy5Xwpui+d+hscJS0dTXYuK06UMMy14Etq46D3i+sI0d00IzuivsxzLBQEA9RiJ5OYU+paBOAVGqgUMy4MyiSBGvrNg5glzqKGDwgiKeOdr4pDX9dpXKmykdXU7dxQN/aC0uGEfiQKEoddbe8ukGMXAkC8WJHufTogO7LvMeWVKcGJ1up7RWBd8seJkzERb0i78NwvCw3HhIbiXT19rvAsVTAcCwKUNzpuysXYaLn0oOQMhf6JhwnChX3JEUuewmOg/EobXbu6lYYK70LqBbbqMW9HyXqYvoaqGWajbvpzm9XuzZAbjzVYC2lgf0p5hf7Gyz1pTfduxE12CsUhbyXJ0SE4HbSHJhljK9AcPObdbt3YPtraKp1EG0i1G2Eoj0bi1SaPucM2lewQHWriMApaJ/DUEYtKY9SYIdeByFMrdYOnBIlwiIjCbY5PXVZ4cHN2nl1Y+FTNUS5sg5KWuLv0TDQgCaaXrFa1Ishugz9hpkGbNOVWWtZm1CCiavQ+cAh3H65ZOiwFsQl17BuJJu7/fLak4oXwFmn0MuaO+s9xFr3Lc+u0d0dLpV2c9JYXfV0MZPgzMR0yu/JZKJd0tiU+/SwQmXIAj46upmRVmRfMppaS3zfbYhMGe/DIWWxcnXpqu4GwVRAC87aCuP70OQldmitNbOlxVzvK/uI3JOWHqF0mYlZlGyG8HjlO6epdETS1zhkJrZ9gCG1j+ITffHj8IAPumqR/HC4Gru4Za+XiF5hkIHHOFdj0Grd0ycDJ0sDMWhWQeC1CDpy8Pnb24e3+Xz0dcr5P3qtaj6F+X924PM8t/n6ssTjlC90g0+PtT79z9T55cNb46ezMo/DrDbv49fR0N8dZX38V+fi88zx+YbS1yPb5wFw58bzy7pvaRn0bdeMX9oqf7wiAWZ4fTu/49fOr4H64PvPx5N/p/x8VPY4v/3SVV+eb1O9zS/izS9AhAHY/Iavy/h1uvfhLXidyH7BSOJL2NSzpa/jdmAg9o68Y2+//19mnfKweS0AAA== -->
