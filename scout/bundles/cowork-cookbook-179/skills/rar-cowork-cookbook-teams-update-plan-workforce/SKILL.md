---
name: "rar-cowork-cookbook-teams-update-plan-workforce"
description: "Drafts a Teams channel post on plan workforce status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_plan_workforce", "rar_sha256": "ec0f2ac2b60ba8bb82977df02941b4b2961773e0a4634d782ca896eccae23299", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_plan_workforce_agent.py` and embedded as the fenced Python below (sha256 ec0f2ac2b60ba8bb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_plan_workforce_agent.py` first:

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
    "version": '2.0.0',
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
