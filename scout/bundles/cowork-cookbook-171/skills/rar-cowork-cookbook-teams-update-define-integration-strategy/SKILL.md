---
name: "rar-cowork-cookbook-teams-update-define-integration-strategy"
description: "Drafts a Teams channel post on define integration strategy status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_integration_strategy", "rar_sha256": "7b60553588756ae0016b05e47f445f300ba46874280aa463babeca1521a98572", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
