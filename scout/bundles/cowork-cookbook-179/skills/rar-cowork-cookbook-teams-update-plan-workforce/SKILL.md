---
name: "rar-cowork-cookbook-teams-update-plan-workforce"
description: "Drafts a Teams channel post on plan workforce status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_plan_workforce", "rar_sha256": "9fc31a343ed0fe4a27905b8ecdb2e5d59e7ebe48d9a760684223e94aa31e3b7b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_plan_workforce`. The original RAPP
agent is preserved byte-for-byte in `teams_update_plan_workforce_agent.py` and in the RCI capsule.

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

Plan workforce Teams Channel Update — Drafts a Teams channel post on plan workforce status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-plan-workforce
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_plan_workforce_agent.py` and embedded as the fenced Python below (sha256 9fc31a343ed0fe4a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_plan_workforce_agent.py` first:

```bash
python3 teams_update_plan_workforce_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_plan_workforce_agent.py   # or on stdin
python3 teams_update_plan_workforce_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan workforce Teams Channel Update — Drafts a Teams channel post on plan workforce status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-plan-workforce
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_plan_workforce',
    "version": '2.0.1',
    "display_name": 'Plan workforce Teams Channel Update',
    "description": 'Drafts a Teams channel post on plan workforce status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-plan-workforce',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-plan-workforce',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd49f2c068bb0b69f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/plan-workforce'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/teams-update-plan-workforce', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdatePlanWorkforce(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdatePlanWorkforce'
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
    print(TeamsUpdatePlanWorkforce().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
