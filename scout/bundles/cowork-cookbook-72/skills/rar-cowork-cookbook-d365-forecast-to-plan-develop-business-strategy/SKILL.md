---
name: "rar-cowork-cookbook-d365-forecast-to-plan-develop-business-strategy"
description: "Answers Dynamics 365 F&SCM questions scoped to the Develop business strategy subdomain of Forecast to plan (10 L3 processes), using D365 ERP plugin entities and USMF legal entity conventions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_forecast_to_plan_develop_business_strategy", "rar_sha256": "5085a7e42eb0eeb15535ab3b71b5ed5797a9e9e894417669bd63739c134a55df", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1: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 -->
