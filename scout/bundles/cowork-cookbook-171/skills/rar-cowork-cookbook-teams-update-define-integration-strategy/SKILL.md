---
name: "rar-cowork-cookbook-teams-update-define-integration-strategy"
description: "Drafts a Teams channel post on define integration strategy status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_integration_strategy", "rar_sha256": "e29f2c4ea8985e430d09515b849eef9a65f3d7a92f622fa5ea9ab45997fc2aff", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_integration_strategy`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_integration_strategy_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_integration_strategy_agent.py` and embedded as the fenced Python below (sha256 e29f2c4ea8985e43…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_integration_strategy_agent.py` first:

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
    "version": '2.0.1',
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
