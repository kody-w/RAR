---
name: "rar-cowork-cookbook-scheduled-brief-define-usability-strategy"
description: "Schedulable morning-brief email summarizing define usability strategy for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_usability_strategy", "rar_sha256": "6f9e5ecd0210e8b210555d84f6e13d239bff7f6b7834987f1c160828f71e0d47", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_usability_strategy`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_usability_strategy_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_usability_strategy_agent.py` and embedded as the fenced Python below (sha256 6f9e5ecd0210e8b2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_usability_strategy_agent.py` first:

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
    "version": '2.0.1',
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
