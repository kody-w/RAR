---
name: "rar-cowork-cookbook-teams-update-develop-project-management-strategy"
description: "Drafts a Teams channel post on develop project management strategy status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_project_management_strategy", "rar_sha256": "2b8272ceaedb7be990c7ccf91bc41b845eabc53ac6f0311a38f85030f28d10ab", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
