---
name: "rar-cowork-cookbook-teams-update-implement-corrective-and-preventative-actions"
description: "Drafts a Teams channel post on implement corrective and preventative actions status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_implement_corrective_and_preventative_actions", "rar_sha256": "ed177a7722d94758a642ed7091500449735b74718d2c96ffc67f48d627736b2f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_implement_corrective_and_preventative_actions`. The original RAPP
agent is preserved byte-for-byte in `teams_update_implement_corrective_and_preventative_actions_agent.py` and in the RCI capsule.

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

Implement corrective and preventative actions Teams Channel Update — Drafts a Teams channel post on implement corrective and preventative actions status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-implement-corrective-and-preventative-actions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_implement_corrective_and_preventative_actions_agent.py` and embedded as the fenced Python below (sha256 ed177a7722d94758…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_implement_corrective_and_preventative_actions_agent.py` first:

```bash
python3 teams_update_implement_corrective_and_preventative_actions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_implement_corrective_and_preventative_actions_agent.py   # or on stdin
python3 teams_update_implement_corrective_and_preventative_actions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Implement corrective and preventative actions Teams Channel Update — Drafts a Teams channel post on implement corrective and preventative actions status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-implement-corrective-and-preventative-actions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_implement_corrective_and_preventative_actions',
    "version": '2.0.1',
    "display_name": 'Implement corrective and preventative actions Teams Channel Update',
    "description": 'Drafts a Teams channel post on implement corrective and preventative actions status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-implement-corrective-and-preventative-actions',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-implement-corrective-and-preventative-actions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a6d303d7ee260640',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/implement-corrective-and-preventative-actions'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/teams-update-implement-corrective-and-preventative-actions', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateImplementCorrectiveAndPreventativeActions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateImplementCorrectiveAndPreventativeActions'
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
    print(TeamsUpdateImplementCorrectiveAndPreventativeActions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZejSJLtX+HFfKiqVmYgNiGyT58zCCRAAgmJTaKyThSLs++LJFRT//05kiIya6p73us+/WGUSwhwNzO/ZnbN3InfXpy+i8rm5cuLBpwCEZwsiyPQIE7hI1x5KZsU/ihTF/5DvLLomtjtu7JpXz69+KD1mrjq4rKA0/nGCboWcRAdOHmLeJFTFCBDqrLtkLJA4rzKQA6KDkppGuB18RnclVQNOMPbzuOGN0prkRZe9y1yibsIDkLiogON85jD+k51/8I5jY8EZYPUfeylCLTMCcErtAtcnVFZ+/Ll518+vYyKX7789uJlTgtvvdzNMyrf6YD0bhP3YRJb+Op3BrEPe6DQzClCOLsaIFoFvK5AA3Xn8JYPAuR59WMLsuAT8pe/pBenCdufvnwtkOfn68v459AXSBcBpCudtgM+4jmV48ZZ3A2vCJtdnKFFGtD1TTEC2cIlFeHrY+Y3SWWF/G189uNDyWsIuh+/vpTQBGc09uvLTwgE5etL04/fX0cp1Y8/vWblBTQ//vRNTtu7CVz0KAxa/fr2vH6KhQO/DY2Du9a/QakPp7vg68t3ixs/D7vHdcKZL69JGRc/PgRXTQkBdQoP/PjTPxLrRcBLs7jt/r/k/vwQHAHHh2t6Gv7TpzvIvyCT54I+ZP5jtRV06z+zEjj8Xd0n5AnUP5J9x/+/ic7iArQfiP9dcX9vwuRvyM//cG3/04RPSPD1hQcZDOXGcTPwBfntTVOX3M8/+N9u/vDL71D0/1OMVvaNd5fwljtFHIC2e3v7+Yf2fvuHX37+oa9grMHseuub7O/J/Hu43vX8AcHnqB//OBfqN4q0KC8F8hHpyG9l9X+a318R08li/9v99gvyfb6MnwkyLuJd6QOC73KmhbZ+h+NPL79D3ijgavpn/n95+Y//QJTYa8q2DDpE88q+Q6CDuzgHo/F6FLcI/Dvm9kgfTRtDYJ/jYPyPHh4tLgPk1//07rT62XvSKtqNjPTW3ynp7YMn377x5BvkybfvefLtyZO/viI61Fg2cRgXToYcWFX9WkAahDQLrYFTWtCcIc+4Qwc+Q4b6PH6BdIr8+q8rfbvLf62GX+/8HT8Y7cBJI5u1fQZeR0SsCBTP9XuQwcEVeD1UnZUetDOIIT1/gki1ZQaZvBvRa9M4yxA/HtWXzXCXDRH+Mgr79ddfXaeNvhYP+iWQR+FpUTjgwxzk82dobpDFYdR9LYAXlcgPv/3+A/JfyP806y581KHC8vD0H7Rwre22CMzHfkQFuhYGAySbu/9++/0JOxRTwEoJvR0HMXhMhvGcAv/dB5rIfsapGeICiD0Ya2DZdJDTkbh7RaQA+bAXKh0fjawfjQXTBxUofFB4A5TqwOV8IFmUHdJCf7TB8AnpW3DX+qvbOHcTc0gMTvcronAqrDFlBv8bzbwPgpPLIobwf0TI4z4U0vzQIot3Ea/IdoxgpHIap4oa56kjcB5+gbXlfToU7iAFuHwtPgLonk4PeOAgiIz3dOnn0eew9ueQO/z2Xfd9jDNWQv1eEZuvRftMFacZXeHB0gGVhn3sjwXkr8+QaqOyz+69QwAtHSU9veA/vXKPQemf6jkefQv37FseHQLytcenGIn8L2luxkWxgnBYCqy+5JHlVj+cHmCPrdmo/9HNwX7iPvmeWN96jHeGeifqr0UWw8hphr8+Rt5d9BzzIL++gYge2MNdPowPCPYo9x6+Yzg2zRj4ztfivSJ8ghjd6Q+iAnMd5sIYgu8Kx6fvlkYwocfrb93B3d1w2RA4GKJI1bsZDJ8AAN91RgyiZkzBp0dgLIMxHS9R7EV/WBUCpcOQgfLvroFug1XjDt22hMuE2Rc0Zf5teDz2XNAKv/egtbD3Ba+IBbNojKQWpi5snMYxEIUf7qKQHECMoYkfCLeRUz2MGdvlp4HO6IsyH4PoOw88H36L+7sto/lQqgNDDmJ5GRnaB9eHZz/sfPoKGpuPmXqf9Ed3P9eKfF+6/vq1uNv4URQgAWRj1f8OHAQGIIzqMWBH/mohB+XgGUAwEu4F/vVRox9NwIctX/60R/jxn9tG3Kuu8UfPfUGirqvaLyj6qJTvhfIVsgcKYySuQPsomp8f9evzR/59/pZ/n6Hqz9/n3+dn/v1B4wPAL8g/Z/UfRDzD/QuCvU5fp+MjOfbAGM/PDwSJ+7w4fSbHp1+LA/jm/WeIjKycDbBKf5So9yGwToUNCMfBj5LVjpXuAovrnaOhf74WHxHyzJ+RncKxvrbld3l9r9XQ3w93fpQS+KjooG5/7AYf+6dsNL8FL1+KPss+vRRODv71fdNYRWBoQ4zGTRhMM9hzdTG4X330X+PFH3eT9wSEzOGXX8Y8/ISMvfIn5KPt/YS8b0TuO76ihzuxn8eWe1QJh8IfH2M/tqoueIEbwm6oxvU8dldjp/fswP9sxJh+0GIPjJ1B+ZHPo8Y/CYFfwhA0fxayu39xsiepQPIf63zcvVNBC+30Ydf0CbnDN9ZXSKY9nPBnNVBPA2BFgKw8Lvcbft+WVT7W8vsdhu6xRf3t5Z1cnj54tqNwOMziz+1YUlEYvVAhvH7EGXz2b2xUn5IhUcJ2CIoGPkbTDk3juM+QNDV3ZiQOfHrKYNR0SpIMTVAuTdLY3Mc9ZhYE3owOyLk/w2mamLl4AOU94vht7Cji0VowDQDBYLjnEzOcokgGo3GH8R2Sdhx/Op/TUzrwYS35NjWFLPuE4LHkEd+PnnmE6onEby/ujIQjRbKV2MeHQxnTcS3UPUTypMkm1ysx2xNGZeRnewhFicJEyztKbM7bt2ncSibOWVQKU6Fnh2O3UW68ehCZRYBnzOXWztujcWr0NZ+Echq6OTX4ReBTdr0PuaWrblMr38b1+SDIGyO2zHO25qg6LbXCWl0ZibmIO91CV85wmpoV3tvUUOrqVauatU6SdBBcwVaT47apNr6kLs3I5UxFPu9FwpKvACdWnUNb0kKaNdi+IuxcNxfu/DJLW4NeTqtjpM8mB83cWNbmau0Osa8W1CxQdYwKAvtUyBgZBJS+Wc3OK4tc8cyln+FVp2VYN7FiDIsW5iqRLUEnePdqSbP52lr7+5Otl73tZsyMjY+7TNly+6SuNpWcnZpbSmxzmbB6LXeaGmPn4cwZZNnidOPk5qDP2s5YMk2mVSdLkxJ1vTaoY9XgOyKxh6Y2/emEWTkWC3LN31yEUti021K6DWdyeilOdWYIaacFl+luc2zjLZ1qdpz32K2y6UmYXOTCW+YMzvnXrCl2J1qyFsE528jL/jY7xZHjZJcAK4tU3HVaZG1EBgzL3Niu5katMP6SRY/ibRm1K2Fwk6zh8cZoC07Lz4J+WG+LwOWiHECC2g7tipysqFm5D2tvtZPgsmeLyrphKoYV+ZB5c3oxXfcnsSmyjCBAiF3xJpdP/TmKBZNvFH5Dq9M2vS09HMuW0rbcXyLNzz3y3JixmwTylW0nbp9eyql0IK/6BA/b26q2VqZO4lSiCsFOrLOlTKneyRJQO0lSae8d+/Jkw5ZUOSaTdtc3vRkdTUssWqzgFtctKqc3xS4daSpZQ0tWmptVNyWlXX3d4bnurm7+dlKlGFOdjbMvw7bnMtF7D11EqO0FiwJwEzS6Hb2ZcdBmaDhXfL5hmDqoMCKkdhnwbwRmOKIsmO3BPdlbbUVZ/lbTDscNtulgFMcrrLjgG5lT/Oa4rCaCa17JYLfcdIsNvk89LO0Coww8Wr5I9ARQ9Ulf1fSNw7SsNTDJ5kzWPmCisRZIIzaC2E4PmwVv29Jkw/X7aGMdDvoq94TktFsDCpUTT3bnerA7Mapge9Q2PW51TC6rWXcx9m5d0jNX6vGitY4tv0QDWlGF4y3YGviw0fFZTE26LWSUzt6ZAWmhjFgXl6TYdzYMJz5sTtRxnptXkMsKqOQk4O1DZ6dbIyWKMroeV73hC+doWanhkagF8eavDjqKnb3srFSZmJ2y+dU5iM12JVR+rU938yaS1aLA6UimiNNs04oBiRnW6XI81pclw3W6m+ZXososmgdYpUi2adbXeR2u8lsjpqQTmvziWFtDOo/PmsusZi3GlZWYc12qqyE+LyMBXDu+uoKDSU5bdDnQ7i3aSUeCcmKT22V1Ntlrc9howG0tYdEysy2IVFT0HDi267Fy7Sb6oe17dscJs8OhysyB63zNJq/FcZe2VbNda/LsvLev80IuDwQOEq7kpjugzmbN1krBJCglajrbT7CUEuOgafNwH+y9cnOTEzY5bxSU2ZMYI1Vnc3NriLl+pKXtmdBQtboBOby6uHZdWahOHQ4TN9gVKRGpKAfALs7UXmNWi5AlDb4Xk8DYbKOaX7tFs+LkfLE4VLMgxqn5Uu6XXLqODXJyo1rGi0J6L2x47pSvyzk+Jw+lFvGLOuXw1aFPVy56SLo6ZcEttY1GwDiNjaIDcdI6d7/iuUHyFkJ54eWFNpB1XWzySlnY7iVrdqInm0uCrZaAovI4dY08K33JdK83nGhaLk263F+F5pkCZ58WdZFwFVJBBcVfYwwzuU1pxWoUXFrLAmijmnaTibrZGpPJ1i1sWlySS2GWMpsh4okJthFzQvWCfhVpm6WahijcB5mTIsjkBiW3M76hOnZ+AjAO5NvgemZ00WsYClK8Z6qiTZRNXDegKQzNxiNRoQmHYPOph7uh1IaYOcxZgRfyKeanppKkzU1sUp5z4nUzQw2DOVYbxm8wFi+3hpUpkCkMrQ5VnWtvbtCwZeqvUHDaT0+Dm86LOX09NAaGpvZ1YpXhGd9KpoWJ2mHu8E7C95qTdZdNYfqNRzT7zG6CxNozK3WzYCJX2EZgFl+SHTMoSzQxXMX1ynZ/2pY3W92AvtSsQXVDnlsPTmMpvdu6PVectPMCRKpzLIODQWi+fHUTFOjt3pd5bY1yEE5yvuqlq3/ic0oi/XO+rkLjqqIFujyxdGddeMMFeMTVw4GFsdKDzVrmJkrsbGFvUtsWZZ/q217H6jzvvdP0uqRZvMKrGPMHzAoGpgprY+NP4qkmYfaBPeFWz1bSImAvgmxDrvHtWavqkzRZisWG2AuOOtR1tu2um9vCuKnXTbr0ucGenM/6ba4eHVvUVocNTJl2spb2RsRY5CSpzJRdFPKyUYzDST7mxgKw56Lr+OW2Nc7WuZ8QTL6ZMxl0vplZ7Nk+20cjXpbDTDxhwolvYJ0Ytqiv78NbvTRTzI4ttJruU0ZwciLWynp+GKIizpSrMVec89q2LKk9pfRu6eMLYJ73RmMYhrNfXGq5HDZVy+29hZbenEXBe1NfCqQwX7OFskJdFW37qZfQ1Rrwh+FiKrbJC+R50ccLendVZnkXD5uE3x+omeKjRXPD48ulP+CZv2lYWlFE2jgEi1ZXFzpR8aC5rabWvNfd2j+26CmmBL0ONJywz/HCgfTExiFRdj05CGWaKktl0bdCEVantTmo2zCQEmOd1CsqqtUS8/qbcW3W10ZauvmttuStX66u2W6X1/Sh0JadU5pLsZ5l+mJukW601uuDNfGnRNtkQ510hpwZ5dSdRyq7XIQK6faWeS2llEsiX9lPq+i83B6FQFF2mTS1INbkzfdKRa9Y3uTwSsnYWbWuUCOfHNJhRjiHbKHEHRGqA1Wp++PR3IZLZ5LZ9n67WqMHWCtjY6VQ+3nqHQ2V9KPtkO/1yIjUfH1pF2UmiOai2PbO3rMAvsR3jnKkqoW4AlTr3MzlyQ7YYK1q27TKGbmJwVJ1BFPuw1a3MBMoGmhMulAKGBGbGYOfdxMtDyq2tOt1BLvXmV0uasJsF4165ZXjzQE3t+Fuh0KOrzjfTFYBLmG7bT2jE72r8fXSpdfO1EwJdLff3HYotZSvctxxgCM1TytW5PJwOQ47kur3u/qYh4W7OZRV7Lr7jHMhry5Sct2pFGVjU7HK3BuaHiShWkRiMKXUFYGtxeAoaeRWNnWp7kAGt3ZVKoOaD9h1XQCttPb8qVtf94tz2t+kFTWdyPtuOfeXG/sgSXNtVqiy688vqz7VTxhvHPpNSlzOpijr17DK9dVNyCFMtt3sTlCmYCq55kK/XdZOoPo34KTL7JgHRY71844S+vjatp0kLpmr55z2ynq/wxoqdJLZdDEPD0oPbGa5oBMhKPYVs02kBa2w8x52LDPNn9B9ni30MCoi0j0qdcbNyQ7bA4YndqhhpfQ+27OS3F8O6pRUKnIBgtwsDttMPBidd1Zhea0ydC3ssdKDfUbegqw3D5RB6aeTyV08i2sHRbGnsgt39dPYUIZ9ou/0ZrhWPcUEZek0ClEuRImrrCC3F03TeGeP1bm8NNoD7HJ33WbwJq0mK7sBJqkonKx8J0aC1Mvt9Oa0eR+gcj9scBtPj6ZzagMdlaf2fs4USXIB2z129Jl1OCxKIJ9zNS/cMj+TpuA4Z4+DyePMieR86oiO6btJcr3OE0ZMpk1JTVpGPeeUGYHJKmVQMzz7fqBhdHvOLoo+mbX05SSCyUSg6Fjb1FpP+Pm0200q0pcETGQvi/WW4cr9Sqm7IZ45blNrKuHfrGM6vV5C4zi3d87OO9KRwl7Rbm5NyqwckkHsvaa5nTwsCk/BTk3Ytds1S/EcE9v0wiQZplqaOp3DvSGrHInD7NKa6K1ybxtnmM59wT1TwvSY8kcpIWm+8COidT23UbwkmRzRiTolUNYgB4LXJhmKyiiNKx1GE1DkgJ8Vy3WO8/1hLmNLWzFKf2GTVjqdhXNyDZt8dmufL7pdkilsaGYbqjBNjgg7ThVVVqeWZghSoudJPkyDqy1eb2eR2W78YjehBMGi5AIuPzmQ/UrlsLTOvU2iD9MzWJKwddsXOVGxl2HCn51tSiSb/XmRm4znnxW+T9GwF5hhxlJX3px4pzNLwe1ccBLneW/7Wes0yyTBl3sX3TM2saLDwZbUVSCEvVScp5q8n+CN5xEOerPOGIEC1eAEcwFQI7FYpx0WlBJErcfjRDETu7zsamxGG/w1lr0LjNubcGVoF5/jPKhLvPNINd/CToAcMowhOCwg1zXLnm9GYZMihwqrfhUK++7KSrCJCw50Y2lXgb7B/VKVXi+AZXm4O+5mAimBWzYB9fpAimESNWq/U6XoIiUnao/PLVM9WQknMnNKo69yERAccBaRfNodo+V0Xk89FEODnnDnQVSLdAj5slmkGjPxCzecxzuFV1Yt57Li8azLi4ukbGOBK9vgNonynoSdRg7QWCI1K6Iv/tz0lO35RnjHU7zqlzlaVGs/TpL1SVarBX6kp+0FrIdQj7pTm6CcN8QodhEB4VCCWxByqB43SSyupltOvYocEREqz1tTaYWKXajw8YyfTiiak29dLntgdjvJS448ify5vvYNvhdQjYgsSpniBOP3mFSBiChn8sCIK73mCPkyWQJzx4aFOnNCm2E7pkpgvQ1g2mz1EnWq1BNJFKQDrPZFJRRUR4Id1vfL5VySNTqZz8LJdnYlrPn0tu0S1Jv0dHI7Bvxqwe9kXvXn6K7az0uWQSdLJTiWxy7oLXE7zLelCIKZHHb4UgFR4TJicYuzKcpJLnom9dNEw+bTpb4WiGy13et6WLtCjc9UqqFg77FpmLgTua3rSfKOp7XzLbjwe1ZnK424eihKDGfJWs8d9JREmBOtmRwjVtV51bb8djbfOqBqrHUUi5dgqsg6z17Dyy4N93bvOIqoqPtbe8EC3V1kFxx1neB81P0SP4GYMdiW1yS6DzxqliX45sxfL4Hd6UQUBJeddAGwcyP3Yjyb8sC92PuDida6xwul4O1OoX6TL6Xr+rm6DysCxFm5mxESbFBaMXFhl7sK4M450lf2cVksUM9v1fyybbKpqKH4wNxiN2wHlJp1qiIeWj7Js1tmZjc7vp6mFZpJnKFisp00XdGdqXLnTnFSFNkFdm13SbvQYA1pTom5TSoO4y+rIa/mkBT1XjmHiyuD8XSxE4bhLBNM6vUEyaxQVvZ3/Lw+bkKWffn0Mh5nPw+l/w1vscfzwH/bseTjBPH9hdb9SBo4/pe7ri//DmN/+fTSeDE09XFc22Z9+DzC/G+HtZ//9Rcko9zh8TJ5fFd37d7fBHROOP5S1Utc+H3bNcNbW2b9/SD504vbt+OvcrRvzwPzlzsQeTWevn+/8Of5/FtXvj3fub2Mv2sxvoECfvwYMF6Gz5PtTy/+AJ0de+0bMaPeQFONGDzfucCl46/TV+zl9/8LvHN3lMgmAAA= -->
