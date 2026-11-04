---
name: "rar-cat-agent-skills-conditional-chat-reminder"
description: "Schedule a Teams reminder that sends only when the expected person has not already posted a relevant update."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/conditional_chat_reminder", "rar_sha256": "903949cd5aff8c68b6177aff8e377b4e321f90c6d9e30f3fb6db7e177293e57c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Giorgio Ughini", "tags": ["automation", "teams", "reminders", "follow_up", "productivity"]}
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
