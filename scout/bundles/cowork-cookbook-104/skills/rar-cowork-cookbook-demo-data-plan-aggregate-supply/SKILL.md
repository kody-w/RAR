---
name: "rar-cowork-cookbook-demo-data-plan-aggregate-supply"
description: "Generates and creates realistic demo records for plan aggregate supply in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_plan_aggregate_supply", "rar_sha256": "d7086b14b497ff08a65e09c0a6fafe6dda6673037abec220cd9b8f904f633c25", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_plan_aggregate_supply_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-plan-aggregate-supply:bf6d8ba5a6e4b1a71a628c4441f4aaafaf913f51afe867ecc26cce984f3e6191", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_plan_aggregate_supply`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_plan_aggregate_supply_agent.py` is
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

Plan aggregate supply Demo Data Generator — Generates and creates realistic demo records for plan aggregate supply in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-plan-aggregate-supply
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_plan_aggregate_supply_agent.py` and embedded as the fenced Python below (sha256 d7086b14b497ff08…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_plan_aggregate_supply_agent.py` first:

```bash
python3 demo_data_plan_aggregate_supply_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_plan_aggregate_supply_agent.py   # or on stdin
python3 demo_data_plan_aggregate_supply_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan aggregate supply Demo Data Generator — Generates and creates realistic demo records for plan aggregate supply in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-plan-aggregate-supply
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_plan_aggregate_supply',
    "version": '2.0.0',
    "display_name": 'Plan aggregate supply Demo Data Generator',
    "description": 'Generates and creates realistic demo records for plan aggregate supply in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-plan-aggregate-supply',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-plan-aggregate-supply',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dcc03802bd8547af',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-aggregate-supply'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/demo-data-plan-aggregate-supply', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataPlanAggregateSupply(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataPlanAggregateSupply'
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
    print(DemoDataPlanAggregateSupply().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
