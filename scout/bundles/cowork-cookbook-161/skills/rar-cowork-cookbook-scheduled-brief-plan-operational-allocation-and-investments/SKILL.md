---
name: "rar-cowork-cookbook-scheduled-brief-plan-operational-allocation-and-investments"
description: "Builds a morning brief on plan operational allocation and investments from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and recommended next actions, then drafts an ema"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_operational_allocation_and_investments", "rar_sha256": "30caf084dac89485ffcba44b67131626d3a29b04cfdf7ea23af3c94a9a943f68", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_plan_operational_allocation_and_investments`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_plan_operational_allocation_and_investments_agent.py` and in the RCI capsule.

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

Plan operational allocation and investments Scheduled Email Brief — Builds a morning brief on plan operational allocation and investments from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and recommended next actions, then drafts an ema

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-operational-allocation-and-investments
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
      "description": "The responsible owner who receives the drafted email brief.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_plan_operational_allocation_and_investments_agent.py` and embedded as the fenced Python below (sha256 30caf084dac89485…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_plan_operational_allocation_and_investments_agent.py` first:

```bash
python3 scheduled_brief_plan_operational_allocation_and_investments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_plan_operational_allocation_and_investments_agent.py   # or on stdin
python3 scheduled_brief_plan_operational_allocation_and_investments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan operational allocation and investments Scheduled Email Brief — Builds a morning brief on plan operational allocation and investments from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and recommended next actions, then drafts an ema

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-operational-allocation-and-investments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_plan_operational_allocation_and_investments',
    "version": '3.0.3',
    "display_name": 'Plan operational allocation and investments Scheduled Email Brief',
    "description": 'Builds a morning brief on plan operational allocation and investments from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and recommended next actions, then drafts an ema',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-plan-operational-allocation-and-investments',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-plan-operational-allocation-and-investments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '29b1f0d93bafc821',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/plan-operational-allocation-and-investments'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/scheduled-brief-plan-operational-allocation-and-investments', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; defaults to USMF.', 'owner': 'The responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where plan operational allocation and investments stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on plan operational allocation and investments for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan operational allocation and investments, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on plan operational allocation and investments from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and recommended next actions, then drafts an ema', 'example_request': 'Give me the morning brief on plan operational allocation and investments for USMF and draft it to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'The responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly allocation/investment brief for the responsible owner from D365 F&SCM, drafted as email and a Teams post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefPlanOperationalAllocationAndInvestments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPlanOperationalAllocationAndInvestments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'The responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefPlanOperationalAllocationAndInvestments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916Z7PbVrblX+Hc98H2o3QRGaCprhpkgEQiIkmrS0YkQORM0NP/fQ5IKrjb/Wa6Xn8aSva9BM7Zea+1j4Df39y+i8vm7dObEbrFgnezLInDZuEWwYIux7JJwY8y9cB/C78suibx+q5s2rcPb0HY+k1SdUlZgO1Un2RBu3AXedkUSXFZeE0SRouyWFQZEFxWYePOS91sAXSU/uPLQ01SDGHb5WHRtYuoKfMFMxVunvjtAluvFqyuLX7OwgvYB1Yk3bSwDJn75dOiK6vFapF0Yd4uvGmR5JXrdx+AxDJ3syRsF0O72HwM3GnRlMApYJE7ABsu4YeH1ib0yxwoDcJgUYS3bgF2A4vaD4suDotF0LgRsAdYHuYucDa8uXmVhe3bp1//+uENKMvePv3+5mdu286x8+Mw6LMwoGanNeCw+t1f8pu7ZBGI350FUsHCC9heTSAHBfgONkVlk4NLAYjd69vPbZhFHxb/+Z/p6DaX9pdPn4vF6/P5bf6j98VsNIiI23bAHd+tXC/JQKzeF2Q2ulMLvO36ppjT04IUFpf3587vkkAw/zLf+/mp5P0Sdj9/fvuWtc9vvyzKBuhr+vn391lK9fMv71k5hs3Pv3yX0/beNfS7WRiw+v3L6/tLLFj4fWkSLb4YGku/dIGEJFUIhP/g3/x5mv4S9wrJl+fin8vqw+LPJc/+/AXY+yxSD8j9c7EgBmDn2/u1TIqfXzqacggLt/DDn3/5Z2JBvv00S9ru/0nur0/BcegGIFqvkPzy4ZG+vy6WL9++yfznaudW+lc8Acu/qvsWqH8m+5HZvxMN2gY00tdc/qm4P9uw/Mvi13/q23+14cMi+vzGhFkyd6qXhZ8Wvz9K5Nefgu8Xf/rr34Do/6sYo+wb/yHhS+4WSQTa7suXX39qH5d/+uuvP/UVqOLQzb/0TfZnMv8srg89f4jga9XPf9wL9FtFWpTjD8i3+L2s/kfzt/eFDfAp+H69/bT4sRPnz3IxO/FV6TMEP3RjC2z9IY6/vP0NQFIBvOmfGAbw4z/+YyEnflO2ZdQtDL/suwVIcJfk4Wy8GSftAvydUaMJQVzbBAT2tQ7U/5zh2eIyWvz2v/wHDXz0XzQAtV/B7ssD4h9l8eUHfP/yHd+/AKT98gO+//a+MIHKskkuycwEOqlpnwuAyUU3m1M1YRs2A4Awb+rCj6DTP86/AIZY/Pbf0PrloeC9mn578c3Db50WZ6Rsgcz3OSbODPvPCPgz7N9Cvwe6Z6HZIkoA9n8AsWrLbABIO8evTZMsWwQJwCLAiNOTVfri0yzst99+89w2/lw8oR1bPKmyhcCCb+YsPn4EHkdZcom7z0Xox+Xip9//9tPify/+q10P4bMODXDPK4PAwp2hKgvQkf2TSOdyAHDzyODvf3vFHYgpALeDfCfRzJDzZlDRaRh8TYIhkB/R1XrhhSD44UyqZdPN3Jl07wsxWnyzFyidb82MEpdttwjCaubSwp+AVBe48y2SRdktWpCXNpo+LPo2fGj9zWvch4k5gAa3+20h0xrgrzID/5vNfCwCm8siAeH/ViLP60BI81O7oL6KeF8ocw0vKrdxq7hxXzoi95kXwFtftwPhLmD78XMxM3g4h+pRMc/wgEUgMv4rpR/nnC/mIQEktv2q+7HGnVnWfLBt87loX83iNuFjqgCmTItLnwQzhfzPV0m1cdlnwSN+wNJZ0isLwSsrjxrU/oVR6dvMsWBzN8kWj9Fj8blHYQRf/P88jc2BInleZ3nSZJkFq5j66ZnAeUCdE/2caWfrQBU/m/X7TPQV977C/+ciS0A1NtP/fK58pP215gmpfQOs0kn9IR/UHEjgLPfREnOJN83sILDrK88AnxYPUAUxBcEF/TWX9VeF892vlsYAJObv32eORyiaYI4KKPtF1XsZKMkoDAPP9VNgVTO39SvNoD/CucXHOPHjP3g1pweUIZA/Jz0BwQNc9P4N+593v5r+h43P0Wre8hg7e5CT5iEA2BHOBs75GpMOgJvbPc8DwM9PDyHAjbzqZt89UFH5h9fFsAnrPmlBdTwTCuIaVgDaP84/n57OV8NbBVoJBAs0TNWD6D5abK6VHAxOwAaAMqDj8qQAgwQIyisID4FuPuMFwOPXpPuU+Lj8cih89OXMgF83zo7Me+ah4lnrbjH9CCvmn5UJkJfPKx56/77SvmmbZc/Q2gJ4BBq/3n1OH+/PAeI5oSy+yv30Dweun/+1M9ljJLD+WACfFnHXVe0nCHrS+FcWfwf9Bj1tbb8z+scHTHycMeLjDxjx8TtGfARGfPwBI/6g8hmNT4t/zew/iHi1zacF8g6/w/Mt6VV2rw+IEv2ROn3E57ufCz38jshAPUCbbmaMbJpR6Ct9fl0COPTSAPACi5902s4sPAKEefAHSNDn4sc+mPsQ0FNxmeu2LX/AhwdSgp545vMbzYFbRQd0B/Osegnf5yPebH4bvn0q+iz78AawNPxvHBhnisvnJmjn4ydoN7CrS8LHtwem3Lr51z8ezdXqKfd9wYQAv7L2x0J9EdNMzD/009N54LQPNHxYBCBk7UykwPlZ+dyLbguKG9T17GQ3VbNXz7PlPI0+KOLLkyL+0aA/UMof2ATAZN2HMxaDA7DbZyDE4NLMMX+q5luN/qMOB4wV896g/DQz7IcXNn14EOCHxbcDCXDudUScNYRFD07fv86HoTnajy3zL2AP+PFt07d//fDCt7/+mV0jKLh/tOkxg4VtBYjtMW8/loH6K+d4h6Bmnpl5sB2o5/DB64+W/FPvv7btP884KMzg0Tzf8Ofb0NCB/H1YhO+X98UYhunMzK9ZAVBZt9i4+Z/oBEofUA4IcY7S9/B/D0L5OB7O5oGgdc9/zfj9DdSsC4rIfVXt63wBlgPk+9jOExIEGh4oBN+frQnu/TtPHi/RbeyC8RbIxmDfjeAtHrj+lsC3qyjyPRfHvfUGwZA1ug4wFyU8GPejINqELoq5EeYTuEu4BI5F6y2Q9+z9L/PgkszmzraCKH0E8BF+vw0uBS8/n37NQfx20Jnj8XL39zdvjYOVAt6K5PNDQwQCLm48vfKWzTosVweycS3APvzhzmE5kSjocpRJXHZuBZXy2oFTUsMtYd0UWzhHY9gntzfmHmtytlwhhi5xO+u4vKXBdOb5CdVtN1ALv8Ok7AgKblMG+j4X2y5jz6fa2CpszOaGHt24mE9bW6uodSEOMLKXOoJTb5mVnCCuFdYVq9G5hYkxBA1whKd5BppEstTpLmbHyq7vK865psSahvbengiFShw36L7TrjWBLKUzSoQJnCbdKhFYt9wmKhQNRbk8nspp2h6Ph8qemu1xLSqHJbNWJqpszlo6WYi6Z7hiebotOYrjcoNlo5iC6DEzlbA7UzqYXxI5co2pXGYjfxsrPkwwObNurIOTJnQ5qhsGDq+35BYMRYPgkLo5W5DQolgwRAPD9SvYss6uc2Jr1vYKie53XXpzTs3GEMfrza9xI8T1TkyS5ng2BAYyYn09iS1zgZRRRPZnBmbJdV02ZD0Sqnfjp1NUZwfH5Fx7KOLzpaB0WN3QsLmSkYNrjBjOBvV5V8RMSznu0fFkf3CxFSbaa52A7uLQXuA7rezEPk7YNBHv04CU+f7GevuQQnhuSe44fud4qzqz8oPne5kJu+u7gOwk32Dcih+50nGOtbl1B1cL8qOP3FdI5XBFliaeeGZkkzN1fSsYoyimCNzts30RXlt6lDp3JWpWn5PRBgut3Du2qkxctY1FeVMFV1UumrrYH6otVKzlfRQNrL3eM1AuJ2Vc7cd6O1Z0dA65PjE3qOjftoaSOH6VNMieu90EkO6cC9GL310GtXQV67qqiyBpDYaCWX4nbsFBqdiGrMvnHsN0MqORp5qylM0J3hH1SHfaAbvsog5F3Btb8YLBIU0r1zdnIOyzbR2MNo4S6bi1lMDJVLnt26VID5u9pERrabLbHY7hFNQd1EsS7iGDS5XkjjcKZcLatKwhPkN3dtZUoaT7B1O8D1qMyh2zV9alM5A5I4d3MpVXF/x059oxF1WhP8j8pqx4Nu1u2voc0N2ZyXpRgnABInlo6cmYDJUqe+/PWlRdIQ5ZqxiYj00xE3Iyd6haItmGqS9nitfx497YoGU8mnGQtWTJkCcBz+7aHSKtiHST1S7R642ebjquvzNBWh3rO8tSVCrjF469enSgtMiuHNhKkii4SZWOHvQVGd4ObBdthcvxkjapC9MniB0OS6KK6L0sQ8VdxmkVOuerK0raodQtqf7aFnnXImeNBCQmMjB3rda0nW6pJTn62gnuPKOLxWFrn7WbDZk3hwcxPXgYet6GXtyQcN3QElSVV0tCMnwMYRTqVocrCjGS77ZbSNiXcIOqhxjmCnpi6jCJ+DV8uWDOxSdRMoHW54JyhsaSb9yaUmmdDcj7nlFRXqhzK91pvNHiuoYQ7qRrR1Ru0AudMI6hX5HQUcKY8RotOey6++pqtBBicBy7Zqw0dUgyH4yBT4WWKY/wJZi0A7M5CnbOZuohxa+1aIQhsTx4090pbVf37avGDKgSKgirZ8tth7L3hLK33XHUdvjR5Io8ntjNuj3ceuhMB8LlHCchQiWbYxVreaLrbivvCKbqWM6QVZzxYcQx2bNnT6UZZl6HnllS0/j7Ca6UfcKslsu90W7cAESy5EVgz7q54pCAnDfndk1Tqe3osEx6F2UZ2HJbwGyOVMc8Yg8wvw426r3dHuLxfAxaWiXxcpNQ8skzdPe2MigC1hkvMA5QBeSw/GFsI8SVD7R6cMfhzlaHHWaOrgdkGKYwHhxWVwl6bE1DFnFdrNjlWRm3dVhNVj3lInZDAJ8MbQp7JzE/TDqm5/rVC9TWMZf3Mr/t5RUS7jsrPbORhKZkQZ4zkh7reiW4Sc1PCbli86BDha1Iwmatn8kDObRRF+g5f6N2kkMPJHECjcVXVwpleEay3QGpb0vmbPpORfmFcJRPG05tB4dOa4wrkGWoRQO6MVW6gqWcj047QSvhOjWuDEPkCckJHOnJ8riRfI7XCAyyRjlubuN6TbMHngidCMmIVmh1aJmXgVeLgKByrgMJmZzuUjjBUlJymhRJFl6Rm15Iw11WGkw9KHpq2+Rw84VSQQ81FaKoTzaVlzjIgQwldTDKu04ehT6Vhxg/1bxyICFqy2h0SCnsnsPZ+HDmmDxfcopwLfJza2wTRjKZPVsq11IUW58HhwR1TwbiPkp7bR+Uw6bX9D1xgnO7O8Qr7Cabk4IiQiYaUeGvd/Fl1FeOuikRnR+K0Vo5LMVMQ0XvDsUOz0v/4AnnqJ0o8zTGE+NIiSYnfEHkeM6l5dLb236zQoJLyq3Hi0uvSVLVyIpRcv8eNVuhzL2EjhNFjdIOHO5YKvPE+/5c7ca1Jxnarp6KoEGjrZqxoW4f6nij2XqfJZxxckwXb9Ja1GSRytsDvvb3up7YR0azGsFKj1l0IFV7FfOZK6WIfGuhTEpunNi2bty4+4EMWYJ2pn1JROK4PUqwZdh5DreQeZHigj7vcWOnxsM0VU5uXy06uNCO0ZLsgcqS3PYwDurb0tDNQnNcI72x3J6AKW/j3jIDSyKHUu2WFDzNVs8czkGaS7CH3omLFNf5Y3W/DLYIK0pvFbLmDFTp7MNwLZQIL0pN2runteI5UnoLdKNq7eoY09fbxkxXwpZnCzaz/bMTuZgTpVsSKaH9WFpn+L7b7/dBy99JiT31Qk31Fh2fdrWXV5vbdTecxCDXDzB2aiFXjrUSIQNLha4Z5LB3/gKVscKHakXCmBev8l1Xn5lu2Ci6fopWlS9xBXWJ4yBHNytc4m9lYvF9068Gz7Fg3CEmQTjbdNpQKBFp9xYnZOLmaS7ADFNc3pG9FSowwu4KAWPR2PLatiuspUntYq3yLwYJn9eKIhyN6VyZWKP7+plS3BKvySrwl7wZ4JGsB5ZcbhgypuzDqlWWGKXf01QhJQI9DMvJuZ0IaLvEzmvi0N6oJMcZTTq1oJdOFu/s87qMquCUnSQsczPkxMseBaCnPt0KomgvqYWFFCutBgX1zhq8RMhtyh3IttvXjJEvdZmII+8iu2i/jzTH55b9dmtuKiSzZHAQGCV47P0h0TyMkCpbowlm4s1NnMYdFx+0HYWkoe4jaG2yx1MEYQUl4AgssHsyq2wpMGq4vdn5gTZUjU7WQ9aZhi4ad3o4wc0uUy+b43TMt9c0Wfs5ebRBIVzpfXbIabZTjO1kada1FwsSZu9sRl3EaZS9i7mr1q7LL2H6cFxVveRSHeJKqKodrdqTyYaEMuZSwgfnVOc6omNg3PMP5ZnFdeReHlXxkPHe1d4eEGo3sIM4OUumJMtM8pLdqGpekHZeoCmTFgSrul1mVKZcFZONoTXeSXtjWbZNSFA9heyjNdntDsk5RPY7DjFbqiUCq0LtVDF9gNopXq9CGjSamExHPDZJXUJPp4bmpjPX2AmR3qSQuQlUecDEikeZ6Xrapnx951XaPh138Sm2aEnfF0fxsEvNXEzuxmYnxORoN2II2UK+2+Xr4FhFKCkTEaSLYXPQp7vPa9eTeb7V8XCcEo9C6RXdOZXP2gTRsNdQV/uyQ49FnMUDg9dXU5FkAsxXPqsI+JaoPNNQV6u7sQTgzRu6xZRGFAdSgsVuOC7P+anZR/60XMF9ea0TZ3Pc7epwI5wod3tZeectKMPcNToO36YGQzPwhJnUxaRdfH+oaI/Bx+ByOSsHDt5JZbVVplNfb9AQrak1XNtVbGnsyUyEwx5bped2H6tUWRIqWXh+aQoF2xs0vRfPSinKMueyXuH2yHE88rKxDR062SQ5KypTzFZVt9l0fnW1CGtVXlcJfeu3mbHfC3KXdS5P1Xl3WIGZmMxzwFGDTDVG7q+L9HLGiuF+CyBhM8JtzDHc7qhpLbERQbCWJ6RpMslFlTvKCQjP8tJFaHN1iplKaemp8mxwJtVqkthZgKrHdEmMx/NS7QtECQWD1K8M4D8DVLHUa4K/vdQMdjrVJOy1Qi+rPWraduLUGGbnroKv41utQDv4UFdSMDKcPWUrZKnlRMTeicRCLXgTDlPjwb65LKONtmOpi5vCdQFTGuv27lXT7/ChQmMHwndWlWG0PprgSHhOSGWwOxOqo4KrDrXFsmqT7rPNkuBM/E6416PsFjJMipAFS0mjOKlKRGnrXuwzsytRxeSr6rT0r8g6gl2h6O4ukxTEOHlMx493TuyQpaLXgcLVMNKQk09dTW/aDZ7Cg2nuJN6PvFAOJ9BVbWFXnaijHnlVSoloLVQq+wOhDiyPIF2E670dHmIAx4eVxhHjei8d3IF3FH1nM7o3NfAqpxWTMEtDXW+QqxUpWLUt5NPgbJZ+JziEFJyI+6gE8L0+KZaDaeHobHSOazDsur0J+YmLyPVhjwsn5ra7s1uhQmqeuyHopUB6Bxx+6vumL0J2DcC3KIKoGcq7iobWcCrUHsK3UseUQin1BZijNuusrlAtvKoYmd9QrRR1m6utFSFI0rBTyC3c29HREUbvkKJCsMlCRqOILePerdsZTeIBETdxJEkeWwisp6EwKTtxMl2bmr6ZdgvlhFg0kRs5Rau1zrUBI/BmIsd2dTa2A8qwa4PYag59IZoRXV21s55mhIlR+bGJQhBx/KxWWCrLuNdFZjVp3hnAtQatVWHDm4aF526zWTrQiKt8pmPYWZOmDXOq22Cg9e7oXxjb9807vkHOxaHMBHmDXhXFh9Zse71OYYwcvVQk+TUPJ4bQn6ALuwOTGFbhGGHl0RLMNLl7Qs+9NxnyMS8rfaUuS2JDGqQQ7aA9qIUJk3pZDvRrfLl7t7gZNEKVMS5T65rwpWS9u2i7NNLAqVFDEALBCeOgXvddsyQ5rcdO5zaPV0a3w22DTLSbVNSTUKH39eB6u1WNgtAzZgsbmr5W45PfGEsjGVbTshHAxKv5m/Iin7j0IDbp6KvD4GRRkLtbcTrR/XrjUKVhW2IvnWUnRMOr6xYZInGHe5O5VGUGU5crfDAEV3tIg2wQxFGG5M3ewdhma65unZbQQ5vsrNSwHP7GV/BpqBq1zOUa3tOjTJ6qOuyjI8f1rpPV27uugjk3VGnWy3fKxVYOh92Aj106Bu2eYGh1ZxHtimrXlCtBt2OmOGc4JZbZgOAyfzxC9dK7rw4Xrm2qnb6lKuYY3lQ/xUpQ5NUSM1Jhi7XbRqvzcQBJzkBNYmsDnE2jEN9e1axIjHWRk7KkY152SlxAktdsOsqTTHCnBgGsot5vAu1Y+uhNYGNCOI28VsDRxJ7Ox+KYXZVle73tsu2aREcFNkevK007W1LBdrsPbzKGZdnmfr5q8c5Vbl19F0ymINyzgtaqci53d7Tjsl63lXCSvMyQmFTQlpNAwdhVgFe9Q+aBT+p7iz0au1C99jx1JqHllcj3FQzre8+EDVT1k6nO0LTViCa57W8jdexJ1wuwUmJuJVoExhqSzlW1oZYFH0ZH2w74OwNp25CvIx/f9ms6zo8xFEhhxNOeHZvKkvXKJTif74VCChAi2PjHeI8d7y5KbC5cEGKl1VQVEnmlb2aKv0z79nI95mFhj3EzKoqGIo1yl7HiUJe4XsLFsdgrR90IKXId9vLSd0MVSog23dbNZu1H28sR9S/Bma5BMVEiY4lrCBWdcUlb50zzOoNwYe/WrPyjQ/Je3SdWRHZ0Gq53S4YVuWUYlpZ4iqadud4X9/a253eFmnJJfeYRbJOllpksXWxFscVYERnspcaWzW9rw9UtW8AnUpDGmp60E93K5wwK7PAW4LVGdKR2Ub0EtyWfvSSVMTLn44mN1nmpntTbTWX2180OlujrcgkdVH7lIiWKF9u2ZsbT3u42xkbaoNmGsq7nDgYcfoYiQxNqtHE6SQ18LAMx3Hq10wdDbdv7G0p3IXLNJwnfKo2mikqQVp0ax2eeCWE1vx+L2tmsWyM8rxOinmxutFdLZLe/lFd9OhUwsi2IJZwPrbOrhOAg7Ty4GvOLYSCa4XMbsc8mAfBh7YcMqgDcC1urqBQsju/FVYk5oeknwsVC8phARbwiczeCz4hpGRkExh95u1JwyMBDBVqJU33rjB2s5wmT7whOSC/s9sSbcUF50RAtNSI74fpahsw15YWcm/gBjHvXxuukztr4XrXqTxjmcNDJJl1NWjXZsg8cZVpVZnXtSyU5BooP0nO9TUeXj3X4eiD0wwrVGjcdlnjjhXZjHdsop6ZjE6Qr7ziY8aRs2cigdpucPO3TyfKOIbSedKTz2iTEOUD04UUlT5q/jRMKtFq413n8vL1g9EiqmJ5v1cRr0BZpfPx0n6LMimGiD4ubkuHufehahRzqqpKVTjYPRDL01DqBm4hbcZGp3a5RCA9+Y9oV1kNe7BFKuJIF2pMgiDsmetkWxHVUEInCZaloTaUf6bww7xWCnSrsTExmo3H22YP0UQggw5ZtZVzGKwLxbyiWNxbtjcGmBiAV9ZqLkXdFdrcWdD8p7qrXUMtsu82WMABdbh12FfL8sRkCP74EAbRBu97fx3CCRkJ3SmmRWWdgVMhzshbFfVFdrlO6nAzzAvVHxViFSrCj79mtINd5xLh0ECvG7mYFmAmXBXxJsPCyBWOzdSx01ttcbijs4F2xxQYlJrmi3ntL/ExsGu5y1zVqZXn7HdpuDx4mN2V1VnAOt0+YlSf7nMdZRT0eQsH2EWLsoGHV4IoqYiJ/VTWYkwedyxG9Yrkk2+rE3rxuurIVrGbDX51orW9DqVoLW8rXky0m6TRJkn95+/A2P6p9PXD9d7w+Nj/U+bc9P3o+Bvr61sfjmWPoBp8euj79W6z964e3xk+Arc8na23WX14Pov7uudrH/8bz/1nw9HyP6+vj5+eD7s69zC9LvyVF0LddM31py+zxpgjY4fXt/B5lO79q64OfPz5q/TvX5yyWTei7bfelK7+8HsQmxfweSBgkbhe+vl5eTyI/vAWvp8tfsPXqS9hUcyBerxXMiXuH37G3v/0fRNnt//kuAAA= -->
