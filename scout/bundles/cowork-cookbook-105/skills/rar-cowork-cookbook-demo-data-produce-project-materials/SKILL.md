---
name: "rar-cowork-cookbook-demo-data-produce-project-materials"
description: "Generates and creates realistic demo records for produce project materials in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_produce_project_materials", "rar_sha256": "56e09629c17989e221ad9c2aa270bcffed01f38122d14691dae388918edad4b3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_produce_project_materials`. The original RAPP
agent is preserved byte-for-byte in `demo_data_produce_project_materials_agent.py` and in the RCI capsule.

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

Produce project materials Demo Data Generator — Generates and creates realistic demo records for produce project materials in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-produce-project-materials
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_produce_project_materials_agent.py` and embedded as the fenced Python below (sha256 56e09629c17989e2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_produce_project_materials_agent.py` first:

```bash
python3 demo_data_produce_project_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_produce_project_materials_agent.py   # or on stdin
python3 demo_data_produce_project_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Produce project materials Demo Data Generator — Generates and creates realistic demo records for produce project materials in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-produce-project-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_produce_project_materials',
    "version": '2.0.0',
    "display_name": 'Produce project materials Demo Data Generator',
    "description": 'Generates and creates realistic demo records for produce project materials in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-produce-project-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-produce-project-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f37241e4d756b505',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/produce-project-materials'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/demo-data-produce-project-materials', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataProduceProjectMaterials(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataProduceProjectMaterials'
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
    print(DemoDataProduceProjectMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
