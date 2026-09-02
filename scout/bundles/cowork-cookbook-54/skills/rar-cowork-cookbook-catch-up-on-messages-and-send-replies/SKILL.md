---
name: "rar-cowork-cookbook-catch-up-on-messages-and-send-replies"
description: "Close the loop on unanswered questions without scrolling back through a week of threads."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/catch_up_on_messages_and_send_replies", "rar_sha256": "df2584d346a31b87577d83441d08eddf9a328147a8cf058be03a89b5332a91f6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "catch_up_on_messages_and_send_replies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/catch-up-on-messages-and-send-replies:8bfadf54095469fb0683743ed6676154fe33e37e78ebeb62572c49d52a06c2f3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "intermediate", "read_only"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/catch_up_on_messages_and_send_replies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `catch_up_on_messages_and_send_replies_agent.py` is
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
