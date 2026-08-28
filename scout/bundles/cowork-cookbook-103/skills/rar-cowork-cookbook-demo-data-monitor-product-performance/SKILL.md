---
name: "rar-cowork-cookbook-demo-data-monitor-product-performance"
description: "Generates and creates realistic demo records for monitor product performance in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_monitor_product_performance", "rar_sha256": "18b2c61d5947a900469cf55c7577ecd41249ff9ed72ec2a905092cad2f7d359a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_monitor_product_performance`. The original RAPP
agent is preserved byte-for-byte in `demo_data_monitor_product_performance_agent.py` and in the RCI capsule.

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

Monitor product performance Demo Data Generator — Generates and creates realistic demo records for monitor product performance in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-monitor-product-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_monitor_product_performance_agent.py` and embedded as the fenced Python below (sha256 18b2c61d5947a900…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_monitor_product_performance_agent.py` first:

```bash
python3 demo_data_monitor_product_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_monitor_product_performance_agent.py   # or on stdin
python3 demo_data_monitor_product_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor product performance Demo Data Generator — Generates and creates realistic demo records for monitor product performance in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-monitor-product-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_monitor_product_performance',
    "version": '2.0.1',
    "display_name": 'Monitor product performance Demo Data Generator',
    "description": 'Generates and creates realistic demo records for monitor product performance in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-monitor-product-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-monitor-product-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd0f000e552949f9c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/analyze-product-performance/monitor-product-performance'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/demo-data-monitor-product-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataMonitorProductPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataMonitorProductPerformance'
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
    print(DemoDataMonitorProductPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
