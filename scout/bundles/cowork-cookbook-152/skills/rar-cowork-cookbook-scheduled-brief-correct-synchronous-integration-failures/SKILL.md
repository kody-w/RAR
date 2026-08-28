---
name: "rar-cowork-cookbook-scheduled-brief-correct-synchronous-integration-failures"
description: "Schedulable morning-brief email summarizing correct synchronous integration failures for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_correct_synchronous_integration_failures", "rar_sha256": "bf9d002d768fe3bf94990cf67d9b29bf19a9d0124444004f4d2a4f9e249b2664", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_correct_synchronous_integration_failures_agent.py` and embedded as the fenced Python below (sha256 bf9d002d768fe3bf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_correct_synchronous_integration_failures_agent.py` first:

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
    "version": '2.0.1',
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
