---
name: "rar-cowork-cookbook-demo-data-manage-the-initial-synchronization-of-data"
description: "Generates and creates realistic demo records for manage the initial synchronization of data in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_the_initial_synchronization_of_data", "rar_sha256": "1349d033a2c40d5244f96acff2c53c3300d7035d255cfe3e6a9f25a495eba6c8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_the_initial_synchronization_of_data`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_the_initial_synchronization_of_data_agent.py` and in the RCI capsule.

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

Manage the initial synchronization of data Demo Data Generator — Generates and creates realistic demo records for manage the initial synchronization of data in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-the-initial-synchronization-of-data
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_the_initial_synchronization_of_data_agent.py` and embedded as the fenced Python below (sha256 1349d033a2c40d52…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_the_initial_synchronization_of_data_agent.py` first:

```bash
python3 demo_data_manage_the_initial_synchronization_of_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_the_initial_synchronization_of_data_agent.py   # or on stdin
python3 demo_data_manage_the_initial_synchronization_of_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage the initial synchronization of data Demo Data Generator — Generates and creates realistic demo records for manage the initial synchronization of data in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-the-initial-synchronization-of-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_the_initial_synchronization_of_data',
    "version": '2.0.0',
    "display_name": 'Manage the initial synchronization of data Demo Data Generator',
    "description": 'Generates and creates realistic demo records for manage the initial synchronization of data in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-manage-the-initial-synchronization-of-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-the-initial-synchronization-of-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4d3321d0db81c317',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-data/manage-the-initial-synchronization-of-data'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-manage-the-initial-synchronization-of-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataManageTheInitialSynchronizationOfData(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageTheInitialSynchronizationOfData'
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
    print(DemoDataManageTheInitialSynchronizationOfData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZejSJLtX9HEfMiqITPYF2WfPuehlU0gAQKJyjpR7CD2TYDq1X9/jqSIrOrqnpnumQ9PuQQId3Oza8s1d+LXF7tro6J++fqi+XY+29ppGkd+PbNzb7Ys+qJOwI8iccC/mVvkbR07XVvUzcvnF89v3Dou27jIwfStn/u13frNfapb+/dr8CONmzZ2Z56fFeDWLWqvmQVFPcvs3A79WRv5sziP29hOZ82Yu1Fd5PHNnqTOimDm2a0Nns/sWQPkOsUwa/3cztu7iLa2wdQ8vC9ZxmnRzhoXPK7jonkFGvqDnZWp37x8/ennzy8xuH75+uuLm9oN+OplBTRaAfG7uyJ65PMPNbQ/aqEE0yAgLbXzEEwrRwBYDu5LvwZKZOArzw9mz7sfGj8NPs/+4z+S3q7D5sev3/LZ8/PtZfqjdvnd5rawm9YHSNml7cRp3I6vMzbt7XECre3qvJlsBnjn4etj5ndJRTn76/Tsh8cir6Hf/vDtpSgnBwCNv738OAPofHupu+n6dZJS/vDja1r0fv3Dj9/lNJ1z8d12Ega0fn173j/FgoHfh8bBfdW/AqkPvzv+t5ffGTd9HnpPdoKZL6+XIs5/eAgu6+I6uc31f/jxH4l1I99NpmD5b8n96SE48m0P2PRU/MfPd5B/nkFPgz5k/uNlS+DWf8YSMPx9uc+zJ1D/SPYd/78RncY5yIt3xP+uuL83Afrr7Kd/aNt/NuHzLPgGQj2NryA6nNT/Ovv1Tduvlz998r5/+enn34Do/1KMVnS1e5fwBrI3DvymfXv76VNz//rTzz996koQa76dvXV1+vdk/j1c7+v8AcHnqB/+OBesf8yTvOhBXXiP9NmvRflv9W+vMwOUGe/7983X2e/zZfpAs8mI90UfEPwuZxqg6+9w/PHlN1AwcmBN594fgyz/93+f7WK3LpoiaGeaW3TtDDi4jTN/Ul6P4mYG/k65XfsA1yYGwD7HgfifPPysab/8H/deWb+4z8oKT8XxbSp1b4+q+AakvD2r4tvfVMW3IrgP/eV1BmoWSPQ4jHNQPFV2v/82TQbFEehR1n7j11dQYZyx9b+A2vRluphq6S//ynJvd8mv5fjLvdrGjyqmLvmpgjVd6r9OKJiRnz9tdgGd+IPvdmDRtHCBhkEMavFngE5TpNep8gM1myRO05kXA2YAtDLeZQNUv07CfvnlF8duom/5o+TiswffNDAY8KHO7MsXYGqQxmHUfst9Nypmn3797dPs/87+s1l34dMae8AFT58BDQVNkWcgB7sMDAPuBAEACszdZ7/+9gQciAFMNwMejoPYf0wGMZz43jv6Gsd+wUhq5vgAdYB4VhZ1O9FU3L7O+GD2oS9YdHo0VfqoaFrAkaWfe37ujkCqDcz5QDKfqA34ownGz7OuedDmL87Ef0DFDBQDu/1ltlvuAa8UKfhvUvM+CEwGvgTwf8TG43sgpP7UzBbvIl5n8hS1s9Ku7TKq7ecagf3wC+CT9+lAuD3L/f5bPjGqP0F1j5QHPOHUB0x8f3fpl8nnoHHIQKB5zfva4bNX8Gb6nQXrb3nzTA+79u9dAlBlnIVd7E2k8ZdnSDVR0aXeHT+g6STp6QXv6ZV7DO7++43F1ALMJnqfPduXiTY7DEGJ2f93/cxkGrvdqustq69Xs7Wsq+cH5FNfNrnm0cqBTuIhbEqv793Fe216L9Hf8jQG8VOPf3mMvDvqOeZR9roa4Kqy6l0+UAxAPsm9B/EUlHU9hb/9LX/ngs/AqnvhA6aCjAcZMQXi+4LT03dNI5DW0/33vuAJ5WQ5CNRZ2TkpADnwfc+x3QRoVU+J+PQNiGh/ArOPYjf6g1UzIB0EDpA/A0rEILUAX9yhkwtgJoA2qIvs+/B4cinQwutcoC1ofP3XmQlyaYqnBiQwaJmmMQCFT3dRs8wHGAMVPxBuIrt8KDP1yk8F7ckXRQZC5vceeD78Hv13XSb1gVR7ioxveT9Fj+cPD89+6Pn0FVA2m/L1PumP7n7aOvs9af3lW37X8YMUQBlIJ77/HTgg/ursEeRTFWtAJcr8ZwCBSLhT++uDnR/0/6HL1z9tEH745/YQd749/tFzX2dR25bNVxh+cOQ7Rb6CGgKDGIlLv7nT5ZcJry+PpPsCVP3yTLovf5N0X4rgywPa3631gO7r7J/T9w8inoH+dYa+Iq/I9EiKQa4CfJ4fAM/yy+L8hZiefstV/7vfn8ExVeV0BPz8QVHvQwBPhbUfToMflNVMTNcDcr3XaGDut/wjNp6ZAyggDyd+bYrfZfSdq4GnH478oBLwKG/B2t7UAYb+tFlKJ/Ub/+Vr3qXp55fczvx/YZM00QeIZgDOtNUCmQUarDb273cfzdZ088fd4z3nQLHwiq9T6n2eTY3x59lHj/t59r7ruO/r8g5su36a+utpSTAU/PgY+7E1dfwXsO1rx3Iy5LGVmtq6Z7v9ZyWmjAMau/7UEhQfKTyt+Cch4CIM/frPQpT7hZ0+60jT2hPBx+179jdATw+0S59nwJUgKx/M0YEJf14GrFP7VQeY1JvM/Y7fd7OKhy2/3WFoH/vRX1/e68nTB8/eEwwHifulmbgUBmELFgT3jwADz/5XutKnTFAVQQcEhKI4MfcQHLcxl0A8EiOIYE7ZbhBgLom7OI4gHo3gpIeRpBv4uE/Z8wAjbWJO+o5NuQyQ9wjdt6mJiCc9Mdt2GZdGCW9OgyE+jji466MY6tG4j5BzPGAYnwCQfUxNQEl9Gv8wdkL2o0GeQHpi8OuLQxFgJEc0PPv4LOG5YVMY7aiRA9WUf7ZOMO/ExyqFiM2YlyqKb0fWKpBGkp2NSLOcxV9ssxJ7XOIVsYwKFlYFaNRpLlBWSygmJVVoXBZzt521w/fZTUoZ8tauFsd178fprTPE2Iy7yEXRMjtk9M2SUfskzQtqRMazYcWpah4vg7EdFR+pglxM/bRe92VwzUsSOl+t82l3JLfH+AJfDMpqS1VRkbrUBNva1UYUI76N01R648/mBpdjZk2eRMughlisjqZQXf1du7SosyY3m746I7JK7XWSYa63EgqulxQWGzK4OjkhR+q12YCqUcRFJI51q6VoezJjtK1EdXEe0SiZ9yiUmAZ+XmbB+bLivZSW3H2+1tNbqd9UdVcJSiWlx0pKiKu5GpFjbEqocSxO6eFwEmxbX+2XVWBomFkt1zRqlLZxsWKbHLpabOWraov73GwLFDawIxkj3t7g/AunV2uLPrkHh5ZKQzyTqXsYPV6Tk7xzE2MbbLLa2qO3PFkLguckMRaGIt1To82NBmHlLLM9WVaGILhJri9NPj8L881YA63ijDYbdZPnRnOodjcXWTBu0IzL4egsWiUrZHvuj65QnZmyNBJMhRtke5iLqMKPTaCJqR7W2lZZZ4udVEXmOjcUKBCMC3zlljEZ+pln4o5HIRCPuqS3k9r5LpO8Na/1u7yBR+ywG/CzeXCWxnYI1MylrrURO5dAGtgGcrqkP9ZLZy2c5s3GyqQdI3N7fZ8pjQUTXaSNRs8Mw9meZ4rQj3nCbCRut27Ly8jdTnQHZUWLGqqB7csmva5WA8VIa2dr88sNUijUrslIsSxjal62ixvVyrWSxNfKyEd0T5q3rLwxJmfP4xNRCJQUQdsVw26211bgNe+yhQm5vFVWEFyuc45XLsu5QWKMvxIuXqM6w0YsfapSxiZTJQG1y6NIFm7jyY257VVsuGzLTlOPaqPuE0Vr3eE0JnRYpXSM5BzfuyTMcJ2/xoVQFKHes4vICU14kay2R/WAimq7IRLdvXThITziZiwZoVQI2qYxj6iVR8OOW198byxuLAU3Egk2AUQ8IMfEO15IiuXtJPAPHscerI3FtNqwgUpZw/kgOW0dksowVbPxo7MvaWR/M6pyXF1ZGm7hyKeUfImmGuMqyzZNg9E6baiqGRLR2ELb/mLToj1ftPthFXeSu3Kx8NKnEIvv3T2nG5xazm1nzns7eb4y2YsYj4mWnbm9Gu4IQU21ysehq9amTWLSkSLgZ2q/CeBoLJsovF63Z4Gs5rvONm9zz0ay6/ygIZJcyaJ465kQkw/93LGto1gEdopUWypnJBUdEKfCjvxK3a83ctEFi82gbxoUNBbO5bi83o46o9dtN66JCwQJiVmqqWXAyJriHVwsChXr4JOmMryuJ0ySDT4WakNCIIQs6c2uZ2ld1Pm6O1tFpe/yHUWiacQXJWX4RrXZH3akJyqMhiTGMu7nBFzZDWofHBfeXXK9XNGanvrc3E+QasWuir4ZiVt2DX1HIa521+uYPfhA/z3rjys2n3uX+Vzne7LDXOUS3RCGSBKrcEhUzm493LDE6C2kwI0u4rmADsXC3W/JjKUCY7vkr9AybNUjf8wtTJBoxsB2+iJBErJNKchf7EYR686so3CVm91odVCXPpklCzrU/OO2Cg6XKl2sZCPe1YvBJgT22PKXxDh3y9VRLszz/rJn0ZLV00r10OIiq2FoO+d1WZBqH3I8udD4Rr/JG2Vt2/xcHHqKvqTIQtugN55CeikzIhpodqYuFr7JiCjzvMAxYhrEHxnkwkJKbkYsNxgB63EtVMqBTsirnBeHVXi0ufxyuvUQ054VqiPnkbcW1zykD3N4f1F7WF1sr3B7DiSCMObzYh9tDofr7roXvEFbL1b8zhO9LLrpimUejUNVelLuHSyeW0IXurPUxebKxtTSyPfDMuwtnuwovnIpce+rS2HgLlllo0cJ2SzYuXCOMOPMiof0YB/nybCxlh277usdhoi9yOMpVsuwIef7CLaCCDpkfYvtXOOICtrOVef20KJEqyFE6BQamlk3HoTLSkVN2pdZFuLb27a6epaj9ibMLfWhlLNdp2b8DmGM5gLLeOxWbqVWl9McUwRVRvdhMwiJSx13feWIrSs6dKCefElBhp5OCDenpd7NUNKLs5OhKkaOszh7KI3wpDa0uNlWlhBGy6VLlEnn6Ia8XlfKco8eKlyQIJ1ZxBc1lSpapW1jbWOLvILsjlC4PMrZ6EiT5yKNyjhr+ObihRK73ocEJW5GUZfNW0Vq28PKrA5nZHkyLLTisbPcWZkw9nqxTgYmgwIHKTt0NEMpDvTVIiW0De7HNwNzto1SKHzHW+fMjC639Ib0O4nnIK+tzlFzSG0UWph4M/inqrTt0gLVEXNwAxUjMerUTlYjliJpc5dY9HKOxBwiXJepcCKSiPKQUlEPaX9MT7GAXmTdXlPBVlulvpHFKrYRbhHnhXki7ajUjovY8tSDZ1rHltDY4/yYSCMTeKd9yR0R0WYtYX+Fz5wJ0pNSaw1xw42Omax0WpAo0yhmqubHtDmpx/OJ9bXIgUkSapxAuLFQyZklr5AsDyG0HuqcHu/mVHASGdWSrnSIUSeL2mG7q5pQOdK2WE0mpi2eVX5ceDVdSQuEI5bRMXTk1eBi8y7V9sgWtjltjS0tLSoJLaYCDoXUK66aghW6LK7IawQitUJXeg8mkUgyRVlbqOiJRXuRGMk02YhzSkRv29obKx14Pu5OdtpnObF2+y3L47TBVAy3sZe2eymjbU0sCaFL9E0dIceBSzIBspTsuCiZeKGfN0m5JtaUtajgSvcBqXpOq3iskjU4K40kKWmn22XFcKrGHC2brK8hMiRoE3fxtjze0t2wQIoTB5OsuoqUU9aGuHm4rOOg4y9CqSjRYNGWviabvsoq4mwOW/kgEJhF6JExroL1rW7SNV7exkRke2oonZ20RlvjmhmCUc3HTM+kcWMFtKnBOhYsbZtY4lx3gKilx6KQ1RJUKrdLVJUP2FDT3WgIHbdfOcqV9AX1CGo1Z2q2J9WjtfWXHiyWNSYHvr+7yrh+WF2bWPJJjVczlN/poWYHvabYtzjybjFE4BKnFmVcF4dUyEXSXVl9hLBtHjLU7lSuY+e0u7F4rWMW2oxwSFJV3s6b3dHMC6eQGz/dV3HKL037ajMCwXbkbheyuK0y7UImV+0Yae5eQ26qkh+W/lG1g3VcgqzG9/zSIRhsd6A3zjJSGBplxyPiiP4FbRb5DefLa8sdFBeB+XQlCFSCeesgj64GLNrjkSc5dGzLXDDGi0aaSz25UUdiq3d0nBgVd9kYnNWsfD49ywV6YvBwZ1HqAkfG/eEYsEcvoDNjSOjy1s79tRZJu+Ue6izD3hCleLW9anNtQXWGokI6ibyk3DQFQfZCsYQD97aLKxrZyFijpDW70vK55pKFyCuSrJfkSSjrVPcPA0uvWLXhhqJgcn69EBGrNopNHGWjm52GlHJ0GtOMqltVF9ZhWU+ExTmge2Wo8fxw7Ett6caLfGgoZLUm5+b6BBx0SjMZGZvGlxe7oywxRC82Ved7rLc2kFUHeiABciW1a1rPuAZoEp9BoJ/MzZwNl4sqqitrj2V1QV2AV+bKedWX8bjxmgXTovXthmvwngjpg3eBqJqQXHruYGSNtXjW9coKo89Q7i8NulvFECfmRof0ruRjHOvxlLds2spTCBLL2aI56Yzt5UyPWdDisGY7w6dEkrZXjMTVeVu1olacz4v1UFmpHq0hfqXsYclZ7FV2X3NyWNU3NzAAq++7VcEmMmIMKwzl0mvoxSdUNnf7YxKYyE5xOBXvdw4Uxniq0brZJ3I+Tx3fO2ysM1yrrhPq8yWNecUe9RWNhEYGholDkEjrnUjhMNPDA4K0A42f9qM4vyKbwDpVhY44yHZTCagS1syJO2ChS0hOvl6ixGUQ4MNZ0xchY85TI5J3/Tbl9DzmqaN78I+3bnWWLsl+sLgFfpVkWWpxESIxnnUNPHPyA+JL8epkNunxdjnmblvjqaIwVnJ0RyW5rSRCIWpE0vd51W8PEkTZp5ibq7eV6w0JEg8XY4O7fLAhMRQN+BPpuBaW7FJ/2QrYZb1C88DxF+HI2hLkLVxZwRNVOkBY7bq0Dd/MK3qFfUVZu9XSqbX9eZHxfH7t5xJoBLchLdPzXGhEUGgZb7c4DwsHbJgxp7YhOB0cUsWd23Zh0H7Fua6M7/H9ljrd6IV8YDcQmTqAc0+Evulbdtx0riZg6xrVGI03C7wzrxhJaWFI7PgAxH57wBeSw+QSOux3kMYG2918RzAVx54Wl4MQ0diqGHVGam4WkdOXerfPWVdELwKhm7d1fKvJOqd7Qt5eduzNW1DFqjHPGq5Ap04feYJne5NYRGHjeBm2ig4Asd1GPcM4uZQ9ox3XMAOL11AWOWeZkxuarL28g7phLblCSyuaBm/w3RA2fshZwVWzzoyUHvKlTXocxLlRDKM95+M2yVk57kT7ExsNl5ZQhGsoBUXvrYge9ZTFVbjZq8i9hjV3nd9o12Hm1gU/IsuUbbYjQVFyXXqI0jUeCtSW9x7ToXZibguPCjYup6FrCEjl173Ts0UnLq6qvKppiF7H7Eoc4AVdwMoFdGMD40endXYKjCVc0OdTjpoUZzKH1aFuaftsrugRd2BNWlw3uBngAYLnJ7ntpTW/ol0GxtIDg6z88LSqUZqgsiue3SwGQQSZPjsdC2fzuL6ifiO1N4oOwjlM5ud5LyrzuuPxE3J16YgfVY84lDF7ZmTQYM0xB8IGgiuwItgZFUXGNLS8xtA6Z85ZaC+1I1dRkJjnEGGoe7W9nXG+sK97BBq2ToXgMXQ0M4oRKg+tVSGK8z5AFEm/sFjYK0lxsDp7q3DK/nBrRtTTnSjtMbAfC66O7mmesh/MkjUX5XaO4h0zPwi0wvXMcTM4R5yQTxmXHeQw1Lp12bdtqGfM1tgaOBXiCVkscj0pkn5gqm2PCxekoAzadK9sQ0NrYoQWpQfvLfYEw0qkh00eXxf7wKjg5JChI3WJAnonecS1N6ygmZtBI6nrxe1GkbdDeUbPrtmJe/IYGnvIzI4UTeJnqBcGSAlYtxAaV1qV9OGcqWXWqGzuUPOIY9RzcPRVlSzhzQnsKiCadXJle9O6OY4NS5Cpfgz7eIp3PVKxLPvXl88v08n18/z5f/SqejoB/F87iHycGb6/r7ofP/u29/W+1tf/mZo/f36p3XhS8n4o26Rd+Dyu/Jsj2S//ypuPSeL4eEs8vX4b2vcj/tYOp1+NeolzDxBuPb41RdrdD4o/vzhdM/1eRvP2PBB/uRuflY/T9aex4Nr2MrD89A73rS3eHifU/sv0uxPTeyXfi7/fhs/DayBgBN6N3eYNp8g3vy4nAJ7vU6bz3emFystv/w9eFTzqmyYAAA== -->
