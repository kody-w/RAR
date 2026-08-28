---
name: "rar-cowork-cookbook-catch-up-on-messages-and-send-replies"
description: "Close the loop on unanswered questions without scrolling back through a week of threads."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/catch_up_on_messages_and_send_replies", "rar_sha256": "df2584d346a31b87577d83441d08eddf9a328147a8cf058be03a89b5332a91f6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "intermediate", "read_only"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `catch_up_on_messages_and_send_replies_agent.py` and embedded as the fenced Python below (sha256 df2584d346a31b87…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `catch_up_on_messages_and_send_replies_agent.py` first:

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
    "version": '2.0.0',
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
