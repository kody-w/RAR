---
name: "rar-cowork-cookbook-adaptive-card-create-a-case-from-a-channel"
description: "Produces a reusable Adaptive Card JSON snapshot of create a case from a channel status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_create_a_case_from_a_channel", "rar_sha256": "f7dd38a3fffa82057652d5a2bcda3faf99b29e3acab9bbe4c135a02cb582301c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_create_a_case_from_a_channel_agent.py` and embedded as the fenced Python below (sha256 f7dd38a3fffa8205…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_create_a_case_from_a_channel_agent.py` first:

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
    "version": '2.0.0',
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
