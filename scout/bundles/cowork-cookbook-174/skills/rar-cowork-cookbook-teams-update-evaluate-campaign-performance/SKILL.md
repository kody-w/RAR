---
name: "rar-cowork-cookbook-teams-update-evaluate-campaign-performance"
description: "Drafts a Teams channel post on evaluate campaign performance status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_evaluate_campaign_performance", "rar_sha256": "46a9d5cb908e960c84513744b3e37137915b48dfecab689405f8a0b0b849778a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_evaluate_campaign_performance`. The original RAPP
agent is preserved byte-for-byte in `teams_update_evaluate_campaign_performance_agent.py` and in the RCI capsule.

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
