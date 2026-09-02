---
name: "rar-cowork-cookbook-dashboard-monitor-project-status"
description: "Produces a self-contained interactive HTML dashboard for monitor project status - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_project_status", "rar_sha256": "747b545e1e0615bbf300ff204ac2cea2a7bb0e7ca7b00e3033828a319b1be7ad", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_monitor_project_status_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-monitor-project-status:634071a5584bdc377ef09d99352d1b3573998147fe2b7bbab0fd43e9af0d4627", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_monitor_project_status`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_monitor_project_status_agent.py` is
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
