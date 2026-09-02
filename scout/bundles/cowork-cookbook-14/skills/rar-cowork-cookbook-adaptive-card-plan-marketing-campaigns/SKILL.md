---
name: "rar-cowork-cookbook-adaptive-card-plan-marketing-campaigns"
description: "Produces a reusable Adaptive Card JSON snapshot of plan marketing campaigns status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_plan_marketing_campaigns", "rar_sha256": "c66f9b95ce1c152df4ec7806cbb8a5b40b4ed4d1a4c0607e4e2ebd13992c2b93", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_plan_marketing_campaigns_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-plan-marketing-campaigns:22c3da45e07de12d86b3847cba6848b6161c772928e156241f01e50d57e13da0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_plan_marketing_campaigns`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_plan_marketing_campaigns_agent.py` is
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

Plan marketing campaigns Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of plan marketing campaigns status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-plan-marketing-campaigns
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_plan_marketing_campaigns_agent.py` and embedded as the fenced Python below (sha256 c66f9b95ce1c152d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_plan_marketing_campaigns_agent.py` first:

```bash
python3 adaptive_card_plan_marketing_campaigns_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_plan_marketing_campaigns_agent.py   # or on stdin
python3 adaptive_card_plan_marketing_campaigns_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan marketing campaigns Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of plan marketing campaigns status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-plan-marketing-campaigns
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_plan_marketing_campaigns',
    "version": '2.0.0',
    "display_name": 'Plan marketing campaigns Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of plan marketing campaigns status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-plan-marketing-campaigns',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-plan-marketing-campaigns',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '87a3d80c787041b6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-marketing-campaigns'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/adaptive-card-plan-marketing-campaigns', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardPlanMarketingCampaigns(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardPlanMarketingCampaigns'
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
    print(AdaptiveCardPlanMarketingCampaigns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
