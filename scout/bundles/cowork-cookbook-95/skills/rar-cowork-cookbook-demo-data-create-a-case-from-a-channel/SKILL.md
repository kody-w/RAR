---
name: "rar-cowork-cookbook-demo-data-create-a-case-from-a-channel"
description: "Generates and creates realistic demo records for create a case from a channel in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_create_a_case_from_a_channel", "rar_sha256": "8f320dfb42289062ab3d219714de73eded62b71e67c9ee90cd09fe7adb33cbae", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_create_a_case_from_a_channel_agent.py` and embedded as the fenced Python below (sha256 8f320dfb42289062…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_create_a_case_from_a_channel_agent.py` first:

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
    "version": '2.0.0',
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
