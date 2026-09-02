---
name: "rar-cowork-cookbook-demo-data-track-campaign-expenses"
description: "Generates and creates realistic demo records for track campaign expenses in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_track_campaign_expenses", "rar_sha256": "d703e6102687d31fefa5c588c9398170532767bc4417c3a37e7f6aa6516a41fd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_track_campaign_expenses_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-track-campaign-expenses:e24ae629e3562c6ed8c0c9204df87788e3b4c0c5ec55157e84ed186ce1192f25", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_track_campaign_expenses`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_track_campaign_expenses_agent.py` is
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

Track campaign expenses Demo Data Generator — Generates and creates realistic demo records for track campaign expenses in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-track-campaign-expenses
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_track_campaign_expenses_agent.py` and embedded as the fenced Python below (sha256 d703e6102687d31f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_track_campaign_expenses_agent.py` first:

```bash
python3 demo_data_track_campaign_expenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_track_campaign_expenses_agent.py   # or on stdin
python3 demo_data_track_campaign_expenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track campaign expenses Demo Data Generator — Generates and creates realistic demo records for track campaign expenses in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-track-campaign-expenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_track_campaign_expenses',
    "version": '2.0.0',
    "display_name": 'Track campaign expenses Demo Data Generator',
    "description": 'Generates and creates realistic demo records for track campaign expenses in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-track-campaign-expenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-track-campaign-expenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9e1c70144438bac5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-marketing-campaigns/track-campaign-expenses'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/demo-data-track-campaign-expenses', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataTrackCampaignExpenses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataTrackCampaignExpenses'
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
    print(DemoDataTrackCampaignExpenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
