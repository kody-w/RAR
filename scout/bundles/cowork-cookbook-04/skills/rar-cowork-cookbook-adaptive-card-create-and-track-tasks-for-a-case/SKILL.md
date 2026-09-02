---
name: "rar-cowork-cookbook-adaptive-card-create-and-track-tasks-for-a-case"
description: "Produces a reusable Adaptive Card JSON snapshot of create and track tasks for a case status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_create_and_track_tasks_for_a_case", "rar_sha256": "485d2dd87b805de268c059642e63f0a3bc405c04559ba914864620ed24749128", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_create_and_track_tasks_for_a_case_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-create-and-track-tasks-for-a-case:6ba4de44390bcbbb62ac1e77fa4c087d09b598f22aa0cc0c594db1a1d944afef", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_create_and_track_tasks_for_a_case`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_create_and_track_tasks_for_a_case_agent.py` is
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

Create and track tasks for a case Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of create and track tasks for a case status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-create-and-track-tasks-for-a-case
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_create_and_track_tasks_for_a_case_agent.py` and embedded as the fenced Python below (sha256 485d2dd87b805de2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_create_and_track_tasks_for_a_case_agent.py` first:

```bash
python3 adaptive_card_create_and_track_tasks_for_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_create_and_track_tasks_for_a_case_agent.py   # or on stdin
python3 adaptive_card_create_and_track_tasks_for_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create and track tasks for a case Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of create and track tasks for a case status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-create-and-track-tasks-for-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_create_and_track_tasks_for_a_case',
    "version": '2.0.0',
    "display_name": 'Create and track tasks for a case Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of create and track tasks for a case status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-create-and-track-tasks-for-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-create-and-track-tasks-for-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e4b5ef57665501c8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/create-and-track-tasks-for-a-case'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/adaptive-card-create-and-track-tasks-for-a-case', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardCreateAndTrackTasksForACase(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardCreateAndTrackTasksForACase'
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
    print(AdaptiveCardCreateAndTrackTasksForACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
