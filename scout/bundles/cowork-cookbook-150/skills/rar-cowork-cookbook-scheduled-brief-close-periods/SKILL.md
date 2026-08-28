---
name: "rar-cowork-cookbook-scheduled-brief-close-periods"
description: "Schedulable morning-brief email summarizing close periods for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_close_periods", "rar_sha256": "0f47571211505e7435e9deb08032e481ec16ada774ad2730011c1de92d332e99", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_close_periods_agent.py` and embedded as the fenced Python below (sha256 0f47571211505e74…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_close_periods_agent.py` first:

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
    "version": '2.0.0',
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
