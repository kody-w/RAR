---
name: "rar-cowork-cookbook-turn-source-content-into-a-deck"
description: "Get a working deck built from content you already have - without starting from a blank slide."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/turn_source_content_into_a_deck", "rar_sha256": "6f38a192ebccdcf950fd407c4d8094a454d4396dec4727903a9170437e284a58", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "turn_source_content_into_a_deck_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/turn-source-content-into-a-deck:09af5dfa797adff52686cba9b359ee861f5c940c73f4436fe6f0ba33f310570c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "beginner", "integration", "prezi"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/turn_source_content_into_a_deck`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `turn_source_content_into_a_deck_agent.py` is
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
