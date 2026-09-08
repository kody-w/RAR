---
name: "rar-cat-agent-skills-awaiting-reply"
description: "A weekday-morning Scout automation that finds emails you sent that asked for something and never got an answer, reports how many are waiting, and prepares follow-up drafts in each thread's own language that it never sends."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/awaiting_reply", "rar_sha256": "d02f3e9ab8faeaabb60ad68970f996c478687c29f591f9a0bce8459a68a6968e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Allan De Castro", "tags": ["email", "follow_up", "automation", "productivity", "inbox", "reminder", "multilingual"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abOjRrbtX9E9/cHlS9WRGAXV0REPEBJCIARCTK4Om3kQ8ySQn//7S3R0Ttnd9r33RbxPT64oM+zcuXMPa+0k69cXp+/isnn5+kJnmVMsNsGCddquKV8+v/hB6zVJ1SVlMb9f3ILg6jvTl7xsiqSIFmev7LsFUFDmziy06GKnW4RJ4beLIHeSrF1MZb9og6J7e+W018BfhGWzaMs86OJZiVP4iyIYgmYRlUCiAH/aW9B8XjRBVTZdu4jL2yJ3imnhNMHi5iQdGPX5MawCIuBhCzRmWXn70lcLv3FCMCYpFoHjxWDWJnD8H9pFeSsWYHlR70TBmy1J95wWmOe3r2C5wejkVRa0L19/+ufnlwRcv3z99cXLnLadl/+cWg2qbALSszbwuJqA+wpwXwUNWFgOHvlBuHjefWqDLPy8+M//vN6cJmp//PqtWDx/317m/9R+9howqQROB77xnMpxkyzpptcFnd2cqQV+6PqmaBfOAoQFGPD6NvK7prJa/GN+9+ltktco6D59eymBCY+ofHv5cQE8/u2l6efr11lL9enHV+CxoPn043c9be+mgdfNyoDVrz8/759qgeB30SRc/Hw+cexzribwkioAyn+3vvn3ZvpT3dMlP78Jfyqrz4s/1zyv5x/A3rf0c4HeP1cLfABGvrymZVJ8es7RlENQOIUXfPrxr9R6ceBds6Tt/kd6f3pTHIM0At56uuTHz4/w/XMBPdf2ofOvp61AwvzfrASIv0/34ai/0v2I7L+ozpICVMZ7LP9U3Z8NgP6x+Okv1/ZfDfi8CL+9bIIsATXluFnwdfHrI0V++sH//vCHf/4GVP+3as5l33gPDT+Dyk/CoO1+/vmnH9rH4x/++dMPfQWyOHDyn/sm+zOdf+bXxzx/8OBT6tMfx4L5L8W1mBHjo4YWv5bVfzS/vS50J0v878/br4vfV+L8gxbzIt4nfXPB76qxBbb+zo8/vvwGoKYAq+m9x2uAH3/720JKvKZsy7B7YiwIcJfkwWy8FicA39oHajQzgLUJcOxTDuT/HOHZ4jJc/PK/PKf7AhCv6L601yTL2qXzRDFQhQDGfnldaEBN2SRRUjjZQqVPp2/FY8A8BcDXNmgGAEvu1AVfQPV+mS9mdP3lj4p+fox5raZfHsCcvIGayu5nQGv7LHidTTfioHga6gGgD8bA64G6rPTA3GECoHdG/bbMhhmjgQEPoxd+AiCjK5vpoRu44uus7JdffnGdNv5WvCEwunjjqnYJBD7MWXz5AhYRZkkUd9+KwIvLxQ+//vbD4n8v/qtRD+XzHCcA/U9HAwuFs3wEJBT1ORCbOQYgtuM/HP3rb09XAjUF4BQQliRMgrfBIPEA7b379czTXxCcWLgB8CfwZT6z3EyESfe62IeLD3s/CNABFNh2Cz+oAFMFhTc9COxb8eHJAhBnC7KrDafPi74NHrP+4jbOw8QcVLDT/bKQ2BOgmTIDf81mPoTA4LJIgPs/ov72HChpAGsy7ypeF8cHVwK6daq4cZ5zhM5bXAC9vA8Hyh1ArLdvxUygweyqR96/uQcIAc94z5B+mWO+8MocFLnfvs/9kHFmMtQepNh8K9pnTs8dABgIMB5MGvWJPyP9358p1cZlnz2aghBYOmt6RsF/RuWRg+80vnjw+OJbj6xgbPH/d2/zWPdup3I7WuM2C+6oqdZbPLyy6OYVvDWBoOt4LOBRe987kXe0eQfdb0WWgORqpr+/ST6i+JR5A7K+Aa5QafWhH6QQsGTW+8jwOWObZq4N51vxju5gzYsHlAFHAziYPQkS6X3C+e27pTGo+fn+O9M/MqLxZ6+BLF5UvZuBDAuDwHcd7/p003ugQboHc8Xe4uThwu+rWgDtIKuA/gUwIukefn247li+RTNsyvy7eDJ3ZsAKv/eAtXHQBK8LY3Y+SLYWVDcI2iwDvPAM0ZwUJTDxw8Nt7FRvxpTN9d1A5z3ngt9H4Pnye2k8bJnNB1od3+mAL28zMPvB+BbZDzufsQLG5nMxPwb9MdzPtS5+T0N//1Y8bPzgAoAR2czgv3POAtRm3j6ydYa4OZvz4JlAIBMeZP36xrdvhP5hy9cFS2sL+g0PH8S0+JS/U96DHS9/jMrXRdx1Vft1ufwQe42SLu7d16Rc/hvL/e2dnb482OkPCt/W/nXxL9udP8g8U/HrAn5dva7mV2LiBXOuPX9fF33xgS6ffnf9DNQjEIH/+VmGwIo5K9s48B8NiBp8j+Q7xMwOngDRfjDSuwigpagJoln4jaHamdhugEsfuoGvvxUf0X7WAkD8IprptC1/V6MPagaxewvNB3OAV0UH5vbnLi0K5q1QNi+3DV6+Fn2WfX4pnDz4ky3QzAYg/4Cz5o0SqAXQ5HRJ8Lj7aHjmmz9uJB9VAsrbL7/OxfJ5MTennxcffebnxXvn/9iVFT3YVP0097jzlEAU/O9D9mOX6gYvYNPWTdVs6NtGaW6tni3vvxsx1wiw2Atmhi8/im6e8d+UgIsoCpp/VyI/LpzsWflt58ygDtD3mQYtsNMH3c/nBQgVyHVQGgDxejDg36cB8zRB3QNi9Oflfvff92WVb2v57eGG7m23+evLOwI8Y/Ds/4A4KLUv7UxjS5DGYEJw/5ZA4N1/1xk+xQFEgV5l3tOukBANKMclQydwHNclVo5PkNR6FVIU4WFrkiDXHkKFOAWHlLNyvYDEcMohSIegCDIA+t6y7ueZ7pPZhBn15hIFifu71+CR/7T9zdbZMR+N6LzG5xJ+fXEJDEjyWLun337skoIdAlunXWxCa8KPMhVCDIzKW6TQ4K7tpC4TW451xdxBRasWMH9/djUpTbCyTH3P2ggsTzAn5BzWvgJVdWA4k2Kx19uZac6QFmNuRuL3/hpNtGUGUyYWZ4Kzvfp8WycDtVyq8LQfdNFstclbX6Zg1XTo9XwV997ArnfnWDvXh+Z854w6GLdGWfiGuL3ZGls36q0hzpTebK0cHq0WPm2zUtsfGafqsx2OMIl0Pm0LaqrDRB8zIYFaRKgpRCpW+925j7d+M3bStJG2GxbLBGuwC/vsJuYBG1XCZycjEXVTyrA1p9sVdFAPjnvJictqdTHDLC+3VHc7ig1G1IOow5Q/8Ev40twJaECzYSWOYd1x9vHAUhJo2CfXHC1ej6HKUDcH7YCjioTeGklMJXfPbX3iyDXoweZxAo+M3q935Z6pVPUSOLcbZG4Fqzfl8uIIW8sszVhTeDZwkFFMG2YYdAe58djWF/UrLqmcLZksLA0qsmpOjau6ULXO8KuTSeXqsmFy+8Q6YhqypMleCC7vM6wypKZBtoi0q8725eas+dBJbb8dSWYKc8am27Kke0RY3ZHO5CBT9nP4dt9p/c5CJTVjNgh6yIIYYgOgm9IOsHVo6v2IiDi62RtscglgK4AN+4ppVxi6O83hIHUGIjeofWCi0x2RC2Z3PXrawYjVe2eFlxVwlCcgAzXwciTs9ivfWFd9Fw6cKPs9wiAQcuf6ZAtZOxMJK3G/Ve+uwSmXQ0fZmxbmKsq79OmQYTcjOCKX4KDHx4QPyVa3r2KGewPjmeKp8LsLoRxx2U8LIb27tWUN97BHCStBYNXmbSjMiBObBgQiOM1FGO5nxi4a2bBtvSiKVRIeDQ8XzKNbdANibsdIJDKs9hQx0YL85J15VB/JXYoJBbQ5muj5ejjcyRA9qlWcpPBYQrmoQFc0tJZsHUC6toFiFfLrISGMeFWrTaGfGVZPkT184a3D0bctD2r2lx5HArVWMNkcNq1rRwFXF4ezFTDq2qBD8sgZrLNsN4I94OctHi/vGUpzaJVktxESdCPfVAZ38pgcO0T7Q4q74uEm6+cTE6B7qhotEB0lCaxkYk0jcKRQWd+ZzQk9VZd17IapiOHexcySycYsaMkH40bLpDHFnfBCwqkt4rutPQU966XwQdZbnPX45XE1mkLhMNPKreIcz7KL0ItbPEzNnMfwq9VThmlf7HCXD8rx5huxizH0kUELZy0xy5JODrRy74t7c70dMBqrQGDNMM4wYwdLYcIc+0z0IIi87baQGevO1VVY5Tzk9xCHmvWqPCLTqAfXUy3mdWF30UBGIxwJGG/CLKAi6ArbO3FJ0qfl5Uw2DgdtT0vEN2jbwVSINKiJXLmZ4RCqpMOSDxdTykt7e3BZv2K3mVxcGncU9MN480v3lhJYnF9l3j7gh8JTuHiznYZbTGUFyypmbh49vPNVMYXCntTFU16o/RI+qTUqQR4Z8vQhGQhkc7110k3bDfnmIkpd1Yj2KnGzOFFhztRvhBS0kHdNcdGlo3iHn85R7Ih2mynOnrlZbY16FqSXedcjOzdi1fqUVji6JNcBFKgnEQ3hiFoG451QzEAPt/yoXjBdoW9+4eyPo3JO6Ibe1hTslv39IPCG7hXDubqE9T5JFCGq6czPtP6yQfYs1+ZNb8XbZUAeNurpiqnxWJ2pvc/tc9q8neRR7eizkO2MiTxdjSXH4qeKkTZwk8Sp6yk4n7K4zIflTrqRxJJrXZeE2fMqbs67K4mLlg6ryK5zkEssEmeRS+CdNEDpSgsqkV/rWbaL96ZrwhN8spN0t/fZ7alXa0m1WwrnGMkxIbCbOi9XacyYIZef5BPDE1f52l5Fchsm2kFgJ5iwJQz28bQT5Wt13+a3AoAdMhrlkF1qz2EMPNHdw07AGbPFK06z+5FiyCNrXLk64SlvOU15GTFHlXNTfbpsacva+CTC79bGvmBLKKO8fBnfupQqztPaJ49jJ6+UDdZKaJwmUXazBV9yepaXQhSJOKVYbcsjJEwqIQiIquJ8pXODcOJA2Xf8HaU6Q6xJ+rgZ3RMmwQdSk7UoFlYwlGp6uxw4vpOMiVc4yleG7enA6SKSYPGRORqWiBwPo7vHu1ZSnRV3sabxju26cTqqmNl5laoYe8sP5IPBBJYeRue9eQArhxuGPjdXmNGbC9tz92qw9SZTN6GoT0h81rqjT7uuEiUB2w1Hnj2ryd7jjlaJ6Opt7690Ury4TpOvBMKRDI/ernLW3KuQcEno1GqREKaDa3XpBqvNry261w60aMQ0m9SVYmlJ01eBXse72uSY0OPY1VDI2TWJqgM3CZlrRV6kwlLf2ZcdmbEaKZ5Oy9bbILLO8XK6tnlfvMa3aZhI1Rw95nhexxsJ2UH7GyJj9o46DfpO2ZWmE6FKf2+TemldMsOFD7YsDHsjP3X2ESqOoXLfXS74URVbZZfyI33yKtPqEp4b8XqllHpboclkXam7Whz7UdTDsK6TaK3xV7kvLuzWVm/JgJv+7jbcuSbbF8MwTXS+jc2bP3kGe9/il4k2p+2KE47yGmXIkTrzqat6/CU+p+XOqADm9xxCWySyVuXScQ8FlfA2HRdmKpL95a4fq3Vlb2ymqQUyqYO1GmVsuhczg4foEd8lJu0aiqxdAtfpuemKbuVWlwXscGAJOk4ROh44BtqaMYVFjb8v1HHjKR12tihW0HS42bNHS+Na7bhiKfNKxN62sLmbrZ7N/d7FCH1J6WYy8A6MsHBXCIUVrwI9zSqFzHuxUFgmOzBEFR+IEuq6MbYt7ZilrXeSrDtZb0+1ENDNNtUVv7t6lQF569BI2VK709HJRS6swKM8esGolepRlLLzVtNBnKR9PwZHTKJ1UsMJa6MZRNJibrn1Vbmt9iZ5tR0UNAlcLx+7Bj+koXmo4SgB0LLRLdlki8nbHaT1HbcYq7TbYpusSiRD1XWxHSuF448Ere3psM73Q7efPJ4PCoXRWMDoWzvwcJmmx3NocANCnltHnkJfS9BzfGnF6JIiqdfDtUMZjmd4iHOuOxGnSqHuhKYWT0TWlHV6j9WVcQyWSoVz+KrdJmhSyGtpT66RcuQrqLm7YO+gI3AjGoUR+mijdn1H6iaKO/tlS8kxlTgIOpiFFFqVIAydz/BwMNVneKvYfkbe5BFj1Glvsp3PoZoV3fnUMaqanGJaSEk/12KO2K8IcUmFyomRdIk/RnWjeUuNLhukJvY3Tmoj5MoT2V0klfCMVApA1fMIO0xkmT2T31uDSiyE0pxbARdd7gZHZWtbQ3zdFQ6LtHpwhJNiv1oyy2Ufrpdc0SUNo8n9cpmIkJEU7RCscWq4BGt721UaIFSki3ZaHZ2DDV9eOcEXqrEaD1hYlsvSQYQoxvkB3wpnjaarFeKRzGYjjDQuhN7upinXEHE0BzQxZtPb5CSZ9CoVT7w+qGuE5427c4iLTWngoTnIhldOQyXEa4Ws2+gOxdMRIzYdBjD64jOXxCiZgfQoJvRH+HIdE32LevtQwBEYdvY5dT0JE3LU7zmGowDc1WQaelLi6Yu4HWSoN1KLhIKE6nYjbsRUYbt1tTROyMoqpXt5z1t64jgTweQtenPVQb4HENiLsE29Nply3GY23o12ZkNUtQ7Mbatvgt4rd+YRqboRQ9t1G3Rk3LYczNIDyt5xcssuwSarUaTYbbjUr8QEW0lGqyZ+fiIMeqPsRmxHR3MdU9AWq1zrCjbPNk6gilbeiqpgx73HenBG58tk1Rl8G+8hpTjrsht4lkx7BzitsDNyZxO0gbSwuE6+XFhqQmxghderShDlWNN75Dhh0p4pNXtD39SjPF6j8kLxqktddjyF3DJddz1oudykDXYQEwlLIFkUjs6tQ2FEiN3kOAhIqpc1fvVATSrrA5Sl90Qerpx3aKbpRDrBKZG3I2/ag+f3zhFU4Jbb+dNqHKI7NdzcrrzrHcSkk4cMVtFgnH6vPaNgTyfHIuGKFhQx6KRcO3eehsTwCCP6jpJWMar7h/te6iwi3+2JXi63wTDe9uStpqNrT+CE1JSIyyf05jAuGbekjoJoKASvIcpBCvKgl/tMiNB+1HtOIffrAHAT0y7zzqGUajBXVFN0YSjXxPqgsiSEnk5pbaJHet30fujHVJ9COUeJNVv4K+MaoisIXxF6gYr4aqmuyUkYpJZdDi5Ku3dCd8/T1pw2A7vllE0R101ed3qIeaAdN/lky2udb8e8k2KhnHhuZoUww5/8aIVYtGv5dsX39jW8QErDZHu9tmp1o54rRU8HnRprbi8eQqMyUc+bkooMxSW9Y2JxaKsTcleybZ8H5TixnnnTZTbnSdZxFQ8KTvvoBnuEqtna+n695AnZlEahoTTAmcuJoBJi3OAl0mjh2XXdGxocc9aWQb/n6HAqDUvN9PQwUdddqZO0iBbb3kwibivc2ePgK/Fyla0ksLWcZJSNl+frMhOWytK3IwAnjj/V1HSIlgGSrnvtZG2sCeIPp6WR+6zvMCIrJ0OANno6IZqEm8jFz+WWKAzo7MKaHPHNipQadcnpnhDDTKNv7LQEG5PIOzHRwQ2cao3FmNdEELZxtKQbSCebdGNXS6DU8bNJuajoi+FJ0io+VMTtejWOeVRVTtEwDFk7bIrFZEMyIKedwNhaekG2hFIu49Wtr1hEcyewVaPcjmfslbIUN9tMOaMIxcSHYErv1wKrVTUsPHRqMiz0A2JfjgV1yGET9Je+hJdnODmBvvHCyDIzKHblbMGu1Ti596UfMic5Z7OC2KhMsOqq7XQ0xoPcUXBwLhBF5Q0DZ2rCanC0B3sNyyGpzONTAq3xotLWGXROuWW7H9dYNQpY750vRqWlm1u9ihTKVHREDp3iBK1SvDHANnqUOV5wOlhbuUHdnFdDBk9nk/AwhbqC7QxLY6hQ7OX+ABmjpHkXbZU0qzFdJXuBccxcUnaahQmKQBwrqLbazHTWnnujr/4uvGFZ3MrIOpCSSTxf3GIt4ya9QaiqkAtDW3ZMxFNbOSv5O3+xR2W52SqhIfO872soC5O8iPfiinAb9wjlp55dRjWbGZw7qe2V95bXELbIzWESI7qJUgtNmes6xXfSZnWdQgpNCEqrr3gdQd3ooEJYmRt/CSmJRbg4mdzFzq/89SnAJDSyjrsW3UCY35DZtGEHToQsGhlO4/2mQktjSJHY4mhNR4P1qN1H1rP5Fve2hAgnkHjQGkZcW/VVUejTZV1QYAfb9zQrrGshiaW7gPebce3Dojk2V0kERC4zUx42BOMrXZ2U9YnfQhdNEAW/UMJtEQhbdXnYbRBnzR4DD72thmPLsBpob23SoVaQwOROIE4pctYGG4vQ1kZ1b+Kx4y1B2wzmYKm7HQgflLMs4w2f+csQJMPxIKwwtpIHdLcbkESTs1U/+CesI2RtHQFgO9xupequ0Z1Z+CdlmV0o656SE03T/3j5/DJ/bH9+Mv+LY/L5e+f/s0+rb19I34/DHt/KA8f/+pjr618Z8M/PL42XgOnfvg23WR89P7v+65fhL388TJmFp7dj5flIbuzeDwk6J5r/6dTL43R09sLj4PLnvgLX389RXx62+vMx05B0s7akcMtx/t4c5POxSQMu8z7rkiyZjzSz2dLneQwwEH1dvSIvv/0fyNvUorcmAAA= -->
