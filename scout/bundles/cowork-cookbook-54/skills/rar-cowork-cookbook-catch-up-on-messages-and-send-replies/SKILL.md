---
name: "rar-cowork-cookbook-catch-up-on-messages-and-send-replies"
description: "Scans this week's Teams messages and emails for direct questions you haven't answered, auto-sends short acknowledgments, and drafts higher-stakes replies for your review before sending."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/catch_up_on_messages_and_send_replies", "rar_sha256": "7afb7ea1e7bd43db83ef6a98952d75fd97a18ba3b295594514f0c5c00e239924", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "intermediate", "read_only"]}
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

Catch up on messages and send replies automatically — Scans this week's Teams messages and emails for direct questions you haven't answered, auto-sends short acknowledgments, and drafts higher-stakes replies for your review before sending.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "time_range": {
      "description": "The period of messages to review; defaults to this week.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `catch_up_on_messages_and_send_replies_agent.py` and embedded as the fenced Python below (sha256 7afb7ea1e7bd43db…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `catch_up_on_messages_and_send_replies_agent.py` first:

```bash
python3 catch_up_on_messages_and_send_replies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 catch_up_on_messages_and_send_replies_agent.py   # or on stdin
python3 catch_up_on_messages_and_send_replies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Catch up on messages and send replies automatically — Scans this week's Teams messages and emails for direct questions you haven't answered, auto-sends short acknowledgments, and drafts higher-stakes replies for your review before sending.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

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
    "version": '3.0.3',
    "display_name": 'Catch up on messages and send replies automatically',
    "description": "Scans this week's Teams messages and emails for direct questions you haven't answered, auto-sends short acknowledgments, and drafts higher-stakes replies for your review before sending.",
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
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '980c21c35db85f61',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Output matches: Routine acknowledgments handled automatically, higher-stakes replies drafted for review - so you stay responsive without spending hours catching up.'], 'confidence': 1.0, 'deliverable': 'Routine acknowledgments handled automatically, higher-stakes replies drafted for review - so you stay responsive without spending hours catching up.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'time_range': 'The period of messages to review; defaults to this week.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Close the loop on unanswered questions without scrolling back through a week of threads. Routine acknowledgments handled automatically, higher-stakes replies drafted for review - so you stay responsive without spending hours catching up.', 'expected_output': 'Routine acknowledgments handled automatically, higher-stakes replies drafted for review - so you stay responsive without spending hours catching up.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork'], 'prompt': 'Go through my Teams messages and emails from this week where someone asked me a direct question and I haven\'t responded.\n\nFor anything that just needs a quick acknowledgment or "got it," send the reply. For anything that needs a real answer, draft it and show me first.', 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Routine acknowledgments handled automatically, higher-stakes replies drafted for review - so you stay responsive without spending hours catching up.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Scans this week's Teams messages and emails for direct questions you haven't answered, auto-sends short acknowledgments, and drafts higher-stakes replies for your review before sending.", 'example_request': 'Catch me up on Teams and email from this week — reply to the easy ones and draft the rest for me.', 'inputs': [{'description': 'The period of messages to review; defaults to this week.', 'name': 'time_range'}], 'model': 'claude-opus-5', 'when_to_use': "Call when you're behind on Teams and email and want unanswered direct questions closed out, with routine replies sent and substantive ones drafted first."}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


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
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'time_range': {'description': 'The period of messages to review; defaults to this week.', 'type': 'string'}},
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
