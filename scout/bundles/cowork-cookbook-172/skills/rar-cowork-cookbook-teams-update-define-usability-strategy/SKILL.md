---
name: "rar-cowork-cookbook-teams-update-define-usability-strategy"
description: "Drafts a Teams channel post on define usability strategy status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_usability_strategy", "rar_sha256": "2357cc531ff0b580edd2a26fbbc4b2939dd7a61221a8ecdfe2bdeb601fa7e4ad", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_define_usability_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-define-usability-strategy:f3215573eb9ccb9e1787ef97e9957b0850d2b66947c9d55f5093fb835e8a3c8a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_define_usability_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_define_usability_strategy_agent.py` is
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
