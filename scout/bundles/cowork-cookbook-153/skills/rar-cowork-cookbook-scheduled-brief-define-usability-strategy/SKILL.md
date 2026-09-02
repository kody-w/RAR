---
name: "rar-cowork-cookbook-scheduled-brief-define-usability-strategy"
description: "Schedulable morning-brief email summarizing define usability strategy for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_usability_strategy", "rar_sha256": "55798514956fd10243e380c865a15605d5817e240ed4d3fffc61531bb39cae42", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_define_usability_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-define-usability-strategy:479db8545265450c625da120aa39e552bde5c1391b57e81d4f55df9a19b046c6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_define_usability_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_define_usability_strategy_agent.py` is
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

Define usability strategy Scheduled Email Brief — Schedulable morning-brief email summarizing define usability strategy for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-usability-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_usability_strategy_agent.py` and embedded as the fenced Python below (sha256 55798514956fd102…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_usability_strategy_agent.py` first:

```bash
python3 scheduled_brief_define_usability_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_usability_strategy_agent.py   # or on stdin
python3 scheduled_brief_define_usability_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define usability strategy Scheduled Email Brief — Schedulable morning-brief email summarizing define usability strategy for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-usability-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_usability_strategy',
    "version": '2.0.0',
    "display_name": 'Define usability strategy Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing define usability strategy for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-define-usability-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-usability-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5e77e86a6e85ef47',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-usability-strategy'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-define-usability-strategy', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefDefineUsabilityStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineUsabilityStrategy'
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
    print(ScheduledBriefDefineUsabilityStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
