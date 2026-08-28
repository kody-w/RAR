---
name: "rar-cowork-cookbook-demo-data-asses-worker-performance"
description: "Generates and creates realistic demo records for asses worker performance in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_asses_worker_performance", "rar_sha256": "34051d5bddcf0f7a96c34a706b23df7b29e1f611e3a39de6e36ea03cab620d86", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_asses_worker_performance`. The original RAPP
agent is preserved byte-for-byte in `demo_data_asses_worker_performance_agent.py` and in the RCI capsule.

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

Asses worker performance Demo Data Generator — Generates and creates realistic demo records for asses worker performance in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-asses-worker-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_asses_worker_performance_agent.py` and embedded as the fenced Python below (sha256 34051d5bddcf0f7a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_asses_worker_performance_agent.py` first:

```bash
python3 demo_data_asses_worker_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_asses_worker_performance_agent.py   # or on stdin
python3 demo_data_asses_worker_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Asses worker performance Demo Data Generator — Generates and creates realistic demo records for asses worker performance in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-asses-worker-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_asses_worker_performance',
    "version": '2.0.1',
    "display_name": 'Asses worker performance Demo Data Generator',
    "description": 'Generates and creates realistic demo records for asses worker performance in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-asses-worker-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-asses-worker-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a77e388bfc101ec1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/asses-worker-performance'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/demo-data-asses-worker-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataAssesWorkerPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAssesWorkerPerformance'
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
    print(DemoDataAssesWorkerPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
