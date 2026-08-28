---
name: "rar-cowork-cookbook-teams-update-define-usability-strategy"
description: "Drafts a Teams channel post on define usability strategy status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_usability_strategy", "rar_sha256": "bff9e9801d20ed3cf1daf00db54b88fd1481c3029a8d1b461f83a2e201fc37e9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_usability_strategy_agent.py` and embedded as the fenced Python below (sha256 bff9e9801d20ed3c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_usability_strategy_agent.py` first:

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
    "version": '2.0.1',
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
