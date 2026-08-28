---
name: "rar-cowork-cookbook-bulk-update-configure-and-management-office-apps-and-add-ins"
description: "Applies a bulk field update across configure and management office apps and add-ins records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_configure_and_management_office_apps_and_add_ins", "rar_sha256": "40b9343e948154b6cb36d8cf9097635fb4ff60e8f8de8180dc2b7e292a6d2922", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_configure_and_management_office_apps_and_add_ins`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_configure_and_management_office_apps_and_add_ins_agent.py` and in the RCI capsule.

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

Configure and management office apps and add-ins Bulk Field Update — Applies a bulk field update across configure and management office apps and add-ins records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-configure-and-management-office-apps-and-add-ins
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_configure_and_management_office_apps_and_add_ins_agent.py` and embedded as the fenced Python below (sha256 40b9343e948154b6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_configure_and_management_office_apps_and_add_ins_agent.py` first:

```bash
python3 bulk_update_configure_and_management_office_apps_and_add_ins_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_configure_and_management_office_apps_and_add_ins_agent.py   # or on stdin
python3 bulk_update_configure_and_management_office_apps_and_add_ins_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and management office apps and add-ins Bulk Field Update — Applies a bulk field update across configure and management office apps and add-ins records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-configure-and-management-office-apps-and-add-ins
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_configure_and_management_office_apps_and_add_ins',
    "version": '2.0.1',
    "display_name": 'Configure and management office apps and add-ins Bulk Field Update',
    "description": 'Applies a bulk field update across configure and management office apps and add-ins records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-configure-and-management-office-apps-and-add-ins',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-configure-and-management-office-apps-and-add-ins',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '81e0a820150ffb5d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-management-office-apps-and-add-ins'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-configure-and-management-office-apps-and-add-ins', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateConfigureAndManagementOfficeAppsAndAddIns(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateConfigureAndManagementOfficeAppsAndAddIns'
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
    print(BulkUpdateConfigureAndManagementOfficeAppsAndAddIns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZfbxpLlX0FXf7DckAr7Qr3jcwbgApIgAW4AAVo+ZSyJfV8JevzfJ0GySnb7ve550+/DUFKJQGZGRN6IuBEJ1G8vVtsEefXy9eUIrAyRrCQJA1AhVuYi07zPqxj+l8c2/Ic4edZUod02eVW/fH5xQe1UYdGEeQaXC0WRhKBGLMRukxjxQpC4SFu4VgMQy6nyuh7Xe6HfVuAuPbUyywcpyBok97zQgXeLor4PWa77JcxqpAJOXrk14lV5CgeQMCvaBknCuvmM9GETIG41fKnaDCkq0IWgR2zg5VC8k6dp2LxCG8HVSosE1C9ff/7l80sIv798/e3FSawa3noRoaXa3cTpu2lC5m4/DFPvdsGd1fC24LqrbNx3YmU+XFwMELgMXhegglpTeMsFHvK8+lSDxPuM/Md/xL1V+fWPX79lyPPz7WX8c4BmNwFAmtyqG+AijlVYdpiEzfCKCElvDeP2m7bKRkhriHvmvz5WfpeUF8hP49inh5JXHzSfvr3k0ARr9Mq3lx+RvIL6IETw++sopfj042uS96D69ON3OXVrR8BpRmHQ6te35/VTLJz4fWro3bX+BKU+/G+Dby9/2Nz4edg97hOufHmN8jD79BBcVHkHMitzwKcf/5FYJwBOPPr4/0ruzw/BAbBcuKen4T9+voP8C4I+N/Qh8x+rLaBb/5mdwOnv6j4jT6D+kew7/v9JdBJmMFveEf+74v7eAvQn5Od/uLf/asFnxPv2MgNJ2MHosBPwFfnt7bibT3/+wf1+84dffoei/1sxx7ytnLuEN5jFoQfq5u3t5x/q++0ffvn5h7aAsQas9K2tkr8n8+/hetfzJwSfsz79eS3Ur2VxlvcZ8hHpyG958W/V76+IbiWh+/1+/RX5Y76MHxQZN/Gu9AHBH3Kmhrb+AccfX36HtJHB3bTOfRhm+b//O7INR0bLvQY5OjmkJOjgJkzBaPwpCGsE/h1zG7ISqOoQAvucB+N/9PBoce4hv/4v586wX5wnw2Ijdb49SPPtgy3fICW+fWfLtwdbvo1seR+CbPkGTfz1FTlBnXkV+mFmJchB2O2+jYsgwUJ7IEXWoOog09hDA75AjvoyfoGcivz6P1H7dtfwWgy/3qk7fLDaYboaGa1uE/A6onIOQPbEwIFEDq7AaaHyJHegpV4IGfozRKvOkw4y4ohgHYdJgrghLAGw3Ax32RDlr6OwX3/91bbq4Fv2oGAKedShGoMTPsxBvnyBW/aS0A+abxlwghz54bfff0D+N/JfrboLH3XsYIV4+hBauD6qCgJzsh2RgO6FAQEJ5+7D335/Ag/FZLBwQo+H3lgIx8UwpmPgvnvhuBS+kAz7XqVgNcqrBvI6AmsVsvKQD3uh0nFoZP4grxvEBQXIXJA5A5Rqwe18IJnlDVLDwK294TPS1uCu9Ve7su4mppAcrOZXZDvdwTqTJ/DHaOZ9ElycZyGE/yNGHvehkOqHGhHfRbwiyhjFSGFVVhFU1lOHZz38AuvL+3Io3EIy0H/Lxjp7D5p7Sj3ggZMgMs7TpV9Gn9/rNHRs/a77Pscaq+HpXhWrb1n9TBerAvd2AJoyIH4bumMR+dszpOogb2G3MeIHLR0lPb3gPr1yj8HpP9t+jO0Bsrg3Mo8uAfnWkjhBI/8f9jrjBgVJOswl4TSfIXPldDAfwI9d26j40ejB/gKB6x5J9r3neGesd+L+liUhjKJq+Ntj5t1dzzkPMoRbcyHHHO7yYaxA4Ee591AeQ7Oq7gh9y94rxGcI150OoTdh3sO8GMPxXeE4+m5pAJN7vP7eLTzRGQGD4YoUrZ3AUPIAcG3LiaFV1ZiOT+/AuAZjavZB6AR/2hUCpcPwgfIRaEQIEwxWkTt0Sg63CTPxjv7H9HB0C7TCbR1oLWyLwStyhhk1RlUNHQAbqXEOROGHuygkBRBjaOIHwnVgFQ9jxk76aaA1+iJPx2j5gweeg99z4G7LaD6UasHYglj2I1+74Prw7IedT19BY9Mxa++L/uzu516RP5ayv33L7jZ+lAhIBsnYBfwBHAQmYfoI1JHLashHKXgGEIyEe8F/fdTsR1PwYcvXvxwfPv1zJ4x7Fdb+7LmvSNA0Rf0Vwx6V871wvsIswGCMhAWo70X0yyMbv3yk4Reo7sv3NPzySMMvYxreh55p+CedDwi/Iv+c3X8S8Qz4rwjxir/i49AGqh0j+vmBME2/iOYXehz9lh3Ad/8/g2Tk6GSAVfujYL1PgVXLr4A/Tn4UsHqsez0stXfGhh76ln3EyDODYEHI/LHa1vkfMvteuaHHHw79KCxwKGugbnfsD30wHqiS0fwavHzN2iT5/JJZKfh/PkiNJQXGNoRoPJTBPINNWBOC+9VHQzZe/Pmkec9ASB1u/nVMxM/I2Dx/Rj764M/I+8nkfgLMWng0+3nswUeVcCr872PuxzHWBi/wgNgMxbidx3FrbP2eLflfjRjzD1rsgLFNyD8SetT4FyHwi++D6q9C1PsXK3mySt1YY9EPm3cuqKGdLmyhPiPQoWPtqMZK0sIFf1UD9VSgbGF1dcftfsfv+7byx15+v8PQPM6sv728s8vTB8/+FE6HafylHusrBoMXKoTXjzCDY//SzvUpG3Il7I6gcBq3JxRNgQnNEwxts45NsS7veBN8wrEU49m057E44D3eBTzB465D2hwgJ6TFuvAnCeU9AvntURyhSIB7gJoQpONSLMkw9ITgSGviWjRnWS7O8xzOeS4sJ9+XxpBonyA8Nj0i/NFEj2A9sfjtxWZpOHNJ1yvh8ZliE92yz5h9CDZolaDXK8XuKZAng47vAmOFEsuza6yEdHa54WG90snpmYlhMrTTwWjk7W22Oywnokcmk/5W840ha+yJEhaUr3cbSskupJFMLqXvT+eXbJ10hatr+cpW5rakpQRZVnUim4RWLcG6ypLCjeP4Slxq3dCNPMnSUF+3MrdbS8m8wjC0qOmbp2gyMZVD5WJ0C5ZxD7FxTfJDh07WgVkosR5e5bo/T/F1BvSzrCvNsEoZvD0s1vWlPutHe9gnROUet2FzWvtLpmv0AtxwEOGsq254FmQVj2KL1umMBOO3otop3NFJjGNdbUtFNo7MfOInQ05K4Uw2Yo0rJI8u9/otacJBo1bMcXk4D+SMIINp65ZFPhcXukMn7LqdhRNzdzle2MJvCnG2m3ZiOw3M3XHnnFleMzRJtgjdtE/yIe18ucW703IOmebS29bJw12CNS3GWM/kYkjDRRJ5Uz5MVm7I6Mfj8RTJvD+f+Ym9PqkXP6sWN81ephNmIs58Q0VXzWoltDyoU58vgKT03fnWugp/tKLV8hYPpZSJjV6uM9oLlY0ACLuc4YSCH2csjV5i1y/ZmXlRzJKQmJg7atfr1Vqv8Qq7xNkEb+Z0ZfVGQhtZGEynRa9x0wSccjGpdvPOkM62fLhd6+U+pROw5xr20hnUdcplduq7XUNfNxtxZi2SJmOtwQ8l+6SFx0SvMx2katUOZqqSQ1dvNhJarhJ7nwbTDpW20TCXHcnmyvS0MOYefTqMOO78Impm+yW1deJiJk6vhLgxtYlYYx1aXaxwTlyYzLxmPOC3ns1duhmlnq5Thq9U2SvTTcumJ0dUHLfEZ3ZYTDm/EA99h5qzatmmeHOddWvqbPiU1waGT4ObyPlrvXOmJlNh/HJxIZQOKwI0cOooZDSLgqHKVNv6sDucmpDGl0nB3PS1rHjVviTXqnSKSD1FfXoSSSY4XjRLuWDBKjw5w3moOd+JWUG7GStty6n8Bj2fL7IJEyg5+Sx+nlJBhs+YbXKQFCuQaDs8KIPKirIYnby+PQuB72/KbLOinUlPp5uIOEm0rteuB0ldsVj1mmvrrNwIV10I131z2ecnRTuu7HB98MtAXkpZlRhbb4GJUw2r1nxGtlZBrQyCPqAefe3UIchmGZZj6U6vjhd8FjOzjuE3BJbI7ca4eFGx6OQoOm2qfVqBKKTp2Dww+iKsHPKwkLf8pQU02JKbCVGaRMdqw8XOtAWqm8dkqkHXxP1GLXd4Hmxc1GiVgzFZ1flWdM+QfjCM4AlBR42ouJiN2N3sRZRyBunuVlgM2eXSSoVu1YK+VhKwWJ/0aW4MhSuLbcmt87Y937bp0MbEMEgaSBh+qjOT03DUa6clhPUOzROavByj1IvWBJv3uBkOfOjSQi03g9CsCBaNqGrYqXp/8NbcZVH1+8ymrHO1Z4Sjuy3oEEeFsi402r2x0dGZQWeyp708OXALRnCG6wyIVnQLjheP3mVVnsgnt6YOwa24hm2+YI3Qq3yyyPzazeVBToSoG9zMPdk6ui+aszWpqK2Z8StVoQZM9crpfBmhXCwfacmwZK3M14RaUlVvLgi6lA5Gz5hbYU7783Y/OA6heDIt5btE1NHC1zd9WW1vvKvthNzt13mg9BVHYkpWSZZKSfG8H4rQ2ih4Q8uGAOb+dZGFJTmVcSzXSl3bHhOukZPbpD8a6xAsbXj4uohzn2QdJczFyBG0PV4dU14ajjSJmgwsLOrKWcULQyhpb23FQ03nO/dABeflcumobW8dZVIWzukZa+YTjK8krweXo2XNGSozsBun3vir1dxMP91f2JtkGI53LXQ62cnK4FzJCDJ4wCqbG9mxpMOfLYC25iRAtXC+Q4EcgHCKgd0JJrGz08su5/k9Fza8psip5XJ0QR7Pe5wVl9OMWfH4MdWTRUmAI4zNUmuVaNezyTy2eHeTH7QpNp8exbwi2TzOaTNG3YBbRSvMTMyTflGHAo8uGl5dqpDZh3t/Y+I5VxSb4yI/FJZ1IfZ6QFpyxnZrAqeypHSxkMgsVitEe35reM5cu7VLyXgt0xVNcahkOxpz5DIY4ZVx2MXtsaea5cGkc2wjnyJp33bksXQKFujkcrvbX6IuJUNDwqXbnI0KbM52mmXL5ACM5jzbgAvWCXYoyRq9kXVKXhdC59q8zIVuENHm3N7iUuOJYLk2wm2m7RaGXMymN7TcLLYGLJBnr+PXk5sm2IPW31wTWE0iT7VehnnC600wSLVyWZozttA3iyjabMVlWm7K6yGw6ZO89vy4WpS0ltdeSuc8e5ITEmgHnDwIuE2KoV/QkiaY3WJbbDYynVNZQAjXclkyp1zSDEbX85w0CVosNwm3GCBdwdRyulhCyUuoRYWwcsSbr54kZ6XOgFL3h2wdiYVwBCa541RiN7sa4nAuW4ncaraBbW3vtPABy64J+SoLHk7VUX6Yahs30sxou6B6I3cGiPvBPyVTm1JOibqqQHaQT7gpV8XZoKPUohfH4GQwYbzqdmG/dueZMgSpT23WxTwpQ326WtrKqVyu2O642PdzabYo5t3kesQ7LJQO0kLyb6zioWayvZ6a6gxmh+GWbK3LFDU7lSxFnhw0Nm12SzObUhQWTXaGV21E6RiIzmrj+hcbTDimjxJms0MTnHPn6plD+W2dtCBSMpm+qEW9qdwSbRZkVNFHVQBHzJqboT8T6EMv9T1ABcgNhsyfRS7cnubkygrVQ7uoCNgsEdJSKczFVlLdui2uAq+Vezw1zC1/SBpRKg2ZrWJam6mYtO/DIupASFsCEyRDkajmttjXxAYWRmGG5r2ZaYeEqfIZGgbKMsDpRIBFpZ2TFu2Uh95pplkRl2Z/jInNLZ3G5kWcrtw5P3iEGC0Ls2jT+XC8OUG3ysJa9tC51qP7mM4JfHbY77152UzWlXBSYw32SLjorI1UjLOjw82Dnbve02Kqi4l+TPHOMFncjYt6y5uNq6Nqzvm7GDbwuecT9I6db6Im0b0CckUvwPYx5+r1XA8M47bNSvd4ORXX5WWQa5fDmrhITjvRPHPL08orlru1TlqKaSUGs2PX6cRY6cQFziWrpW3JXnK5Hl0vstWWxrGwmQRzdHBRedhwSZSA1GvLBbMgtUAdnDW63vO1tNYUzyHFC+CCVJ8lB1VPVqajx81+GyV9mwnGfqN7DeQtyPST82Y/c1fRtNJ1K+XoQ3nIG4yfJiHPKdRy2eO8ctOb1XADiw1sLudbUDqev66z1Fnl2sxq1uRevM2724q5EurskCy27nw4HPQVf2SjtDIsvj+3+fSiz4yoPxWTFLAkZPwDhae3cFsbxhq/WW6/F05ayW5psrCL/ZFG1VvGx/n62NWosW5MxoYBtVhcDmxCbYpwQiyFYOrT5eU611dJLXJCmrv1LlpFN2nLQSJi0U4w7P2CvZF0latMrnEWvl5M03J+hX3U5uyFCxNV05xEsTKmWDlv8jzHOWGFHvesFKzRbZFeFBq/LDQC9nAbvygibC3NzitHYZYKzcsOex7UOL32xkwk8+lh5bfZXiFl/gYgqMxMjRmlqS44iRH0/KpvM3c1dYQ5a6k6J02u7gLDlbg1h0HsD5CncGYib2YcjEtzIu/OvRM0lbmy1FWMU5NoXuIV6wnRmZ4T++F6qnYxMLeXjjRWQKjm4dbds9xuu6w0ghS980oISqLkzicmL88aeiGDpZgvZirYBVS9ulJDZlGXFY/tVfvKShSB2RcDAw1jZjtQbHg+3cFzF2MZmGMkjuR2deSZ5CK2uVbly2BKN5ELvWYVmLKmiY1QiWtlMo38BV0W+Ir1bKWWIPF45+UcB30bG1ShmqKRcYEsDFiDxpiZ5vGN5lqnLDmv1UMYduoM9uZ23yyoLqQWNTqJUmJxPu9w2j2nwnZJHah9fcDo9emmWbc9r0iXjCGoKhaNVUQz2c51qa5xKaJVDwfMwjDMrDx/pmvtgGM1hoXMRM2X8HTPXVHXVNuBMqdZOusX3iqUyjbqFTXk+oQ+x7hnrDspm0zF63Yu0AS2aeR1LFhbVwXmLRZRkTlJF6UP1Qt52mFqSDc42VFbbpHl6SGR69BhoTxHAWJT56kz9bmEAXzO9JncrLcbd9qXw7RjFz51k9su6OMJ0F1Ki2OvRyWGZacgUDJU1dzlGqUoQ1vwtWo1ZGwde33P7WMW03YwaQCtSMcZc5bzTbjiVNjxQzcRsA2vqsUGM7yWtvhrfAp25Ir0pWrue6clbSyFCcGgPmeVG4ewPUs4awcrFV3nvCeb7nI2Wroi3KW+7mb8oaAqdVuhntsXGSqZvnjjbyoBxHl3Te3AEbWNQ8eXer0sXJaI6wOJXbBq06rbpS8I1A2nnJujdasB2+lzmoeRjjNZslzGhrO41vrKBuuA4WV6amO2wxQ0SRnkHAWiX2myEawG3rrCJrYHu2WEWzPLbvcTTRw2ir+J7JOhMPPtXLxE5pL09z6QWuG2N4fNCrQ9PJEJbNnasarRbdz5E9W8BBmv7zfGNIN905Ce6cgmQU5zK2DmPnoeWOakHFlhclic5o7Mo1E36y6FzXFRVbLokWxIzBGPrOaYbCv2J1Tc786R78lSUPVRr9q9c9Ed5YKezEW2pDvJbElHcFYLnySW9mXn2mqEw+0dzpMzvuWn6CKKFVgbQLai4YGHAxuR6flbLooHD7/tCXbnYkASGYE/RRwJorqUFoM3u7IHdlaXaH7pTtSVVUrXERrMl1pqM1n0vE002JHnYT/RUIZrTlC26jjNFzsuyNpJt9RygE9r3+uMmc8tUYVe07N4q2zSxfhoaXlz9sAZOq2huj52J0q6pxhv3954nWOXebmfA1l1/JIXNFTRAQFPoXzFWKLBncFWLFmmPgsqyXgh1lupcJ4eYwxCp6YZ6LUDpdeT5SnGpRmh2OhJBZVu2pXLhPNAMXhqyuxgs79Sg+WBEfzJYuonSWn7/s29TXGBUIjOosSLTnTtZLG5MpSG6WEs5tPkkO2xS8SoS0dRlxGNDjJbTAEWulefWU2JPvDEPj/GfdDzUblbLZnzZb+lhZtIpUffR3VOLxPxlk4WtuZ023oiSY7uKZR6cLs5dSXPqyquOdTwu1AmJdVMFywXMQZrnSdstwe2h1+0TBXz9Ir2ZY7ejkAeaMVLvak/LT2+0NYocWuvUZxJNMPDxnW9Z8+VTfvXeXRyVvujSuHctLPCI5rXsw11QOXaP1z54XZKIcJLsFxyYd8S9ESa0HsbTfpjLgjCTz+9fH4Zn4E/n2T/S16Fj08R/2UPMx/PHd/fhN0fZQPL/XrX9fVfY+4vn18qJ4TGPh70wibWfz76/E+Peb/8T96tjJKHx1vp8UXftXl/idBY/vgLWi9h5rZ1Uw1vdZ6094fQn6E/6vH3Quq358P2lzsYadHcxz42D68sNw1hf9qA6q3J3x7Pv8f7YTa+wwJu+P3Sfz4a//ziwgqehk79RrHMG6iKEYrnOxuIAPmKvxIvv/8fckXpWiUnAAA= -->
