---
name: "rar-cowork-cookbook-demo-data-terminate-workers"
description: "Generates and creates realistic demo records for terminate workers in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_terminate_workers", "rar_sha256": "4ee0fced8f7c73b0a631163976e5ea920790f539fb8186d7651694d3494bfcdc", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_terminate_workers`. The original RAPP
agent is preserved byte-for-byte in `demo_data_terminate_workers_agent.py` and in the RCI capsule.

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

Terminate workers Demo Data Generator — Generates and creates realistic demo records for terminate workers in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-terminate-workers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_terminate_workers_agent.py` and embedded as the fenced Python below (sha256 4ee0fced8f7c73b0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_terminate_workers_agent.py` first:

```bash
python3 demo_data_terminate_workers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_terminate_workers_agent.py   # or on stdin
python3 demo_data_terminate_workers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Terminate workers Demo Data Generator — Generates and creates realistic demo records for terminate workers in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-terminate-workers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_terminate_workers',
    "version": '2.0.1',
    "display_name": 'Terminate workers Demo Data Generator',
    "description": 'Generates and creates realistic demo records for terminate workers in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-terminate-workers',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-terminate-workers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4396caa24bff6eab',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/offboard-talent/terminate-workers'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/demo-data-terminate-workers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataTerminateWorkers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataTerminateWorkers'
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
    print(DemoDataTerminateWorkers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
