---
name: "rar-cowork-cookbook-dashboard-monitor-data-synchronization-failures"
description: "Produces a self-contained interactive HTML dashboard for monitor data synchronization failures - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_data_synchronization_failures", "rar_sha256": "a4fe3f16022cc206e98f69a099e9579860e6051538ef6b3affcf045eee8a3598", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_monitor_data_synchronization_failures_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-monitor-data-synchronization-failures:d9c96d2773ea28b9fa3c7f0bd30444ab80efc7accf4ae947b5c44f86ea71673f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_monitor_data_synchronization_failures`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_monitor_data_synchronization_failures_agent.py` is
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
