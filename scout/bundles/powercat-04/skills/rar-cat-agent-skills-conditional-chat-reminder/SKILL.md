---
name: "rar-cat-agent-skills-conditional-chat-reminder"
description: "Schedule a Teams reminder that sends only when the expected person has not already posted a relevant update."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/conditional_chat_reminder", "rar_sha256": "1452500a768e389d1c97a53057224a79ac96991e2267344caed384994b7a8c46", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Giorgio Ughini", "tags": ["automation", "teams", "reminders", "follow_up", "productivity"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/716abOb5rLuX+Gu/cHOkb2YQXjXrroICSExCSQEUpxymAcxD0KQm/9+XyStZeck2eecqltXdiUS9NtzP90N/u3F7tqoqF++vKzjog7jAjLCKM7jl08vnt+4dVy2cZGD23s38r0u9SEbOvh21kC1n8W559dQG9kt1Pi510BFng5QH/k5uOhD/q303db3oNKvmyKHIruB8qKF7LT2bW+AyqKZ7tqAVepf7byFutKzW/8VCPdvdlamfvPy5edfPr3E4PvLl99e3NRuwKUXrsi9eFLMTjkgXX+qAs6ldh4CgnIAVuXgNxAdFHUGLnl+AD1/fWz8NPgE/cd/XHq7DpufvnzNoefn68v0R+8eFrSFfVfRtUvbidO4HV4hNu3tYTK/7eq8Ado3bR3n4evj5HdORQn9a7r38SHkNfTbj19fCqCCPWn+9eUnqKiBvLqbvr9OXMqPP72mRe/XH3/6zqfpnAS4cWIGtH799vz9ZAsIv5PGAfRtv1txT1m178alD5j/YN/0eaj+ZPd0ybcH8cei/AT9NefJnn8BfR9p4QC+f80W+ACcfHlNijj/+JRRF1c/t3PX//jT37EF6eVe0rhp/1t8f34wjkAeAW89XfLTp3v4foFmT9veef692BIkzP/EEkD+Ju7dUX/H+x7Z/8Q6jXO/eY/lX7L7qwOzf0E//61t/+7AJyj4+rL00/gK8s5J/S/Qb/cU+fmD9/3ih19+B6z/Szb7oqvdO4dvmZ3Hgd+03779/KG5X/7wy88fuhJkMQCHb12d/hXPv/LrXc4fPPik+vjHs0C+kV/yos+h9xqCfivK/1X//god7TT2vl9vvkA/VuL0mUGTEW9CHy74oRoboOsPfvzp5XcAOjmwpnPvtwF+/OMfkBy7ddEUQQvt3aJrIRDgNs78SflDFDcQ+DuhRu0DvzYxcOyTDuT/FOFJ4yKAfv3frt1+tkM/bz83lzhNG9j9jmcgsHb77Q1cf32FDoBjUcdhDG5COrvbfc3vZydpZe03fn0FCOUMrf8ZFPLn6QsU59Cvf8vz2/34azn8Ctm5N9FOSuvcZoK5BkD862SQOaH4Q33XzgGW+24HOKeFC9QIYgDNn4ChTZFeAUxOxt9NgbwYAElb1MOdN3DQl4nZr7/+6thN9DV/4DIOPTpLAwOCd3Wgz5+BPUEah1H7NffdqIA+/Pb7B+j/QP/u1J35JGMHWsPT/UDD7V5VIFBOXQbIQGRALAFW3N3/2+9PrwI2OehfIFhxEPuPwyAdL7735uK9wH7GSApyfOBa4NasLOoWgD0Ut6/QJoDe9QVCp1tTO4hAV4M8vwQN0c/d4d4ev+bvnpwaYANyrgmGT1DX+Hepvzq1fVcxu4fqV0jmdqD5FCn4z6TmnQgcLvIYuP89AR7XAZP6QwMt3li8QsqUgFBp13YZ1fZTRmA/4gKazttxwNyGcr//mk8N1p9cda+Gh3sAEfCM+wzp5ynmkFtkoPS95k32ncaeWuTh3irrr3nzzHS7nkLhAuQHQsMu9ib8/+czpZqo6FLv7r/7BOG/RcF7RuWegz+0eWjq89Bbo4e+dhiCEtD/z6FkUohdr/XVmj2sltBKOeinh6NApbWTQx+jFBgSIJAtj6L4Pji8gcMbRn7N0xhEvR7++aC8u/dJ88CdrgZ66Kx+5w9iC6ya+N5Tb0qlup6S1v6av4HxJ6D1HXmAWaBOQR5P6fMmcLr7pikwOpp+f2/M91DV3lS1IL2gsnNSEPrA9z3Hdi9Aq8k7b24HeehPpdRHsRv9wSoIcAfhnpwKlIhBQQDAvrtOKYCZoHKCusi+k8dTyIAWXucCbSO/9l8hcwodyIIGlB2YhiYa4IUPd1ZQ5gMfAxXfPdxEdvlQpqgvbwraUyyKDITtxwg8b37P2bsuk/qAqw2CDHzZT+Dp+bdHZN/1fMZqyq+pyu6H/hjup63Qj13jn1/zu47veA2KN50a7g/OgUDRgMSd0HLCngbgR+Y/Ewhkwr23vj7a46P/vuvyBeLYA8Q+gOreR6CP2VuHujcz449R+QJFbVs2X2D4new1jNuoc17jAv5TU/rHDx3k8wRLn9+q6w+8H274Av1xf/gDyTMpv0DoK/KKTLek2PWnrHt+vkBd/g4AH3/4/gzZPSS+9wmA1YRsIGWm/GxA8d8nB93/HtNn4CecBGXvDO9N440EdI6w9sOJ+NFEmqn3TPhw5w28/jV/j/uzKoD1eTh1vKb4oVrv3RNE8RGkd3AHt/IWyPam8Sq8bzPpZG7jv3zJuzT99JLbmf9vt5gJukFOArdNWw+oDwBWbezff73PLNOPP+5o98oBJe8VX6YC+gRN8+Un6H1U/AS9De/3FSvvwF708zSmTiIBKfjfO+37Auj4L2ADa4dyUvmx60zT0XNq/bMSU90AjV1/asfFeyFOEv/EBHwJQ2Dxn5io5cMvTzRoWntqrnH7lhDNE/g/QSBoIP9BuQAU7MCBP4sBcmq/6kAX8yZzv/vvu1nFw5bf725oHwvjby9vqPCMwXOEA+Sg/D43Ux+DQUIDgeD3I5XAvf/BcPc8CRAMzBjgKEqQGIkgNk3NfXzOeKjL0DaJIySNYYRNM7bLUAyD+hhG0ThBuLbv4XOCYQiHtucuQQF+j1T8NrXpeNKGZOgAYRgsIFAM8cAKjBGeN6fmlAuYIjbj2KRDMrbz/egFqPY08WHS5L/3OXNyxdPS314cigCUAtFs2MeHg5mjTRG0o0TOrKaCsEqYpr2RyiUTb5WknL1t4bDZ6Jy4c9ucQ1uMcV3JvYuhm6l7GhesgG122To4S8zSyD3yXIpxPJ42q7SJlz28Iw/XYOPj9PXquaWzaspVSfYlefVdQb0ZVNa4ydmh4fkQU3F9SiR9uVTxMJshw3DFoxNyLBoEvQzpcBLadpB4bS6sZshtFZ2i8zYXW6N20qwyq9Ny3C5O853Eqzaei5t9o6GHvjXPyeqqqwvyTDFBTjPzIHA6Urti87LFSXi+xZbNJuF1m2NHoAh/7Pa96ohoEdjp+bZUZ5fwwvSjZ1/dGxJaR8yKt5bqzneHGc62rubjC1YWRTUeRaCXl5Erl0njGNNN/rKiV8iity5dZDouBvNGXRgd2S6JddJx5TGOi/gqS+meESSsZeT9uoU1ZmBMdC9cbM7sUSPJsVw++TnIf311biRjPyfa1dHjpOVaUHMxOsq1yctrE6Fn2FrLFzNZttestFsGu8LaXlPhZNFlRKFjmzXrvbCxUGIUuTzt9JhYMhpLSwO6H1MjMXIQ3NlNTmIVWTmLlm5NAU0zz1yRx2DtGQR2hFtCjDHUzxW9WRC5cKtSjms3J3pZMqPTz4pNCgfmhT7OxuRiHA4c4xlX62pSQrbGvYWzq0uS1hMT3gyNQ+/dreWub8nqaG8EfiVqmKowq2qsvWLLD3B/5eoxZkWl0a5jczxf+jMVXE0l168Snxr9frRP9No/ihVu3Ho4uXY5eWrWqH4WypufVjsusQdsa9eaWB/ihZvrTXNwzL0XRBvUtE77Xl/lR51C9WMjSUpUV4GoHNWBXh77GhsUl+XoEzFb6HM2usIxkmiakMHx7ZSZomytWuLE1NRBIIYkWt5y0eDGIWXFBYuu8jHzfR80M2VsuQMttEnVC3tjoEatZEztsp5jnZdohLJsjN4/6xqbrG0Hs1OfRmQ/Qwhcc+E4TM/CZQuLrqf1bhZt97Z0E7mh9/ZE4vTr1SyUC6kfCqsnWeY0uj7tJZYmhh5zC+QRz0zTUYM+GWe4RO5mBh3S/kEKj4q9C/PtFhPSC5E5VHVTmnEmXM+MMWJq2RBa0F9qxNDidttHtbYPGrjPqlQrsDZLUCfXj3TfzRArolU7c2tG2uYrRESK+ezIVbaEdUd2JXByJV/57CT6J9zI94OnLiLH4fVZwRrpSVgf1uSaMjs6v0TKLNoYRrnVduQqUc6wO+PHmSVHLsWrF7RyzEY65ws1jMhwKTMMPb/U5Kzrtra+NKxgGWCrq43fFIyFVYtVT8SlkASSm3Erdz4MgtviHKFJGOADNB16wdQiP7ny2zUzLOLO3Ug877GWbnFnk6wqY2+MBc/JSjxn+XqTouJ6vsSEKh9jdx6QvnVqqXkzU5Z7e57Be85fsoFpeJdlu11H5zOtDeyMa2r7NGR2dGgqxfDnp3GDq7MySXdw1m+PRelw3LjbhxGtHNbHEN0nYb+pcPc0OxV512EuGJJ0cUfjN3TWEM082MFEDHfSdkeSRiHwjr63jpq9EMJzhSCYnF47jt1xbOUPx9E631ac52PFDnXj641lTFKtfHhVu5U757FMX/qIqYSbmzdnNOMSW4KWdJWWUYfx6Pec4qDE0mEuTnplh8Q5q8J1uwC7YXXpc420N8VpWPKiTpyEnBV3VSL25ZwOu80Gtah6lVbcapRu6OoyOJVKIQuuSf2lFtHycUTX8mDz3YjuwyHIqXK5UeJTh0nZsfJv2UpOCg1pb1ReBGfgnY3LMlbCl32vap2B54trtRW2ETKfH4i96a5nx+KwIFaz63GbryVYdkvP2zTR+bqNb5U39+LR3WjV5iIqihGbrnwYpDM5Wl42HhNKQ2RuXfCDHswVCz0dZHuZHbZkXlC6hm8WlEYHmWRTfHMd0/RU7LZwezjNc23ZwG0bKtgtHYlbxAqH7S50GefEO0Fb3ChFE+NrqGi00iLJ4na5xunQ7S8VvjY2y0sjSu0wCyy4xDqJmXMZY8bl7HRpj14xn/eCbibixZVX/ca79eMp0jlTvVVww0e8IaOaiQwlJ623tMuOJpCd7Vi34htXTtYRLshy6lZ71pSZ4rQg4yO2uC20uCDiY2MsNtiG4EzPEImlmDJkddUNyWil5ZkvOeQ4XyAeOwAKDE4vi926SHuNj50sGy4jAfqbjomqHBD61rytLG6tKFE6rIJKwApZQ1HBbGtke9lKatjQ4X4bHrSErUJRIuxDnGftoUDZ5WqoyTUmadHB8A4ob9nG5tKylLbp7T1KbqptetmsN5HQGPHGVIRsWJf5dnlCdako4WakrgyRWBK/6M/j4XyZyaKHzLQDotlsYKuoXEvBtt4gubTUl7ZZHKzZpahnA+UVZ1jUV4Y1CLg2Xjk5En30NOedmMjPXLKu08PCGa1IdVjz6NmShFrMIltH9CLnWk+tT1UU3kQ69RBncZXR1rBE9cK6Sp9wvex5ttq4yJnjCG5x40tGIzLQEdz1XuWrXtkOiaAhnF6zdLOdiy2fokVEdQq/9ZLigNloMWekPdxUVx+N41XJn7dM0138XF9l3LjYor480wt0xY0rx0QEHbncCtUgAW7PlL3GecflLY2SpbBYz/X1xnMFeS6cC4SSQQvnW3G/1FbpUdjn4RmNZFMgRfocgSmCILPzVjCcS836DqdeyzoIjxrbUDQp9iNCa1tcPYO+I3epurxo8TYUF2YRVFgx76IhIg1d4VupSBVKj0hkCDTOXZiSmu0dSST3HiZYWaocwyiP8AHdheLGKiOz3NIVp2P9HHXDqKkXCj2G/kFbWmrsVRqMFcVaXlC8aaSXw/6IS+t1hZmNbW4VrybF1LM2FRIOh1BeU73bLaQLYWilWhjsblEcxbWzuRWpqJAlps77ztv4/EEN+ZhlT+Ww4PbzK3uzUpy9jFuO88yy7S+LvsmkCuVaBYmLYxjs9+M+cqtNeHaq9flYmajnjLqE7lOzVtZ4Ve+7mNplFeXY3TjrRHvdMIQR8RneXMSEVQgs2TqlVXh55gsKXxMRVqOj79kpjWaOJfuBh9aY1zC0aOHnQIKbmzpnYgcTaivHAs3g2IVnB1alMAfEPpj7W2bNrruIW4bW7Cicjl2Xhaa5bEQsHTx5rSxWfHMsNVSmtsRMCtbVmNebbbWi+liy3GDRkcfE8S+9vOhYeLP0fGIF2+tLGRLyVkAbS4/OlOCsbhWYxQxkNNGOoOejOSpNtlk1cj6nuEOeOJjarKn5bUx3A27h8MKiT0dOR5JOZODYmbVn4ex78EjbBYPtHX+ftUnMB6wieILhYTu92YXDaIw50V5nQ37jstuO3LnkbDyre5bl1QytI/Z03m2s7Zq+WoxpLGejaI9jsifbRLbYm7u05GbemjMGb2R1nyH8duCQGS7aLamN2aoTsYN/GZUa3vb1NfGty85a+Hgqsmc2o3ocJmHLsoLE2m521sAX/LVsMYw/SAoddEna2LXAj8jaad0kzQNPq8x0l0u6x7iKOp5lFKxo65A001lWBlECmyq+Cjj5UNpZw95WlwMuz3mwToIdVfDmwwrjLRRrErA0VQ7oEnK9w9pgN4DhzVApcgjPu7x1zomOO/gJDcilfCV4dbmj/YG/YmDQcjt0ZELFy/aurgbDoTns1VFiJI0vlgqxZPdKkixv5JpmnVO6UOuyp6UwKHsBIEF16nh2gBfO/najEOU0BNmoeDbRRljUsKRRL004beP1ijaaGyzpxMzfsRnXC1So1tw+amPOyKwjfrmRpx21kbfYQjmJtmBgfSEGyyaaV/qVwbTUOtYus8J3kQQPQ9z06XjGNAfbOlepzfa4cVDHdFXf/NsmoNNmgR2Z2TINd1a2mqv1wAlu1unDumJ8dDDQHK90xWKjW9n6DOvT86XPZDtzhwpB1J9a1el2dqDAnk6memRYXaPqGOvm5BWr9TLxm21tUmSFb5Osc/o6a3kWUdtiKJY66XuayARJoZMLkFfqEdcRHd01mLJi1WMy5+cpgl3a89IZ6UtmFHbugz0w7KllyyX+ZkHomIvbcqLNwAY0g/mriTCp0OWBWlUDbsY9TAfLGK3pdKfQFsZeml2d0wqlgZk1aSj4IFv7q41QdlraTgkSGM635kFLYa8lO7KgZFGf69aQJCyPnLh8X1yzY6t7O4IEGwx7s+vaVOt+yR9ncu5dFYqQaaLNMEpzZFbq1PkQ0nNMFQP5yFbx9ig7or5JDJGCMRGsjZyhpDvarmlj5dzImcyPzYIlUhRDJYIsjAQ/CMamv2apQxnaLWIiLkFxOKY5Y6kIamZgJMLO94buo5R48PFkdQmk/LjuPTFnDMeppfOua/u2WUuCKg2J3dpIj8H4EaCPn4QjjoABnDQtYUHH2QpdjJyXBNoCxtO1fFIHcuWRBt1WQb+iU1eM8avepjtSN+i0P+bO7YyLu2SJuUU0OBSypfVLvrEHlGjQVqXPxrmO5zGz7RLeZMZiVrpIkZ94lFJVo7jm/eFcogv6zJ1H92QuwgC/IZIzVzRpUxKZpTK3DKnPB4sgK6NoFOPUZrchvQ54hw3mbKYLexUrzC1cJ0t+cRgwxZxL8z3Cr/twqNvGlPSSPB2jQ3DBDU6VRfdgRmeuJQWh9m9DBZelBubiMK0bTF+I/pCMYU6nuhLUHD7UKRF4PrUpbldmk6FWvkc8+VyYaAwWAjdm85pFCxlbR30qSjPYh5l83u9mrVaLYIm5tZvuPCBbdsDxIyleVW/lGdtheURInM5dLIEPR4IWiR1/vB5vu6FFpaySD7C2FK5xfspjElV1O1XlHVfvF0v0zFkr0qs4WE0Dz8ZqSdpEi5lRKydmnWe10e4oNdHSmble70g29cJQUbiTtMJ1T9RmSufwhJYW3o1iBZ69icOw4i6mwJwGO7ThGxgjea9Tbi0LmsYZXgyidPIUbK6AZbvU46BjUnexc9CMo9rzboau2QA5UWYYyJ6e84v5GgxHzXzXUFTd8TWMWOPxWCG4idFocJ0fmQXCi6uVMzdhhXThmqaUI8Mv1j3rYXtZwkNDuYExe00PrQI75dEtFSNAi4NJG14euNek80l60wmZulPbIbdOONWP/nJnWyPYakPsSmPERp73NZaOWe/lo7xy+N3uhmuyAuMVfPUJYz5jc9ukdwCMB6ZwCX6D9nkWV81e05YG2ODsts8wdtgSVdmFG56nuwQlXH5n3epGlQ6HlXs4i7Njz9O6tOcjCxVSykjI5cbLDZ+3fJnv8Uuiw7IXrTvVmTsWNqwinT5gZH9mEErSMcOXhhLfL2ubIPDu5nT1eUmsiPMZ31dgjl8TfKvi2nmZN/aNNAN47s5UXVfLsDokjBjVTHEZN4o2c5F5fz1QDi/RKNj2DZXpl6pTjrtrgLseWO08WWPZl08v01P057Pw//pt9fSI8v/Zk9LHQ823l1/3p+C+7X25y/ry39Dll08vtRtPmtwfADdpFz4fmv7nx7+f//YtynRueLzznV7L3dq31wOtHU7/7unl7VXG/R8ytdP7zemJ8fP09D0o0rTov3Xly90ab3rtdI3bu3rPdy5AK/wVecVefv+/SELHAuslAAA= -->
