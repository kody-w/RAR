---
name: "rar-cowork-cookbook-teams-update-estimate-the-cost-of-production"
description: "Drafts a Teams channel post on estimate the cost of production status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_estimate_the_cost_of_production", "rar_sha256": "2d4fe8a4d0236a0dbe485b7aa1ac3c7a7d35f4ad072d9e9eee55d7465b26d911", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_estimate_the_cost_of_production_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-estimate-the-cost-of-production:665bd5b29ff79483fae1f3765844d6f70ed5a4036de6bad9fa222cdc61fc8d8c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_estimate_the_cost_of_production`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_estimate_the_cost_of_production_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_estimate_the_cost_of_production_agent.py` and embedded as the fenced Python below (sha256 2d4fe8a4d0236a0d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_estimate_the_cost_of_production_agent.py` first:

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
    "version": '2.0.0',
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
