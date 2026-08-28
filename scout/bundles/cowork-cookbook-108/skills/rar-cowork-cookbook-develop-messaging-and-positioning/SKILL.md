---
name: "rar-cowork-cookbook-develop-messaging-and-positioning"
description: "Move messaging development out of scattered docs into one working surface the team can pressure-test together."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/develop_messaging_and_positioning", "rar_sha256": "4f2bc3c52fad6f088602687bd24efed631ad6bd17d2e3dae00729fc8828a0607", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "intermediate", "integration", "monday_com"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/develop_messaging_and_positioning`. The original RAPP
agent is preserved byte-for-byte in `develop_messaging_and_positioning_agent.py` and in the RCI capsule.

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

Develop messaging and positioning — Move messaging development out of scattered docs into one working surface the team can pressure-test together.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/develop-messaging-and-positioning
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `develop_messaging_and_positioning_agent.py` and embedded as the fenced Python below (sha256 4f2bc3c52fad6f08…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `develop_messaging_and_positioning_agent.py` first:

```bash
python3 develop_messaging_and_positioning_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 develop_messaging_and_positioning_agent.py   # or on stdin
python3 develop_messaging_and_positioning_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop messaging and positioning — Move messaging development out of scattered docs into one working surface the team can pressure-test together.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/develop-messaging-and-positioning
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/develop_messaging_and_positioning',
    "version": '2.0.1',
    "display_name": 'Develop messaging and positioning',
    "description": 'Move messaging development out of scattered docs into one working surface the team can pressure-test together.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'concept_to_market', 'intermediate', 'integration', 'monday_com'],
    "category": 'integrations',
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
        "upstream_slug": 'develop-messaging-and-positioning',
        "upstream_url": 'https://coworkcookbook.com/recipes/develop-messaging-and-positioning',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bbf2afef0d8a93ee',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'monday-com', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/develop-campaign-themes-and-messages'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/develop-messaging-and-positioning', 'uses_skills': {'custom': [], 'ootb': [], 'plugin': []}, 'verification_status': 'draft'},
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DevelopMessagingAndPositioning(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DevelopMessagingAndPositioning'
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
    print(DevelopMessagingAndPositioning().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716ebObSJbvV9Hc+cOukX0FSGJxR0c8hAAJCRCLBKJc4WLfdxBLvfruL5F0r11T3dNdERMPhyxBZp79nN/J5P72YrZNkFcvX14U18xmrJkkYeBWMzNzZlTe5VUMvvLYAp+ZnWdNFVptk1f1y6cXx63tKiyaMM/Acj6/ubPUrWvTDzN/5rg3N8mL1M2aWd6CjzerbbNp3Mp1Zk5u17Mwa/JZnrmzicm0pG4rz7TdWROAj2umMxsIVFSAZFu5nxu3bmZN7rtguHoF7N3eTIvErV++/PzLp5cQ/H758tuLnZg1ePSyffDn3wQiM+eU1+EkLLgDyxMTfH15KQagfgbuC7fy8ioFjxzXmz3vPtZu4n2a/dd/xZ1Z+fVPX75ms+f19WX6J7fZQ97crBugmW0WphUmYTO8zsikM4d6VrlNW2X1zJzVwHqZ//pY+Z1SXsz+Po19fDB5BSp+/PqSAxHMSdyvLz/N8grwq9rp9+tEpfj402uSd2718afvdOrWily7mYgBqV+/Pe+fZMHE71ND787174Dqw4uW+/XlB+Wm6yH3pCdY+fIa5WH28UG4qICvMzOz3Y8//TOyduDacRLWzb9F9+cH4cA1HaDTU/CfPt2N/Mts/lToneY/Z1sAt/4VTcD0N3afZk9D/TPad/v/N9JJmLn1u8X/Ibl/tGD+99nP/1S3/2nBp5n3FcR2Et5AdFiJ+2X22zflRFM/f3C+P/zwy++A9L8ko+RtZd8pfEvNLPRAgn379vOH+v74wy8/f2gLEGsgEb+1VfKPaP4ju975/MGCz1kf/7gW8D9ncZZ32ew90me/5cV/VL+/zi5mEjrfn9dfZj/my3TNZ5MSb0wfJvghZ2og6w92/Onld1AhMqBNa9+HQZb/53/O+NCu8jr3mpliTzUKOLgJU3cSXg1CUKHqe25XoJRUdQgM+5wH4n/y8CQxKGu//h/7Xic/2886uXjWvm/v1fAbqKbfiu/l59fXmQoI51UIRs1kJpOn09fM9KdiCZhONc+tbqCcWEPjfgaF6PP0A1TM2a//kva3O5nXYvj1XsPDR32Sqf1Um+o2cV8n/bTAzZ7aTFXW7V27BRyS3AbieCEoq5+A3nWe3KZ6DGSq4zBJZk5YAcXzarjTBvb6MhH79ddfLbMOvmaPYrqcPXChXoAJ7+LMPn8GenlJ6AfN18y1g3z24bffP8z+7+x/WnUnPvE4gbL+9AaQkFNEYQayq53wZYISUHxN5+6N335/WheQyQCQAd+FXug+FoPojF3nzdTKjvyMrNGZ5QITA/OmRV41ExKFzets783e5QVMp6Gphgc5gCHHLdzMcTN7AFRNoM67JbO8mdUgBGtv+DRr6weY/WpV5l3EFKS52fw646kTQIw8Af9NYt4ngcXAf8D874HweA6IVB/q2eaNxOtMmOJxVpiVWQSV+eQBkPPuF4AUb8sBcXOWud3XbAJHdzLVPTke5gGTgGXsp0s/Tz4HAJ+CSuDUb7zvc8wJ19Q7vlVfs/oZ+GY1ucIGQACY+m3oTHDwt2dI1UHeJs7dfkDSidLTC87TK/cYfEL0D03DFFQ/hPLsa4tA8Gr2/7e1mEQjWVamWVKltzNaUOXrw2RT/zMxfbRMAONnIG4e6fEd99+qxlvx/JolIfB/NfztMfNu6OecR0FqJ7llUr7TB14GJpvo3oNwCqqqmsLX/Jq9VelPwK/3kgT8ADIWRPQUSG8Mp9E3SQOQltP9d8S+O61yJlODQJsVrZWAIPBc17FMOwZSVVMiPQ2fTTYE5u2C0A7+oNUMUAeOB/SBnYGo4KvL7qYTcqAmMLlX5en36eHUBwEpnNYG0gIzu68zDeTCFA81SEDQzExzgBU+3EkBdwMbAxHfLVwHZvEQZupJnwKaky/yFITojx54Dn6P3rssk/iAqumYDbBlN5VTx+0fnn2X8+krIGw65dt90R/d/dR19iOc/O1rdpfxvYKDNE4mJP7BOCDuqrS+h/hUhWpQSVL3GUAgEu6g+/rAzQcwv8vy5U+N+Me/1qvfkfD8R899mQVNU9RfFosHer2B1yuoAQsQI2Hh1m9A9vk99z4DVp9/yNA/EH7Y6cvsrwn3BxLPqP4yg1+hV2gaOoa2O4Xt8wK2oD5vrp9X0+jXTHa/O/kZCVMJTQaAnO948jYFgIpfuf40+YEv9QRLHUDCe0EFbviavQfCM01Avc78CQzr/If0vQMrcOvDa+91HwxlDeDtTI2Y706blGQSv3ZfvmRtknx6yczU/Xc2J1NxB7EKrDHtaUDegMamCd373XuTM938cQ92zyhQCpz8y5RYn2ZTQ/pp9t5bfpq9dfv3DVTWgu3Oz1NfO7EEU8HX+9z3DZ7lvoD9VTMUk+SPLczUTj3b3D8LMeUTkNh2J8DO3xN04vgnIuCH77vVn4mI9x9m8qwSdWNO8Bs2b7ldAzkd0Mx8mgFTTjhQzUB1bMGCP7MBfCq3bAHOOZO63+33Xa38ocvvdzM0j33gby9v1eLpg2fPB6aDtPxcT0i3AHEKGIL7R0SBsb/eDT4JgAIHmhFAYeUhlr2014hnOqgH4TgKISiOWQ6yAnjqoEsYPLccGHMQd+mYLgRhCOHZOI7gJoRCGKD3CMxvE56Hk1Au5LlLAkZsZ4ki6/WKgDHEJBxzhZmmAzhgEOY5AAO+LwWw6Tw1fWg2mfG9MZ0s8lT4txcLXYGZu1W9Jx8XtSAuJrrCrD7Q5xXqXvloHquKerCdEkqshhHaFjaHDRIxyFKySDml6HUcGkdb9sXWOqAaRZ5ixePjhYTZc0bAm4KDpD2HMVE4ct3aHjBvbq8lSab4LC+s2Ewp66prHrUcBVdYD36ZGMrlojbEYu4mGZEcnbBGzzCFmWHVh2VteYzDc9VQyGGhJIeG4dfFJTwETl3guaWVx8quz2pn5sLCL+eGlJ20C0MZDHLQlAvUKyXMBH7bEbscO2XjsLplBoK3WXU4XsD3rVsaLNofLwwmJ9XQCmV5hg20uZApd44Fs9NEA1IFPIeWpZTYiRAUCR+u161OhBy6jrlbd1YPoVqGZnLE8TbS/daGabO29gfkWh/8ulGoerky+WZsrwf3jFtGpfjwyPND4vS+YGNlgwpyNXdZtIOJI1Rej8BgUTI/yNy5QPSQXi81e7gqTUAHUdb0JAcF+8hmxjpY8m1z2xsCj21Xp9iO58P1QuShTiDieUSUlsH5k1JehAbh47VJtYMH+xkU7BhmOGIGvi8vjrk2ttSiNUlUPI0mtWLVqxBAcNCcLT0JhBUdRmzoYeWA3GTBK4XjXuM3qFvAVyAGaHf4vDo11QbN4nKZFCfhlq/X0JY7nvvb0uGWFZDykjTLzh3RwY7yvnFiwz0RR5Hvd0JjbmhGs6ozt47HVFgXDcyYK3e/yy4XKCUTI8L4Arc2slHvhCTKyhamEf6G9AMnU+WIsUxwQvhepM925hfXdZjAlCvN7fm86o36DGuMXo9ZeEmv7e4CEM8Y5b1UBxyKZVwOa6q1VStB3GdWogV8gxwItVJuG9mjKE/O51RABGuqNah9IRH9ora3GIY3N2M30qs2UBpzvRw5J8HH+Z7gq/lZNvXMiysanjdKxSaDsR3iDjmcJP7aCaE+Rn21bJfyXoh6jxoRRh8LQwHl0YKLjNa2cZnuTWmZMtWF52ytXvESxUfmcb9G7HN9ERAB5babbWXsjxS1kZqDHkhjjq9srkNTJxozbbWTcdnTePV0Y925UJ4YdsMiYRR5rJofxn2XrLd0M0eLeXYObGMJOfNg4YXWUZC0PY/mHuGtT5cDcgrDhU44wSmDmQtRVUfgkrlTzXe5Zxr6xTlYfbJfRpovpM11RapkNi80b9VSUDkv5T29yMnuGudlGSg4C6/3eJdHuUczZUJ7p+xmrhSHxuCLK5XVHtuxCmofR+qklc2ommo5sjC8qLZxoDEydz2jfOPUaN/zi1yWFnBwRMJYnisrxxSKVbmhyEaFSQ/dZd1G0o2TaJhcZA3k6MH7hYkeJDqYE9glGMILdapKF5KwvMJrJY30Coba0xq9YjTdiixjDfRhIMTCQMxr7hSRQJ8ibnuWx/SSGraCjAlJDkdXK6kEnqeCQuGR4VXi3CJ4fRSQc1O0yDWTFxy8KctkPEXdMp7PSTuwETnVtSuES6yNUdhA5Al0KYliqd82+DwqCWSBdu4Gv+xWO7YbD07oJJujZ2pTxBlMH4eMjhf+7VzImsi5trAwR9LYhFuO1eV2zoYUOR/rhZEQ+GCx3CAybBEapX4kUDq43VbztCkJekwQHd24pLA9+wFec8wQDupaGLcss5SiTb2J+GC+K3YbOjrlPkxDjpWWoyGbLptTlHDgEDrkyRqSLi60r83lJd1LjKL48i1LDSpYq+GiHLtlFUU3VaPh465PfSOtZDgebQLTi+UuvVaZI1jry7AQj/Da0Y3N/kzJA3fehg0UJ6x8WZTLA3wyNh13qHJoxy9Oi35DYlUrrrCm6wRG2Qy33U28aFv4sMCPi3kRS8dka+cludGs02BpF4psfVqEQS6tm+wk8JRSGkNjcFwm7Wwmd65pxpzVnuhoSzZrxs05Uqmc80WMztEYVT6FKk6R1ieHddl2o58owgzOZcNFpc+LA+Je0iiu9aWVnq14dUoRUeol27GLeWH3x/nR8u0CWWpu6o0bihoYSk1HQw1UC0P21MGjgPWNulzhZulp9FCg8FaVc/0mlDwzH/Z2gJPUmoquakDsMZEfM3+ptmSV8vGZbsOgbIKFVffrmzXuLvOW6xmlUnh+I0jxtRgu3kVd+yBsITYeIrLSHTQVHanWN3G8pZCtYKBpqXV8qzEL4houuVOpJox/u5l04+QOTmEhtc+PsokM7fYUJXuERtdUfub2VBTvoaiWfJzkaUxYdSrnrvGMHVQBWjPdhfeFZYtW5YXKEaLvw7FcKdxu1Tk6IqJ4g7BrXWaCwfAlxOYYQQ7PJeJd8lo8qcGRNmmeFUIHscK5lEHwKNzY4KBbzGiY8z4R+eKoXE6XMj14nodmcuJW+4rdzwkm3xzoY01YZIKKcHauTuujIRm2Ni9oJyNYKV4mByjfXUQUGnxx2aYku9dBj+BaoWzImHRkfIgq2COTxyHlQ6os75t6I7lBHK+sftsXa4JbCJQWswo1J/hFcCVFuEDgnRBUxuoQn6Fg1Vrrdi1diVQF+3/QK+b0cD15nniqR7fN1es623MHqRlktTnAOhmKemivMVU54vL6eMMCGdVRJO3rmwz6eqjJkJxrYpS6ynuERCuiEtN+B0nSec9iCl5E2aVLjn7lsbsVaFz1W4zu6ItegZwqNfuK9wdoUMQNttyDZDkjhrIryTTmTFgJc/F0uPDbnkiu1MHRuGVUZra0vI5lSFTaUKZShWx3Z2sTn1bWLWw2JBumOoleg7wh3YNZ0HOh4zQnDLe7BT1eSpnpgmC8MnHAtrlAiqXEWutgFa4HqD3DAu/GNUYeh/WqUjI426ZiGq/ydSWN3OYaCSXWWDQZFtWBQ7esKu4gk96c495WzANuHJjdynW9xTo9hMCmjHmKYmcpKrtNq1TYjbFoA9aDuIzwRD3i7Hq9VGzNY1MRjc19Iq1ODuSWRni0C2sPxdtllqSWvbciU7ssjK22ObIMzinejowadb88uAK6EvJT0LfXHN6NTJdcM/12aHqtd3oA8MXhGLHWABAjc3vI5RA7dcLSICw1X2VVVjH1ZqnJdFGDuFSV+FB0HRNsyzXUxk7UEoKicsCYnFqeC16gEKW50sSGqtK8uaHxcR3LUYNSNqHtVKSxeSm4qJuog6ECRC+1PiQ5meWHhl4N0lZasRS8w87OnIK1q8cmOZuXjEoFo3KI9XBvHKqbidwsNbPgY6BxCotR3YLa97ZgsJvELy3W4Yz0XNupLeLnce+oaw7VEI+W+dE9LlLhSqrVMUAsfSvplNOnmU1QzFh0ZniW9xsVvxzW4SFS0I3fhLyoszqz9XkDlXt4RE/kZUeyjLtzlUYlTGapNQdZCtJgiy9Ph4Zy0nN7WJdMVaFcg/i2oB/YI9upYoycNtWA2fztnKZov2GgVAs5fx5hqFJjHcfvWKaA8GOjCcMW2rNXL/AFdFMr5MlAqahrqfF8ZcIgHexSHxrUUnaILZfttoxIRyaEfUbFOmrvPLi3OoYfJF+/5qcecTAqgNqIIpHNsBktNrQUZHvwEJriPOiaIIJxdFaLAYrEth57YukdGuXSiPoV4v16c6y1C4YEEq7hOQe2F1sRDda5lRhiUspir6205XK3RevlrkKqA9iEmpW5SJCCVhe3rY+3CdYsdUcnOvEyGi0MmUdx4LeObRw38l4mEOzIRmypRYpg1MPWR9NgPPlmKh8NlzhgSSHtmiYtnNRcsCufHlm59HUQ19IeFBZPOmln1ySRXLkN7u1W5cJSd+l6sxVDhN7N/TEXJW8ACSjtd3G2ri5qOEAeJLNYa5WNasvRWdtFJWgtDvOt7ZvQYGdXZXGw3BH2F5d4fYpWx3GxAL71tU2imTcPdhZsFhMnEV2tk+V8lA7zRLQCYX2TdmYuI+aGXbVtcIGW+0uhdUdL55ITClL6ym95a5kARMRIU+arE69C1Flx4127XVFS7PWmGhOrobX2FdPZ7aZRNUNb7+SVuDtZW5PiMCr3DFu9iSIQdaOoNCbVZe1X82Ar4IaQdYQvVskNlBTUmW9XFlp1FD60RwSX55RleI4TOKPTH+s6MmlFP0nnm4v3KFELR3Isrsf4muZtmhno0MfuLilPhHFBjwsUXmBbhtKb7QUnFc1XwiFYJ/PduuMtzcscvKcRQV8iARPRst010cFAvMh09WRtMhI2YjdykBs4SoWMqInIWcQ00knnlegghMJd63hxJZTCx8hVxsdo6Cwbsd8doajVbh7YwZFnL2V32XBK5WV/cG19m8AjiSm+x7IK1NuHTYhQCNg3Lq9ixIlXBwLNWYujY8h0uzC5lnMSxiUoQ28KNm/YqF8ttvxR8koSo6Fma1s+UQ8+f4z8SN2ofhwKOUYPnY0eQWObV/Jt3UhTZFHX1PJ6gO26tL06KwzpTAS0bFUD5AotYYTiuBdH4Xqsmg1igTabIhfG9dihN35PwFzgymGbY2sBy6qqT5ahlPtjK8O8ffIKdlsbLHvLOxLPhFxkyjmFe6bTWGGnRbZnIh2dM92gqU6ltUwmoYaFHaZjYW3RzhOQqIKyLkaucwToSLBWp3ABRpJ5i6rnxc01GnXV7fNdx3swOWSjTKnxmsWg9CzBIpFzNhPFkbVzV9K2ixqihU7bDO2qE4F4Al2jGKq7oEp6i5uwuTFB1uPtTstdaFOfcNTa6qwHe+M6tOJ5bpmXZXW6wkG15Fyw18uOmOcvFkPQjcFZwHSbawxlJMzrdkgbbEEytLTNwrxBqrojepHNYQYON76gW6LuShdcx3be9gxtO1PyHV3vVyv8RIV7U9AXme12KD6MFm7BiNGwaagaukeoniuzpShKmx1ojucSaUbcVQm4zKQ1r7XZ4FhkA0G4qgITTUs0HFJgKy/ENbLeBSwBL1u8kQ6YuO2GC9OrZ3iVYWM0kmx3pUo67xrBV9M5e2EvW0K1Yi7fZGpcxl2PV2yPxT16IWhMs29SvV1S9sWjoJvd1L5FYJ2UdJq6yjsPdc3tjuaKtl3Nz8FIQV5TUvISYy8p2PX4qTAHkYQKm90RS9Q+6A80muB4jGSYTuFsKvDNZrXaNpy4NbT6dtiyikMSVEejizpnFyhHDtFwzIQTbwV1gmFpIErF4jSqaCZUgijf8E3WGHvf4HOSJP/+8ullOkd+ngb/+690p+O5/7VTwseB3tt7oftBsGs6X+68vvwFmX759FLZIZDocRZaJ63/PDj8byehn//l64Rp+fB4Tzq9wOqbt3PzxvSnv/N5CTOnrZtq+FbnSXs/jP30YrX19DcH9bfnofPLXa20mE6w8+mN3nSqnQMVi+Zbk39LzSp2p7Ewm97IuE5oNu7z1n8eDH96SfPMMYfpAHXS7/laAqiFvEKv8Mvv/w9M1waZNyUAAA== -->
