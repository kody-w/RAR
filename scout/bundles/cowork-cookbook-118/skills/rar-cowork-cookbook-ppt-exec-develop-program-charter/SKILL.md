---
name: "rar-cowork-cookbook-ppt-exec-develop-program-charter"
description: "Builds a read-only executive PowerPoint deck on develop program charter status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions, and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_program_charter", "rar_sha256": "16fba68279040220cbab6a12c7f0c35b3af5878585d4214c9c451a264ab54581", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_develop_program_charter`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_develop_program_charter_agent.py` and in the RCI capsule.

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

Develop program charter Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on develop program charter status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-program-charter
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-develop-program-charter-2026-05-24.pptx.",
      "type": "string"
    },
    "review_length": {
      "description": "Length/format of the review the deck must fit, e.g. 15-minute monthly review.",
      "type": "string"
    },
    "topic": {
      "description": "Program or subject of the deck, e.g. 'develop program charter'.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_program_charter_agent.py` and embedded as the fenced Python below (sha256 16fba68279040220…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_program_charter_agent.py` first:

```bash
python3 ppt_exec_develop_program_charter_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_develop_program_charter_agent.py   # or on stdin
python3 ppt_exec_develop_program_charter_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop program charter Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on develop program charter status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions, and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-program-charter
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_develop_program_charter',
    "version": '3.0.3',
    "display_name": 'Develop program charter Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on develop program charter status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions, and appendix slides plus speaker notes.',
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
        "upstream_slug": 'ppt-exec-develop-program-charter',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-develop-program-charter',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '474fa672422ff0b7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/develop-project-strategy/develop-program-charter'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/ppt-exec-develop-program-charter', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'comparison_period': 'Prior period to compare against in the trend chart.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-develop-program-charter-2026-05-24.pptx.', 'review_length': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'topic': "Program or subject of the deck, e.g. 'develop program charter'."}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for develop program charter reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on develop program charter for a 15-minute monthly review. Produce 'ppt-exec-develop-program-charter-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop program charter data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on develop program charter status from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, issues, actions, and appendix slides plus speaker notes.', 'example_request': 'Build an exec PowerPoint on develop program charter status from D365 legal entity USMF for our 15-minute monthly review.', 'inputs': [{'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': "Program or subject of the deck, e.g. 'develop program charter'.", 'name': 'topic'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-develop-program-charter-2026-05-24.pptx.', 'name': 'output_filename'}, {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'name': 'review_length'}, {'description': 'Prior period to compare against in the trend chart.', 'name': 'comparison_period'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready monthly review deck on develop program charter status sourced from Dynamics 365 ERP data, without modifying any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecDevelopProgramCharter(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDevelopProgramCharter'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'comparison_period': {'description': 'Prior period to compare against in the trend chart.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to pull data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-develop-program-charter-2026-05-24.pptx.', 'type': 'string'}, 'review_length': {'description': 'Length/format of the review the deck must fit, e.g. 15-minute monthly review.', 'type': 'string'}, 'topic': {'description': "Program or subject of the deck, e.g. 'develop program charter'.", 'type': 'string'}},
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
    print(PptExecDevelopProgramCharter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9166bLbRpbmq3BuR4zthnQBYiOojooY7ARILATB1aqQse/7TrfffRIkJdtVqq6qiPk1VFwRQGae/XznJBO/vlldGxb126e3g2flC9FK0yj06oWVuwu2GIo6AV9FYoO/hVPkbR3ZXVvUzduHN9drnDoq26jIwXKmi1K3WViL2rPcj0WeTgtv9JyujXpvoReDV+tFlLcL13OSRZGD795Li3JR1kVQW9nCCa26BYyb1mq7ZuHXRbbgptzKIqdZYCSxEP73gVUWrtVaC78AAi4CQDlfpF5gpQsvb6N2+rAYojZcbHXpw6Ktvdz9sIiapvOaDwvLmeWcL4BiVlmCwWhcNGkEtFiUKeDYlJ6VAAHyovWad6CfN1pZmXrN26ef//rhLQLXb59+fXNSqwGP3vSy5YF+3FMN/akF+1QCLE6tPACzyglYNwf3pVcDqTPwyPX8xevux8ZL/Q+L//zPZLDqoPnp0+d88fp8fpv/GV2+aENv0RZW03ruwrFKy45SoOr7gk4Ha2qAuduuzmfDN8A5efD+XPk7JWDjv8xjPz6ZvAde++PntwKIYM0m+fz20wKY8/Nb3c3X7zOV8sef3tPZZT/+9DudprNjz2lnYkDq9y+v+xdZMPH3qZG/+HLQefbFq/acqPQA8T/oN3+eor/IvUzy5Tn5x6L8sPg+5VmfvwB5n+FnA7rfJwtsAFa+vccg7H588agLEDJW7ng//vSPyDohCNA0atp/ie7PT8IhiHlgrZdJfvrwcN9fF9BLt280/zHbEgTMv6MJmP6V3TdD/SPaD8/+Dek0ykHgf/Xld8l9bwH0l8XP/1C3/2nBh4X/+Y3zUpCztWWn3qfFr48Q+fkH9/eHP/z1N0D6n5I5FF3tPCh8yaw88r2m/fLl5x+ax+Mf/vrzD10Jotizsi9dnX6P5vfs+uDzJwu+Zv3457WA/zFP8mLIF99yaPFrUf6v+rf3xckCgPL78+bT4o+ZOH+gxazEV6ZPE/whGxsg6x/s+NPbbwB5cqBN98QvgB//8R8LJXLqoin8dnFwiq5dAAe3UebNwpth1ADQe6BGDbCpbiJg2Nc8EP+zh2eJC3/xy/9xHgD/0XkBPFyW7ZcZtL+8wPnLC5y/vMD5l/eFCegWdRREOUBdg9b1z7kVAPSdeZa113h1D3DKnlrvI0jnj/PFIsoXv/wz0l8eVN7L6ZcHQkdP3DNYaca8pku991m7cwgQ/6mLA6rVs8B4i7RwgDR+lM5ID4QoUlBz2tkSTRKl6cKNAKqAqjU9aANrfZqJ/fLLL7bVhJ/zJ0hji2c5a2Aw4Zs4i48fgVp+GgVh+zn3nLBY/PDrbz8s/nvxP616EJ956KBYvHwBJJQPmroAudVlYBpwE3AsAI6HL3797WVcQCYHVQh4LvIj77kYxGbiuV8tfdjQH1GCXNgesDCwblYWdQuQfxG17wvJX3yTFzCdh+baEBbNXHrnsuflzgSoWkCdb5YENW/RgABsfFBDu8Z7cP3Frq2HiA8ntb8sFFYHlahIwX+zmI9JYHGRR8D83+Lg+RwQqX9oFsxXEu8LdY7GRWnVVhnW1ouHbz39Mhf013JA3Frk3vA5n0uuN5vqkRpP84BJwDLOy6UfZ5+DviQDOOA2X3k/5lhzvTQfdbP+nDevsLfq2RUOKAOAadBF7lwM/usVUk1YdKn7sB+QdKb08oL78sojBrl/0Ljw3+t2uLnb+dyhyBJf/H/WIc22oEXR4EXa5LkFr5rG9emjuU+cfflsLQHXhziPfPy9gfkKUl+x+nOeRiDg6um/njMfnn3NeeJfVwNHGLTxoA/CCkgy031E/RzFdT3ni/U5/1oUgCqLBwICYwKIACk0R+5XhvPoV0lDgAPz/e8NwiNKanc2BojsRdnZKYg63/Nc2wLuacPZiV89C1LAm7N4CCMn/JNWs9lBpAH6s0cjkIugcLx/A+rn6FfR/7Tw2QfNSx49YgcSt34QAHJ4s4Czm2ZnAvHaZ1sO9Pz0IALUyMp21t0GqQM0fT70aq/qoiZqZ3c/7eqVAKI/zt9PTeen3liCbAHGAjlRdsC6jyyaASYDXQ6QAUQmiMMsykHVB0Z5GeFB0MpmSACQ+2pLnxQfj18KeY/Um8vV14WzIvOauQN4RrWVT39EDvN7YQLoZfOMB9+/jbRv3GbaM3o2AAEBx6+jz1bh/Vntn+3E4ivdT3+37/nx39saPer38c8B8GkRtm3ZfILhZ839WnLfAXbBT1mbufx+nBHh4yvzP74y/+Mr8/9E96nyp8W/J9ufSLxy49Ni+Y68I/PQ7hVbrw8wBfuRuX7E59HPueH9jqyAfZGB4JodN4F6/60Mfp0CamFQA+QBk59lsZmr6QAK+KMOAC98zv8Y7HOyAT3zYA7OpvgDCDz6ARD4T6d9K1dgKG8Bb3fuHgNv3rE9UqPx3j7lXZp+eAPQ6P3zndpckbI5oJt5ewdMDnqxNvIed8A7YDhqinzen0SFOz/8875XB4/rxXN0hpfnEiB18IjfrzXpAbZPCJ8lbadyFu25ZZubvAcSje3f09ceF1b6DmoJQL20+WN4vyrWXLH/kIVPawIrOkCXD3NBAOAChATWnNWcM9hqQEqAbPiuLI+C8eVZMP5eoD+VnD/Wlln7spvbrUcFmhP5R+89eF8cD4rw03c5fet7/57NGbQcM0W3+DRX3w8vUAPfYK/yYfFt2wH0e20EH3v2vAN77J/nLc/s2seS+QKsAV/fFn379cL23v76PbkeyPdlDr9nEP2tdOqMaADxZ3O/g7wdn6E6W6Au3M4BZn+o/s9S+iOKoORHhPiI4g8y37US6OMjb/gCZAna8O9l2T2ew/PuGZjsJdRzzePy0U9kHYhFP2pfci2JjwC/5945A4EXptNrwXf5t0UZOd+L/GdfAiLr628DL+YzxxejH/5BF/PDdzg9VAUVCtT52Ye/B8fvLioefGahgEvb5y8qv76B9LXmoHsl8GuPA6YDQP/YzL0dDCAOMAT3TzACY//27ue1vgkt0H0DAkvSty2SQldrBEdQFHFsyyatJeqsfMTBCBuzfIJaUQRFuDi6xJ21gxNLCyVxyyZwgloCek9I+zI3sNEsE7EGa9dr1MeXKOK6no/irkuRFOkQKxSx1rZF2MTasn9fmkS5+1L0qdhsxW8bsdkgL31/fbNJHMzc4I1EPz8svF7a8HVlG+UOviCwMQ4nDakIXjN0W3PifA9NN+fMOCt6bG6jz9Q8Y974vuL44wTrzFWkp4FbCXrHr6eerDui9ArEjeQ1djU1meHd1L0sIa+v8sYZx8yZ9tR0SLfGrUlIauVEqB7eJFMd4ZQXbxYPHTaicVH6RkqFUXKIxGEvEGV7cAR5IGtlB2K3ph+HKp4F+U2F+IS9Joq5Wp2oZNdP4b1xqkNtxvboE2fGznGo52PKk2CMICG+EnxI3J5uQlhwTjVGmmnF+EFhl5dG7mRLMPqxH51eJnfSjRm1UKnvx+5q4ntPOGQ7ki981lxq1IlZC5sq3RPRVm3ErXfoqS2nGLJ0UTFlE6PYxe3v9Xq17laUKU+w3/uZvPQoFAkMeSMy49XwhbJJBqJWzJ1gdPuYWgpQFcmr8IRvmNut4rgLtYrU/UStdJe/L4fyIJchytCiYaRyoo9Em9hyB9WiOOzPpzOOZ0dmSLNs2F5hVK/Gc5NRA2fzDJGnqLyVko7eNniXnIuVd45xzK/JEBvpe6ldNsH1wAbRfncwaE5noUuyr/lDUw7kUbmPVxsZx0pNltH2xp47daqvrX7j8IZADblBqn1JXRRnj5q9lV+I3DsT6kAVVWoajFF18lZT97d4cHd8GMU3g9uGd9y4ieXtmJDZXVGp3Vpl1zWCRNSxrQJ/Su7QsSodwTLi3RG6maW32l6wSeiyEJbjbSGx+6SWpcMQLy/eLg+v9eXadZuRhhretrCTvWFxnMHulEntTLMzRh4P8VXkC/RaPXUMf9buVz6eZG3rj327s+RQRaU1hueJmF63YW1aYZ2e6WV5FSlZdjuyPEvt1oiq9dQcsyHLUVtGj+eDEnrRzqdOp6hyMNG6sP5NMMlDNV0ggdQwpIAFF2J0+8DgRRu4+8zmggSafHqy9NV1qYeeXSTxHToPZ0ox6ftG425cb8aadVdZNCP00sQh+euf2uTVyoGFMueOpch514iEHQbCuV7PPVTeERwq4bm5gi2/2O8GtyeEmu0u08QcJtcWhV25hdyzRvCbbF/t/O1t4+0IEjuLpLRjILpgCJEkg7sfqMY1JfeQlSYIFBpAsftO0MUM1zJ0Uwv3mgXBIlGWtNnCEZ10m0jUb2JcIvxm2OSZ52K6zh8x/l7wCO7ZLJOYwOHnvXRJ1eyGX11t1NebXDjgHTacSfRSnY7K1lHi2yUUxRthhJl3VMw9HzORPLbOnlB91LPiSdVlLE+xICFUzjiGFXQrBT/zy6EjDuhdbSlVadAG7+HNWUNvLidcndQW+5w45vz1QuO8o6bZQcEILikVh851V2MSm7qdbl2uT3riHU/sdeltGYT12I00nTimhMaebVWDk+64jvdqkgb4JawSGl+7cluprerdjqa+PkCluex5Wcbiih1sS6GcvYazrDu5k0ntfQuzthNrSE3PnG9Bia8wQl7eiRtUB7vWKfAbFLjj8XAcTqsBQx1kJ8w/mdEUFqzb1Nrb3TpVtI2uyN0ERhnODsJrHvNX9N7V14A5Z5FwHUBKoicLoHiTJqhxvbeHEtSauEFQxtPIAg2issP1bFXLBxMqEW9FpnuWrNNa0deOa7dabZvKaqdIYYkb2NiZ9W6i/G1xUTXqiogrF96NqgfZPFbLIGEODOxnEn9Vupulxh61XuGZeK4SyDxwQIBSdo/KKitHImK5ldG5DkvKwcbycrxPdbropOOePLsnDtuP0DWUVIlesYq6H6V9bNUnAJmdUVvicZ/4Fl3ubm5o55xa0m3K7laJufW4y6Hg253XHMzicGC4IAwlR7tx0qFQGkndSbXe8G04bRJ3X0sssVttSPMoFRUsYKm+JblKZAR6iejiqvSu8GmazFrjvfwst5xqpg2qCK04XWSRFG0UdnqTWgNMn/L9jQO5yK/5VIHiQ7zfwqhykNfNmo0RFKge3BpvpUOe5NaOqqHxhgeQFa4p6qJnen9PCW+znc7x8upnejMl41S1nKLcqbPN89LtRreQOeGeJ2w66yBV6bUWbntD6gRKh0fxKKhpPpJ4VvSXQB3xZkKNpUF3ka+ImndwWwBmJyvypNTQtyezTniKGJzmsN3Ikubsk+CcGSaPHM6cKR6tutzcb7XGZvBwxkvGG7NwNWLDqUgRWG6aMECDphr8FGuOTdZXtXHqLn0ljP29anSd8gJGiRM+TaFyu5VdbD9wJBvfuDi3I1ZIms5Uly3LyuUS5sRDUp7l1MOS+1LJfGI/CB4fdIXlGAFqw3Z6ccxm78qMMULHFomVK3uSbEsNZK0tcVGLB5JaeoLq8bDDJwyId5o43+99vG0pie/o00pgiUs6mgcaO+cbmDzx1HGbToWxj1kR2zFiGghuzCYokWtNEl3gi7iiaJ8tG1VIaieQ9lMkGDhob/ZCPx4TAxL3jr0foINZstgxPDLUCm+nlE6vmTUi/ERxBnfhRRdJztkW71qVzzd0UK0j+qjJ+Jgy1K6ULkkFSwxLlFKsTLG7kpvgEuhrykpOHCFt1cmtTj0T1v1JQoAcAHKGtiZKgU5ELKB42tAc6rR0l104FjRzDtssOwieROiXUjSH62EsLgjFFvKERJBZFBf2uuu8mxVimbA9h5tluElOCbIl+JLcWOF+OfDxZQr2vJxtdzl/FFVrtUFyChm3R2PLxMUVhtIcIMo6atDyim2IoiP9O2+4t4wfutiuJtMxrXW+Exmdo2CkTbHRlAOFv26d+lrpbcBWO8627gReMdGlXzkXgrTOcXjvdvKSnW4A5lgSWSYiu8Gkc3AETaCqH0eT2d208hgcJEQhVVWoDtmtPGC1cTVkWrUKAWFMewtxpou7CuMewz225jbxngFq954YcYy8FHfL4qYzxGXCImY0MNddZccYEsJBvO+bIQL2NHvzauDTKTc0nbpfL3t+r9oy6aiWP+hieAji4JhD9t3KxexyEhD2Sgdb2WabaFuqWQxvxzXt6Vv7rB434UbD7QaGYB3pWCfpRLvf9Sav7dFLS0KI0tzvu70Tp9QQnS5RSVPT3g3im+z37mFPkgKsZ84REtSyGk8HvmX2JRqw92Nl8EfJOiGyU01keg8GSCkweXuL09tQGtNevaUntgup4riuZPg4uhqHy+RyfV9KV/yankSmctrzrZlohtwN9NIX/O4QXVmychoVZ3PmFtkSB3Yo1QHKLCYP+kHDs5OmsmpHM/tCjonW1Kleq3PRVA7YRrXu0rV2vel+vjGmNuXy/tBPqLV1Wb2sgf/xdXvZUTcrj8Yihg0mudpSb9k0DTvRMp0SsoDIkpUt8TI0tNQqhBCccwKntE1C+T5TeP12P9mBpebjnmprzso6latXuX3XtljPdA05eOMJIq42I1CBcwlPOVEhvllf611QDtAuto17cg8E0LNCOEPD+KncHdmDZycJK+5kHllyQLiANwUkd5stYbMjKVi0WrdnBWfbKqpTHQ6N6SxRu9tmm22aYDqZmCAkgkLTheDtjh7KrjfdtCGlpdFGV1diyctGbQsBE4mLLROWpCD3/aBtzJoHnRbEslEHinBDekJZ+hTs1Rt1SZls7maWb7fGwd4g+l05b/AMiu6VNmxC6L5Fr2eyWRJtiiMbCQcBIJOHO21wZM1Ytn0e3DbnipyQLhsLnjp6IG56roxQVijONETXu2IqZnGLcAwZhiAzNeQubKe4pnyVZx3oKKY2g1wVTwoYXCAwVOIoUgljweKlwW4314Go0AldBtSWhO43EtTIlb1U3DQ/wPtJvebeZG6FvL/o/MRV0pTurncVumgbOtO2KJFhh9iJSUI6T5ksrGJ8x26oA/BHfbGdxvKETq9TrZxUknaHq6FNdQcZ1J6uV0uJGNw06a940uJLybw3AwdK1HEJcTu/YwfB3JUgkTCo8VfxjaoHEdmh2609xLWuterGW1eru6TSLXqF5CSSWEciaFlJS7Y226Pguvx2KSY+La/k4no7VY6o2vXtABHjvt87VzGym8MyvnKwxqVNTBb+CSSKW8B5TF4QG+VuunZYXgpl3E6YZbsoxYIAySu5ZxFiOwgdfW/NEhh76+lhe6rZiOEuV+HCeXa4Wm0YU99cMdIy1mxEHSw0JihMQtz72b94CDPwhdSL4iQA7JCHKqzztMvMjtXhi0QPu+2yKsJrD6rKFtZSClu20rUQPWM3tN1KBy2WetlMIqR50D2yr+aphY1cSqfVwBFVXx3xcEPXxXK1KVN8nZ8GmrpLQxGo11ULrxhJucfZjdiiozI5KZafMG+5Oi33Qbq6yCOrGVm17rSk5TI2SbyTHIdH4lyotLiuOMWiqVUtKhtRKSC4V7b8lYCVyEeTY5V09j3I0IOp7sxIKQYyqou0CQQ0ZUbczyxVxNdWekaquIuJKAshBc9AViqyVnlnXkOR03rdymWwSqmure3LOUWOROWmmuD6NLIJ4aJWSayL7uit3oc6WlErguxVZA3v1k0ruKhd73fHe+OLnYbD9dmuu2TnarVVY0vtEASQxbdeqawTZ3+Sb7diD7dQ1UfYVImoRO7sVhyq9Vmg1nh0WVX7VSdmx2UPl2U23FZZlbsitkyhAuxepqu5za/EWvbtiE+yJqrC68bNCmvDlOeC4yhMu0kbvF1trjLocXbt1cptQ4+nyT5vWJDOECPhZd079hW+ZImOJzRsbe99FRa+eFcbcpSPVz2sVrUVlcUyWcESAnzpw/EKhjl/vZf5a6nddhB0hsea4OOYuykMvKrQBj57B/Vy3FSrJG62l4O+iaXjtFFsYc0f/V6nMaTGTNIt76BBlGmksC1P6sJiTTvJhOJcGKfw4RY3Vmudq/RGrbDTdugrLwN9yYo79dsYDZHt0m+mHOxFccTQYiGtDd5A4LjVRgnrptyZ4G575tiDeuRWULxWXRe6XA+3+0pYuQMtEyiKmtKoG1zSWDW35eLKDp01n/s5cymMCr1nG18wHA0k1vkU99fUgHouhc6X5RX2wqqre4NP6KWUcCMBkfi0alo9FtFt5Kn387mAhorNuSbb6fXGaNvd/SqQhXdbngKSRix0zcco3BsVPMjTPUzwrUuu2/EWcZA8Ecd4pJfoyFcHULvUa8zjio6y98rklFIJEE4TSSu1T+th73M3JLXxdHAPxmBE97gYSkUpRYtRfdW0lNxn19qEyvt1f+OIYc2LcXphmEG1Dh5cnyhK45Jxc3Lh6/GAniRmhGnimNWYHIaodsf4qrdLae/etfvQdJXNwpzjTpnd7Bp6iU+QextE1+y3wnWDSkuXc8tTJGUUJ2nnCM+YVbljbmpBDt2tQxnyMNGefTYqO+lbN8CWiGDLsdd6jgI6RlDF4HovnumOhTZux2oN2J/2HHFc8Utfsy6YkFHUiSAuIkg3RtFcpCywCl8J1b7T+VpZTrtbTZ52VGvsCS421YZLvMvuqPWX3rp2+yV94m+Gj5keyvFNoN8N2EwNygoiJcT1OI63IPK9MRKDbFopa7rAGtq7ujk6ckbvZ2sLcripL+NLn6sIcV/jhRBiK0SBsRK7Ei4UdWm2y6jVcgVfxmlvIrhe28FhhZKMj/LUqbRX65Og5huqqD1iP0GFUEkwu+W8Qu3ScUS4LOmxQTrDobo2TIlf4mJ2yCAtGitsuFS9FY/B6SI2DjY1pOnhRHejkLpjsF2D+KOwQW8tm8tYttuL06EpokZG8mXYn7qxPnNXwSTPd73GQteAtT6kIzW42IGbZGuwFzPWFQpkEb1LXN1YxcfpYxcV1NJhwqAgkBgx9fyOFEiYnQ6ktWl4g1lv/astjLV3uDut6kp178mb0GaoVjHQ053M2ljJIeR0Fy6j7qMIj9JQsKouzCiHqrkLtLEbaHhp52202uAkUulKbyy3OrkicGJDIOfYnvphKmAjKEWs2SUJjPjXKeHkvt3HtTMiIFtAcGZoyLDXxiYnxD5r6LJPa1s2D0oax5viSjQRtLlbw7ISkwnHNv7QcIFZrksFIdYT7KLTadIrFpXH4xI9G+umuDPVpO0DWFwG2N0e7nuSxlJyFNWtL+M02NeQh6BXnSBx5fqcVvtJxFxLTEOfVrA4T1Rp1WTEZlOLI1Vhil+cWn2NHG4KXJhqXJCZpl5a855gNWbRTA8n8fau2wontTovJqBrxnTQKuwVMXPiEfbA1p9gx8lGSlxAElgRTyxhl1O7QlG8W5pp1286IvWVpr/Le6aA+qo7kyFxw3ZVpgsaFKKyi6xMcltx2M4tLEFELLHe8qCHt09EP8XoRbXP7DqiBs10W5RLWw+qLwo8eGuJT7srE1SmZrQuQa10/Yx2d2IVnAo3RkCTxIB+wQ/20WBWG0NlKfbCYrTG7WtH3Pm2rHarfD8uD3FKQx20Yath7eJ1nNdduuz3HMVrZdGGVbmhzimzdoJtT5JRX/b4FGe1vbRPp7N/j7ujAdvnzjfud8KEgJvpE9Q6YFMNYqbug8EOiRxnShn0+e1pSQkndTxx53Y8ogc4AfN87BYvjauOe35rC1pDFEu6osD2qSWJ8yo+t1RHBC2Lt1B2PWNDRguRD9/jTTDcDdIVVuSp76oRW3nrCVr52hD6pCYJuhkhMptw7lS5Y1bRtUSX+snYJEa+r8vb5hCHp+X9El+C4qhsFG+dgIqPcNfAPnLG4KMmFfB71LlrvbfXcEtaez2qoheLr+AWg6/9slAZzt/oeqcq7ao6Edo2d/ZeGsSuBzoTwd36CsSfiVHGz1UkpvleQDTO8Feug62pDgKd2GAlXDsIlQNzkgdZslKt4ylW9VW9XIuuO+ViHSDG8lDqra1pDExtUF4lcb3kaJr+y9uHt9+PHt/+5Vfn5lOh/2eHU89zpK+vwzzOVD3L/fTg9elfF+mvH95qJ5oFehzANWkXvI6r/ub47eM/OyqdV0/Pt9G+npU/j/lbK5jf0X6Lcrdr2nr60hTp42UYsMLumvm9zmYW0AHffzoUfinxfDYfGn5pi3miH83DUT6/5OK5kdV6r9vgdR754c19HYJ/wUjii1eXs56v1ymAetg78o69/fZ/AZ1oxTFdLwAA -->
