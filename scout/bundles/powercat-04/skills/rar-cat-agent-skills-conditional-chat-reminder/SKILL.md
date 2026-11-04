---
name: "rar-cat-agent-skills-conditional-chat-reminder"
description: "Schedule a Teams reminder that sends only when the expected person has not already posted a relevant update."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/conditional_chat_reminder", "rar_sha256": "903949cd5aff8c68b6177aff8e377b4e321f90c6d9e30f3fb6db7e177293e57c", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Giorgio Ughini", "tags": ["automation", "teams", "reminders", "follow_up", "productivity"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `conditional_chat_reminder_agent.py` and embedded as the fenced Python below (sha256 903949cd5aff8c68…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `conditional_chat_reminder_agent.py` first:

```bash
python3 conditional_chat_reminder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 conditional_chat_reminder_agent.py   # or on stdin
python3 conditional_chat_reminder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/conditional_chat_reminder_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/conditional_chat_reminder_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/conditional_chat_reminder/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
