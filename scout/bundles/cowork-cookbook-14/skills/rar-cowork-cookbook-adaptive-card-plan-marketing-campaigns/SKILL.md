---
name: "rar-cowork-cookbook-adaptive-card-plan-marketing-campaigns"
description: "Produces a reusable Adaptive Card JSON snapshot of plan marketing campaigns status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_plan_marketing_campaigns", "rar_sha256": "c66f9b95ce1c152df4ec7806cbb8a5b40b4ed4d1a4c0607e4e2ebd13992c2b93", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_plan_marketing_campaigns`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_plan_marketing_campaigns_agent.py` and in the RCI capsule.

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
