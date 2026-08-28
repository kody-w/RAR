---
name: "rar-cowork-cookbook-adaptive-card-track-campaign-expenses"
description: "Produces a reusable Adaptive Card JSON snapshot of track campaign expenses status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_track_campaign_expenses", "rar_sha256": "1da452507faba8da0e06ffc4afa0b26afe8715eb64f29f45fdbfb3b7b84ad9b3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_track_campaign_expenses`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_track_campaign_expenses_agent.py` and in the RCI capsule.

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

Track campaign expenses Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of track campaign expenses status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-track-campaign-expenses
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_track_campaign_expenses_agent.py` and embedded as the fenced Python below (sha256 1da452507faba8da…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_track_campaign_expenses_agent.py` first:

```bash
python3 adaptive_card_track_campaign_expenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_track_campaign_expenses_agent.py   # or on stdin
python3 adaptive_card_track_campaign_expenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track campaign expenses Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of track campaign expenses status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-track-campaign-expenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_track_campaign_expenses',
    "version": '2.0.1',
    "display_name": 'Track campaign expenses Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of track campaign expenses status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-track-campaign-expenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-track-campaign-expenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6cc254ad63466277',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-marketing-campaigns/track-campaign-expenses'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/adaptive-card-track-campaign-expenses', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardTrackCampaignExpenses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardTrackCampaignExpenses'
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
    print(AdaptiveCardTrackCampaignExpenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
