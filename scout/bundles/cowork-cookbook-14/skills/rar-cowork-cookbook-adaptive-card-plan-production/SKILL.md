---
name: "rar-cowork-cookbook-adaptive-card-plan-production"
description: "Produces a reusable Adaptive Card JSON snapshot of plan production status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_plan_production", "rar_sha256": "c7cb69a5f7d29012bb8a9f71246a2f5a7775cdfc93415f6bd6faf3cb25cb86d6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_plan_production_agent.py` and embedded as the fenced Python below (sha256 c7cb69a5f7d29012…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_plan_production_agent.py` first:

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
    "version": '2.0.0',
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
