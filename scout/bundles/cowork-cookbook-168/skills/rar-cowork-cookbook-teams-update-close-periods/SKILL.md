---
name: "rar-cowork-cookbook-teams-update-close-periods"
description: "Drafts a Teams channel post on close periods status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_close_periods", "rar_sha256": "b07a7247635b6177c72461409a72f208868b37dca7fc33f8c52dd2bdd7ca6fac", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_close_periods_agent.py` and embedded as the fenced Python below (sha256 b07a7247635b6177…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_close_periods_agent.py` first:

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
    "version": '2.0.0',
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
