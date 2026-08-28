---
name: "rar-cowork-cookbook-demo-data-develop-production-processes"
description: "Generates and creates realistic demo records for develop production processes in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_production_processes", "rar_sha256": "97ef3fafdd7521c7a63e1d9c64d87ab2d45dd32b5abfee5923f7f6a7513b37cd", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_develop_production_processes`. The original RAPP
agent is preserved byte-for-byte in `demo_data_develop_production_processes_agent.py` and in the RCI capsule.

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

Develop production processes Demo Data Generator — Generates and creates realistic demo records for develop production processes in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-production-processes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_production_processes_agent.py` and embedded as the fenced Python below (sha256 97ef3fafdd7521c7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_production_processes_agent.py` first:

```bash
python3 demo_data_develop_production_processes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_production_processes_agent.py   # or on stdin
python3 demo_data_develop_production_processes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop production processes Demo Data Generator — Generates and creates realistic demo records for develop production processes in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-production-processes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_production_processes',
    "version": '2.0.1',
    "display_name": 'Develop production processes Demo Data Generator',
    "description": 'Generates and creates realistic demo records for develop production processes in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-develop-production-processes',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-production-processes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6527e59b48819249',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies/develop-production-processes'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/demo-data-develop-production-processes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataDevelopProductionProcesses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopProductionProcesses'
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
    print(DemoDataDevelopProductionProcesses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
