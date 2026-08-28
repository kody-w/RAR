---
name: "rar-cowork-cookbook-demo-data-develop-production-processes"
description: "Generates and creates realistic demo records for develop production processes in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_production_processes", "rar_sha256": "9bbbe4c4a836cb23887ba355c80822ed94d824c4f903e340763f213149d6b999", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_production_processes_agent.py` and embedded as the fenced Python below (sha256 9bbbe4c4a836cb23…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_production_processes_agent.py` first:

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
    "version": '2.0.0',
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
