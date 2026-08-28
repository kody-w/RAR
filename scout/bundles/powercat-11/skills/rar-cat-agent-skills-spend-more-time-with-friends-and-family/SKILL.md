---
name: "rar-cat-agent-skills-spend-more-time-with-friends-and-family"
description: "While you're out of office, watches a group chat and answers questions from your local knowledge docs (clearly marked AI-generated), logs anything it can't answer for later, and pings you on Teams if its setup is incomplete."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/spend_more_time_with_friends_and_family", "rar_sha256": "d11659b95fb22912398412b573f58ec52b940dcff10574f772ed0a4b4be892db", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Adi Leibowitz", "tags": ["automation", "teams", "out_of_office", "knowledge"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/spend_more_time_with_friends_and_family`. The original RAPP
agent is preserved byte-for-byte in `spend_more_time_with_friends_and_family_agent.py` and in the RCI capsule.

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

Spend More Time With Friends & Family — While you're out of office, watches a group chat and answers questions from your local knowledge docs (clearly marked AI-generated), logs anything it can't answer for later, and pings you on Teams if its setup is incomplete.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#spend-more-time-with-friends-and-family
  Upstream author: Adi Leibowitz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `spend_more_time_with_friends_and_family_agent.py` and embedded as the fenced Python below (sha256 d11659b95fb22912…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `spend_more_time_with_friends_and_family_agent.py` first:

```bash
python3 spend_more_time_with_friends_and_family_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 spend_more_time_with_friends_and_family_agent.py   # or on stdin
python3 spend_more_time_with_friends_and_family_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Spend More Time With Friends & Family — While you're out of office, watches a group chat and answers questions from your local knowledge docs (clearly marked AI-generated), logs anything it can't answer for later, and pings you on Teams if its setup is incomplete.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#spend-more-time-with-friends-and-family
  Upstream author: Adi Leibowitz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/spend_more_time_with_friends_and_family',
    "version": '2.0.0',
    "display_name": 'Spend More Time With Friends & Family',
    "description": "While you're out of office, watches a group chat and answers questions from your local knowledge docs (clearly marked AI-generated), logs anything it can't answer for later, and pings you on Teams if its setup is incomplete.",
    "author": 'Adi Leibowitz',
    "tags": ['automation', 'teams', 'out_of_office', 'knowledge'],
    "category": 'integrations',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'spend-more-time-with-friends-and-family',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#spend-more-time-with-friends-and-family',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'bd12abb4ba09a5e5',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Scout'],
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'kind:automation'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class SpendMoreTimeWithFriendsAndFamily(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'SpendMoreTimeWithFriendsAndFamily'
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
    print(SpendMoreTimeWithFriendsAndFamily().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
