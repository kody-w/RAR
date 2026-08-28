---
name: "rar-cowork-cookbook-catch-up-on-messages-and-send-replies"
description: "Close the loop on unanswered questions without scrolling back through a week of threads."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/catch_up_on_messages_and_send_replies", "rar_sha256": "c66ade34996200f9019b892172be4fd546b3696f15d36f2af207f37a77fc16d0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "intermediate", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/catch_up_on_messages_and_send_replies`. The original RAPP
agent is preserved byte-for-byte in `catch_up_on_messages_and_send_replies_agent.py` and in the RCI capsule.

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

Catch up on messages and send replies automatically — Close the loop on unanswered questions without scrolling back through a week of threads.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/catch-up-on-messages-and-send-replies
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
      "description": "What to apply this capability to.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `catch_up_on_messages_and_send_replies_agent.py` and embedded as the fenced Python below (sha256 c66ade34996200f9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `catch_up_on_messages_and_send_replies_agent.py` first:

```bash
python3 catch_up_on_messages_and_send_replies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 catch_up_on_messages_and_send_replies_agent.py   # or on stdin
python3 catch_up_on_messages_and_send_replies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Catch up on messages and send replies automatically — Close the loop on unanswered questions without scrolling back through a week of threads.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/catch-up-on-messages-and-send-replies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/catch_up_on_messages_and_send_replies',
    "version": '2.0.1',
    "display_name": 'Catch up on messages and send replies automatically',
    "description": 'Close the loop on unanswered questions without scrolling back through a week of threads.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'work_management', 'intermediate', 'read_only'],
    "category": 'general',
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
        "upstream_slug": 'catch-up-on-messages-and-send-replies',
        "upstream_url": 'https://coworkcookbook.com/recipes/catch-up-on-messages-and-send-replies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4bef0a8e9c6a1bb7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['work-management'], 'process_tags': ['work-management/manage-communications/triage-and-respond-to-messages'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'work-management/catch-up-on-messages-and-send-replies', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'general', 'checks': ['The outcome is independently verifiable.', 'Assumptions are written down.', 'The result was checked against the original goal.'], 'confidence': 0.0, 'deliverable': 'A completed pass with the goal, the method, the result, and the assumptions it rests on.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'What to apply this capability to.'}, 'refined_by': 'rules', 'signals': [], 'steps': ['State the goal as an outcome someone else could verify without you.', 'List what you have and what is missing before starting.', 'Do the smallest version end to end, so unknowns surface while they are cheap.', 'Check the result against the goal as stated, not against what turned out to be convenient.', 'Record what would have to be true for this to be wrong.'], 'subject_label': 'task', 'verb': 'Run'}


class CatchUpOnMessagesAndSendReplies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CatchUpOnMessagesAndSendReplies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to apply this capability to.', 'type': 'string'}},
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
    print(CatchUpOnMessagesAndSendReplies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
