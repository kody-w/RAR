---
name: "rar-cowork-cookbook-demo-data-refine-the-training-program"
description: "Generates and creates realistic demo records for refine the training program in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_refine_the_training_program", "rar_sha256": "eea789b01c44187fe5d10e437cae2f87d03da7cbf0367913080b1ba0c6989cbb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_refine_the_training_program_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-refine-the-training-program:e830924641ac791257256fc28edf8928fba26b85abdfa80611e134bf5f30c6b5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_refine_the_training_program`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_refine_the_training_program_agent.py` is
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

Refine the training program Demo Data Generator — Generates and creates realistic demo records for refine the training program in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-refine-the-training-program
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_refine_the_training_program_agent.py` and embedded as the fenced Python below (sha256 eea789b01c44187f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_refine_the_training_program_agent.py` first:

```bash
python3 demo_data_refine_the_training_program_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_refine_the_training_program_agent.py   # or on stdin
python3 demo_data_refine_the_training_program_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Refine the training program Demo Data Generator — Generates and creates realistic demo records for refine the training program in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-refine-the-training-program
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_refine_the_training_program',
    "version": '2.0.0',
    "display_name": 'Refine the training program Demo Data Generator',
    "description": 'Generates and creates realistic demo records for refine the training program in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-refine-the-training-program',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-refine-the-training-program',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b914e24f576d9b03',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/refine-the-training-program'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-refine-the-training-program', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataRefineTheTrainingProgram(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataRefineTheTrainingProgram'
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
    print(DemoDataRefineTheTrainingProgram().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
