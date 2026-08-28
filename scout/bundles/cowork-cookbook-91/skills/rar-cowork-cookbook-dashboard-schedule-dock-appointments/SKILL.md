---
name: "rar-cowork-cookbook-dashboard-schedule-dock-appointments"
description: "Produces a self-contained interactive HTML dashboard for schedule dock appointments - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_schedule_dock_appointments", "rar_sha256": "4993d32ed39823279b47c359ac9896819a1ca41096a216046b934e6d15e52178", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_schedule_dock_appointments`. The original RAPP
agent is preserved byte-for-byte in `dashboard_schedule_dock_appointments_agent.py` and in the RCI capsule.

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

Schedule dock appointments Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for schedule dock appointments - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-schedule-dock-appointments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_schedule_dock_appointments_agent.py` and embedded as the fenced Python below (sha256 4993d32ed3982327…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_schedule_dock_appointments_agent.py` first:

```bash
python3 dashboard_schedule_dock_appointments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_schedule_dock_appointments_agent.py   # or on stdin
python3 dashboard_schedule_dock_appointments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Schedule dock appointments Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for schedule dock appointments - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-schedule-dock-appointments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_schedule_dock_appointments',
    "version": '2.0.1',
    "display_name": 'Schedule dock appointments Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for schedule dock appointments - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-schedule-dock-appointments',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-schedule-dock-appointments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ab1a5ff2eb379b61',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/schedule-dock-appointments'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/dashboard-schedule-dock-appointments', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardScheduleDockAppointments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardScheduleDockAppointments'
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
    print(DashboardScheduleDockAppointments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
