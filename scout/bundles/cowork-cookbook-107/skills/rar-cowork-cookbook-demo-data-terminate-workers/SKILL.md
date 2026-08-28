---
name: "rar-cowork-cookbook-demo-data-terminate-workers"
description: "Generates and creates realistic demo records for terminate workers in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_terminate_workers", "rar_sha256": "24fc672875e5edbd79108e29153fe37e2c5ccee50c1b9d37d0732c7d791d4a91", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_terminate_workers_agent.py` and embedded as the fenced Python below (sha256 24fc672875e5edbd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_terminate_workers_agent.py` first:

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
    "version": '2.0.0',
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
