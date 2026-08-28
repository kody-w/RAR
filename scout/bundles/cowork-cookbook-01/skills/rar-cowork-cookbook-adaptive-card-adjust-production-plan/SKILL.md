---
name: "rar-cowork-cookbook-adaptive-card-adjust-production-plan"
description: "Produces a reusable Adaptive Card JSON snapshot of adjust production plan status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_adjust_production_plan", "rar_sha256": "a6b0d7069bc960382c3a44aabd738c078304f3524050f12453120f4fb8270f64", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_adjust_production_plan_agent.py` and embedded as the fenced Python below (sha256 a6b0d7069bc96038…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_adjust_production_plan_agent.py` first:

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
    "version": '2.0.0',
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
