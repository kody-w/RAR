---
name: "rar-cowork-cookbook-demo-data-monitor-system-performance-and-health"
description: "Generates and creates realistic demo records for monitor system performance and health in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_monitor_system_performance_and_health", "rar_sha256": "564301f8700d68e5f8378be9f64a423cdae093bd9142c07a0dbb781842612a75", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_monitor_system_performance_and_health`. The original RAPP
agent is preserved byte-for-byte in `demo_data_monitor_system_performance_and_health_agent.py` and in the RCI capsule.

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
