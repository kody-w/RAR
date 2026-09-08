---
name: "rar-cat-agent-skills-awaiting-reply"
description: "A weekday-morning Scout automation that finds emails you sent that asked for something and never got an answer, reports how many are waiting, and prepares follow-up drafts in each thread's own language that it never sends."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/awaiting_reply", "rar_sha256": "d02f3e9ab8faeaabb60ad68970f996c478687c29f591f9a0bce8459a68a6968e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Allan De Castro", "tags": ["email", "follow_up", "automation", "productivity", "inbox", "reminder", "multilingual"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `awaiting_reply_agent.py` and embedded as the fenced Python below (sha256 d02f3e9ab8faeaab…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `awaiting_reply_agent.py` first:

```bash
python3 awaiting_reply_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 awaiting_reply_agent.py   # or on stdin
python3 awaiting_reply_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
