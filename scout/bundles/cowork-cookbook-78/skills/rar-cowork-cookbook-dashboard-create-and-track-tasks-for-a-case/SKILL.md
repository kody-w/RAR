---
name: "rar-cowork-cookbook-dashboard-create-and-track-tasks-for-a-case"
description: "Produces a self-contained interactive HTML dashboard for create and track tasks for a case - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_create_and_track_tasks_for_a_case", "rar_sha256": "88c44a50e7c38144026fd2ea81cf76792b3fe08347094dd03159febfee023cce", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_create_and_track_tasks_for_a_case`. The original RAPP
agent is preserved byte-for-byte in `dashboard_create_and_track_tasks_for_a_case_agent.py` and in the RCI capsule.

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
