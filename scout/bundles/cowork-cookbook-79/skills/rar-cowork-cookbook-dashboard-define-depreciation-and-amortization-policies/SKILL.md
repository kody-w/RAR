---
name: "rar-cowork-cookbook-dashboard-define-depreciation-and-amortization-policies"
description: "Produces a self-contained interactive HTML dashboard for define depreciation and amortization policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_depreciation_and_amortization_policies", "rar_sha256": "82f97321edaabfe5c308e5fb1a85447e6bf44ed207dd9650eb5b11537e70874b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_depreciation_and_amortization_policies`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_depreciation_and_amortization_policies_agent.py` and in the RCI capsule.

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

Define depreciation and amortization policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define depreciation and amortization policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-depreciation-and-amortization-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_depreciation_and_amortization_policies_agent.py` and embedded as the fenced Python below (sha256 82f97321edaabfe5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_depreciation_and_amortization_policies_agent.py` first:

```bash
python3 dashboard_define_depreciation_and_amortization_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_depreciation_and_amortization_policies_agent.py   # or on stdin
python3 dashboard_define_depreciation_and_amortization_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define depreciation and amortization policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define depreciation and amortization policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-depreciation-and-amortization-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_depreciation_and_amortization_policies',
    "version": '2.0.0',
    "display_name": 'Define depreciation and amortization policies Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for define depreciation and amortization policies - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-define-depreciation-and-amortization-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-depreciation-and-amortization-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd56238a3a051b6af',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/define-asset-strategy/define-depreciation-and-amortization-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/dashboard-define-depreciation-and-amortization-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardDefineDepreciationAndAmortizationPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineDepreciationAndAmortizationPolicies'
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
    print(DashboardDefineDepreciationAndAmortizationPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6aZPiSJbtX9HEfKiqUWagfcm2MntCCIQQWpAAQWVblBbXhvYFEDX138cFRGRWV/e81z3z5ZGWEUhyv/f4uau74rcXt+/isnn58mIBt0AWbpYlMWgQtwgQsbyUzQn+Kk8e/I/4ZdE1idd3ZdO+fHoJQOs3SdUlZQGnG00Z9D5oERdpQRZ+Hge7SQECJCk60Lh+l5wBIttrFQncNvZKtwmQsGyQAIRwGPxVNcBP3FHcXbubl02X3B43qjJL/ARK/4yUFShaKBQOGhCvKS8taD4hRYnMSIZGXB9iaJECgACq9gakiwFyTsAFNK8QM7i6eZWB9uXLL3/99JLA7y9ffnvxM7eFt15m78Bmd0yz7yAJRSB8B8h44oEiM7eI4NxqgDwW8LoCDVxWDm/BlSHPqx9HTj4h//Efp4vbRO1PX74WyPPz9WX8t+mLO9SudNsOIvfdyvWSLOmGV0TILu7QIg3o+qa4EwzNUESvj5nfJJUV8vP47MeHktcIdD9+fYF8NXfMX19+QiDfX1+afvz+OkqpfvzpNSshOT/+9E1O23sp8LtRGET9+va8foqFA78NTcK71p+h1Ic7eODry3eLGz8P3OM64cyX17RMih8fgqumPIPCLXzw40//SKwfA/+UJW33/yT3l4fgGLgBXNMT+E+f7iT/FUGfC/qQ+Y/VVtCs/8xK4PB3dZ+QJ1H/SPad/78RnUF/az8Y/7vi/t4E9Gfkl3+4tv9uwick/PoyAxkMysb1MvAF+e3NMiTxlx+Cbzd/+OvvUPT/VYxV9o1/l/CWu0USgrZ7e/vlh/Z++4e//vJDX0FfA27+1jfZ35P593i96/kDg89RP/5xLtS/LU5FeSmQD09Hfiurf2t+f0V2bpYE3+63X5Dv42X8oMi4iHelDwq+i5kWYv2Ox59efodZo4Cr6f37Yxjl//7vyDrxm7Itww6x/LLvEGjgLsnBCN6OE5is2ntsNwDy2iaQ2Oc46P+jhUfEZYj8+n/8e8KFqfORcCcfifLtkSTfvk+SbzBJvn2fJN/ek+Svr4gN1ZVNEiWFmyEbwTC+Fm4Eim6EAkXAlHm+p8cOfIbp6fP4ZUypv/6LGt/uwl+r4dd76k4euWwjLsc81vYZeB252MegeK7ch7UGXIHfQ71Z6UOQYQLT8ifIUVtmsFB0I2/tKckyJEggAlhzhrtsyO2XUdivv/7qQbBfi0fiJZFHMWoncMAHHOTzZwg/zJIo7r4WwI9L5Ifffv8B+U/kv5t1Fz7qMGBZeFoOIlQsXUNgJPY5HDZWIJio3eBuud9+f3IOxRSwekI7J+FYrsbJ0JNPIHg3gCULnwmaQTwAiYek59XIZxEhSfeKLEPkAy9UOj4a831ctt1YIEERgMIfa5oLl/PBZFF2SAsN0obDJ6RvwV3rr17j3iHmMCW43a/IWjRgdSkz+GOEeR8EJ5dFAun/cI/HfSik+aFFpu8iXhFt9F2kchu3ihv3qSN0H3aBVeV9OhTuwup7+VqMxRWMVN1d5UEPHASZ8Z8m/TzaHHYVOcwaQfuu+z7GHWugfa+FzdeifQaJ24ym8GHRgEqjPgnG0vGXp0u1cdlnwZ0/iPRe9h9WCJ5Wufvg7J/qNpZ/27p8dAjI157AcAr5/6DtGZctLBYbaSHY0gyRNHtzeJhjBDua7dEDwl7jjuweet/6j/fs9Z7EvxZZAn2rGf7yGHk34nPMIzH2DcSwETbIOxnNXe7dwUeHbZpxSe7X4r1afILs3VMjXDLMBjBaRid9Vzg+fUcaQw7H62+dw90hIKeQO+jESNV7kDIkhER4rn+CqJoxSJ/Wgt4OxoC9xIkf/2FVCJQOnQrKRyCIBIYdrCh36rQSLhPGZ9iU+bfhydiPVQ/jBwjsmMErsodxNvpaC4MbNlXjGMjCD3dRSA4gxxDiB8Nt7FYPMGOT/QTojrYoc+j+31vg+fBbZNyxjPChVDdwO8jlZUzgAbg+LPuB82krCDYfY/k+6Y/mfq4V+b6s/eVrccf4UTNgisjGjuA7chDo3nl799kxw7UwS+Xg6UDQE+7F//VRvx8NwgeWL3/aWfz4z20+7hV5+0fLfUHirqvaL5PJo4q+F9FXmF8mY4hVoP1WUD8/wu/z9+H3Gar9/H34fX4Pvz+oe7D3BfnnIP9BxNPXvyD4K/aKjY/UxAejMz8/kCHx8/TwmRqffi024Jvpn/4xJu1sGCP9vYK9D4FlLGpANA5+VLR2LIQXWHvvKRwa52vx4R7P4IEVoojG8tuW3wX1vZRDYz9s+VFp4KOig7qDsU2MwLitykb4LXj5UvRZ9umlcHPwr26nxhIDvRoyNO7MYITBVqwbH8Grj7ZsvPjj9vMeezBpBOWXMQQ/IWML/Qn56IY/Ie/7k/s2sOjhBu2XsRMfVcKh8NfH2I+9rQde4C6xG6pxNY9N19gAPhvzP4MYIw8ivqfisRA+Q3nU+Cch8EsUgebPQvT7Fzd75pO2c8cmIOnes0ALcQawpfqEQHvC6IQBB/NoDyf8WQ3U04C6h9U2GJf7jb9vyyofa/n9TkP32Ln+9vKeV542eHapcDgM4M/tWG8n0HehQnj98DL47H+rf32KhQkSNkpQLkeEPEsSOAhc1wsB7ZMYB+jQw12OpigWMF5IUSAgMDYIeIbGgEd7OE6TLGAxjqU8KO/hwm9jr5GMUAnX9TmfxamAZ13GByTmkT7ACTxgSYDRPBlyHIAyv009wez6XP9jvSO5H630yNOTht9ePIaCI2WqXQqPjzjhdy5Dqp4We2jDhIJfTJZesq0tOzzK+/1tywNam2laXiwGAs2pRXw4Lc0TvrEFyZVCHKwOBmaF7Qm9kr4oVVaxcAMjkNdElkrcbNofJ2d5tlqV3Txtj1Z2UPPSreaKV5v1wuJv1xTU2lkpeGZqxf5wwvQr7W5tbT2sz9PwzNwO3ZlY6D3OFEng0yiK7hy+rvbgqMUyEbjzdVdVp2Zm2nThF9HFu3D97kA2BuWqq52+W832y0On7ytvz2D1CrTz1fWKc1y/5qlpTGEryln6zp457g8dsdpud8xK3zC6feQmepFeWBAap7VzHriWPPK3ORsRu2R3tBac77Y7i9Tws5Lh2eqWzn0uM7f8heClmsmx2nTCVKiPeHMDRmF6Gbs0D2ZLaEpWuen0EhTqIkqOtYW7bj7DyOX85igCF3pOVGXYyhPtDbnaVxoVH+qem1Yl3zTuzLn0Bw9lDFDvKpDQi22+mFtFKU1K72AXtgmzrbXDTobaCukwjRrNqt1p3e03jkvnXYBu4nJ+PSf2YSbwalQwrbWCGXc5R+kDjGbPa7STai0u7k3x2cO+O6THgOj6vUYK+upU4lOni8I4tai4m8qWl+LNnEn3Z1kE9bkRWz9YTYhCSNGsLrLjXuDOAhdgFxMfZrJPsBQjVK5KGtdblg+0z3lT7NqXclVkGXkDUXYlqpPqdr6xoQ/kOVl2e7R1pls+JiQqnakMhwXHqYhnwFWP+wUq89Pj0bGPmOIuiSs+8eSskmgd3+3xuZ6pmcpdKRqIODMc2Vg0C3RPFYK68Ib9KthYDGGYEwPAhvDYetsho1nteIz4fJINfu0T66g+WaA7LAjenBONGbpzw9d7TCZSU9qfOaJiIxq9JQv0anEONzmSYazD6GlILl6ftAlj8DOdCa2GZYLJBVVLWzYX/EDFw0bxxBwEuLccAEwjijzgdbtfaUm499K674rpWdU1a93WZWCWoaLlbjb0scJO9yp5VGR1dV0P87VDe6v1ksiwflbLWt447QKTNmqxkjIRFw8K4Kx+M2ykSl3jpEi4LZPmO3uPs+tL5NubKzM4obga9DNp53l0ZAP7uCqWhHUuMctXPMw7mtKCwnjH5YNlQRj8tAc0rjjTgMupgJ3sPPrMmF0xcyZkwQjidM0Em6thy2hoU94tXlGkTRPGqYg80G0JbBXD3dXtGlOsvTlJYTMVcgus5gUqz+1FWFYsby+v6ZUluNhVpEN2FIlsahM42tVLWa3KEJ/sDG1mdKxY3mRT9DfaZofq8+Nwnk2qfd0NmwOL3VS+6xdbXNHS6WYPZonuSM1m0Zj7LO6DxFhZ13mPxaW38C9my0sToxwmymXvV/hNuW03Id04XCbrorptryg/3aptIke3JbrUpA1wgl3kweYE7WLOFdeODxLF2wpq5FX2AbS9AcQFs9lMM5wQNAXMS/pEtG1UHQEwb62Jajl+iMiTU3OUSnTWlCYm9eY0MJrnT06eicmt3QCZD0V1MeWutwMRmHPPu2T+xDemIXbq83gf6JSNTbJpHvM5bXL700En+UbdkTuGaKt2tYrOrmsvt7FgNJYz80PvnAnC8TKdqZiuXxfLOEhPs+GGNeZFbGBFamsUrdhYis907tddDCvPJHGJQSSiKdVeqhru8AuDUs5iYFZCRAWmd9UMY5gtp2mTYMfdgEbK7NSfZwWlinD5UtcWIrUSBE9YJXvoMpIV6acaVgDBnhYierBEN936hjmolKWvLF/a72Xb99F8dZ1W27xT0+1AcmXWB02VMnjm1vJm0bYMChyWoXWnUTDTEiS+Enc5WWDuzp2mqF3t6hYL42iFbjBVvxgTWlnyYcALA5tjkBjtOvF1VA0nwhlVSDbg13Kon4LrBl0R3aa1WeqGJ3ufxNVlRPfFWRNFrs58NXf288WBLXquIKlVOkRAtjhhlwUnlr/Sa5YfQrLpDP3makuwzhVpYXjLvZk5R9bSYlvRL5WyvzrSKiIUdWdtSrTKzrG7nu3qRd5MywZs3JZm+RbndvKqi4+Z6K7KGcEX8hU0Yl5dOVXI8OPsEmZiP4H7lN3MTfpadTaOs7hV9W5my3QtRXN6Fjq1iJ+21VJtfNNT65Y8ZElExNHRrunMSWmOyUxHK3DU6A8OYcfqTMIHv2Qvx/3lqKRaqwW2Fne0aF41x6NOa2xez6A3kLmkDIvLzTxZGRA9bDmtbGrRrjFhsSexcuNpvjDdUPMbsdM8156tqXrRLcnUTchM2S9tYWvlqVuuuZMouUeT6ukV41EAc45VLKLSam1aZbmXNEWwkmEYsNmUnZ0aMIfJD+NgKZ+b5FAdhSkz0U5YPz+2c2y2SZubcWoWabLAbqE0R7vddu74C2JTuMEpMvWYd+mpHW3JeMrbTq0fl0XH5uYpP/ZTmKS0OpkPBN/tefzoz48Wd/J2O/VyiYxpRgUJZe28k5tKh1Rnd7kHHOhqwhqzF1StiwabxEyAKfoGKEAZGsEx1Xxuzs/cTpQnRp01neTuT6kmBcQMKMmE0rHW2m9rTMSAlO6lSFgelRwdjJ4lsZj1pE7Q+WlI3M58vE+2QbC6XVwd+FcxPqlKjzKMNL+xc6vOmbIW56IdeyyL9pZWEPYhVNZkZ4q0MBAcSzqxPGu7ycp2KjfwZIMczN7xmMBZ79P51dB2oCO7zpDW3uzKTUv5fEzty+G4Jy7CAnZLBz0Q8yiWBbyZ0W4zWwfmStc23LnZnXCtHjiXm6blmrDq9XyIfXUfY0xoKmY8c9erZeLvt/1BjsjZCYafN8AeJgs4Zlu6KzpyVumROrfbk7BeRZO+R92tdKv1QG2LrFkqoTTZK4oXY3tUPhFztFQaX7JjYZZfmqmlYPolWTh8El5nqVwdqj6XfOvmC+ESbvFXIXrYHljfTvDA3w8XrZnT5oS9JMJCh5vdSJmsec44ZHAfbi8qa3OyrzUj3XiKk0EdMyuYwkNpyRKBpMtWWTlm2q+HKAFLXBSyncq720278N1gn+9oC2fjznLqfFts6ox2razurTlGFWd9S2kySvoSSZ/jVdxa0ixKeydyimPeuAKVD81xft7i88Byzrq2GkTGcjgrt+Srp9I4viiieXOTyN7KypwMiZRx5iSrx+YVLDjldouD68op4niZqT7sihJ9zVZRLbZ5vstWFlF23sFd9S5GSbbQ7Xgyn9ySOW+VeMvDvlVLMV6WZaZ0l7GoN0NduVJkKsMKr6ViGNufjamhUirPvcpaSPFOg4uDupJoW6uDuMiLPtgSldt7oTd0zPwySF0aZGqvm67LAeHITK/X3HfU64k1jkKB26cYd7W9Z+/WJlAV8owKTpTNXR6VD9d6FeCO4ASWtDqDs1BLnmj6KV3vhmy3iDHhMpPLdY0Xphyvj8zm6twoQ/BaQTuGbLvrRM2le6ITN2ZcxzPSOc+EKyDIwgSwS+Unkk5XS0w2Z4viMC2AL8sBbehRj5fnRVyKeX+5rIizuwuHTTRVbmm4bAt7nxHLdWLG7k1YLoThIDbKRbDMzpMZQlVmxmlJqTuXwiyvDW13mNZm55oaLqvDlTtf1GMU4MTsJO5SQxHdQuNax6kuVLCJMnoxn1KbWaRV7HpquBnsDmCPQ2iOGtTNqcp0A9DppVpfDVCml8wE0gYnFN7Z3pJaEYijM1i7VnKcvMimCjPZSkGq4wJLiDs2c7LwtAXh7aZSvMzW5xC3c8xYcirRt7Bq5WKCX/kZ/Nar5aEIiCMeUTrfAYnOb+v5JfPON4l1A6vuNWO+xeNFMoSU3o+ZuEk3mLN3zmvQy0R/Vs7opd7s0RPT0mgIS85shpKMh4lmq5BeTa2Us3al90IkbP2dOlN6q50D9Obv44ZYOc7uUE6sCncN4RoGsiZeZf6WBWnquEVc3jRWyTkqXhCXiV7SpKFNaLJmbnLJcd550uH45DLHxPYiFV04we2JTs57DzAbdO3s0KQKxAkQwQYsxT7x7Ho1mdOYdpTaFX8GmxWltDc0PnNJIhxWE1razXpTWeikKh2gPqHN0nXObWU/ON3QpgQ6ODhqbXM3zF4OWzIA2X5D6bJ+yVrVifToVkNn8nk6H3Kl9XwxXdxSg1H8Au+2oUEvV9uzd1qFJ4NrFh3DputlnPOco5FTDqBDfqOF8MxeDQxP6mh3CsvjdlLJOBltu5meNesYrRPvwIE2OC5Quk5RwjkmBnoOj5fD2uXLbUFJt4OwZXytP1O5HrPVDSW7uuwG3GW3syFR1wd5ly1ZHe+8cDhkaOVl3CVyfZIpizTo2RVFsLSsBXDDJBbsGTaSzcwgwtNw6C+ulJ1SzO8cm1heQTu57phFOF1KMzBceLCBnQ6nBEXN+EAwl0ybXufF2gc7cKmnSZUGZAe7B4XVW6aiCjLx9FAXuG2zcLCkEBVl4pQx6umFcyapNCYMXAis1X5+meCAOB7keYxFVdJFwkVk+MvxYOjTeO2YO9gRTkpJwRfUcnuecJzeZuU2lyYzWdS8lido4jZtUv1MMxfnkNNFN0+xwlP43FvLiV6u2WavLicXNmv3aE/RROCseLgn9acDs/UPVD+9nrnVRW9lE91qth2xF5+IKENlVJtl1lNd693u6pWVUCXqtAV6H7uMEcyaugiObGbbdhgT3T61twsUHANjgx6YtKNamZxdTqWerM+tHmkoE1wNQUjakFIGRy1pb8mFcilQi6FhmoKfsVJEdOTl5nCCywZnc5hR8lkOUj7M1VBGE/TkpZhjnDaRMOEvtwkwZmluMKu9Hh6z9IozLDkJDyuzx7tr706DktT2bMIHAmE2HZFO2CgbvOtJY8i10vIWju7WCpWwSVJcpufLblFsbv6N04aDfN6XkwO7gS0fya+6FLQzTrMFQ1DEEA/Cxe02OayWVU2upy2tGQdu5bLUrujhzoezyWVigoYWYBPM6itRLjcYMJfGxjysqO0cSLnTHohyUW0X3KwXbngXo3ygESm2RLNDND0ItcqWIdyjRinBnWdX01E6O4zMs28shX0x3UWRMedL0Z9EsEbXkxPBqW50vNDJVNuexbiN8S2oZhaAqdncZf3FTlVGlkgOvVghyZlJbw29shdRdNoY7VVTs5ucTDCsY+Mgoo+ojQfohZcu+vHgKPu9g+fGsXMbdBtp5uTgO+seBczkFNETW418XyDBscTASbWXl9NteyjbYC3brOCIVqEqxnzR0jwmy6So6j4FexdAnsnlJjhfGRUlN7Z7rsRSEISff3759DKebj/PqP+nL7zHA8L/tXPKx5Hi+5ut+wE1cIMvd11f/sdI//rppfETiPNxcttmffQ80Pybc9vP/+JrklHo8HjjPL6uu3bv7wM6Nxr/4uolKYK+7ZrhrYX7zvuB8qcXr2/Hv/Ro354H5y93CvLqfgr/jgN+d/37OfZbV74FSVuVLXgZ/xRjfAkFAojs/TJ6nnDD2QO0ceK3byRDv4GmGgl4vnkZT4DHVy8vv/8Xexu2rQEnAAA= -->
