---
name: "rar-cowork-cookbook-teams-update-define-usability-strategy"
description: "Drafts a Teams channel post on define usability strategy status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_usability_strategy", "rar_sha256": "2357cc531ff0b580edd2a26fbbc4b2939dd7a61221a8ecdfe2bdeb601fa7e4ad", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_usability_strategy`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_usability_strategy_agent.py` and in the RCI capsule.

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

Define usability strategy Teams Channel Update — Drafts a Teams channel post on define usability strategy status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-usability-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_usability_strategy_agent.py` and embedded as the fenced Python below (sha256 2357cc531ff0b580…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_usability_strategy_agent.py` first:

```bash
python3 teams_update_define_usability_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_usability_strategy_agent.py   # or on stdin
python3 teams_update_define_usability_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define usability strategy Teams Channel Update — Drafts a Teams channel post on define usability strategy status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-usability-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_usability_strategy',
    "version": '2.0.0',
    "display_name": 'Define usability strategy Teams Channel Update',
    "description": 'Drafts a Teams channel post on define usability strategy status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-define-usability-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-usability-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f3284fe087a39824',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-usability-strategy'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-define-usability-strategy', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateDefineUsabilityStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineUsabilityStrategy'
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
    print(TeamsUpdateDefineUsabilityStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
