---
name: "rar-cowork-cookbook-teams-update-close-periods"
description: "Drafts a Teams channel post on close periods status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_close_periods", "rar_sha256": "f0fa4d5782cce2be7f506e9d6b8d95231d18073c09edc2c675f5a6283c717584", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_close_periods`. The original RAPP
agent is preserved byte-for-byte in `teams_update_close_periods_agent.py` and in the RCI capsule.

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

Close periods Teams Channel Update — Drafts a Teams channel post on close periods status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-close-periods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_close_periods_agent.py` and embedded as the fenced Python below (sha256 f0fa4d5782cce2be…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_close_periods_agent.py` first:

```bash
python3 teams_update_close_periods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_close_periods_agent.py   # or on stdin
python3 teams_update_close_periods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Close periods Teams Channel Update — Drafts a Teams channel post on close periods status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-close-periods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_close_periods',
    "version": '2.0.1',
    "display_name": 'Close periods Teams Channel Update',
    "description": 'Drafts a Teams channel post on close periods status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-close-periods',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-close-periods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e40e9a478e06965e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/close-periods'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/teams-update-close-periods', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class TeamsUpdateClosePeriods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateClosePeriods'
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
    print(TeamsUpdateClosePeriods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
