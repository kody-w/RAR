---
name: "rar-cowork-cookbook-teams-update-evaluate-campaign-performance"
description: "Drafts a Teams channel post on evaluate campaign performance status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_evaluate_campaign_performance", "rar_sha256": "7272c34a0533c0685998d1a5796f0d67004c779f3082417d78a4e980297a311a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_evaluate_campaign_performance_agent.py` and embedded as the fenced Python below (sha256 7272c34a0533c068…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_evaluate_campaign_performance_agent.py` first:

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
    "version": '2.0.1',
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
