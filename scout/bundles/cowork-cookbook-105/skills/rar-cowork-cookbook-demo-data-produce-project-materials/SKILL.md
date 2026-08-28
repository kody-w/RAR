---
name: "rar-cowork-cookbook-demo-data-produce-project-materials"
description: "Generates and creates realistic demo records for produce project materials in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_produce_project_materials", "rar_sha256": "6f353ff253d13c6b91bc925e7b546ddad7e8e061a1bea02f3b49feca1a34cffd", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_produce_project_materials_agent.py` and embedded as the fenced Python below (sha256 6f353ff253d13c6b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_produce_project_materials_agent.py` first:

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
    "version": '2.0.1',
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
