---
name: "rar-cowork-cookbook-scheduled-brief-correct-synchronous-integration-failures"
description: "Schedulable morning-brief email summarizing correct synchronous integration failures for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_correct_synchronous_integration_failures", "rar_sha256": "b9b47c05691108221d633007ac058e8bd4400f7cf1df61f72c5aea403b6648e2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_correct_synchronous_integration_failures`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_correct_synchronous_integration_failures_agent.py` and in the RCI capsule.

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

Correct synchronous integration failures Scheduled Email Brief — Schedulable morning-brief email summarizing correct synchronous integration failures for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-correct-synchronous-integration-failures
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_correct_synchronous_integration_failures_agent.py` and embedded as the fenced Python below (sha256 b9b47c0569110822…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_correct_synchronous_integration_failures_agent.py` first:

```bash
python3 scheduled_brief_correct_synchronous_integration_failures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_correct_synchronous_integration_failures_agent.py   # or on stdin
python3 scheduled_brief_correct_synchronous_integration_failures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct synchronous integration failures Scheduled Email Brief — Schedulable morning-brief email summarizing correct synchronous integration failures for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-correct-synchronous-integration-failures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_correct_synchronous_integration_failures',
    "version": '2.0.0',
    "display_name": 'Correct synchronous integration failures Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing correct synchronous integration failures for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-correct-synchronous-integration-failures',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-correct-synchronous-integration-failures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '39977320e999647f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/correct-synchronous-integration-failures'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-correct-synchronous-integration-failures', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefCorrectSynchronousIntegrationFailures(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefCorrectSynchronousIntegrationFailures'
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
    print(ScheduledBriefCorrectSynchronousIntegrationFailures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
