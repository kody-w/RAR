---
name: "rar-cowork-cookbook-bulk-update-plan-physical-capacity"
description: "Applies a bulk field update across plan physical capacity records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_physical_capacity", "rar_sha256": "d1f65904af71cfa6c7f4dffe31788f463cd2405ae13f3e8aa7309d35d5edb567", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_plan_physical_capacity_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-plan-physical-capacity:68dd396b2ae4b4eb51b47cfb0c086bbc3f260782538628251aaad28806a8799f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_plan_physical_capacity`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_plan_physical_capacity_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

Plan physical capacity Bulk Field Update — Applies a bulk field update across plan physical capacity records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-physical-capacity
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_plan_physical_capacity_agent.py` and embedded as the fenced Python below (sha256 d1f65904af71cfa6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_plan_physical_capacity_agent.py` first:

```bash
python3 bulk_update_plan_physical_capacity_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_plan_physical_capacity_agent.py   # or on stdin
python3 bulk_update_plan_physical_capacity_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan physical capacity Bulk Field Update — Applies a bulk field update across plan physical capacity records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-physical-capacity
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_plan_physical_capacity',
    "version": '2.0.0',
    "display_name": 'Plan physical capacity Bulk Field Update',
    "description": 'Applies a bulk field update across plan physical capacity records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-plan-physical-capacity',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-plan-physical-capacity',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '97deb7c63cb33b8f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-physical-capacity'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/bulk-update-plan-physical-capacity', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdatePlanPhysicalCapacity(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePlanPhysicalCapacity'
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
    print(BulkUpdatePlanPhysicalCapacity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6d3PjxrbnV8Hq/TH2o0YAkalbrloQJMGARAQGeFwahEYgciIB+vm7b4OkNDPPvvc+b23VUiURofvk8zunu/X7k902YV49vT7pwM4QwU6SKAQVYmcewueXvIrhVx478Bdx86ypIqdt8qp+en7yQO1WUdFEeQanc0WRRKBGbMRpkxjxI5B4SFt4dgMQ263yukaKBHIowr6OXDtBXLuw3ajpkQq4eeXViF/lKeSLRFnRNkgS1c0zcomaEPGq/nPVwqkVOEfggjjAzysAxUnTqHmBkoDOTosE1E+vv/72/BTB66fX35/cxK7ho6cplMe8CaJCAdQHf/7BHk6HTwM4ruihJTJ4X4AKMkjhIw/4yOPupxok/jPyn/8ZX+wqqH9+/ZIhj8+Xp+FHgxI2IUCa3K4b4N30c6IEsnhBuORi9zXUtGmrbLBRDQ2ZBS/3md8o5QXyy/DupzuTlwA0P315yqEI9mDmL08/I3kF+UFrwOuXgUrx088vSX4B1U8/f6NTt84JuM1ADEr98va4f5CFA78Njfwb118g1btDHfDl6Tvlhs9d7kFPOPPp5ZRH2U93wkWVn0FmZy746ed/RtYNgRsP7vwf0f31TjgEtgd1egj+8/PNyL8ho4dCHzT/Odsh2v6OJnD4O7tn5GGof0b7Zv//RjqJMhj+7xb/S3J/NWH0C/LrP9XtX014RvwvTzOQRGcYHU4CXpHf33R1zv/6yfv28NNvf0DS/5aMnreVe6PwltpZ5IO6eXv79VN9e/zpt18/tQWMNWCnb22V/BXNv7Lrjc8PFnyM+unHuZC/mcVZfsmQj0hHfs+L/1X98YLs7CTyvj2vX5Hv82X4jJBBiXemdxN8lzM1lPU7O/789AdEiAxq07q31zDL/+M/ECkaICr3G0R3c4g+0MFNlIJBeCOMasR4JPVXfbMSxZfU+4rAp0O6Q4iw26RBhMqOEghR+eDxQYPcR77+b/cGoZ/dB4SiAza+3VHxFiJv73D49g6HX18QI4SM8yoKogzipMapKmIHIGsGlrfgqNv083ngCiWK7qij8asBceo2Af9Avv57Nm83ii9FPyjyJYOesaG7PKQBaZFXdhUlPWLf0LxvwGcIsBBNqjxJHNuNkeFPW7wM1tmHIHvYzIXYDTrgthDxk3yAeD+CoPwM3V7nyRki42DJOo6SBPEiiPqwjvS3QgOt/ToQ+/r1q2PX4ZfsDsUEci8wNQoHfAiMfP4MC4GfREHYfMmAG+bIp9//+IT8F/KvZt2IDzxUWBRuFoPhnCBrXZERmJttCofVyBAYEHhuvvv9j7srBukyWBFhRkX+UOGawT3fBcKgwd0/786BOg8igurB6Ue7IZcQ2gWJGmgtmOX185dsIJHDodUlqsG7Ee+T76Z/9/adz+CT+mFD6Kdb4RzG3mJwcOZQUF+QlY98WAqqC/3aDB4N87qBYVuAzAOZ28OZdvPNhVneIDXMnNrvn5G2hqoOlL86kPRgnBTCk918RSRehZUuT+CfwUA39nB2nt1q+yNc748hkeoTjLHpO4kXRAbQmkhhV3YRVnYNbuN8+x4RsMK9z4fEbSSDJX+o6WDw0S2nb5Gn/nU3MVR7ZHHrPu5FH/nS4tiYRP6/NSiDsJwgaHOBM+YzZC4b2vEeWUNDNSh678EGVnDePU2+dQ/vQPMOwV+yJILeqPp/3Ef6t2C6j7nDWlvBSNE47UZ/SOvqRheKgqwGH1fVzQ5fsnesf4ZGgQ6pB9iCmRsPOJB/MBzevksawvQc7r/V/Yd1hiyAcYwUrZNELuID4N1CvgmrIaEePoDxAYbkghnghj9ohUDq0PeQPgKFiGCgwnpwM50MEwP2SnfrfwyPhm4KSuG1LpQWZg54QfZDIEM/1NABsCUaxkArfLqRQlIAbQxF/LBwHdrFXZihyX0IaA++yNMhJr7zwOMlDMqhqEB+HxkHqdowgqAtL9AJMKG6u2c/5Hz4CgqbDtF/m/Sjux+6It8XpX8MWQdl/Ab7sC8f6vl3xoFQXaX1DX1gpY1rmNcpeAQQjIRb6X65V997ef+Q5fVPnf1Pf6/5v9VT80fPvSJh0xT1K4rea957yXuBWYDCGIkKUN/K3+d7zn0eku3ze7J9fk+2HyjfDfWK/D3pfiDxCOtXZPyCvWDDKzFywRC3jw80Bv95evxMDm+/ZBr45uVHKAzyQZR1+o/C8j4EVpegAsEw+F5o6qE+XWBJvOHbrVB8RMIjTyB8ZsFQFev8u/wddBr8enfbBw7DV9mA8N7QzwVgWOskg/g1eHrN2iR5fsrsFPxP1jgD1sJghdYYlkYwcWB/1ETgdvfRKw03P67qbikFscDLX4fMer5B5DPy0aI+I++Lhts6LGvhqunXoT0eWMKh8Otj7MeS0QFPcJnW9MUg+X0lNHRlj275z0IMCQUldsFQufOPDB04/okIvAgCUP2ZiHK7sJMHTNSNPVRDWIQfyV1DOT3YPT0j0Hcw6WAeQXhs4YQ/s4F8KlC2sP56g7rf7PdNrfyuyx83MzT35eTvT+9wMVzfm4F73MAJf6NlG4z6XmrfBtL2QODWWN1sfGtI36B+0VBSv3sVDP3B2z0Qn14h2oDnp8GSVQS77Ott/fx0lwcq8q2VhRQgbnyuhxYBhXkEKcHCXQxKxBDzvmMwPI682/jh4vUv+99/DQCvNOt5xIR2cBuQDgkcauyQjOs7mIuxtOO4hI/TGMPiFMHSOPwa27bt4SyL0TbLTCY+FGPwZWo/xEDHgxegAh+m/r/oyp/uFGDNwCl62BgY+zQ1wUjbZ8aub9Mu45Oe7wNizLCsT9KE6+EkRtlgTPgEYG2bIbCJR1AeBesiRTMDvUdXeBfr7b0Df/fLHQne7j0E5Ijbtsu6zJj0JgzkBwjMIVwwxsceQwCMmhA+ywISzv+Y+vDN4Lq75kPcwhYFtmPngc/vD18PsUiTcOSSrFfc/cOjk51N44yjhc6oosHROqArJzKhA+zDzrNFpaSNmcfHgSW3phPwSq8tsWZrhqP9dlfpQmBQ84yZqnXDUhLTr8yixyJ2HwVbVczW8dVimUSZsNYmiHjMbSSqXB8de6xY/FHfu+F8Nz53rUS3naY0daKxe1rvzXZDHAhyZ2F7zd7vF4uZIItExHqt1G+O+Dg/BXU11tebnVQtyp3Fs9ct2C0Oq0bB0zySq+QYiY5v1LWjm804bzSh2xehHrl6PWbyjUYr1wJjzyJFg7PDkHrSs2BJUL4Oyw4ekNVYA/wuOWzGqq4lQVIWe/y83NcSUQrnvpCqoHESs2w1KlX0cdIumXTNU3hhBXk6nie7pM93CQ4O4oIpD2uzXmTlyurMedKbztHR9+2OzJV8Zcp0ieHtNpLYeLyDbS9xpAThOj5gJZMz9AqT+/IA7A1r7XnDWxmZZ10Lje9NPVWsw1zK9PnJmlTZOjE4sd5lhSXurstguaYsK+b7KNigV5uazSyeVK+U2WQsceyNJC+ZNbrnfc0td5sFWbW7itNrB1/iV6HLZzmJWvEiqvYzx5O39rikYtLYdpSxr9Z1NrLisYaJEn3SL7vTys/KncI3qyMZHXktv+B1VvrlyZfjEkbqrNDcC2ooonNuJ7o/t1u3TWVsJFSLFpaKvdVOsvR4DXGJjPJETPBiE9amN3Lcw6Za79UFcQJjYR8dZ2Z4OC+Xu0KwlJnHjpfyqUpVdoGB82IukhvH2dbTibick2FIuXSYJBtw6S1ixNB2ZO13u8MRd5P1JaiNc0/Nz2s2WGV6yHBZgstaMqYM3W7KeOxo65KhAotWrNESpyf6gZyv6fWJlZbkVpH8DWZo+rJE2fmWmqhLAkPRqF5qBShYmhmrZbpz5vvRwoAVeqfacaqJa8pZmzqVu/WxqffCReu1k1CkBmqCBs0u6FpvLdHSvYvBT2TaOMUG7AzBLFMN3azD82qzp12bLJzLMZjGArbTYnqqrefMgjkGytwL49ANNla0yq3dQtpbmJHNomOrLtwq3AndmKWv2MUZMxyzaoESyRdNBvRKyIB03oZnfS32vJX2wKLKiDw4pQyXCY5AHOyRe3SIGu1qW0ZLMublnZ+gWxnUVetoR98whVmjXWB49evyXABFWQsSGE99zRYuQj0/96mFRqQY5QSelTM0MsbzIFF3pO1t2QlmhOnZbIkMkydiuFEOGc6EU4o40soiyzC7FCXrWo1tfmQ2BoTs4GzsG/yEHuKAa8vKiC6UvKOra4aOxclBaXTcPCUyoY8AaNFtsOzYQAP5yJ8mnc6vGWEOxh2YLplyOlon+37Bs7Z0Xo6FMtbE3Yngxm4p1XoaEftJyVrdpHOihXEWubHFCzuvLjxcNy9eESqx5qxlUxMzI7VcG9MMdqY28lZMBP6gWh1pylQSX9qZXGUdutxZJRYTVGstlWwv4HWasz7Nrk+SgB3kwErGqazOgaBgcM1/MXC7A1hVEMfReUoBFEx8YjoacYIKTmTLuZ7KxyeYSIoaYNtlF2SCVgSuxDmbfX4m5udWuIIrZ0/L2Vo4VMuTuJtyITXyI9Z3+ZSY8uvegUCVjZjlYUVtggJbXOdF76jNSZ4v+cA0G4GvCq0qpBQ1NZg29SSylF3ArUAczHVTThc5joneIp0sVa1quRWjR9HGlGq+7qaaQ55OCiOJIUfrJi+z7NXayhtv79TsekJSDJOEU70bXXD+MnXA+UIr3qSjsdRN/Wh+zap+4qjXqANnMQ5iZa13Qup7KEyV9UbRHaxrx1mtz/LtbumXMK/QkcUtQu9KLJlgNdfck6/Gkx26zHrclWL/HFzQFMrCmmc+qeaUtTtvAnJNTpVwM11Z+KnX0p05j4myw+apt9pPsxEV2XNwxDnNm5ZUQnL2ZhPDChjvpBOWXetVN+dO56shb9oF0WeBh1UXesR78YwsT3ZWp3wxC0Zno884m7N1xt5t0VlN89ODMCrWhR1p/HHV0mmRcKDLEuFUchQwG3Bt0sliPtHMSyW0FNcxqWXipGgUdCM5Onmok0rD1hTOkJIcC3KoHtqmJi8KMBqFnPHXZSZN5nv5uFHs64Hp1jvFkbDmhNPZsU41+5rtlyjPmSfN2Jet0GvdGTBkSkaTWCOpWuZNEQXr/VwR9tJB4DJHdTarcFL1zGLVlpE1UvEZPbvKZi2r9hKucTZBok9ZcmUmBn/iUv56XpIZ3uycIC7WNe8UzWkhe/kVm2uRyNplqjfMSI63QWpsEqw3xTlmcfMFzk1WOjvjjsUhSKUky3q3Erds4Ow2a96iebuic3ps2q6sXiGMdptgrk471UvOOepW807YY0G8OTmXuDrN56jajOri2B9zK+P0yTH1GWks+5ewa/EiEjrerA6k54DrAgUlVZRJYnJn6+wdzHJe4pRAjoX5rDo1RwZTNAfkHcVXl8bYtatONcrTulcWGJ+XrNZPjqWzNQyyu8i6WMe6c7E27orJF3Vnb83K3Jq2No1KMe83Rc1tQdjMJzY3Q1uqWaFpKOozdYqNKhPFeRG1PW96io8t4MsZsxLFdmRdsYVEx5PKnuNOjy19VF2eG/HCHY1khaHalMhVdSzqG/5I+9fM122ciMRiN4HNw5YhrP6y6JXMHCVNO/EnfKaj0XSxrTrfM47zYL06buYzK8ec1GrinBLARY2tfN6T0xOph/TEF6NsUbq1fp2SXSHZVdH3yT71LmQjUvy+nsOl5qlsjdB0GZzS4sVmQnMHtCAsX0w0QTTVxMwxkQ7VLT8NJNJpdbkrpZPg8PTxVOy4abH3y/lUZ9wdt6WoFKRGknGCb+pTa6Mx8WVVGTvUTEfbuKeJ8hhnmbVztirlmmouWl0EjKhoC+Gw58e2Z+ojer1Y64qprpcLzRstV5oUhxEZr4xp74rqNkJHqnYts3mZs7R2ij1c6dWpYijbojosrOZy7H3blFRMXy87vqPwXvLHa22/5GTGwkC6iEo2d5LUGEsFsGoyqWXPUibZ2J5PIqI71h6vYC4q5qOQHc+vWkPI3uXU1cVuusg2jV2DJqdQM04WHa7A9Y5YZGW5njfMOiPL1HcVuaiv7ESbBS3dr3ImOXaboxlqynQW0mHQaR3IPVNdcC4On17X+2s337aCRApMyOVEpSptTiriHsyWOQZMZ9VIlRrOKSEk/EIciUyZuVpzwoKxJ+ymu4Y223KFbXW7ktttdlGlmCOjmSyv+3hqBsFstbDGhrgZLxRvvqG0Xc7qdFaKjs1eFm1uWNbM1fpNTVzO3lI0uoCmt8JVEMUssnsYJpe5IZWUFGeFZ2G6BxQ0Y5N8zWW0Xws4ztb4yltmFrWJVbGKJlgQhHrAlvZM2K2SdtYE6dGrTQKSk6yRZmT41A/cEUfqKC5VzZqiMsfG1gmf2vNu7PYlJnZROvHxfD/iypygl2ZT53kNsWtkbEcw3Sb8Vep1pjXNw5Gly5pvNufx+pqGebiqR0qWuGna7uTrbDGrpalw8YXo1LuBwVZaNt0H+43grHvLF7KiUc/UOi1JpZSmEqdijVsQGyNg9ufSm1qrVs85V9qBqaPUXBd5dshRgmWR1iyRG0aEvhNmhrqRIkavy9FGYEb23MkLAGC3zjjZyVzsOl87SoG90cnLiSp0fH29TNQxvVJKQV3vcFewCfusoX7OnpPRhIXQ4vkNXtA5scDxhpayllX4vlqOLI8xGWU6agkxToX+Wp+2xEHa5WWxUb3Wm+QdndZYhYfHrbuMUcxyZ/u+OIgHhXE9ZzXxvMmuNQ5UZs53Emy5Bcm4hi1Trm1pwa7CPKcm0x1wiJEPZn7NTZfzMNq3/eYCu+CJtl/4ZuJmk8iYYE7RwcLEcFcHT/C6OND8eBGSdM34fRWcV0KjqKda8TZL0DVdW3e9quJLlJloPmzQYa8mZJOMGG2yMaUAesIsM3qyNbwEMIk8UY+2vQICrZ8uLmxJpstLYUwn7ojd+9giji9HniHYqF4nPYeRtMtOZ8apn/WpfHGmkhuOHIlUGsoqQq+l9le1O87str56tADpcaDexWXqbgImmQC26C4nic9SLY4szZ8SibJwqLo5cHQEiKvpbc+lehRP51Ua7KU9ozLdjDwrfVtRPGosU6cwFmZQ4iDPJdRa4kRwlEKB7bItoWqNLBuYX+QEscHOLFVNHHR8ujbChmvpq0Hzls5vGGlpMKR4ygHhomva4sUGPx8cbi9tF/jCdlMbP58tPxth1pjt8gNYpiciW7pXmbi2C2x0OR2nUz+CamIi1a5OrmOuQvG0iLxwPREdPaIilahE1vLk9bbmp4reqQR5iJJzZCZ0nWVNMlVOPGhdXZtddmlLcjh7WJ4vs2B9RrU+yU6O69tTFpvBpNmeo/2EhKUbHXMs8NX1Wlg5LTfZT/czVWYO/vowpebunD+KLhduPQOk6SzcrnxKWmhHlKB42ds1cG3LoptzIG7mDJ/RBpNUbtaO2m5xddcNo+g6uiCkLlBbdmn5Z946omzCZbxNecuR6gYsOr4sAWFTSysjHNg2cWF3Sklhjl5EbnXxZuRl7CkzZk6dp5d4dyEqPKGurbwHbcecSa4P9jPL9Dx2cmlp9WC0fUEUbQZXrHbTz2ZmyyaRIlY2XEfjLNRFvnDmQV4dFqNo4h28SONmyREufDA/0TYjgwSqrmhyTIwNmW5HwrqRz+HiLHCYQoG9sgwA2+AE6qt4epjIWEZUaQMospn64gn6tV2mgY9FueVffX4xHpGH4zkchV61lz2MZ7P64E38cTRt3YPDLtHR7iCxm/AsoIGcUOKBlbZS7IC5fQyE88zcywfYSMVnS+ulMiPmtpLa7YisSLXZoEKSC0GQTu30HHWTUbtwt5gN60dHL8XTVa1zwt2n7L7HMOxwoXR/AlaSZI5mo7CzJXeJCVMs4WfSdXUkXXIyU67ibiy3wmHmjJtiNGnkcYGR6MKOp0chdojtiLmOuawm/Vm3PSwa4xAdzpIKVzYzbuGKRug43FKmpVIqGLrGYyueZrM6j7mOLXFyvJ5hBb3BawqsLUaRyGi0KRkG9NyZYBd8xltEf576plzK9TZNaOY0MhjpCkbESjqfcbdQlWnJHwnamzMlNteb1vCFwzw3ysNVNGzfd6+BfcR6dpkFMhaTMmX1bC55a2yGiZyRsE5QoXk8K9VVy2JoUy0w49zaK2a2LlDHNynPCnEVDaSkFFaY18ccx/3yy9Pz0+1k9+l1jNFj6vlpOBp4bPD/ve3h4BoVbw9aBEPiz0//73Yu77uI78d/t+1+YHuvN+6vf0fM356fKjeCIt23lOukDR7blf9tf/bzv981Hub39+Pp4aSya97PRxo7uG1rR5nX1k3Vv9V50t42taGx23r4F5X67XG48HRTLC2a27sPReDdcJzr2nXz1uRvj2ONKBvO34AX3UcMt8HjFOD5yeuh2yK3fiNo6g1UxaDr4yRq2ModjqKe/vg/2+jqFHwnAAA= -->
