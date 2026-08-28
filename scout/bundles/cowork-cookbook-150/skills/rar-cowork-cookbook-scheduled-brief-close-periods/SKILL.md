---
name: "rar-cowork-cookbook-scheduled-brief-close-periods"
description: "Schedulable morning-brief email summarizing close periods for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_close_periods", "rar_sha256": "2bfa0c1c9f1012a65eaf0f8f01905693840b0660a0f71b9b1df4815ac23f6a69", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_close_periods`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_close_periods_agent.py` and in the RCI capsule.

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

Close periods Scheduled Email Brief — Schedulable morning-brief email summarizing close periods for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-close-periods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_close_periods_agent.py` and embedded as the fenced Python below (sha256 2bfa0c1c9f1012a6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_close_periods_agent.py` first:

```bash
python3 scheduled_brief_close_periods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_close_periods_agent.py   # or on stdin
python3 scheduled_brief_close_periods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Close periods Scheduled Email Brief — Schedulable morning-brief email summarizing close periods for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-close-periods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_close_periods',
    "version": '2.0.1',
    "display_name": 'Close periods Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing close periods for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'scheduled-brief-close-periods',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-close-periods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '22b7e87e25f2aab8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/close-periods'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/scheduled-brief-close-periods', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ScheduledBriefClosePeriods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefClosePeriods'
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
    print(ScheduledBriefClosePeriods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
