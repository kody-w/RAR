---
name: "rar-cowork-cookbook-turn-source-content-into-a-deck"
description: "Get a working deck built from content you already have - without starting from a blank slide."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/turn_source_content_into_a_deck", "rar_sha256": "6f38a192ebccdcf950fd407c4d8094a454d4396dec4727903a9170437e284a58", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "beginner", "integration", "prezi"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `turn_source_content_into_a_deck_agent.py` and embedded as the fenced Python below (sha256 6f38a192ebccdcf9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `turn_source_content_into_a_deck_agent.py` first:

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
    "version": '2.0.0',
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
