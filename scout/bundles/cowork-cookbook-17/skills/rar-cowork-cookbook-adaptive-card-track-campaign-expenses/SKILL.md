---
name: "rar-cowork-cookbook-adaptive-card-track-campaign-expenses"
description: "Produces a reusable Adaptive Card JSON snapshot of track campaign expenses status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_track_campaign_expenses", "rar_sha256": "5dcb34547a8a0388a92ceb8719cb94a34c518398671c03f5fd3d07bdd82a7a1e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_track_campaign_expenses_agent.py` and embedded as the fenced Python below (sha256 5dcb34547a8a0388…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_track_campaign_expenses_agent.py` first:

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
    "version": '2.0.0',
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
