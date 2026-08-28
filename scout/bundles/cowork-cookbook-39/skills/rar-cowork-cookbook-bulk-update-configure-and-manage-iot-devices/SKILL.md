---
name: "rar-cowork-cookbook-bulk-update-configure-and-manage-iot-devices"
description: "Applies a bulk field update across configure and manage IoT devices records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_configure_and_manage_iot_devices", "rar_sha256": "0e355ebce08cd8587a26fa92dca58349f550f661a5c36b7774d25c6797ba3c6e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_configure_and_manage_iot_devices`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_configure_and_manage_iot_devices_agent.py` and in the RCI capsule.

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

Configure and manage IoT devices Bulk Field Update — Applies a bulk field update across configure and manage IoT devices records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-configure-and-manage-iot-devices
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_configure_and_manage_iot_devices_agent.py` and embedded as the fenced Python below (sha256 0e355ebce08cd858…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_configure_and_manage_iot_devices_agent.py` first:

```bash
python3 bulk_update_configure_and_manage_iot_devices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_configure_and_manage_iot_devices_agent.py   # or on stdin
python3 bulk_update_configure_and_manage_iot_devices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage IoT devices Bulk Field Update — Applies a bulk field update across configure and manage IoT devices records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-configure-and-manage-iot-devices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_configure_and_manage_iot_devices',
    "version": '2.0.1',
    "display_name": 'Configure and manage IoT devices Bulk Field Update',
    "description": 'Applies a bulk field update across configure and manage IoT devices records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-configure-and-manage-iot-devices',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-configure-and-manage-iot-devices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2ababc757752c640',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-iot-devices'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-configure-and-manage-iot-devices', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateConfigureAndManageIotDevices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateConfigureAndManageIotDevices'
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
    print(BulkUpdateConfigureAndManageIotDevices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZerxpblX6GzPtgu8qZAgCTuW2+tFgKEhARoAAG+b6UZgkHMowC3/3sHkjKvXX6vql3dH1p3SAERJ86494kgf32xmjrIypevLydgpcjaiuMwACVipS6yym5ZGcEfWWTDf4iTpXUZ2k2dldXL64sLKqcM8zrMUjh9medxCCrEQuwmjhAvBLGLNLlr1QCxnDKrqnG+F/pNCe7SEyu1fIBssjPigjZ04NwSOFnpVohXZgkcg4Rp3tRIHFb1K3IL6wBxy/5L2aRIXsIZ4IbYwMugOCdLkrB+gzqBzkryGFQvX3/+x+tLCL+/fP31xYmtCt56YaBm6l2l1Ycqy9Td3xXZZDX7UAOKia3Uh+PzHvomhdc5KOFCCbzlAg95Xv1Ygdh7Rf7936ObVfrVT1+/pcjz8+1l/HOEmtYBQOrMqmrgIo6VW3YYh3X/hizjm9WPFtdNmY5eq6BrU//tMfO7pCxH/j4++/GxyJsP6h+/vWRQBWt0/LeXn5CshOtBr8Dvb6OU/Mef3uLsBsoff/oup2rsK3DqURjU+u39ef0UCwd+Hxp691X/DqU+QmyDby+/M278PPQe7YQzX96uWZj++BCcl1kLUit1wI8//SuxTgCcaAzr/5Hcnx+CA2C50Kan4j+93p38DwR9GvQp818vm8Ow/hVL4PCP5V6Rp6P+ley7//+D6DhMYVJ/ePyfivtnE9C/Iz//S9v+swmviPfthQVx2MLssGPwFfn1/aRwq59/cL/f/OEfv0HR/6WYU9aUzl3COyzU0ANV/f7+8w/V/fYP//j5hyaHuQas5L0p438m85/59b7OHzz4HPXjH+fC9dU0SrNbinxmOvJrlv+P8rc3RLPi0P1+v/qK/L5exg+KjEZ8LPpwwe9qpoK6/s6PP738BpEihdY0zv0xrPJ/+zdkH46glXk1cnIyiEIwwHWYgFH5cxBWCPw71jYEIlBWIXTscxzM/zHCo8aZh/zyP507iH5xniA6GdHx/YGL75+A+A4B8f0BiO9hVr8/AfGXN+QM18jK0A9TK0aOS0X5Ng5K63F9iIIVKFuILHZfgy8Qk76MXyBsIr/8lWXe7xLf8v6XOzCHD9Q6rjYjYlVNDN5Gqy8BSJ82OhCbQQecBi4WZw7UzAsh6L5Cb1RZ3ELEGz1URWEcI24IUR0yRn+XDb34dRT2yy+/2FYVfEsfEEsgDyqpJnDApzrIly/QRC8O/aD+lgInyJAffv3tB+R/If/ZrLvwcQ0Fgv4zRlDD7UmWEFhzTQKHwfDBgENAucfo19+ejoZiUsh9MKKhN3LZOBnmbATcD6+fhOWXKTX7IB5IMFlZQ9xGIP0gGw/51BcuOj4akT3IqhpSXA5SF6ROD6Va0JxPT6ZZjVQwMSuvf0WaCtxX/cUurbuKCSx+q/4F2a8UyCNZDP8b1bwPgpOzNITu/8yJx30opPyhQpgPEW+INGYpklullQel9VzDsx5xgfzxMR0Kt5AU3L6lI3WC0VX3knm4Bw6CnnGeIf0yxvxOvTCw1cfa9zHWyHbnO+uV39LqWQ5WCe4MD1XpEb8J3ZEk/vZMqSrIGtgwjP6Dmo6SnlFwn1G55+Dqv+ogRoZH+Hvv8SB65FszxXAS+f+gPRkNWK7XR269PHMswknno/Fw7NhYjQF49GKwP0DgvEcRfe8ZPhDnA3i/pXEIs6Ts//YYeQ/Hc8wDzKApLsSM410+zAXo2FHuPVXH1CvLu0e+pR8I/wrdc4czGC1Y1zDvx3T7WHB8+qFpAIt3vP7O9k/vjL6D6YjkjR3DVPEAcG3LiaBW5Vhuz2jAvAVj6d2C0An+YBUCpcP0gPIRqEQICwiywN11UgbNhJV29/7n8HAMC9TCbRyoLexcwRtygRUzZk0FAwAboXEM9MIPd1FIAqCPoYqfHq4CK38oMza7TwWtMRZZMmbH7yLwfPg9x++6jOpDqRbMJejL24i/Lugekf3U8xkrqGwyVuV90h/D/bQV+T0V/e1betfxE/Jhsccji//OOQgssqS65+yIVRXEmwQ8Ewhmwp2w3x6c+yD1T12+/qnD//GvbQLuLKr+MXJfkaCu8+rrZPJgvg/ie4NVMIE5EuagupPgl0f1ffksuy9wuS+PsvsC2enLs+z+sMbDZV+Rv6bnH0Q8E/wrgr9hb9j4aAeXGTP4+YFuWX1hjC/k+PRbegTf4/1MihFz4x6y7icBfQyBLOSXwB8HPwipGnnsBqnzjsAwIt/Sz5x4VgwE+NQf2bPKflfJdyaGEX4E8JMo4KO0hmu7Yz/ng3HPE4/qV+Dla9rE8etLaiXgr+x1RlaA6Qu9Mm6VYCnBPqkOwf3qs2caL/6437sXGUQHN/s61torMva3r8hnq/qKfGwe7vuytIG7p5/HNnlcEg6FPz7Hfm4mbfACt211n48WPHZEY3f27Jr/rMRYYlBjaEg16vJRs+OKfxICv/g+KP8sRL5/seIncFS1NfJ2WH+UewX1dGEX9IrAGMIyhJUFs7SBE/68DFynBEUDCdIdzf3uv+9mZQ9bfru7oX5sK399+QCQZwyeLSQcDiv1SzVS5ATmK1wQXj8yCz77v2oun7Ig/MGGBgrDAEFRwHYAtnDcBbWYW9OZZ9FT17GoBUHSHkVh3myGW5RDzOz5fE66U8qZzem5bRHODEB5j1x9f/AdFAkwDxA0PnVcYjalKJLG51OLdi1yblkutljMsbnnQob4PjWC2Pk0+mHk6NHPPnd0ztP2X1/sGQlHCmS1WT4+qwmtWbMpaUudjZYzzz+nk42dattqji37xDx2xLpn8gxzpE29ioHhJEYWelomM4Q8lTiLabOD52zQXp+nkSBrZHh0d7ul3ezUxXa5UAZUnRMol602u2PhxBcQY9qp8itOa8zeVk8Uakkn6YRfc1U7z0rsdB3OYkRwNBGFp15HURknHHOXFo6V8cxaKolw4TT7fpf1+CadeRS34/MorC6MloRDvDKJWAvjs+2E28bdRceTvbb5WE0W/qbEN9MNvs+X+rqfXnBCPhbymVos2iGfeS0bz8WKAm2Zks7JBvbaJ0Vcu6ziRFvjSubA3uSUH2zW1KJdKLvYVVlol20fu02vCpv5KdXUfr0jeg53ZtpZU4dVEEaNs+k4fds5ld7ke/50u4DsOnCZuPMrrLtdU/xUc8d8F1wCV024WbIt56uZtMenEl+WjclPD8QkDez4kjhdSJ1w1g3aABwvsRwYZW5uN13sHVbHzYmOtsk+1Penuqvc3ZCnqrt0Su46PWzEGSNO7KtozEWdQW0Rr4houJj7oRLoU+cyAywInBvoylzFvndohhy11lTDkkZnRLVfTM+qJRkAX1MReVbxvrPyXWXPDZXtpiW2CKybHpDp1Y9P62YT3XxXtgsGtyWu1S/AVs7DkK1PF+oKGktv9ZRelYLd+DVsnDuhDMoVG7vp3DplV3ln4eEq0CpbdTIxlctiMBKR6BeHnZLMig1v3ZJu3aLTVdhzIlhfibwY+As3WZyPFqkevIysJXkQuMw99/Kavyaryy2gWKp1ab0nuDzshoa6KgZOGiihDp1SOZzFDyYAqq3Juknvk5tlGzbITraYS7KnbvGaWF0uVaBE813pH7xh2XYoGJj5kl+3lQp4cUAFrOvllOjJyWHHbshGk+tYuAFr2C3OmDo3GomhLODhMb9qcFKzMPR0SC9aih7I7nrhq1NOGpIp+PteAf26r+fLQzMLD5VgOM5sclt7U2CKhs6rvBnOsCNLMCXKbph5NqwqdVD33UXq5NmWZVgbbPbWKjj4YgLcs5YAmbs5Z4mab0tnl6FMm2bTtN4K5n7G3M5SRm4zTcgERlntLZ4YJH+36I0YHOgA309Kikym4JQThk2Y3VTCNlhEGZPanfjuoaHtPXM65LTOBRdr0VJuHtJANQDPBbJgBdIl5pkOVzo2LHYr1poGK58p1FpxFMHWZjPMMXVadPf1tWAnRbY5dbKVbuQTkx7XC3F5Irx4flXXExgI1ieO1W1Oo/TlkoVpv6B3JZ/sFtPOoGQcT88zhSq3h0i64Zuy9ldmXpW3fEsdCn5R6iffLpreYsu4IrZReVvvLzcyxRQlXGfpAZys+hoPBZNOii2QLmpEpeTUBdZeEjZJu00BM89V9MDXcqsfwAQcqQ49rYzWXtZmvzOBfRosYe/IWB/12/lsZYnxeTvIhbTf7IwtTJBMm82P4t7pFLEhj0PlspFCzSbiKcMtx3Mm/DKFsEXnTNsO0/qcB+6KmZqXo5qd5wvBmRc7Syl4qRguNdr5vhJes4nXTtbObdLwqmB24aKhJJhQQmnz9pUm+S4q1gx/cxaxyJA3VI+wlKPX87DsAoa6qW5WLGch1R5VRYmPBqPItORHAle1Qz3ZJzyh8SZl3qRjNLtA5FgehCV5NBZbPAzpM8XPcvF8jI3r6uYqzerAi6cNwWaYrSl5gpZtw9WSEjH9OuY4/Wb6fF4vjv15K6tLktys1GW4drdW0u+xcoIW3Y3aXa89e+E0hoOMszPxYG5QhUMzC/SKc8dBbtrFdKKcR2geMD86bcNunXju5JzkW1FWbQxP6rQ6sf7BEPQcDNSENny+dDtCoKM1W1CnvckcJxOg6zoxofbKvAiH/DARRd+/bAFq21G0ZJKbMVMJiU0Sta83zVUtqItcdKdDTV+FqXYKRclheEwsA93f5llztLXLScWUkyffrpwTyql0wApSiMQTQ51ytnK2tHjgfUOlsy42bpeFCOLEtZYtOuxhg9PPi3QYYnl+m8GCEtWoPgTTSU1yui16os2ummi2Rwm/txOgNtQwFCIOC3oH9znDAVtzknIjh41kr4rWFPM+cVHCcG4Un8iobW0WEJL350QWKrugj2ZR2rBLwY19TSfoYt9ujBzyT67BnuO6pIc2K5vtlFGC8HjYQbxi0f5QbS5KtQztRA1qq+PiGOhGoE1VF6fom37je80Qz7Y8DeIiUclN6MOG4Bycpune2B2lQzjRitLgjO3e5yTcMG4FLeB+qh6JK6/utH7XOZiyicLc02MBSGt1zUiRXW37ZYDxh86ON6ap8+t+oRQX5lDrouuXCboram49rNuVyzvtZsacFwInET16gPiUbE/TiAt8W17G+yPmb2psWjLrVbxPPIahr+akGtSFwtJr2kpIm+uOtVd19XwP+Fl2SYqLqa7ohMbcU3ZibNhvqsahaVb4NVRnao0GorptHVxWST+i5YJLN6R+6KO2W0Z4VtSrRLkqy2kphwfJW0X57Tr1Lzum8E/1cRuEq8MyGtBejAnmYC2Z6GYbV7qh6A2aDGt/bbETehrQlVjtrvVVda/acIuXdsZsAaEDKElXk9rU02lzCoQJ1S0q29ux7GrLBeuQbQ9q2wJuIRytWZSmFklNEyGXcCeZqnhLNQOPybEKpLapXXVln7WQYc9QXMVvDmGQHUSO1fPJvBZrNSLXKLaPtpXR83vdFIWBnsH2Ri6sbrdnKSsLiylBiJplrdiIVaKtdTsWcS8XlMwzQ1sm4KDmRHZ0pCV9C/pc2xULrNGtuMtSkgcqtz8VxnSBJ0wrMZJ8xG7pMr0KWOhUjnxJNpXfKYOm3fytXCjpJjI6bG1I2Ik9TtQEPUb9jJjp1tLlzWbpxcMRRG265km5iMkNjrHM0gJq0kCy257kSNmyuyNAl1lvUExErS7oOTBWtLUTc3xbHND4Zu7UM5dX3W6Wzs31wHvmsRr8K1tigr4lzoZotqcUh2gWdtFx6ujbUiyatbnVisWQnItdz5ne/HL28kFilKNzmMf2xnNZ2bcm+3XlnsqFR7MD0CMLdaqcsbWhrnhvGpK5KHfTa5lLCq512LXd7ie8Ssyv11pNvNzekgyhHreDQ60351O03mJbV0WX/sEcwL7P3GJ7rHKWDfdx7m9yZwfBmljx5+F4qd0jtbuEGEccyUWGa1beAO4cWYKL+jXZNr3TraeKzGrYBOMvbRhjJzVZKbwp3Th0SaWcuFoCLZcv/n4fTEx9J+ekWWf5NUtYcVezgVLIVu2Ww/IyC7axKh0VZp9OtXlmitZW8E676aannEVC6OeCXfZmpDOpgNumGGpsR4STKD5uOHSg3AQfYquzIVXvZDWgHUdock4VVYE/y5sw52pfNLmBrYOCbhfMVelFB23N2YrYsEQ5sfsmmieBW5eHSBXN7CxIw6Y20Q2uoyq2IghanU6OvFZHvJYaW70/Cdxt6w2ymVw1l+6TmatrnG/WFprLjmruNzyBY4vCv2l9UR6MzA185cJmNxWcfb7ArT0xu626w2DKrG5O621OTyRJExj85Cs+A8JlDGjXEQxsMsf4qKE0n7kdcZLBKJTlt3ixaSMrTkNDVqdElfACZ/D7Sdbt6lkfk1lZ9VY4M8/lLmJ0hXPwPeoehq5YTedtbqwPGrNzUI3GgvMaTcRsDjKh1oU1PV0IIgFSNQUlrVxZnOkVItZ5m6jwtpzz1twy6I0j0NOJmyx2u0nD9M1uSxCDaUyZyC4TBdO4QJnOK9NyrLyXxDhfrwWGUui1vqSrwsUgeBA7o1f0w+Ric3h3W612ay7d+8l2dsgOxmQ6WXqnbWHJ7kGLE3xiB6Eq7FfHLjLyugkr0ZNbVQt1fGtLEyOauNHMSVbX5raf0rXbrzSUlo4GkEt5WBSk1C/L85Wk0vYSEJXrKHgjHymUnkwU0vYidqMWPTapJpOQomU7bVqAm6hrwL45Nft0f214d6nMXelIyiBsbil5ziO0WVt7ZSYo4WbPRHP0Yqk6uRQdVwbccGbRVb+WertbOsMi9FCX72wqBo152cGaZkFRhc5Mvt6cPbDWU/UsMwe3n7VAdahjcjwNm+lhX7S+3V939aIHu5t3aO2+REk9mi/4G4FrB1gUjk6TwUJITV1zAg/V+10EO98lQ3hGh05yFicOhhwk/U1fDtLR3QOls6TrxKiPk7Ys+d1E91DSWHTRufX843y5P245Gii567A9lpqttz9KgUbTJUN2PLFh6s5MTVTK58COW40FrZutdQnNnG5BVOnCqxdBMl2drsszTRRHe6mmZLrTTiy3U+fcuRD1LJ5zTnuSKWtStMFmxVZdALy82SazrU4kFGhEUygOLEnFtqDEB0MxdhYje+5tto8mS1u6gK3b4akw+AovdtpiU5JB5+Go6BU3QxbYKRgSr166J/Z0Fpq5cpZ1puMcbm0ODpcdagLy17r3b8TGEItuIs2EYnY1om06R019ecJIjG/nDMFeJoJLuaEIN5g2Cshoum3MknHcTO6BdhmOpCiuZUGjOgFlnbxX8E7wzNaha0tqFieek70MXFmm7e3lVBGWF24veFfYY546h7G8Or4JZJAoRyD29Nlg+tuFNVW3FqVbNSN0zaNcA5uruEeQ2f5A4fOdYV17fOZL5F64wd1GJq9WbUAzu4Vuc/1+JTJ02nahK5y11TWjhTmWqJ4mu9hQHc6zq8uWYMOQxyk6y3YMTdt4S1s3a2viKTG4MjpDy2plBEtv3qYoVgjJ0iY25NEhPYXQJjQpEXPzsJ43sYzxqIxKTRtQ3Y1WCADL1POlSMrPhOAOawtNbSHarnu2XfHcgU2DopyW1QA7EcXH1/i18yVdl3VviBc6WU7WVLb2o5iZNW2YU+PW44DZiur2olAOlIIdm1klkW2c50W7KlKlwC6Gt10ILhti5E3K9nwu7rlWYnUhYTN3akIqrYcLVcp1LRF13ixcuFm08uVlna/h18Shz9v5ir0tHKE7qzipEz17hT5dbvUVt9ATfzsAVg7FAM0kSraWJkaJ2/3eE4MK7w1alBO3lHX/AuaBLLa+pbfz6WE7obFMJXfiQiN3c8gYYcjBBsXxdp4Z2ERCMzHcZcUmfZOWZ2G+yq7uOgq1urcmqwW/ktSJaRVnuoxd2H6lcCO5YKZ+yizaix4zYS5HKCwVt833nEdzgXu01kSSLgJjemXnPWSfuQZcoqLpIIa5lhHTaNCG80w8LJcvry/jEfbzIPq/9SZ6PBH8f3Yw+ThD/HhRdT+GBpb79b7W1/+eev94fSmdECr3OJSt4sZ/Hlv+hyPZL3/lVccoqX+89B3fs3X1x5l+bfnjrzS9hKnbVHXZv1dZ3NwPiF+hf6vx1yqq9+dB+Mvd2CSv788+jYNXlpuEaTi+lH2vs/fH2fR4P0zHV0jADb9f+s9j69cXt4dxhE3tOzGj3kGZj6Y/X6FAi6dv2Bv+8tv/BglwatZHJgAA -->
