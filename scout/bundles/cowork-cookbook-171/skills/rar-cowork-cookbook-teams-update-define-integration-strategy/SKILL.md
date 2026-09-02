---
name: "rar-cowork-cookbook-teams-update-define-integration-strategy"
description: "Drafts a Teams channel post on define integration strategy status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_integration_strategy", "rar_sha256": "7b60553588756ae0016b05e47f445f300ba46874280aa463babeca1521a98572", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_define_integration_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-define-integration-strategy:460cfe73160e438276ba0aa1a4d76466572f0e3f2fb4990511b0f982606609ca", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_define_integration_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_define_integration_strategy_agent.py` is
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

Define integration strategy Teams Channel Update — Drafts a Teams channel post on define integration strategy status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-integration-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_integration_strategy_agent.py` and embedded as the fenced Python below (sha256 7b60553588756ae0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_integration_strategy_agent.py` first:

```bash
python3 teams_update_define_integration_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_integration_strategy_agent.py   # or on stdin
python3 teams_update_define_integration_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define integration strategy Teams Channel Update — Drafts a Teams channel post on define integration strategy status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-integration-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_integration_strategy',
    "version": '2.0.0',
    "display_name": 'Define integration strategy Teams Channel Update',
    "description": 'Drafts a Teams channel post on define integration strategy status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-define-integration-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-integration-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9d9b3d2aace5fe1e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-integration-strategy'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-define-integration-strategy', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateDefineIntegrationStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineIntegrationStrategy'
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
    print(TeamsUpdateDefineIntegrationStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
