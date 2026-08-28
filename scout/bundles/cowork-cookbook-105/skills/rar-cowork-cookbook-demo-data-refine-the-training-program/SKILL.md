---
name: "rar-cowork-cookbook-demo-data-refine-the-training-program"
description: "Generates and creates realistic demo records for refine the training program in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_refine_the_training_program", "rar_sha256": "eea789b01c44187fe5d10e437cae2f87d03da7cbf0367913080b1ba0c6989cbb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_refine_the_training_program`. The original RAPP
agent is preserved byte-for-byte in `demo_data_refine_the_training_program_agent.py` and in the RCI capsule.

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
