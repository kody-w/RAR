---
name: "rar-cowork-cookbook-scheduled-brief-hire-for-open-positions"
description: "Builds a morning brief on hire for open positions from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, an email saved to drafts"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_hire_for_open_positions", "rar_sha256": "e81607dec21e66306c81f8f66ec38e4212b29c9ae9e63f86516baccc0ea17f3a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_hire_for_open_positions`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_hire_for_open_positions_agent.py` and in the RCI capsule.

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

Hire for open positions Scheduled Email Brief — Builds a morning brief on hire for open positions from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, an email saved to drafts

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-hire-for-open-positions
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
      "description": "D365 legal entity to query, e.g. USMF.",
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
      "description": "When the brief should run, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_hire_for_open_positions_agent.py` and embedded as the fenced Python below (sha256 e81607dec21e6630…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_hire_for_open_positions_agent.py` first:

```bash
python3 scheduled_brief_hire_for_open_positions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_hire_for_open_positions_agent.py   # or on stdin
python3 scheduled_brief_hire_for_open_positions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Hire for open positions Scheduled Email Brief — Builds a morning brief on hire for open positions from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, an email saved to drafts

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-hire-for-open-positions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_hire_for_open_positions',
    "version": '3.0.3',
    "display_name": 'Hire for open positions Scheduled Email Brief',
    "description": 'Builds a morning brief on hire for open positions from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, an email saved to drafts',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-hire-for-open-positions',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-hire-for-open-positions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3c55090618bf5c87',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/recruit-and-onboard-talent/hire-for-open-positions'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/scheduled-brief-hire-for-open-positions', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where hire for open positions stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on hire for open positions for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads hire for open positions, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on hire for open positions from Dynamics 365 ERP data for a legal entity, returning top 5 items by impact, anomalies vs the 7-day rolling average, recommended next actions, an email saved to drafts', 'example_request': 'Draft my 7am weekday hiring brief for open positions in USMF and email it to the owner as a draft.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when an owner wants a recurring (daily/weekly, e.g. weekday 7am) hiring-for-open-positions brief drafted from D365 F&SCM data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefHireForOpenPositions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefHireForOpenPositions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefHireForOpenPositions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abObWLblX1Hf9yEzH7ZBIIHwi4pohEAgBAgkQJCucDLPM4ghu/57H6RrZ2ZV1uuqjv7Ucjg0cM6e91r7XPj1ze67qGzePr9dfbtYHe0siyO/WdmFt6LLoWxS8FamDvi/csuia2Kn78qmffvw5vmt28RVF5cF2L7v48xrV/YqL5siLsKV08R+sCqLVRQ3/ioom1VZ+cWqKtt42dKugqbMV4epsPPYbVcYvl0x6mXl2Z39XG2vMj+0s5VfdHE3fVg1fte/JHdltdqu4s7P25UzreK8st3uAzC5zO0s9tvVo111kb8iPnr2tGpK4BLYZT/8xg79RZBb5rlfeL63KvyxW4Hdi0GLhJWf23G2asFiD+hZeY0ddIuz/mjnVea3b59//uuHN6Aye/v865ub2W27xM6NfK/PfG+/OM0Bh9mykYG7l2/eAhGZXYRgbTWBgBfge+U3wM8c/OSBQL1/+7H1s+DD6j//Mx3sJmx/+vylWL2/vrwt/9S+eDrXlXbbASNdu7KdOAMh+rSissGe2vdILbloQb6K8NNr52+SQPz+slz78aXkU+h3P355A+lp7MXYL28/rUACvrw1/fL50yKl+vGnT1k5+M2PP/0mp+2dxHe7RRiw+tPX9+/vYsHC35bGwerr9cLQ77pADuLKB8J/59/yepn+Lu49JF9fi38sqw+rP5e8+PMXYO+rIh0g98/FghiAnW+fkjIufnzX0ZQPv7AL1//xp38mFiTXTbO47f4luT+/BEe+7YFovYfkpw/P9P11Bb379l3mP1dbgYL5dzwBy7+p+x6ofyb7mdm/Ew26BPTOt1z+qbg/2wD9ZfXzP/Xtv9vwYRV8eTv4Wbw0ppP5n1e/Pkvk5x+833784a9/A6L/j2KuZd+4Twlfc7uIA7/tvn79+Yf2+fMPf/35h74CVezb+de+yf5M5p/F9annDxF8X/XjH/cC/VqRFuVQrL730OrXsvofzd8+rXQASd5vv7efV7/vxOUFrRYnvil9heB33dgCW38Xx5/e/gbwpwDe9C/YAvjxH/+xEmO3Kdsy6FZXt+y7FUhwF+f+YvwtittV/ILExgdxbWMQ2Pd1oP6XDC8Wl8Hql//pPjH/o/uO+XD7Ddm+PvH86wLmX0FXfl3A/Ot3MP/l0+oGxJdNHMYFAG2Vuly+FABui25RXTV+6zcLpjpT538E+z8uH1ZxsfrlX9Tw9SnsUzX98uSm+IWCKs0vCNiC/Z8WX40IUMzLM3dB89F3e6AnK11gVBADAF/wvy2zB0DQJS5tGmfZygM6XUBr01M2iN3nRdgvv/zi2G30pXhBNrZ68V0LgwXfzVl9/Ai8C7I4jLovhe9G5eqHX//2w+p/rf67XU/hi44LIJD3zAALT1dZWoFO6wE9dSBpIM0ARp6Z+fVv7zEGYgpA0CCPcbCQ3bIZVGrqe98CfuWoj+gWXzk+CKO/8GPZdAsFxt2nFR+svtsLlC6XFqaIyrZbeX610GLhTkCqDdz5Hsmi7AApdnEbACbuW/+p9RensZ8m5qDl7e6XlUhfAC+V2cKczTtPgc1lEYPwfy+H1+9ASPNDu9p/E/FpJS21uarsxq6ixn7XEdivvCwDwft2INwGxD18KRYa9pdQPRvlFR6wCETGfU/pxyXnq4XvQWLbb7qfa+yFPW9PFm2+FO17E9iN/xwQgCnTKuxjb6GG/3ovqTYq+8x7xg9Yukh6z4L3npVnDXL/ZN75PiSsmOeQ8ZwVVl96FFlvVv8/j09LUKjjUWWO1I05rBjpppqvZC0T5ZLU1xAK7Hya/mzM3+aab9j1DcK/FFkMKq+Z/uu18pni9zUvWOwboF6l1Kd8UF8gWYvcZ/kv5dw0i5v2l+IbVwDbV09gBPEGWJG+rP+mcLn6zdIIAMLy/be54RmQxluQA5T4quqdDJRf4PueY7spsKpZWvg9zaAX/KWdhyh2oz94tSQKlByQvyQ9Bk0J+OTTd/x+Xf1m+h82vsajZctzdOxBZpqnAGCHvxi4YNoQdwDI7O41wAM/Pz+FADfyqlt8d0APAU9fP/qNX/cxqLQFL19x9SsA2R+X95eny6/+WIG2AcECzVH1ILrPdlqqJQfDD7ABIArorjwuwDAAgvIehKdAO1+wAWDv+7T6kvj8+d0h/9mDC4t927g4suxZBoNX/dvF9HsIuf1ZmQB5+bLiqffvK+27tkX2AqMtgMLc/371NUF8eg0Brylj9U3u5384If347x2inrSu/bEAPq+irqvazzD8ouJvTPwJdB38srX9jZU/PmHi44IRT1ZdMOLjd4z4g/iX559X/56JfxDx3iKfV+tPyCdkuXR+L7H3F4gI/XFvftwsV78Uqv8b0gL1AF+6hQmyacGdb7T4bQngxrABkAUWv2iyXdh1AIT+5AWQjC/F72t+6TlAO0W41Ghb/g4LnvMBqP9X7r7TF7hUdEC3t8yWof9pOZIt5rf+2+eiz7IPbwBL/X/1NLfwVL5Ud7scBEEfgXmti/3ntydYjN3y8Y+HZPn5wc4+rQ4+AKas/X0FvrPLwq6/a5SXp8BDF2j4sOA76H9QnMDTRfnSZHYLqhZkf/Gom6rFhdfBbxkVnyzw9cUC/2jQYeGN3xPFgnt1Dxrvw8r/FH5aaVeR/VO53+fTfxRqgGHgif7l54UXP7yjDHgHZ4oPq+/HA+DN+4Ft0eAXPTgL/7wcTZbwPrcsH8Ae8PZ90/c/PDj+21//zK4BlNM/2qT6bQUS95x8n0tAZZVLcH1QDa80PMkKVOqLw56N9aeef2u+P3Pcfw0YL/J+T+gzBM9gDr6fLpz6zvGAgroVYed/ogWoeUIwILIlJr8F+zeXy+fRbDEIhKh7/SXh1zdQkvYyA7wX5ftsD5YDxPrYLlMMDJoXKATfX20Grv3fTv3vYtrIBuMmkOPv1jhCeL6Lrn0cxxDc3a2DXYDjvovt/A26Rh2UdEnbJ30cC3b4do0DjnRdxLfXRIDZQN6rZ78uI0a8mLbYBSLyEbS9/9tl8JP37tPLhyVg3w8Zi+/vrv365uAbsJLbtDz1etEwuXbgDeGMzR26I7vRMpmmtrSyIrLeaNLerOF7rzj1eKY9tmWNkgnS66ls1RvvInkXtRoVgBiZJyjD5nCE467y5N26O6KylLmxJaKBPEOQmwfazoFVWM68OIXMeNYVUL+3Uqn9E2PAdGE2gsHc44Am1+cTkRs5xlxgAvXgI7Lm2DTa3wiJIZE20pug0nKz8Ol1bF1I6GzxFktwajNCxi6IH5d7gygpvcuTykx0vbXok6n1h0RWa1xAMr5FmAFiz93Njy/6HueQfED53Dqde8uedMaHJIGzhOBwvGwZLrXV+Xa+ZP72LjQxS5vEw61jhz6rHFLuj+ZNQdS9IOHG4FM8vgnLbPugE8a6PB5NTQbZ/Ubi/mW8FHeCJGELeWC5sBcZRGhpLzX8+cqxw7TZ6fJx5ISbsF3fRAjZ2o54OzFNr8KsX2Fn+HLgD91cGqx+EAVKbLW+hYPmZE/mw7NP06luz3diKJVDcrFNcupO/gmLo4M8Bma+Y3z1NB2zrTPbSYYb8HGbohaHEeIusHfX3LwKkcVyKJciw0OaOL9TnNNVWCfCbs9AIXNm8XRWVb5D+XqLyN4WI1P+PFEkk1t+Sz/wzTWYVfxK9DMx1b5MykPbbrSbfhit2BJw+lLgxn7PGI/wqs8gJf5VtbjG0zLBSHhpB7yjuwYxItM2COWi21tIONzF6za3UjwQtv3jUHDEzPZ5BFV01fK0gjRn/homa+daSYpqT9nIjfx00mtuejAbjON9yI/dlJRoIkHZPD56+gXTTe14KHlRUDfMg71sIM0+5laS7dI9F8p6WB9JyT5CunkwitAZ0gIlalDASHKor5OE4jqhO8ja3tZHmuD1zTCSrHrXqrkTGukMMw2sTklAxrvU2WPnHR1gJTeoFxaOqOk4Wru8aiubI5x1EF0JvozF3YPle9BJ1qMYCMTIsuMssncq58RdzopDzl8CWTEOvoqIaHfrmiqINyNoN+zgt/trACnwbo8l8wn1rkQEpe7NgqEO2wUwO5Fs1bH3UUzTLLRdRbH3aMPFMZofDnfDYIy1taecxt0OEX/cTJfUvMwtJQSUPY3CNYrXB2t0BXI+WUxr2J5gjKSEThLgw5wqrhZvDP1e1/JDdeUvLls3CMOPnKIftn5E8yN0wtXTY7ieVQK/omy2a9t8Fgkams2cLDBaGARn5wXG4y4KMILIYWaeBq468XuZ6k4nTe5SQg43tipU88RdZvxRpDfLOlPkvnO33Nac7PjMx1742BVnie8MvcGIm5MQl8EuNlE32PN5Z+Kx1phozAy2O6vubbhtML1KD4JIq1SqwFNuzZaP1L6P96lqEyRPIeGxgOLTLU6gWksOs/B4GOsYNiZ2GsJNSDCHDL0n2ZFqx6B65Huysm2EkCAKyipeMVm2Gck0pyyTL9YKLWNEOoVa4yPD9t5ZbHqSwzRim7IP3MwIxvhsInKjdrjTh4/RbvEOBiSodTvFvkWhqxH9fuuKLjm5nO8mPt0mZKyb6lVG9zgin3yEKe7+SPWteCIPZc9kV+aSZL1tO6dIlNpmXT1oryWEIMSK5iGZCp7F9BaFZ61FbQ+zdiUtNjW/OSQbmNNvhNluoX1qaD6y2ztK4RFabASDeMuy3vHE7eaCNBGBm7B4LOWmE3k9gmGU501jTOt6CqkDscmPWB9GD4VyUuF0Sn2plmgBO8ai+CCcU6+dnPZkzCLMIfKGZUfx1lpH4vAoh3Sg2uhIsrSUyWeWFPjEn7OY8KHRpGQ5Tk/o8c6KsylTIobnvDckOYNfrP1NwY3E0te2FkY3hTlqVJt7KrvBaUpQx5zwVOLQnvhavytsZKAc1m+vV4NneONaUORIJULHUltfNqbGMx/6NNfhOsZIm320ujWOioHPkXcewuM5IJBNP+/wOShYzprGe8UFlxSp02uS7snreHETOpTz6z5LNRPDHrPPBze3k6HoyLa4tHFl7oAR8ObsB7CBk76aQETYFTqKX/XBa4pHHplUR5u81AqKQOWQO0ngXFaT29Zjk2PMP84blHIVBF0HihPacQ7tE4fLsTUot+EUX0SjVya/RjOTc5KClsaZ7gZU0mmDvvBaHI03PWcDgRS20+A36/ggXCgpmY7YrEXejIra7ubZ1SxIW14phDOz3RJluQbkoOvHLAn2oz+2aLmpaDUl9MnwsTG/jmgjIr0OuzIf7zP+4M0A/U2ycMlDfay9A5yz9O3IiKjd7bBN5NoB6g76lJtzZ4WPpnUNujnwpdlSxtUVzhQ9okTkCbM7u0p7ulkzxEgkaw5abaJtnrUtdctqLQJIxwl5C1meG4UHnlUPEhZOuldqDEvdr6wLBpqy2tJ7GRF9mmNC7ZLd3HnNe/qcTff04FCOdlKnOs5mi9j0XnOi8ritqfNZr0Q4PNFb6gFmiYM+tFwYmVmab1xCDQc5vR5jKwmPCjaqWcXKY80frlQfXnllE42jnTcVDaG1No4Tvjmr1pAdYoTRwUDQ9+s0vO/nm8ZaM8g0GtBJzG0kWBIkRumxc4bc2/4cetH5pl1uNxdMaNBZb9OkxI8mciy5Mu0D+9odjEWkMlDIrDzGbL8hy6ubkFdWm/bKQyPOcUNeYt9sNv6WKAQeN9NMBylgrQh3+fyQ8pp4jM1TYkJVqQzp3KYOYCPBkYxLxSnYACbFmg4iFG5oK1YumpoT56OGG3LVuyODrKW9MZNbQ7M537rTozWYfFB4XQ/59Mlty4hq6jol0MFZU1nnViPvKSdhsLr7FnXvRYT1jbpVbz5jqpuRjj3do4gMnU/I+djoZ37t3YbpqvYHkQ272y48bMm1YAiGV8/39KpFOS3ZoWxrD51D5RvJ3KX9yevMbRhxurqfY3Xopz5R951+b4wrRJxMZIbhYvays74PtchAhC1sUftwd8h5w6xv28jPkHhOe183DDVRE1NOsk6VZbgNQkq97jai2+EuTrBa4RoU7ZaZSE9mXEl2QDA3gSF9Zkrs3Znf97jTXiDY39rHrbURMfseR5qWxFiAkFXHXNxuP0HBQFuBa/PnzWkPh1JbH2b9lJwrB4LnPNmcoKouh+ikMKZ3bWuVF1I9v4qpaGZM5oPhwyWtK4Gda9jEGNiBTKu5RwWxqXI2kzHokO/1WC1p2876C5nS+zvV7Rl3Fgp65HYhddyI89GvnOtdqq40IUpbnzz3D8XPhwOh1yadifLmIEewgDweBTbvmsLbqQajZpIvbKUI2za4Dk/KJi7HMqbcaYIKpkzubDO5FrxGCy1L4ZTPWNU73sWeeGhHxemZprri1ciZ2WV3GnlnQyW1yhhcKtAubMy6KRVubVX6fH/4ZHanm/OlUG5MNrHdQQED/e6mC/RwlKs6r9ZX97jlqce2NpHkSnK7+p7JhHuLvYQmOyHl/b11O0dgGJwZ1j31qe7fdrUKXRUNRYQiB8oiDT3gswSrXdfvqngUhU42h+6R6XVLbSBRO3uMJRnJ3d/X6E7q0IrC64TdQM7pHHi3HrekLhnnyAnTGJHix53kah9fk+0csBN0FelNspfsU0FtsPRCaV0y3FLY0FACw5yrJw19ccqiE70/ZxayDmtHzPLgfqId286nzU1JqaY/mbySD7V4pATpmtdVPG2nQm9vUq9Dt/U6psb9oyfvrnzvz8Gx3wTbvMwplZkD3uuQfYtvty5NpI9RMymMPkmKW0ieXvfiLaKqc6rt4Hp/s+zictrFtGRMzjEIUq50L3qb8GuNSsh1zprKAYFQgy3t3LbXB6O3lRh0PTgxDnG2B3Ney+dndL7DI0mKON5vlLqpIqJ46PbDCxDOE+09prJdjPUPJOhMQUSohM8FPLltm5iGMp7FKwxTTusU80W7xEQiV9Ctn24HmdpD8fqEStMk5txdsHJXmaJN657pedtu80shHTXrIc8H27+srVG/jsejJnQKsimVEznsVfVWWSnMSf5DCATRMdaOhzncBX7I51Rf9y4Zszqt6KwtrfMHtifOFdrZI4o6GEX0x51+RtoMce/pcL+b/h2o47scIto1vWtNvbhBDjbDKQPl2XE/6wPvlQnI/KA4xnFUvcN42FmCcy3XuySJskE+shgbkpaQ6NvaH6QECdpZ7pJkG0MacTDBNLORWiedLFyXjozbxjy2QWTxFDCT54a+fThuucyIW/vmbdPNbENVohqbPR3N2namN04jp27KX07zTEF5cSbBbKQyYr/WtjU7EdjtNrrrNTrJoSxpd6+79odttYnFXC5JvOjNtMh8nYtBXfujYIrwrIiKsT3LeMbduc4+VUjg23yyCWYKM9Aas/tsfU8gOHeSAdfvUuBNzYTn8eOUwM2jx735bFwOE4Sf1wGZW1jSSwSzbh7QRdiOuJS4Hr/Z4A9Pg6TTyXJLm8wdjh/Csm6mATgBDEzL62PWMl3SK6mviwaddGQmY4YilPPUi7xbwhvdZk5qidSaFHH3hsPCwHagWm6Yh45dbDB3VuSWtJsBH3GmoQNUw49snOu3O3TFpEOA5w4VdLO12anFBBtCnzp+/shvvtyeTOtSFZuCzmKYODSTJyt4GsAbiIQHHjPruQ1pwgvguCKNmbtE6EO7n3EyfSRGhzLeHgLDBi3txcshMHKS3V9FUzJ2EJoF6a1uMQWHtbQ3txzOX66nyt4kEHNLT9OVxBp/TXukVUmVtW189FSc+VF3wmMSJEV5kXfsbo+HUuRVpOyCAz3H4nzrtMdhk2ERdNXZ2Sly8ZHg635iqIkS4TJZb2HMXN9vviB2Tb3fBjKSz9bhHMV+mqj+VouzZHdn7TTBm0iq0fXBt7v0zg5rAmYTTU5qgxPQR7o+k92lHlF4n6llQDLgvFQxoX+5zMcctjJrB4ZC5ho1dr+mDI5d0+AE4bDFuqlQI9t4NGnI9foW4vzaRgkm6eF+rOHBnrAo3Rw9lOxOTqxD53iDFONBR0emulb06WwmGi4GiF44JGvZW8o8UiJCitijCXNgXGkXrTtLV/WwB2c3a6hEzmLsvRx0N1ss7gdnYJp4zdkyBXmU2JGbZohlWRcu8LqE/AvtYHAMOTOpyFnXmAzXp3mgY+H1cDUgypCQowzpYVBCnO6RWn6BUGV9PzUD4N9LeCaQjLcmcqd6AoqzPd6PVOOqCC6bbscSYvLwjNqxbuvAUhL3FHOisOvH4nxXWYfbJk099VdcRGF3X2iae3Ue/nBxGyXe5bDNrPUghDU2cKDzUUbb/hEI1eScDYO74JRv77BGPSHw9DgRN5kiylbCT9UcT4TWK8P6UEcbbI8gNw6BeoPKdXcfiyXddwLuyIjJpgcI5yDQAuqV2WayirmbqTmW9/iqQj0lHJwHLfnDvuowd7vjjglurRuU6nG06OTZxua67fVN7QdeUozrC1FwHSJo2ryDwOSdXLCsDs9Dvy4eHVneSNEX7+cGb1CovV765e9iTqSd7eqgskbhsD6mbuba3HZnyaC5e22g5yFqBulw7w850RT9FOrqmkv2dd8pm0KyUP1gjec5q+9p8bjHDBzXcmmPoltASr3XmbxWcgXkrxyaizs7icaruQZ3zqUPVI4Nxk3vUgIqeVQF+aamOlUxtt5ePsPDeW8Iu6uvKCnkXYZyWIuxClVR6hTKaPj6+lw1QXiV5OoAcyaYm+CTNCEoEpfzeXCvYA5NzLqf5Z0QO3MDbWqicFpEJXDa2/td1gvyyEeSwoQ9+hiUEeNCFfAlT7QC5zahJ1wInLidIUjsKkxssJNwQAh77okrQUsd0FCRpC20x3w2pszHCLUTdog5zW1DeJWp+4+ddGcFXI1bd4A5TsrvIwoIyVPQHAy59pEN3SPMd/u8ePTMOc6vvYeDKdtV10HHuJrAD3ZbpKfL2Jnert+J60sobfftLbkWk00ds9pPyzOm8yyngiaws13YwUZkKffo6IzzdEy9h2MmyfphQbrzuJ+z4DaQTG4EiDpjGskSsUEgu620gcvSluCtMtVkdTkhah47BkWyXB4ypHl0rjhUBI8AulhVdhII7byR6sj1xA2bNI53rytsw10IN3o8YidDNMq+nKFHBrXesZu2VYI1femFd++82yR1/pju9jHSu2NUT9F558hry9lV3ro11ro/yiZ3qrv1bV35JESwsKLCPFO0plqWt5PVemcEDA0+0l9ZIsx6L0k57LpP0qx11Zi6NYV62kNEgnohR5W3/qDvvBTFnHmKcOh24KGkZ5Js3AYIfs8amUTDgSNZOSq7Mam59s7tPY3QH9HIBvduPAR+C9nHGyutwayhYPYRnrtid3eInYV5+R2XYHt38HYwtt9r8HEOWuZ28LZIDXdMU9MZH+P2Fe0RaLjL9xtmjUVTc6l8gbq4uJtrfLj5h4tlzG5Djo1BytssusccZIMvh3K35S92cx+xvci5mkGNvm0bjsQGkynUMNwomMBdp611oeJQYUuOyJC5ktq9pkS2j9OXc0LylXyAtt76fE/uimuIBe2C4yaUIUciPCusqgXYbVcWylEh5AG6yhvjnPShJKE2wdhEhQ3IQyr39A1MbRdf8jssVrZ9nrphn6Xz3d+w22OH30UIuW7WNqLhsZDnA9vJN9XnPHdN7noYHovR1m79wOYunJoGVJ8kPFb4QjpvEniTk0QYiRejUdjjg/RinOBuyG07CC1fOopCUW8f3pZbpu83Pv/dR7GWGzL/z+79vG7hfHuq4nkn0Le9z09dn/9ty/764a1xY2DX625Xm/Xh+w2jv7vX9fFfvJe+CJlezzp9u7v7umnc2eHyVPBbXHh92zXT17bMnk9YgB1O3y7PELbLY6YueP/9jc2/cwn88nSqK782fgc+vS2P+S1PT/hebHffvobv9wE/vHnvj/58xfDtV7+pFpffb9ADT7FPyCfs7W//G544zB3gLQAA -->
