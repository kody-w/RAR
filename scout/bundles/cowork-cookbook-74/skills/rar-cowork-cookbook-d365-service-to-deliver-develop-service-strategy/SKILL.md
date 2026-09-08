---
name: "rar-cowork-cookbook-d365-service-to-deliver-develop-service-strategy"
description: "Scopes the conversation to Dynamics 365 F&SCM 'Develop service strategy' (10 L3 processes under Service to deliver), answering using that area's entities, USMF legal-entity conventions, and documented honest-degrade opti"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_service_to_deliver_develop_service_strategy", "rar_sha256": "16777628a83848f4384c6bb662adda4594aa078df168fec009c009cced73d08a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_service_to_deliver_develop_service_strategy`. The original RAPP
agent is preserved byte-for-byte in `d365_service_to_deliver_develop_service_strategy_agent.py` and in the RCI capsule.

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

D365 Develop service strategy Expert — Scopes the conversation to Dynamics 365 F&SCM 'Develop service strategy' (10 L3 processes under Service to deliver), answering using that area's entities, USMF legal-entity conventions, and documented honest-degrade opti

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-service-to-deliver-develop-service-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_service_to_deliver_develop_service_strategy_agent.py` and embedded as the fenced Python below (sha256 16777628a83848f4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_service_to_deliver_develop_service_strategy_agent.py` first:

```bash
python3 d365_service_to_deliver_develop_service_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_service_to_deliver_develop_service_strategy_agent.py   # or on stdin
python3 d365_service_to_deliver_develop_service_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Develop service strategy Expert — Scopes the conversation to Dynamics 365 F&SCM 'Develop service strategy' (10 L3 processes under Service to deliver), answering using that area's entities, USMF legal-entity conventions, and documented honest-degrade opti

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-service-to-deliver-develop-service-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_service_to_deliver_develop_service_strategy',
    "version": '3.0.3',
    "display_name": 'D365 Develop service strategy Expert',
    "description": "Scopes the conversation to Dynamics 365 F&SCM 'Develop service strategy' (10 L3 processes under Service to deliver), answering using that area's entities, USMF legal-entity conventions, and documented honest-degrade opti",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-service-to-deliver-develop-service-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-service-to-deliver-develop-service-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5a7e17010c613b1d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'service-to-deliver/d365-service-to-deliver-develop-service-strategy', 'uses_skills': {'custom': ['d365-service-to-deliver-develop-service-strategy'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Develop service strategy Expert** skill for this conversation. From now on, scope your help to the service to deliver domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Scopes the conversation to Dynamics 365 F&SCM 'Develop service strategy' (10 L3 processes under Service to deliver), answering using that area's entities, USMF legal-entity conventions, and documented honest-degrade opti", 'example_request': 'Act as the D365 Develop service strategy expert and help me set up our service strategy processes in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user wants D365 F&SCM guidance limited to the Develop service strategy subdomain of Service to deliver, working against the USMF tenant.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365ServiceToDeliverDevelopServiceStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365ServiceToDeliverDevelopServiceStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(D365ServiceToDeliverDevelopServiceStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916efObRrfmV9H8btXEubLNJgHyrbdqEAIhQEgsEkucctgXsYkdMvnu00iynbxvcmdyZ/4auWwJ6D5bn/M8p938+ma3TVRUb5/eVN/OF3s7TePIrxZ27i3ooi+qG/gqbg74u3CLvKlip22Kqn57/+b5tVvFZRMX+TzdLUq/XjSRP4/r/Kq25yeLpljsxtzOYrdeYPh6wf53lT4uftj5nZ8W5aL2qy52/UXdVHbjh+MPi3cIvBCxRVkVrl/XQGSbe8Ag9TUQyPP8NAYKfnwPrKx7v4rzcNHW879NZDcLu/LtH+qFnzdxE/v1+8VFPbKL1A/t9MPj5vi0MJ/tq98/XPUKt83AHd9bREXu180Hzw8r2/MXBXAQOOsPdlamfv326aef37/F4Pfbp1/f3NSuwa23HfDsZaBW7J7mvTx83VZf/gFRqZ2HYE45gsDn4Lr0q6CoMnDL84PF6+pd7afB+8W///utt6uw/vHT53zx+nx+m/8obf4IdlPY9Wy2a5e2E6fAu48LKu3tsV5UftNWeb2w5+iC8Hx8zvwuCcT/H/Ozd08lH0O/eff5Daxj9Vi7z28/LooK6Kva+ffHWUr57sePaQGC/u7H73Lq1kl8t5mFAas/fnldv8SCgd+HxsHii3pm6Jeuynfj0gfCf+ff/Hma/hL3CsmX5+B3Rfl+8eeSZ3/+Aex9ZqYD5P65WBADMPPtY1LE+buXjqoAGWHnrv/ux78S60a+e0vjuvk/kvvTU3Dkgyyq3r1CAnJ2XoKfF8uXb99k/rXaEiTM3/EEDP+q7lug/kr2Y2X/SXQagwL4tpZ/Ku7PJiz/sfjpL337zya8XwSf315FYzup/2nx6yNFfvrB+37zh59/A6L/t2LUoq3ch4QvmZ3HAajkL19++qF+3P7h559+aEuQxb6dfWmr9M9k/llcH3r+EMHXqHd/nAv0X/JbXvT54lsNLX4tyv9W/fZxcbXT2Pt+v/60+H0lzp/lYnbiq9JnCH5XjTWw9Xdx/PHtN4BDOfCmdR+PAX78278tjrFbFXURNAsAyG2zAAvcxJk/G69Fcb2InxBd+TNCxyCwr3Eg/+cVni0ugsUv/8N9YP8H94X9kAcQ7ssLrL80xZfX0oDvB8p9e/QVx3/5uNCAnqKKwzi304VCnc+fczsEGDvbUFb+PAPgljM2/gdQ3h/mH4s4X/zyd1V9eUj9WI6/PKA8fuKiQh9mTKzb1P84e69Hfv7y1QVE5w++2wKFaeEC64I4nYkCGFWkHcDUOVL1LU7ThRcD1AGENz5kg2h+moX98ssvjl1Hn/MniGOLJxPWEBjwzZzFhw/AzSCNw6j5nPtuVCx++PW3Hxb/c/GfzXoIn3WcAbW81gpYyKsnCTBb+GApsIxg4QGwPNbq199ewQZicsCUIFZxEL+4GOTuzfe+Rl7lqA/oGl84Pog4iHZWFlUzE2fcfFwcgsU3e4HS+dHMHVFRN4BySx/QcO6OD479nH+LZF40i5nq62B8D1jYf2j9xansh4kZAAG7+WVxpM+AqYp0pu/qxVxgcpHHIPzf8uJ5HwipAH9vv4r4uJDmbF2UdmWXUWW/dAT2c10AQ32dDoTbi9zvP+czQftzqB6l8wwPGAQi476W9MO85qARyABOePVX3Y8x9syn2oNXq895/SoL0FaAqLiAJoDSsI29mSz+45VSdVS0qfeIH7B0lvRaBe+1Ko8cnNuExV91PgtmAKXeLD63KIysFv8/91NzLKj9XmH2lMbsFoykKeZzjeYWc17LZ1c6iwaJ+qzH7w3OVxD7iuWf8zQGCVeN//Ec+VjZ15gnPrYVMEShlId8kFbA/1nuI+vnLK6quV7sz/lX0gBeLB4ICSIOIAKU0Byorwrnp18tjQAOzNffG4hHllTeHAeQ2YuydVKQdYHve47t3oBV1Vy5r2UGJeDPVdxHsRv9was54CDTgPwFMCIGtQiI5eM3IH8+/Wr6HyY++6R5yqOHfK73LADY4c8GzivUxw3AL7t5dvTAz08PIcCNrGxm3x2Qb8DT502/8u9tXMfNvP7PuPolgOwP8/fT0/muD1LYnRcd1ETZgug+qmjOpGxe+3gGElBUWZyDrgAE5RWEh0A7myEBQO6rbX1KfNx+OeQ/Sm+ms68TZ0fmOXOHsAiA6eDO+Hvk0P4sTYC8bB7x0PvPmfZN2yx7Rs8aZDDQ+PXps5X4+OwGnu3G4qvcT/+yZXr393ZVD36//DEBPi2ipinrTxD05OSvlPwRYBf0tLV+0POHV+1/aIoPr5L+8OLMb4++wsIf9DxD8Gnx92z9g4hXrXxaIB/hj/D8SHzl2usDQkN/2JofVvPTz7nif0daoL7IQLLNCzmCfuAbLX4dArgxrADcgMFPmqxndu0BoT94AazK5/z3yT8XH6CdPJyTtS5+BwqP/gAUwnMRv9EXeJQ3QLc3xyz0P86btNn82n/7lLdp+v4NAK7/d/d5M19lc7rX81YRFNYM77H/uHqgx9DMP/+4jT49ftjpR8ATAKnS+vcp+WKZmWV/VzlPj4GnM2O8X3hAfz2zIvB4Vj5XnV2DNAYZPHvWjOXsynNLODeR3zrMf7VGn/F/Zoji08xj71/wAL7BruD94luDD7S+tlyzBj9vwW72p3lzMYfhMWX+AeaAr2+Tvv0XguO//fwvdgHDHpgDkHuW9d3I70OLx6ZkdgGIbp576F/fQMhtEAP7FfRXVwuGgxL9UM9sDYEkBcrB9TOdwLP/6373Ja+ObNBfAYEIThAEjpI2iZErMliBf13ccXActT3PXq03K9uGCdILEJwMfBeGN4+/ru8RmAeTNpD3TNIvc4sSzzbOBoLQfAB57n9/DG55L+eezsyR+9Zez0F4+fjrm4OvwEhuVR+o54eGNohD6IQzSsaywlsz7S93Qe0UrRE96lZNZnTmdFkzHersoKgY0e144JhsKm9he172h6hgfUVY9teNmOfbVJVX1aisCrYJUVc/iceczyfI6qfk5K1DzO06KLU79mwIt9V0sRNSLzyB3V9alTDsuDmfM7cUSXsDQezJjdAso9N9m8qJtmarNFIHJCvCkfWXaOxNRb3dMjiEdRNMLuOWiW634+Dnq7rLybJOeul63VMWf2WEKMi9WCwUtdLRPUUy2qF0UrW9rfWC7u6YcWzUkZ14U2Uvl7ZU7+ghDpIJWrIEY8dGImiQm0XHzBNxOmbkWK2lezi6d6at4cvlsk48+Z6uGdW+Ovfe30neZunlBoGtWxHOtWSz8sWaRzbunrFEcSuMQuOVWqEatrne4YzAHMujyHnHybEV1fK3yujCIVI07rppDKvl1QG/+2GYXnXWXGs5h66LiVfXKOWrQqUiG1JgmNVE7q+3w0nSzrKq9BcubBUJLgiNpO7VwVbw03BvJiLTB+u+lAkrNEZTtnCClg6bwzY8ktVgD7v6qt71MOrH1qUVOb5mJH03I1jQCf2UjtiSZrdrpI1Fg6IMXzQ0/3DeRgGTK1k1bQY7KhGkzOJtXLraHb3aSXwsTlFVri+2ga+YekT6TkhFI9nnIcS3NS+YxnEn9PYWvxtnRMUvglFy82JfJXZTl5Bu6ri9pyfTvuGifK/7ku4uUXqxRMRhkqAtlE2qVgHOaInrJu5x2q9D10q50/kGs6y64+95GummxCdsqMhd0Z21QMyoqHRXx3JdD17tCrW+lWqbaVNzq0et3bMNStiVFV8S7lTd7qaAmZWyauC4OLO63A27FGJ3xjXTIt7ZiCRdQeq9N5Zxs1/finy1awPN7mNf4Oz8JmX9SjqR+8M5S1BUmkgVF0Up9nL5QtaiXHXnncdJtx3oL5Vgt74bxmhb6anyoViCGuiIaERHtJJpkFmeW2q64pF4na6ICCKGIVljzV2H5NOQM1MAJdqG6k3OQu/paj+qDiU55dCZbJt2wmA5F1NdT3UV3/mVOkqXuwInW4sbGZkqIJQ8EMfDIKlKvUM2Ij+QAqKx1i27Gfd2hw8yYnUe5e9US4BZSt/fgOvKqDasod0PSngO71t0GVNyRRpNyCd9nFNSAbFZXzdpesPWJyYIUb413YsSRB4XNbB1hpFSqfiJsmOqgEGS8sROsE3bXu17Xq8YdbJcmTh2uG+rosg7TiER/dHNEt1ujzGFAIwk17mn4MfAksL8bkeeGwtL/d6fKrG44DEdDV04CtLp0p94VFgdtgTlZlurRN3MpRw2NdfJslzTXZJu0J1L+/dCowv5DpfbFFKQGtk1zDVitpnFCfWSc7m4v6F2sE7TaEISmYNwXU23t93In60Bs/D79XpJsKM7IRflflLtPd9jUnkobZrkC9nDiRwRt/kSvh0up0TxcK+tukFwswHKY2Iyt9tyv6fWFhQtgy0DHY/3mMDqgSc3yhWEYVKZpqXY1r3wKJe3GL3lbEs77dnV1gP4sHKyouEHZXcbqNxPHQy9YsrIScS6IgSK541oebt69zqqJ7KXJJk8naAe4NNG95FpH+RleuWaM+PDwqrFY11DdgxiVvpZ09vNwBNLagiym4U32JkGNuy8QdgltXiobiv+7Etbx66ILOTvB0nX7CJAnIMCUkyGT5NUtqQV1TyuMRCH8itWGoTIPJBqD5PNgWpMeR0xp3V0c3ie3TucGZyRabWNEPsiXG4UnykMKVzIYMuzPaxQ8d3UwmAp0du7g7ROOUYMFW0ULZY5BkvTXk6ZfdNsDJLTb2OkW2HAuLLRImOaNle+3S+DEcCjpCeaDHk7BZLvxLXvdN9kw1YUBvIU3yxF4uIJZOmWpU5dtezJvNwt/Zw9eGNqGyHTc/mIh2py5ZdaKcE17EfDaCa6e0/8ioDcFRv6p8CUtU6/MexGDJZgZwwNy3M6LI/YlK663LPiKSb6zO/OwjReHYY5eBZTD5TtrUXg3cXdXUf8croTibvLAgLWsn0WVcSOo+4Tlw7QSXDwgDPgwYOKbebca809xNSJEw9WwAIo3t1jjcw9QRCcnOHKAxlpAqcccN0JdgO39oZjKSqo6WGabCz9WpmErDiufE+gMtnLBrdsFXmTMptU18ZtEUyoui7DdONP5DoqqJY5SHxKaiqh0UzZHCQX8m5uLceWGJruzZqAivVpLUc8clUpQ9YOuw0byowRtQbRGDLGBL4MHzVaBEgqnezQTKRhPN3smlnqbLDfqJst5hn3FA2vZgVrZa3mOF6zKlWZNGt22AnkAK3vPT6ZyMudFYqyLMK7MGoVLdIVc5R3cUSxdpFdMmQp3iJ6a1d1sVoLMNqa5d4mudDM2JRkxH19y7cN7jLYJVMh7ehS8NJLWT+9cJIe4kVss1edt/eAFq/NBsMnLTse7fO2cHSmcDdy4hB4NUTWYZUMshg3Tc3xVn6vJToXlyZyP0Ruy9nrbr03wsk+Z3c7i9fiUHGI7sIKfcm9nWzuGB4b9PS4zJJqF2oN7RAHWCSvjt+pgCmnyxqhotgYjsVY6mdcS5eDGi017Xy5hANvnw6YyVsMcYsbRdmG4sEYXOPAni4MP1pxSA57KTH8yb5A0lHP93bE4FKwNEVYZpb3s3ksTG2NXL0CVWMvuRp4vOoqRCiWGLwuQpbjk7LVOYdFl8ykHkFhG+lmddpEsWMkgTVVzJoStATyuHLErbzEuv6asn0Q8EUmHAPbHylpR+Se7Jx1W5dF1wpvbn7PZJ7C+YbOE6zckRaDVlvQT3EUfE/YQvWQi2mdsS3WC0K73B9D/17tT/4UcP2lsG2+tpZuJ5KVQMK3mGEt6+y1ti/37okKaDa7uecwvuJOfL6oYrM+TdOKZyaNOiVpM+yZY1ftLtujVprHrZryzXEpHNcR6JiyzGRVM462BaO6W/K+rfWjuIv2ErdnSJkTuqq0D+cVJWE2G/cp6AjTG0MfbZc26MGX6Ezrby6RDSuvvF150c+JDE7F/TmslPooFsjuQF/pNPRgZ11u1hFN0fSBbvb8TFZ0GwrkdoPqLB2oW8vY+vm57EFQVj4qmbpn2tsr2nHrrBZrvTavNmS5Rtxp0pJv+4NDuLi6Fko3aoaNvizvx8Eu93Exhs6RDS/lza/2OoLLVwu9mGWhXoYykHzezyTr2nbI/arBzWESs0YUylToL2tR8uKrqEelfCNTeoSjfcYDGrZKRUb77REaElJbDtb13N5vWwul6/AcI36mpjDkEfLIVli/n0Tp0klnhctEGwE9WL8ftYuNlBLCrzY+3E+rzW3K+g0a6HQOMNhV94yrR9SxIrNR3eNrXahXBWIyEuCOU3RCmORGa14qtBZnEbfIRHwMOYAqnfRUsU8nKeD4IGDIxlgfYvZ8ShzzVHiZMii0Z2DHFQwp22g5snBe5H1gbA55RthFLC97Qb4bW4k/oFfUp9eSRo8JcyJRf5eJm14WLmNv0UfqUJz0Y8FlWVXp+MrW0UnIz6hfUGu8oLKDyQ7LTJo2BSYDsOsu9qmCUaT3VJ3eYUG4haFEOt7JxJc2jqNIJVzLO0G6JI5dmLBK7c2w0berGFVcRb+DNvAyQEZl7njJj0AXavNl3EPQuoxilq5y3ox0uR7rxJrC6LpvjiS74pr9XhYtnLQvJ/9KHWiaE/rOvxFIxjEelwSSGIUCfJFgfl9dvbHi2+J0scljdUsSHpOrfgsnSgSzma3fkEYgcs3SU5NYDbGh7xHUPg1VhkfbneLoBWQQVrG+8VTfqPG+swEH97qdy8IobzK4XsskgraebB+QbumQhdQH3XlPNXHrUDa+VzFOMWONcacppC707uAETEs3k0CoEmnF15RHySC/1njCKSq6lJzpvKUmm+vUFasQoSqhk1OeQM1NEbEy1F1HobIh9aQfuEm42gpDpxM0QXQXDIUnu1/Dp85oA1e6+TnnGU1XTblpnHTO9Yppj1/oxtbcTZZLVCMFg4ZUIYZam62tjK1j3Jfi3amG2gvYpaR41faAMVtscyf3VQcIG4du7EkdcXPCrVLyvH4VevHBpg9tI5oUEtNZKaWkEFQN151q5b5HO2Uz0M6QFHa9tnzHn7qw0hT0BFkesYelu35SCHPZpQEE9VyQhNkNTiQEWgoc6VuONo7XgLvufD5caSGi2Jeqsa+XYyfWxkmeks2RDzR6e5vILXaw/HItZnJIL3eCLu04JoBhNzyp1rQRx0GDqqPSnvVjBcMC6hFCYmLI3oJhLjfjlK/CHVwg522qLVdu0h47zh2P9X6zCuBSdfX6vr7gYd4slVCXh1oSIX+DbFIE38TMGYWo1aknuxajJIuYVjdbntIQdFQ3e0eUe6jykOPW7wD8ID1MBNcKtFGFgQlwB6/uG7+7D8QuKmBFUTWVthhaWB85jQC7nitmZV18zOhQaargchBwc7yhGps3eYFm5bqLN5cjvtFD+4K5UjgcNx2ZAfLqE9PfBzGva9i0bg+V6+RwJIasgvc3RS1G/mTvKLKGGLBFu6fjVj6SbnkPuoBjRf9oqIhvLUP8lnjcQbR1RQp1RpLLZkUk1FHrYhW7JDGz6wgAuPlpRDfaSsZEITcCvD0lyJKUT9fknO56A43bHLtGRzoYlGKZktz9wJpbBjlQG3y/Xa77aarueb+8otw9lVh2lZtLyy9cPE1GKblIvOliV1RonVCqrGE3kMZR25NLb4WOrSF68oSs6bN0D3uLYKYqkDbeVh9trDKuOxa/ysM29bzRMe0JPyZaR+Nx1ZNqnNXYrsz9ySeWvA/6HAUV1nlESutc10H34Ne6T8HwpuSwIs0QNO3UNbe7SZKxzrcwqomwVe246VRTChcbWIPbJ2XaUXUYQNZGy83ePrTnYUWxHKoE1+1G1fMRpaWkc/toHaJVXdkTvWzwadM0e6DL8blmSVT5eqNyWg1CAuC62LQXH6v44mwsxw2ydx1P4ww81KFel/BeIE3dcRAsHbbxKgjI6tDB1O1+W0aNLNwDSMU3AKxR5K4a/UFxL2ItH01dOG6oO3Fqsiluou5qI9zE2O3JhpHDnrAwzAMsMUEplidOtjsJ9+XKaPDbnVRUHr3ZN02/4SCDsAJbbWzNZLXstm4QblUXQd6uetCwXqmRW/ONxu7zwDv13CoAXRQiF0O0oegIQaCbTxWX/Qk5Edmu9I/m+oK1eoJTh9XqdiZqxkKrPIYELfB5Ym97Zi4bInfUUh9O5S2qLa8ewULdEhlWZ0xWCizCrVh21cNVR24S3Ey3o9EnYKeQkF52zVGxwNQEhQBVwpv9HnGyK5SmW7xuBMwrvZvmqCQnaM1dEZMqiooSrOW6Ka9ZctKb1LGaSlgjUGmZpSMfkerOnZXJSoFopKxuWT2sMNEdjmJiWJv78UJC60SZ/9snuKSxE0sV5GKmHx45/uZGu+WpibGdMU0UTmPXcdQ3vMsXh70e4VrYeZi38y/X7gIZkWUi0T7op5jjWj8dDivIQ4NSX8N4qcMQpvAptjmv8EaP8qVk1TsixSrcC1fEMptOZTbJe2WvH043iRC5M8Uf+lO+heAegruu2oy+ds+hrUfuU7fRWaw9O4ZfaSm0hFpUx8ouHm8H6yyu703boJsl5MG5FnM4Z+4gjTa2g1asiGa3rQkFIHqhLjmkuWbQ0WhgF6lEVJz6kasCeWMbXTdu8j2NrQ83KaEkljYnqapObECBLoA45+1Wj9CzfBgO+9a/Lre0uPULj1lJ6wpTSbDBUyoyH4NqX2M5OSD9mCR0Hy89P3btqZ/4ZYsb+oY69zKOba0djEsrPd1uzEMAVYKwzKFE9QmPgFHe8Jx7Z0xj2G1MD9DjEgSA2GyyMEDPFGF0KhbC56HGuC0zEr6kNoTC49GKC47aVrKxvWN1S7CT86Cbsz95NRRZKFqvEHu6tjQxemuywU6Yq2P+8pj1VaRBkoxUMenWDNehDrXco1rb1p3HiuySjHXo1twTqFif5D7tc3J7NTTzQF/EYHT1laZRV2Zl38qw61edzTkh7BqeDvockqW3BZEYdZQf0dC57UrZO+9WJddTilhZrRW4h+sIK/gSOnrtyRWB0cEmO6sJDIvZ2tpMJdsF6pkfLsSdheujU631a2+QJakdVAeD20jQRXvv0ReZPK+DFJva80Sgq+hMYQduakW4I+lQRHmVh9kwdR2oQg04oru+vpJcsnfOCGmB0pQgamAliYbZM0VRb+/f5rOo14nSf/lll/kE4P/ZYcPzzODrAfbj7Ma3vU8PXZ/+6yb+/P6tcuPZwMeBS5224euo4p+OWz783fPLWdr4fL/k60na86CuscP5Hc23OPdaMHj8Uhfp43gbzHDmlxr8uv7yehfi2+HUl8e7PuCyaCK/mmX/i7dv88tW89G178XAgtdl+DqTev/mvd7J+DIHy6/K2ffXoShwGfsIf8TefvtfWDzEBm4rAAA= -->
