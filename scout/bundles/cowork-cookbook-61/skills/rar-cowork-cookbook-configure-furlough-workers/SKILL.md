---
name: "rar-cowork-cookbook-configure-furlough-workers"
description: "Applies a bulk configuration change to furlough workers from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_furlough_workers", "rar_sha256": "9de55d9a04d6ab274a6ead3d44a3d6501e048d256023e002eaddd44bb6324544", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_furlough_workers`. The original RAPP
agent is preserved byte-for-byte in `configure_furlough_workers_agent.py` and in the RCI capsule.

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

Furlough workers Configuration Bulk Setup — Applies a bulk configuration change to furlough workers from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-furlough-workers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_furlough_workers_agent.py` and embedded as the fenced Python below (sha256 9de55d9a04d6ab27…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_furlough_workers_agent.py` first:

```bash
python3 configure_furlough_workers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_furlough_workers_agent.py   # or on stdin
python3 configure_furlough_workers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Furlough workers Configuration Bulk Setup — Applies a bulk configuration change to furlough workers from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-furlough-workers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_furlough_workers',
    "version": '2.0.0',
    "display_name": 'Furlough workers Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to furlough workers from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-furlough-workers',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-furlough-workers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'be24cf5d32508078',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/offboard-talent/furlough-workers'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/configure-furlough-workers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureFurloughWorkers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureFurloughWorkers'
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
    print(ConfigureFurloughWorkers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOjSNLmX2Hz/VDVL1UpEIegxsZsEUigg0MgDtHVVs0N4hSHAPXb/30DSZnVNT09O2O2ZquqtBQQ4eH+uPvjHkH+9uJ0bVzWL19etMApIN7JsiQOasgpfIgt+7JOwa8ydcEP5JVFWydu15Z18/LpxQ8ar06qNikLMJ2pqiwJGsiB3C67jw2TqKud6THkxU4RBVBbQmFXZ2UXxdAkOqgbKKzLHKwGJUXVtdBq8IIMCpMs+AT1SRtDVydL/IeQSaW6zDLX8VKo6aqqrNtXoEcwOHmVBc3Ll59/+fSSgO8vX3578TKnAbde2Kciwfq5svlYGEzMgFJgRDUCBApwXQV1WNY5uOUHIfS8+tgEWfgJ+u//TnunjpqfvnwtoOfn68v0T+0KqI0n45ymDXzIcyrHTbKkHV8hJuudsYHqoO3qYsKmAQAW0etj5ndJZQX9fXr28bHIaxS0H7++lECFu+lfX36CyhqsV3fT99dJSvXxp9es7IP640/f5TSdew68dhIGtH799rx+igUDvw9NwvuqfwdSH450g68vfzBu+jz0nuwEM19ez2VSfHwIruryGhRO4QUff/orsV4ceGmWNO2/Jffnh+A4cHxg01Pxnz7dQf4Fgp8Gvcv862Ur4Nb/xBIw/G25T9ATqL+Sfcf/H0RnSQHC/g3xfyrun02A/w79/Je2/asJn6Dw6wsXZMkVRIebBV+g375pyor9+YP//eaHX34Hov+vYrSyq727hG+5UyRh0LTfvv38obnf/vDLzx+6CsRa4OTfQPL8M5n/DNf7Oj8g+Bz18ce5YH29SIuyL6D3SId+K6v/Vf/+ChlT3n+/33yB/pgv0weGJiPeFn1A8IecaYCuf8Dxp5ffATcUwJrOuz8GWf5f/wWJiVeXTRm2kOaVgH+Ag9skDyblj3HSQOD/lNt1AHBtEgDscxyI/8nDk8ZlCP36v707VX72nlQ5e6O/4Nsb4X17Et6vr9ARSCzrJEoKJ4NURlG+Fk4UFO20WlUHTVBfAY+4Yxt8Bgz0efoC6BH69a+FfrvPf63GX+8smTwYSWU3Exs1XRa8ThaZcVA89fcA4wZD4HVAdFZ6zoNzm0/A0qbMroDNJuubNMkyyE9qYGpZjw8G7oovk7Bff/3VdZr4a/GgTwx6FINmBga8qwN9/gwMCrMkituvReDFJfTht98/QP8D/atZd+HTGgqg8Cf+QMOtJksQyKcuB8OAa4AzAVnc8f/t9yesQEwBqhfwVhJO1WiaDOIxDfw3jDWB+TwnSMgNALYA13wqI4CToaR9hTYh9K4vWHR6NLF2XDYt5AdVUPhB4Y1AqgPMeUeyKFuoAUHXhOMnqGuC+6q/urVzVzEHie20v0Iiq4AaUWZTFayfNQNMLosEwP8eAY/7QEj9oYGWbyJeIWmKQKhyaqeKa+e5Rug8/AJqw9t0INyBiqD/WkyFMJiguqfDAx4wCCDjPV36efI5qNQ5yH2/eVv7PsaZKtnxXtHqr0XzDHWnnlzhAeoHi0YdKMygAPztGVJNXHaZf8cPaDpJenrBf3rlHoPrf6z/7A+NwnLqHTRAFxX0tZsjKA79f+orJl0ZnldXPHNccdBKOqqnB4ZTFzRh/WicQJmHQCA98uV76X8jjjf+/FpkCQiIevzbY+Qd+eeYByeBtPYBGah3+cDtAMNJ7j0qpyir6zsKX4s3ov4EILmzEjABpDAI8QmHtwWnp2+axiBPp+vvRfvuxdqfTAeRB1Wdm4GoCIPAv4PQxvWUWU8PgBANpizr48SLf7AKAtJBJAD5EFAiAbkCyPwOnVQCM0FS3b3wPjyZWiGghd95QFvQZgavkAmSYwqQBmQk6GemMQCFD3dRUB4AjIGK7wg3sVM9lJk606eCzuSLMgcx+0cPPB9+D+e7LpP6QKoDfA+w7Cdi9YPh4dl3PZ++AsrmUwLeJ/3o7qet0B8ryt++Fncd37kc5HU2FeM/gAOBfMqbe8hNtNQAasmDZwCBSLjX3ddH6XzU5nddvvypHf/4n3Xs92Ko/+i5L1DctlXzZTZ7FLC3+vUKSGEGYiSpguZ7Lfv8lmSfn0n2g8QHQF+g/0yrH0Q8w/kLhL4ir8j0aJ94wRSvzw8Agf28PH3Gp6dfCzX47t1nCExkmo2geL5XlrchoLxEdRBNgx+VppkKVA9q4p1aAf5fi/cIeObHg19AWWzKP+TtvcQCfz7c9V4BwKOiBWv7UxMWBdPWJJvUb4KXL0WXZZ9eCicP/vWWZCJ4EJ7TBdjDgFQB7UybBPer99Zmuvhx83VPIpD9fvllyqVP0NSGfoLeO8pP0FuPf98wFR3Y5Pw8dbPTkmAo+PU+9n1n5wYvYD/VjtWk82PjMjVRz+b2z0pMKQQ09oKpaJfvOTmt+Cch4EsUBfWfhcj3L072JIamdaYSnLRv6dwAPf1uonHgNZBmIHMAIXZgwp+XAevUwaUDtc6fzP2O33ezyoctv99haB+7v99e3gji6YNnpweGg0z83EzVbgYiFCwIrh+xBJ79Bz3gcyYgM9CJgKm0HxCETzsI7pOOO1/gDgn4F/Nx3MF8kkDQAMEpH4xF5liAIHPw0AcPXZfE5jiB40DeIxa/TcU8mbSZO45HeQsU9+mFQ3oBhriYF6Bz1F8AEQSNhRQV4ACY96kpYMKniQ+TJvze29EJiqelv724JA5GCnizYR4fdkYbjmvOzkMswHUGD/ZxtnGvxtgd1bYMtZ28wa+KwxLLIrSW5apuVu24NVHRU4sOOS8MUWJCxJidLHpb2IVXJdWW1k6XhBT5rR0smoU8UspZ0tNEO2dz9JgXDr2ygrwzeGltB7nZZegcSYqjpsMu1biU4RBt7M7gxpsNuuFnaGVvdINnZ+kSwKaiRrm1KfUyCkcj380Pmb80sGM10EfCqoxzpafYqrBOrqe1e8uK8iapVieqHNNZLjU86ueUK6kXeb9f0JQ3s7LB7eo9dTRIzL9eq/nWH9o1cWsNWVu77Y2X/HM3iCXa83N0vc87m7R3Aa5RAl478zpbj/JYoWgT5zSZFltulbCHs4PtTWnXaG5yC0Wrq3aSN5gdkeGEx+KOEa1Lct7Qq8qW8BXpFuv9qqYQ+IDOD304yOuL5OVkivlc6JtSZ2hmbW0ynnBOFSmVZ4WHb3rnJ5VxXNKY53psfKIIs8o4pvbcUIUDN1KinZcP2LCOl4w8G8kLyY5o72IX2g7oARlc0M0WaxiRg6N3WbnSwHkuqR+PRmanl7OKqRulPhO5Omdr0A3EaFLrrmm129O6MY/2Hr4ZJxL1PbJ2eiPbhEWsBmzFnBasoewRdY5YsXW5un66RameK4/e4WoF+02Yc8dw5eZUd5FQWM73NrG9IDfpdNWIYtkIncTuAqc2rdmuMNATZfHu2urX6DloV/Ou5PQYu+6FY8WsN+XuGuSFeDy5s0HK3KURwqvUL8kNRXBpscE3mFxuXb4olaLo6bZVGZeYXxa5SN+wKhFCV/FcOezZNVLL+GxZOaeh2J3iQinFq4mbeBNuUdk7WIIXK1VJ5zeMG2MarZsI7W9UiQt7EnbDozVfD/TKbV310tRpYcuE0MYi4lrHZnEetcraUW4LwiBboWd7pstCOWTCqiIFzJhzmBB5eOL3LEtTu2OdLnM6Mzn/ct7KJjsYXOpZfHczmzXJxpy9Q4bk5GhVkCiNamm7AT6cgkwbVkiTkEW9wT26x/PwjGo5bhgN6ORPrVgixdxOkzPvb6O4EE58rG46Aj6ynXI7tB2Z7RukuS6WF9c+l/uBZ2bKTA93ElLEygZZw8Vutp7pZLe37PA8CPO9M8IaiVTmrcKUpXCu99amlZx8XCFE2Iq3ULqZ5zOBqhdmJsU177F2m0kKnDh42a3NGDfrYbEwLE5B7QXPsIV/RXCUnqWXSy4kMKdxRYmSro04BhncLup1TmWEu9cdT7dULO7mfaVsUv58zak4QlDD11vMxBzzMpiaSVicdT1Q8Gmk3ApEFiaGbJpGM7fAu6ThxRmP6WyhHRJxh0l0tEUT9KK2Gx89rw/Nkho7foUzZ7Ht2DXJ5aUrIrBdCKy/qTYjP2PMrtYoanAs1dF3ZcvX6LINvWVfr9a4gHDB0q3w4SphR6fJQYIoBVyzO7iMEtEVfG5VLiviFsX77rhRFVu8wdUlCdGt287L62guS7oLMK7CEFwh6BQTG02YmeNyKRuZwLcoEoqtFprJyQ9IQ3H26NI86fiI3mJtgwQX0Ujg02m1WDE7pdv3eoFRtcdEgjvHd3QlX6167ooBuW3tsKZoVSdMfMn1IikWS3SzXefJgsMBjzF72RXVcxlSdZTKGkuJ9cVfmFVvEB59KZOeUdjzCdGJUVsqhOMGK+s2kPEJXuPLPYMFbZLtbf5kzK9s04gyabsHJHc9N2/S2CQJtiYqTyCqoai8IvelkBBQ2rdqFA4QvWFOsIi653px8YetSsjXc2DMVWKQ5bXsyxkBygptE/woFBde0fsNwfJ2cCXrUDG2VCjcjsSCptvsGsaNtzWHXdfddjJNLfyoSDdwojJxqF23WmbYB5M2Lxm1sFdy1ngEvdTKcsnHSBOj+o5aRu56rG3UljR9u6SEI6KNaj1UoNRqC/VY+WldoRd/HMF284SPtxNZsploFrd04NbZbJ7sYq3YsXZO6xdxsamqlNAImwoHf67d9BBOG1dXMly8pP7JX3RONJfC06La1I7lNtJKPmLUBasF95Aoc7XyssTCZ7d8tWoG9HZUl2eMq888BpCzAwmuL7CAtHzj9AuSU9dIQh90dbSEan9zQh0+igc1WZw6dsMMK1qLBMpblkLi8pnW+ztAw6DMuRbFMmTjwSPDqIeLiIR4unNGahlybNXPWsvcY/N9W99SnWpDTkPPW3SDep3aWkrnU4woKCu0Ii6V3a/ySD2tNRo90Qiijmd86ISFcdYXY0YdbXF98mrRnGlc7+gghi6X9X6xwDtHpoxLdejWK1zy9IyX0kW/c1ZZv84GrVXH2t2BOhkyLR8JrUMuRZsm6Yrlb7zC8k2Hde7m3KSptNnFnou5+XYnp1tbtWRuddiIEb0g1ZutImd2mUWkI2Cc5eXqJRaUvesYB6nxGow5oAicb1Y0oed6LY3Mtb7aip6s6pjkNyh/2tfRVSXg4HoOGWTJun0WJM2sQg46zWvpSoWxlTGPZQ235rRjLKuavvDXA3YTU/dU0zHiWNvDBV3lecU0twPdkJXX6wzDb+Wu3t6uTpCGqTdumAhhZ8cqWMi1mmDYXo4rgsBWfKeucgwLFtHomhfiwEiMNG9aBgsXMb4eT3Ihn3bb5a6X6fUlJnD9VggHJ6VJzNLmPe0qbjoOOb2Q5qdLlZHptjujl7a3HDeMNozM1TMzZnVhzrA8M8+ZrKfnpEGdbyfhsull14m3Is2TfnetR7Jqh3q/zKORaDf4MudWx4Q72jOAFGsiuKFKKG2uo06g58wpRkMlaC9bdIcGl0pZhLDBncUrpeHMaRfN2o7YIfw+UXf8EoGtU+SEKeZtqaEn9CImdkshT8hTfzAS0Hec+X1miZkZw7ZEnokz0ujokSG2Nuib0ttgrq8zdneyNhqlE87QLhg60dHe7FitwWsts0t+dShPN0mm0B69LMWIOwi47qPG9mg2Pldo88gcajUyhhPuqNi63tbN4nBd1xKzOXbdqBug392ZJcfttXPXd0fTtzwxCWqU0JurbqdbkpJdHz+KmTxcMquJqJhKRbyw0AyNk3ksdWTTrRTpcM3Ns38jyTx0F1xnyIsysNGrUrj1kWQlSq8jIw3n2zk62HGe6mkRnlnOJ4+UFhMb8Viai62nMpHV4fb6MNf9ta3lBY+6CLepPLfu1xSb8puBZOpqdbDMqZ/bc3CFGvIsslH/OCdm/P6mIetx5Qu1VbJlsl2y6KVQrqy1xaxkGzMLV/MbJlP3zSjpvhLPB1UuVNnTVe3KXkr1QgOOF8qy70T9hi9WQ2ikjqRXV1Gntwh+FngSJ3KrvnAd62SgvcsXrt6wLnabG7Mtz+r1uDkmi1E+DsnsMPC8OHbLnbjgDl6c7pZJ5vO2F8yZDc5eWqw3mUChTn3Db/YVO2c6epnU5ZjIpXvtbWReble81Mg0n+V4jl13m4puQKSjJDcfkpUupyd1FqjWamTELdWc1Zq/llVeo6S5ZPjNdietNJ6jbyYZ+M6JR611Jh74vjfPzFFarxNyiS+NwhmcZbixEWtbXdwgn4PGLzOrhKwYM2KEo7a7qlshZwJ3w1yWgbk9cxLchcp2u1GNBERzduBpLpLqhbA+DJc0Uy4yu9i1RcHllbzByCFXTg2G2pyrj5q9wzEivGpGiOOpWik9dUL3uH2Et7LR2cE2ICw8XJ+jEhXOtJXBuHwRNB8XfGWLh9uIb4NwleHhPiEFuZ/x3kaWrq4VKw0psMm65MhTiR0vxlGtNvzZvojnPI+EVN14uJIGCyyxiiZY1J2z36AVguEHc2USe+8Y1Wc8JIJuO25yB7MtRrm2Z+R6bbxqsRLZrU/M8jOlEmKHhB5dWVEiycpCHwvuXOInTe775Ipza7+C+Vi0moUwO8nz055aCMMcl2YB3ZM+bfX6Sslns2uqzBgQCkdDsq/zcDZ4s6sZyUZE4TB8kjF736pHa4kObSpz6spGQPVxYY1SElu5nufJGY49KjkyR7ewYiHmHNkPgtMt3cJL4pjboMmV7flRgbsbddq2AWzP95tBPF9dWyIMX4hwTwCd5dlmeA4umvVoXVnPP2V92O9YV9qFYHMcUDQOC5cDaGiU5iCWYUWJNxTJPFUpyE7nhC2MKeFhzSayN9w0qTrYJb0xcataaNfzjKlG3t0vfc5XBTsZQEmh+YHoYspywf5p3oQhPrdrENVh5ErR0qoiCtSJqxwvzmC7i8z1ridbsMuyDYW2jWG0C2fOZXYoaFcDQQ7aEiNjTNBpIljSszGhh+NqI4ddhu1BOMI7oEdisJgs8S6rkjM1O+1XgeIqFOmXVeRtdjwc5ELuRgW3tHAyzRgPZmVBnOG4NuJMInkV5w56MGM7Jp8dQ9kJ5J4c8OKmimtna1DHIUoa6zqiYeg2cKjYrnya6UtsI60UN4xDkdBX6ZY423wdqbh8U5ltI9nrSLZOVrbofb3mCW633Jc1Ie8L/nSY8XUwUfscne8r96xExOJmlTEx5hqx4NoM7NAKVjkhsn+rV6tg1Y7Y/oR5vhDUYPvPhR1DeztZ9rADvunzRqi3iJJxOoIzlCCVsnSB1XFGX0J7cPa3fL+AD+xK6133dnUlzw1idKTCpB6sm0XMfTJeH1OZ1lSzKOGGU2HKPC5i4rjitvyszJd75IDR1ElIuUFWrjIpX5oTtoWVa8WUy7EmY5PW+/Qwr+iew2DGgekwgYVEpRv5irA9uXdRDG3oTqPhI8KIM1GcKTROZmAnukYU6lBGglmGYSMLBAvaApOoR8pvAFFeyWzbOYdFU8zgNaaYNhcWMDu3omvo0NzIDIN6S9dYyRbDpaYldqBGWE6NAS3ODNnB1jrg/GZBWRSH9Ew/6hlnhbf1Hsd3m+yCAPhwyWepnTxLb5GDmjzpBWEsgC17egqqsyBxHLLEwU5aOB3wre0E+EaceX3L+MfGJ3hvWdTukSZJN7IadbZHGbZXV0cMHevVxQzB7k0ptnSGSsGam63w85I8rOuYWe6Lw5q4qvFybcCl1ItOZPdEoir6la1A524E1f5YkueMWM+DnktqYnOlFUEOYaXljolmEbbozdZBt24UjxAl9Arc4lFdIXlnKliUuyUfcsT67Btb1ZdLyqBJFzYPEkOrIXlsbnBnIKKXkjOBOYgNC3YkRUsfTolaRelma7mkEu8b1Q51A7Qa5Yy3ZAoPCq/zbvNN6o8BRXFrVLmWmEFj4q1ZVQzD/P3l08t0LP08XP43XhJPZ37/z44eH6eEby+W7sfKYMyX+1pf/h1lfvn0UnsJUOVxpNpkXfQ8hvyHA9XPf/0iYpo3Pt61Tu+8hvbtxL11ounvgl6Swu+ath6/NWXW3Q9zP724XTP9pULz7Xlo/XI3JK+mE/D3pcD3OAH6t+U3wBrJ/UZSTG9xAj9x2rfL6Hmy/OnFH4EjEq/5hpHEt6CuJvue7zWmY9npxcbL7/8HmnP/tXclAAA= -->
