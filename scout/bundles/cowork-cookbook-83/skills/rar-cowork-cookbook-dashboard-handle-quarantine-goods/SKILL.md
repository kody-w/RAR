---
name: "rar-cowork-cookbook-dashboard-handle-quarantine-goods"
description: "Produces a self-contained interactive HTML dashboard for handle quarantine goods - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_handle_quarantine_goods", "rar_sha256": "220f55074e5b0a325a33b0173afe34376e2c53c4bc69455c29e308ab162c6801", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_handle_quarantine_goods`. The original RAPP
agent is preserved byte-for-byte in `dashboard_handle_quarantine_goods_agent.py` and in the RCI capsule.

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

Handle quarantine goods Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for handle quarantine goods - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-handle-quarantine-goods
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_handle_quarantine_goods_agent.py` and embedded as the fenced Python below (sha256 220f55074e5b0a32…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_handle_quarantine_goods_agent.py` first:

```bash
python3 dashboard_handle_quarantine_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_handle_quarantine_goods_agent.py   # or on stdin
python3 dashboard_handle_quarantine_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Handle quarantine goods Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for handle quarantine goods - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-handle-quarantine-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_handle_quarantine_goods',
    "version": '2.0.1',
    "display_name": 'Handle quarantine goods Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for handle quarantine goods - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-handle-quarantine-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-handle-quarantine-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1313ca5585b7c314',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/handle-quarantine-goods'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/dashboard-handle-quarantine-goods', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardHandleQuarantineGoods(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardHandleQuarantineGoods'
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
    print(DashboardHandleQuarantineGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8166bOiWLbvv8I790NmtZmHGSQ7OuIpKoiCyKyVFVkMm0kEZBCwbv3vd6Oek1VdXbe7It6HZ0ZmCuy95vVba2385cVtm7ioXr686MDNEcHNsiQGFeLmAcIXXVGd4H/FyYN/Eb/Imyrx2qao6pdPLwGo/Sopm6TI4Xa1KoLWBzXiIjXIws/jYjfJQYAkeQMq12+SK0BEQ94igVvHXuFWARIWFRJDVhlALq1buXkDdyBRUQQ18hkpSpDXcDsUZkC8quhqUH1C8gJZkAyNuD7kViM5AAFk4g1IEwPkmoAOVK9QOtC75zID9cuXH3/69JLA7y9ffnnxM7eGt14WbyKId+77d+bCyBtuz9w8guvKAVonh9clqKCwZ3grACHyvPo4avoJ+dvfTp1bRfUPX77myPPz9WX8o7X5XaymcOsGSum7peslWdIMr8gs69yhRirQtFV+Nxs0bh69PnZ+p1SUyD/GZx8fTF4j0Hz8+gJtU7mj6b++/IBAK359qdrx++tIpfz4w2tWQEN8/OE7nbr1UuA3IzEo9eu35/WTLFz4fWkS3rn+A1J9ONkDX19+o9z4ecg96gl3vrymRZJ/fBAuq+IKcjf3wccf/oysHwP/lCV18x/R/fFBOAZuAHV6Cv7Dp7uRf0ImT4Xeaf452xK69a9oApe/sfuEPA31Z7Tv9v8n0hmMqPrd4v+S3L/aMPkH8uOf6va/bfiEhF9fFiCDqVa5Xga+IL9809Ul/+OH4PvNDz/9Ckn/WzJ60Vb+ncK3s5snIaibb99+/FDfb3/46ccPbQljDbjnb22V/Sua/8qudz6/s+Bz1cff74X8zfyUF12OvEc68ktR/p/q11fEcrMk+H6//oL8Nl/GzwQZlXhj+jDBb3KmhrL+xo4/vPwKESKH2rT+/THM8v/6L0RO/Kqoi7BBdL9oGwQ6uEnOYBTeiBMITPU9tysA7Von0LDPdTD+Rw+PEhch8vP/9e8wCgHxAaPoO/x9e0Dft+/Q9+0OfT+/IgYkXFRJlORuhmgzVf2auxHIm5FpWQEIhNc76DXgMwSiz+OXESh//re0v93JvJbDz3eITx74pPHrEZvqNgOvo352DPKnNj6sCqAHfgs5ZIUPxQkTCKufoN51kUFIb0Zb1Kcky5AgqaDiRTXcaUN7fRmJ/fzzzx4U62v+AFMSeZSNGoUL3sVBPn+GeoVZEsXN1xz4cYF8+OXXD8h/I//brjvxkYcKYf3pDSihpO8UBGZXe4bLxgoCwdcN7t745dendSGZHNY56LskTMBjM4zOEwjeTK2Ls88EzSAegCaG5j2XRQUNGSFJ84qsQ+RdXsh0fDRieFzUDRIAWLgCkPtjTXKhOu+WzIsGqWEI1uHwCWlrcOf6s1e5dxHPMM3d5mdE5lVYMYoM/jOKeV8ENxd5As3/HgiP+5BI9aFG5m8kXhFljEekhG4v48p98gjdh19gpXjbDom7sHp2X/OxOILRVPfkeJgHLoKW8Z8u/Tz6HNb/M0SCoH7jfV/jjnXNuNe36mtePwPfrUZX+LAQQKZRmwRjOfj7M6TquGiz4G4/KOm9bD+8EDy9co9B8U/6gvU/txPvtRz52hIYTiH/X7UioyozQdCWwsxYLpClYmiHh4lHsUZXPDow2BPcZbin0/c+4Q1l3sD2a54lMF6q4e+PlXfHPNc8AKytoAzaTEPe1K7udO9BOwZhVY3h7n7N31D9E7TTHcKg32CGwwwYA++N4fj0TdIYWmu8/l7h706G1oOGg4GJlK2XwaAJoSE81z9Bqaox8Z5+gREMxiTs4sSPf6cVAqnDQIH0EShEAlMJIv/ddEoB1YQ5F1bF+fvyZOybyoebAwT2q+AVsWHujPFTw4SFzc+4Blrhw50UcgbQxlDEdwvXsVs+hBlb3KeA7uiL4gxD+rceeD78Hu13WUbxIVU3cBtoy26E3wD0D8++y/n0FRT2PObnfdPv3f3UFflt+fn71/wu4zviw7TPxsr9G+MgMJDP9R1nR9SqIfKcwTOAYCTci/Tro84+Cvm7LF/+0Nd//Gut/71ymr/33Bckbpqy/oKij2r3VuxeIWagMEaSEtTfC9/nR6J9/p5on++J9jvCDzt9Qf6acL8j8YzqLwj+ir1i46Nt4oMxbJ8faAv+8/zwmRqffs018N3Jz0gYITcbxpx+qz9vS2ARiioQjYsf9agey1gHK+cdgKEbvubvgfBME4jveTQWz7r4TfreCzF068Nr73UCPsobyDsYG7cIjENNNopfg5cveZtln15y9wz+k2FmLAYwVqE1xhkI5g1shJoE3K/em6Lx4vcj3T2jIBQExZcxsT4hYwP7CXnvRT8hb9PBfeDKWzge/Tj2wSNLuBT+9772fV70wAucx5qhHCV/jDxj+/Vsi/8oxJhPUOI7wI4l65mgI8c/EIFfoghUfySyu39xsydK1I07luukecvtGsoZwObnEwJ9B3MOphFExxZu+CMbyKcClxbWxWBU97v9vqtVPHT59W6G5jE3/vLyhhZPHzx7RLgcpuXneqyMKIxTyBBePyIKPvvr3eOTAAQ42LxACgSBhTSNsRSgPcwlCdolSQ/DWdINAUmRLAMInyZ9yvMZjqJpn+AAiU1dD2cIn5liOKT3CMxvY/1PRqEABrdyOOEHJEPQNMXhLOFygUuxrhtg0ymLsWEAa8D3rSeIjk9NH5qNZnxvZEeLPBX+5cVjKLhSpOr17PHhUc5yWWfrKbHHVUw4q1Pu1PTbQJHJNq224AJqyrVdV9k1p4ZTekXv1/tYuiTn2QwrWJuiTxNNmnQGu82pYnfaKJnUVvKNoAZjmGmd7yzRW4o51lxbFQRHnTXAX22Cos9mo08FW29tQdW5qnAyexiu82ue36jsSsRSY12qdEfYExSVS+AeTfJs8LI87Da9oRlHn+h352BoF/PramDM46VmubIerEOuHxZ5Sh/czM4wr9BBbe1uUneboof0toDutfatcZAUogOJc8g0w9nXIMX88+04CfIbxoJ8gcfHAQ1zdbqvb/5BulhL21ABzrfZ0SN6odlXrpUKG5rdRCUbK/TWsjaeHV04MTY7HKevotdK/D6r0bm2cyuBwlaLCN3ZYXxTLpvMceS88ffV1jy11M2+SvvtARSSJ+6zRhIux7Wz2VYCY7U4ocwrzJFXOie2GX40C3A8SeXJPh8Wp4N3MHLDqtYpj0cRreUZN5OWZYfqkbW9RDbr1FndOCaY1xmzZ9fHlTTD0apuD97G4Vu/yoghxr2Ll0rKxTTynD53WbNOjxyceGSOnO3cU4EvHKULRdGK5x7PRYTI2oKiN2BnEua10i++t0Htq+JyG3y3xuo5NVnRbLmPKl3Y0eztXBDN4erfVrtJKFkpehX5hI7bc2CzXsBgkzXu04G8bWh1u2GmunUknAu6EaNNTx7swyF1G321OFDogFW8ZUd1uEX5qZvvof6O4DStWunrW3CpatOcWO3p1mc9MV1V/enG8qtYJep+tzQhWNkbf0hu+uqE5qpn3XbEpb1ubmtmJ1d1N51cE2NDqMu5MCxbtzDcttSZrMxwyTjjEtf69FJGj/3lamaTGcT2fdjTqJgLamYfi3WCq5O5aDK5g047VNssClLV2uDAOvRWUWidkprdcKlx7SxtO9rabCUT31XrQHYEbD/MU6E8GxMTNJO8o45p1ZnHaINy242ZnlQQyAx/mjY67vfRZTP0wZ5eYqeakvfbOj2uT7QA9FpQCJmRFhp/9NYenwiHGquYS2kBfy1R1NmrbieXErWpFe7kQI3OEJCSUBGw/JTWAXUAXQ7SxDjxeDrsnQTouGyF0m4pGhTI8EbqsvzAohIaB9pc64FaKqyo2drBQXdZBy5b2eCTvd3Xy8tuExfUNK/mPREnhYt1/JpXAmZ+mlQQStXWDjottWfEKQZH1dzU2WpviEkeyyBZdclWVq86plfkIIbdcjrI3WmXz+Igha1/vb/dsn4uapO2cTVbVPb55JQVG0D2J25blFNdk7Gd1KxZs0v05MqsjRt+qTtQMPKeFGKaWzmrzUrcGP7gEydj4p5DUxQJTlfOKponp3avC5aKxittzrTxZs9em64FBsOuFFXX9RXrClvBgGkvmo5Dp/HkZNpHJdinuhMfd0el2q55C79ttQBnJXVLJ7YZTPPz7CIqodGjRV/3jO/56NI43zKYS0YIcs0fjv0MBcSBaC+8xFHzOsSFziA2m+Mpr8iinQIcoCEnq9rV5ab5dXZIBEZlTlG18Ha7SMg4iLOL7Xk/IQetGNhFC/Spf4yUYG6lyWIgQeXXECF7UF8maLGKl/R1f/bLBt/2FJq4RM+fTA+/RiVT1EqqLoVJAvFxttDQvauH0jVaBtEMP8hVj8mUNDPTItWWa/28BVJzcAAmqbPNVApsfOss9dkuKS+FMtU42K973cxaYxFsTr2ztOHEuQ0E1J9ylL4vKxPU2KyTDuBK0buG7Zlsfrio7uYm5iSLqkZNg/q2jLJJeRiws7pjS2kjnyvOKK3qqiuRYTlGUdxmKNqcZp1As2lDCPO+5hb9dHpTk1QjOS5TqQygaaT30yLMRHN9oYOJyxDr/QqLYqxMXVExceqw12flqmuPyt6ZeZ67vcwskdlj8wzjK8GppWXRaoG1M8xe1a88aPfXUjrD8Y/tjWI3OFgQxjtT4orSLiAWOfM92mJWI8/YUAUWXyTBlFkSWDVjqr035eZcsAr02wW/bo6Jbs4cocYEegpUvKw2R6y3M6XAKucy8dvQK7iZuJ6tlkKT7pw6SYtgEaaLHa0zrNBIdidPGYPANhOgio7NCy7XzrObToMATy3V5MsB34juKun1iUNdySV7UPX1yQ1tAkgTeefqsmPFpwbi6bwR98Ki8aaYGRRX3yD6ZCZzZrQh2ls1AeUujADDa+ymssuyz/hbKk4bitwL07V0SIgY25iKkAaJdtivtLqHSaaqCliJa2egte1ZX8FaelzOS1vQxb3hHX3c68q6t52Y4p3LcmN56xlP4oHCZibLJ915UIldJG80TQ3r8LSbkpeMby78GiP66BichlurURc2NWb2NQlgSd3I7NoOWblXbgPDo+e9Z5y2cU3bTecO6DbP6PX5UtiKriarXMM38SZrNULR4hlTE3WT5ReevMiBsaGq0r4SioExhe6nU50yLB8HkRjZs5w8m521VAPZFQ+JRc9v2vaY4L6kb+dmrfPmxpRmwdKawMhVLYnnJiJp3Zg9riTnaLkxYLQuKpcKuRueXXYaT9Pu7KBG0wvViI7u3S76+eJeeJBXA6aGYb699VYn2xoqCTyVelivsnQszuvANAyybDy2mmOXaWt5zNGJueN2OO6kCd60nOzIqLFK5uK+KsNA3K9TcX3YLBfHgjwTnnfQOvnSofaGGrZLtUywUGLwIC85g0u3JyHu2m6llviQWVtW6+U8WTaHA+5aouaf9zVFNsR1vbEYLGih01lqHxvmRfFb3O7ocF/os4Mch6twqhcbBTM7igwP6Qps3HI5qbu17SXJQkSXa7zVrC6K+4OFxUJ7wue71tDDeHs9SXLbMGdOoomVjS0mzmrByIR/2NG4ed15gpxRHVNsXZy3tFNTHJMynIHWqzShj5ex7JyuEWnvo2UyuXh7wmTEFZz5Zd3OcmKZx4G3DPBZXhxu3XWxlRxru9vdzHOzCU+4uXEEZXEk/ItmKvhRN4+t3tOUfuNtkshOJBHeIgPP9mkwZ08qkeYdbTsVMZPONUrIrJYZlF7wbl25+J41ysVkW2281PY0HGvzyabW16R/DpPLkTv2jepc42pN8WRVnMPWTJdlrC+Wg1u0sXj080q0Fv1edAmo4942CkJqLjNaYONFIXjqpMIOjNmcg42aT4VrgHGypPX7S3s5RQJOV7Ylb9bLZiVMKeMgWvZsM5/PiRMMuGSwmRTWl+tWWC0vx+WR3mMFd2POl63Vk8wUDaV6MxHW5FH3ToawS457Qo/aqXLOrqjNpdImSxfXeDmIaVUelc7W1tWV5EmqFNYCY0wPxHJCrHjRp1fkdh93jG+f6iW/NicrtzWHoi/3cnQwtudhNeBUKoQn+TidGtjc6RTM2eEnz8ydM1eWe/6wPrIuPjf9sG48HHO1kGHgkIv55twxwlmXMMGU7K+d2m47bN0wxnGHbeyi6ARi7lrhoJ3n6yo9FOUutzNiI5/4faBFO2E+HPir1M3sQ71dlN5Kj8+D7K42JRCMqvUMd5hfutrdK5Z4HcopSgm3AndCO5obcr1Z4bw0rR0xogK52NvThD+h07g4YUHV5Y010/NsOQ8ae7iCY7/CVNRd56E8kbg5jvWcZg7JZR31mtPo1rV1+GUOe0qOYxZJH7qCJ0w5tnHCsMXgAIgCIGqO4bHHS5PG4QWz1OAExGzQOYB22+og0tOdZdNBElE2V4Mlk1Amz9gJwSak6+uXY7Aiimq9SwdAye28OppVU53pepfJMGOICylVnDcsNZkWSkE2uhgUDWozsMedLUwl11aE26GLplzEjr/s1lI7R5cs03TbidfqbXLp1pOctAqTEziyrT0BVeRr01txRbnLGxiaawt7GlklI1lhNn4csLA7Z3aqVKPbIAynS5VZ2fPM99BJEVIMsDGOrXJCCh1G0uQtC6Q2o3g2mMmiqU22eWEp6sTyrCLB8epoTCK3PqezAQ7XmDZrO+EkGnkiM3t/D8y0Td3t4qz2R1Hr2+0RThnkhqAIaea5yla5Fa6qdPyFdqKddrvcWhNnhyxfHiPTH3anG79lhGnVpcDhV92uyJupwJUoqmpV21Ipvy6u3hSvl9cMJwg8XDu06h/tk+waC+1AGvmEuV2VfNYdN1vaE6L2nB+nt1URstZlx5VBtkYZEs1FMRGzVcPtxXrWL08GWXPKtfCFiFVYLod52Hou2sga7BLtGvrt3FQs4dBsIwThjufZYWqCKeVBT4Kga3NC8JLZdopvCKA5KrxqDhocj6ilYeuhvsOK9pBO6AOalFii8d2RYiyJ4NLgpEyHurWWU7Rez7GDx+bLaD9dDeRh7oF+zk5nVOKQDq33PU6uiMhR1M4qlxUVX2GJF9WbG4You1qRS7/tOHOOS6VrM+iM9bLItNhYOm3EubRkfWqZdD5zW4P4cHWuEq4X3knhqTYINd4/kgZ64CagDQFJs8VWIeDIzx5vuFnflHTn3cKMJ7a4RAxrdLdcsZ4qb1CSTq9x2xTEcCDtyVUIgcQnotIpxzSq0EMfpFGHN/xcxOh6HtUOZuek17DAmvZuSlrkDJ+1QtKxzLyCdhCuFkfbraEoATEhPdPc7lnc20SNuMLbORmxLR/Ks72ypEOLmDtZQErYYWkuWEEdmqNYafwi4kQWO5uOJcNw8e38lLCiTe0XXdqwJ9NcVMzNU+sGZfoAz7lVsJsw07kbLsB2oQZcsGv206L0r9zF3sK52UXji3w12rjJLUUhb0R6uLA9WdYC3TdXLERpOENQF2HKTmZES7uTUF5RCQxbY7nEqM1pKKpamuLoipg3FoxbDUstMrPCOXdz2I6bYctltzGzqaOiOFYOfGLuG1K81q2MTTYuS/VkciOEbtFSBcq0w5y3vHpayCAWNW4WcSstquI9PtWPoL+5Jzfbe92OXqg2kbMERjpi0ePrfs0PcyzED5O0h4W3psJt7Dir2iCT4KqS8myrRBs4afI2sSA87GjSexVvLtp5L4TEkOwX7HD1OldjJWhu++oCWmN2NZWAQARHMVyQ21s0314VVvLSq+YTArEz9MC4hbGX06jmYtO8JaaxvIvb+cEp3eX2TC7ruLFQ87wwVWK7um2veXk9zkSVof35LRLoQdmh9Vy3hFNLz3klLQls2616XM9OeZLbLmrkYpenrdvd0pPPXtXab+uOW6GzuR+lQrvd7Gezl08v4xn08yT5P399PB7t/T87YXwcBr69U7ofIgM3+HLn9eUvyPTTp5fKT6BEj3PUOmuj56HjP52ifv63ryLG7cPjnez48qtv3s7cGzcaf1P0kuRBWzfV8K0usvZ+kPvpxWvr8fcN9bfngfXLXa1zeT/9fuP4Mv7WYDxlLuDmpvj2/GXG/fb4UgcEiduA52X0PFuG+wfoo8Svv5EM/Q1U5ajs8/3G6IJX7BXa8X8AJypjmM8lAAA= -->
