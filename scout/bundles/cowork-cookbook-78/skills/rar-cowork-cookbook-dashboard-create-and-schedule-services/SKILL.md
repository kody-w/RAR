---
name: "rar-cowork-cookbook-dashboard-create-and-schedule-services"
description: "Produces a self-contained interactive HTML dashboard for create and schedule services - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_create_and_schedule_services", "rar_sha256": "dfc2998dd49d78c2646d8f4c0a99be1cbef6de9a8079fae06c32fc9d7cff48f4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_create_and_schedule_services`. The original RAPP
agent is preserved byte-for-byte in `dashboard_create_and_schedule_services_agent.py` and in the RCI capsule.

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

Create and schedule services Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for create and schedule services - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-and-schedule-services
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_create_and_schedule_services_agent.py` and embedded as the fenced Python below (sha256 dfc2998dd49d78c2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_create_and_schedule_services_agent.py` first:

```bash
python3 dashboard_create_and_schedule_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_create_and_schedule_services_agent.py   # or on stdin
python3 dashboard_create_and_schedule_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create and schedule services Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for create and schedule services - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-and-schedule-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_create_and_schedule_services',
    "version": '2.0.1',
    "display_name": 'Create and schedule services Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for create and schedule services - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-create-and-schedule-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-create-and-schedule-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ecfb4cf4bdef7fb0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/create-and-schedule-services'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/dashboard-create-and-schedule-services', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'word:schedule'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardCreateAndScheduleServices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardCreateAndScheduleServices'
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
    print(DashboardCreateAndScheduleServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
