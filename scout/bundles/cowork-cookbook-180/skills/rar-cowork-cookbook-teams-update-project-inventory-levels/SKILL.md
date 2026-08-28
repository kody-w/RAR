---
name: "rar-cowork-cookbook-teams-update-project-inventory-levels"
description: "Drafts a Teams channel post on project inventory levels status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_project_inventory_levels", "rar_sha256": "9afd5bd374b1a07464494d7d58fcc65c35d23c4cace7b1936e5d0b945eeb411f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_project_inventory_levels`. The original RAPP
agent is preserved byte-for-byte in `teams_update_project_inventory_levels_agent.py` and in the RCI capsule.

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

Project inventory levels Teams Channel Update — Drafts a Teams channel post on project inventory levels status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-project-inventory-levels
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_project_inventory_levels_agent.py` and embedded as the fenced Python below (sha256 9afd5bd374b1a074…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_project_inventory_levels_agent.py` first:

```bash
python3 teams_update_project_inventory_levels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_project_inventory_levels_agent.py   # or on stdin
python3 teams_update_project_inventory_levels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Project inventory levels Teams Channel Update — Drafts a Teams channel post on project inventory levels status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-project-inventory-levels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_project_inventory_levels',
    "version": '2.0.1',
    "display_name": 'Project inventory levels Teams Channel Update',
    "description": 'Drafts a Teams channel post on project inventory levels status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-project-inventory-levels',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-project-inventory-levels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '68032c2774d33aab',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/project-inventory-levels'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/teams-update-project-inventory-levels', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateProjectInventoryLevels(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateProjectInventoryLevels'
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
    print(TeamsUpdateProjectInventoryLevels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716+beiWLbmv0Lf90NmPiICkEmiVq3ViCgKijIIkpErkuEwKJMMMmTn/94HNW5kvqp6XdmrVxvDFTns4dt7f3uf4/3tzW2buKjePr/pwM2RtZumSQwqxM0DRCi6orrCH8XVg/8Qv8ibKvHapqjqtw9vAaj9KimbpMjh48vKDZsacREDuFmN+LGb5yBFyqJukCJHyqq4AL9BkvwOcihgQFJwB2mN1I3btDXSJU0MlcL7Dahcv0nuAOEDt3y8EdwqQMKiQm5t4l8RaIQbgU/QBNC7WZmC+u3zz798eEvg+7fPv735qVvDj94elphl4Dbg8FS/+aZdeSiHElI3j+DScoAo5PC6BBVUlMGPAhAir6sfa5CGH5D//M9r51ZR/dPnLznyen15m/5obY40MUCawq0bECC+W7pekibN8Anh084daqQCTVvlE0A1tD+PPj2f/C6pKJG/T/d+fCr5FIHmxy9vBTTBnSD+8vYTAhH48la10/tPk5Tyx58+pUUHqh9/+i6nbr0H0lAYtPrT19f1Syxc+H1pEj60/h1KfQbTA1/e/uDc9HraPfkJn3z7dCmS/MenYBhSiKab++DHn/6VWD8G/jVN6ubfkvvzU3AM3AD69DL8pw8PkH9B0JdD7zL/tdoShvWveAKXf1P3AXkB9a9kP/D/L6LTJAf1O+L/VNw/ewD9O/Lzv/Ttv3vgAxJ+eVuCFBZH5Xop+Iz89lU/iMLPPwTfP/zhl9+h6P+jGL1oK/8h4Wvm5kkI6ubr159/qB8f//DLzz+0Jcw1WEpf2yr9ZzL/Ga4PPX9C8LXqxz8/C/Wb+TUvuhx5z3Tkt6L8H9Xvn5CTmybB98/rz8gf62V6ocjkxDelTwj+UDM1tPUPOP709jskiRx60/qP27DK/+M/kF3iV0VdhA2i+0XbIDDATZKByXgjTmoE/p1qu4KUUdUJBPa17kVpk8VFiPz6P/0HXX70X3SJNRP9fG0f/PP1tfjrO/99ffLfr58QAwovqiRKcjdFNP5w+JJDesubSXFZgRpUd0gp3tCAj5CMPk5vIE0iv/5b8r8+RH0qh18flJ48eUoTNhNH1W0KPk1+WjHIX175kIRBD/wWakkLH5oUJpBhP0D/6yKFZNxMmNTXJE2RIKmgzonMJ9kQt8+TsF9//dVz6/hL/iRVEnm2iRqDC97NQT5+hL6FaRLFzZcc+HGB/PDb7z8g/wv57556CJ90HCDDv6ICLdzq6h6BVdZmcBkMGAwxpJBHVH77/YUwFJPDvgZjmIQJeD4Ms/QKgm9w6xL/cUYziAcgzBDirCyqBjI1kjSfkE2IvNsLlU63Ji6Pp/YWgBLkAcj9AUp1oTvvSOZFg9QwFetw+IC0NXho/dWr3IeJGSx3t/kV2QkH2DmKFP43mflYBB8u8gTC/54Mz8+hkOqHGll8E/EJ2U95iZRu5ZZx5b50hO4zLrBjfHscCneRHHRf8qlPggmqR5E84YGLIDL+K6Qfp5jDfp9BRgjqb7ofa9ypvxmPPld9yetXAbjVFAofNgSoNGqTYGoLf3ulVB0XbRo88IOWTpJeUQheUXnk4OFfTQjPgUJ4DRTPfo58aWc4QSH//6eOyVR+vdbENW+IS0TcG9r5CeE0Hk1QPycq2PsfDz/K5fs88I1NvpHqlzxNYD5Uw9+eKx/Av9Y8iaqtIE4arz3kw6hDCCe5j6SckqyqpnR2v+Tf2PsDhONBVRAAWMEww6fE+qZwuvvN0hiW6XT9vZM/ggjdhmGHiYeUrZfCpAgBCDx3wiCupsJ6gQ8zFExF1sWJH//JKwRKh2BD+VMUEhghyPAP6PYFdBPWVFgV2fflyTQfQSuC1ofWwvkTfEIsWBtTftSwIOGQM62BKPzwEIVkAGIMTXxHuI7d8mnMNLK+DHSnWBTZlC9/iMDr5vdsftgymQ+lujC7IJbdRLEB6J+RfbfzFStobDbV3+OhP4f75Svyxzbzty/5w8Z3VodlnU4d+g/gIDABYQJPPDqxUg2ZJQOvBIKZ8GjGn5799Nmw3235/A9z+o9/bZR/dEjzz5H7jMRNU9afMezZ1b41tU+QEzCYI0kJ6meD+/hsQB9fpfbxvdQ+PkvtT8KfWH1G/pqBfxLxyuzPCPEJ/4RPt5TEB1Pqvl4QD+Hj4vyRmu5+yTXwPdCvbJhoNR1gR33vMd+WwEYTVSCaFj97Tj21qg52xwfJwlB8yd+T4VUqE+dEU4Osiz+U8KPZwtA+I/feC+CtvIG6g2lIe+5h0sn8Grx9zts0/fCWuxn4N/cuE+fDlIWATLseGAA49zQJeFy9z0DTxZ93ao/CgowQFJ+n+vqATPPqB+R99PyAfNsMPLZYeQt3Qz9PY++kEi6FP97Xvm8DPfAGd2DNUE7GP3c407T1moL/0YiprKDFPpj6ePFep5PGfxAC30QRqP5RiPp446YvsoCkPnXlpPlW4jW0M4AzzgcETNhN3RCSZAsf+Ec1UE8FINNDtp3c/Y7fd7eKpy+/P2BontvE396+kcYrBq+REC6H1fmxnhogBlMVKoTXz6SC9/7vhsWXEMh1cE6BUjg3DGgvIFnKI1ycpRiK4qiADeh56PsM7ZN0MCN9ynd9wHoERzKADnCPo2gAPIogQijvmZ9fp1afTIYBPAQkR8z8gGRmNE1xBDtzucClWNcN8PmcxdkwgO3g+6NXSJQvb5/eTVC+z60TKi+nf3vzGAqulKh6wz9fAsadXM/CPC1W0CpF+55kjqRZ4tndcCNygxKS5dsbPls6I57Um9NMsOgrzPqWH+xG3o3LgyZxi3CWct1Yz2vb9GSDk3hpL0ZeRg9B7sxsh6Yd+ZgIuHvXMVnW9fYy11vrJBt+YhL+rUbl/TWrKyP1h5Ews3vC6Zae9yiDYokOUnulWbqAamCTCzPxdrYXGil7+qlaF1WVW4R4USQUv512txxPtU1+00cqJvZOmW1j/b6eEXWW3sQCln3hX0wGHIwaA6Q30O2wVaU7Td9HyVR6R3bEM7OLqg1obg4sfc+OyyaQOz0+D0R85brZ/BSrd+GUmLWUmYySWTCQnbgaS+NyjETmpt902pLn9H48JRxRXUvrxjTHg4xGrTAQ3X0luXRexZ5yWsgMZd7skyr12fXa1tV1YCWPaNhVv20ZJaR0hdJadyveTvJyQ9VzUhdp0vIZ81inYnnR/SA8mgfZqLl9VWhOorYnI3U8upeOSyFY7sk03IxKphahYsc3XyFQWbNyKzcWqpVUdc6dt+xqKM3CTmLaqrVVnp/q423H+dcIVQ+WszrLWDSTPEtt9MZRxWYH/CzTQxmzTnuGU3rVo8/yWB9GYpEuTlc10ARvixvWPL+Ft/zcXF16flgWvd9hZqvs7zGnh6Ib+227x1GpWjXD4kRlrho6xnZ9XrYHYX306thS+5ilS82sauKM2v2CNml/u3WKY4XlElEKjro8zYnV/qJkh/m2o4HMGPfdbIgpA7PUhR5HW5+J00YGXRKQM0xyE8c6nezzLFhpXVQb94HejYdis3ZFxTnPb7cbXY62SXKmSXjn5sYUt1vFtbSrn9GxGtBFia122IpGhcU8WoYhc9W09F5g851dcts6LAksokHsB0AiBHe5Zfta8yhtr6eEyd0iLQHaYLlFKpi+v9Vqaz0cRzvbG0K9LozjKhSha/rMzBNxdjfbK7VaifaOPzIjjqfKik1XnqPy+ibdmGfeXTQr86ReTF1Xe3+2WcbS2dnYVyE7J/L6pBn7zN/QHZUpF7I9ddV9QWDseTN6rnLZxDKdiEd0k4re1Y9XjjoQYIXqRRF2dBvu54ThbUrVu+3ztMAE8uTKfoTha4zkRC/qe9X0Z+FqtPagrlpPO4eGuF41+gYb3GF7u5e2qm7XO0Aswt7V57Q6F+ZcR2FVcZNDtF1H5Gx91RMtsZ3rRsnO+1DWCb2y7CJAbV1MsKNXLtaSlhR4EGKXk+4YawDYWh8ELJaN0vFwouK4xhXrcpWenDmIjbat2b5ciMUq7E9y3JbYplDV9fxyGi68XTJRzC1Hat3I3W1/tsoZNUTJnBHC5BTU2fG+Htlhpd1SEdIQWixSTbIcvfOqFkPDkh731sq6SzLRCKtzU92AdbK7Jo7V6yneboOjYttZsHOJMd3KhWeYyVDhnK+mC3QfHLzr3N3V3sihZuOUOEv383J1yG/yzF23mLw/m72+nXPX3HKugOesfRkShyiv04wrJTNcKAt27/UYRUEUPYLlDsIS96J7uhBrCwXpolySdwGm3E0ie11brXH3KJ8vFy0u+VvtHIHPzBrmuAL2lpErljYt3qjau1huO06hGUxwrvnem7kolpv0Ps3iqlu2Nz5SnFhpTbfHFg0cCHK0Eh1rGRGdLpYKvb4ZF8VrZhYeBsNwLbR1JDP4jU84AxaAc77u8Z5MgbpN+BQilMvAqRPxFEp7S5OWfoLykPtv580MLM54fTjjILdokUsuO0PiVs6Fpbkwr2bzu+ncjnqwS51xgcVLK85letkaGSzv+DJztLOPuq2xtIeBZ5WzPVvPzgU/0vNsfpAuxE7KWYLQwhLmkd5faA32nGhxogHqsknKL2TRgXuHtbQ36dTRLKFcdW0AOYyH47xSLa6xR+870R0gbYRRJSVjldSye9UtjjueZHG/Pye4bFCSYOLbeIGpIrpalcbahsUvumDLWU5ddYcW3Zoa5sidaVMFX6hJq/HE7ko2R3O47WgdNTbZbcfq5EEVXddMyhvYLeioZyPjZpxXKbG0y30Je4xOFKnPLnIq0kThFGuHpvSpQW2rvSpK/ihVu9G0dpQLzgd7ebNSSd8LXU+2Vcpek2Y+cG1fbug97wviuTpaqy1enStvTZM5ll4Coz5y8kV3sKXD5hRFN5s+mF8SdoMHe2tbbQzncMkxAecV7jRXDy4bt6IcXQVBosq8LXTvyhyzDTu7M8Sp1UU8OwpGVp3PBH2BbzNne7oSfofrITPfOoaSZkPrZsz5FulbdmlTxnzddga28h1FUa+0bcfspmNW2Wq8LhSbCIhbgVPu7XK82knAy62QaNgF28f03dg4nr7Sxv2Fd2eb4SgM9BrfX7ZOnvWeIg6i7FA7bocJwwJzRo1dlHrK9PN+xnL9yahi3dFqJhKxPeYy1+7K50d2XcyiYOdUa1vkziiqrWTJjvVrNT/inHoT8w3sY6ZppnYm4ONCX4+Mv26lxkrjeGttd4qmBBFRbK1bfE74UrIK9SqdMlNZ8NH1vJcFbC3mOslttsJx60sV42BBOutnakutxr2kbM0+NSVcAaN7W4qBTsMRZnUN1pHRSwzlzHMP6zle36tW6cvM/bwbcibRpG299G8GmXS+xy5xBm8N7+bZWj+uhn1qggZrl7ta6MbtsBCMxrFBv+GT5nyUzaXuMLDcGvNKST2uXre1OBxXOJWkDKZe2tS3olofBXRRqe7GoW/pOYt47jimgjU33Uy43Boj9gVW74F5EjiWoUdgselxbZL3VK8JryoPR8OOdrJx11O69JdA1/aChjNXfq0cZoLe+OpKvKrgOMKxrKb4I1EL9PEiGatjIbSoHhLLi126ZZOF1dZpj6Y5dtbpTgrq2RaH+al06TqMyD7fV2adKOVpTHf9ginsuyxIyy1/tLMmYsAxwi/KLRqyy7rcqRqB0xsPTuWllgm1Y8F+V4xwNlOuB3Mr2Z5c3Y2830RrrZLjuqsNiziBWndhQeW7XAyuLsPN2hYds7DkZxxOhcpSjVzUi7l4uw7GNd5xh6u3GiRzbTHiwbfWXWD2akKNkqu2BH4LYL9WsauBnxISEwv5ssfSzuiUBO6Mdcqo9TylxGPhZqU4OGOwMcxDI9IzM9bG84DHg0gqqM8HfENwRJ7bouul1RJT8GO+qU0WlbbrFpQuyzqCHUOtg3yHIDKFvBLI25XshIBnh+PSKbZrXDocV5xL77rQNnZXHF/SxHHriPFIHG4+Ve8VjAeu2Vxszl1TiRHqju03SiYwcNjbWWiL7miZJpdUvO3KK6MBos80OWDZ2OvNKFuCdBZ4GQzQJsVP+9Qur10aVxdNj4vbYpYGu4sfWhtpI1Tp2NvHDlB9vsK3cLJgec8/sCsjxsneaEaAzwrZX++Tw0J2Uji13lXOUO5HbrzDHFG7rbkRlmwtGJzKbcHyvhrVsRRrVrNBjtWMoKUXJj0r2pV3bc82hnap23LG8clRXfPjeXFZnFYqr15OxWh7vJIuD1dqh+U6nqUkg99NQTqtlTm/3Knz24ENI3ZxIZre49OzfNxk3m4czyrMmlhz4vKkOjRVCXhfUNv+2LWjsb8NLo3No9mh7cZhj4eHNVNRinFYRQy7RKuzsxDXl0GyBz2ol7bt58Y6X3O46EE7gGehBnux0/C6A3cuFOYgae18NhJ+5iVsbKEzg+UAn1U25gSsxPkX2m/tE7dPL2cwBn7fJ6W51WYM5l5CE21SlTotzz6dqb28UYUi88sAa3r8vCRmJgHYvWmFhaY7V6dwnFAWXQFDSRzuR5ZHfoyyep5XnO8sw0CipeUi2anoJdyBEJwqAQ5JtarSFeoq4bnmpEaKMfbGArOCW9hlhy5np4aeDafrMlwvO5Kv8BPZenpYUX4ycnsOQ/sTnAProVIMlBixFUnQDsrELJvDjnLMZa6+ebKKpzueW+JXKXIMaMKyuINttCV3l9Vhtnb1zWZhs6humeQxkvlAVc2459FoXi6FdadLG98a1eXFt+BW0mtP9XZ+5Eml2pHBXaNU0bJvM9NYrI7BQN+BP6f6TBxGBY/PvbcgufXOo6OL3XU8IFnPgFPmgVLie9FGlm8UB49bUXd1mLH0AiuVVLnCSfaYrUExwIkEI8njWY2zrss7MtAsReoZeY+7bO5KaECgJbbuOfKy4q1gH3D8juNXYbbsLXTZMdI9l8aDcdaCGSF51NAnC7WrqrqbERdWnhOzXK2u2WLFhjcJ7jPYlJOqUHG4KCv4Ixa4Td6d+vk2oaxI40l1IUqJwR45ocqKsbXus1umDZfzZn5guDVeeEV8Ah7BUPdr0PCHS3YSfXSlRWPUFCKNkctiMOabIBnjPTkdEagHH69Eu0vSRDqR9tzEyKjzVemsJYzERId+W229fA4RPUfRBW7feTETvHLmUOsV39+zjtBiFKtXhK2TGz3s53G40E2FFO993PZNBdg1K0r7/kpG2JbFdZ9WFuGePgx375ItSNQcnE01wwGcKNIMoBkzu3jbMfCYucNRV3njkzwhHvhwqS4Dyl84XbdAVUV0lFUnlhwuofZw2Fk1LGrc6ZQ4qtUhWtMXb+HhDmju1/FiB2HAzFY9jGUV2EvRty0qB/dmMOgI5xcgxMmjx9hKze4MmWcu0rwHl3mxOg1gGTMGI9VtW9AhqOLWMzzqCLNob7SHmhU6G1iePU/P+3PLkNgmUFGGbvfozo8OHNmTTLAcoiXDUGeuRrfbCh3rMZQDoUNb17uz1LyPyTtmnXt6bFo+xGjPJ7vbGmV7fmZf7yGx4AetwbUy4b35XjsTweyIAq5hd7Ob7WsF49xYKqmPKF7NXStyBeGc3gCq5CTD4D3f30aTlLC6VU10cNmsJ5OZpc0yVJSPWkWs4iTFAa4ejpeIizo1Ko5O4riosjsc2WZYGYbXN8MsNLzwbkN6C/eHhVvx1qpc74lD63JGyQpSRwUs4ZkcZZMMd9lJHb8lBXFuzyJ3DEc1kWOu2NOqyzukc6N3/l3mmv3ABjc0VYlKIZVD0OUw/0rlfmE3AhZi4tbf5uFtvuISq5j1gmNX7YFW6nHPYn7EoBg9RLW/3In9fd5t7eC2WxkAOlVvj3fznoEMBzM65+dj2XSHA9w9xec9Swu4u9uvZitRWRoEVRyV8XYdb4fNgpphqSR1WNm6HcuXjO1WEGg/Zg4Yv19FBtA9+cjzbx/epuPp1yHzX/sGeTry+3928vg8JPz2tdPjgBm4weeHrs9/0a5fPrxVfgKtep6z1mkbvQ4k/8sp68d/6xuLScTw/Hp2+p6sb74dzTduNP2m0VuSB23dQEPqIm0fh70f3ry2nn7lof76OtR+e7iXldMJ+R/dmQJQVMB36+ZrU3x9nac/vn/MQJA8V0yX0ev4+cNbMMBwJX79lWTor6AqJ39f34JAN2ef8E/E2+//G/5jfHTJJQAA -->
