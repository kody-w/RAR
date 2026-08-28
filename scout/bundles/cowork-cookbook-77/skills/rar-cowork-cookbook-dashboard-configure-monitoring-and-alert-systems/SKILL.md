---
name: "rar-cowork-cookbook-dashboard-configure-monitoring-and-alert-systems"
description: "Produces a self-contained interactive HTML dashboard for configure monitoring and alert systems - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_configure_monitoring_and_alert_systems", "rar_sha256": "7674f78d3c531143d0198667b5c0bbc1fac778de1b8bccc37e717f5a5bdae881", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_configure_monitoring_and_alert_systems`. The original RAPP
agent is preserved byte-for-byte in `dashboard_configure_monitoring_and_alert_systems_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_configure_monitoring_and_alert_systems_agent.py` and embedded as the fenced Python below (sha256 7674f78d3c531143…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_configure_monitoring_and_alert_systems_agent.py` first:

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
    "version": '2.0.1',
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
