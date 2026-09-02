---
name: "rar-cowork-cookbook-teams-update-close-periods"
description: "Drafts a Teams channel post on close periods status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_close_periods", "rar_sha256": "b07a7247635b6177c72461409a72f208868b37dca7fc33f8c52dd2bdd7ca6fac", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_close_periods_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-close-periods:efd46f904ba930c67e644e9e7c388f6a84051fda2ed97f13048996654df6c9ec", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_close_periods`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_close_periods_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
