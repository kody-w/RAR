---
name: "rar-cowork-cookbook-dashboard-configure-monitoring-and-alert-systems"
description: "Produces a self-contained interactive HTML dashboard for configure monitoring and alert systems - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_configure_monitoring_and_alert_systems", "rar_sha256": "8986df07f2c9a1044e1bd35a911981f85f4ecfda329c214a68e5ad1c3017592a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_configure_monitoring_and_alert_systems_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-configure-monitoring-and-alert-systems:7deb0326041cfbd3888a3fd0c3c8e5e5f51f14b7a7eda7b941633ef6926f023c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_configure_monitoring_and_alert_systems`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_configure_monitoring_and_alert_systems_agent.py` is
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

Configure monitoring and alert systems Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for configure monitoring and alert systems - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-configure-monitoring-and-alert-systems
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_configure_monitoring_and_alert_systems_agent.py` and embedded as the fenced Python below (sha256 8986df07f2c9a104…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_configure_monitoring_and_alert_systems_agent.py` first:

```bash
python3 dashboard_configure_monitoring_and_alert_systems_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_configure_monitoring_and_alert_systems_agent.py   # or on stdin
python3 dashboard_configure_monitoring_and_alert_systems_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure monitoring and alert systems Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for configure monitoring and alert systems - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-configure-monitoring-and-alert-systems
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_configure_monitoring_and_alert_systems',
    "version": '2.0.0',
    "display_name": 'Configure monitoring and alert systems Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for configure monitoring and alert systems - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-configure-monitoring-and-alert-systems',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-configure-monitoring-and-alert-systems',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '024a2974f934f648',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/configure-monitoring-and-alert-systems'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-configure-monitoring-and-alert-systems', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardConfigureMonitoringAndAlertSystems(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardConfigureMonitoringAndAlertSystems'
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
    print(DashboardConfigureMonitoringAndAlertSystems().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
