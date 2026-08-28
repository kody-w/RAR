---
name: "rar-cowork-cookbook-dashboard-monitor-data-synchronization-failures"
description: "Produces a self-contained interactive HTML dashboard for monitor data synchronization failures - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_data_synchronization_failures", "rar_sha256": "e82a621b41f136d6c41ec47af1100429bf49170614d32ad805554296a4ca860b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_monitor_data_synchronization_failures_agent.py` and embedded as the fenced Python below (sha256 e82a621b41f136d6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_monitor_data_synchronization_failures_agent.py` first:

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
    "version": '2.0.1',
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
