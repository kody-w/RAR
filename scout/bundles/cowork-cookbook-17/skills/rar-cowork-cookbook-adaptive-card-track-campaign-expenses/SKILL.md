---
name: "rar-cowork-cookbook-adaptive-card-track-campaign-expenses"
description: "Produces a reusable Adaptive Card JSON snapshot of track campaign expenses status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_track_campaign_expenses", "rar_sha256": "5dcb34547a8a0388a92ceb8719cb94a34c518398671c03f5fd3d07bdd82a7a1e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_track_campaign_expenses_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-track-campaign-expenses:cca6fb5383b74205c825420a81e00e36538491081b4b236c8f8c4c8f31d2fd4e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_track_campaign_expenses`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_track_campaign_expenses_agent.py` is
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
