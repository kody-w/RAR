---
name: "rar-cowork-cookbook-demo-data-produce-project-materials"
description: "Generates and creates realistic demo records for produce project materials in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_produce_project_materials", "rar_sha256": "56e09629c17989e221ad9c2aa270bcffed01f38122d14691dae388918edad4b3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_produce_project_materials_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-produce-project-materials:73bd5c079ead9430e10ee226b718998367ea2b4d3744af1d8c4eee4b7a2adc79", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_produce_project_materials`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_produce_project_materials_agent.py` is
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
