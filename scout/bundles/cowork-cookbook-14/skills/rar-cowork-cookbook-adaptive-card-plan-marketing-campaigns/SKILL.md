---
name: "rar-cowork-cookbook-adaptive-card-plan-marketing-campaigns"
description: "Produces a reusable Adaptive Card JSON snapshot of plan marketing campaigns status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_plan_marketing_campaigns", "rar_sha256": "ef415a0c7a5c10cc5619c3f09a0d2ab60058a216322c4ce4d81411db74325fcc", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_plan_marketing_campaigns_agent.py` and embedded as the fenced Python below (sha256 ef415a0c7a5c10cc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_plan_marketing_campaigns_agent.py` first:

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
    "version": '2.0.1',
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
