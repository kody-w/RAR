---
name: "rar-cowork-cookbook-dashboard-configure-monitoring-and-alert-systems"
description: "Produces a self-contained interactive HTML dashboard for configure monitoring and alert systems - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_configure_monitoring_and_alert_systems", "rar_sha256": "8986df07f2c9a1044e1bd35a911981f85f4ecfda329c214a68e5ad1c3017592a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
