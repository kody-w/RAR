---
name: "rar-cowork-cookbook-dashboard-approve-budgets"
description: "Produces a self-contained interactive HTML dashboard for approve budgets - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_approve_budgets", "rar_sha256": "a7c07b5731f5ceeb9c8e8d25b66ff26f0ca2fac7ea3c514d3b125d7d85253ec0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_approve_budgets`. The original RAPP
agent is preserved byte-for-byte in `dashboard_approve_budgets_agent.py` and in the RCI capsule.

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

Approve budgets Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for approve budgets - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-approve-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_approve_budgets_agent.py` and embedded as the fenced Python below (sha256 a7c07b5731f5ceeb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_approve_budgets_agent.py` first:

```bash
python3 dashboard_approve_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_approve_budgets_agent.py   # or on stdin
python3 dashboard_approve_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Approve budgets Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for approve budgets - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-approve-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_approve_budgets',
    "version": '2.0.1',
    "display_name": 'Approve budgets Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for approve budgets - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'dashboard-approve-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-approve-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9bb8ba26f7d41ca4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/approve-budgets'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/dashboard-approve-budgets', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardApproveBudgets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardApproveBudgets'
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
    print(DashboardApproveBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZOjSJL2X2FzP1T1UpXcINVYmy0gCR3oAolDXW3VHMF9iUMc/fZ/fwNJmdU9PT07Y7YfVmWVKSDC3ePx4/EI8tcXq6mDvHz58qICK0MkK0nCAJSIlbmImLd5GcNfeWzD/4iTZ3UZ2k2dl9XLpxcXVE4ZFnWYZ3D6oczdxgEVYiEVSLzP42ArzICLhFkNSsupwxtAlqetjLhWFdi5VbqIl0NNRVHm8JHduD6oK+Qzkhcgq+A0aESP2GXeVqD8hGQ5MqNYBrEcqKVCMgBcKNzukToAyC0ELShfoVWgs9IiAdXLl59+/vQSwu8vX359cRKrgrdeZm+q+YdW4aEUzkuszIcDih7CkcHrApTQuhTecoGHPK8+jkv7hPzXf8WtVfrVD1++Zsjz8/Vl/Kc02d2eOreqGprnWIVlh0lY968In7RWXyElqJsyu+ME0cz818fM75LyAvlxfPbxoeQVGvjx6wsEpbRGrL++/IBA2L6+lM34/XWUUnz84TXJIQIff/gup2rsCDj1KAxa/frtef0UCwd+Hxp6d60/QqkPr9rg68vvFjd+HnaP64QzX16jPMw+PgTfkcyszAEff/grsU4AnDgJq/pfkvvTQ3AALBeu6Wn4D5/uIP+MoM8Fvcv8a7UFdOu/sxI4/E3dJ+QJ1F/JvuP/d6ITGPHVO+L/UNw/moD+iPz0l2v7ZxM+Id7XlxlIYG6Vlp2AL8iv39TDXPzpg/v95oeff4Oi/0cxat6Uzl3Ct9TKQg9U9bdvP32o7rc//PzTh6aAsQas9FtTJv9I5j/C9a7nDwg+R33841yo/5zFWd5myHukI7/mxX+Uv70impWE7vf71Rfk9/kyflBkXMSb0gcEv8uZCtr6Oxx/ePkNloYMrqZx7o9hlv/nfyLb0CnzKvdqRHXypkagg+swBaPxpyCEFam653YJIK5VCIF9joPxP3p4tDj3kF/+27nXTVgBH3UTe69335617tuz1v3yipygwLwM/TCzEkThD4evmeWDrB6VFSWAle92r3I1+AwL0Ofxy1gZf/lLmd/u01+L/pd7DQ8f9UgRV2MtqpoEvI7r0QOQPa13YNkHHXAaKDnJHWiGF8L6+Qmus8oTWJjrce1VHCYJ4oYlXGhe9nfZEJ8vo7BffvnFhuZ8zR7Fk0IevFBhcMC7Ocjnz3A9XhL6Qf01A06QIx9+/e0D8v+QfzbrLnzUcYD1+4k+tHCt7ncIzKYmhcNGqoDF1nLv6P/62xNVKCaDRAZ9FXoheEyG0RgD9w1idcl/JhkWsQGEFsKaFnlZw4qMhPUrsvKQd3uh0vHRWLODvKoRF0CGckHmjORjweW8I5nlNVLBkKu8/hPSVOCu9Re7tO4mpjCtrfoXZCseIEPkCfwxmnkfBCfnWQjhfw+Ax30opPxQIcKbiFdkN8YfUlilVQSl9dThWQ+/jIT6nA6FW5Am26/ZyIJghOqeDA944CCIjPN06efR55DgU5j5bvWm+z7GGnnsdOez8mtWPQPdKkdXODDwoFK/Cd2x/P/tGVJVkDeJe8cPWnrn54cX3KdX7jHI/x3xr/6+T3gna+RrQ+IEjfyf6DHupkuSMpf403yGzHcnxXxAOpozQv9oqSDn33Xf0+d7H/BWRd6K6dcsCWF8lP3fHiPvjniOeRSopoQ2KLyCvC23vMu9B+kYdGU5hrf1NXur2p8gPvcSBf0EMxpG/BhobwrHp2+WBhCl8fo7g9+dClGDYQADESkaO4FB4kEgbMuJoVXlmGhPf8CIBWPStUHoBH9YFQKlw8CA8hFoRAghh5X9Dt0uh8uEOeaVefp9eDj2RcXDvS4CG1DwiugwV8Z4qWCCwuZmHANR+HAXhaQAYgxNfEe4CqziYczYsz4NtEZf5CkM4d974Pnwe3TfbRnNh1It16ohlu1YZl3QPTz7bufTV9DYdMzH+6Q/uvu5VuT39PK3r9ndxvfKDtM8GZn5d+AgMIDT6l5XxypVwUqTgmcAwUi4k/Drg0cfRP1uy5c/Neof/71e/s6M5z967gsS1HVRfcGwB5u9kdkrrBEYjJGwANV3Yvv8TLDPzwT7g8AHPl+Qf8+oP4h4RvMXhHjFX/HxkRw6YAzX5wdiIH4WzM/0+PRrpoDvzn1GwFhak37M5TeeeRsCycYvgT8OfvBONdJVCxnyXmgh/F+z9wB4pges45k/kmSV/y5t74QL3fnw1jsfwEdZDXW7Y0Pmg3GXkozmV+DlS9YkyaeXzErBP92djNUeBieEYdzNwIews6lDcL9673LGiz9uyu4pBHPfzb+MmfQJGTvST8h7c/kJeWv371unrIH7nZ/GxnZUCYfCX+9j33d8NniBO6u6L0aTH3uYsZ969rl/NmJMIGjxvaKOnPTMyFHjn4TAL74Pyj8L2d+/WMmzLFS1NfJxWL8lcwXtdGF38wmBToNJBvMGlsMGTvizGqinBNcGEp87Lvc7ft+XlT/W8tsdhvqxEfz15a08PH3wbPrgcJiHn6uR+jAYoFAhvH6EEnz2r7eDz4mwksGuBM60OAfnbIajCI9xALCnzgRMXJKxWdbzSNbDHYuEvM8Bi3IYgnYpmyAZl3MnDMlQwBkNeUTit5HYw9EYgHuAmhKk41IsyTD0lOBIa+paNGdZLj6ZcDjnubDYf58awzL4XOFjRSN8753piMRzob++2CwNRy7pasU/PiI21SzOkO0uMKYD65l5NMnXqpI3eGbh2TmrwpbL8tiN0JaMiTnN8mszDhpBX/pGvO2uu/V+2QuHVDXKxvN5X90m631BFAd5vTMN70aVuMcwLGcKyiJn9le8KTaVfFpr7IrkJO0iTshBb+SLhk6B55DAsXf7heswKJYts6lvl94qndOX7hKrXSZZ11KOK8XhYkdaAjlpr4MX+FmfnBLV3yXRAthJeiXsswKq9aa7cFPWvB0kB21DUkrms3ReELVetjoXN2uLXfr4Pss6+jZUnZNyFelV3EHnJug0nPrcrFi1uTWxbHAl8VKGbqXyeubUdKftLvjsMFHKjdXXijXZknm8yVJwu5knbdgc82OR7oTYtfZBe8jW+2OdEZpVldKBrPKLX6rGxeROQaG1mzM+9dO+CSLtmGwIhQxdnYCdW4Rbs0wKrJBiiURNmNRPU2WjhdsEi1cD0+CxkNitbxZDzwbz/kgfGPW6mLc16WnWpWncySCsiKRRB0vkg02mucf0dNNM2uCSUGVxktJVR1vdNvuTllnsYjHIDIzKshAqZq1YUmMd2f2Bs0RybvP1Lc13VneZTIoiv6mJZpInzNUlgl3fXKW4iIp/GKh9JkjxzjkN2U6Zui1aJHJE0yfOZmG08v2R2HLTvmcJBjteO5LL5csA9gphkrd+W+oobgjnISSrNpjVEr2VlIJL1kAqXU1Cl6HAEHq0baVy69m6l7Zaau9OF3PKXmslCUusYjeUvzYaQVZP1aU/7wtmNqvPXbBIyf3K23oNx1oVpbkaaaIpCX8C2+gumTUIvFIF65S42idi46nExlUNhh6GyzDdFwY7z4Z4qLMZOl9OeHHn9Xh3vBxybH/Aiuk+oWBGtvtZbmTnZor3xgXE1doaVvV1Wm7bQp2XxMUqpaA3IyKi06vMb812F+pDRFwpdDitiLJzxNNeOFDlRXWcQB7yrLWT5KoX6XZx0slZvuSbWMsER6Diy3p+W/Wq65/caB8e8WOq93s/j1J5t2kZSD5bZ7/O6eoi34K5uTSwYjlb7ZZNOomX/m29o2WTw1SSnugHerVY0nbWnBSttd11fBhkxwbaat0tbt4JE/vjvilTesVpqAHUxfSkeZLVoxK/nUnVid9F0tXahzndxnZBU0Jrdut8FhXHCmsd7aBNxew22xqSnImqHur8zjJqQWoOkeMnxxCb3OL1HDQZs4hYJT0nLTmHG5hyaNVUN2/EmlUn3rXUU82rp61fWnFSrcDSYg21T6yAzLpbsbDSuXrWKJVWQL0iZ/XyfF00+OGQq20p6s51Nyy6VFly1yWbAbReHSsKY5piGc/jRMHa28XfD8fEvPTNYOyYyTRKCWq1UKcVTySrosDZgqvOnc+dNsoqamgll/0q25JEHCu7lokCd+ndJpUVLxkNRxslyPHudqDQRDrJebcbUGU3OwJmp9AewazieJkv19GFXa1SKt972NkQDnlcpIFeN93uPGM5FpVMTwDNzMka09Qk6sDGPjoz9pK/oGd0m628iLQvaNRtNxdm03UpT/ELab86yB5b58f5xBDYvmDQjhPXg0tsmdNlY5TEZEFU+8X+2sJcOmmKbe/BSj7N4wDn5xeQ7x105rarQCE3tG3Iza5T+RzrpONqXx90mrtIe9pUNvwmV8XbVU83MQ9cFYZ1Hslb0iF4fqOUgt5Yi+1smbgnv7zN7Abo+GJ1Jq43Xec1tTpo9uG01LE9Hm+S7VCW3L4xChLcKIZm3E16jk9ROS3d9VqJCYwVNrWbnhxRtNidOGxnGNoexRuM1j1lnmdhIWJFk3jnG5eHqO5NJhNwubXDsg/Qs6uKV4JictsM+JMqLtWkzh1iMIJASMXQUJmYUGzcHTBHqPdiXoRLf54Giw5wQt6j6QyS4OF2dS5pb6VFb+N8wpphE2f26cSjwZ63ixOf4EvWPDWhZm7Cs6y126VZLy6nCLVkKlKv0tHNWh1PzJkaU1Jv+n5trDueVc0ZPTF6LKoF+mYRVZadtCKmrLB2S6kubezCOR21ml2ZQNYVNUYnOO3jhzO0peS7W0Rv4ile1NkwJS7+ZN7Yle04SZNZDn7yl+i+T2RbjJUrlWIe2aacQh/j0qWNJbPvfEHxmGhti912dhhcPNlwLGXalnI+gmzjSKwbmseB2Awn47LW7UNxsondfOfszzZ6CxasSgq8LCrnklOEHDeqIJBBKKeliYXMuuDzYIMK17mk+kEvzkR/E6Jtq4prrj+WINllVo/vzhtG1dXg4kckVq4LsBmOazu1JUqy+DS9+fueAnOCrDVcMJ3G9Hc3UbErOtu6ARFusmBHiEMi1fgcdRsvVQJTuFG73TqUOkkrDSKwARGT03mparJeSYrU5Zv6FOvRhtN93K9FxtArAe8O5bJwfSfeBf2FU2GmstsAMkSy1DjhvLqIy+NiYAx/iw+lO2f0ebafu6QIzIpptLBfr6VEWFfoqs7XArvQT8R1e2i4FA9Qa15vt2cJY20KbQXPyQx1Qktl5l8VnRdC7kZWgeCiwdYqrtfN1V+u2+kUnRrr/RTb6OxshdvMjFrNARG5nLhi3WVmqxZxOMmXCwp3Zj3nKeylJM39msRrlADLye3Y9Wup3WjAHXBsxYkLMeBJS77UOtnPndmmOhBhsw27mWfWy96tqAvrnWuzZ4RoLlvCibXwwuinjjMr6EDQpZ2eKLixjuX9jnOhKxNQL+1kpjTomM2LyJBrrRqMdl/44mxlDAY2v4ow+Lf7HUUuFCNMr8qh3IpJSud+h3Xizo41Z7Vy4MOVUpbT46yM8YxWl4x4kktQLFXgBlrNY0mnotEuk2aNq8lD2tVrE9+rIllV2sTkLMm8GvmO2y4gha3CcyqHumKVq6MuHLWttjhu8HC5Yhs33kXqOR+OV3JV0sFphVOCJC1ZIm/oZcAQ1hkrhiq+CmdpKLg5JJO12JTiMdL68y2ba/SVneJVg51SV0TnVymqJL3aKBQ6KdeEzUsDqXCLacYWzlwXLI7pGGeLs8dJeEUTGvYarisXNzFahC62yfI080jeUhcYawlYWFv9OpCDTbdxDD/YzBMF5f0j7IK27vmQzIqyEFViqq2j/EoUg283czHaTCgGU7yrKrkja3TWFFPwNpAWYUqb/co29No681Wg4qY9CFDt4ijkzoyBey9+28bStaozFdbcs1gkClUIqkxtr/b8ZpReOdR00m7ml8hN5EY4Xlha4C/WLm1TVWdqG5/EobHd98tTft41u5gQIthGYWbhibHlc8W+G84KbMQX7pCfnelmPiumpsqfN8Fpcr4Wp3UklXwjJPuGO57Xy2Z7AU6bDcO+XQgznNE4PUhUt+HwFDYdvnILhsGs2EuK1ZdzyuELh5qY84ZvIosXLiR7GTKhPQADO2pWrFMXetVsFfxULfEEO5d7URyETrHcw864nouj4F+HmbOd+e1CPQbt7WiQS4W0Cn573pJyojLb7GRhehfOtM7FefF6KIojfam2mUBNpxNaTNcrRb4eddpsar5FPcWPrfliQd8id1vIUnS4pov4Jm7FUiyThiAiGzMByGmKWBiKQRTRZpXLS08DtazvNU8QTy4kZTx3bWmKR4UZLptFTUzxjvLyncK5mqnd3LTAGz4pL2eGDFrP0G+UXec3FzZULQP3j0QqBDbZ08N14x35jZWBZukW/Wa9oKoNuKmWvMJ46sJ79amZNnrqo1Jn0Z5VOtlpER4VwU6t81TZh7tZSHWWs+47vmoJ/XyybKP10tyyuDidBrV/IA4GbKa9ZKoqFHRRxpaG4bdzixLIoeI4pgccpulZlA87bgNN8iW8xfY5Q7X1bUGlbLvMJxMM45gCFgEeX0OmNLobRjdeVq45mWp0z0h2Rh7heH1dXRujnQH8gAMlo2+NMCOmF7c59zPtNA0ObCC21vYwL43oOBeXMytWtsDEckUR2BNgD/levGBa7C33sKvEr6TDcbFJ78ocz8m94E+ps5TXgGeXTbZjBuO20Z026WDLs7H3Wyy3RUAeLtzkzGcCoHyAZR6NSmjPRtXWD6dgpfs6alCeqU1Kx3OJ2Dp2pTNpE2sSH3S3q2hpJitmROMLnOAmuUoc6iu13OO3HrcnNkZFUbAcwpC1I5K/hJATyX1K4d7y6KYMOuD93LBrsCf56nrjdC0yB52YcnKPkREoU0FxaWAdgOMOW8rb08aJW+yC+QLdJPbBnOjwiqzM1mwm0rpcH3LZWhmVErmVB4kNFgZ6yzsbHANd00vSWjU2PQA9Pme3O7YP+q0nFrbH16XZTlnBUWROq4oLfeUijj9kvrkhoh19bDExzLLBOyyjll3MnQ6lZ4S5OOupbHNUUgN9pvC6lPJpNd/Z1dCCjTDL6+C6iKZoG2vXujmGXsQspou1Ejn7qU9SFhFwt7L2Rco6gVOd3RRl2LKHRQ5bOM5rjgfXirb0yZBzrC37WEfROUuWxnpwWNa5oPR8v3KMI56iQs1FAn6IZhpOi5Nsl+8XPRrigKobu4/S0gEs2fL5oiX1JayWjtz4REfdrnV/KcqmIDk9DKwluF3URU437lGaLGe0wvCbWZ7JzPEoonrTbSM+9D26Q8/yamqtHG+Z05O4L9nCqOVS3KI+daSpkAdz9+ag4tHzdM7mlhkH5KbBJnZCGUbkwZre0RfuJnfEdVnPuYVXNZ3GeJzBKJ3L6ufNns1P1RRl5TmltdM6pHZljUYYtirn2OJIRW6bEoRs0FP/sNGMruLPCr8Hm3DPNj2GXcx0drb1gyQSrsO41MLovGo62Z2OB6EQZ4TrSacTZm5W0RV3tnXHHsq+kKNURw87s8bchq1Qq+lFcWHUE5oHAXWZ8DwhKW0WHhP8dEGZzpqD9FjiO2Ymn0mKI/HscjhGqB76i0A0hwadyhlsAcwWXUY+Klvpje+ACS48ORM0PzgsprnoUP6Qh1fsLE1ly7/gzFXYbm9iUAXEFiQzFe7KIZlmDX2KZHaRUGAaCx4GGQYV+2YBRBS1VW8V7OSEWoYUaerT7nZUG+zSVxit+3CzpiUqiFQl7Lmze/Z2fKQdqDiYoCyTHidtQUz2B97L1zGQh4Q5muEJdrAqn9mcwVOYstL1y3rHFNOkUhTKc/tgWK4uS3sGKTKZ5QA7est4QwyLMOZ5/scfXz69jIfLzyPi//m973h09792gvg47Ht7OXQ/HAaW++Wu68u/YMvPn15KJ4SWPM5Fq6Txn4eJf3cq+vkv3yWM0/rHy9PxrVVXvx2a15Y//pXPS5i5TVWX/bcqT5r7geynF7upxj88qL49D55f7stIi/sp9pum8bz1fpz/rc6/PV7xvox/FzC+iQFuaNXgeek/z4fh3B76IXSqbxTLfANlMS7w+XICrot8xV+Jl9/+P3ucCDdVJQAA -->
