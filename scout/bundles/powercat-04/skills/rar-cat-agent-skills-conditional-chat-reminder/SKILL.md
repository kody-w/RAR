---
name: "rar-cat-agent-skills-conditional-chat-reminder"
description: "Schedule a Teams reminder that sends only when the expected person has not already posted a relevant update."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/conditional_chat_reminder", "rar_sha256": "2ff960cf9799c7e9336fd4eea85e8acf88d5d9ebf2ff5c3a52dce0da0f069171", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Giorgio Ughini", "tags": ["automation", "teams", "reminders", "follow_up", "productivity"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `conditional_chat_reminder_agent.py` and embedded as the fenced Python below (sha256 2ff960cf9799c7e9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `conditional_chat_reminder_agent.py` first:

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
    "version": '2.0.0',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
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
    print(ConditionalChatReminder().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716eZOjSJLvV+Hl/FHVo6wEcZNjY/YQEgIkBEJCV2dbFUdwiPsW6u3vvoGkzKranp7dNXv2lGlVHB5++889Qvn7k9XUQVY+vT7Nw6z0wwwx/SBMw6fnJxdUThnmdZil8PXGCYDbxACxkC2wkgopQRKmLiiROrBqpAKpWyFZGvdIF4AUPgQIuOTAqYGL5KCsshQJrApJsxqx4hJYbo/kWTW8tSCrGLRWWiNN7lo1eIHCwcVK8hhUT6+//vb8FMLrp9ffn5zYquCjJyFL3XBQzIoFKN14qALXxVbqQ4K8h1al8B6K9rIygY9c4CGPu88ViL1n5O9/jzqr9KtfXt9S5PF5exp+jOZuQZ1ZNxUdK7fsMA7r/gXh487qB/PrpkwrqH1Vl2Hqv9xXfueU5cg/h3ef70JefFB/fnvKoArWoPnb0y9IVkJ5ZTNcvwxc8s+/vMRZB8rPv3znUzX2GbpxYAa1fvn6uH+whYTfSUPvJvWfkOs9eDZ4e/rBuOFz13uwE658ejlnYfr5zjgvsxakVuqAz7/8FVuYBE4Uh1X9P+L7651xAKMNbXoo/svzzcm/IaOHQR88/1psDsP6v7EEkr+Le0Yejvor3jf//xfWcZiC6sPj/5Ldv1ow+ify61/a9u8WPCPe29MUxGELs8OOwSvy+9eNPhN+/eR+f/jptz8g6/+WzSZrSufG4WtipaEHqvrr118/VbfHn3779VOTw1yDJfy1KeN/xfNf+fUm5ycPPqg+/7wWyjfTKM26FPnIdOT3LP8/5R8vyM6KQ/f78+oV+bFehs8IGYx4F3p3wQ81U0Fdf/DjL09/QGhIoTWNc3sNq/xvf0PU0CmzKvNqZONkTY3AANdhAgblt0FYIfB3qO0SQL9WIXTsgw7m/xDhQePMQ779X8eqv1g+SOsvVRTGcYU631EHBtaqv75D4LcXZAs5ZmXoh/AlYvC6/pbe1g7S8hJUoGwhjth9Db5ABPoyXCBhinz7S55fb8tf8v4bYqXuQDsobQjyAEYVBOKXwaD9gLV39R0rhYgLnAZyjjMHquGFEECfoaFVFrcQzAbjb6YgblhCS7Oyv/GGDnodmH379s22quAtvaMngdzxv0IhwYc6yJcv0B4vDv2gfkuBE2TIp9//+IT8B/LvVt2YDzJ0COAP90MNlY22QmA5NQkkg5GBsYRYcXP/7388vArZpLDLwGCFXgjui2E6RsB9d/FG4r/gFI3YALoWujXJs7KGkIyE9Qsie8iHvlDo8GoA7QD2HsQFOWxbIHX6WxN7Sz88ObSpCuZc5fXPSFOBm9RvdmndVExuofqGqIIOW0QWw38GNW9EcHGWhtD9Hwlwfw6ZlJ8qZPLO4gVZDQmI5FZp5UFpPWR41j0usDW8L4fMLSQF3Vs6tEEwuOpWDXf3QCLoGecR0i9DzBEnS2Dpu9W77BuNNTSy7a2hlW9p9ch0qxxC4UDkh0L9JnQH/P/HI6WqIGti9+a/W58H71FwH1G55eAPzRgZujHy3o6RtwbHxiTy/3N0GBTi53NjNue3sykyW22N491RsNLqwaH3gQe2cgRmy70ovrf3d3B4x8i3NA5h1Mv+H3fKm3sfNHfcaUqoh8EbN/4wttCqge8t9YZUKsshaa239B2Mn6HWN+SBZsE6hXk8pM+7wOHtu6bQ6GC4/96Yb6Eq3aFqYXoheWPHMPQeAK5tORHUavDOu9thHoKhlLogdIKfrEIgdxjuwalQiRAWBATsm+tWGTQTVo5XZsl38nAIGdTCbRyobQBK8ILsh9DBLKhg2cGZZaCBXvh0Y4UkAPoYqvjh4Sqw8rsyWRm9K2gNscgSGLYfI/B4+T1nb7oM6kOuFgwy9GU3gKcLLvfIfuj5iNWQX0OV3Rb9HO6HrciPXeMfb+lNxw+8hsUbDw33B+cgsGhg4g5oOWBPBfEjAY8Egplw660v9/Z4778furwiAr9F+DtQ3foI8jl571C3Zmb+HJVXJKjrvHpF0Q+yFz+sg8Z+CTP0T03pbz90kC8DLH15r66feN/d8Ir8POX/RPJIyldk/IK9YMOrZeiAIesen1ekST8A4PMP14+Q3UIC3GcIVgOywZQZ8rOCxX+bHAzwPaaPwA84Ccve7j+axjsJ7Bx+CfyB+N5EqqH3DPhw4w29/pZ+xP1RFdD61B86XpX9UK237gmjeA/SB7jDV2kNZbvDeOXf9hzxYG4Fnl7TJo6fn1IrAf92rzFAN8xJ6LZhbwLrA4JVHYLb3cfMMtz8vJO6VQ4seTd7HQroGRnmy2fkY1R8Rt6H99tGKG3g7uXXYUwdREJS+N8H7cc2zQZPcJ9U9/mg8n1HMkxHj6n1z0oMdQM1dsDQjrOPQhwk/okJvPB9aPGfmGj53S8PNKhqa2iuYf2eENUD+J8RGDSY/7BcIAo2cMGfxUA5JSga2MXcwdzv/vtuVna35Y+bG+r7tu73p3dUeMTgMcJBclh+X6qhj6EwoaFAeH9PJfjufzHcPVZCBIMzBlyKex5HY47HMRznMIAjCNpzSQAslgKs5Xgs61IuB2wPElIOYVG46wDMtTAPo7kxM4b87qn4dWjT4aCNA+GbJsaYZ3m0g1sWQ4w9gnEp1vEACzh8bBE0hrHY96URVO1h4t2kwX8fc+bgioelvz/ZNAkpJbKS+ftHQLndiTmSdn05cDqGTrYpJW/KzbXOmjBcdXWV7qoxJmznWr3ycfm8ULrTJlFwY0bPU2UvXtYKFU4vQVps0yi/6JaLRca6nanaFTriEFMeRnJcf9Jk+iyOyxiLihqoIrCXcbzD5XS3IQuu1XSdEQl8Z0fuZnY8cUBgur5M4t2yiqyMmAp16Ou2TR6ENSvNRmMl2jWbSlQORpjg1NHM7UtWL1j9ym+ScRabq50MaLIqusbBKXEW7Q/lmPPaw4UDHtE7qN33o6b0+kM197NrafX8fIHWu9jbSHAMwdB0U8n9QVdMUXdWrSvl7jyrr248CzAyPwQjFzjC+BL0vOBvi6u7Ns9lSLeplDWiRc2sYrfCJ9XysjPjYD9j8XQWj9nlUdv0o44k/MXOzpiJxZR7Ws+4w3wbX8gNMzrENrkNi1olF8WpTCdpbLrkoQDidRVY4fQa45txJVcO6fZNPVmtSk1cJTgrcvOpcZiMXHUu8DVaV2WjXZZnr8mnu/oAakfZdJl5hTP4VDo1xsbccD4mlotid7SijFOoyNFxxWQNnC+ZVcZZl1NVL20yaex8nKd637pdYBKjBqsCsZMKcNRCXbaK8zkUEp1reRpr9twZN8pD52snY+UwrNpP5yNSPtiMo0o1laaRrak2Wy6WXix1oizVurqoCkWInelWM5dgbns7LZAuE0rauaeTkZ2X46vOWPPlKlz2eI3T2w3aUDvx6AaYwqwWcwbHVTZA9eN16id4vXSIEF32u83Z3thNhUVexpKore4PcZIumOuZWTR9RfYTDcq1tJHVjCaTQ1W79t5IUpxb74P40MsRKcvc9kRGW2baT6lI2ZTT7sSKxcRIqDg7z2vduV6cSFw3xjX3N8AklbUcZOZI6BdltD5cgkm28Uiu0rf8VrQVLC+vRrIVV1S9sGcBSQEqj2r57K9UdYe5dTHTC5JTCpntHBUEO0XdK3LjTH2SL9Z+MVX2u4sr0IGdafxlLRTWcldY6Xx8DLxKL2T70h3lGugXvzJ3S6xtuVQjFYphXGdH8EWzvZK0gGWtEiaL3krkXtg10xpPCRVVCPbaH/LwSh7dfeYFhoB3hACufDYiRoKVaMK1x2jvFLhXu4znpL5LsGjrLbDEucIcmaAcppwzL05L3g/7Imrpi6Op8cHJCCfqC1m7XszTYXLN13xwJOLdKk+a1aiYpsGFzRdr0xbXPBN7PlPGXhjEudktaKnpF5eYZqMNEUkLnrrmwOtOhoexlHlK9OBwlvXMAFwb2uxiJIwEtg/3PSbREjdT6V1iiiRpreR+WzkjjrGOWi8d1gHovFWu5cUkhLOBPRFdv90dJidwGpdLOXSxPp7PV36k0ITsXtpqxtViTnepXtK1dV1W4yUz2tTT9UlBpWi/nK76YO6nhlAXpBx5l73JuSamx80pq0mSvdDT5qQxXtVeJBSnZSKL0aVx6CI6k7UOu8aOa+bkej/dlZF0FQVO1a9nod5MDijGrSAE9/qW4kZJitKMiuqpvxen2HhvBuwMxGcsVzBqDOR6MlpPTDcq90bMxMHBGck2vu7xgkf3jHbajUzF24tgzuxma+IsnsmpevB0U1RkU8FlpolkMHaSLc4rqb3sxBYPgj27qyOcnqmcpZ+EmJH5puwhttGRpjrTS6dr3dod22BFyUI4MTWcaAr+rAmz7Q6bb4VLOw6OlJ8fl1OpojaHYnYysekUttCJiU5Xe6BaZu7WazaB8CrL1L7zcymRMz9kRIyRnSO6Pkt512mbZqxAJKZXUhl0Ibslt/l+51mq4rML99DENtXTuUATe6tVATM9VjixjI8VZy4KOdJW0324F9RNsTxRPeEm6ebKyaf5TFkJDb1Ez5f98TwRIXTOzNGGvibTes00511ouhSRh8zSL/0iAAu7HXNgwhZLj59SPIuLTbBylhQf0meXK89ei9kp5i9wjwAl6yyPqDsSLXBqCnJVndvK4zmKV31VbTWcVLetBUaTwjybYZ71u7mwQKeXox5rlYpnkropXZrzvETQWny2Yyd70J/FQMgqVpwUuk/11+N2Q4aHhbiiu6zYln3c+axENWuNwLDS2NdzhtwHxmy9wNviuMHatdJ3uCRjPY5G7ESOou06svuGvZa1Q7sdY+6N64lvXQVjJidX5mJcKQo1z0yzcOesmfZcmBXjqEJ5e6FQZZHq+1qcQ3CMGTvu0nXhlMVSbEPBtZk+bLApbK7yWDH5SAMrsBmFCiXMQslgoiycMgblBGVMG3vNLp36EOITbhHKSsV07cyuVZM6eLbabJfOrFtPLSn0m6vmzmPJ1czx3M6mUyLU2Hrn0oQx6ueenZvnTeSrskRfenuxDAq+q3Er9JpFtfHMZt7s28VC41OaYrcm7QHfOKy5CV0DjR3H2yNNRuyi3mh9iZVAU3ny5AuYINOEflGnS8rvMDFLpnwr4gqlSgY5d6KxnftbYzeTjKjXW/7QyZV1nkXmIsy91SxzW2u7ZwhsBwjlsNcIvbucimO6iTCUSGSQKaIwziKi1UyeXsBKnOt1puGn+W7ZrnOrAuJY5hXdlJPdzI2MuI0m9b70uWaNTqT9JUyd8ymIR1lmnoxG7cxqKjvKFVNyWpEXTE5vF0SyH9uVFQljNluift0L3VpfrWGbiJtkzo8uOdR3Ec0ypVKMxXyTzendrOQu7ppJ5T7CD0VRav7J2PImNnJCH5Xxk10VdpQTpDOyzNFoMr9I3nLDduySu/IYYFR7PSbr6yKTbbljaJZFLxF/XE8al7eTcyZOvVHXcxZY1ItWlLvxJCzTDeWWrq7BnHWF1Wka8dlxufJFdWLuSUwpwWot1Ok6MdXR9rwumlXmVgB2v2QtVMt9JDATmjUNsc3n8oacJzS/uKSBoWXr9hqQKh/HcNTplutywRmaaNhHXx6r0tLBrlYVjgB6mst5ISeZmOHpYYcJ2QXfHmzPA6AmCN0ltkJ0PDrnce6RlS1EJE6NyTOzPZz7UMS39HLeeFM0wx0Mw0HhTClXinARPZbYaRkyktY5ZzIJzjaOs1d6Hqz5udWZW6OM9W3Oi8uGms5ZXFUmE2989Ma866KTKtKPRD0zrTWwellxln1QUqwRsXt2OYY1t17uYLeXCsJipxxtS6Ar/ePSmY42q6vun+kLVdB6KkQ03F8Ehirpp2vnGEHqXEFfBySYMBrB0uKyn5QhNo76zXwE9xCrKDX3E6CjLEaipEAqO0xtBFZrWzIZtclMN3m2GRF7NVNLPFRahRaI65SYaiu/v87hTrPAKiytTqOQmLHHU6mQF/XaAnG2lYVJZsJU8D3fXCSOSZxDoBhb3Tlntq2sypZYXcT5grfGWN5eipXkU2srrEjemqM7RmBP1HV6mC7VkuIvNOq31vJKnH3CO6sTauROOxTtW9Y7O657qZwo5LzZNISbS9076o6gtyPT5M7FWj60e57oxzrgOpecT5cX5yziIhm7hyWPGxUAGarFRXVAV2dmNPfh4OIRhqjQk0W7kGbESD7huge8BCRdyATxjCE31wKtqEN5Xtp72cmW5Milm7014w3OBCx9SBVSItCFcvWT3DdQ8uC0EK+ZYIVXR9ZunI16UKSSkeJ1lWEAb3EiMQSflIGO9UcwIwxtKqQwUySesnhvrqHHbmql/kjA/fOWqA+GTzh7Dm83DmhY8uIoVLbXWnK5nauZVoY4WioR7ulRuL3oY97bLMxz3WInfGlKYs6tT1HRGbFwNbqqmrtJJy3AomI4z5yNiflVM2SJ3R5wG5tUCjf35KktcPgKvypMCbsPfTkcY7I/hAyzcZMReb6E+m4/5yZlH+rTxDkkTllLawUFU++kjpyNNEtcejVRFXtVXFdGRVoTVDjMqNa4pAc2a9uCWlGw8AvZ3bPSUexY/GzXRrPC1zhnSXnpNNaJMbYelmVaQPhVPsEcwseMVsRGEViveNbYceEC9lYXX0Vr0TyzKbEv8ryAHEKUmmZGz9AZgWKNeqynaCC1CT/WGDDT9NDgmjnB+HvGtkcCnNKZpBodl6Lhtef0Mm6luPIw3T2h+VmRJOLs4hfV2kkedq44btUqbZXTTLQ/Hjk0RNHV5njWd9zueGxVzzhF3sx0TXD0kytv4uMZ15OVN4cTz+4ghStps/JY2HS21dJrXWy6Xm9n5QabOCjahpm8VwSLo/pUKlywS6uRM5vVF59YlfXBu26Pq02OAaebguBqsd1MnU+weMMXnMIyDskJYDs9cHU4P2xtuI/tWdflJPVIR8fZyZpjB7xc52M62GJOmo/NMWrNUHrbriSVXy59bQYCAccnmoSdTMrwLMY8r0KVdsazSNPrPT6nABjr68y6xlTccV0qHVjgOXjV6SM0rDVfbXv/UrIiiopzpWYbk95frgKBLnkp9WhQkkve5XuNjo9GU65P/Ygaj47OItAKr1UmFMd1lZGft3YHJjzEYdZeXkUSIuIS4+W9kNojTRbH401Rm8VEHXO00o24+JTE541ITKiONOtChBOZcDlpuLCOeJ7/59Pz03Di9zi3+++/WRuOU/6fnercD2DeD+pvJ3bAcl9vsl7/B7r89vxUOiHU5H5YVcWN/zjg+a9HVV/+8sR3WNffv58avkK41O9HmbXlD39J8fR+7Hr704h6+C5mON16rB6uvSyOs+5rkz/drHGHI/I2rG/qPc6HB2cNB8RPf/wnqLHAcD0iAAA= -->
