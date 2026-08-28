---
name: "rar-cowork-cookbook-turn-source-content-into-a-deck"
description: "Get a working deck built from content you already have - without starting from a blank slide."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/turn_source_content_into_a_deck", "rar_sha256": "11a8df4e0e6a58f4ac0622497eb295b52d7349137930c6e7dc8a29790b65bba5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "beginner", "integration", "prezi"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/turn_source_content_into_a_deck`. The original RAPP
agent is preserved byte-for-byte in `turn_source_content_into_a_deck_agent.py` and in the RCI capsule.

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

Turn source content into a deck — Get a working deck built from content you already have - without starting from a blank slide.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/turn-source-content-into-a-deck
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `turn_source_content_into_a_deck_agent.py` and embedded as the fenced Python below (sha256 11a8df4e0e6a58f4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `turn_source_content_into_a_deck_agent.py` first:

```bash
python3 turn_source_content_into_a_deck_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 turn_source_content_into_a_deck_agent.py   # or on stdin
python3 turn_source_content_into_a_deck_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Turn source content into a deck — Get a working deck built from content you already have - without starting from a blank slide.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/turn-source-content-into-a-deck
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/turn_source_content_into_a_deck',
    "version": '2.0.1',
    "display_name": 'Turn source content into a deck',
    "description": 'Get a working deck built from content you already have - without starting from a blank slide.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'work_management', 'beginner', 'integration', 'prezi'],
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
        "upstream_slug": 'turn-source-content-into-a-deck',
        "upstream_url": 'https://coworkcookbook.com/recipes/turn-source-content-into-a-deck',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3968b18a5f8a924e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'prezi', 'process_roots': ['work-management'], 'process_tags': ['work-management/create-and-repurpose-content/build-presentations-from-source-material'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/turn-source-content-into-a-deck', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Meetings'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TurnSourceContentIntoADeck(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TurnSourceContentIntoADeck'
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
    print(TurnSourceContentIntoADeck().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
