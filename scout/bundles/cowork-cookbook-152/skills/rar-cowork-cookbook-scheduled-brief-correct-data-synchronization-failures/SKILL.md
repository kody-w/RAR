---
name: "rar-cowork-cookbook-scheduled-brief-correct-data-synchronization-failures"
description: "Schedulable morning-brief email summarizing correct data synchronization failures for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_correct_data_synchronization_failures", "rar_sha256": "99ec13f23c908259facd6ce594c2165ebf113b77bcde52257fe529061b34ba32", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_correct_data_synchronization_failures_agent.py` and embedded as the fenced Python below (sha256 99ec13f23c908259…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_correct_data_synchronization_failures_agent.py` first:

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
    "version": '2.0.0',
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
