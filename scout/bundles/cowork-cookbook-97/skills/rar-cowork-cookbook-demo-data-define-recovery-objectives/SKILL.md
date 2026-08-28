---
name: "rar-cowork-cookbook-demo-data-define-recovery-objectives"
description: "Generates and creates realistic demo records for define recovery objectives in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_define_recovery_objectives", "rar_sha256": "c58dce74791d43a7321d987bd040cbf0deeef1d6fcc1b402a4de2c0f9d6fd2a7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_define_recovery_objectives`. The original RAPP
agent is preserved byte-for-byte in `demo_data_define_recovery_objectives_agent.py` and in the RCI capsule.

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

Define recovery objectives Demo Data Generator — Generates and creates realistic demo records for define recovery objectives in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-recovery-objectives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_define_recovery_objectives_agent.py` and embedded as the fenced Python below (sha256 c58dce74791d43a7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_define_recovery_objectives_agent.py` first:

```bash
python3 demo_data_define_recovery_objectives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_define_recovery_objectives_agent.py   # or on stdin
python3 demo_data_define_recovery_objectives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define recovery objectives Demo Data Generator — Generates and creates realistic demo records for define recovery objectives in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-define-recovery-objectives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_define_recovery_objectives',
    "version": '2.0.1',
    "display_name": 'Define recovery objectives Demo Data Generator',
    "description": 'Generates and creates realistic demo records for define recovery objectives in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-define-recovery-objectives',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-define-recovery-objectives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '425a1557d7a88d3e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/define-recovery-objectives'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-define-recovery-objectives', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataDefineRecoveryObjectives(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDefineRecoveryObjectives'
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
    print(DemoDataDefineRecoveryObjectives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
