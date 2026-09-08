---
name: "rar-cowork-cookbook-catch-up-on-messages-and-send-replies"
description: "Scans this week's Teams messages and emails for direct questions you haven't answered, auto-sends short acknowledgments, and drafts higher-stakes replies for your review before sending."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/catch_up_on_messages_and_send_replies", "rar_sha256": "7afb7ea1e7bd43db83ef6a98952d75fd97a18ba3b295594514f0c5c00e239924", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "work_management", "intermediate", "read_only"]}
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
