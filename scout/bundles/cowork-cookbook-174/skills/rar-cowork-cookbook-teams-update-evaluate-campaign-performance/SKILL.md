---
name: "rar-cowork-cookbook-teams-update-evaluate-campaign-performance"
description: "Drafts a Teams channel post on evaluate campaign performance status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_evaluate_campaign_performance", "rar_sha256": "46a9d5cb908e960c84513744b3e37137915b48dfecab689405f8a0b0b849778a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_evaluate_campaign_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-evaluate-campaign-performance:8df17140186bfcf99fdf6379d5bac3efc71de925a331d80aba696327cc4e0ad2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_evaluate_campaign_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_evaluate_campaign_performance_agent.py` is
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

Evaluate campaign performance Teams Channel Update — Drafts a Teams channel post on evaluate campaign performance status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-evaluate-campaign-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_evaluate_campaign_performance_agent.py` and embedded as the fenced Python below (sha256 46a9d5cb908e960c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_evaluate_campaign_performance_agent.py` first:

```bash
python3 teams_update_evaluate_campaign_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_evaluate_campaign_performance_agent.py   # or on stdin
python3 teams_update_evaluate_campaign_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Evaluate campaign performance Teams Channel Update — Drafts a Teams channel post on evaluate campaign performance status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-evaluate-campaign-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_evaluate_campaign_performance',
    "version": '2.0.0',
    "display_name": 'Evaluate campaign performance Teams Channel Update',
    "description": 'Drafts a Teams channel post on evaluate campaign performance status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-evaluate-campaign-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-evaluate-campaign-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b8c4ec60072fd87c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/evaluate-campaign-performance'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/teams-update-evaluate-campaign-performance', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateEvaluateCampaignPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateEvaluateCampaignPerformance'
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
    print(TeamsUpdateEvaluateCampaignPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
