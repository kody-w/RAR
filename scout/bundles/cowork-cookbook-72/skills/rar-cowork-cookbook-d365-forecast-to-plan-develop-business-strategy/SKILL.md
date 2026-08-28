---
name: "rar-cowork-cookbook-d365-forecast-to-plan-develop-business-strategy"
description: "A Dynamics 365 F&SCM expert scoped to the Develop business strategy area (a level-2 subdomain of Forecast to plan) - covers 10 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_forecast_to_plan_develop_business_strategy", "rar_sha256": "3cb025b1d70f69022e50ddd2b8158a8efe3a713ff8d4f53327ef20647995da87", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

D365 Develop business strategy Expert — A Dynamics 365 F&SCM expert scoped to the Develop business strategy area (a level-2 subdomain of Forecast to plan) - covers 10 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_forecast_to_plan_develop_business_strategy_agent.py` and embedded as the fenced Python below (sha256 3cb025b1d70f6902…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_forecast_to_plan_develop_business_strategy_agent.py` first:

```bash
python3 d365_forecast_to_plan_develop_business_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_forecast_to_plan_develop_business_strategy_agent.py   # or on stdin
python3 d365_forecast_to_plan_develop_business_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Develop business strategy Expert — A Dynamics 365 F&SCM expert scoped to the Develop business strategy area (a level-2 subdomain of Forecast to plan) - covers 10 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "version": '2.0.1',
    "display_name": 'D365 Develop business strategy Expert',
    "description": 'A Dynamics 365 F&SCM expert scoped to the Develop business strategy area (a level-2 subdomain of Forecast to plan) - covers 10 L3 processes.',
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
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '16049eab41a04023',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class D365ForecastToPlanDevelopBusinessStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365ForecastToPlanDevelopBusinessStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
