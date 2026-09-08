---
name: "rar-cat-agent-skills-conditional-chat-reminder"
description: "Schedule a Teams reminder that sends only when the expected person has not already posted a relevant update."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/conditional_chat_reminder", "rar_sha256": "1452500a768e389d1c97a53057224a79ac96991e2267344caed384994b7a8c46", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Giorgio Ughini", "tags": ["automation", "teams", "reminders", "follow_up", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/conditional_chat_reminder`. The original RAPP
agent is preserved byte-for-byte in `conditional_chat_reminder_agent.py` and in the RCI capsule.

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

Conditional Chat Reminder — Schedule a Teams reminder that sends only when the expected person has not already posted a relevant update.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#conditional-chat-reminder
  Upstream author: Giorgio Ughini
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `conditional_chat_reminder_agent.py` and embedded as the fenced Python below (sha256 1452500a768e389d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `conditional_chat_reminder_agent.py` first:

```bash
python3 conditional_chat_reminder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 conditional_chat_reminder_agent.py   # or on stdin
python3 conditional_chat_reminder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conditional Chat Reminder — Schedule a Teams reminder that sends only when the expected person has not already posted a relevant update.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#conditional-chat-reminder
  Upstream author: Giorgio Ughini
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/conditional_chat_reminder',
    "version": '3.0.2',
    "display_name": 'Conditional Chat Reminder',
    "description": 'Schedule a Teams reminder that sends only when the expected person has not already posted a relevant update.',
    "author": 'Giorgio Ughini',
    "tags": ['automation', 'teams', 'reminders', 'follow_up', 'productivity'],
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
        "upstream_slug": 'conditional-chat-reminder',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#conditional-chat-reminder',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'a519bd3119d92722',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'word:schedule'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConditionalChatReminder(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConditionalChatReminder'
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
    print(ConditionalChatReminder().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
