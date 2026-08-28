---
name: "rar-cowork-cookbook-configure-reserve-budgets"
description: "Applies a bulk configuration change to reserve budgets from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_reserve_budgets", "rar_sha256": "75c1e518be4af43832e65b525c6d7ddc82605985bc5463a3f6651c3f0e12ba6b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_reserve_budgets`. The original RAPP
agent is preserved byte-for-byte in `configure_reserve_budgets_agent.py` and in the RCI capsule.

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

Reserve budgets Configuration Bulk Setup — Applies a bulk configuration change to reserve budgets from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-reserve-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_reserve_budgets_agent.py` and embedded as the fenced Python below (sha256 75c1e518be4af438…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_reserve_budgets_agent.py` first:

```bash
python3 configure_reserve_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_reserve_budgets_agent.py   # or on stdin
python3 configure_reserve_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reserve budgets Configuration Bulk Setup — Applies a bulk configuration change to reserve budgets from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-reserve-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_reserve_budgets',
    "version": '2.0.0',
    "display_name": 'Reserve budgets Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to reserve budgets from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-reserve-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-reserve-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2b36e23b46df8ccb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/reserve-budgets'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-reserve-budgets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureReserveBudgets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReserveBudgets'
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
    print(ConfigureReserveBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6ebOiWLbvV+Gd+0dVXTNTZjE7OuKBiIoMighIZUcWw2aQUWasV9/9bdQ8WdXd1bc74kU8M08cgbXXvH5r7c359c1pm6io3j6/nYCTIxsnTeMIVIiT+8iq6Isqgb+KxIU/iFfkTRW7bVNU9duHNx/UXhWXTVzkcDlblmkMasRB3DZ90AZx2FbO9BjxIicPAdIUSAVqUHUAEvkhaGokqIoMCkPivGwbZD14IEWCOAUfkD5uIqRz0th/8pg0qoo0dR0vQeq2LIuq+QTVAIOTlSmo3z7//LcPbzH8/vb51zcvdWp462310gNoT8HcUy5cl0KVIEE5QvtzeF2CKiiqDN7yQYC8rn6sQRp8QP77v5PeqcL6p89fcuT1+fI2/dPaHGmiyTSnboCPeE7puHEaN+MnhE17Z6yhyU1b5ZNnaui+PPz0XPmdU1Eif52e/fgU8gkq+OOXtwKq8LD8y9tPSFFBeVU7ff80cSl//OlTWvSg+vGn73zq1r0Cr5mYQa0/fX1dv9hCwu+kcfCQ+lfI9RlGF3x5+51x0+ep92QnXPn26VrE+Y9PxmVVdCB3cg/8+NOfsfUi4CVpXDf/Ft+fn4wj4PjQppfiP314OPlvyOxl0DvPPxdbwrD+J5ZA8m/iPiAvR/0Z74f//451Gucw6b95/J+y+2cLZn9Ffv5T2/7Vgg9I8OWNB2ncwexwU/AZ+fXr6bBe/fyD//3mD3/7DbL+H9mcirbyHhy+Zk4eB6Buvn79+Yf6cfuHv/38Q1vCXANO9rWt0n/G85/59SHnDx58Uf34x7VQ/jlP8qLPkfdMR34tyv9V/fYJMaay/36//oz8vl6mzwyZjPgm9OmC39VMDXX9nR9/evsNQkMOrWm9x2NY5f/1X4gce1VRF0GDnLwCwg8McBNnYFJej+Iagf+n2q4A9GsdQ8e+6GD+TxGeNC4C5Jf/7T2A8qP3Asr5N/ADX19w9/UFd798QnTIsKjiMM6dFNHYw+FL7oQgbyZh5YvcR9yxAR8hAH2cvkBwRH75U55fH8s/leMvD4iMn3ikrXYTFtVtCj5N9pgRyF/aexBuwQC8FnJOC895Am79YcLmIoXY3Ey210mcpogfV9DQohqf8Nvmnydmv/zyi+vU0Zf8CZ4E8mwE9RwSvKuDfPwI7QnSOIyaLznwogL54dfffkD+D/KvVj2YTzIOEL9f3ocaiidVQWA1tRkkg4GBoYRQ8fD+r7+9vArZ5LBzwVjFwdSJpsUwGxPgf3Pxact+xCkacQF0LXRrNvUQiMhI3HxCdgHyri8UOj2aMDsq6gbxQQlyH+TeCLk60Jx3T+ZFg9Qw5epg/IC0NXhI/cWtnIeKGSxrp/kFkVcH2CGK9NEBXx0DLi7yGLr/PQGe9yGT6oca4b6x+IQoU/4hpVM5ZVQ5LxmB84wL7AzflkPmDpKD/ks+dUEwuepRDE/3QCLoGe8V0o9TzGGXzmDl+/U32Q8aZ+pj+qOfVV/y+pXoTjWFwoPAD4WGLezKEP7/8kqpOira1H/4D2o6cXpFwX9F5ZGD2t/1/tUfZgRuGhtOECtK5EuLoxiJ/P8ZKSZN2c1GW29Yfc0ja0XXLk8PTvPP5OnnyARbPALT6Fkt39v+N9D4hp1f8jSG6VCNf3lSPvz+onniEaxpHyKB9uAPgw49OPF95OSUY1X1cMKX/BtIf4AeeSASNAEWMEzwyQ3fBE5Pv2kawSqdrr837EcMK38yHeYdUrZuCnMiAMB/OKGJqqmuXgGACQqmGuuj2Iv+YBUCucM8gPwRqEQMvQ6B/OE6pYBmwpJ6ROGdPJ7GIKiF33pQWzhggk+ICUtjSo8a1iOcZSYa6IUfHqyQDEAfQxXfPVxHTvlUZppJXwo6UyyKDGbs7yPwevg9mR+6TOpDrg6MPfRlP6GqD4ZnZN/1fMUKKptN5fdY9Mdwv2xFft9N/vIlf+j4DuSwqtOpEf/OOQispqx+pNwESjUElgy8EghmwqPnfnq2zWdfftfl8z8M4j/+Z7P6oxGe/xi5z0jUNGX9eT5/Nq9vvesThIQ5zJG4BPX3PvbxVWMfXzX2B4ZP/3xG/jOl/sDilc2fEewT+gmdHkmxB6Z0fX2gD1YfuctHcno6Icn34L4yYELSdISN872tfCOBvSWsQDgRP9tMPXWnHjbEB65C93/J3xPgVR5PdIE9sS5+V7aP/grD+YzWO/zDR3kDZfvT/BWCaVOSTurX4O1z3qbph7fcycC/3IxM4A6TE7ph2rzAQoGDTBODx9X7UDNd/HHT9SghWPt+8XmqpA/INIB+QN5nyQ/It+n+sVPKW7i9+XmaYyeRkBT+eqd939G54A1upJqxnFR+blmm8ek11v6jElMBQY09MDXs4r0iJ4n/wAR+CUNQ/SMT9fHFSV+wUDfO1H7j5lsx11BPv51AHAYNFhmsGwiHLVzwj2KgnArcWtjn/Mnc7/77blbxtOW3hxua577v17dv8PCKwWvGg+SwDj/WU6ebwwSFAuH1M5Xgs39/+nsthEgGhxC4ckF5GKAwxgWkE5AEQ+CAplwKpzzaX/i+x+A0Si0ZyvUokiYcIqBpCvOIAAUY7jq0C/k9M/Hr1MfjSRnccTzGW2Ckv1w4tAcI1CU8SI75CwJAZkTAMICEfnlfmkAYfFn4tGhy3/sgOnniZeivby5NQsotWe/Y52c1XxrOwly4WuQuKxpcbGu+c+PzTXc74ZgmHV1FqpKsdC4X8JjZGfhqTSU3J1NX47bZyxh/OEazQlsmV4K4dxyfqj1qnnpzQ5+UQcwob+bP8m3Xntfr41UhixtTViLY0ZaT7+Orqktz8yZlZqqfaIA1mdEKnGFdrkEwx5Scs4WyPBvrRh4S9S7r/mW0xlTbGGvVXlFSPaxH4V50dHLzOrQ5i+WFPg/KUNAt1oqOrZeonDkgVoTEHGfaHpeKQhcyoVhuS2bmd/dyFnRXYq6V4xx0XRZhK8Y6dU6XipRoan51xssbjV2yVDw7OCbswtqmyRGQUMvRMqIbJon301X3Trm00GQi8bWizLhVbmjYzZAGqjsqMUwFYzQlzDgXVno8WqJdh76wofJb6fImpziU4Zzz5X2lWSaL6orSac7+kJtNgQWn5d6jsTE7efs0KeXM3w8aEYGBStVB2JepvAyq0zqyvUMupsFKki3FjIMqD+TdaUUTotCw7BGrMqr2RIhvnkQxlHkP9NoWT6S1RO83Ls8a45ZyTEc5xl7tvDiNUqpwM/IQXYX4iK8qW9FoLFoYhalHim5Vwi1ph06pxFPgdPq4rjiwjYEaGzuHjHVPOnuEx98AnDbV8wyf5Xl+lBNFV+deDfcrAbqv/ZZe4QDX16DODFxLlzltjlqsLk59vE+NVpJ9q+zkar+0s4IYmf6gZlIkC7c+HXpt6WrA3q34xS3TBUsOSF0bvH0R9J6JXy/X8ayWFM+fBoKX9udlVA/zxaG8SY1tGP6VckW37+tTtxrUe3Zax/5+W1dy0iiBZSsHy8bEINd52drS9ski9wdCysnDtj8famnX3EtNEPMZz1BzJSfofq5JPLur1NKnS7wdl4a7NvGNfo6AkeuGvqtSJzVLIRkP+JXFJem4u/TL+HznqRsBFnq/2uxyjw06MCYkxVq5fQgJvidSl72MsEvl5m1nMgLF+lwtrA3FShxN5TbE7l6uL6KMsfHtEtOrs6YLqW9eSE/nBnKRe/vdqHbERc30C6Dd/ghOyzURNtduKbnX4TIXwxq/Y0oTo0NboO64JS3br7Bx2Z3G+T1g8fF67Ys7OpM41lnalpeZwyzfy+l+HjEZluiGq3etKm5kgHFe6Wz6jbXuBuk+54YzpqO34MwGljCs0/NmEbMKbefq3jWMWySU9wAYdT8sddfvwzNVL2XDCkjqbF56y7olawYDGaHsB5A1TmnNSvEk2MYmFzTUH9228HSqEMvglmIVR5YHsVIbPPYNPGI3GMUWgcbMuGpVlba0x1RrdVkHbZGTueGuEmlIaEY/OzeNU4wDw+meGV3SRmmbi04Fec7iOx0wNYslOyvF6bSyy9OAZ2taW8mJoa1bX7XToXLVc8jvmqW2x7D2LJXD7ezP82t44xT7PszNpX1DC5ya2YKaOwLuZTFzoJdinGzrrRhBDqkSsGw3I2tnhh7xG+arqdWwS3V1W+Jz3MrZ2V4C27U9J+TdLrePJwJLsyvrFzw5arw0P0c47RU3i81Us/PurM3erpsr3+buOuLX/TKzweHG9yvH63apqJ5L0OWhK7d+SccLi7rlYj1DPeZoZPaWO9YiN4a0Tgqz1XwPjrWWXlrKEnar63xtcwra3PC5e8bw634fcXsWVKfrSmRV75SMgwh3iNUK9YSE28cmr6Do3YZfF+qpZZSWotzjOfK9O6jDVZV64Ib7marg/mC3Ozu3LHxxae8M5llUT4FVJmP3qlqq+yQpKKnTNyQOhp2qcbIPGlfmiRnO7sdFnikEeWEr/XAXjFk1CPONZdGW1I2auGAPgtSXjq+axmIs1JXDaot1VK5wHIxef2MTc2mpt+QechlDoOv76XSzB6VfuycnxoIwH642xp0p5SQpw508sb67UxL8blYrn83GnJMu6hjmRrHcXWBRGuzFByhTyocL3Js1amFEo8eZ8/QoMxmKu/xdaMlZsdrFWllsmTkEDKAYy3aF0molZ3grVKKDLnmwCGfJQbTdjWwA+tRfCXO+XQVDqGRyu8r2csj4jLhasIvqpIwnqhsoUZTE+mAXODuL0/2pNrFo0Ja4LBLrxTovYuq0y9iaW1tFP57YNc7E4bAzXUMD2qI8ZSRzvAiWcDlG6voiZBg3SyP7HFoHvQzM2jJ5DF/bTS9cYDlUJn6Q2vNIl2K1npHEkb3f0Lg++JpouLukId04O1GNcsaPvEN1s71hUvYldNld6G7K1trLPsfPlZXj1FnV3eIFQ3Ab3GbKs5saiu4k+2N3FO6rPLwYgsOsxaxmcL2hTmuLP5ZxoSs9sWtvenXWatJO7p4msAUrixV5WG6J6u6XSbMzUV09MeLm4mhStjhcbbPOdur+3KEH7tTO6/uZG60jgZIuSq1IWyXK46buxHzdKWcUG9GKnd/wVk+M2CDAFT1GK2pxN2WD286JWj6poWLbBnkqlirtpbudnu1P1bB2qaL09/MDL/OzbnXXiAWbUGTU9u4gjOmx0TSt9CS5UKvdzWRE7sLFelPtPJ84lDyKis7x4nCHMg8WbHM6+f5wL5wWrEpeZTWpnTnEeX2g0WG/FYtSJfJitoDzSne2+GK47y12TYYUildkqll87Ss33brKvrvYovTY6u7NI+S5HVPb460zCaLNcM6FzZANXfJWtfZaOMYFu1/zDrlutxlxuib2gp1pWahLZ9Hiz5Y+zLpRhlP4IK3X+ebONW64uTTcQfJ5bnaFg4dyKg10K2C3liN9vIWzXym4FKG3oiGlxnZhLdIziVZz/tBvuORAVq2JcddNklksfbkWBgf2TrleXkhFVDSbuwaZe0tZ09uFHs7Ze60dTb2kivnNCnYnO3D9TcqqcUuEh5EqD0frfmWZ3Dgxie2KChMttYSYzodO1LFPPeIo9w0Yks0GxL2Dsdkx8njm1p1u16g8qxp2WYjumlrTalYwtkmIhLgs+n7O3vx+d1RV3NBnsG31Bbtx4Uawr7Uz3BefMKfx7JqEuy3DmqGLjrXx0uTMm3M5kasGUCw2sxtyoVx4u63caAtTsXLgILLBgqXLEfNK3O+vtV/QtKYHy2q9UueJjlqwnyobA3dncliFlmGvtwaaXFIo/5IeseFInuBY6aORwFKmc4UN31IpSVe1E4nfQz4UVFmboVFw2q2z1s60zsyZ+82uZlxOt4DIyLu2N+HguBnpMy7eivh8VJybUvV5r5IJi6/41hdHeWUn7X0n2CgcFNI17a9FShNuzGmfbqQFYHqlveqXgZe1do8SfXfeSroWFo6O3zeGRMT7ceb3y16Xb4ac5KVuM3oA1JnFJIXI5lmQb7CM6UyYP/mF2h8Poh5TaBheTuH5Zl03xtZoebW/XfyasNQ8lu2ZxuXoPQi3p+huXFvb2uhtrhIYqe3Xdb+b01RqFFYc3pYkXpgz/JYS5Opiquej6beZX4ae3gvLg53Zgk/Q+yolfSngiJ2491GD3Qh4gzJViBpj2e12iR+FMs4XvQH0kI8NIGO3fjUc77bKH6ixEcvlQpGwLYdpoRKyZpym5szwtra/iGl2f7QiTR53OY762SFG44bb3Ly7juFCfNXQQxylTpb550QgMHdD+6k0U0FbFAtBsAwLL/ndPjQBfVvSpwYwuH/OvUBeRcudMV9vT3e5O0uexEhXMD861xldjZW3UNyW6vAm1XNny1H+MNe71bgkuMHi0/vV8i4boXOlWIW2RiwgVPFcLPTE1KtYVtr76bKQZ6xHrYPUbfi2xUIARqfN7Yq5nnjxtgsVS93jYaJZh3HOAbij2q+ccDDRoFMiUlmcwdrjNtvLIlGWOoVujwQVnLHLenmCM7rQU7W/DdihIzfSzHDbxl0d8QA3GgpjjfQ6a4Sh5Q5A6mw8nBskdcjJxWK+jCsmNLnUNLs5Np+JnURlS+xOSF1VchWuLU5nIlkeKzLK3WJ/4O6og66Dw1LeYsN9sOdHZdS5UEzvJXlFo0ZV8wN7REkmZMqrt+n17S7I7ipfAdNxLLc1mDtzZrFFJRMgKpgtuy19e1/mq0KlAqvbe95lJEsqsXeZafXGoAMT9vW0V3qr6bE5P1+ad97zhwSNh7gUCG8XCBSOYcGOmG09G0/kFKxicSaOnnel3VDewnS63KESRZbkIi1hqLtIne3Mx2a3OT0siavAmv7GmHFywwpKxpdLRhjQg9sGyVIeBHxhVU0obYoZnHxVXnEtou6kuaPQ7QWTOn7UKuLaitmCIjaLYGc3bFj18sKnt/F9bUM9NsdoiAd1SGZXvxwgIij4fb61dBGV2FBPan05E8jycknhcCdSC+moF33e5HxyhBuRCrBKJ1ALhiVX7lLyKIdc3K+LfpuFlxXOY8yx7/axvp012+tAzvn6cAwcll5v6qzpUADHGX7Fkru6Ny47+mp3x8Tkc+3Cr1VhCSCUCwc/Su7r+4KR9UilQ8ATzI3mFkHenqH+LpCa/KDBakBloWhmZ8nu/MCG43sSdlubirZzu27CA7bctLpJEVhBLIbd+UjNIlqWN3Of4S+Mx12OfTDzzN3dlEL5XpXEHA5+sskssQZVj1Ia1upYOCThci7WAiOAtaT7d9jgBC3bgM4/82tgqeQW8BG5Y3qHDa8BKvcRvfVpf8MJsIteZ+5Wm2FsQR0iOPxjW1wPzJV1K0muxfB2fWZ20mnR4DtyptAjYTCHu9Kk88A3eZqqgvgcct02ylum25oFQMU6CuLDGsPgbEPPI3xQbgbvowMDOrAcFCxSWpjNy203bg/z4y6a72fhsiGlAC+OTHgBZ3AJ4RbijCuGPwRZMBMHeV/ha0dNnRk5ViTf7efC/LhUWHmV7gKDYJaKugyLUK3cPFW3Jx/YlT/uCcyutp7SHYzt3cCvx0hfHFR2W/g43NMoWuKJfX331pughZurbVmWNE7xUtks8JoCuIrndG2Eymrd8fR2IQc2SYc66h2uZFHdUHFBKUTGJ6xQRSsgVUehvPLZAMf8i0LLdGKjYsbLdc5GTIlflns+aalUOgYHJuS35tENfAnY24CHQ2HISQXcbrnXwGTwLa7qJ9+9X6JFLvSDncx0zJ0dUwhYvFwR4iq92/HgoOU8Pa3OBxiqSNcPbnBngYuO5DZnFSK5KFt7hd5kRcDZtcTrFbUNpTvcS9wOO5XE5jghoARNyJ4fJl7VcfG5LcnlZs76h3sVmYv9kWXfPrxNh9Cvo+T/+XXwdMT3/+yk8Xko+O0l0uMQGTj+54esz/+GLn/78FZ5MdTkeX5ap234OnT8u9PTj3/6zmFaNj7fqU5vt4bm2+F644TTH/+8xbnf1k01fq2LtH0c3H54c9t6+nuE+uvrgPrtYUZWTqfd75Kmc9nHsf/Xpvj6fPP7Nv25wPTGBvix04DXZfg6R/7w5o8wDrFXfyVo6iuoysnA10uM6RR2eovx9tv/BSoc4TldJQAA -->
