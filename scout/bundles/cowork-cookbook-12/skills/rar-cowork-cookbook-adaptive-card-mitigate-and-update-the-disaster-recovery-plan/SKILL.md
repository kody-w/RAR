---
name: "rar-cowork-cookbook-adaptive-card-mitigate-and-update-the-disaster-recovery-plan"
description: "Produces a reusable Adaptive Card JSON snapshot of mitigate and update the disaster recovery plan status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_mitigate_and_update_the_disaster_recovery_plan", "rar_sha256": "c0d2e6031b9b3b5a3b9f9b36280f79ac75ff4f4a9af69de04412f208b7dd31ba", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_mitigate_and_update_the_disaster_recovery_plan_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-mitigate-and-update-the-disaster-recovery-plan:8576da17a1eb92d24a977d4f2ab13fa85ed137be73d5bf2bf3b1d290d4ed2aeb", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_mitigate_and_update_the_disaster_recovery_plan`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_mitigate_and_update_the_disaster_recovery_plan_agent.py` is
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
