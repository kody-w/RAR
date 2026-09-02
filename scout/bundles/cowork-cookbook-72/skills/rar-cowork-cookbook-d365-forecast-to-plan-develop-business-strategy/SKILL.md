---
name: "rar-cowork-cookbook-d365-forecast-to-plan-develop-business-strategy"
description: "A Dynamics 365 F&SCM expert scoped to the Develop business strategy area (a level-2 subdomain of Forecast to plan) - covers 10 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_forecast_to_plan_develop_business_strategy", "rar_sha256": "8fe55d7da2ecfffc82ac86d5a92cdd9ab16c64fdb23570ec8478d42c84a182d2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_forecast_to_plan_develop_business_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-forecast-to-plan-develop-business-strategy:b127fa5a87b0ad437623fe10ab77b090b31d7780498ecf3d845b9fc6b7f30e9d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_forecast_to_plan_develop_business_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_forecast_to_plan_develop_business_strategy_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_forecast_to_plan_develop_business_strategy_agent.py` and embedded as the fenced Python below (sha256 8fe55d7da2ecfffc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_forecast_to_plan_develop_business_strategy_agent.py` first:

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
    "version": '2.0.0',
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
