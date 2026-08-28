---
name: "rar-cowork-cookbook-demo-data-monitor-system-performance-and-health"
description: "Generates and creates realistic demo records for monitor system performance and health in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_monitor_system_performance_and_health", "rar_sha256": "16244b013efd61b91a88793d64f7016afd458b1098cb9afa52cb4dae32707d25", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_monitor_system_performance_and_health_agent.py` and embedded as the fenced Python below (sha256 16244b013efd61b9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_monitor_system_performance_and_health_agent.py` first:

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
    "version": '2.0.1',
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
