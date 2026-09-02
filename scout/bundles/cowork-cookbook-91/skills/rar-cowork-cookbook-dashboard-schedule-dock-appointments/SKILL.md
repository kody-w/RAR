---
name: "rar-cowork-cookbook-dashboard-schedule-dock-appointments"
description: "Produces a self-contained interactive HTML dashboard for schedule dock appointments - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_schedule_dock_appointments", "rar_sha256": "31a61d5bc24bb77d43dfcd0b0b34f1df52980f720729e9a5d30f2a2380fc68ec", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_schedule_dock_appointments_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-schedule-dock-appointments:5828396db7a506e5c6276b79667f1c33782f00b1bc8d3530d599f449b883a10f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_schedule_dock_appointments`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_schedule_dock_appointments_agent.py` is
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
