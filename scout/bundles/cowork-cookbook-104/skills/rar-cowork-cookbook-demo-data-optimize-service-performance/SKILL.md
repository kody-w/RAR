---
name: "rar-cowork-cookbook-demo-data-optimize-service-performance"
description: "Generates and creates realistic demo records for optimize service performance in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_optimize_service_performance", "rar_sha256": "f26e68b22bf1b83d1d7356f18f5f0b51ebdc882c8e5b9c72f893bb8894461b75", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_optimize_service_performance`. The original RAPP
agent is preserved byte-for-byte in `demo_data_optimize_service_performance_agent.py` and in the RCI capsule.

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

Optimize service performance Demo Data Generator — Generates and creates realistic demo records for optimize service performance in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-optimize-service-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_optimize_service_performance_agent.py` and embedded as the fenced Python below (sha256 f26e68b22bf1b83d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_optimize_service_performance_agent.py` first:

```bash
python3 demo_data_optimize_service_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_optimize_service_performance_agent.py   # or on stdin
python3 demo_data_optimize_service_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Optimize service performance Demo Data Generator — Generates and creates realistic demo records for optimize service performance in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-optimize-service-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_optimize_service_performance',
    "version": '2.0.1',
    "display_name": 'Optimize service performance Demo Data Generator',
    "description": 'Generates and creates realistic demo records for optimize service performance in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-optimize-service-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-optimize-service-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7d0d80106334bddb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/analyze-service-performance/optimize-service-performance'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/demo-data-optimize-service-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataOptimizeServicePerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataOptimizeServicePerformance'
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
    print(DemoDataOptimizeServicePerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
