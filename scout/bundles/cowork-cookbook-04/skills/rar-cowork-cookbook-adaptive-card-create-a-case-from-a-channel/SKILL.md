---
name: "rar-cowork-cookbook-adaptive-card-create-a-case-from-a-channel"
description: "Produces a reusable Adaptive Card JSON snapshot of create a case from a channel status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_create_a_case_from_a_channel", "rar_sha256": "29d8de4f968353c2e9c760f4fe04f7103ab2ba055997fb9ade9aa29840f7b5ff", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_create_a_case_from_a_channel`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_create_a_case_from_a_channel_agent.py` and in the RCI capsule.

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

Create a case from a channel Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of create a case from a channel status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-create-a-case-from-a-channel
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_create_a_case_from_a_channel_agent.py` and embedded as the fenced Python below (sha256 29d8de4f968353c2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_create_a_case_from_a_channel_agent.py` first:

```bash
python3 adaptive_card_create_a_case_from_a_channel_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_create_a_case_from_a_channel_agent.py   # or on stdin
python3 adaptive_card_create_a_case_from_a_channel_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create a case from a channel Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of create a case from a channel status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-create-a-case-from-a-channel
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_create_a_case_from_a_channel',
    "version": '2.0.1',
    "display_name": 'Create a case from a channel Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of create a case from a channel status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-create-a-case-from-a-channel',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-create-a-case-from-a-channel',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1e126d0d736b4e7b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/intake-cases/create-a-case-from-a-channel'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/adaptive-card-create-a-case-from-a-channel', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardCreateACaseFromAChannel(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardCreateACaseFromAChannel'
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
    print(AdaptiveCardCreateACaseFromAChannel().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
