---
name: "rar-cowork-cookbook-dashboard-schedule-dock-appointments"
description: "Produces a self-contained interactive HTML dashboard for schedule dock appointments - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_schedule_dock_appointments", "rar_sha256": "31a61d5bc24bb77d43dfcd0b0b34f1df52980f720729e9a5d30f2a2380fc68ec", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_schedule_dock_appointments_agent.py` and embedded as the fenced Python below (sha256 31a61d5bc24bb77d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_schedule_dock_appointments_agent.py` first:

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
    "version": '2.0.0',
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
