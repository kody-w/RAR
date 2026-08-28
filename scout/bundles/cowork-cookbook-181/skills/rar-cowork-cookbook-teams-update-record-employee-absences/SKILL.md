---
name: "rar-cowork-cookbook-teams-update-record-employee-absences"
description: "Drafts a Teams channel post on record employee absences status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_record_employee_absences", "rar_sha256": "42037663e721f0e989101afd977e0a0d9b6d908ad43c1ca8e58048e789357e0b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_record_employee_absences`. The original RAPP
agent is preserved byte-for-byte in `teams_update_record_employee_absences_agent.py` and in the RCI capsule.

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

Record employee absences Teams Channel Update — Drafts a Teams channel post on record employee absences status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-record-employee-absences
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_record_employee_absences_agent.py` and embedded as the fenced Python below (sha256 42037663e721f0e9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_record_employee_absences_agent.py` first:

```bash
python3 teams_update_record_employee_absences_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_record_employee_absences_agent.py   # or on stdin
python3 teams_update_record_employee_absences_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record employee absences Teams Channel Update — Drafts a Teams channel post on record employee absences status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-record-employee-absences
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_record_employee_absences',
    "version": '2.0.1',
    "display_name": 'Record employee absences Teams Channel Update',
    "description": 'Drafts a Teams channel post on record employee absences status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-record-employee-absences',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-record-employee-absences',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '01960b195cc10dbf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/record-employee-absences'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/teams-update-record-employee-absences', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateRecordEmployeeAbsences(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateRecordEmployeeAbsences'
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
    print(TeamsUpdateRecordEmployeeAbsences().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716abPa2JLtX1Gf/mBXYx80D75REU8ISYAmQAghyhW2ZgmNaESqV//9bQHHdnXd6r7V0fHwcBDaO4eVmStzi/Pbi902UVG9fHrRfTuHRDtN48ivIDv3IK7oiyoBP4rEAf8gt8ibKnbapqjqlw8vnl+7VVw2cZGD7cvKDpoasqGDb2c15EZ2nvspVBZ1AxU5VPluUXmQn5VpMfg+ZDu1n7t+DdWN3bQ11MdNBJRCcd74le02cedDrGeX9zecDbYGRQVd29hNIGCEHfqvwAT/ZgOBfv3y6ZdfP7zE4P3Lp99e3NSuwUcvd0uM0rMbf39Xzz+1s0/lQEJq5yFYWg4AhRxcl34FFGXgI88PoOfV+9pPgw/Qf/xH0ttVWP/06XMOPV+fX6Y/+zaHmsiHmsKuG9+DXLu0nTiNm+EVYtPeHmoAQNNW+QRQDezPw9fHzu+SihL6ebr3/qHkNfSb959fCmCCPUH8+eUnCCDw+aVqp/evk5Ty/U+vadH71fufvsupW+fiu80kDFj9+uV5/RQLFn5fGgd3rT8DqY9gOv7nlx+cm14Puyc/wc6X10sR5+8fgsuq6PzcBkC+/+mvxLqR7yZpXDf/ktxfHoIj3/aAT0/Df/pwB/lXaPZ06JvMv1ZbgrD+HU/A8jd1H6AnUH8l+47/fxKdxjlI5TfE/6m4f7Zh9jP0y1/69l9t+AAFn1+WfgqKo7Kd1P8E/fZF3/LcL++87x+++/V3IPq/FaMXbeXeJXzJ7DwO/Lr58uWXd/X943e//vKuLUGugVL60lbpP5P5z3C96/kDgs9V7/+4F+g38iQv+hz6lunQb0X5b9Xvr9DRTmPv++f1J+jHepleM2hy4k3pA4IfaqYGtv6A408vvwOSyIE3rXu/Dar83/8dUmK3KuoiaCDdLdoGAgFu4syfjD9EcQ2Bv1NtVz7AtY4BsM91IP+nCE8WFwH09f+4d7r86D7pct5M9POlvfPPlwf/fXnjvy9v/Pf1FToA4UUVh3Fup9Ce3W4/54De8mZSXFZ+7VcdoBRnaPyPgIw+Tm8ATUJf/yX5X+6iXsvh653S4wdP7bn1xFF1m/qvk59m5OdPr1xAwv7Nd1ugJS1cYFIQA4b9APyvixSQcTNhUidxmkJeDNSCbjDcZQPcPk3Cvn796th19Dl/kCoGPdpEPQcLvpkDffwIfAvSOIyaz7nvRgX07rff30H/F/qvdt2FTzq2gOGfUQEWbnRNhUCVtRlYBgIGQgwo5B6V335/IgzE5KCvgRjGQew/NoMsTXzvDW59xX5ECRJyfAAzgDgri6oBTA3FzSu0DqBv9gKl062Jy6OpvXl+6ecegHsAUm3gzjck86KBapCKdTB8gNrav2v96lT23cQMlLvdfIUUbgs6R5GC/yYz74vA5iKPAfzfkuHxORBSvauhxZuIV0id8hIq7couo8p+6gjsR1xAx3jbDoTbUO73n/OpT/oTVPciecADFgFk3GdIP04xB/0+A4zg1W+672vsqb8d7n2u+pzXzwKwK//e4oEpAxS2sTe1hX88U6qOijb17vgBSydJzyh4z6jcc3D/VxPCY6DgngPFo59Dn1sURnDo///UMZnKiuKeF9kDv4R49bC3HhBO49EE9WOiAr3/vvleLt/ngTc2eSPVz3kag3yohn88Vt6Bf655EFVbAZz27P4uH0QdQDjJvSfllGRVNaWz/Tl/Y+8PAI47VQEAQAWDDJ8S603hdPfN0giU6XT9vZO/IQbCDhIPKlsnBUkR+L7n2BMGUTUV1hN8kKH+VGR9FLvRH7yCgHSQCED+FIUYRAgw/B06tQBugpoKqiL7vjye5iNghde6wFowf/qvkAlqY8qPGhQkGHKmNQCFd3dRUOYDjIGJ3xCuI7t8GDONrE8D7SkWRTblyw8ReN78ns13WybzgVQbZBfAsp8o1vNvj8h+s/MZK2BsNtXffdMfw/30Ffqxzfzjc3638Rurg7JOpw79AzgQSECQwBOPTqxUA2bJ/GcCgUy4N+PXRz99NOxvtnz605z+/u+N8vcOafwxcp+gqGnK+tN8/uhqb03tFXDCHORIXPr1o8F9fDSgj4/E+fhWah/fSu0Pwh9YfYL+noF/EPHM7E8Q8gq/wtMtOXYnTW9dHuDBfVxYH/Hp7kQr3wP9zIaJVtMBdNRvPeZtCWg0YeWH0+JHz6mnVtWD7ngnWRCKz/m3ZHiWysQ54dQg6+KHEr43WxDaR+S+9QJwK2+Abm8a0h5nmHQyv/ZfPuVtmn54ye3M/xfPLhPng5QFgEynHlA+YO5pYv9+9W0Gmi7+eFK7FxZgBK/4NNXXB2iaVz9A30bPD9DbYeB+xMpbcBr6ZRp7J5VgKfjxbe23Y6Djv4ATWDOUk/GPE840bT2n4D8bMZUVsBg4Uk+2vNXppPFPQsCbMPSrPwvR7m/s9EkWgNSnrhw3byVeAzs9MON8gED4QOmBagIk2YINf1YD9FQ+YHrAtpO73/H77lbx8OX3OwzN45j428sbaTxj8BwJwXJQnR/rqQHOQaoCheD6kVTg3v9sWHwKAVwH5hQgBUdhjCJJzKdQJIB9hmYQGLEDj6EoH7Zhj3FIj4Fp28MxF3Ft2idoGKd9imYwAqxwgLxHfn6ZWn08GebDgY8xCOp6GIkSBM4gFGozno1Ttu3BNE3BVOCBdvB9awKI8untw7sJym9z64TK0+nfXhwSBytXeL1mHy9uzhxtyqIcNXIYigzC64WmYaYc4AY2r7I2kqvdMOzOBRwvNs0QZ1FSbhoF1WSuiNX9trPW7Gy/mfUHSs7pRNPPLp2Q5vpkb7isSSL/1JBbl56lK/60Jzen9XEDj7WdSM3e5OijLiuRZnd7gS6Y/JyVfiqpF+zokqolz+ezqKFOWy2FrZESz1lg6GmTceU5OHus40SlKrfmuUbwwdyXewUe1yTNazRCnA8z19Vv3rW8Mo65Rwejb2ZGxRfMqoRJvxvLmd9d0vmoEEG3yhGLHv2KPcmCqBtRtxIrwWhGz2pVs95Up4tgIPlOwfoxU28G2hx2vnBYN5qDMKXotBtd4ASlL9xUMfDW7Q4lc3aPo2mBAbE0snNNKwvVR25ijtsKsHh/sA8iJ0mIAKY95SRVHW9ftzZlhjAp55mfYMEVKb34LC+lWrA75bbyVTKJ3NEyipAmTgda1Q8J0sapFB4POmYzaZOSxNgrSVs3g+5UOhaJp7Pbo7tWoAmjaq7jsSxbJWEsbjbz1MUFOxWRdZuhK3Vpt45RqYagXW2iXeLW0K6d3b7OcMbuZwVSEX12rUj4motDx5Q7f6vXh1ipWH8b+T5prCU4usSaPtNC+xgzI+0SRN2AqPWe5GQLkiDOHjMvDlZ1HAV6aFc4WjtFeDTVlOyGCOdqDxUyca0mu2q5hpkh6VQkKy6BPLI0eS0BsvAtpZwLCccuZmeUsNqmcqnQe5ryY3jXJbNbZB2YSjlEwmqDy0fNKj1nlWxzprrOM0dElNL3R9O0Tuec8HIpV5cLPpJIIY+qTYU2MZ1RRZ9ZdpIVdkLWDXour+MF0TqZFlb0uWcuizm/HJdD5d4KcebM+8U5h1Fmlm9xNew5bazgGcsdzoHb6bKnnmW9vZxRQepTvzKvt8LNJKbU1GuMLkVlaaUCPtr8li13TjzwecFh892QWsRylRtaSG5lI8oy5biznQ283Isld2EvOzW56omkbvqEskYr1Hg/rS8+JxHxcPWPR7U6FGO+jO12K+pOvxdvCE0R8LD0iNuKb/39TczOizWd9Lp6kemTk4R7ZpnVs6XCjFe75RxC6wc4iMDhltfYLbUMqHm86A33IKy0/OYi6xMSXWn4mM6UcGeoc5lRG66wtcbD+/pcFr04N2OXlbW4IvfJzInLZQ6OjoXGVKbV8dLqIuILhal3gR0LIykGeyY6LWG8U5qcY8c8GJFhoHXjGFwiz7328+F4rTy4akj72LbYUvcVHe8Npr2tQWs54ElmGWxjXW8WyfvGcWXO97MrrLMyPOx6MyKY1UlYS2MqtufWGdZzQFao0qK6cqjPCLNI0j7euON2YE/JPsWOsEhibZ7mW0oiImO89Rd7Fx0P9vUUISm9tKxDKZiZfuIVJMVNPbvot4G7cnSa1IfZbLjFuyA9HWxCEuODSM8DZI1anqi2QbwZz2TsXRZVN/ZNqexinx01p71yG2ZYlAEi9gdSks/JqdqGkb+ES3xOW8HC51fMLI4i+hTPrzq3ExJK6g18e1loSrvXV91mc4nXyoZQDjeURy1BV1Z7YsEQ9rDmKW1sQmw7bmqrUkiDytS8DbZYrZsb6yg5dkccNyfBK0icpaxiwy5wnUIWddc7e10ygrgVRdwVNE4XNuYaWUhqK2Fn57aHV5y+486Scdx7XCpW7HA00Q21vMhK7+qJsL7ESkvzy2sWsUwe7YLVdjdr19J+AzoqbIhjujNvaNNuz+bxWnj8Oc9PGAWspW9+M/JhMpTOgTcdb36QCkHpCC01r+NmJrBnVYxATc3m61pMVAxdybXM33bR8kbMGN9cMppwOqGHc997RNvpCzzyBNkf7dSfKctdFgrabU3ubk3eLTiu38jtcZQqLmHdTmXOHIzbWb9u2b09eomsCLbiLMolYNk1TZA4lyWFfbzKfaqF9Ga/Q9c8jZ8QXUJPcKYVyzDojKuUrBj42PGNuWOxbXiNpJ12OQ4huqvoIeWW7UIOl1dKubkn5GoYOzgp2FZZmOuBksyzg57H0k4lp18YmD3r5NMZnvELPtQVNZula3NxxppzOS4OZjE2lclfTNFEFhQxCqYvq7tcbfAS0wi2suHOqR2Xz86VN4bJbg8voiFTK/MMZ13juWMTMXi8K7eyg+fwIJTs4FWrmOFxd0mJY+xmfLKl+CY8h3rv0BapbL0DKoYzdHGQ1+BQdQaDCq+tXG+O4hGpz9gbu9MFqQxRW8XYFVxzHIdlVUTF1Ggu9FigZcNoEmJn8JLe7UwrBkxzHc7kLbx4adM5Q8Ia0sa+6ovDpbCZbWJUwhlfwiNzKZYqbxwwakusOpWsdpUdxipWW6C9ifXc8KWWgHuhIfqWOJxIHi/4ALVi65bDCKOGYiSdqhO6cFok9b3jqB+3R/iytDrmdLwaEU1gFiwmqwKTSITVutK3ZgdFzsqjiFnq/FCkG1K5yY1yXFvM/gbSZKXbh9s+ZKqhhU+Mpbv4HrM2RIyIhCmvk8RcyPpJSvaOyIfIctwMaLbCvJHcMWpsJiK3HBkHm/XyzspPJ5cQqzxUdhW72HjYxc9CDNtliIEcBe9wTHBvNtOCUsRowuL4zEGLhbvzSauhZ+tLhLbtZlPNBbVBLiRjn6SG2VZZcIzxXL92JoZpmSaOUXhjEwotqkaw2INmsCtu0aKU4+wQU0aPVoAt3PIYiX4ZbfkSDEb9vGCIfBTrXbdeWIWp5SfZpMdhVWjeWkcuXFy0W2mlcgnGwrJxLU6dgWxwouj2hti0uVies67mR1YW2TFqZ+cTn+rquZbLWMvcoxVVyYW8saXXSsXapfvuSAgOK53WbMyFa1EPPTdL5vEpWOvnwEE07jDW62a9olspQM8KPngHcPB1UaxUtAjdGdg1zmPJtZx4cwhpejCS5sJtYqPZEJu+XqhnYW/QBiIsddyNruWgo81ml3jyaA3VcUvt02i2MPGZtdM0yswYzeO3vcXVV3NUerOoyFm94ZDTRp+5+1NcVZg+UIx2JhM23WUNRxUqusxvBHq4oqGa1jWqOrdGPx1S8rIEXa0oO1gg+LNWEoI5+J5TLbiLGntzKS3Q3EepmS50Y8j5qi/qm1YGXVsCY0xka/1e48NdiXnKbacJ8K0odRM5V4fVXoiRnMXcdbpViTOCrS6IMwZtI26G5bLtsg4X8wPM3JqIigxvpS6OFdqWtpjsVFJSazbfabOaFfWl6m2GenFKWoQ7jueZaUobfFj3Q7zfE2mqeSZKNWw226sXQ9ubGOiaLWNw6RFMgeGauShwtr/IZJRwlrodNiE9EKVq3BZYnddzgvA53h0pRryNMELu3I0vrPWGUZSVuo83ibTIikA6Gv5qt8TqczhUJuMDN7fogiHVbak4oSptiUHGmSVdU94pUq46GIK28phFVn62sXoDDxTMGCS9o9sqPi/ZPqYW9PwWct1FvvFSQ67PGsybZUdy4aU0Z8lF4ezTcr+Pva2NGeUQLiQk43FrtQil+rJc7GK4XkXN0eas9b4+XdNbqbXILKh4sYqJgl32LGVjvWMVF/dSyxZfgpgJ9sjN0GVC0FZ8LCzjEJn+um9cW+Nswzwp61GqszZoqmq1CkacJDdgsDxut0eFtuOqlol6n/LGQk6lbZZWhdS1EZdF5m1m9F7kZxFcwxUaY9x8jc+9q7agvKPddF5cEu3qWJUGg0Z9cDp3qNNZnde7x55wCQ81F5GDDviYSclOkK+522peeZOkIxxLIElseT1ne2I1RhGGYNtDGJws9Zg3SLtnOHB4uwijKp3X+X7V3Zy+i/ibxWKs3UubTr3Bwuy6HTRRCHvqupgfCITSaXFWSjhJ8TlZMKe4521sgY61A86RPtGZZn4pRpWSgEmhCPdzrSAwtsEELCP7VUHT+nzONMj8JlB61fNV083xct45Opp3njubyza237Vl4O/FpAtPaZEUeLy9ucyBO8jDxRoTsyUozoN5JIFxrTl1IuCSloPXg0vfut0lXvYZAzt71xhn1ZrUPMLZlMeawDDlxsp+qY8uKV5Gt7dbBF8mLllTqerT5RkTLWGlXMAhZJhdWom2sHRYuMteoACb4OEcdmFs5Z4jwzC7vY9xq4GiZLtLZOYAToK6KFULg5/v4Gg2dE3H9mdOEzotas2LPezSKnD2HQhMkBYYjs1BiujbTDgizYrmB54/obWqdsVMiyhvpPMyWbfgrOfVC+vGxnVl3rKmotBTStUic1K5gerpxGZwKj63M+/WYoPo6GuJXmqYH+ENKga1FSU3r1AOph7sUbjurItIWvNchpcI16954liS9MVL1FovuiOM0x2uwpZ8SwXenQncmC8c/RZR8BIfDujyHI83AVuhu0Bj+2MlOjA4kwoCmOON7erSz3zvBma07ZH1dNtN227UUMIShAV+KDlwCvE0TFus65UWD2Jhygg1eMZVJJaHVs5PsJ6LHiKjy6Cqrlgz80lO9iKVaFGXOcrKaPVmjBG7JmMCpou2uS7SXp7xwZANKDs/wTahOrljXoKOj/bLnBSLHowyq1693HohWi4wHK/3SX0C8yd2bCgfp2/OiJnYPmVbM+4pKaoytRa6PUEeZydNVREGu+JHeTcizpWuVwJWL1YF5XNLhe0XQjWLV8vtTm/H+rYuloMSEMIQgAH2tKG3q3JbtINDRhlDbBcu2iJ9iEWsvfK6Clv2oDooaj7PKUeeaeSRQvAjNkP73WpGEfNGiohIZK6O0IGekCIzfHvWBo+7mJ1IVURNMgG2xcw102XUtgDHBWZ+jfgtcYJXDZMhjKwot3SbrExeKkJhm+4db3nO54nrLK5qubps7LbV2xlX4RjFM0sYZnvJiJhTMMIwhXKxgDfYqnfbdkfLNkUc83a01UZC+2ZhdyLHCaeGxlk/ws40yyLivs/jXQofzjPiZvN+tqtglVjKBopRKJxbebFn5JvF9QvewYxZPiJsXuPB8rY7Cc3hFAedslVYB/Axruccii40pz8bZ2OLqK2ehaKn6fFhuRoKh/UPq3IPb9Ca8DdnSgODATg+eO7JYTFqjoNJu6bKUxhceGSFSgedCW5WNM+EznNgpepQt9xqiysHyvnMV1eYd5v2uDVPYnG4nqhh5wdgTO59Cx7oVR6qcEKqwnmgC+W8gQVDZg8VHYXVvEjkjcK3NDy7tUoxDwJkMa7W9smpDMJ1I3Q7DxUlTREw2yQsy/7888uHl+nR9PMB89/79nh63Pe/9tTx8YDw7Sun+8Nl3/Y+3XV9+pt2/frhpXJjYNXjGWudtuHzYeR/esL68V/6tmISMTy+mp2+I7s1b4/lGzucfsvoJc69tm6q4UtdpO39Qe+HF6etp193qL88H2i/3N3Lyunp+I/ugMsorvwvTQEca8C7l+nXEaYvfnwvftyfLsPng+cPL94AghW79ReMJL74VTl5+/z+AziJvsKvyMvv/w/M1CkJwyUAAA== -->
