---
name: "rar-cowork-cookbook-scheduled-brief-configure-and-management-office-apps-and-add-ins"
description: "Schedulable morning-brief email summarizing configure and management office apps and add-ins for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_configure_and_management_office_apps_and_add_ins", "rar_sha256": "bd1664a0b96581daba3f7508773637f584057395d251a1354370c23afb97ee44", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_configure_and_management_office_apps_and_add_ins`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_configure_and_management_office_apps_and_add_ins_agent.py` and in the RCI capsule.

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

Configure and management office apps and add-ins Scheduled Email Brief — Schedulable morning-brief email summarizing configure and management office apps and add-ins for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-configure-and-management-office-apps-and-add-ins
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_configure_and_management_office_apps_and_add_ins_agent.py` and embedded as the fenced Python below (sha256 bd1664a0b96581da…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_configure_and_management_office_apps_and_add_ins_agent.py` first:

```bash
python3 scheduled_brief_configure_and_management_office_apps_and_add_ins_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_configure_and_management_office_apps_and_add_ins_agent.py   # or on stdin
python3 scheduled_brief_configure_and_management_office_apps_and_add_ins_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and management office apps and add-ins Scheduled Email Brief — Schedulable morning-brief email summarizing configure and management office apps and add-ins for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-configure-and-management-office-apps-and-add-ins
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_configure_and_management_office_apps_and_add_ins',
    "version": '2.0.1',
    "display_name": 'Configure and management office apps and add-ins Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing configure and management office apps and add-ins for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-configure-and-management-office-apps-and-add-ins',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-configure-and-management-office-apps-and-add-ins',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7edbc27f1186d39a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-management-office-apps-and-add-ins'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-configure-and-management-office-apps-and-add-ins', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefConfigureAndManagementOfficeAppsAndAddIns(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefConfigureAndManagementOfficeAppsAndAddIns'
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
    print(ScheduledBriefConfigureAndManagementOfficeAppsAndAddIns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816WZOjSJbuX9HEPGTVkBkCsYlsa7PLog0hkEAIRGVZFPu+g1hq6r+PIykiq7q659627oeriLAA3P3s5zvHHf36YrZNkFcvX18U18xmGzNJwsCtZmbmzNi8y6sY/MtjC/zN7DxrqtBqm7yqXz6/OG5tV2HRhHk2LbcD12kT00rcWZpXWZj5X6wqdL2Zm5phMqvbNDWrcATPJ0Je6LeVe2eTmpnpu6mbNbPc80IbPC2K+j5kOs6XMKtnXl7NmsCdVW5d5FkdTkzyLnOrv8yAFKGfuc6syWdVm80cwGyYgfmd68bJ8AoEdXszLRK3fvn608+fX0Jw/fL11xc7Mev6u+Cuw0zSsu+i0Zlz+BBMustFA7HAY9pxdtlkgMTMfECgGIAFM3BfuBUQNAWPHKD28+6H2k28z7P/+q+4Myu//vHrt2z2/Hx7mX5kIPSkW5ObdQP0sM3CtMIkbIbXGZ105lADtZu2AmYwZzVwQOa/PlZ+p5QXs79OYz88mLz6bvPDt5cciGBO7vn28uNkkW8vwEDg+nWiUvzw42uSd271w4/f6dStFbl2MxEDUr++Pe+fZMHE71ND7871r4DqIxAs99vL75SbPg+5Jz3BypfXKA+zHx6Eiyq/uZmZ2e4PP/4jssAvdpyEdfP/RPenB+HANR2g01PwHz/fjfzzDHoq9EHzH7MtgFv/GU3A9Hd2n2dPQ/0j2nf7/w3pJMzc+sPif5fc31sA/XX20z/U7X9b8HnmfXvh3CS8gegAifR19uubclyxP31yvj/89PNvgPT/lYySt5V9p/AGsjj03Lp5e/vpU31//Onnnz61BYg110zf2ir5ezT/nl3vfP5gweesH/64FvBXszgDODD7iPTZr3nxH9Vvr7OLmYTO9+f119nv82X6QLNJiXemDxP8LmdqIOvv7Pjjy28AOjKgTWvfh0GW/+d/zg6hXeV17jUzxc7bZkKgJkzdSfhzENYz8PvALWDXB2w95oH4nzw8SZx7s1/+j32H2i/2E2rn9Tsovd0x9O0DMd8ALL59R8y3B2K+TYh5HwKI+QbE/OV1dgZ88yr0w8xMZjJ9PH6bFgGQBTIVAEjd6gbQxhoa9wvAqS/TxSzMZr/8q6zf7lxei+GXO4SHD3ST2d2EbDUg/DpZRwvc7GkLG9Qdt3ftFgiQ5DaQ1gsBWn+e0D5PbgAZJ0vWcZgkMyesgNnyarjTBtb+OhH75ZdfLLMOvmUPKEZnj8JUz8GED3FmX74Atb0k9IPmW+baQT779Otvn2b/PfvfVt2JTzyOoFo8fQkk5BVJnIHcbCdLADeDwADAc/flr789jQ/IgAo1A54PvdB9LAaxHbvOuyeULf1lgRMzywUeANZPi7xqpgIZNq+znTf7kBcwnYamChDkdQOKXuFmjpvZA6BqAnU+LJnlzawGAVx7w+dZW7t3rr9YlXkXMQUgYTa/zA7sEdSbPHkvmtMksDjPQmD+jzh5PAdEqk/1jHkn8ToTp2ieFWZlFkFlPnl45sMvoM68LwfEzVnmdt+yqebeg+aeWg/zgEnAMvbTpV8mn4PGADQJmVO/877PMaeqeL5Xx+pbVj/TxqwmV9igjACmfhs6UzH5yzOk6iBvE+duP/fROTy94Dy9co9B9p9tQz5ahdnq3tPcO4bZt3YBI9js/9cGaNKU3mzk1YY+r7jZSjzL14cHpn5uYvpoAUHD8WQDsu17E/IOYe9I/i1LQhBO1fCXx8y7355zHugI1HIA4Mh3+iBogAcmuveYnmK0qqZsML9l7yXjMwiTOz4CtwIAiB+6vDOcRt8lDUCWT/ff24d7DFTOZCwQt7OitRIQU57rOpZpx0CqasrLp4tAgLtTjnZBaAd/0GoGqIM4AvRnQIgQZBqw7t10Yg7UBC7zqjz9Pj2cmjIghdPaQFrQMLuvMw2k1uSBGuQz6KymOcAKn+6kZqkLbAxE/LBwHZjFQ5ipx34KaE6+yFMQ8b/3wHPwezLcZZnEB1RNx2yALbsJvB23f3j2Q86nr4Cw6ZS+90V/dPdT19nva9tfvmV3GT/qBUCFR2B/N84MZGP6CNIJ1GoATKn7EaePDuD1UcQfXcKHLF//tLH44Z/be9zLsvpHz32dBU1T1F/n80cpfa+krwBS5iBGwsKtv1fVR2J++UjDL4Dll+9p+OWRhl+mNLwPPdPwD3wfZvw6++dk/wOJZ9B/nSGv8Cs8DQmA7RTVzw8wFfuFuX7BptFvmex+j4FnoEyADdLdGj6q1/sUUML8yvWnyY9qVk9FsAN19w7fwEvfso84eWYRqA6ZP5XeOv9ddt/LOPD6w6kfVQYMZQ3g7UxNo+9OO61kEr92X75mbZJ8fsnM1P2XdlhTjQExDsw07dhAvoHurAnd+91Hpzbd/HEves9EACFO/nVKyM+zqav+PPtokD/P3rcs9+1h1oI9209Tcz6xBFPBv4+5Hxtdy30Bu8dmKCaVHvuwqSd89up/FmLKQyCx7U59Q/6R2BPHPxEBF77vVn8mIt0vzOSJLnVjTl1A2LxjwntEf54Bp071o5qqSQsW/JkN4FO5ZQvKrTOp+91+39XKH7r8djdD89jM/vryjjJPHzwbVzAdpPOXeiq4cxDAgCG4f4QaGPu3t7RP+gA3QcsEGFgOQhCYCVsUgS8Rx7RM1CNxeEmSKIGSHr7EYJxEKdxZ4IiJoDiGkrC9QE3PokjXxTBA7xHQb1PXEU4yu7DnohSysB2UWOA4RiHkwqQcEyNN04GXSxImPQeUlu9LYwC6T0M8FJ+s/NFdTwZ72uPXF4vAwMwtVu/ox4edUxfT0o9WH2yhMaF6+YyflNjvnKaMC7eRjNVlcZQP5LZJGr4UO5gWO55dsvaZluJDn4v8wYsv0FWn+IzqsBuziXGn2Rt9Ka7WG/xmLSgvQ+CO3Qlyaae6m2i6UvvLtdwaA66bpdApRpWprIGBdlxNUtM4Z5dbf0jSqjng6r7GFmrqhaqZXdTbOMDLuRjm3cifzXTcalBam8uyiBSkaEXhqB1dllCoEVmYaiFXhponCnKwItW5lvh4OWOn0uKJRJX8IQ+HMdb2HXllKdHZ65pl2dyJcD0hnksjP5jtWC3PxhLxMhTTw/UlYIK8lJKthoil1jY37GSpasj2WRXxZCCMJSqk/WVfxYZxzlvDSiiMDvVNxmOrgFOVq0oWrrDE+dFQOphPzUV7um1guj0om3p7kUFXpoeFdb6e1AtRwmA0PCzTpIWdcbuHF3ZJJLpz9GQtbS8sOQaCIqfcLpGvaHfbYWN2DRM1jesYvu0YGivS4YpKjoKsRafKzB4lwyPdOp1idSvG2Vz4EuEMGzuS3YUT4LQjrs0AXzh/XsnHXQs2rmytoSaSymi52F00sw1Plr4dD1F92Z6sc1GutZteZ6ySHveKbEixR0pyArqR7GJobF1xS+rEny57LlP7hFc9Hd6Wbhl5UlwiSzTyT6uA0CXyWKeN562E1mlNZgEtuFVdr9a5pi281ly2orQr1wpuy4RBeKMSVrpRiteiMjNBXq2rUzXGEQH7NrouoX2Z9cm4gVZL+3Y5DWuY6oKdBaWSdAro3iWCoNy7cO8e8QpBjLE2ibKr8azGTiif4V7KRyLHEAG7uGSNn5zXmHAWWzaVtluTcUaVcQaVzgndO3BIhIJo3N3QmByP3fmG6WInHDt43tuVLvEHe3GEuDQmsogkrHmQCjl6vGgOSQahebZW2nJ9vhbOZWto6kEZHK28sHUYNSEthsNiuT3UGMIOYxkhXLBshkuV7hdqdljXt1CKCWPTZ8o8oLOi2WvsmKyvuCQ6YXOVDrSiH1RZRTG5WGP7Db5xdintCITcXboV75xwQ1+n7XbV2W6Lo2xYRxUFO0W9CNr2sLY2fd4Y15Wp7KVUXI+JL2+urX7dd7s+qEiaHEziOpLqUaHwLC0tY8tbzmm3PNbx3DBJO7Z6fg7Nk3y90SVPFKSEhHRpvOG7KqRg/Too/qYgkMgcedB9Uy4rbGxtIS+JhRiz6nm+NzJI8Iv9LYcP3ImK22SDU3l4g5VLqI6MHsOCVIIOAREcCG3Xsk6d2lxFHG0fjSM5V4jz/lqN3TLUfB1PBmX0alLLEg9BBKVay4V8qehLEqmQg8EBqxKZ1uQus8MvDgyrlwqHdwEOXXk28CmOxGIRn6/htlr1F9JXzktFoHJzfa3mEL3TCrkILnN4u7xa2B6rFbiFtUsPBdwYQKvrwl2czOVqj5GM5dWxL0vpiggW0kmpNmu4H6XWMQyFiSnhZvbslljZKMO5sjmOwWgy2DGt6gTESY3K8lggYVPyi9sK0mXHkxY47Au79jDslzt8i4qjToRar1WLyLOWaMvg6VwjLK8kffsoEPpNCPbULh72gQceX4s17Wnh1XGJWNLOu5WNMUUMZWsuOim3PmXwsXFKWzaXxFxWj8dCwhhOYvOEX7iue9Thy6GSK4y+cPE+42sItlE/p02GXtDrW8KE28UO4WUfcWyubGyhXiWDkQXYFRYWvZE2IsfRpr2BTkzQmEMrXozytErOFptupfKwSxanmrcGbGzEw8LgFHkr6putZx8gbH+WymuklTJzsSHWxiUH66BwPJxHKGxrAvKyAqM8NNkIuxUdORpGzC2uZfZHpcL61slq+xz5zvZcgHzz5ikrz1OcDBpEFNpToHfcnL+5c00kSIryjqC+QDwwKLRCmJQ0cBxv9/ppj3N6GfM0U2zr22Efl33aDOhY0CY+v+ESL+XzHOVkgymFAuOMVExAZMbIzo9JclWthMEcxMo+qnqbJQDsYo0l4ou6SY7GwdF0UEAO+1Fs9rUUynCbENIirin83C6126grBc+puXOz3JXV+B0uZbK6YDbuEuwk19uLBgtcSbSQoMl6HZRntd0WHtkMp8tWMyNPb/N6N0ftiBGv6Gbc6IdxtWFKSdPgg5FHECLqdL/29rJDmevRiQYdZrUOS6MLO1eD8zYs61z3xBajcKln4FpcZYSU1XrUaVjEL1BJiSN2cCvhIul2EiMnbyU7sEK7vdbB9dU1b9eSVU5CznYuQfEa3CkuueY0AimB6Pl8NSh9cas2ot3RFt+fw2pdkm3eeSVWCJq+R1BOVVdIwKjWYpPRJbbRafO4Vg1BkGJSz4LRH/a7xXrM2ZuOGEiZL66iHVRMGfI4Yxy8/a3UoFvV2FnO7rK87zbuanGQ/BsI9h7lOn2lr9TGV7Ir7S1sNvKzuKFEIM+p1fTGh6VSiB14PJtyqp2y/IbrAI98jECv8CbfFtnRGcKb2cjdUmAtuDivU16en/OAJw4I36zWxgUzaoCAGj0X40g1FhqP5jkuqSK8gYwmiVsmCw++d0UgbBmWFh1ztNYcFmXRoeJWOQ47PjwJIuuhpr4YhcGW2lImxOwoqkwZi3w7J5bqxiIvckkQws7kA2Z9qxbZ4N6AcVc1Iu19WiPp5YGOoG2w5W6cv0pvKAahi2OVFGqKwlBtaON6OBQXt0Frjr4yy0Y6GbXEjVbmh3sB4RiOts4sgt1S9mJH43Ub7hDWMoM8NyNC0oQaOZbE0hxkzijVJB7LPXM1rLGI26XRBYJZrmUGobTCb7fOlY4DxBNdij3BtLEWEmezyrN90Cc6cfB2J0fd9FoNmohrsEs4ligybOMaG/yMRwFcbNlB3XjpuQCY4+58kAvX/alf1TtAs+dv6vrQNmHaniy+ErtN3bpKlyyx/kzjoe43gi123XYsKUjZxysyWbOXkaJJ9oJDJ3iQM2OR75XVkbYup8VFtcRDspCarcFa28NGVGE0Ig67XmGkdGzYpXKDGUYiSF6+EO6yYP3DriY0ku1F63LBen5RIYZ0hXdJgzeuSCXLQZ1X2cne77IlvCIStE/QIF/4VIkNrqCJN+NywY0Bg0q+cg/eZS3I1DmypJZU3fMV6kIP1/qtIVKdNyzH44CzywEr/GwurvT5Lj0lSE8hDdGqh3Jbhnm1P+V4wVt+wQqZKDFtp5w6YTxXsXgt0RSU7ZMVb3bO/BzXuqfGztKRb3B/3jhC6ZhxxfrVqtJyx9sJdabJO5AeTsMgGDPftOfDtodh/rymIUdlFXm3os5ldhQEbd5t0oTDAGIG7S5GUemCCgrkh1c1GLenKvPbAj3koOnbJ6tEsaDyADOuN1d7dx+vCzR3sg1eL+f8qmWLNqcO2OqA2KYQH5mTpFY4oM25IBEPOcLherc5zHdBRNg3X8hPhtShu1vEZ1FGlh2/VrR8JRvuQHT7Xq3dg6BanoWcLYopNfgkm46/dvnc5ejV/LRED6FvnsPW4rgg6Aq4n8fRyoQldhlpmJtAhoKriHLNj4Gfw8wVVrXR55i161TrfL0MMgXsbvqEsCxyqVzKlCsjxqXpRtT34lhi7YCjIsxe/Ihfj1zq4dGxzhWi20Uys78dO1sOzCvmrq4x1o7nQzmYONRUwI/JHskJ4nzcotq1dm4brnRpDiDG5UyKgrPVHRTpz6edn5tUCUHnJtoTaQwZRRE73K6Ihs2R9UFMXoiKNPRq6ev7o7yAKmK0yYsFGcfKyM6ZqTPjkZ3n5/GaOf3BGfDDfGlZ0tBwntMfE3V3Feox3mR66Y7KQdQ6pVPO3inHGGhf2TcpTweij0CvhfS4mNV8sUYINY0SfH49+Ycb6RW3ljf5HSWRtz2xRMnkam/4s3/qrim570USa3pDvF1xx7jEESVtL8WVYyjYhYWNx5TX5VIDCMPJqQU5DY7TyLCDpK5HUYckUIIYtztsnnvzDOfnHZ2n+tX0Fp6HhZ5eMWSJtraXpaJV3xZ+QfrkoA+7vizzJXfOmyXvrPEO6yWMyjtARNz5/mZxw3njfIo5OWqGcSWdttg2ORgxyu5wrk6d3hGG8azMnfGWuqGxsYmRR0viyHQ4XDfJdQjULSjZY3x0V5iBi76VayvtZMxlaANdzz11UKM2pNrUh6P56jQe9ZMl8jUJh0gNWkCIJE+3mB+DGzwqmlJyRgBFBLfIvK3LKTENa0tiQ4TSGJyorWmuqdERSMmca/PmCpFy6AubaumdzqIve4W/bG6+u/dJmaLOK0hrdbN2VMYMGOp6kRdGZS7mSW/hyvaCRHRN3RChlXJqoKLxlqz67hzvJK9t0PHKrqCV7Akg2ix0F4oyS2HH621NsKilj4rDB76db9YQFF1VETvTx/WSWl58sMHaRhsdtt2L43u7UeVbEhHywVryDV1gKapr9tyWsVw73HxGWakjVAXUXMsyiphvMTOAYAbZiddDdGwckbe3K7n3Db/1zz7LNp1xlXgmOOinSwJ0Br0Cshl2lzO6lDNQXzqIvm1JX2s3LsmSq5OIZbpN7YSDahsCY1DFYvRW0iLIoz3jQmjIHuehUW1vVSk6mTPWJHND/VOTZHupoq/rOYGBIohthsC3lpTNpPV2ZWRbw7Mk1ujJAdE4x/O3HHMVGxlBBnSDVhRVkrtMK4mFA7XrKBYpxXCyHdY6wUDp59HHY5hla7JoexI+VBB5OA80Fm2XnRsty81l8LiekAmuLqG8uF2EnhVbx6bFub9pUIsKuqWFNC0CyangWVAIoWQzgn2qw3DHkTs6c08qTsv86LBzjtgxiz2JDtsQOtVIm58D1K5dsWvIjkXlqllw6DwAynI7sm+vkecpIuKuImaNJuujDxC9rKQyNT2cFGiXMiMqaracGJ0OwkLAFK8Pr0zO8Oe2qrDa9sj+snLAeCKdT6fjKW5xwyKoS9i6aIopK8TzYUGFxshniI2T+TSnXresLRx0RkzJdJ0zhGm6TUsPhOVSpaRH2e1KbaR+47Ma06ypbF5jzqknXS/CdkK74KtBQBfb2BfO9NoWuMCy6C1HHPJDeUv4hhlPnLSVZJ6NcLUJ2su2PcOXRh6WLI5e+T5ZrlWUg2DFQ6ld2CpDy0schAiGx4eWLoTSet4UVrZBmSKZnxHXxTbhdXs8CpnACwS5DftAnu/9TT4P4THTrSOpDyd7XiXdRqKjKLg6x5JdsaJI9/yePMrOvgkFoczG/ZHfYBDEb7dofpFszKL31NplA5bMIlhfMuqiWRonuqJp+q8vn1+m8/Dnqfa/7T35dJr4bzvUfJw/vr8dux9ru6bz9c7r679P5J8/v1R2CAR+HPzWSes/j0H/5tj3y7/6zmWiPjxeXU8vAfvm/eVCY/rTN7pewsxp66Ya3uo8ae8H059frLaevkRSvz0P4F/uRkmL6TT/b4wAnphOGmbh9Hr5rcnfHufi7sv0dY/pHZfrhN9v/eeR+ecXZwBxENr1G0rgb25VTCZ5vs8Blli8wq/Iy2//AzHPhfFfJwAA -->
