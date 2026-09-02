---
name: "rar-cowork-cookbook-demo-data-develop-production-processes"
description: "Generates and creates realistic demo records for develop production processes in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_production_processes", "rar_sha256": "9bbbe4c4a836cb23887ba355c80822ed94d824c4f903e340763f213149d6b999", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_develop_production_processes_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-develop-production-processes:1952330323bbec9bc9fcf41b8f22b8c72ea95556625b67b890dc8bb459d36f24", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_develop_production_processes`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_develop_production_processes_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
