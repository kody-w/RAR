---
name: "rar-cowork-cookbook-d365-forecast-to-plan"
description: "Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Forecast to plan process (5 L2 areas, 45 L3 processes), using USMF legal entity conventions via the D365 ERP plugin."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_forecast_to_plan", "rar_sha256": "41c7eb3df0ed6f88a8f92d34d527f540fadf5ab3e7f614dc6e783bbabe5991bd", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_forecast_to_plan`. The original RAPP
agent is preserved byte-for-byte in `d365_forecast_to_plan_agent.py` and in the RCI capsule.

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

D365 Forecast to plan Expert — Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Forecast to plan process (5 L2 areas, 45 L3 processes), using USMF legal entity conventions via the D365 ERP plugin.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-forecast-to-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_forecast_to_plan_agent.py` and embedded as the fenced Python below (sha256 41c7eb3df0ed6f88…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_forecast_to_plan_agent.py` first:

```bash
python3 d365_forecast_to_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_forecast_to_plan_agent.py   # or on stdin
python3 d365_forecast_to_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Forecast to plan Expert — Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Forecast to plan process (5 L2 areas, 45 L3 processes), using USMF legal entity conventions via the D365 ERP plugin.

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
  Upstream entry : https://coworkcookbook.com/recipes/d365-forecast-to-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_forecast_to_plan',
    "version": '3.0.3',
    "display_name": 'D365 Forecast to plan Expert',
    "description": 'Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Forecast to plan process (5 L2 areas, 45 L3 processes), using USMF legal entity conventions via the D365 ERP plugin.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'report', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-forecast-to-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-forecast-to-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cdf3017670605fb1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan'], 'recipe_category': 'report', 'recipe_type': 'prompt+skill', 'upstream_path': 'forecast-to-plan/d365-forecast-to-plan', 'uses_skills': {'custom': ['d365-forecast-to-plan'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled'], 'confidence': 1.0, 'deliverable': "The recipe's output, produced on the target platform.", 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Save time and improve accuracy by giving Cowork a persistent expert context for the target domain - it knows the right entities, the USMF tenant data quirks, and the honest-degrade options before you even open a task.', 'expected_output': '', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Activate the **D365 Forecast to plan Expert** skill for this conversation. From now on, scope your help to the forecast to plan domain only - use the entities, USMF tenant conventions, and honest-degrade options documented in the skill. Lead with: 'Using the Dynamics 365 ERP plugin against legal entity USMF, ...' on every D365-touching prompt.", 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-24', 'what_it_does': ''}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Forecast to plan process (5 L2 areas, 45 L3 processes), using USMF legal entity conventions via the D365 ERP plugin.', 'example_request': 'Act as the D365 Forecast to plan expert and walk me through master planning in USMF.', 'inputs': [], 'model': 'claude-opus-5', 'when_to_use': 'Call when the user needs D365 F&SCM guidance limited to the forecast to plan end-to-end domain, including its entities and USMF tenant conventions.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt into the target platform and answer what it asks for.', 'Review the output against the expected result below.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class D365ForecastToPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365ForecastToPlan'
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
    print(D365ForecastToPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
