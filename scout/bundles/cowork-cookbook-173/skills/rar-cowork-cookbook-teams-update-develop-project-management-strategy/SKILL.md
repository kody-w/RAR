---
name: "rar-cowork-cookbook-teams-update-develop-project-management-strategy"
description: "Drafts a Teams channel post on develop project management strategy status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_project_management_strategy", "rar_sha256": "a071c0ecb9fd935eefdacdabe6ee4cb8c3146402f86cd2e5ee7256ee6af1bd4b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_develop_project_management_strategy`. The original RAPP
agent is preserved byte-for-byte in `teams_update_develop_project_management_strategy_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_project_management_strategy_agent.py` and embedded as the fenced Python below (sha256 a071c0ecb9fd935e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_project_management_strategy_agent.py` first:

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
    "version": '2.0.1',
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
