---
name: "rar-cowork-cookbook-teams-update-define-environment-strategy"
description: "Drafts a Teams channel post on define environment strategy status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_environment_strategy", "rar_sha256": "5ec9e3cf16188b9633506d27c2cb61bdcffc359f4f04291f64e96a83f051490e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_environment_strategy`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_environment_strategy_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_environment_strategy_agent.py` and embedded as the fenced Python below (sha256 5ec9e3cf16188b96…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_environment_strategy_agent.py` first:

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
    "version": '2.0.1',
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
