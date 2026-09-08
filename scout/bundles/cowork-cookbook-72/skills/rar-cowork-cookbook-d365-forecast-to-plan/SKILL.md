---
name: "rar-cowork-cookbook-d365-forecast-to-plan"
description: "Answers Dynamics 365 Finance & Supply Chain Management questions scoped to the Forecast to plan process (5 L2 areas, 45 L3 processes), using USMF legal entity conventions via the D365 ERP plugin."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_forecast_to_plan", "rar_sha256": "41c7eb3df0ed6f88a8f92d34d527f540fadf5ab3e7f614dc6e783bbabe5991bd", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
