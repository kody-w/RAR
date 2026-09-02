---
name: "rar-cowork-cookbook-teams-update-define-environment-strategy"
description: "Drafts a Teams channel post on define environment strategy status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_environment_strategy", "rar_sha256": "58e4e2b1f3beaf1122e012545a58d540ef5bd7adea01b53967fef278c0a84c81", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_define_environment_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-define-environment-strategy:7411cedde980ebd2d275d767a59cc8ee31a02c44a5c5452c1fce9946bbb21a96", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_define_environment_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_define_environment_strategy_agent.py` is
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

Define environment strategy Teams Channel Update — Drafts a Teams channel post on define environment strategy status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-environment-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_environment_strategy_agent.py` and embedded as the fenced Python below (sha256 58e4e2b1f3beaf11…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_environment_strategy_agent.py` first:

```bash
python3 teams_update_define_environment_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_environment_strategy_agent.py   # or on stdin
python3 teams_update_define_environment_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define environment strategy Teams Channel Update — Drafts a Teams channel post on define environment strategy status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-environment-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_environment_strategy',
    "version": '2.0.0',
    "display_name": 'Define environment strategy Teams Channel Update',
    "description": 'Drafts a Teams channel post on define environment strategy status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-define-environment-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-environment-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ddb62191c431f4bd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-environment-strategy'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-define-environment-strategy', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateDefineEnvironmentStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineEnvironmentStrategy'
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
    print(TeamsUpdateDefineEnvironmentStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
