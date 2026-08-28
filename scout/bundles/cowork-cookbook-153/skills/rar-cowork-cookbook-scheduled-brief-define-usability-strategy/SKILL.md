---
name: "rar-cowork-cookbook-scheduled-brief-define-usability-strategy"
description: "Schedulable morning-brief email summarizing define usability strategy for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_usability_strategy", "rar_sha256": "55798514956fd10243e380c865a15605d5817e240ed4d3fffc61531bb39cae42", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
