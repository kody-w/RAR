---
name: "rar-cowork-cookbook-dashboard-monitor-project-status"
description: "Produces a self-contained interactive HTML dashboard for monitor project status - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_project_status", "rar_sha256": "747b545e1e0615bbf300ff204ac2cea2a7bb0e7ca7b00e3033828a319b1be7ad", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_monitor_project_status_agent.py` and embedded as the fenced Python below (sha256 747b545e1e0615bb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_monitor_project_status_agent.py` first:

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
    "version": '2.0.0',
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
