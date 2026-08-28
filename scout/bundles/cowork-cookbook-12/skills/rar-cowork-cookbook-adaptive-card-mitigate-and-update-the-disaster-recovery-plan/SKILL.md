---
name: "rar-cowork-cookbook-adaptive-card-mitigate-and-update-the-disaster-recovery-plan"
description: "Produces a reusable Adaptive Card JSON snapshot of mitigate and update the disaster recovery plan status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_mitigate_and_update_the_disaster_recovery_plan", "rar_sha256": "c0d2e6031b9b3b5a3b9f9b36280f79ac75ff4f4a9af69de04412f208b7dd31ba", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_mitigate_and_update_the_disaster_recovery_plan`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_mitigate_and_update_the_disaster_recovery_plan_agent.py` and in the RCI capsule.

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

Mitigate and update the disaster recovery plan Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of mitigate and update the disaster recovery plan status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-mitigate-and-update-the-disaster-recovery-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_mitigate_and_update_the_disaster_recovery_plan_agent.py` and embedded as the fenced Python below (sha256 c0d2e6031b9b3b5a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_mitigate_and_update_the_disaster_recovery_plan_agent.py` first:

```bash
python3 adaptive_card_mitigate_and_update_the_disaster_recovery_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_mitigate_and_update_the_disaster_recovery_plan_agent.py   # or on stdin
python3 adaptive_card_mitigate_and_update_the_disaster_recovery_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Mitigate and update the disaster recovery plan Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of mitigate and update the disaster recovery plan status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-mitigate-and-update-the-disaster-recovery-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_mitigate_and_update_the_disaster_recovery_plan',
    "version": '2.0.0',
    "display_name": 'Mitigate and update the disaster recovery plan Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of mitigate and update the disaster recovery plan status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-mitigate-and-update-the-disaster-recovery-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-mitigate-and-update-the-disaster-recovery-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0b3fc7d6631a2892',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/mitigate-and-update-the-disaster-recovery-plan'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-mitigate-and-update-the-disaster-recovery-plan', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardMitigateAndUpdateTheDisasterRecoveryPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardMitigateAndUpdateTheDisasterRecoveryPlan'
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
    print(AdaptiveCardMitigateAndUpdateTheDisasterRecoveryPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
