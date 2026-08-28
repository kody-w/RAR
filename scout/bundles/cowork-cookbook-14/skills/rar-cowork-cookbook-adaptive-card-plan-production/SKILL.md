---
name: "rar-cowork-cookbook-adaptive-card-plan-production"
description: "Produces a reusable Adaptive Card JSON snapshot of plan production status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_plan_production", "rar_sha256": "2b4ffbaa45445cc4f1d6d7435fc1ea27713f08cb6e2548b03c7d85df11ec336c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_plan_production`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_plan_production_agent.py` and in the RCI capsule.

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

Plan production Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of plan production status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-plan-production
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_plan_production_agent.py` and embedded as the fenced Python below (sha256 2b4ffbaa45445cc4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_plan_production_agent.py` first:

```bash
python3 adaptive_card_plan_production_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_plan_production_agent.py   # or on stdin
python3 adaptive_card_plan_production_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan production Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of plan production status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-plan-production
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_plan_production',
    "version": '2.0.1',
    "display_name": 'Plan production Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of plan production status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-plan-production',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-plan-production',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b604d47ba6c87be3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/plan-production'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/adaptive-card-plan-production', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardPlanProduction(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardPlanProduction'
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
    print(AdaptiveCardPlanProduction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
