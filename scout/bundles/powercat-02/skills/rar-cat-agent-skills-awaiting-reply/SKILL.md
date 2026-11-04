---
name: "rar-cat-agent-skills-awaiting-reply"
description: "A weekday-morning Scout automation that finds emails you sent that asked for something and never got an answer, reports how many are waiting, and prepares follow-up drafts in each thread's own language that it never sends."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/awaiting_reply", "rar_sha256": "b7aa264d0020c3aa19ae1edc112ef65f8ddcd16dcc3ec5d78bd9775e3b957719", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Allan De Castro", "tags": ["email", "follow_up", "automation", "productivity", "inbox", "reminder", "multilingual"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abPiSJblX6FffcjIVsQTQkhCUVZmI9CKAAmBNjLKMrW4NrRvSOTkfx8Xj/cisyqzu8dsPg0RFqHl+vXr5y7nOs6vL07XRkX98vWFSVMnn7FgtnGati5ePr/4oPHquGzjIp/ez24AXH1n/JIVdR7n4ezkFV07gwqKzJmEZm3ktLMgzv1mBjInTpvZWHSzBuTt2yunuQJ/FhT1rCky0EaTEif3ZznoQT0LCyiRw7/NDdSfZzUoi7ptZlFxm2VOPs6cGsxuTtzCUZ8fw0ooAh82UGOaFrcvXTnzayeAY+J8BhwvgrPWwPF/aGbFLZ/B5YWdE4I3W+L2OS00z29e4XLB4GRlCpqXrz/98/NLDK9fvv764qVO00zLf06tgTIdofSkDT4uRwhfDu9LUMOFZfCRD4LZ8+5TA9Lg8+w///N6c+qw+fHrt3z2/Hx7mf5o3YQaNKmAoENsPKd03DiN2/F1xqQ3Z2wgDm1X583MmUG3QANe30Z+11SUs39M7z69TfIagvbTt5cCmvDwyreXH2cQ8W8vdTddv05ayk8/vkLEQP3px+96ms5NgNdOyqDVrz8/759qoeB30TiY/XxSuc1zrhp4cQmg8t+tb/q8mf5U94Tk5zfhT0X5efbnmqf1/APa+xZ+LtT752ohBnDky2tSxPmn5xx10YPcyT3w6ce/UutFwLumcdP+j/T+9KY4gmEE0XpC8uPnh/v+OUOea/vQ+dfTljBg/m9WAsXfp/sA6q90Pzz7L6rTOIeZ8e7LP1X3ZwOQf8x++su1/VcDPs+Cby8sSGOYU46bgq+zXx8h8tMP/veHP/zzN6j6v1VzKrrae2j4GWZ+HICm/fnnn35oHo9/+OdPP3QljGLgZD93dfpnOv8M18c8f0DwKfXpj2Ph/Hp+zaeK8ZFDs1+L8j/q315nhpPG/vfnzdfZ7zNx+iCzaRHvk75B8LtsbKCtv8Pxx5ffYKnJ4Wo67/Ea1o+//W22j726aIqgfdZY6OA2zsBk/DmKYX1rHlWjngpYE0Ngn3Iw/icPTxYXweyX/+U57RdY8fL2S3ON07RBnWcVg1kIy9gvr7MzVFPUcRjnTjrTGFX9lj8GTFPA+tqAuodlyR1b8AVm75fpYqquv/xR0c+PMa/l+MujMMdvRU3bSFNBa7oUvE6mmxHIn4Z6sNCDAXgdVJcWHpw7iGHpnap+U6T9VKOhAQ+jZ34MS0Zb1ONDN4Ti66Tsl19+cZ0m+pa/VWB89sZVDQoFPsyZffkCFxGkcRi133LgRcXsh19/+2H2v2f/1aiH8mkOFZb+J9DQwu1JOUASCrsMik0cAyu24z+A/vW3J5RQTQ45BbolDmLwNhgGHqS9d1xPIvNlQZAzF0A8IZbZxHITEcbt60wKZh/2fhCgAymwaWc+KCFTgdwbHwT2Lf9AMofE2cDoaoLx86xrwGPWX9zaeZiYwQx22l9m+40KaaZI4T+TmQ8hOLjIYwj/h9ffnkMlNWTN9buK19nhwZWQbp0yqp3nHIHz5hdIL+/DoXIHEuvtWz4RKJigesT9GzxQCCLjPV36ZfL5zCsymOR+8z73Q8aZyPD8IMX6W948Y3rqAOBAWOPhpGEX+1Ol//szpJqo6NJHUxBASydNTy/4T688YvCdxmcPHp996xZzbDn7/7u3eaxbEDROYM4cO+MOZ81+84dX5O20grcmEHYdjwU8cu97J/Jebd6L7rc8jWFw1ePf3yQfXnzKvBWyroZQaIz20A9DCFoy6X1E+BSxdT3lhvMtf6/ucM2zRymDQMNyMCEJA+l9wuntu6URzPnp/jvTPyKi9ifUYBTPys5NYYQFAPiu412fML07GoY7mDL2FsUPCL+vaga1w6iC+mfQiLh94PqA7lC8eTOoi+y7eDx1ZtAKv/OgtRGowevMnMCHwdbA7IZOm2QgCk8XTUFRQBM/EG4ip3wzpqiv7wY67zEHfu+B58vvqfGwZTIfanV8p4VY3qbC7IPhzbMfdj59BY3NpmR+DPqju59rnf2ehv7+LX/Y+MEFsEakE4P/DpwZzM2seUTrVOKmaM7AM4BgJDzI+vWNb98I/cOWr7MNc54xb/XwQUyzT9k75T3YUf+jV77OorYtm68o+iH2GsZt1LmvcYH+G8v97Z2dvjzY6Q8K39b+dfYv250/yDxD8esMe52/zqdXu9gDU6w9P19nXf5RXT797vrpqIcjgP/5mYbQiikqmwj4jwZEA989+V5iJoBHSLQfjPQuAmkprEE4Cb8xVDMR2w1y6UM3xPpb/uHtZy7Aip+HE502xe9y9EHN0HdvrvlgDvgqb+Hc/tSlhWDaCqXTchvw8jXv0vTzS+5k4E+2QBMbwPiDYE0bJZgLsMlpY/C4+2h4pps/biQfWQLT2y++TsnyeTY1p59nH33m59l75//YleUd3FT9NPW405RQFP73IfuxS3XBC9y0tWM5Gfq2UZpaq2fL++9GTDkCLfbAxPDFR9JNM/6bEngRhqD+dyXK48JJn5nftM5U1GH1fYZBA+30YffzeQZdBWMdpgaseB0c8O/TwHlqUHWQGP1pud/x+76s4m0tvz1gaN92m7++vFeApw+e/R8Uh6n2pZloDIVhDCeE928BBN/9d53hUxyWKNirQHmXcpwFufTn88Xcwx0Hox2AAd/DsAUISCJY+b7nY6TveTjwCJ9auT5NUQTAXZqgKIyG+t6i7ueJ7uPJhKnqTSkKAxd8fw0f+U/b32ydgPloRKc1Ppfw64tLLqGkuGwk5u2zQRHDoS6S2xIWfScDps3J45mNDqZONZZZGbQRn0RDJ1b+ac+1gRntTQY/bbbnnaq5+VEdLuVeDhFtuxrP1O5qkRxy2o8KoZdGY2yqrcswFo8GCS6qWrBxEbQG6LJCluoOWXKSqbippqmnYrEoKuNcnhmU3h2uQmfwySHSY2MhLJVohQcbvAuv3LlOyyGg7OxwsqILebRRRDzfzhR2id1V6V02FW5uqDax6zI+xfuTNO6j0zI7VhdqkdHXKk8Tzkvnx7SxMuxW2sfOWGg5F2iOXONKqd/vdtxysj0oUmweR85oLoG1wlCdzAkbWMsQ+EN2yS+ILFYIKkhmNsh22RxKfCSkxTCA+47AaOTQzotMO7qc1qaaWciOsMXlCvgIR+tEcV2adFZTeExHNuNyCKr6He/wRDsKZnG/m6aZX3hhf011tTeDY91owXDZOWdwpE+S3t9dXrhgeJhhXJ0weURlbc8brU+ebqea1+5aJmL5VeDmt1NAalmKAEunfBJJ9Wt8V5FgfwGtoRBXqj6SVqVV4/2yw8PmrrrxXYrR8/6Qlh6rExEXeD63WiVbFfbfTt94pd6bEXfgBT6T63qvL4Fh6nzotcfrnVLXJ3Q5IlI3H9MBm885O5ZjBOnxoiljqthJm3VAssc6XjBZmDD7EO0sl7XMcCE5nqYyQ5lu62NZlLQ3ipod77C9lgHMLGvOkMZ04XS5ruArHI3QobbtflFzMuw+RSsOu0KlGs7Yo04Ho05MY7IfKDSac8czs6Tv9jlF7mqPopiLSF6fSnjjj4GrL8C8jYwLV10dLLPr020Obp1iCelY+6WcG5EgHNug2wiiumm4691wo8vIcsxxE/aaSZi7QwfQczCXtYsoXXHPbcJNy2yJK8sTmMNhpGkfC+ClSxgxvnmJdwoBd0JLfj8ukvU4auHWFZ3yJJzIXXxlzbXvI8IisrI7ewPsarFY9ThOUGhPtQIqLlpk1aP34IpK6d4sWUSBlhK72m7QYs8T4p7gpZxm7oGsJrv72rU9tpUOrIThFNrckuFws4+j3BSef92smjy+Hg7HsNGj7epIlXJ/8JZYNIaiWvM2IxODdcQusna9lFfNWeuttjgYedmFojtXvf5Q62UqpLysxY46mhKrbhArtinuVKVL2dm77sgvPK5Ih2o4gvvJrZNMDRVtdaa2WlQx6WLYZwiJDWp6Ty9tux+ueZQd7tzleKQPYyk2QbU+S5TXLuRyuamcEDlQA8YUmRgdBfrSXRR7vg+uh2p0apk/tBW9l7gUT8F6SW31qI63yrBTtFBbhKC6ocqVMhA8SY/etS3GrCOpXs956YQRG9LG3aXXCOR+J8l0PmrjxvMWfCTwYw3M413VyOOCp1KXAJKYM2anha3JdYqstifpvgrqVX+O8tEAe9OU55jBdzV/NezVHbV8T2WPrtlgxQ1Ia/Q+Fowq7Bl3394Hgtx6xC3lzZV+XBdJmeB8RM/3l4AmkPUtwZFU0o2EUO8HrSzjxBgKRNjpyBUPbFQq5F3lOXQV3JqhMRIYLCdaX9Y3SWu6EuzUYKPVuaIrm0o+RS2Jja3jyrVX2jJhkkkuHG3AM9SC8VbjtSKN3N6MVDBedwOL5ruuEEop3x9iebO4+fZNTmU02l5365u51S5gHUsGue1ugq/sWG1d8Wxk08SabO4wcDex1qqEcYl8NbJlrSYRn+JaRbsLasrT57t5uPbXIBW35HI7qnpDmPfr9hbQfSYTe4qRrcSXDrhXVJExuCy/UhH7zMZaTOKan2rpynFoBl9jDt+HOjMXgb9r5iISbqRizSpkoCzOTB2ycWaxCkwlPLJrfYFs5wtSb+/LhIj39bLdyLS0YLg4RQ+ZSiC1qDf7xYawwLWu74vqGtp3cWRFk8lDP9Cd6HAzDYxQJHTFK0FsNw55VQcNW4l8zQvk2ke3LOiNC5VmfVSv6YOf1verKMmX3mXay4ZPlVyv3UGCFXf0pWBMhGWSzTfCZcQgzEc+Sg43sba0yy28CoSBm8ouME72PafQw+l8KYYDjkSOmdh34h4tvWMlo7UNI7MCbH1AN4nuSl3p7pzbyb1mJwPj1HON6ehlRYcnYueuQ00g1FMYOzujSxkgJdzgGoJwQaRBdf3rHg+5SEcVeYeiNb8jaHHV9Ki1o5Yo05drn7BWesDz58hg2M2CjqL+uEUwI1w3KxtXXIszt75Myn2aVIFE84ZYjXIhWVubSI90yAw7OezX952y65OeCfUzqXB64Fzzo6htdqFtlh0e8psxOTtAzL35br7I9CVsGHxeMJukzBOGEHbVnBVscHAT81LWPc5xVOmfd2Te3YfabNPTWKgEfXKSHOQGfrlu1VUd0tV8YJeVfDgvKccqBq1mDtHYY+F+z1aCTsfH7lBbp36I/OVpWVQ9qXEiel3TMa+Z8WHFBIPE671zkH116V7IpN3trxeUz27OsPDJwbQLXjhXKpM4g2z0DLfKytOVjIY9ESDz7el4qRhnniNiSBubsxxvFwIbFtXxdhOSZdvxt+vgrI+0hY6JgemUe71dcTUwwG7dnET3NgzHzepw7eK9pYmZWlMaK51J7rpBeWfvc5AFiibBmvh8Fcf9XBLSwQ/EBW1ZYRkG9xRdZ2UQX046t4Ubrbnj9Lm/DOmymh9JKa1lmdS94qSjp23MzTmMaFpbr/km6bDbjS+Og5bIoho5FLvH8oOBnVJubbcxdrxVdntPjLxt4a7USKLL+uYeq7GKLMbZOdvzqjNORdLzMeUey92C9RnXPYYx2Bz6g2t5mZTejnwiYuLi7vMBYyzIivBlkLHbjAGBPiwCSSMlfZQiezUGGGPm5bxs7X2XNTgjy+Faj0I5rLaOc46Ttuy0KlrEFgepczUCfr/FDroO7ZfNliWYpLEPslG2pcTnBQh6keDx0K6WJ1sYFiolXpQwVTNixOPlKIdqbHqNsTxHK36407GNVsd4f4sx9YKBTDYM5ITtmrzy5/HcynXcFLImR0ahLS7oVt5X5dVkxGPSZGLHdK3ZrhOpicSlLuHGbrA9wSO2rokzWNsF4zkOC1K8Kt11Th7stZ722z3K6ziVp1l0Fu/ooE3f/4eGZx3iRjtZ3I1HIn+9PrMVfZuayGG1mMOiuZ1fiW1anajsHrKhoBxAc6q07lYGdqKEfID37Ao2pr0v1AfccqQzp9JrPsWiwdlzoXUpQXEs770kM3wn4YdC8Ut9Q4BLIipyrhccPxicRiSslscisknmTrPa9ZxVEWxotsuNRW/Wup6q4qaNbG9+2AYXQrEDZisYB0E/pmMsowpsurTDqh7MEoS+dRm349YX0wtB2vutGy/nx8Lph2GNncgCadshvizPhyhpPFV1rDQhIzzcjHaqi+5F3RpBreD88lxdbxcL2bYXRrr2YNuVGFXEBEUye6KEmwKFz23YRPiivmJxQkovOqnU5G65BpGZFsv7PL2MwzEJxLbTioLY9x6uJPOwMhcCt7QViylPkrpduUuqOBjFNoyE0cssoyEpk0eKI8fvHW99lTjMmnvWMOVeytb3cLulVwMTx6aVC+ee2es5Fu7onquEpMlxfQk3BcZus+QlusB3rZP1Rpbz+SErqvqEBM7GqTWHjM9I6ZBysVrqPp9Y/VwGmkIL8eBGVu5nHPDr44WFDQ1BtQrtUA6W1qeS7T1y7rp1wGM+zgKLzktdbHbmQqV9e6A3TZopGOQGneCvZVHdkOVuW3j3JZdcj53gVLtGiNapamLd2Riu8TIQ7fsm2mxXWrkyV4e7dtCY814sr/WO8vw1MKyzeEwhY81DVN/461FEdF5mkRCc1FqXxUNeoEV8CI6N6xGtY1JJfz+4MjLa4Wl+CxLvoOi73iZvbg0UpuxEmmpTbtuf2KVB1ZJLmjeaqvPF3aNaDixSr+bYDGEuIGa0Qgjim516Mu1u8xN+DOZ6MN+63E2nk3xZw4wIGW7pKoCLymIVetd7x9rb4aRSe61TlX2NjfLCE3ehc0zzvNJCQEcD1izi8HIjxc7iqXuay/uahHVi5FOj4dFilQDlSAEG2RHq0ZDSinFR3jriuGcYUmOnIMA34gD8ljbjbX9hR69NHM7DVcXotsugoaieXd/4DeLc+zotFlVrFb2rFcAoAmJhkhFaizjY68JlfrmfNpfTRqb24plaHgYcv3RB0+4j6Np6mA/QIhJuW/JLh9UUYhGFIfr9vuCtlgx97YY3eAPaVa82OsYwAeXUlyXvofzdc+dytEvY2I+2cbVSTU9becKOWB/5gpWWLKMHWcMOtLgsKPvagroklnjoljcxgo3dPtg0Q8qYeNzQztrTZOSYO6Yimt4RYVZ6vTZvR3PYnNAK01CZWNFBzyTsXFyESs3qZ2G7zqld5fI3oIlrLtvjDMeJ7Dm+2IvDAeb4ysBqxNd5AyPRvaqiKxK2XMWu2AbqLhNaYFLOnbN8QsA9WpP3Z++e7VH3aKSBMxC3/DxsgGgQ0Y5u8zUikOS6vlK90mWC263ZOBEIikMHWli5gmqqmBhEc7s9uB1TgsOIYMj6AhHtmu4Iu+Ir3y+cqIxAw9eAXFb4Nsk6Z6yzlo8q0cS0Mzu39Hyu9GtpwQPGWN9OAIUdvaF5iy3HKEaCbEAyx7j2Andy6lYqIvJCEtiy3Jv0QqFvkRixzt2Z39icvNVqI7uG3Ts0aql13IFUz0AvRnm06iizAXOlBfQdRkN9Q4m2OTnXCkfZ5gwSNHXLwEvGigxCGlmW/b7ZoD1A62hNLtKWuGxgf9zatypmdORgeIvaCFbKahHp4mkrnH3fSXEzXNaHhMZPZ6SSFbC71A3D3W8ydVb3VYtuj7F1F47VNTISZZCu50Im0YVszrGNvktVGF2UwbnDfeXteklYD4e+KUXsfizFTgRFtFECK7wc4A4a2cjB2UMue+m4mnuk4Vwo/L5MFzy2O5dUxAFPFmkw+Ha6igOjLPx92zZ2wl7C7Nzqfpb69n2HYjTO94NEK5yCMjw1Jok6nDbClYg2i265R8gNotpgiBRLvqObOZ1e0CNKaxEdJ44fV+hYXVdA6KmOVS/a6gLYlEewbX6EMJxuSVHj7QK3V+31rhh0Kl6SWikxtFyTJX7cYBWMsCUVywhzI+dDFa2GZSAMCdzlhaYQ3s/UPF42eYQUiXve1N2qg1lqytDn9YXYnGnXEoNdLx7OBAuKhTsUCXpgWBNTBZNfCg0vBjkegqXcgOg8LuvNHk/zkedXCsSoMG8uCO6KWgfFMlFikXDspmJMgN+k8rzQATggBdmfBJcyFiu1Uw1OX6K0lGEWfhr9PVGcsFjV1oS+VpR1f7Q1hzcvmqlaFGIEDGu57OlMs8UazP2Sv6nmICkwKMApXxw1UTeJdUkOwT30qz7ED8RSLlTxgBoL9XRV3VVqbVF7m+SYFa8X9LC17FSR9gIFNixvsNaNpqsGX57QrnMNIuVsL0jl+0LVUmKkdyc0d9fbIC2jFjlvXVtiz8dsfyPJujzlQzsOgNs6ueeE2+G4PzUtu97s2HXl748y2vJUac/3nRHdFkykEHuIvux6wWHtKaMgGPM7ArfTPnt27sM9660zFcdhPko+deoEpKBg98FiVw1DzGtAN+raWMkXwvPLeQ4WeGWjy3pcF7LmaD1vjXPjjgSBldykQuoYthvZGFnquRcwZYg0ZhJkiIVXZ108mBbW7ZSLisBqDNB0mSkZEkjNSFmOBe54xx4IgQXUYUQ70UG3XnyrIxbdR4GZFzTs1px7PuDHZsNIVQ6oCLaDm71BNOWBIiksREw96nUq5LHO2DByGHTBGZR9qMSbTUkV202k3AvKE88LqlrkiVXYxl7c+6J8QfqCxzaLSo5D0rMIbX9t0oWfwHo/2I1CrBdopsxjC3rWx8e7NMI+6UCsLvRI7c7LaoVrGtDZ06hRPclfBZaw9uXIeijHbX0N7jrtTSdqtcKinVPSVhDciJWQMqS3NnP8nrAWrkn5aWniWb5a0LxG3yxckW+3QnOpMbNyoK5RVh41R7UXDMP84+Xzy3QA8zxG+YufTkzfgf8/+7r97Vvz9yPSx/kJcPyvj7m+/pUB//z8UnsxnP7tvKBJu/D5Vfy/nhZ8+eMB2yQ8vv3UYDqmHdr3g6PWCaef0708TswnFB6H2T93Jbz+frb+8rDVn44e+7idtMW5WwzTGQTIpqO0Gl5mXdrGaTwdc6eTpc8zOmgg/jp/Xbz89n8AWYrDBMsoAAA= -->
