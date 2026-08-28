---
name: "rar-cowork-cookbook-demo-data-refine-the-training-program"
description: "Generates and creates realistic demo records for refine the training program in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_refine_the_training_program", "rar_sha256": "2b042fee052ac6cb91ff24b1cf94dff8939f06b1e33244f25da2889b9517d8cc", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_refine_the_training_program_agent.py` and embedded as the fenced Python below (sha256 2b042fee052ac6cb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_refine_the_training_program_agent.py` first:

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
    "version": '2.0.1',
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
