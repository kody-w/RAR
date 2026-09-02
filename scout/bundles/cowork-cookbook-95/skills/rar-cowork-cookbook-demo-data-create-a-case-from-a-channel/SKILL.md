---
name: "rar-cowork-cookbook-demo-data-create-a-case-from-a-channel"
description: "Generates and creates realistic demo records for create a case from a channel in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_create_a_case_from_a_channel", "rar_sha256": "8f320dfb42289062ab3d219714de73eded62b71e67c9ee90cd09fe7adb33cbae", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_create_a_case_from_a_channel_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-create-a-case-from-a-channel:4923982ae41f2d5a9e183d8ed4f58fb354b2ad267f9df49b51ef2c643dbe5cd5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_create_a_case_from_a_channel`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_create_a_case_from_a_channel_agent.py` is
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
