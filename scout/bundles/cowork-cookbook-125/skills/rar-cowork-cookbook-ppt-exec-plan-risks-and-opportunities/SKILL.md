---
name: "rar-cowork-cookbook-ppt-exec-plan-risks-and-opportunities"
description: "Builds a read-only executive PowerPoint deck on plan risks and opportunities from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_plan_risks_and_opportunities", "rar_sha256": "e18360b34f9729e2609cc970f30fad9817bfee68dcc8a1fa65856ceb9d2d1c68", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_plan_risks_and_opportunities`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_plan_risks_and_opportunities_agent.py` and in the RCI capsule.

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

Plan risks and opportunities Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on plan risks and opportunities from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-risks-and-opportunities
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
      "description": "Dynamics 365 legal entity to pull plan data from (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-plan-risks-and-opportunities-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period used for the trend chart comparison (e.g. monthly review dated 2026-05-24).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_plan_risks_and_opportunities_agent.py` and embedded as the fenced Python below (sha256 e18360b34f9729e2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_plan_risks_and_opportunities_agent.py` first:

```bash
python3 ppt_exec_plan_risks_and_opportunities_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_plan_risks_and_opportunities_agent.py   # or on stdin
python3 ppt_exec_plan_risks_and_opportunities_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan risks and opportunities Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on plan risks and opportunities from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-plan-risks-and-opportunities
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_plan_risks_and_opportunities',
    "version": '3.0.3',
    "display_name": 'Plan risks and opportunities Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on plan risks and opportunities from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, action and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-plan-risks-and-opportunities',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-plan-risks-and-opportunities',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '24f93da677eb0c61',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-risks-and-opportunities'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/ppt-exec-plan-risks-and-opportunities', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull plan data from (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-plan-risks-and-opportunities-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period used for the trend chart comparison (e.g. monthly review dated 2026-05-24).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for plan risks and opportunities reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on plan risks and opportunities for a 15-minute monthly review. Produce 'ppt-exec-plan-risks-and-opportunities-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan risks and opportunities data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on plan risks and opportunities from Dynamics 365 F&SCM data for a given legal entity, with title, KPI, trend, red-flag, action and appendix slides plus speaker notes.', 'example_request': 'Build the exec deck on plan risks and opportunities for USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull plan data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-plan-risks-and-opportunities-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Reporting period and prior period used for the trend chart comparison (e.g. monthly review dated 2026-05-24).', 'name': 'review_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an executive-ready PPTX on plan risks and opportunities for a 15-minute monthly review, sourced from D365 ERP without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecPlanRisksAndOpportunities(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPlanRisksAndOpportunities'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull plan data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-plan-risks-and-opportunities-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period used for the trend chart comparison (e.g. monthly review dated 2026-05-24).', 'type': 'string'}},
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
    print(PptExecPlanRisksAndOpportunities().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916ebOjVrLnV9HcFzG2H1UlVgE10REjFkmAhCQWCXB1lNn3HcTi6e8+B+lW2e52v+memL9GtVwE5+Sev8y8h1/f7L6Lyubt85vq28Vqb2dZHPnNyi68FVsOZZOCH2XqgH8rtyy6Jnb6rmzatw9vnt+6TVx1cVmA7UwfZ167sleNb3sfyyKbVv7ou30XP/zVpRz85lLGRbfyfDddlcWqygC7Jm7T9smrrKqy6foi7mK/XQVNma+4qbDz2G1X2IZY7f67yp5Wnt3Zq6AE4q1CQLdYZX5oZyu/6OJu+rAa4i5agcvM/7CSLsKHVdf4hfcBiOR9DDI7/LCy3UXcJ0e7qsDDeFy1WQxUAQL17aqtfDsF6hdl57efgJL+aOdV5rdvn3/+64e3GFy/ff71zc3sFtx6u1QdD5S8AF2URZVt4Z1/rwggAB6FYGU1ATMX4HvlN0CBHNzy/GD1/u3H1s+CD6v//M90sJuw/enzl2L1/vnytvxR+mLVRf6qK+22872Va1e2E2dA60+rbTbYUwuU7PqmWDzQAi8V4afXzt8oldXqL8uzH19MPoV+9+OXtxKIYC9G+fL20wpY9stb0y/XnxYq1Y8/fcoW3/3402902t5JfLdbiAGpP319//5OFiz8bWkcrL6qF55959X4blz5gPjv9Fs+L9Hfyb2b5Otr8Y9l9WH155QXff4C5H3FoQPo/jlZYAOw8+1TAuLvx3ceTQmixy5c/8ef/hlZNwKRmsVt9y/R/flFOALBD6z1bpKfPjzd99cV9K7bd5r/nO2SF/+OJmD5N3bfDfXPaD89+3eks7gAwf/Nl39K7s82QH9Z/fxPdfuvNnxYBV/eOD8D6dvYTuZ/Xv36DJGff/B+u/nDX/8GSP8fyahl37hPCl9zu4gDv+2+fv35h/Z5+4e//vxDX4Eo9u38a99kf0bzz+z65PMHC76v+vGPewF/vUiLcihW33No9WtZ/bfmb59WNxuAym/328+r32fi8oFWixLfmL5M8LtsbIGsv7PjT29/A+hTAG36J4It4PMf/7E6xW5TtmXQrVS37LsVcHAX5/4ivBbF7Qr8XVCj8YFd2xgY9n0diP/Fw4vEZbD65X+6T6T/6L4j/bqquq8Lej/j4esTpb8CzPz6B5T+5dNKA8TLJg7jAqCwsr1cvhR2CNB4YVw1fus3DwBWztT5H0FOf1wuVnGx+uVfov/1SepTNf3yxOv4hYAKKyzo1/aZ/2nR8x6BMvDSygUV5VVz/FVWukCkIAbQveB/W2agDHWLTdo0zrKVFwN8AYVsetIGdvu8EPvll18cu42+FC+4xlavCteuwYLv4qw+fgS6BVkcRt2XwnejcvXDr3/7YfW/Vv/VrifxhccFlI53rwAJRfUsr0CW9TlYBhwGXAwg5OmVX//2bmFApgA1CfgwDpbquGwGUZr63jdzq4ftR5TYrBwfmBmYOF/MCGrAKu4+rYRg9V1ewHR5tFSJqGyXarwUQb9wJ0DVBup8tySogKsWhGIbgMLat/6T6y9OYz9FzEG6290vqxN7ATWpzMB/i5jPRWBzWcTA/N+D4XUfEGl+aFfMNxKfVvISl6vKbuwqaux3HoH98stS5d+3A+L2qvCHL8VSgP3FVM8keZkHLAKWcd9d+nHxOWhVcoAIXvuN93ONvVRO7VlBmy9F+54AdrO4wgUFATAN+9hbysL/eA+pNir7zHvaD0i6UHr3gvfulWcMXv6rXob/sy6IW7qgLz0KI/jq/8fOabHKdr9X+P1W47kVL2uK+fLW0kQuXn31nYD5U6pnZv7W1HwDrm/4/aXIYhB6zfQ/XiufPn5f88LEHkgKEEh50gcBBiRZ6D7jf4nnplmsY38pvhUKoNHqiYpAKQAWIJmWGP7GcHn6TdIIIMLy/bem4RkvjbcYA8T4quqdDMRf4PueYwMfddHiyW/uBcngL/k8RLEb/UGrxfog5gD9xa0xyEpQTD59B+/X02+i/2Hjqzdatjz7xh6kcPMkAOTwFwEXNy0+BeJ1r54d6Pn5SQSokVfdorsDkgho+rrpN37dx23cLYD5sqtfAcT+uPx8abrc9ccK5A0wFsiOqgfWfebTAjU56HyADCBMQXrlcQE6AWCUdyM8Cdr5Ag4AfN9b1RfF5+13hfxnEi4l7NvGRZFlz9IVvILbLqbfY4j2Z2EC6OXLiiffv4+079wW2guOtgALAcdvT1/tw6dXB/BqMVbf6H7+h6Hox39vbnrWdP2PAfB5FXVd1X5er191+FsZ/gRQbP2StV1K8scFFj4u6f/xmf4fAbOPf0j/PxB/6f159e8J+AcS7wnyeYV8gj/By6Pje4C9f4A92I+M+RFfnn4pFP83oAXsyxxE2OK9CfQA36vityWgNIYNQCGw+FUl26W4DqCeP8sCcMWX4vcRv2QcqDpFuERoW/4OCZ7tAYj+l+e+Vy/wqOgAb29pK0N/Geee+dH6b5+LPss+vAGY9P+1MW4pUvkS2e0y/4EcAo3a89EyDS5AMXbL5R9n4vPzws4+AbwHoJS1v4++99KylNbfJclLT6CfCzh8WGAb5D4ITKDnwnxJMHtBfhCsiz7dVC0KvCa+pUd8wvrXF6z/o0B/KAy/rwAL9lXAJK/i8ioWS7L96H8KP6109bT76U/Zfe9X/5HXHTQIC1mv/LzUyg/vwPPhyeLD6vu4AJR8H+Ce83bRg9n452VUWaz+3LJcgD3gx/dN33/94Phvf/0zuZ7o9HWJjpeP/146eUEdgMqLzT+B3BpfkbSYoSm93gW2f6r+L6XdRxRGNx9h4iOKP2n9qalAEx77wzLexqX3jwIp/ree7bXiGdQVuGq+3QCR4n0HqWd9XtKh6ZZmB4Rn3IIi8vJXDgIyyhYUXFg+g8hb/Sbjn7nyKSAoAKCMLub/za+/Wbd8ToWLKsAW3euXGL++gaSwl3h5T4v3sQIsB3j5sV2aqDUAD8AQfH+lOXj2fzdwvBNpIxv0uoCKj1DYBnYwPKBJlPbRDUy7Lk3CAQYHtkdTCOmAmryhPNelbCSwNwRFbFzfoT3UQ9wNBei9EOPr0i7Gi2AETQYwTaMBjqCw5/kBinsetaE2LkGisE07NuEQtO38tjWNC+9d25d2iym/zz6LVd6V/vXN2eBg5QFvhe3rw65pxNlgR2cSDWjeBKVi13eLl9hHOXnRjngkKibqm43sWEaqGpZkuju55AuU3V6Hfhfl9U29RVSoEWmBnjeuc8Ml1TnTaVocRFE5lpcC2xhHYt5YTnIWLprOmzHiZZmYX/WYi0Q8uT6ECmkyM9c0qny4D0SJvQuu1veiNYnJtWdKXe8vjzXiPdgR3u9ZWxX1U1XwOllqdT5y14gL1emOHBtPxCWcwFJvrC/j+VLMuNKsyXl9jmV2f+1HtTq37mB77EmpG/0UmdVU+FSOp02xx/eX0qqF9ZzRF2VH1LUYbiub3ai1vsHza1BvxrMEl+lwfdCqr0Ras83TzLRY8ZgdR702k9jYG7154eIeWp+1hiCpgEzv4kQFxhoNp4fvENqAT8khT4U7pFrnVtPmbE/DYjFZk6SfN0oOEUrkikxhpnLH1KJfaYfgMp/YG5fpBLM9SZdpva2SiHRdJ61McstUh1uvdj4xsW4VX+2zl0iqROtZfsLwWpZOdHXdX3ojF7EDYhzhrldmgTzJgb5W97ykpTYV8gl93o5HfnuCjpYd0e1NqO98XYo0dOWzvNOVoeLtNY/oDpnTFqSemyrJY+1c3M8G4irKxfa9PPAzbcKqfJcVamyXp+NNYRSl3Ek+F5l6qzuSoMNnS9wUfpZfx946bdfjIyUG9GGpxBg58pW418VQe7YdtWZ/r9I+m+SNETz426bm8Gxqqag6JkI6iGygrI9HOVDu+ZhdL/NWPpxvTnFPKS8pMO009qaxt5SYdaGwnELnppPtjTEttOVaqtQL/oKjhorG5vGW7c9rfor0hoFl29Rlt77uu+MWS8QmQ27SeKh0PhhyHT0hbo3db1P6KI9tpCVFspHSc+QdqNvdNXrRCI4FH8z85oaxFEmxAZZyg3Lkyeg07RkFKlAlhB8o3QQsjvoWkVJ0cSLwHCr8YEMZVr4/IblqiZcpgAri7Gn041QhVY2uj6OIQiNxTDaXh2ruNkM3Ux5D4xy5zWfaCsnjWhD6ZOO2QdWtQ8JnTo2iU5ooMuY5w1n8BMo9xruxO13om1i0mCRYhNsgp5C7OomwUa+9m56P5cG4i4p+2se2POf3B3FQ8n4Y4/EBaV0b6bMrhcSN3zK1gt/uugml21y0+1IPD3duHh7yUbvoFLWjXQ4tVQ1SOjNOToYWlny+RB00m7mVYAM/7TpKfiSGlFeGJQgjUY3sWfalQeHWI3404dNR0Rt1OsJ7WaQMDr94glOdN7RLuC2rpDd5rxdOZmxkwdbcOtk90N4o9kZIXIig4Y6nR5SUElsl9tw+4lTajWfmwFkWHxnAwgyuwZTV+3uHSzXEmWkmJW8zMcxUl8ihsmGqlKURNTR9LqNno8Ui4dIwW5qVd5qtie5dJKhktz5sTAJFrEijglET1PTqd9sDOc54yxoIeSqZRO6rKRluga3JR7UmhWPBepud4PcEpZImdKeqE0SZzEF7wDIkwXGe99B+yxWRV0I7Etrq+EGEJ20nz50y7fGNJqNmE6eiY+6OJh4lV9ZD0pjZ2ZYGifSa9UQ1wp08bac7ye0EWq2wxuqnCJcJnHT2TFzqQ3DBbJvPaa2dse7M8Dft6JkBicPNekNE55kKY+5ehEeL84qdJo3UgzVTbCZLI3koWm884tlMjcc+RE2zYx5cL8JCIqtSsV8TM6bA7MOrxku63Sip3kvDgUf8y1XDiyrfgow0W/GcCOvDxOC73cgmziSr28d1SPnI3Ge6iZ5mk7hG0xA6CLH2cMS3aDkjFL7O7/yJGls4uVREArJxTNzNdEVvRg13m0FWwqoSIna7jSAiTcNjjlnbStp59Ji357BirZu5VeNHG0Sytjk1WVMICTLwUCZJzFC6cmRDo9/sUuXubx/H2+4hZ8o0Mvk0M/4cJ0geYBXtHUR0fdLCatRF7YCy95k41RUvEH6Ax4lPZofypKsS68jT49IlTDeRthcxe8QQSoag23WT4PAWWgfYAwkkZr1Wo05tyclOhzz3oKnL2e2+5B/WluwPaTbAgwLG1Jv66HYsP7nkII8qz3ho7R6a3omPgTg+5PR+dq30UBx8QXC3nWzCzfbYSTpDqjXTCaGwYyZILt0wYiwAROk85yJ8gXf4pSQ47TyU8bh16ECsxLsQIbe7wRSwxw8yZjXehjJZVKuNLNszKYoD/z0oAot90bhpU4NxkAKZlk9qO5BRV6a+juzMEgjI2XuDuxDNWI9onI4jw0z3RuA3vcqJFUJR2a1UdoYEQeLGvghslqA6Hh9gRiRFqR3uTgZqnq6511TQshkCTtyZ4am5osLjgj64sDFyhfIBYj+OanNYc/I15lNYBt3l9GjaNjtlfNr30k2Ld9aBtMrhzBbbTj8jmqmpBd/2d50heLHfjzvXulf9NY6gJjEnBa9v2RDPSH81BVFhyvYYIXDMjfdWmeLjJBOmLzJwUsf6RjkQVBH5TNLeW01UcrwbDki4A6a41TUUN5oyTPH+7hZZJiWHvd503o2+HcVCPp5Em4clet3nnsge1tPMO3IZi9O61fZ0GrmFmVMwZyLGWfUN0Yb2il4rTmhzWzM5+zZebWGsgvkoiWQA3GZt0Odwd1HScs947Fi1uMQfEbklgvHKxems7BxX1RP2WLPBSaoGCeGrzYGKDGRoQx0hrrl2ut5dczjZ2XSpDAoeJV2RWLJE1uTRjYV9xkCjdD9R1nWq9iOu6ZanS5IEPcyJwwKlHsMjOl843ZHb2xFX5X14ELK7ARcaykmNJNPxuU5STgTgQp+dapgPTEFdR+kY5RitKw131QC8u50tX3MuHxnOknmGp3R2dyy26wrWLbO28uLoRzuGFE6IHZHX7CgQQ+w8uCo81l28P6V39L6VzMSPBl3HI86xfbk+bh4S7afahmlt5Fhz/nU4na+wfjwJpcHwJIzyfpuNsJYQ51Hfn7Qt0mbVdmzWc3yV6kPBqJr9kPOAlJCbszXS3fWattJGk7KzfWmTPczgUOXpqOiGDpZ4yfoyzoeg4bMr6Y7+3VHTLj34j7bXW7eyj+mpwDgxs02qgFSOEXDWbDA9FfosmImCuYy38/6UCfqlvu1U1M3FXVRu4aY643kG1/yYpVLjolUVAoRz5iTvvD0YXsL1uQ6P3D0JpvrKgkzdaUiRTrewmWUGdrU6Q8cDFW73+Gm2PBVOMw26xqAJpP1J7purHyOkHdkbhM1ObBgfbTTS+FHmE0slvdbACDDaJCYc3nnBZy0hDPMYEl11a4zM+hgeOxE5VbzL63O/5zTQyjZjSAWBFsLepQqnQFNoajh6Lr8uadswimto4tVdqX3Jqlgst31XmVgO3qp0uOd3mXYfVJ307uy24ZNHua1kwT20zrXrHB64mubjoyxukd0YorN3I9tDfSLu5MlU7qRLbJq4eSSz0N454sCYwrGb4is53XMQyFNk1NGpjap6c2Z3fEFhXcOdOACprC5uJ/wYRbNtIkqboQOTGrwA40yYzLZfEJ2OTT4u2vv7zRSL26U8njPXUsp8d8dPZY9MyWbP3wJAFQv3UkzXtO6NdEHcYge0jDkbGNgJ6aBRJWZXRbcb7tZAkecajxq3zlVrqefZaXRqYg49GAyxx30U9K4+puZl3DiaZY+FkNqXMZcSi+HYsi6ISK1m+pC4bu1f7u7jcTpvHU4ItfGIttuzO9vVVbQrTSFYLwEZ1mVNSYQ+6sJmX+BkhcmJMZh0eVOiMt+3XvSQNwReGGkE38OpIe3s0tUiL/QpkSE1VlpGIu5TiVV6hjxkEqOOst0cgiC0Vb4HgI1bhbxhJlKK97nklteUOKCYZAFwM2Kai25YoEfWeWYvGZsnVqg5EJtl5wkrgMi4edzgKMRyk8FmscAwZ411LQK2NEmsOmtt1R0B8xjBB3cp3prbIB2N1M7FSkvR4XAydAVVMWLXcHXkhE1iOPY6d+Ecv/h34doiXmQqWdrRbSpRoK+J2kD0mEuFQQObR6a/c0qMGemU0THMZe1muJk3zgudUzayadrdttN8dI5Vih6Q/MGk9r4p6oyn1rKOxmGeEJopZrp/rfAJ9aUHW+yoar0mh+st4UHOTdwkiZvAYR+cqA2Yk65lo7oS6dxdBPVY6KS0xihVN0Q18ZONf8lBrD1kMWqsGccI2d8eRwOFwhhp6lzmEBwnN9tEzYlCRYXLzczB5Bpo202QHudu9B8NFJAgilK4NcLgHug1L0rQNjph427Ir4Ll0pdObqwjjpa+A9sZXiBgQgCQA0U+6+7A/JAaCFHeRtuyars8nCF72pGTZgt5Kdus5PgXGJnOKZrgpDnrXXyUDolxk/3SCRNT6ujxIG6Hi+mJNxtzcDRSDvANhhK8P8wY2kUnmzTlfIOC7g9dc4O9z4fi3hC3rW/cHF6EMKNwLgficSiV4JGVST97LmnmXoQjBHZQlNFj28hm5uLmb5oWVD/U6uFNuoaVTIhrmQuK+wlR3S09Bz2ptueRzY/mzkfV4v6Y19Ea8mX7IfX5mnkgXMM4Kufzm4KvLhtye2k0Xrk59zPZdSZqKpcdLAb3jQG3ZHenHjCLb/p9cx+dNZXvmwlS5GQIzBO92c4Y35CG5zXaYa5K+7ht5YNJ+jsAdBaabadDF+XkvIbWSUCVQijya4Gh1kaA1z7Ta5aJMk5PWLcTgqScD2d0hlYHKzAAiMkKPMfuSPMHmCwKbRMXgR1odH/bM+7WUKPWwuPNPoGZSbsk0Xl/NmgxP401Uvn5LZ8fHpi6iV3u+NzcyveTdLD5sEQgUnJlIklwPj7lmnuyWmKtOHtczjFPixQPE1kGdCZSvqbRHnyKg6CO9GXHedOuomF474hDwCeqL+pxylHGDm+hjdflLVTAZ7MjbsgAk5ds1v2sNDAJvjRCQweXekRnTtYMgRUFRrKEA0fS45hhVh7w8knZ4Z1j3IVprPcN26LcqTFubXdc2zu7tW9Sw8FMiXW5eOjWVnQLSi87cMdBmGWSjGeepLTdFB3ifdLFopqpqbof98xkBmlZFPpekSKu3LsXmBbgBoxQWWeoyNmoik0ZksXWPzdsNhBhVfID5ewp6wyJkpG6akT6A2fB1KY1xLOk5HAlkuvOSAYclEcEM2QwPKzVEd4R8TaWAjc/izfEL6Nb4hAc11uov4tgzTQIZ670/d0nWfvkBdCeosBcHm+gMM/O16jH+5EXXQhxzkF72c18VLT30LYM42FNFKEZqHmbH8eW9sbd45Gf8+RIHEvEoaOTNGSjElHkFhrk3XFwPFy73XyOhinyPIq3+bajaqI8V759H6FyK85c7tn2ZRNIdxvmosl2ZDfemNAuJ47pfV+610RyD5pyemi1ZUJWNjC8dS0QErLlg3tiJ2btHdCTl6hljK8PIZcG1o42GonnWOtaei0lIOR2nxse5Aytg1XN/dGfNo3tYo52DM7SBnrEJUHn54DUyd49Y1dG5S4z6hGy229GHfWFPTRSIa3CqkiPQhfcfUwn1W6kOy/x0cjR95trs5FV33MecL+ti97Q5vspzNYCPjCeva2wXa7Nrk0TDNncy+BkV3BjHKAaSvG2B5FDSzgto0RVwEMy1Y8MG6GUpWbQogqZklkaAUpJcOtHFj4MdnKqUEd/3Ok9ZUPGDgmZHDs26WHUrtUBbYMBYiXXSOoduweAr0NxCaJFjeJqroRWCvghH0BjdVMnG6t2h8M2WmetsX+Y10ecomCWGmsekjvOAhX7fiPVXRafHnTdgGFHOK+7Umm3s2vsewCw/E5wto1EMslav/oYg16QweIdKx4pPchmkhia+Uzv0V0A2PUHRu0etmGNVNWjmbA3gn10uCsDsY87F9O8XuIpMmusO+rYU+sFuH237zAn25sIBSB4AmiNtrJdNSdfnrDTQRwqCoLPOkUTVB9aEoHVWwxZG7eNrqyZMmHq6ayEUPcQAq8XHawMNz58iyeDtq5SqbcdpxeMLzXlQT0jvh3hUVeAKXKWdgSkeoLtjb088mCwnWgbO09GjhU9weT3y6acsnp012NzK323p/yhvewDeGNlFtpvJ2EemVqkd2Qa8pS517Tzvif9NdUQ7IgA0IAS+GZsbYQlbBG5k3uU7G9awZ9nlLg55xia1SoR8WCXdsiMSD12E91BQTnqDlXNwzX12Ls55nyUh+GUXuVA28NN4hRHCj5j9hEWEnN92uW9T3MTWnlHMg7wg57FLC1vTU0sSqhzdScv5sCweHquT1vHE1D2eofwhN8W97OqskQK8usqbcHMsD+uHVHusRxhZjphBIg7C1wxEAFOFlFz7tCHyUDSOSu7KK4PrVGEfulJ2OgpBkxS1m02ZIqp68eZiO/0ea0ZfWUN2bReozfCqI/i2qS4rh5Qmh1Jfg7abVUBcOssFL7f+PF2uHWMY7iBEEiGhlljUZcH/AyG7uLcIjUS1tShH9pNdSeTezdfLP3RCtE6x21kdr1WeDgOBm0yMzDLUw/Rsj4bU02mx/ix7jNLME1cg1h1Enl+i0gIta9dsQqF2JdqSeD81J9YOT1Yhu4FfI9Y9iQUSc8FWTvu4cLaonp3YNbmZQpVddpbCDkpmBSvnZLWvBwdIoOG1psd9BCv4XqcNSzRGh/PICcqD8KxMk+I0dM+0/i7+dKG2Fm8s5muwPhmW0WDfXw4Tf547DCMkgOmvp6xrV6RNBs1RJnOzXSRWnjdXyTYwjCesnpWudzUFpIHHD+sB3+eOgwMmsuxyl/+8vbh7bdjv7d/702z5Vjn/9np0usg6Ns7I89DTd/2Pj95ff435frrh7fGjYFUr7O0NuvD90OnvztJ+/gvHVguJKbXa1zfzq5fB+KdHS6vOr/Fhde3XTN9bcvs+e4I2OH07fJqZLu8PeuCn384n31XZzF+2fiu3XZfu/Lr+7FtXCyvhPhebHf++9fw/Xjxw5v3fib9FdsQX/2mWnR9f+8AqIh9gj9hb3/73/7+Q9yoLgAA -->
