---
name: "rar-cowork-cookbook-demo-data-monitor-system-performance-and-health"
description: "Generates and creates realistic demo records for monitor system performance and health in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_monitor_system_performance_and_health", "rar_sha256": "564301f8700d68e5f8378be9f64a423cdae093bd9142c07a0dbb781842612a75", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_monitor_system_performance_and_health_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-monitor-system-performance-and-health:5ab4fd62c4496380f0957eb24d319a1be21603f3d717c51b982b2635861f7719", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_monitor_system_performance_and_health`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_monitor_system_performance_and_health_agent.py` is
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

Monitor system performance and health Demo Data Generator — Generates and creates realistic demo records for monitor system performance and health in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-monitor-system-performance-and-health
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_monitor_system_performance_and_health_agent.py` and embedded as the fenced Python below (sha256 564301f8700d68e5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_monitor_system_performance_and_health_agent.py` first:

```bash
python3 demo_data_monitor_system_performance_and_health_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_monitor_system_performance_and_health_agent.py   # or on stdin
python3 demo_data_monitor_system_performance_and_health_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor system performance and health Demo Data Generator — Generates and creates realistic demo records for monitor system performance and health in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-monitor-system-performance-and-health
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_monitor_system_performance_and_health',
    "version": '2.0.0',
    "display_name": 'Monitor system performance and health Demo Data Generator',
    "description": 'Generates and creates realistic demo records for monitor system performance and health in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-monitor-system-performance-and-health',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-monitor-system-performance-and-health',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6e81880dbd35ad25',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/monitor-system-performance-and-health'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-monitor-system-performance-and-health', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataMonitorSystemPerformanceAndHealth(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataMonitorSystemPerformanceAndHealth'
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
    print(DemoDataMonitorSystemPerformanceAndHealth().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
