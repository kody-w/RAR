---
name: "rar-cowork-cookbook-teams-update-develop-subcontracting-strategy"
description: "Drafts a Teams channel post on develop subcontracting strategy status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_subcontracting_strategy", "rar_sha256": "d8b8fb0698d21fdac1b096f5d80b5eadde71645662f0ccb5c6ff03efcdcd3df2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_develop_subcontracting_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-develop-subcontracting-strategy:5df7a18479c588f56fdf562f879f1a819aec592bb525b7a5779f59eca9192e9b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_develop_subcontracting_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_develop_subcontracting_strategy_agent.py` is
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

Develop subcontracting strategy Teams Channel Update — Drafts a Teams channel post on develop subcontracting strategy status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-subcontracting-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_subcontracting_strategy_agent.py` and embedded as the fenced Python below (sha256 d8b8fb0698d21fda…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_subcontracting_strategy_agent.py` first:

```bash
python3 teams_update_develop_subcontracting_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_develop_subcontracting_strategy_agent.py   # or on stdin
python3 teams_update_develop_subcontracting_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop subcontracting strategy Teams Channel Update — Drafts a Teams channel post on develop subcontracting strategy status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-subcontracting-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_develop_subcontracting_strategy',
    "version": '2.0.0',
    "display_name": 'Develop subcontracting strategy Teams Channel Update',
    "description": 'Drafts a Teams channel post on develop subcontracting strategy status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-develop-subcontracting-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-develop-subcontracting-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a964139b06681734',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies/develop-subcontracting-strategy'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/teams-update-develop-subcontracting-strategy', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateDevelopSubcontractingStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDevelopSubcontractingStrategy'
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
    print(TeamsUpdateDevelopSubcontractingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
