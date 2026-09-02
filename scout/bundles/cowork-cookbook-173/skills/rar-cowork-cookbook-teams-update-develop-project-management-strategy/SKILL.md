---
name: "rar-cowork-cookbook-teams-update-develop-project-management-strategy"
description: "Drafts a Teams channel post on develop project management strategy status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_project_management_strategy", "rar_sha256": "2b8272ceaedb7be990c7ccf91bc41b845eabc53ac6f0311a38f85030f28d10ab", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_develop_project_management_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-develop-project-management-strategy:a8ceddca39b7ec5533d0b172fe7db6edaf6bf3c7010b735044fec4e6b52cbe12", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_develop_project_management_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_develop_project_management_strategy_agent.py` is
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

Develop project management strategy Teams Channel Update — Drafts a Teams channel post on develop project management strategy status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-project-management-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_project_management_strategy_agent.py` and embedded as the fenced Python below (sha256 2b8272ceaedb7be9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_project_management_strategy_agent.py` first:

```bash
python3 teams_update_develop_project_management_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_develop_project_management_strategy_agent.py   # or on stdin
python3 teams_update_develop_project_management_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop project management strategy Teams Channel Update — Drafts a Teams channel post on develop project management strategy status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-project-management-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_develop_project_management_strategy',
    "version": '2.0.0',
    "display_name": 'Develop project management strategy Teams Channel Update',
    "description": 'Drafts a Teams channel post on develop project management strategy status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-develop-project-management-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-develop-project-management-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f19f3cdc0895163a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/develop-project-strategy/develop-project-management-strategy'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/teams-update-develop-project-management-strategy', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateDevelopProjectManagementStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDevelopProjectManagementStrategy'
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
    print(TeamsUpdateDevelopProjectManagementStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
