---
name: "rar-cowork-cookbook-demo-data-optimize-service-performance"
description: "Generates and creates realistic demo records for optimize service performance in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_optimize_service_performance", "rar_sha256": "410539822055de7bb6b96843276fc9ca552ce02c92e1059b055116acbb62f2aa", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_optimize_service_performance_agent.py` and embedded as the fenced Python below (sha256 410539822055de7b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_optimize_service_performance_agent.py` first:

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
    "version": '2.0.0',
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
