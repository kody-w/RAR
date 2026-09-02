---
name: "rar-cowork-cookbook-dashboard-create-and-track-tasks-for-a-case"
description: "Produces a self-contained interactive HTML dashboard for create and track tasks for a case - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_create_and_track_tasks_for_a_case", "rar_sha256": "88c44a50e7c38144026fd2ea81cf76792b3fe08347094dd03159febfee023cce", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_create_and_track_tasks_for_a_case_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-create-and-track-tasks-for-a-case:56bd330dd8cfeab824aa1c31eb8fb16bd6e99a248a06f0f31673630b5a4f9aec", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_create_and_track_tasks_for_a_case`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_create_and_track_tasks_for_a_case_agent.py` is
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

Create and track tasks for a case Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for create and track tasks for a case - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-and-track-tasks-for-a-case
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_create_and_track_tasks_for_a_case_agent.py` and embedded as the fenced Python below (sha256 88c44a50e7c38144…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_create_and_track_tasks_for_a_case_agent.py` first:

```bash
python3 dashboard_create_and_track_tasks_for_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_create_and_track_tasks_for_a_case_agent.py   # or on stdin
python3 dashboard_create_and_track_tasks_for_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create and track tasks for a case Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for create and track tasks for a case - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-and-track-tasks-for-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_create_and_track_tasks_for_a_case',
    "version": '2.0.0',
    "display_name": 'Create and track tasks for a case Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for create and track tasks for a case - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-create-and-track-tasks-for-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-create-and-track-tasks-for-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fbd67c1f5a8bd93a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/create-and-track-tasks-for-a-case'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/dashboard-create-and-track-tasks-for-a-case', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardCreateAndTrackTasksForACase(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardCreateAndTrackTasksForACase'
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
    print(DashboardCreateAndTrackTasksForACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
