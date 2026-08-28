---
name: "rar-cowork-cookbook-dashboard-monitor-data-synchronization-failures"
description: "Produces a self-contained interactive HTML dashboard for monitor data synchronization failures - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_data_synchronization_failures", "rar_sha256": "a4fe3f16022cc206e98f69a099e9579860e6051538ef6b3affcf045eee8a3598", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_monitor_data_synchronization_failures`. The original RAPP
agent is preserved byte-for-byte in `dashboard_monitor_data_synchronization_failures_agent.py` and in the RCI capsule.

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

Monitor data synchronization failures Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for monitor data synchronization failures - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-monitor-data-synchronization-failures
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_monitor_data_synchronization_failures_agent.py` and embedded as the fenced Python below (sha256 a4fe3f16022cc206…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_monitor_data_synchronization_failures_agent.py` first:

```bash
python3 dashboard_monitor_data_synchronization_failures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_monitor_data_synchronization_failures_agent.py   # or on stdin
python3 dashboard_monitor_data_synchronization_failures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor data synchronization failures Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for monitor data synchronization failures - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-monitor-data-synchronization-failures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_monitor_data_synchronization_failures',
    "version": '2.0.0',
    "display_name": 'Monitor data synchronization failures Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for monitor data synchronization failures - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-monitor-data-synchronization-failures',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-monitor-data-synchronization-failures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c31aaa5642066ddf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-data/monitor-data-synchronization-failures'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-monitor-data-synchronization-failures', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardMonitorDataSynchronizationFailures(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMonitorDataSynchronizationFailures'
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
    print(DashboardMonitorDataSynchronizationFailures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
