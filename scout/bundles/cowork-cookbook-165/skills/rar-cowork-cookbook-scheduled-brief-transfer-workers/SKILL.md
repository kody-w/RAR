---
name: "rar-cowork-cookbook-scheduled-brief-transfer-workers"
description: "Schedulable morning-brief email summarizing transfer workers for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_transfer_workers", "rar_sha256": "e71faa8de020906f6ff44cb70c984c0dea5a9ad46ae301944112633fd6a932b7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_transfer_workers`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_transfer_workers_agent.py` and in the RCI capsule.

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

Transfer workers Scheduled Email Brief — Schedulable morning-brief email summarizing transfer workers for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-transfer-workers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_transfer_workers_agent.py` and embedded as the fenced Python below (sha256 e71faa8de020906f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_transfer_workers_agent.py` first:

```bash
python3 scheduled_brief_transfer_workers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_transfer_workers_agent.py   # or on stdin
python3 scheduled_brief_transfer_workers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Transfer workers Scheduled Email Brief — Schedulable morning-brief email summarizing transfer workers for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-transfer-workers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_transfer_workers',
    "version": '2.0.0',
    "display_name": 'Transfer workers Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing transfer workers for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-transfer-workers',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-transfer-workers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0f8c71f75a13d0a9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/transfer-workers'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/scheduled-brief-transfer-workers', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefTransferWorkers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefTransferWorkers'
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
    print(ScheduledBriefTransferWorkers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZObSLbvV+HV/cPuwS6xCYQnJuKBhFYQYhGL2h02S7JvYhFCffu730RSlbunZ+7MRLyIJ7uiBJw8+zm/k0n9+uJ0bVTWL19eNOAUyMrJsjgCNeIUPjIv+7JO4a8ydeEP4pVFW8du15Z18/LpxQeNV8dVG5fFuNyLgN9ljpsBJC/rIi7Cz24dgwABuRNnSNPluVPHN3gfaWunaAIoZeQP6gYJyhppI4DUoKnKoolHJmVfgPqvCJQShwXwkbZE6q5AfMhsQCB9D0CaDa9QEXB18ioDzcuXn3/59BLD7y9ffn3xMqdpfigGfH7URn+KNh+S4erMKUJIVg3QDwW8rkAN1cnhLR8q/7z62IAs+IT85S9p79Rh89OXrwXy/Hx9Gf+pULXRgrZ0mhZq6zmV48ZZ3A6vCJf1ztBA49quLhrEQRroxiJ8faz8wamskL+Nzz4+hLyGoP349aWEKjijk7++/DTa/fUFugF+fx25VB9/es3KHtQff/rBp+ncBHjtyAxq/frtef1kCwl/kMbBXerfINdHOF3w9eV3xo2fh96jnXDly2tSxsXHB+OqLi+gcAoPfPzpn7GF3vfSLG7af4vvzw/GEXB8aNNT8Z8+3Z38C4I+DXrn+c/FVjCs/4klkPxN3Cfk6ah/xvvu/79jncUFaN49/g/Z/aMF6N+Qn/+pbf/bgk9I8PVlAbL4ArMDlssX5Ndv2kGY//zB/3Hzwy+/Qdb/ko1WdrV35/Atd4o4AE377dvPH5r77Q+//Pyhq2CuASf/1tXZP+L5j/x6l/MHDz6pPv5xLZR/LNICVjvynunIr2X1f+rfXhHDyWL/x/3mC/L7ehk/KDIa8Sb04YLf1UwDdf2dH396+Q02iAJa03n3x7DK/+u/ECn26rIpgxbRvLJrxz7TxjkYldejuEHg/0d3gn59NKcHHcz/McKjxmWAfP+/3r1hfvaeDXPSvLWeb/dO+O2t73179r3vr4gO+ZZ1HMaFkyEqdzh8LZwQFO0os4LtENQX2E3coQWfYR/6PH5B4gL5/q9Yf7tzea2G7/dWHj+6kzrfjJ2pgQtfR+vMCBRPWzzY/cEVeB0UkJUe1CaIYU/9NPbkMrvAzjZ6oknjLEP8uIZml/Vw5w299WVk9v37d9dpoq/Fo5WSyAMemgkkeFcH+fwZmhVkcRi1XwvgRSXy4dffPiD/jfxvq+7MRxkH2NOfsYAabjV5j8Da6nJIBsMEAwsbxz0Wv/72dC5kA3EEgZGLgxg8FsPcTIH/5mltzX0mpjTiAuhh6N28Kut2hKm4fUU2AfKuLxQ6Pho7eFQ2LYSmChQ+KLwBcnWgOe+eLMoWaWACNsHwCekacJf63a2du4o5LHKn/Y5I8wPEizJ7g7aRCC4uixi6/z0PHvchk/pDg/BvLF6R/ZiNSOXUThXVzlNG4DziAnHibTlk7iAF6L8WIzKC0VX30ni4BxJBz3jPkH4eYw5xHkJ14Tdvsu80zohq+h3d6q9F80x7px5D4UEYgELDLvZHMPjrM6WaqOwy/+4/8MD3ZxT8Z1TuOaj//TDwDtiIcJ8c7riNfO0IDKeQ/19jxqgpt1qpworThQUi7HXVfnhwnIpGTz8GKQj4TzGwWn4MAW8t5K2Tfi2yGKZDPfz1QXn3+5Pm0Z26GiqjcuqdPww6NGPke8/JMcfqesxm52vx1rI/wTDf+xMMCyzg9GHLm8Dx6ZumEazS8foHfN9jWPtjOcO8Q6rOzWBOBAD4ruOlUKt6rKtnCGCCgrHG+ij2oj9YhUDuMA8gfwQqEcNKgd69u25fQjNhSIK6zH+Qx+NQBLXwOw9qC8dO8IqYsDTGCDSwHuFkM9JAL3y4s0JyAH0MVXz3cBM51UOZcVJ9KuiMsShzmLG/j8Dz4Y9kvusyqg+5Or7TQl/2Y3P1wfUR2Xc9n7GCyuZj+d0X/THcT1uR32PLX78Wdx3f+zms6kfi/nAOAqspb+5tdGxKDWwsOXjP0wcCvz5A9IHS77p8+dN4/vE/m+DvsHj8Y+S+IFHbVs2XyeQBZW9I9gpbwgTmSFyB5geqPQrv81uZfX6W2R/4Ptz0BfnPdPsDi2dSf0HwV+wVGx+JsQfGrH1+oCvmn3n7MzU+/Vqo4EeMn4kwNlRYzu7wji5vJBBiwhqEI/EDbZoRpHqIi/f2CqPwtXjPg2eVwO5dhCM0NuXvqvcOszCqj6C9owB8VLRQtj8OZSEY9yvZqH4DXr4UXZZ9eimcHPwb+5Sx08NMHS/g7gZWDZxx2hjcr97nnfHij/uyez3BRuCXX8ay+oSMs+kn5H3M/IS8Df73rVTRwZ3Pz+OIO4qEpPDXO+37ps8FL3Cn1Q7VqPhjNzNOVs+J989KjNUENfbAiN7le3mOEv/EBH4JQ1D/mYl8/+Jkzx7RtM6IxXH7VtlvefkJgaGDFQeLCPbGDi74sxgopwbnDoKeP5r7w38/zCoftvx2d0P72BL++vLWK54xeI5/kBwW5edmhL0JTFMoEF4/Ego++48Hw+d62N3gYAIZAAYPHGfmA4zAWIwO6CCgKM9lMI+dUR7mA2fqsI5P0Q4gMZylKBwnaJIMfNphScJlIL9HWn4bsT0edSIcx5t5DE75LOPQHlznkh7ACdxnSIBNWTKYzQAF3fO+NIWt8Wnow7DRi+8z6uiQp72/vrg0BSnXVLPhHp/5hDUcxmbcfeSyDB2E52Q2w9hqwHKa7GbTHPMyLA1JpZKEtMOO172h7socJ05LIar0pLM3HKpu0V5nxGKWytrJBJpfL+39NkzX1Wp2EftgOp2Ksn2OMe2y1xjpmOeEcYngTLoNTman7jfWlmjAarA3KLYULgQ9QycRvwLLcttm82nWnc65n+l27rgnV4zNAypMz5QfZ9j5BmLCXp5PWnUSUnWFi6WK9hYfT3f1MqpPUQcfLIjNNJpkzoYmNlaCnQp9OvWspJ8C0rou3ZaadPXQTWM2PEdS5h5LZ+a44Exg9dpHBSKzr3EHhnIHKD1wWjqTasUKEu58cs5TcsHehMpWQBCW+X5Z+M4qGoB1qq6WtF04uG16QeMoJL+KPSLZzIjLVhVtUG4ptN/rcWQMytmw3PYWyXi5l+PpND/tL7jvXFQhE2/yoJ5P2K2IT8lkPtOU7tQ4RwV455uDhsLcTWH6Zbt8ddm2eXeqg0DuB/7EYCER9rthn6tGLg/T/lKE8c4wc4Ia9HO5ZBvUXazPXaTaV5R09w6zY2wnLfGtm1OHKNlRUcuvBjfB60WemJdi7vZn3NynE9KIWhC75NExldRezNhb1avVwhJm09sxcM01LkX+pdB8d+Jeb+Vcic+F2hEWuByGpSmTAc/ILj/I9cog1IyekHPVzArBsMWLvkwd+apaUUcY0UXlz4aaeJRQS66tTbqrYeryrTqydJ1p+FCgTSVbYRU0c9dRmi1qyNvrfNF6Q2TkmGxbUoCSjNMwpm8QJ9QcTMI2T9bVL5xkv1ClaJdv060DIs3lS83pSv0cT0zTTOSgavNASdFQDpqg6C+XEqg1ccx3woJdT5MoONRlh+aBpMf0cosXFzDLcuu2xiLslp9OhmueIq3ZWrsBOmyRXxfJ9toeJQ8mkZtejHUd+CyMS22daSH3uPaiaRk15W6FMwkpZnvc65K9y9umOHYbc7ZaC0ce1oASHU6ycDAVcnOrBHXh+rNVIm8aAkJPbeRgLWCets/IPpEWNYpdsmwV3XRZk6+3NJ5LV/GSiIJFSfhGSqhModyi01Wjt/wtIS8Wiuj74umqXoA+Wfb92jcGzDzi6JEZlqxuBCtnQFehxK2KCM2ukbFfa/TM1vbYzOY8Ct+Gy81pcvYLVIwr51JiHqewZtq0aVZmZqtTqsCmmpd2sMeFcwa9CJsWjch+vZ8l0nY7YafBXqBX59lsU2W5yGog9dc0jVdLa+J70o6otu58HU2qLs92By7V23XiKxzQ48NmX1gLVa45jRObQUHNcMqurOUavWV8d+ocbTPZawdi0xGypDc8PpumWR+v0TJIuWizWOKVI/oBbt3OB3G+jXT92ieOEuk350xq9IAzjbQl52Wb4qp0cPXcdYb5pqClAbf2zlW/Eq5vLEB12ojRwrnNgsFwGy1dkYebME0ZBSUybBL1VhpLStB7uV+UIcTo0FmwqiegsZY7Swdn1nQPrOCGHvTZsbXRHUOvVxN1eiaEdEm5/LUN002w0ryTFGcH2dmu50erji0r8fbNZufZCqplUHC228TyjDwQ9KJb6WZPn4YzKQWHhnYutnfeKhlBtsX5PBASpromL89z4ZCdN6S2XQXhfBVhy+Z6WdthKOw1ab6dK33stAlN7v3mmqTcSRFw52h021SxPX15ZLjEL3zZVXqV16ojhISZKGSyG9XrBehkMFvaCna2TIezhvawrve3C/DktBEzjylrUb4U02lwWLNTRdvyxUlTZfnSsViarXRjcsbOuHzi++0uKTFR6g8TRuXEaQcoxud7sEvXF/FCnAJyyaIzPZ9M8AxNJpM9T1XBUjQoBwdobeIbbtuGKlbFzkG2l5itqFKdHWGP5czYXaPbqjeWpjLjMmxVy0UpB3au67isH6OFfomdTgm2sBr9kOGDkzy3Gr+LDsoWP1dEOVQSP091osHZ0xylBSKmimW6yK4GBxE583lxnorc9KqpexyvWoe0GkrCrGV0OV7ClAusdYSGPZO7Rjercn0JdsRFa4FIEEV7s+gDrnB8uromotXESXlcBMniMFVzRmjXZi8BWifqra1jh+vNIIXBmnpm4LeAtIdp5R3MW8FzYX5Wy6tutLmjTgrAUIU7ZyIu0vyDdQ3aVJzzGbMSF84ptSNBTZjVDfaQ44ayZ81M8epzk0XTLDocSUmRL/ySzaLzEZvdrls8me1mbml5wjLac/o5wh1FuoXDzuS5aHVbkkY/Q01lpyiXfBfbabbjwnAwmbk5cPRCd3dFLfP73CHYg6CxSrw6n7iVg7rbzjsXtsjPvZUauuU8dtANI/nThdtqVTmnpt5VOYH0TPbX9ZlJko2xPlR9Vuz2TCnN+y16QpfpauJhWL5xhZPZBlHWMqYi4vp+e2yd/sTsJ2c6U1KjkJhViYX+irHMdIEvxNv6sE08Q6gthhdY+SwVm4lACLDSizjdWRNNTa5GyB63dctHZlrshZZYADvbyEJVpkLVl9qRlnbbUy/Ma6aSrB4jqG7iCJXkYZxKB5NF6Luz9cRmbTpJlQ6Y4WpDHXYdo16xdEan1Tk/h0VFzNo5ObldmanRTuZDOiUKYiOz4g2czxK1T2qgAbZNXN8GuYUPdaC73o2eWQLtaKyrTGir4Ct/Sy3zfXBjSpoT1GjBK6G7lwGR6Ke5zBfmerhaq5MTTRozmcqmGJP7szs7eRyBzdXSQIu1aDRJt855f6PhcbKMjr6B2vOkCMgtFlfWRZujmZzcpiAuBTgCn7PcQauE4jkpuvD+7OZp0eaa912uEeEprKdHtFF2lhuf5+uDJOJANXs+G+ylFK1ATvByrmiTdnsRDLlrh5ytcGyZUzxq7be0h3o2uGJHqFSimexmbx33kHB2Ep2VfbZsuZYy6mb3sZKLsaF64kYxeduQjaVyw+L1hu781E+0Y7VQ8NWmpqLbBoMj2WpNLfmEjnqMbncBNjUdg5PXJ8yH8+Rmorg7KqV3GUXFE9600Cwl6eOtt2aZEu7nTLknFsV1SuhnItxnjUZIzHWvWdqZmULA1zFamcTnIafwHPP9XdUrzdUugqGitxXJhkR6DSBaJWFtNrGjUVpwzF3poHdzvk/jvcRU3Y6Hg/I+22lElldSK1gy4XE+1xkMmRXWzFkblz0aYkqxaVYMutWvPntTSQJfulrl6ae92WbJMeODrdlyAspZVcFrc9fsOJxUpEiYd9GuaiYiHORnJ+50UjfVLNEKuQ48QrHAJsfP683FybeEwdNL7ZycTOywjSSsEx3ywm6Fxg4EcTVdFqa7X8zxKV0fuoMVRmsJnaiNxx5AaM2tSBNggi74m2sIw5Ibjods5xqHINx513y9bRnc7VfSZBPdaP8S7lzOMYJ1p161PT0liHauKlkebQLrsosSthVBwyhi4GK6y67tVa6oph9mYEsFurKcGEZcLn1iMnfLle/pHHu2sN0thdBlW66lD8aurY/KSWlCZsHZ0uKICUBM53bkGfW5F5eLfU4dZWuHrdLDjGpwb23wHMrxzmq3dLHG8/3W5ZbSoJT10U6mfsiGG9/OjXJ1VCMAlj2rOPLgHM2C297oMO0m9cm6FHY3nfabidZuKK+wLAvf6vKujBeCESy35oT1Tpo3mwckVXL6ik2ZxtmsuyVQUUllgrOPU+yOcgJ3b/WevDTjdtrAPVrHu7XFVj6jzLoovpB1o6zmZJv05NFc9aaGgat/cvXEEMQqyPgTizl6f836/XqX+Yk33V/xTYJjN9yc7q3aU+Iy2eCnPgbCFltOUAJb4BHnRi21gfNC0BNnbmaQV2E+n238KY+WHuFt5a1+NOzjQnNRUotuJ/rgbJIAY82cuQxZKS6m5MkkC5c3tQWtgWJm0ErHJu6CdfXUDIrLhBkkcsq11Hknpolfk+imwKc7QLPMrSBYFfgpOGd742A75ibI6bk+eOyKUcVd4/KS3hmuGKQbKz0eF8WFXi17kueqK0GV+jpfU/PUCVIyDunEywPcKyoy2U39+aXgB2qFLRza38lJ70lsvSzFopEjJruC2XQ6LAt2K+n+fIiH5EJLGxKPumBx5OjGaGnOHQJMXwQnXzVXqgrIldiLgehemh3qdrqPp45yrSV2LtDo6mD614ZaLUTVTihsieGwUOf4ITljaxm7DJg7cydkkkTrWxzTnU5wp3i+ZQg5JzFQKH4+RW/YIFhBC2Ri09ihaBqJfTNxlhGHmZyAOudVnwLOAXj+TZoEMmXpDL+PhCUqZu7Bnpnwimjt3u5mq229PZSFo1iNGrP2JBexhQExU5gaFT1L/HQPR9eLgVGzmtpjtnjNhNhDl/ObxbvaFWWwBdw9EtOTc7uKnez1saf2tSkVFe9KsgguEeuhE1BNJysP9OiRxzeVZk4nNmNnoWeu1WW+S/gNJqrkNgtn2Eq4LnizhmNvpBRHdxYJk8lQ0gMaon1NXXwUb26kb7nSspPySVFv/djNHcw8aIumIEiv4Vl/4/ZE56mTylpTCQ+/NETnZ+4epfQltvPSG1jMAxpdE3LBEdJ+HSTRdeX0Hp/7PjqJGTg9Xg6G7eMeN3VEHu4pu6NJWey6LoLTkcFInQSH1mwXi2PHmIO31vAlmrTUVugXPXe0fNES0IT1136scovMngxJ2hnbHapj/kED6iLFcGNP52A5bfeXiL+sOExmgA7WIT+7ECRaHwjCYnHsRNZhd2H8NDy0t1tPG4sbbIAb4hBc94lYB8Tl4sfMclU5e1JPTjh669ZdyzMOSwQ+w8IZmNMkMFyalVvva9qDoL4LNvJsc1Q5Geximc5v6wlud8nRMjerOe57uM8s4RTY3GaSHuwvW/LqTw5JElK7zSEmPcAPDLno67a4FpdlLrnOulU1uBAG7hxOp8qGXcg3muPPcsKvV1HbaCdwvTmpkyluL08XB5MoGAIjvYOS0EasLMN5OelQdl2c+cOpRw9a2Yl2fhEmwAM2Z4qc0bfysm04j6SGcgiDs3ss9qFEedkxXR0yhwix/KAVMIVvGZ0lDXVLRPpcX1xmM58EqLD1loW385bsgijR69yx6u6w3Hh9y9ROmPlwT3hieynU17O6TP1VmmQtUdLpzIkg6F22/JRlbxI/TXSxB4AjNb3EjEIcwmtaKHul4WWrR+cXNFaatNeYm84s7E7vCLbUO1m5dRixwPG4sBmUo9aFWF5PO4XjXj69jKfQz7Pkf/vt8Hi69//skPFxHvj2Tul+jAwc/8td1pd/X6VfPr3UXgwVehykNlkXPo8d/+4Y9fO/ehMxrh4eL1zHV1/X9u3IvXXC8a+FXuLC75q2Hr41ZdbdD3I/vbhdM/7pQvPteWD9cjcqr8bT778zAt6J4hp8a8tvNWjht5fxrwvGVzrAh1vat8vwebb86cUfYIBir/lG0tNvoK5GW5+vN8Yj2fH9xstv/wNF7hwFlCUAAA== -->
