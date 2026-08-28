---
name: "rar-cowork-cookbook-teams-update-run-events"
description: "Drafts a Teams channel post on run events status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_run_events", "rar_sha256": "fe7d21d3f0c69f0f72ef209de7832782917a6293377cf7a68e4efbc85d49e12c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_run_events`. The original RAPP
agent is preserved byte-for-byte in `teams_update_run_events_agent.py` and in the RCI capsule.

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
