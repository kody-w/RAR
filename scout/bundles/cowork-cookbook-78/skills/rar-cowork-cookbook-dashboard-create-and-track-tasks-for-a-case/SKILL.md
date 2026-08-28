---
name: "rar-cowork-cookbook-dashboard-create-and-track-tasks-for-a-case"
description: "Produces a self-contained interactive HTML dashboard for create and track tasks for a case - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_create_and_track_tasks_for_a_case", "rar_sha256": "0887c062bffd28bd6e001cc47504fbc72e516f45a704175b9bd144aaec0b204e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_create_and_track_tasks_for_a_case_agent.py` and embedded as the fenced Python below (sha256 0887c062bffd28bd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_create_and_track_tasks_for_a_case_agent.py` first:

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
    "version": '2.0.1',
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
