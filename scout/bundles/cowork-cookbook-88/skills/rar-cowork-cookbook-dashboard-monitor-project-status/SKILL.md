---
name: "rar-cowork-cookbook-dashboard-monitor-project-status"
description: "Produces a self-contained interactive HTML dashboard for monitor project status - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_project_status", "rar_sha256": "26387cf52486c19157f9c269f1b994eece31687240011d57ef042d2a05481442", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_monitor_project_status`. The original RAPP
agent is preserved byte-for-byte in `dashboard_monitor_project_status_agent.py` and in the RCI capsule.

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

Monitor project status Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for monitor project status - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-monitor-project-status
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_monitor_project_status_agent.py` and embedded as the fenced Python below (sha256 26387cf52486c191…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_monitor_project_status_agent.py` first:

```bash
python3 dashboard_monitor_project_status_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_monitor_project_status_agent.py   # or on stdin
python3 dashboard_monitor_project_status_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor project status Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for monitor project status - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-monitor-project-status
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_monitor_project_status',
    "version": '2.0.1',
    "display_name": 'Monitor project status Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for monitor project status - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-monitor-project-status',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-monitor-project-status',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4abad62186270302',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/analyze-project-performance/monitor-project-status'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/dashboard-monitor-project-status', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardMonitorProjectStatus(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMonitorProjectStatus'
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
    print(DashboardMonitorProjectStatus().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
