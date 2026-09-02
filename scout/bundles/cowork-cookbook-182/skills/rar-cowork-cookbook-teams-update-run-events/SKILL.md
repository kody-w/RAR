---
name: "rar-cowork-cookbook-teams-update-run-events"
description: "Drafts a Teams channel post on run events status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_run_events", "rar_sha256": "fe7d21d3f0c69f0f72ef209de7832782917a6293377cf7a68e4efbc85d49e12c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_run_events_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-run-events:9d33cdf37067d70891e185253d94be4d06a0a5c28e6d3463d0d0883620164d0f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_run_events`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_run_events_agent.py` is
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

Run events Teams Channel Update — Drafts a Teams channel post on run events status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-run-events
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_run_events_agent.py` and embedded as the fenced Python below (sha256 fe7d21d3f0c69f0f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_run_events_agent.py` first:

```bash
python3 teams_update_run_events_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_run_events_agent.py   # or on stdin
python3 teams_update_run_events_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Run events Teams Channel Update — Drafts a Teams channel post on run events status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-run-events
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_run_events',
    "version": '2.0.0',
    "display_name": 'Run events Teams Channel Update',
    "description": 'Drafts a Teams channel post on run events status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-run-events',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-run-events',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '98455c3b0dd428a5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-marketing-campaigns/run-events'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/teams-update-run-events', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateRunEvents(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateRunEvents'
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
    print(TeamsUpdateRunEvents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
