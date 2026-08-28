---
name: "rar-cowork-cookbook-scheduled-brief-correct-data-synchronization-failures"
description: "Schedulable morning-brief email summarizing correct data synchronization failures for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_correct_data_synchronization_failures", "rar_sha256": "b46885e7a1dc6c6df4e5a9ff031b559943ef0306670523a1790e701e0217df88", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_correct_data_synchronization_failures`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_correct_data_synchronization_failures_agent.py` and in the RCI capsule.

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

Correct data synchronization failures Scheduled Email Brief — Schedulable morning-brief email summarizing correct data synchronization failures for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-correct-data-synchronization-failures
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_correct_data_synchronization_failures_agent.py` and embedded as the fenced Python below (sha256 b46885e7a1dc6c6d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_correct_data_synchronization_failures_agent.py` first:

```bash
python3 scheduled_brief_correct_data_synchronization_failures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_correct_data_synchronization_failures_agent.py   # or on stdin
python3 scheduled_brief_correct_data_synchronization_failures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct data synchronization failures Scheduled Email Brief — Schedulable morning-brief email summarizing correct data synchronization failures for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-correct-data-synchronization-failures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_correct_data_synchronization_failures',
    "version": '2.0.1',
    "display_name": 'Correct data synchronization failures Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing correct data synchronization failures for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-correct-data-synchronization-failures',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-correct-data-synchronization-failures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '32a0e2b823e02a50',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-data/correct-data-synchronization-failures'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-correct-data-synchronization-failures', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefCorrectDataSynchronizationFailures(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefCorrectDataSynchronizationFailures'
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
    print(ScheduledBriefCorrectDataSynchronizationFailures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
