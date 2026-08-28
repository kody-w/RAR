---
name: "rar-cowork-cookbook-scheduled-brief-define-banking-policies"
description: "Schedulable morning-brief email summarizing define banking policies for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_banking_policies", "rar_sha256": "030e138eae56e06af084bbb91e88876cb0705b937868ac600da2c6a42feae303", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_banking_policies`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_banking_policies_agent.py` and in the RCI capsule.

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

Define banking policies Scheduled Email Brief — Schedulable morning-brief email summarizing define banking policies for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-banking-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_banking_policies_agent.py` and embedded as the fenced Python below (sha256 030e138eae56e06a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_banking_policies_agent.py` first:

```bash
python3 scheduled_brief_define_banking_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_banking_policies_agent.py   # or on stdin
python3 scheduled_brief_define_banking_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define banking policies Scheduled Email Brief — Schedulable morning-brief email summarizing define banking policies for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-banking-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_banking_policies',
    "version": '2.0.1',
    "display_name": 'Define banking policies Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing define banking policies for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-define-banking-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-banking-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3fdeb9e068a6bc27',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/define-banking-policies'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/scheduled-brief-define-banking-policies', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefDefineBankingPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineBankingPolicies'
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
    print(ScheduledBriefDefineBankingPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOjxrrmX+HW/dDtS3eJRSzqE44YEIs2kMQiJLkdbZZk38QiQB7/90kkVbV9fHzv8cREjLorSkDmm+/6PG8m9euL3TZhUb18edGBnSOynaZRCCrEzj1kXnRFlcBfReLAH8Qt8qaKnLYpqvrl04sHareKyiYq8nG6GwKvTW0nBUhWVHmUB5+dKgI+AjI7SpG6zTK7im7wPuIBP8oB4th5Ml6WRRq5EagRv6iQJgRIBeqyyOtolFV0Oaj+AafUUZADD2kKpGpzxIMyBwSO7wBI0uEV6gN6OytTUL98+ennTy8R/P7y5dcXN7Xr+rt+wONHpYS7BvxDgd1zfSgjtfMADi4H6JQcXpeggkpl8BbUGXlefaxB6n9C/uu/ks6ugvqHL19z5Pn5+jL+06CCox1NYdcN1Nm1S9uJ0qgZXhEu7eyhhiY2bZXXiI3U0Kd58PqY+V1SUSI/js8+PhZ5DUDz8etLAVWwR49/fflhtP7rC3QG/P46Sik//vCaFh2oPv7wXU7dOjFwm1EY1Pr12/P6KRYO/D408u+r/gilPmLrgK8vvzNu/Dz0Hu2EM19e4yLKPz4El1VxBbmdu+DjD38lFsbATdKobv4tuT89BIfA9qBNT8V/+HR38s8I+jToXeZfL1vCsP4dS+Dwt+U+IU9H/ZXsu///SXQKc6t+9/i/FPevJqA/Ij/9pW3/3YRPiP/1RQBpdIXZAYvmC/LrN30nzn/64H2/+eHn36Do/1GMXrSVe5fwLbPzyAd18+3bTx/q++0PP//0oS1hrgE7+9ZW6b+S+a/8el/nDx58jvr4x7lwfTNPcljzyHumI78W5X9Uv70iBzuNvO/36y/I7+tl/KDIaMTbog8X/K5maqjr7/z4w8tvECZyaE3r3h/DKv/P/0SUyK2KuvAbRHeLthnRpokyMCpvhFGNwP8PjIJ+fUDUYxzM/zHCo8aFj/zyv9w7en52n+g5qd8A6NsdFr89QPDbEwS/vYHgL6+IAcUXVRREuZ0iGrfbfc3tAOTNuHQJsRFUVwgqztCAzxCOPo9fkChHfvk3V/h2F/ZaDr/cUT56YJU2X444VcP5r6OtVgjyp2UuJAbQA7eF66SFC5XyI4izn0acLtIrxLnRL3USpSniRRV0QlENd9nQd19GYb/88otj1+HX/AGsJPJgjnoCB7yrg3z+DK3z0ygIm685cMMC+fDrbx+Q/438d7Puwsc1dhDnn5GBGq70rYrASmszOAwGDYYZwsg9Mr/+9vQxFAO5BYFxjPyRfsbJMFMT4L05XF9wnwmKRhwAHQ2dnJVF1YyUFTWvyNJH3vWFi46PRjwPi7qBdFWC3AO5O0CpNjTn3ZN50SA1TMfaHz4hbQ3uq/7iVPZdxQyWvN38gijzHWSPIn2ju3EQnFzkEXT/ezo87kMh1Yca4d9EvCLqmJtIaVd2GVb2cw3ffsQFssbbdCjcRnLQfc1HtgSjq+6F8nAPHAQ94z5D+nmMOWwBIIvnXv229n2MPXKccee66mteP4vArsZQuJAU4KJBG3kjNfzjmVJ1WLSpd/cfeHD+MwreMyr3HBT+ok9453JEvPcWd0pHvrYEhk+R/8+NyKg3J8uaKHOGKCCiaminhz/H9mn0+6Pjgs3AcxlYO98bhDd4eUPZr3kaweSohn88Rt6j8BzzQK62gsponHaXD1MA+nOUe8/QMeOqarTI/pq/wfknGPQ7dsEgwXJOHra8LTg+fdM0hDU7Xn+n9ntEK28sbpiFSNk60GOID4Dn2G4CtarGKntGAqYrGCuuCyM3/INVCJQOswLKR6ASEawb6N2769QCmglD4VdF9n14NDZMUAuvdaG2sD8Fr4gFC2WMQA2rE3Y94xjohQ93UUgGoI+hiu8erkO7fCgztrRPBe0xFkUG8/f3EXg+/J7ad11G9aFU27Mb6MtuRFwP9I/Ivuv5jBVUNhuL8T7pj+F+2or8nnf+8TW/6/gO8rDGH/n73TkIrK2svoPqCFE1hJkMvOfpg51fHwT7YPB3Xb78qY//+Pda/Ttlmn+M3BckbJqy/jKZPGjujeVeIUBMYI5EJai/M96j/j4/qu3zs9o+v1XbH8Q/vPUF+Xsq/kHEM7e/IPgr9oqNjzaRC8bkfX6gR+af+dPn6fj0a66B76F+5sOIsrCqneGdct6GQN4JKhCMgx8UVI/M1UGyvGMuDMbX/D0dnsUCIT0PRr6si98V8Z17YXAfsXunBvgob+Da3ti3BWDc2KSj+jV4+ZK3afrpJbcz8G9vaEYSgGkLXTJuhmAJwWaoGR/Bq/fGaLz4427uXlwQFbziy1hjn5Cxif2EvPejn5C3HcJ955W3cIv009gLj0vCofDX+9j3raIDXuDGrBnKUf3HtmdswZ6t8Z+VGEsLauyCkdiL91odV/yTEPglCED1ZyHb+xc7fQJG3dgjTUfNW5m/JeknBAYQlh+sKAiULZzw52XgOhW4tJAPvdHc7/77blbxsOW3uxuax97x15c34HjG4NknwuGwQj/XIyNOYLLCBeH1I63gs//bDvIpBiIebF2gHIzEAE6ywAYUDTDa9jF26jjODAcsyzK062AMRjkzkmFp1nZpDPNswqXtKeHDKSRGQnmPHP02sn80qgYwH5AznHA9kiYoajrDGcKeefaUsW0Pg1IxxvcgKXyfCjX0nvY+7Bud+d7Mjn55mv3ri0NP4cjFtF5yj898MjvYzIlx+vA4q2hwqmM0MXTtMr1p7ToHm0r1KhwTalluyb3DadlcpJLIjraCvmjWXS3VoUBx+W0l4OQuidZYxtSSaGonAq+2hkoyzbBzWdZbB9G807Z9skkDxZ0clRQd9pk5JOb6hrPpulyYmZnb1NRYxTFWl1J7O+bkpF/ebltebQulBoNu9XJ4zkqaJeR0sszF0gfLIxHqMB34eSttUr1dualO4IMZM7w4ENbW16/SEJf52jJaeXu+hocwb0mu2y4mBLOtBsLPnGHwa7a1nAs6m88COxLLw3F5YU8V3R7WmYW7VLO8aSvASmE244YJ5lB4YTc6q2BBQi5WwwyLt6QYFifgBEGKm42ZqpuEvt420daldLmSh3mT3+bFZpMUjMD3LRimxz1+DvtZQpvW5eKe9fJMkLspY8UmzeQRSKyJRB/oFbkGK0JXtZVZTsmE7nYKHVaL074IMKpO7G0ize142K9nobnxQmJ13h3IPDmtVi6T1EQQrDvM0swM0Gm3i8PAtEsVRiHf7I+EgdYiuFDi2twQzKk8nhe+eirlcuOSPHvyZFGtl4Rw8tSlc1jj1Mk46JR6Kfu6mtisWGKVOY31bhFPj+kl1efN8kTn1+1a2NgDKNH1bGbpcU4q21TUAso7NShK4StWu9ADfToarC2r5DS59PV1NTmfZKzpolJz4v1Zzq+JzeIWzDK7UPXLJlT4y21BEHlfS6usn8O4gsvC3NZnX4XIDhSYuPt6hfbZaqLnCSttZEVsS2MQbsdJi2aVdDhoB1otseycLSK8sFZE0mmis9yDSzlTm1LJZhGbVfDnGrF0ciHD8tLH+LZbswuJPfUzqaTlso8pK7Ln08aYBYbZrgp0kk06KZgqFWZUp/DEJQM6O11lhV5bB422M1+8LtI61DZZ2J13aNYRc9lVTr0Kk19YBaFrRnvYR6PSolaY/DCkU4rfVe41oOP+KHnKaYA8lpuXpcWuD9yZb0XRRHV6u8wdGVYjFi1VtQUCH+/dbHPKNjDQG7Hzoi1FdrEiVOxQlfn0ShpotB92RVYbwwY6KGbO2zjZyq1+4UBHET4K9BJPfMmjdj61Fvk25MLqVPn8pM+i6+FE8Et8vugt0c9JKe0vVTV1ubCvwnrZYkNW0NRCUMJcbiBIW6LG1Z0/wQSeJTXT8kFDh9rN1ouklPYCfsiyZFgNwf5i7mu0QY9zSSY15iJYhB4VLOv7obyqw3ibW8WKimaH1t4JnnfCLhXabHXJP4hpKHDCdZia5kVjr73X2F2la4M60UQA1GVX8yvltuL9PYsuL7BDLm8bbeusC9lBM5+4XBJ36V/59GwWqRvpdAASfrZON2JRNPhkOIrLmdJmMrVYzNVyLjFqUQWE5WCzMFQKaZXcDmI3w61zetts5gfXOMr0Ot+vzselNjS1WFOLPSW04DqklWIxC2bXL7Fm3qWEIXRkghpkwXuylh2tE8Zq1JTRmWFWpNghmpXk3ouYVDxfGRLXhg2DHTA6kZdBG9flkr5ZeLoE5QlVtNu0EyaEXsSVgAFjWZxZ1eMPQrTpBiL2XL6SBtcVgc+CLnLzVlubWZBOWb9XbLTVNu08v4nUIW/7NBIGbbPcp5ytFCrbmvl+WeW8eFKqocumK87MivC4oOb0GhxU4PhJv1E29SqUcekcldzZM1lrqyiMnadZh3Ga656JPPO4kHK6yZrspswu7Oa6hDuLIQ+s84YnHCO6kb7Rqkp/UGh6YlRUD44bfOZb7b5MV6cpjTKkrptn6Yhe3cqkkgWXNG28N2/sZCKJwkBMmbghFvPisr/1oIx2bGaEM3TQJvJw2k7ahO+j6VL2a3I9o8zVXOcOjBiUMMkAm3SbLmkpS4mS26Xy3MVpWYXpgvZNXsLE6lJYudBTW6NCT7tdND9nt0tUdg62T+hT0CalYBg7nd9xSmBw2X6DFsbEtFOzPHnmZriJhl7grhlMGGyIL/kKwxsjXSSsfgDeQZ0QmUcfU1I9HUJpl+jsphOFVmbs/nKgAsWOmkPCTqUKP2HeWjjyhCKGcnoy6FmaNuLZmZ5Wi7VL7HE1JHhOjmpSE05WgGrepabTmyIcnCs4eyd84gsQdXDF6VgxEp2DalZKaapxtZw4sFwdldHEWJ/JJGHdNlmy3azLmTlgRaRlBXM8NAfn2G9Lv5tDwTxQr+XJxrVeFDed4Z/NtLrYq2W4IrqIrUyLWg7cmZtS7OHUVzLfmcoAOkxeZfSgok2w77LjHJdGJYoVl6j0fApbCVkezJ3lnquJmlBgHy57bX2IxBumGsfDGV/3tg3mGOSiPW90XoB7l6lG2pSppU1HCSLhrpaKNAgWKdhZDYR9ON2tUyuM1pzjZqd8vfJ432D6UpeGwQ0sBtJFaEVsYhysTVSLUmxTlmYvJ810x3PiKj9fMN5i/WDbD9Kwx6RN3igxy5SDOWcNTNNqDay5MG9oaZtYi/KcZqEWz40qWjh8pYiVJrSbZZlusJ2tSU0yF4LlQhb8qd9stqXBYit7f57uYoxEpcDs4y0RnjFlI/DmkHGSdAMebEDKRrcPqiclmqSugtkMZSc3FZ3K3YlXrNKdTwsauxXUYXmLCav1+vLWbj08pvHDJW3ZlLCr7mRB351nrTALM0zu8JovGKKu8MuJM0yTW8xBTKC0a+OiZMvs3tscTquUW6mduMFR75jyjCfvU5bzYhygFWw6VeO2P7VBaoaCdRE1vqesMtjuGnXf65dwO6P5TXEtuCsk1JkvH4ybZzjllItk7ha26Oa6WgfOzdnvU2Y5d01S7zEn6BJKSmQVLdvKnAvhQsi69Wquem3EeWaWoJHvL/Xz1fG4htsGLRPsBqrYaTke89n2kk0pr9qfZvzVroxpEoeb856UXJynqaJc2itOF3ugD0J5pgWDTYJLMKzjvFS2GmzmVo7MFJGFrmvt2IuQ+HaDolw77biYqeGKtU0YcUL2rhpxztaNHvuymZv+bqFYxZ5Ek6JCb7R32S/NLncvZWBYrXvw8xhsbxZHYJP2lMdLq4niLslmte5J+GStLtfxBewPdZUfS34xqNmKdC/Z1VZts6eojD4G6izV9sZWuywrJ9vKZIjyQaf3oPDMHc4p8VmOCNU4iKGq5o5C1EuP259RHK8Orm3klQdxhovXdX5kJQN3vRvACVxZ6NT+fPYO13VULudAb22OZ4XrWVESDpN1tz5AV08N3sz8/qJHYM3bRa8sEwuUuHGR4vbWSVmin/DY1NqBnXTBYbE59NzF3hN9tl6oqVNJiVBsd8M5Cja+KRvHSQq23eYa2spJpdMztXWogJaI4YZZIJvPLbpdiWs5KRbrA3GjJ33hxrVsrkmFDFhvqsUURvt78cadMZ+U9/2Nos6kfVU0M814ERyvcj1v0srFJsZmYeBG1S/m9KBplhZmKF+CeC+RSzwuyzMW636hNoeBm+147DJJBIV1nI2hDUDVK/PY7t1kKnA+JhSdBIxAyLSTXE2xtSSoyRS7pTpG5Du3u2pl1xfdouM2OtNVZr0VanriYJIyN+NyGahUs1WjU7rP8EAjwkzbnhiI10S4Mrc9p/mTWLwM1Xmirs6wpXBWR/3ENsbxllrbdVE5cuvCxm4qHs9WTLWXy7xhpvvLNZ9cJXezJ9edt/G2Xt10zeAqO2whTtt1A0i0P7gkS+Fs4DPdBO6zbFqaCkd0urtN6stszhxBV1MnnyJ5/bQQ8UV9XCrYND1saRs3ZNxdwA7OduNqKJkduTP219N+1mDqoTF4PphqRz2xE0fbzZ1LRLKOzLM3AV1mkXgAzm26neUk3qAGxy2Wm0nnX0gJuiWycAmsOKxFG1l0iTbGoxPpM2lZOE3tzH3LIw4NTXCHNEZbuHXiGlwmr0x3LAZXvM1wfIb2AVocpvaBuJJ0OInL1ca5te3OpweCXqv4yl2vcRvlgHw5aNOtDassTY5lJK8qvkknmRhHyxUob7OFO7twgTt1LF0KqQAN6sBwM3afL43kRqywuvKUTXtbEyd5wzklnsF634NJuIAlz4uT0FzUbUmmi+1pJ5WrwFtaptV5My2RWcVgmDbwHRbPXZk20PmkojfdnB3mAj3RwNw5O54Xep034ITVQ2RN84scXunTDGCyVEDMX03wm3k0bjA+U1oVhtkCVS4TaTI7TWZhEG7QiAadsYG0d+6wYSKYDN1Uu9uWOEWMWpFEKMWiXndNvD4TfmyDY4ra0p65MVdu0BosztScKScL5rosmyApuvkEtgZJd6bQgcaOHMHh2/OqF6tb5kW7PIhb6+pzLuz0/Exe5BCd9mS/HtyjkBILbqIHvixDXnfXfAzmRAj3dOY2Xm1PEnG0xNz1qJ6bxr1ea/58nS1dw/PPM/9Y0VNRPIXXk4CfpJNcbxzmRKnAEnjRkmluVcNmpr517hoIVxW98PGs7fL0grd+6sQwryVqn7sGFVqsY2HMtWoyl7QNWHt5ruk3Zbqjrnxr3rT2zHVncxVEV19jwmNpKAKr4rWMGhmD491A9Ut3f76CRnW3rKQsHF3BHT/QZltnUWwkVpJQsoJQc1TkAsVn3Xm/aYNGZg6qy2wDDPOvl9lglxVpEAyIAnuxFc42X6DtbC+zcjzVKZ4Wgqhi+v0WpYleibko8LsePdxEoCarrdFZbDJc5DJv1I3AgozZT8mIA6J3beR5506sjTPRTtK5pm9M2ubA86cVt+6Oi4lDTb01SgXyrDWkq6P0kEympO0Os3lsdTJTzRR6FjM8eVzOdhdmV8/QOTrB+gVBHTGhoTJ8tsPUPtslC0tcF4G0SzWn2ZxzRq197SKUYry0W9hIoFxFXwkelcsC9iblnG6v8WrVuZLoEfZ1gk29RqLyjKQMyAm2qm4zrOHt65qdS6bLFtw2ZM4sx+Gy3uVzQyZWCulOm/nBuDYU7bZ55RgeY8N4k9OJVCTeabfeMbvco+zgQLi7OLlsomx1HazrdqdwDh+sCz2eYwS/daZn8wwpUG33WUh7W/1iCIuhdhatsSgP2IqoKVCema0yjYC6AS7jcCRDsvwmVhjqEFzxAqeJrQGTMpzwQkZdPQdT4iuhlKq8O/LKYZKHc0rtN0vn4A8lv17QKjtLiJg51j2TeUrLw51WQ8kCIIJmLcw1LwznHYYDdTpn6VIZ4kHIVX8+i2dzmVR1EBpomdW3rXOMgDDp5tpOn4NunnAc9+OPL59exiPq50Hz332tPB76/T87e3wcE769frofMgPb+3Jf68vf1uznTy+VG0G9HqetddoGz0PJfzpr/fxvvrsYhQyP97bjO7O+eTukb+xg/EOklyj32rqphm91kbb3Q99PL05bj38PUX97Hm6/3E3MyvGk/J9MGs9y7y8RvjXFt8c75pfxjxbGt0HAi+wGPC+D50n0pxdvgHGL3PobSVPfQFWORj9fiUBbiVfsFX/57f8AUNJU5PglAAA= -->
