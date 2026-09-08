---
name: "rar-cowork-cookbook-d365-forecast-to-plan-develop-business-strategy"
description: "Answers Dynamics 365 F&SCM questions scoped to the Develop business strategy subdomain of Forecast to plan (10 L3 processes), using D365 ERP plugin entities and USMF legal entity conventions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_forecast_to_plan_develop_business_strategy", "rar_sha256": "5085a7e42eb0eeb15535ab3b71b5ed5797a9e9e894417669bd63739c134a55df", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_forecast_to_plan_develop_business_strategy`. The original RAPP
agent is preserved byte-for-byte in `d365_forecast_to_plan_develop_business_strategy_agent.py` and in the RCI capsule.

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

D365 Develop business strategy Expert — Answers Dynamics 365 F&SCM questions scoped to the Develop business strategy subdomain of Forecast to plan (10 L3 processes), using D365 ERP plugin entities and USMF legal entity conventions.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-forecast-to-plan-develop-business-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_forecast_to_plan_develop_business_strategy_agent.py` and embedded as the fenced Python below (sha256 5085a7e42eb0eeb1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_forecast_to_plan_develop_business_strategy_agent.py` first:

```bash
python3 d365_forecast_to_plan_develop_business_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_forecast_to_plan_develop_business_strategy_agent.py   # or on stdin
python3 d365_forecast_to_plan_develop_business_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Develop business strategy Expert — Answers Dynamics 365 F&SCM questions scoped to the Develop business strategy subdomain of Forecast to plan (10 L3 processes), using D365 ERP plugin entities and USMF legal entity conventions.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-forecast-to-plan-develop-business-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_forecast_to_plan_develop_business_strategy',
    "version": '3.0.3',
    "display_name": 'D365 Develop business strategy Expert',
    "description": 'Answers Dynamics 365 F&SCM questions scoped to the Develop business strategy subdomain of Forecast to plan (10 L3 processes), using D365 ERP plugin entities and USMF legal entity conventions.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-forecast-to-plan-develop-business-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-forecast-to-plan-develop-business-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '30c006510a1992ad',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'forecast-to-plan/d365-forecast-to-plan-develop-business-strategy', 'uses_skills': {'custom': ['d365-forecast-to-plan-develop-business-strategy'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Develop business strategy Expert** skill for this conversation. From now on, scope your help to the forecast to plan domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Answers Dynamics 365 F&SCM questions scoped to the Develop business strategy subdomain of Forecast to plan (10 L3 processes), using D365 ERP plugin entities and USMF legal entity conventions.', 'example_request': 'Act as the D365 Develop business strategy expert and walk me through this Forecast to plan process in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs D365 F&SCM guidance limited to Forecast to plan / Develop business strategy work against the USMF tenant via the ERP plugin.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365ForecastToPlanDevelopBusinessStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365ForecastToPlanDevelopBusinessStrategy'
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
    print(D365ForecastToPlanDevelopBusinessStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6d5PjxrbfV6HnVVnS4+4ip311qwyCCQRB5EBqVSskIgcig7K+uxskZyXdKz1bz/7HnJkigO4++fzO6Wn88uZ0bVTWb5/ftMApFjsny+IoqBdO4S+4cijrFHyVqQv+Fl5ZtHXsdm1ZN28f3vyg8eq4auOyAMvZohmCulmsp8LJY69ZYCSx2P53jRMXty5o5lnNovHKKvAXbbloo2CxDvogK6uF2zVxETRguK2dNginRdO5fpk7cbEor4ttWQee07TzsioDQn6PwIsjtqjq0gOrguaHD4uZQrhYzzw3qgymdSFYHBRt3MZB89DG0MTtIgtCJ3s+n2Z9+vkSSPYJ6BOMTl5lQfP2+cefPrzF4Prt8y9vXuY04NHbTPtdEr2UgRwv8Vcv6bWX8IASGAzBkmoCpi3AfRXU17LOwSM/uC5ed983QXb9sPj3f08Hpw6bHz5/KRavz5e3+UftioeZ2hKwBFbznMpx4wxI/mnBZoMzNYs6aLsa2NWZTQcs8Om58jdKwLr/mMe+fzL5FAbt91/egBOArEDvL28/LMoa8Ku7+frTTKX6/odPWQl8+f0Pv9EBDkkCr52JAak/fX3dv8iCib9Nja+Lr5q84V68gMXiKgDEf6ff/HmK/iL3MsnX5+Tvy+rD4s8pz/r8A8j7jD0X0P1zssAGYOXbp6SMi+9fPOoSeNspvOD7H/6KrBcFXprFTft/RPfHJ+EocHxgrZdJQDDOLvhpsXzp9o3mX7Odo/rvaAKmv7P7Zqi/ov3w7D+RzuaA/ebLPyX3ZwuW/1j8+Je6/WcLPiyuX97WQRb3IO7cLPi8+OURIj9+5//28LuffgWk/7dktLKrvQeFr7lTxFcALV+//vhd83j83U8/ftdVIIoDJ//a1dmf0fwzuz74/MGCr1nf/3Et4G8UaVEOAJjec2jxS1n9t/rXTwvTyWL/t+fN58XvM3H+LBezEu9Mnyb4XTY2QNbf2fGHt18BDBVAm857DAP8+Ld/W4ixV5dNeW0Xmld27QI4uI3zYBZej+JmAX5n1KgBOtVNDAz7mgfif/bwLDEA1Z//h/dA94/eC90hHwDc1+sL4b625SMuvvpPkPv6jtFf3zH6508LHbAp6xggLcBUlZXlL4UTAkCdRajqoAnqHsCWO7XBR0D343yxAKj889/k9PVB9FM1/fzA8fiJiirHz4jYdFnwadbdioLipakHakQwBl4H+GWlB4S7xgDXPwCbNGXWA0Sd7dSkcZYt/BiIAQra9KANbPl5Jvbzzz+7ThN9KZ4Qji2ela6BwIRv4iw+fgRaXrM4jNovReBF5eK7X379bvE/F//ZqgfxmYcM6srLU0DCgyadFiDzuhxMA04Ebgew8vDUL7++bA3IFKA0A7/G17mqzYtB5KaB/254bc9+RAly4QazeReghpV1O1fGuP204K+Lb/ICpvPQXDmiEpRWP6iCwg8KbwJUHaDON0sWZbtoQHg212kus8GD689u7TxEzAEEOO3PC5GTQZ0qs7lG16+6BRaXRQzM/y0sns8Bkfq7ZrF6J/FpcZpjdVE5tVNFtfPicXWefgH16X05IO4simD4UszVOZhN9Uicp3nAJGAZ7+XSj7PPQYnPAUr4zTvvxxxnrqb6o6rWX4rmlRROPbvCA0UCMA272J9LxX+8QqqJyi7zH/YDks6UXl7wX155xOCj//jrrmYzgkxvF186FEbwxf/nDdOsL7vbqZsdq2/Wi81JV89PP8xt4uyvZ2c5rwPB+My531qYd5h6R+svRRaDoKqn/3jOfHjvNeeJgF0NDKGy6oM+0BT4Yab7iOw5Uuv6IfiX4r0sfADB8sBA4FwAA+nTju8M59F3SSOQ6/P9by3CIxJqf7YDiN5F1bkZiKxrEPiu46VAqnrOzpcnQZgHs92HKPaiP2g1Gw5EE6C/AELEIN9A6fj0Daqfo++i/2HhsxOalzy6xA4kZ/0gAOQIZgFnDw1xCzDKaZ9dOdDz84MIUCOv2ll3F6QH0PT5MKiDWxc3cTtD4dOuQQVQ+eP8/dR0fhqAKPXmDAFxX3XAuo9MmaMlB30OkAGABUicPC5A3QdGeRnhQdDJ57QHsPpqTJ8UH49fCgWP9JoL1vvCWZF5zdwDLK5AdPBk+j066H8WJoDeHO5Pq/1zpH3jNtOeEbIBKAc4vo8+m4VPz3r/bCgW73Q//8u25/u/tzN6VHDjjwHweRG1bdV8hqBn1X0vup8APkFPWZtHAf74XhY/tuXHOXc/vsrix/ec//ie839g87TA58XfE/UPJF6p8nmBfII/wfPQ8RVqrw+wDPdxdf6Iz6NfCjX4DUwBe4A+7Qz22QQq/rfK9z4FlL+wBlACJj8rYTMX0AHU7Af0A6d8KX4f+3PugcpShHOsNuXvMOHRAoA8ePrwW4UCQ0ULePtzOxkG837ukSlN8Pa56LLswxtA2eBv7uPmipTPwd7MO0GQVjN+x8Hj7oEdYztf/nEjLD0unOwTgGuAU1nz+4B81ZG5jv4ub54Kf3ii/YeFD/g3c90DCs/M55xzGhDEIDhmxdqpmjV5bvnmJvFbB/mv0ligPM+w55ef50r14QUOHx6F4cPiWwMPuL62VI+tcNGB3eqP8+ZhNsNjyXwB1oCvb4u+/RPADd5++he5gGAPxAG4PdP6TcjfppaPTcesAiDdPvfIv7wBkzvABs7L6K+uFUwHCfqxmesxBGIUMAf3z2gCY/+3/eyLXBM5oIEC9AiYJhwqwNHAhYPARQgCIxwXcynEJQKfoBjKYQImoBkcRyiSZFyfxCiM8RAMdwjCvwJ6zxD9Ovcg8SziLB+wzEcQ5cFvw+CR/9LtqctsuG/t82yDl4q/vLkkDmbu8YZnnx8OYhAXQiF3jGzItqFtooi5cDHLAwIf9W2+k0pCX+1ictifse2BYgsv1sdDGVs2OfJjuGPSa3NkxmvTMJQPe77gVagYqaVJarzuk0BD6EpQSCKLtNvLxUSS0GaHWUkaD3ZM3UQDsazyNgiWU5hmNTL3ranGV4gmGSg+cEhvmjvhxLSG2wnD9qjfKZXu9HZ5LNDWNIuddc6lM6GVmqk5t9a+sW6W9mU+JDiiphq0QQVEKSf8hhLnTByDhGiuSacRG9s6R/4tGuXVdnvmAhel5GGdtUbtbi/V1gxGoTRFHtqvx2uH8dmmzoOksMZtTioYw4kUPQTrFEUh+U7hTKePFE+Ty/5+h2A1sPHVthZug9rcKMsydlSWpSuqO2nRWrDjexxdoPi0Eqq7JqzTS7XexDBvoYRP4vpByrYot7LNM6JYsLcnpnunRFV8O7vbO4Fn8HZI7ZXN0qhYorZxIjbafrOmzgcztfSo9Z1IPlOBlVB2k911CmGly+FU3VgNzkZDJS2OJSAjjg1pNLnKmWTWkfktN64uYoNoap9DtudG3WSIgkBdNhbOrTrxcG2nzPDTQiPtwCKYM1qs7kWcOOWFTZPqsrkF6/ZsiIqDBgZat+e1ZZrbXkgO20TK2SuOBYbJHVHFVGCdMVb2jbiXHQ7fzA15kjODttGpYO7aUVMGC1tzTSk4Xd3zF+14l/E1VvBq6m4SPDKqc3UqxAu+Px5hfTN25/3ucpBY75TWR+UqGzEryJG7CsG2OMcryJoGo+lZ/RgcebMeuvOWHduWbZFeEeDpaCF1XS2Ry7ipDiLea9RWak4Vk6MXxLDKct9Exz7an51CGncZmo+2veQ6yu5WkOhWSny49IO5pKNOOJwL79ApcC3HvSBayRI+urguTLUQM4UKe5E73E9yAomnNHDgK18qrXrKpgtfIQZaaZyvJje8ujuPP8yUYGYtj855Ireb0biL6h1iQmis+j7ZdReI5Ex4WdR70odGsV91ZlmBfEwReq1Oa26QU8qPQ3PSs2QTmEaAatbKFmChYptmLCFFXRaFNSh7uzspYuOyvq0Ijc228GgSlyolUgOK09OphuntFU60WuUz2zlbSTkmqZlwVYQNFMfyLg1vQrvMKVYpoizYOHInn6LtlZcP9CTBgYIe+pKBY4LLl3sMDe+6g/ro2lm1BqJclP3lkHAo54wtm3du6WyLdlOmPa4GPaXLJRVuQgsJ71irBVaICiQSK1CI2QnXmKfbVnNWsocKVE8I9abu+qjYOMhlVewI9TKU2SCtQN6mws7HbrmBnhS78Q9KzRTGBlnJmN7qIhRnK8GP82M5Xcll2PIi5IWlPLGQYRjLYtWhSnuozXw8iDtfHiBXbh1d2MIr97ge6ENG7YT62Esgdm/haASpHN/VppiApZVVxU2Q7i3xM73Mw2i6J8Y5cC6VS9t7onSIsoXykLdVkPa1XBZK2EVmp2zzU9dLYbLLxunGrce1y54cey15YXZv6HAr5RtcvQQbRBMbHNYV2wdxa8pirG2vxCEKiaTZ0euUalcG2g2yfCwzR8f0jpHLpEJcVi9FmfGBE6SG0huK7zZZjSt8hZ6QgllxJl1cL8y5pbrqauAcwVwOdiV7DK9VWIttDEkw8l669FPA4FsE2cMUq0oK7uWDQoHm3CxPqe3KvrlDBbZbelh5s3u69PjwnFnthVwrPT8UilJGO4mP8nq/5bb1Xu9tBiOtvrlMnJ6WK9dKsTUccldNvdabI6U6Trp2oxvf7oNGAJjkqOytIg57XLMENGXl21oZCYrcVKSvniP+Ctcax0idGGfnrIWRcqkSWpQZJ33NwPoR4sirxekmHm8cQtwnA+m6xQbWjodtGhg3frkMMFCwemy7s6xI6YwLQFdyqU83VZC0PSXC6HJUyf3+oG3daRIo7AqGuI72ZTQqdjdyNS73I+37V1lfWncIgqvxqh2S/D5ZzXRaQrR13Ox5f6fWsNzjktPqm2pL6pfg2EmDfqtb7+hc81EWMP8MsRi3PWlLycYGRr4St2UnyO3uoJsIQLhYWynIxT4iVUdDuVGW2NQ5uG2ubxxfnlYRot66fMfXR8ZVQ6vyGVvFLc5vxv0hHQ6uxMdulQgXnwH4g4bTNpiOVckj7IU6Oil8ZEpoiUjDqowTuEtjTdpf15u1K5zi+6VC+IR2OHq8sMfckfsb1UXrY26lHRFl7CoTlBK2T+tYzqdgiWd4uFHFTT958uaSrONbzvK+V533xWVr6eixI6+7ZS3URpoeAw46dFNNozXA9BIWCHw3+oo+xBiyT1eNcD8bt+auOExJLm+xGvHrYQNXHmHeqrhpoHbqLoqNm6csbfCyUlOOPx+gYbm2hmYfFpssL3C/VhRklQr7iihYNrURFdnurvHECRWPbVS+g6N1kOaIrpvtsmlwe9oZ4nkVRUIh0cemmy5Uqel4ah1W3KVlBjoSKdPgoaarTAVVOSbIifWVPN90VL45Geoe4mlXEYg2aOGxvK7Zcyh1EtPFvQGdpbWXavTkSvHmBlWwkjI7J5ZL44gEB2brO8LyTt6wnX2cLHMXKtZBQCOOWrtifjHMm3DmWUybnKjad62SbXVR2R3OCO3Uo6tBkLqpGKsUpbCHLle0RM7n/XJjnCrCXReXu07n59a3y4tMEsnt2LayyyMAOg+ebeXjtWAjXeEEpUEwpJykTdXEJ6Zs64I/aJ68jyhZF2C6Y5ZGc0Z1fnk3BdgK4LuxX+5l0QpN0BaLPYzYq+NW3nqhxosKejrtXfJ2rhTMVQ31wp2cMnDY1s9c7tjRcs62NxR3JvYQw0sPN3xYqXh48u2Exlc2ZSGDfUhlYTx2DS00oXpWONo4iiUurzY1DJwnZksTPq122MZRpqE508fruIrY7crIMpM9annDk9mAikOibXaiqMSSImcaaFUzzeOJkg7DNYuptzZNw+WZvfstKuj5jjxYG/8ghjuMXw0GBWAh1A9KTohtC3aqRx0zUfxyCYQEIhvH2eEeO4HSkqr7Jl/m0qqGAAj30mqjmsawsoY9YjLqMFaWQtjmgenFijX7O3zckTkjcq1cEgSIhTEHZbg+ZceldoI7MaR6HpP352RirO16nzcNX/XTNhcdR+c5T7ISTjCLCneMS6MmzK4lraAYJQbJW9hpAtns8po01/Aahx2kTMlqE00wsq98fLJHle2tnRt3hgTAVNltLnXW1VEgOLf1+ZLYp9ZnyfJurKPRgnHi1B5PvNiuAqUXHcnd6yTkbY3pdMEMbqwZXfQhBRR0fTgdi4kLi2rd4YXToL6cZzwdoGdhyMmlxiBLwz0cyzHS9qV3WbGn2osRzeb2ltAU7XV3vOz1+zlXlKzkUko408Vu2RFZIe04pppW5LRbbdW+2bK2fcEPm3a5XPL4rnPUDSoZ+30ODXcR5DApEl3ARxe7Z5XrKEYSRClDBcvBkFLKJkGCnaPtysyjxrtGHvSdZeI+ej+q7lDoyzDXNJFdhVxrsfrJwwz9hvSB05buhPo1MFO5iVlnXY1pe8dde2pUUhZ3B58gnVLK1uqW7MsNfq2i1A/Uftf5bYne4+OGbRP9iKLO9rBpVhl/NMML3zr2xr/lnYlIV+SGHoe8GwZkmTO57clQhKT2QZGISRVNYx3WtXHb7Jyp6GwYHzdTjmM7SBcI1ZeKmHdauyrcTrP258NAF0gxMF3JQ9nKWZfjVFcnzzjJQbRREy7xSdDjTdcLvNP4mlVu5kG96YV1yBLT8xTsYOR0rLVtmKBSEuGKTvroiOz97kgeDjrk3kzCLvRDUDrxxWpS0zk6dea5Lno0IdPe7AioOVDAPcfyTkqMWUeYwTfMTvAGYNZGcXriGNQ23zcDo9T+vnZI2eJI2YQVqtr1yS1QQcOks4xjcWVnn9Vu3HoVuR8Ddx3EhOjb0hjj3U7P1UFaN/u8G52yjQCmVephiZlFI1EBm02ITZOUhLQ64xE7AkGwPSq2XWjUFiGLRIJEJlUN0ykJsFyFVqpZqUcjII43HgApAzk8n1QCNPipk+9P8Mni4IRYQgYcht7t0Kigdk8WVa7SVlbZk+K52qq6l9uqt3OP3LYZbVP70nJyu9h40HYXClRWHDBMWi7rxh5gJuuDWkVb6lIkYZBLECT31+VGHkZfu10p5ATt97Fl6YlxlwMMPR63ISkaMEGaVXs730T5KFqTaCdaykPkUT/Iw46MMrLQUeecIPEONhynA+7nCdZL7y2JtWERLJ3Es1q3PynUBWtypL0Kyw4NaYozq5PLeglXZk07UMl6j168M4zS+KkeoIrIcRhDhgOMyRSdrehQVUhQ9Bhmyi53fxwq6sqjKxylsGPKF51C1LvbcFDwlXnzCAjV7aBb3tte7rpbTDhMEBvObonUSUPKMFIzTe+q5z4qla3iJA57SbkDQ8sHymXuZmFS/Y1PNcVvb7JXCTdeU+oknHZI4wo0hGVObVuqeA7C035/RKcjaL8JpfFwYrculrUvojTYKKxsDV7yEpxs1OyQ8ikSy0k8QIq4am5ht2UTuN5tSdqFeyqM293xNvb1JSTT2Jc51tmZfmjwsnGocIpNRa2PajtPwvReUDElZJK2pNelgqzJ1oDITk62E6SgUngV5LQ/d6SEI8JavwinfdpHjMrW7Dkq+305DDKIX0jqbvc15Kbri9FutnzuMlu3OuehN4knM+FpHzVRvqNSISEY9iC6mJbTjF+h9864+qw+7rnev4WDOfb3/ur7/tqaTKTGmNVWuKijmgT+KnDRdQft9paJrK8RvD3Jl05WJX9kMhps/5Esak7EZu0hRIGiIbZFG1QSpOnUNBQS3HNyB7deVE1V43jJjXCSlqSp/fae4yxPtXxh3k/7cxGyoyNDxugUJe7ywXrED9s1al6NLvHVPUuuEc6+DisqQakId8KOaR2Mjk+7Du3sK7dekvc9hPJJAZUE1LodMVL+PnVESM4wULIu4WR7XBvQhYcFzZFKq22GLqnT3T3g0ElsaMZyS845yN0+GevoSJE0rDgSw0iWlbKNs4qFwtg1O+tmE2pzB+1Pb9+g810NZbvgN4QnB42LnJeeTjokds/9aLVH3Y7SJ2jalvsznxuqZSxVMsVq7FzVW3pXMRumQ2z4VvYJgitCcj7B4/506BUzT6/n5Vjg2lGAGb1UR4jlMvgupxB7Pu8knx9yZjrJVaSrpgR6cCiMWTm7U+vSllTazBFS21kYOYy9T+cTvC0uiRy1eudA6C0461SNXqTQUmREnTYDbYRxdcPtjmpY2b5eUeKUMN5NtfNLMwkJqJH+eGfyGHVNc2maK0I8lei1umbFMqJWRnxpkdu2Q3cF0h39PmhdyyPOWBFVKO03NSTJyCrOCJfNZXa8E1s66JCsToNmwrH9dfDWoV0xtQiTDM6CIr2Fr6LZWXHdx05xdUPP5WEvWy2lNsTu7nBUSBbLSGR3Eq4Vzu6siNLC3id96KQjsqbaK9+xwkTGD4ieFJKMo+fAo4RD7ZEnww2uVJNO7jJOPKKW7v3K9e53GKsROiwhKE1u94Eo10Irb/Ycx5j3VNkg5f7eJ4R3zW2sZSoxha80I2EbLAi91nDO0vJAqZSZeyl0Pd01acr79UVf4cs+7yQihehNwqjrJXe+MCoDrQ5KeiLbRPaO6+QihA7t20p0uolXbFv4e9FVg3F5PglBwKzvaBbcgVJ0lmhjaHWheMlHGDO64ACVHoYtoyNLFrwUGGu2PMrefcMVlkQqHMPUt7NihOW2O4JcAFtsiCg52lWT7CpDnK/gQU8b4x0JAeKW6pLbaziPX3K131ba1VI3EIklfRXhad/fA5yKM8wmbcKjzwljZcE5oe0Jo+/mpZSXrSJhNbyl1vfpfCKWmihiObAzpi3T4+pKcgq7bEcTtSCSZKkrnqf3xJGNwGvdnYTSsBMFtBVAsj/52Kq9ksGBDpZaP+ar9rxLxjRkuvtlHw53ExlNCvWtPokObmehrUyTmhFH9SjjUdNpJasblD156KD7rLklnaoMgeXARtENJwP18yXjNAduhVOhTVepgIZOuo4UXz7C5X7gVLewu4Pt8dslppIjJM4ucgvKviKhzCXY5kQvRYmRY7u67WO6XGcshQagXqxX+C03oIMni3tBV0/6seHI4lJKJ6h3CMK6YrS/tDIW91ZmIVPtFjQjSnOpNqs4oXXG2ukYwxb3BsXu6l7OBHVJ4PQW0pLjXSj0hmXZf/zj7cPbfAL1Okf6r77EMv/j///ZGcPzqOD90PpxYhM4/ucHr8//ZQl/+vAGGnog3/OUpcm68HVA8U9nLB//5pHlTGx6vjXyfnr2PJtrnXB+7fItLvwOTJ6+NmX2ONAGK74J+np94duB1NfHGzzgFnSNQT175590fZtfn5qPqgM/Bvxft+HrFOrDm/968+LrbKigrmbFX6egQF/sE/wJe/v1fwEliftRIisAAA== -->
