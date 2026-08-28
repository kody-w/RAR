---
name: "rar-cowork-cookbook-adaptive-card-mitigate-and-update-the-disaster-recovery-plan"
description: "Produces a reusable Adaptive Card JSON snapshot of mitigate and update the disaster recovery plan status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_mitigate_and_update_the_disaster_recovery_plan", "rar_sha256": "1a38fa036d56d0e91b355b66650109669136aaf8aa47b8f6326076299d12ea3e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_mitigate_and_update_the_disaster_recovery_plan_agent.py` and embedded as the fenced Python below (sha256 1a38fa036d56d0e9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_mitigate_and_update_the_disaster_recovery_plan_agent.py` first:

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
    "version": '2.0.1',
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
