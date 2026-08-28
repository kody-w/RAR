---
name: "rar-cowork-cookbook-teams-update-estimate-the-cost-of-production"
description: "Drafts a Teams channel post on estimate the cost of production status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_estimate_the_cost_of_production", "rar_sha256": "5816b90100992cdc16d65d9541ce1f8c7680fd10c5edf9f2fd49aa722dcad850", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_estimate_the_cost_of_production`. The original RAPP
agent is preserved byte-for-byte in `teams_update_estimate_the_cost_of_production_agent.py` and in the RCI capsule.

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

Estimate the cost of production Teams Channel Update — Drafts a Teams channel post on estimate the cost of production status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-estimate-the-cost-of-production
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_estimate_the_cost_of_production_agent.py` and embedded as the fenced Python below (sha256 5816b90100992cdc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_estimate_the_cost_of_production_agent.py` first:

```bash
python3 teams_update_estimate_the_cost_of_production_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_estimate_the_cost_of_production_agent.py   # or on stdin
python3 teams_update_estimate_the_cost_of_production_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Estimate the cost of production Teams Channel Update — Drafts a Teams channel post on estimate the cost of production status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-estimate-the-cost-of-production
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_estimate_the_cost_of_production',
    "version": '2.0.1',
    "display_name": 'Estimate the cost of production Teams Channel Update',
    "description": 'Drafts a Teams channel post on estimate the cost of production status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-estimate-the-cost-of-production',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-estimate-the-cost-of-production',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1a12d3f6e1de129f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/estimate-the-cost-of-production'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/teams-update-estimate-the-cost-of-production', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateEstimateTheCostOfProduction(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateEstimateTheCostOfProduction'
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
    print(TeamsUpdateEstimateTheCostOfProduction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
