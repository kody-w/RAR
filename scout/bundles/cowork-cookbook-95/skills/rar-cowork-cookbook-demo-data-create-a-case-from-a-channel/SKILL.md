---
name: "rar-cowork-cookbook-demo-data-create-a-case-from-a-channel"
description: "Generates and creates realistic demo records for create a case from a channel in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_create_a_case_from_a_channel", "rar_sha256": "6692ce897e26cf746a7e97d0353293815e7ba6a74d8c1732719ec3c993d74b11", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_create_a_case_from_a_channel`. The original RAPP
agent is preserved byte-for-byte in `demo_data_create_a_case_from_a_channel_agent.py` and in the RCI capsule.

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

Create a case from a channel Demo Data Generator — Generates and creates realistic demo records for create a case from a channel in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-create-a-case-from-a-channel
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_create_a_case_from_a_channel_agent.py` and embedded as the fenced Python below (sha256 6692ce897e26cf74…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_create_a_case_from_a_channel_agent.py` first:

```bash
python3 demo_data_create_a_case_from_a_channel_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_create_a_case_from_a_channel_agent.py   # or on stdin
python3 demo_data_create_a_case_from_a_channel_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create a case from a channel Demo Data Generator — Generates and creates realistic demo records for create a case from a channel in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-create-a-case-from-a-channel
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_create_a_case_from_a_channel',
    "version": '2.0.1',
    "display_name": 'Create a case from a channel Demo Data Generator',
    "description": 'Generates and creates realistic demo records for create a case from a channel in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-create-a-case-from-a-channel',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-create-a-case-from-a-channel',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'db48ee14f395c680',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/intake-cases/create-a-case-from-a-channel'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/demo-data-create-a-case-from-a-channel', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataCreateACaseFromAChannel(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataCreateACaseFromAChannel'
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
    print(DemoDataCreateACaseFromAChannel().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
