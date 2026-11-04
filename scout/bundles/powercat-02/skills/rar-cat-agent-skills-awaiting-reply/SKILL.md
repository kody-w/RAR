---
name: "rar-cat-agent-skills-awaiting-reply"
description: "A weekday-morning Scout automation that finds emails you sent that asked for something and never got an answer, reports how many are waiting, and prepares follow-up drafts in each thread's own language that it never sends."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/awaiting_reply", "rar_sha256": "b7aa264d0020c3aa19ae1edc112ef65f8ddcd16dcc3ec5d78bd9775e3b957719", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Allan De Castro", "tags": ["email", "follow_up", "automation", "productivity", "inbox", "reminder", "multilingual"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/awaiting_reply`. The original RAPP
agent is preserved byte-for-byte in `awaiting_reply_agent.py` and in the RCI capsule.

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

Awaiting Reply — A weekday-morning Scout automation that finds emails you sent that asked for something and never got an answer, reports how many are waiting, and prepares follow-up drafts in each thread's own language that it never sends.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#awaiting-reply
  Upstream author: Allan De Castro
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `awaiting_reply_agent.py` and embedded as the fenced Python below (sha256 b7aa264d0020c3aa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `awaiting_reply_agent.py` first:

```bash
python3 awaiting_reply_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 awaiting_reply_agent.py   # or on stdin
python3 awaiting_reply_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/awaiting_reply_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/awaiting_reply_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/awaiting_reply/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Awaiting Reply — A weekday-morning Scout automation that finds emails you sent that asked for something and never got an answer, reports how many are waiting, and prepares follow-up drafts in each thread's own language that it never sends.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#awaiting-reply
  Upstream author: Allan De Castro
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/awaiting_reply',
    "version": '3.0.2',
    "display_name": 'Awaiting Reply',
    "description": "A weekday-morning Scout automation that finds emails you sent that asked for something and never got an answer, reports how many are waiting, and prepares follow-up drafts in each thread's own language that it never sends.",
    "author": 'Allan De Castro',
    "tags": ['email', 'follow_up', 'automation', 'productivity', 'inbox', 'reminder', 'multilingual'],
    "category": 'productivity',
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
        "upstream_slug": 'awaiting-reply',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#awaiting-reply',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'd269450ca78b236a',
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.636, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'kind:automation'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AwaitingReply(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AwaitingReply'
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
    print(AwaitingReply().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
