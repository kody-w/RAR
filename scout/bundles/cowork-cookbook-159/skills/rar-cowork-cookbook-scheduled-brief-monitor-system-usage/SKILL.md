---
name: "rar-cowork-cookbook-scheduled-brief-monitor-system-usage"
description: "Schedulable morning-brief email summarizing monitor system usage for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_monitor_system_usage", "rar_sha256": "acc16ce1ffa70a64541ca19c66023f823b23bf6272ad4495f34800a19991ad5c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_monitor_system_usage`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_monitor_system_usage_agent.py` and in the RCI capsule.

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

Monitor system usage Scheduled Email Brief — Schedulable morning-brief email summarizing monitor system usage for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-system-usage
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_monitor_system_usage_agent.py` and embedded as the fenced Python below (sha256 acc16ce1ffa70a64…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_monitor_system_usage_agent.py` first:

```bash
python3 scheduled_brief_monitor_system_usage_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_monitor_system_usage_agent.py   # or on stdin
python3 scheduled_brief_monitor_system_usage_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor system usage Scheduled Email Brief — Schedulable morning-brief email summarizing monitor system usage for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-system-usage
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_monitor_system_usage',
    "version": '2.0.0',
    "display_name": 'Monitor system usage Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing monitor system usage for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-monitor-system-usage',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-monitor-system-usage',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b0478e985dc45228',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/monitor-system-usage'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-monitor-system-usage', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefMonitorSystemUsage(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMonitorSystemUsage'
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
    print(ScheduledBriefMonitorSystemUsage().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZOj1pbnV1Fn/1HlpiqF2KkXjhixSWgDIRBCLkeZHcS+Lx5/97lIyiz72a/7eWIiRpUVKeDcs5/fOfeSv76YTR1k5cuXl5NrprOVGcdh4JYzM3VmbNZlZQR+ZZEF/s/sLK3L0GrqrKxePr04bmWXYV6HWTottwPXaWLTit1ZkpVpmPqfrTJ0vZmbmGE8q5okMctwBPfB8zQETGbVUNVuMmsq03dnHrhRB+6sdKs8S6twYpR1qVv+YwYkhX7qOrM6m5VNOnMAw2EG6DvXjeLhFSjj9maSx2718uWnnz+9hOD7y5dfX+zYrKrvyrkOM2m0f4g/3aVrk3DAIDZTH1DmA3BHCq5ztwQaJeCWA2x4Xn2s3Nj7NPuv/4o6s/SrH758TWfPz9eX6Z8CtJuMqDMTMHdmtpmbVhiH9fA6W8adOVTAvrop02pmzirgzdR/faz8zinLZz9Ozz4+hLz6bv3x60sGVDAnX399+WEy/esL8AT4/jpxyT/+8BpnnVt+/OE7n6qxbq5dT8yA1q/fntdPtoDwO2no3aX+CLg+omq5X19+Z9z0eeg92QlWvrzesjD9+GCcl1nrpmZqux9/+FdsQQDsKA6r+t/i+9ODceCaDrDpqfgPn+5O/nkGPQ165/mvxeYgrH/HEkD+Ju7T7Omof8X77v9/Yh2HqVu9e/wv2f3VAujH2U//0rb/bsGnmff1hXPjsAXZASrmy+zXbyeZZ3/64Hy/+eHn3wDr/5HNKWtK+87hW2KmoedW9bdvP32o7rc//PzThyYHueaaybemjP+K51/59S7nDx58Un3841ogX0ujFBT87D3TZ79m+X+Uv73OzmYcOt/vV19mv6+X6QPNJiPehD5c8LuaqYCuv/PjDy+/AYxIgTWNfX8Mqvw//3O2D+0yqzKvnp3srKknqKnDxJ2UV4OwmoGfB0ABvz7w6UEH8n+K8KRx5s1++V/2HTc/20/cnFdv6PPtDojfnvD37QF/3+7w98vrTAW8szL0w9SMZ8pSlr+m4EFaT3JzgIpu2QJEsYba/Qyw6PP0ZRams1/+Hfbf7pxe8+GXO7KHD5RSWHFCqAosfp2s1AM3fdpkg2bg9q7dACFxZgONvBDA66cJnrO4BQg3eaSKwjieOWEJzM/K4c4beO3LxOyXX36xzCr4mj4gFZ09ukU1BwTv6sw+fwameXHoB/XX1LWDbPbh198+zP737L9bdWc+yZABvD9jAjTcnKTDDNRYkwAyEC4QYAAg95j8+tvTwYANaCkzEMHQC93HYpCjkeu8efu0Xn5GcGJmucDLwMNJnpX11LXC+nUmerN3fYHQ6dGE5EFW1aBL5W7quKk9AK4mMOfdk2lWzyqQiJU3fALdzr1L/cUqzbuKCSh2s/5ltmdl0Dey+K3LTURgMYgmcP97LjzuAyblh2rGvLF4nR2mrJzlZmnmQWk+ZXjmIy6gX7wtB8zNWep2X9OpSbqTq+4l8nAPIAKesZ8h/TzFHLR90LlTp3qTfacxp+6m3rtc+TWtnulvllMobNAOgFC/CZ2pKfzjmVJVkDWxc/ef+2j1zyg4z6jcc3D/V7PBe/+e8fdh4t7GZ18bBF5gs/+fk8ek8XK1UvjVUuW5GX9QFePhyWlYmjz+mK/AAPAUA6rm+1DwBilvyPo1jUOQFuXwjwfl3f9PmgdaNSVQRlkqd/4g+MCTE997bk65VpZTVptf0zcI/wTCfccrEB5QyNHDljeB09M3TQNQrdP193Z+j2XpTGUN8m+WN1YMcsNzXccy7QhoVU719QwDSFR3qrUuCO3gD1bNAHeQD4D/DCgRgooB3r277pABM0FYvDJLvpOH05AEtHAaG2gLplH3daaDEpkiUIG6BJPORAO88OHOapa4wMdAxXcPV4GZP5SZBtinguYUiywBmfv7CDwffk/quy6T+oCr6Zg18GU3Aa3j9o/Ivuv5jBVQNpnK8L7oj+F+2jr7fa/5x9f0ruM7toPqfiTvd+fMQFUl1R1OJ3CqAMAk3/P00ZFfH0310bXfdfnyp6n9498b7O9tUvtj5L7MgrrOqy/z+aO1vXW2VwANc5AjYe5W37vco/g+P0vt86PUPt9L7Q+8H676Mvt7+v2BxTOxv8wWr/ArPD3ahbY7Ze7zA9zBfmaMz9j09GuquN/j/EyGCVxBSVvDe6d5IwHtxi9dfyJ+dJ5qalgd6JF3qAWR+Jq+58KzUgCSp/7UJqvsdxV8b7kgso/AvXcE8CitgWxnGtR8d9rGxJP6lfvyJW3i+NNLaibuv7d9mYAfJCzwx7TvAcUDRp86dO9X72PQdPHHXdu9rAAeONmXqbo+zaaR9dPsffr8NHvbD9w3WWkDNkQ/TZPvJBKQgl/vtO9bQst9AXuwesgn3R+bnGngeg7Cf1ZiKiqgse1OzTx7r9JJ4p+YgC++75Z/ZiLdv5jxEyqq2pxac1i/Ffhben6ageiBwgO1BCCyAQv+LAbIKd2iAT3Qmcz97r/vZmUPW367u6F+7BR/fXmDjGcMnlMhIAe1+bmauuAcZCoQCK4fOQWe/V/Ni08eAOjArAKYmLa9IGx34XkmCZsEhmML21zQNkHACOpRCGqBH49ASMR0MIzGPRSjYBhQ0PTCdHAb8Htk57ep3YeTXohp2pRNLjCHJk3AG4UtFEhAFg6JujBOA7aUiwEXvS+NAEo+jX0YN3nyfXSdnPK0+dcXi8AA5RqrxOXjw87ps0ledtYhsOiS8JbVjY7qfnu+1q1Tlju3cPcEYnewaTtSTR/6w3k4BqyqCXv+eGXGM4ZHkLKBOpXcpZds6WXBMSVsUlJvB0kM5GVvX2hJdmyN54+3DWFdBDcR1tdyS2pKfdXKzYlQa60s1e0l9NjDYhMQFz1EBYucU0g2ipJwCA0qt3GizsettL3SOVHhq3gepPL+gi9pRpSLUjvl1lYYTDg5ukZyhrRbdCrK8xghpdFlxGKI+J1/TtbQbbHWEU5zbzDhyDuK8NISo+ZwYbdogFPaPrtEG81oN1v8qh8dS0Nyk0C84FArJ3G3cpt92vAoUtqNJWhFo8SxFOJxc0GjTYgtaJlR91tBKsqC3wDAEoYegNRNNFLtHCb2mdnYWK2ch3qzwi9hbqnGUSsX57y2Y+Gab0oHwxOpz2ta6HcNYXkhvaXOZbrnyc3KqHJt4DoHu0TOdcyUE3E56ax1gZfRSbtd51a6Ncwhbha3/Eri/fq43uIbJ2LZ5raN4nNQBfYKx/ZjXFyuzubQw/EmmJOKlEmOGZ8yDSXoWLmYqBib18bkcUkmDMZIDn6CqppeGw1uCjB10hbEYG5kgClmr6FQBlex2K1zIlX99LRqNtE2rPAmW5+pxYm2r3hFe7LkX7diUQ/41XHpeaYYpNMJFV2vRdo4GEejrOb2KBCJo2ineMjg+IhI8vxQbGsnho96fLicjO05kMPoBiFhNQqJu7qlQTyuXamVdrm2Dxy5MvTV/HwL7WWGt4djPwo706BulFU7F5tcNUW1k66kxAvDFbpcQ2M8dkp2rOMred0oVyfRcFrTcEfTYKJokyDNrRTbSyjBp91xpPQUM+RuqZnQIktCUT7PDbEYCXfv5Tkd2OtTIDU0MUeqAVpYvI6sVC1wz6l6VsUyNmM9F6LhgEQ+stvp4rWjQ03mmEKkmFTZbXVIK6/seVRPiyPB3VINOtbQmB5U1miCdr/TC8PEBK8zlhKz0pxTZDKnDY/yZBbt+evBPXCSEW5XZ0UVEmelYbZ66LHdzd5m0L5NdSi5XfZEAKtVtPfJzVqUQscPjGHOJ/guklnldqho1TLqvVUckmhur7GzydqVtYBbyKsOQ4azW7n2Eh9ZtfoZ3cSVlxccz2b88WINm6LKA0naIKK96A3DWsH8gi87eUS5Hl4osOkyGhQqKmcTizEIV2ct2fvntbhEs5RjlrlVolBXcF5xgFlinvX8dT6v2hTU746yd2WMcNCQK5aUCK1qtvNikZ1wXj+fk064yqskKBJ0NJRTa2YLjhnyOac5zmFNVDG37LieOZrrtLvaWlQeDD1HMHmZUgtxztcIemD3+tzTVhstg7XCIw4ozzYxr23Ii7lLbShR8L4cmK61lofraYs4yzhAWAN28nhvHMpkZXI3ZzD6MjV1vliBfd3iklVYpPJ2QZLrXQ+zBpmWVGWOl7yvR+q09SSNq66HmvAWkLoRxU4at+PuxlrukhhpxVjQYt6et4sSlZOA1PYsSc/h45GDMOVI7+UGYVhtvmW327pa8Nzoe6uTcXWJaO+ezisF0zcDZoVX7sycDSykjMPZmmdiJqmVekOpIyKeRmnk854ix+tAc3nUHxDXOsm3M17n8I2I2Irbi95ma9micIaY4gjLIicM+zxY+vjmaMSipe2UutHJnZtIEXfaL6shFi76bX/eclkehyf0lnIsZeuCz5blTYLh8RodtrR0qmxJwnB7qQWOPUgVzI7x0R0RJ5EMxOmvjXhNLxeEtqSR6t0LPhxP4z43qCZFaDiKV9czZaDbEbkeOnHHZfDukHhtqDLG6NDKQLK9qIneihvnJBF4pSXgUDroriejIxYcKa0dggy7Ope2iLCNyCgVu4/3pIKLN6lk2XJhF4kq+TI/ek5/uEoZgPml4jDFLiaWbbKJtIUXLUQfJrGojMSTmZeaIS+1ldol3NrxVTJy4/1VczQczfg1biZ6wlFi617YLLdwikBgmJY6rSHoXbRCxESD1SgWg2rpn7y1Np4YrzH9sC7M6oCtYXmFmn2ho0vIueil6uLsOalMqRgzCOFXvRAbizNZ7raHG4phqnTYVH3clz0TrkI6MkfWyeZ5BDSM2qvYQDyBNz2+yQ9qxadZfrzEO63Mit2aQWMvnzuqfaTFm5JDYU7GWCfkYu/wXFSLWGsUJ1TeNfpgJjtaRDC/22aFtkkOsnO0zso24je9Kh9WcWkam2WtLJYFXZx1bHM+Wcu8MLD+dt5z1+LKoxvjcHFi/kahAWdeqVDTNxqu1hF7bI9ri734xk04UjyeVBSi1viJpzk2v2Tq4biwm0ItNaXCDGO0OcQXUqZfO0gbSLR+bfZ1zohmMvoblY9FybId0+yjmlmDraZOrMRsKQ/X0LFj+EBLK1o6Niu1JtBruRuu7jieDwe73nYyUZcRLmSRgGY0Lx4bl4rz9WXamJwVgdDwcOCBV+FTRK/MCA1PWUE5/ZHd7j1P3y5byIlD1RQ2arx2QMbsLmEs7hglEI9LR4WGbdyyR3PJRr1V3cgGp0U3CbgjJ2/mENLTVUEpmwUmSUqIY1uQh37VkHR6OcZqoSJllu2bkh402ZvPZTi3aNY4MBtisWFQce0i50PF7B2JHEcwS3i9EDXzlrNyJ81GY6BXauGdENRsQQtZK51r+WZBExJmMlseOYtsd7zKMmkF56GKfQ+7aRshXB2DRMqquh0pKFOUcsdnN7UTLupiITX7YAEn60KqxeNiG1+O9kUvsHWAcpikEZHW6r5J7DfMLj4L3IWMNQzakQzn8/4gUIv5dsFk0i25sESeGhyy906boe8I0wgHjp/v0ct2GRHKEq/YQQvRXRSuz/I+pY8GTly2VukL4hXS9IiDLrFMsivDTCMsQ+HbZsf4TRpHTRPuGW2MlwNDaqDeQ57bSEZzUHnEjtlsddC483nlnWznVvTIKdmMeJgfDGyow03nq3g1du2y1GRjs75Y27xVU0HUmD2dnhBD35Sn3KsGtehXarJjN5Zn6ap3nUuMTNsqc8uGC3ocs1U7Cu36eltaNMzZF9uEkn1+suKOri4XKoKzQgqIW3k9SDedV0VyUOX+fICwq3XepDgx6EtnESkJKinEvjWVLTdXoKV/vI6uqGjymYcRLVBG/QT3kVVB1+6AsoyKubrjgJ6lUyi+Vgbb78gSF+YMvHBk29K8eicsukg4t6d4oWgh056V1ucJBo38FUBbJ5d0f0/FyNVvpfR67bL1rQhUdiOkxVnD8at1aZY1XFirzPQPvZ5AwlDgpr4X5JOIGHPcplRdH5N1xyqxuokS+ujVnnvekRcBK48q18KkfFAtfB2dsF1CjHB3PKLnHuwYqHiJn9pkwJZmwJPLeNVAKSXcZHbvQalKsNVxha4hPKacA1WRziXYF6fb8ibvBl1X9O2JJEpT8Qi38NyMkZCB3Q4V33YHDjGWLbndq/uyqRzV2aBFuOTRqj2WkrkPuBPYYUlKb5r4Gc2WJ6nr1hbTGdv5pmPAXni1pa+MkV2rVEioXI9hiExj4hYQWbfqlvKRPpVeC3GVKQeoULGany/DazWkRC9J2sYx+EtmxZdkK/FDXelg3DAOOwrrt1XReORFU9BexlfEebfJbh6vUhThF1WJ5wzPKcOFXXk1ezkKF5eNt+Z6vVCZaDvXudoCexS0WUBy3/RH+0bjeqHTKJEG48GxtynUSdxAXqDamZ/Jhguh9TbVmkVn71xkvXREQmFPdeGscAZJl1mOqkfTScUOuVKMMxxu29RmnEPN0M5tcWlQHV9XK61SBLMxtL7fh60XoozHbkyJtbqFF9OuxS13UA5hmL5nFLTbQelYIoIh0Kdz3yIbGXX1VPAzsuIOrQUGxtirLE0HuTXW823DUr4JY5DU4TDmkCt0RYxrkZor3rxdCPNh6azOhukhrYeF3gVM6yXaJt4F4eZVilR5JZKqduQG9KS5XApQcuMIeLftJSzIqnl2dUTfFyxvQMYkXzLqrR666LCXsZ1ooJuWZ4Y1vp+HxDpIkzNBxN6eFrpDQ4wbNCNkpusRTA+ba1esm4tAjmm63XfFyVgNQhxXa08z8jY5CR7nMoTteDAjRXO/WUEDwVz7Q0g3vOxT5JZsox1UNOc6rq5H9oIT/o2EIvniMD6xsnaswVELAYZxSZGam2e3yvxWtAtvrssQZmSnMWvbSowzPqt8R267RgrI60ihdSI2o0k7GWP0vGcIdX8tTYiOcZcEpT3qtY1J+sGtnH6PejKGWjhzqHhBYlKr1SgdbM77gzbwkqiD2T2FlVraIWLvVu1g4a3LH0VpXIEpKsS0mjrlrdDRlNtJcLbuR9aVPNbvsE6HQ40mGeq6gTj9WlGqdSv3crq0t4vbDotv4VpAL4MxR/3OltaGEhLc4rg2qoVW09TFRqNjdxSC2mdlRohJE9sKyx7WuwUTzL1qszifUPF06SkCYmFMaTberW6QunBJguT9uk9QsJ8hYc0eJa43RS+W4DJRUUIbDLFcwC7mQNpOtjjHUsqIbhzH3UP2ac1Ll4xOJMbjEK5yV2yVHWUvpf29ANSrIPIg13Q4Co0MBqOVxmLGjmsLpDkjRxPi0FjH9/ACTUinVAwzQGv43NHrs1qwwEiPbZcrHxO3EMkzbVNWqtiJ2ZqSvNuekPVwve7BNmOzL6DiSipNR8u5A0s15q+DtYWe/GqNLhoE6hHGtZpqTlg5ml4OQsfxIkfa1ByJjxTMudma2yEkFiYtehoVKoO39ZaGFGpRXR2yXYSbxr5Y1HoOXS6SvQ3a1dw/xPjuQsPHfWS5vGn4q5bTdDCQ3eZRawfDvkhR3pQSs4GWJSbX2/lKyFa+nzBm0oY9PW8F+wiDPRbdE+vyFshV3+C1g1VxUOetT0QcGGAMI6fXNXeDRUzO9utsy6+MRGnDkYMl0g40DaEsu041BCURODVSVaX0ohMCU7k5NzKVtcHtAkpeM5S+OLiCQ/nYyFBL9twFskBnrI36YxaWbaG6auKvHOkUqtx6yCzOTuTTLS/NMcaEtMFUkHzbtgnKPTdvwZREMbFtUjxNIAWksNZlV0jCvOpq8ub54TC/DtUc033x1sYLtbmdlGLADrbunQK28Kh4n9OLUeppXy0p212SR/WI6amF+D1/U9Wjz0goqrAyER6hjArLUYXE6qpAEJWPkZRgfeOMed9cNAryqaOnFUQVRsvl8scfXz69TAfVz+Pmv/VCeTr9+392CPk4L3x7/XQ/anZN58td1pe/p9bPn15KOwRKPQ5cq7jxn0eT/3Tc+vnfeXExcXiIub8t6+u3E/ra9Ke/OXoJU6ep6nL4VmVxcz/0/fQCCmf664fq2/Nw++VuXJJPJ+X/ZAy4YzpJmIbT+9RvdfbtceY8yQ3T6WWQ64TfL/3ncfSnF2cAMQvt6htK4N/cMp/Mfr4UmU5wp7ciL7/9H+pE2mblJQAA -->
