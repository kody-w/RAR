---
name: "rar-cowork-cookbook-adaptive-card-adjust-production-plan"
description: "Produces a reusable Adaptive Card JSON snapshot of adjust production plan status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_adjust_production_plan", "rar_sha256": "ed1e51b4ca66da059437398e980822046a3f0fd9b996a2f768ae8508c1098449", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_adjust_production_plan`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_adjust_production_plan_agent.py` and in the RCI capsule.

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

Adjust production plan Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of adjust production plan status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-adjust-production-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_adjust_production_plan_agent.py` and embedded as the fenced Python below (sha256 ed1e51b4ca66da05…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_adjust_production_plan_agent.py` first:

```bash
python3 adaptive_card_adjust_production_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_adjust_production_plan_agent.py   # or on stdin
python3 adaptive_card_adjust_production_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Adjust production plan Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of adjust production plan status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-adjust-production-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_adjust_production_plan',
    "version": '2.0.1',
    "display_name": 'Adjust production plan Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of adjust production plan status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-adjust-production-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-adjust-production-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2754295b0dcf60aa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/adjust-production-plan'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/adaptive-card-adjust-production-plan', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardAdjustProductionPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardAdjustProductionPlan'
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
    print(AdaptiveCardAdjustProductionPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
