---
name: "rar-cowork-cookbook-configure-maintain-and-update-the-business-continuity-plan"
description: "Applies a bulk configuration change to maintain and update the business continuity plan from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_maintain_and_update_the_business_continuity_plan", "rar_sha256": "620470dac2c3b06bd9fb6fa326cf0baeac659f36f5a9d13d7aab4075e12e133c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_maintain_and_update_the_business_continuity_plan`. The original RAPP
agent is preserved byte-for-byte in `configure_maintain_and_update_the_business_continuity_plan_agent.py` and in the RCI capsule.

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

Maintain and update the business continuity plan Configuration Bulk Setup — Applies a bulk configuration change to maintain and update the business continuity plan from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-maintain-and-update-the-business-continuity-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_maintain_and_update_the_business_continuity_plan_agent.py` and embedded as the fenced Python below (sha256 620470dac2c3b06b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_maintain_and_update_the_business_continuity_plan_agent.py` first:

```bash
python3 configure_maintain_and_update_the_business_continuity_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_maintain_and_update_the_business_continuity_plan_agent.py   # or on stdin
python3 configure_maintain_and_update_the_business_continuity_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain and update the business continuity plan Configuration Bulk Setup — Applies a bulk configuration change to maintain and update the business continuity plan from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-maintain-and-update-the-business-continuity-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_maintain_and_update_the_business_continuity_plan',
    "version": '2.0.0',
    "display_name": 'Maintain and update the business continuity plan Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to maintain and update the business continuity plan from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-maintain-and-update-the-business-continuity-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-maintain-and-update-the-business-continuity-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '564455039af327eb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/maintain-and-update-the-business-continuity-plan'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-maintain-and-update-the-business-continuity-plan', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureMaintainAndUpdateTheBusinessContinuityPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureMaintainAndUpdateTheBusinessContinuityPlan'
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
    print(ConfigureMaintainAndUpdateTheBusinessContinuityPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZPiSJbtX+HFfMiqVmagfcm2NhsQWhAggQAhUVkWpX3fd2rqvz8XEJFVU93zXrf1hyEzIpHkfu/1u5xz3ZW/vphtE+TVy9eXo2tmM8FMkjBwq5mZOTM27/MqBv/ksQV+ZnaeNVVotU1e1S+fXxy3tquwaMI8A9MXRZGEbj0zZ1ab3Md6od9W5vR4Zgdm5ruzJp+lZpg14OeuoC0cswG3AxdMqsPMreu7kjBrw2acFQmwyKvyFAyehVnRNjNusN1k5oWJ+3nWh00w68wkdB5KJolVniSWacezui2KvGpegZ3uYKZF4tYvX3/6+fNLCL6/fP31xU7MGtx6YZ+GurunZYvMOd/tOgXu8mkV+2HUHtgEZILfPphcjMB503XhVl5epeCW43qz59UPtZt4n2d/+Uvcm5Vf//j1WzZ7fr69TH/UNrsvvsnNunGdmW0WphUmQM3rbJH05ljPKrdpq2xyaw18n/mvj5nfJeXF7G/Tsx8eSl59t/nh20sOTLh75dvLj7O8Avqqdvr+OkkpfvjxNcl7t/rhx+9y6taKXLuZhAGrX9+e10+xYOD3oaF31/o3IPWRA5b77eV3i5s+D7undYKZL69RHmY/PAQXVd65mZnZ7g8//iOxduDacRLWzf+X3J8eggPXdMCanob/+Pnu5J9n0HNBHzL/sdop4f6ZlYDh7+o+z56O+key7/7/b6KTKbk+PP53xf29CdDfZj/9w7X9TxM+z7xvLys3CTuQHVbifp39+nbcc+xPn5zvNz/9/BsQ/f8Uc8zbyr5LeEvNLPTcunl7++lTfb/96eefPrUFyDXXTN/aKvl7Mv+eX+96/uDB56gf/jgX6D9ncZb32ewj02e/5sX/qX57nWkTJHy/X3+d/b5epg80mxbxrvThgt/VTA1s/Z0ff3z5DcBGBlbT2vfHoMr/4z9mu9Cu8jr3mtnRzgE0gQA3YepOxp+CsJ6Bv1NtVy7wax0Cxz7HgfyfIjxZnHuzX/7TvqPsF/uJsvN35HTf3rHyDSDb2wMr34DIt3esfPuOlffk+eV1BjALlHvoh5mZzNTFfv8tM303ayZrisqt3aoDOGONjfsFINSX6QtA1tkv/7rSt7v812L85Q7A4QPRVHY9oVndJu7r5JFL4GbP9dsAzN3BtVugOslt8wHn9WfgqTpPuokOgLF1HCbJzAkr4Kq8Gh/g3mZfJ2G//PKLZdbBt+wBv9jswUP1HAz4MGf25QtYsJeEftB8y1w7yGeffv3t0+y/Zv/TrLvwSccesMMzfsBC6ajIM1CPbQqGgdCCZABgc4/fr7893Q7EZIA4QbRDbyLCaTLI59h13mNwFBdfUIKcWS7wPfB7OjEUwPRZ2LzO1t7sw16gdHo0oX6Q183McQs3c9zMHoFUEyznw5NZ3sxqkLS1N36etfWDS3+xKvNuYgqAwWx+me3YPeCYPJkIuHpyDpicZyFw/0eGPO4DIdWnerZ8F/E6k6cMnhVmZRZBZT51eOYjLoBb3qcD4eYsc/tv2cSx7uSqezk93AMGAc/Yz5B+mWIOuD4F2OHU77rvY8yJCU93Rqy+ZfWzVMxqCoUNqAMo9VvA+YBA/vpMqTrI28S5+w9YOkl6RsF5RuWeg7t/tvVg/9DDLKe25gjgqJh9a1EYwWf/S1ueaa0LQVA5YXHiVjNOPqnGIwaToilWj55v0gcS8VFv31uPd+B6x+9vWRKChKrGvz5G3iP3HPPARAAbDgAb9S4fLBTEYJJ7z+opS6vq7qVv2TtRfAYuu6MiWAKAAFAik5/eFU5P3y0NQJ1P19+bhnsWVM60dJC5s6K1EpBVnus6dyc0QTVV5jNCIMXdqUr7ILSDP6xqBqSDTALyZ8CIENQaIJO76+QcLBMU5T0KH8PDqRUDVjitDawFHbL7OruA4poSrAYVDfqpaQzwwqe7qFnqAh8DEz88XAdm8TBmaqqfBppTLPJ0SonfReD58Hs53G2ZzAdSTRB74Mt+Am7HHR6R/bDzGStg7JR2jyj9MdzPtc5+z2h//ZbdbfzgCoALydQM/M45M1CPaX1PuQnWagBNqftMIJAJd95/fVD3ozf4sOXrn3YSP/xzm407GZ//GLmvs6BpivrrfP4g0Hf+fAWgMgc5EhZu/Z1Lv7wX4Reg68ujCL8Au7+8F+GX70X45d4G/l7jw4FfZ/+c1X8Q8Uz3rzPkFX6Fp0fb0HanfH5+gJPYL0vjCz49/Zap7vfoP1NkAutkBOT9wVzvQwB9+ZXrT4MfTFZPBNgDzr1DN1jnt+wjQ57188AnQLt1/ru6vlM4iPcjnB8MAx5lDdDtTE2i7067qmQyv3ZfvmZtknx+yczU/Zd3UxO3gMwGLpp2ZqDKQCfWhO796qMrmy7+uOW81x8ADif/OpXh5zt6fp59NMOfZ+/bk/s2MGvB/uynqRGfVD40f4z92M9a7gvYJTZjMS3nseea+r9nX/5nI6bqAxbbE5BPDPgs50njn4SAL77vVn8Woty/mMkTU+rGnNg/bN6RoAZ2Ou3EACCgoEJB0QEsbcGEP6sBeiq3bAHNOtNyv/vv+7Lyx1p+u7uheWxcf315x5ZnDJ5NKhgOivhLPRHtHCQvUAiuH2kGnv0b29enZICToEkCokkUxinYMW3UxiyYtBzGs0jPxFDS9mDLdE2bJBgPIz3CZBwEcyjTtHCYIlwEdREMs4G8Rxq/TX1GOFmLmqZN2xSCOwxlkraLwRZmg/GIQ2EuTDCYR9MuDhz3MTUGIPt0wWPJk38/OunJVU9P/PpikTgYKeL1evH4sHNGM63L3FKDLVQl0DBg5AE7F2coK7Cx1Q4DplGLaw4f5XXFJp5f2aHWrHT+aqWxeEWCfAWFHcXOCYm8YsdzcYxTk1mQ+NLHaxt1sivkIakqRJtlziRVmdPafL0OZDm1EzPUy2jYboY2WV3C5nBujripuwyX2g2bSU1YOI4sXZqG7YR+NOecjZyxwosQAplzFy1LL0kc1Cq9JVUCtDwiLzSjjG6pJje7jcVxtcNzaGMFeGoWdiUeW6mVBGRohq2uOO1ZWRuoPnpsdtqgglVHqiYajHBFGIZxb2FJ7XQegdbhaHdZBnvhYOMRTqjqEYnPKLNTTbc5LTRJZo+HQruVmUQF22HTbi6Is7Fih9CL63gpMGwQjsKa45YcYsqEvhm2yu1K926DHLSa0ZDtktIMftCqzVbVgitZXHrGt8pWu2jSXB5jjfFl0dAjc6Wv2yuPHjBIT6zkEhyHo3QstTQsIxOf9x2fpUpwrorTBvIoeBngfXMmApa1dkd5aB2rs9o1zRJowHeLAw9HGo0ttRM6KEtocKqiC3XhdGx5mtqlwbW3wA7V8LauCqrD7PMyGWtYht0VaaBG3PgleTubjdEiQhLjxzOCDqa0hS3KipcrtIHpwjzoCZ5FcXAUyj6+sYgoIwsSvqR6VGybTiJweLm2IylLMuwGBU3Y3HY6IlBdhPhoezQAc+g3nSUClMOjPLE0pJLmhFXidSpFTV1R7Dh0aVhosJQfbvMk2tC+zdmyvj95qZlnc7w9En7YzIPjDmZ2th2MakxzeZdfrU2Wb7Nm3qJp3sj61UH3RZt0KxGBoO3ZErye5eFS6btlQRoBtjFws61Y61AGxSjaRYLip2NmQ75NYjbGo3RmE9DScUccipQ5z1CrsTnjWmtS82V/cU4DA+3nMBeSclZWCsH0hTw0oUScKaORpcS6uEtJEivH1C+qNPbkZbCpdhVcdmZwlRyVHGzolPRKHeyMaulCzhIea2oXVjx9LgLjcoQvcn7byU7aGDK8ZUVWk1i5j7nDnKMMv+WcBF7g0JYIN+WVT5TLtb9awSBjYh40fVnhNOQMprW8Sug1Ttl0qazjW9xLVLHgduPFSdX1CDPhjfHzlAogNaz3txPfHqir1DMi3SCWLW4EW/Xm0dz01ns4KvZSLHq3wlvNk7Ld6lcvKnhUyCJtW3GpBUU2fT7uLuMukEkLP9nz3ta6C7OJkV0HBzUJtw13ho6X8pRKEpOqps9DBwOwu4uhbbaf5zeUFo5KpUsDwTBpGZYiC9FXNssR0jJhByFdkCwemseFc4yRvOqicRysQ06zh6MGlZmaWBtpU1JFmHeXfqOxUYgcU+niqgR0smnoArfVWdVu8dGhTyemNfl1M4eMjXZdVkuto7dEvh1KasM6+45Hdl7iGYQ5bJZZ45+7pZKALgclkfXiVCQ7ThdzHkm2GRK1h1u036B8mmhjRG5DnChYgQ6RfcZeMLPf73TN3KXYtYxO2Cnlt2e9hORVGyytRW+ThyY5K6oASZmIyb3OSKtrh8Tk2aGxVGVS6HKtPB02FRHAmxbM0Tg4nwjtYFSynG0WiYjkqai3SYTU7WLVLpSrQgw5Z5QaqvTeztDNijvvlYrWVzdabxeHmy8UoxPtxYghuZNMswPLGrZ15vdJu/Jpflzt1vyBLc287UFIN5q9iG+cddlmez9uTwtaqfymMnkuRGlbWeT5svVLydCKk7lyJECMoBu+ScmqlQ7sNtDtDlTo9SJvVq7Q7pQWvzIGkq7UrVw6/C3pqGRlU9htj1lSahHGrVW6joS9jI8hWx+W6/yGhHILUW507IZS0bZnImoWhh1Rsalnvk5CnLtNRE/fQQN0CLk95B1vpxtFMLJMiYAEq4iCyB1TkirGW3hlSjuY0hmr5uogg9kdvy9PxLm9Xs5apZWEpqTDrbBF0vAxRVIC2t7m/Nmec9x5mVcoaaT5aMSQE1DrbA3hyfmkXdu2gCP9DFd6FUoH++yXBppTRbo98oZcWKYZCOxANryK6TFMjsPxSJLtyt5bl7PV+DihYJIp9JHirrjW0kkEk3LnrLWRpRyRpDOVFIe3dFa6iwNL6daGwLJCiiz7UGxTCDVYwjYOlLZFAjtamt7GkE5blOLjYUcLACWOG5ZZoWZL7BsJ0dP5qsVj3FCEQIjkZa731Cr1/SY/LMP0WIWhpTZOCS16pTKzK+xLNOduAkIa07rjDcnTqxPma2iEILti3cNc3hxMdjhpmKQFzJKJsPqWbuC06a4GCopjLdQLZy4kVdozJ5XvqjojS03UAFXEy02M4msp8Rn8etmiPmglNIzluLk8HOh61NTBBU4sWRG/1avj0h127YJxN+ooaKdi2e1XFJGdt+o2O+y7PQlZp2U9sGjQSwWZHXeiOqw8uavTOXoN7ahgL5zpZYMQrtEcakmNLi+nnZkEZ1MVJd1DnVJI9muLdJayfWgxPVrDbbmF3Wt0MtVUO3R5R+haePbXtIDDQi4W2d4mS2Uwc5XYcFixPfM+XXBOxgjHmFsOyVYlo9imtUsHdyu7klTtEiCorNyClRNkqRUSfK9Ka7+UxXnGh1qFLvx8s5QuVKMoSEWq42E4m8trnkBiiGKqy7AIQyqqTVDmeiGuCBmJDXnVK8T5iCpe6o83GDvNFb2LihXrqat1LFBrcifpNxB0zxDgZucWikgcCGtP0SN6IcgduqukmEzHtkON1SGwiuMi6tlk32aCst5sOO6wqGmRDljb0SrQAO46lJMSqT4gyH7AkxvBuBmveMrV0NYCs24vfNw3ML++8Pp6xA9JsxSqc0lWNX5eKYygL8Ii62x0aSJWq62J27koebTcSRbO+fmWxbe45ZrwUs+zo3ZNdmuRvjGgy9BXyVFZZbnNyPFNWex21qLhjJvNEHEIzwepO6u7tglT9tBJldwLdetu+oTGh9OCCHU/2p7stcktR8EPa9aYa6dEGA+8HXmSsFNs5KaZPBqcVHg7x7e87mrnuawko9Jkqmj5Ja+nLOVvBDy66o24EUnZSjU2IdBx08GMeokXjXiFHVS4aImu33ZZ6Rz5WzGI17FsmOM8N1PQc9lnMb7m2G4JJTadXfiouJwPKGbPMwHrvJN/4K8jSZaedTXmZXVMSUxAHWcs4B6H+tAjLkCezIzjyAx7qmDpkqgWpSdzIpdDylIs06AXF+42jsokz/ebW1ysEx9fbwJ+KLMFZUuHpUHk+0uiEqqxQUab3o+ARB3mtDdal5KoA7nShtLkrrxijcVZNQ5cnpgIFSFLKiZukjD4BpMrp/U110grJoUs2MGleApT5bguRMHRc8TAMVdEYV8Xd1dUHrSgx48pb55g/hbtFFwwA2Jf+ttSbNiyUAs0Ha1suQizOWLoYbI8Orh4Hdrrfl0et/51dRIL3S/4amW4wXmzChvzOBpD6597UbOyiAtsB1cDC+69A58vYzN1tCW/9g6Z1QIKOh5zzjKccX9TAmvvOjfN6k7aqYI5uRLWa2fTg/aiVoZ84RWmld7O8nGpy6UK1/RuZ462sY53IiE0CH25xpVmHM/Dwlotjd0ywfM628jyWRqby+E0Co40WHmJFE7tqoWTG0pp8/mChRW8wvBbQFWVifVLja3z05GmcMjGE25gLqyaI4neHpR+rGtbXh5hvMHVWLvyNtPPh11gZ9blyjMjulB9rzosmNuNb2hIdY6es9T1hOHy0JcqjYkz6wzvfIpvgVvy8Mbtt2v6QmmkSgVeTp+69X5JMmVReVSjk7uF3NyIrt728zTxYIKEdAhPN7iN0gfFiYzL0LX4OJbcNkAteHWuEmUorkJraO5ayu2zvag4zcVSg3IcJYAop9oxaTRy8YjS0k2+0R1goZud5TE2cgN/3K9qAs3FBh0uvL+AbUdZwph6ERcY717GXlF0HcHx1allzNO69xzREYYMJtL9mq/lUw9f03mmu+5hZQf7U7tjEMyFGgiqi1HZ49icIS4evZCiBDSjTIZB6wwhfZdsKEckEH+gtoy/cQ8KrdHh1iyl/Romt9tQjxangLHPtOnBAhTDh5Vq465Ery31FNxugnLIDDHZEDkawkRUX66kTaXYaUM5Ny9dhpJySTfNrTT3y36Ly02yG/yzaHdbLNkrO0qTpMACOHiBHeZQC/RV1Wgl7qpw2x1k1IEi3EqrjXALV1sI96H9rala6CCSJMMWskHGLOhO/G3giY1CK7aQrVXAQGce4ZiWXZoCApereC5q4vwyb3GTPo7Fhl6dysW1ZiVmt08cZ1WdM3PflUYyIhSlRWG4PS/2gOOVW2NdMBo0aKWBt+ludRPmFxDvCKMgWYEOK1FVTj6BUtieL9cr+pRsgm3IR064Zjj9JlG80R031JlZeX0sqGhoZBS5HY5wsKUZ/XTrhaXoxS5nOBKDa8LSjhoj3ruDJ5y8iDpuXElDsGwngtZCCyuSjQOOnpf9YS53eu156kmsvWbhXNhCUFeYi9rtalyTfT1eDlK7cDb0rhZ9v0e3+SYc5ntyyTpqG/IcMxeuaCJvMz8ZGBtn2htmakYod2fyljXBNYxAg7TtEgXFEN9Zb9ZloHcN3kdz1dmGMI+I0K0kMKfGKH+nj5GfIf2OnePwGolxcQxyk97aq5QWBU0/uZ0WLWOcIExQc6W/CvJaQGOSTKzIg9t2YOJTpzlLZe4dkVFoK1BwvqO7OOFWDT7skNUiL13YqlOGK5YOKuOLnRbNN3t1OGdbYq/CzPq6ULSTtp6X5EDKlUODzcpCAL0JFgV47VlyM1cve9dqmznhWabn8jJ7E/vV3AN9eXOg8xCqoW1XZv6u6WiFgxmn3IkOnI6HDg9GjlpR2KJq0BtGZpf5aeBkCKOXdSd5brbkx9AKo2whdT0vR9rJWdHQXBX3l7LHb2ofnbElOwQQUtHGZWEuWIMoTWhLUcz8vFypnaEX45YbSD6B1ph3KWltbGk4OqAVufCbk9huFmJ+Rd3FQlZ9W8Kbm80JVmtcfLGIN8zKXYyI3ECMLA0reD1vksOqX64P2AHiI2Qv1pIrnnBoNNGOTee+o/bEmkX6YM8POUvfhr4PyzlnEoJz2OG7Qc3Kk2+gZ6rcH/ICccOklDH3gAmg6fccfn/YdiKmkvJ6m3e6nS26xkbF1k55EguGVDEuFWP7YP3FGCj2SpIjW9MOThozWjOadExrC/k8J03Uo6rUWWGS0g0DvpIXqoo3CtjEhIUQ44c8dbA2ZDtVgvixkTpZxLvr5eQQWZrtjGCUu5VIBb0yYMzyFhkqG0CbfrF4+fwynY4/z7j/De/Kp/PFf9sx5+NE8v392P2I2zWdr3ddX/8dxv78+aWyQ2Dq4/i3Tlr/eST63w5/v/zr71smuePjlfX06m9o3l8sNKY//c+tlzBz2rqpxrc6T9r7wfTnlw/TnwfwL3dHpMV0mv9hCvhuOmmYhdML5bcmf3uciE/3gYlulbpO+P3Sfx6Wf35xRhDv0K7fMJJ4c6ticsPzLc50kjy9xnn57f8ChPy/JEAnAAA= -->
