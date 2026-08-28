---
name: "rar-cowork-cookbook-dashboard-deploy-software-releases"
description: "Produces a self-contained interactive HTML dashboard for deploy software releases - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_deploy_software_releases", "rar_sha256": "28d49580e7f94b537e2a80501a7216077f37fdb312bb245e3fa22a90aea07896", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_deploy_software_releases`. The original RAPP
agent is preserved byte-for-byte in `dashboard_deploy_software_releases_agent.py` and in the RCI capsule.

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

Deploy software releases Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for deploy software releases - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-deploy-software-releases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_deploy_software_releases_agent.py` and embedded as the fenced Python below (sha256 28d49580e7f94b53…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_deploy_software_releases_agent.py` first:

```bash
python3 dashboard_deploy_software_releases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_deploy_software_releases_agent.py   # or on stdin
python3 dashboard_deploy_software_releases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Deploy software releases Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for deploy software releases - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-deploy-software-releases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_deploy_software_releases',
    "version": '2.0.1',
    "display_name": 'Deploy software releases Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for deploy software releases - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-deploy-software-releases',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-deploy-software-releases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd08b3f9c0689f02b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/deploy-software-releases'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-deploy-software-releases', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardDeploySoftwareReleases(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDeploySoftwareReleases'
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
    print(DashboardDeploySoftwareReleases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8166ZOi2Lbvv8LL+6GqD1XJJFOdOBFXUQRFFBEEujqqGbYMMsmo9O3//W3UzOo+ffqe2y/eh2tFVgqsveb1W2tv8pcXt22ionr58qIDN0eWbprGEagQNw8QoeiL6gx/FWcP/iB+kTdV7LVNUdUvn14CUPtVXDZxkcPlu6oIWh/UiIvUID19HondOAcBEucNqFy/iTuASIeNggRuHXmFWwXIqaiQAJRpcUPq4tT0bgWQCqTArSGjz0hRgryG66E2N8Srir4G1SckL5A5xdCI60NxNZIDEEAp3g1pIoB0MehB9QrVA1c3K1NQv3z58adPLzH8/vLllxc/dWt462X+psP8Ll5/St8/hcP1qZuHkLC8Qf/k8LoEFVQ3g7cCcEKeVx9HWz8hf/vbGa4O6x++fM2R5+fry/hv3+Z3vZrCrRuopu+WrhencXN7RaZp795qaHDTVvndcdC9efj6WPmdU1Ei/xiffXwIeQ1B8/HrC3RO5Y7O//ryAwL9+PWlasfvryOX8uMPr2kBPfHxh+986tZLgN+MzKDWr9+e10+2kPA7aXy6S/0H5PoIswe+vvzGuPHz0Hu0E658eU2KOP/4YFxWRQdyN/fBxx/+jK0fAf+cxnXzP+L744NxBNwA2vRU/IdPdyf/hKBPg955/rnYEob1r1gCyd/EfUKejvoz3nf//xPrFJZA/e7xf8nuXy1A/4H8+Ke2/XcLPiGnry9zkMJiq1wvBV+QX77pu4Xw44fg+80PP/0KWf9bNnrRVv6dw7fMzeMTqJtv3378UN9vf/jpxw9tCXMNuNm3tkr/Fc9/5de7nN958En18fdroXwjP+dFnyPvmY78UpT/p/r1FTHdNA6+36+/IL+tl/GDIqMRb0IfLvhNzdRQ19/48YeXXyFE5NCa1r8/hlX+H/+BbGK/KkZgQnS/aBsEBriJMzAqf4hiiEz1vbYrAP1ax9CxTzqY/2OER42LE/Lzf/p3IIWQ+ABS7B0Avz3A79sb+H17A7+fX5ED5FxUcRjnborsp7vd19wNQd6MUssKQCjs7rDXgM8QiT6PX0ao/PnfM/925/Na3n6+w3z8QKi9II/oVLcpeB0tPEYgf9rjw84ArsBvoYi08KE+pxgi6ydoeV2kENab0Rv1OU5TJIgraHpR3e68oce+jMx+/vlnD+r1NX/AKYU8WkeNQYJ3dZDPn6FhpzQOo+ZrDvyoQD788usH5L+Q/27VnfkoYweR/RkPqOFK36oIrK82g2RjE4Hw6wb3ePzy69O9kE0Oex2MXnyKwWMxzM8zCN58rUvTzyTNIB6APob+zcqiaiBGI3Hzisgn5F1fKHR8NKJ4VNTN2NVAHoDcH9uSC81592ReNEgNk7A+3T4hbQ3uUn/2KveuYgYL3W1+RjbCDvaMIoX/jWreieDiIo+h+98z4XEfMqk+1MjsjcUroo4ZiZRu5ZZR5T5lnNxHXGCveFsOmbuwgfZf87E/gtFV9/J4uAcSQc/4z5B+HmMOZ4AMYkFQv8m+07hjZzvcO1z1Na+fqf9o5j5sBVBo2MbB2BD+/kypOiraNLj7D2p679yPKATPqNxzcP5ns4H8zzPFez9HvrYkTkyQ/13zyGjMdLncL5bTw2KOLNTD3n44edRrDMZjDoNzwV2Je0F9nxXekOYNcL/maQwzprr9/UF5D82T5gFibQV12E/3yJvd1Z3vPW3HNKyqMeHdr/kbsn+CjrrDGIwcrHFYA2PqvQkcn75pGkF3jdffu/w9zNB9MDFgaiJl66UwbU7QEZ7rn6FW1Vh6z8DAHAZjGfZR7Ee/swqB3GGqQP4IVCKGxQTR/+46tYBmwqo7VUX2nTweZ6fyEecAgVMreEWOsHrGDKphycIBaKSBXvhwZ4VkAPoYqvju4Tpyy4cy46D7VNAdY1FkMKl/G4Hnw+/5ftdlVB9ydQO3gb7sRwQOwPUR2Xc9n7GCymZjhd4X/T7cT1uR37agv3/N7zq+gz4s/HTs3r9xDgIzOavvSDviVg2xJwPPBIKZcG/Ur49e+2jm77p8+cN0//GvbQDu3dP4feS+IFHTlPUXDHt0vLeG9wpRA4M5Epeg/t78Pj8q7fNbpX1+q7TfcX446gvy17T7HYtnWn9BiFf8FR8fKbEPxrx9fqAzhM8z+/NkfPo134PvUX6mwoi66W0s6rcW9EYC+1BYgXAkfrSkeuxkPWyedwyGcfiav2fCs04gxOfh2D/r4jf1e+/FMK6PsL23Cvgob6DsYJzeQjBubdJR/Rq8fMnbNP30krsZ+B9tacaGALMVumPcCsHKgeNQE4P71ftoNF78fmt3rykIBkHxZSytT8g4xn5C3ifST8jbHuG+78pbuEn6cZyGR5GQFP56p33fN3rgBW7Lmls5qv7Y+IxD2HM4/qMSY0VBje8QO7atZ4mOEv/ABH4JQ1D9kcn2/sVNnzhRN+7YsuPmrbprqGcAB6BPCAwerDpYSBAfW7jgj2KgnApcWtgbg9Hc7/77blbxsOXXuxuax+7xl5c3vHjG4DkpQnJYmJ/rsTtiMFGhQHj9SCn47P9hhnxygBgHJxjIguSCCU9zOGBP/MSjKRaQLofTOOGyJMHgLHui2FPgUQTpeeSEBtTJJUmXx13g4izHM5DfIzW/jUNAPGoF8BOgeIL0A4ohaXrCEyxcEbgT1nUDnONYHHKEbeD70jMEyKepD9NGP76Ps6NLnhb/8uIxE0gpTWp5+vgIGG+6DMl6+8hDKwbYjoXJXmxcDhZQzPTcMcnFmmWJ3m/S1vBCYXvbS3ijGRF9jthjqE4pUt5ly5OjcINIr2NHODV2ITYT1b45qLfJrB095GAZX1YFL0ZGFBS3gvYINQCCay5kr9hHA9e47oo1ufOl93iGQ1c2T2dusL7QA9/UXceurGNrqlGe+UtzUZf0+eLeaOV82NDWKqYEOljX2K2du8HGdGX8uOEn7fFYmk2wZKbnSrQ6jgQBZg/DPChcU2sP9iogbyCm7HR/sLQaJDjIBgcNdnlJouC0tndWTtPdTcoUarZZntNbWV3LdFIpoG1MVwQ6t7lZnWiInbY50cu6TNaEmPfDOtMvbTBB/Whr1dEsEmIbPwZEsZZmKKhZofAMc4229s7louOyWUVR2gAhs/pGOyy36doVVPOmXUzruCKqoGrc+aFobbdktvz6cmv2XCInKKmty1ZNd7UyrGLifC3dXvMvg46GC8GfRKVeiAbekJ3jOaD1uflKIdJMG9bCrMIUyM5bW0LrVyZ5KwnX9ZKVejEOeUdnfdPIicOTDdjw1HTrngtibqn9SZLMaO4JakhK7HGpHhuwNUijq/SL760xspu5/JrYyrd6NkFFmi21sNKXW5odsoJs7M4fxC16WpkJ1klCTIcgC46UFzA4KhM+HWyUhlaVNcPtTYe0LthaCtdXyj7aWuIluji3J9gNrwSCDMOTggmcm2uZPbeWVtPuKn01BBevNnzUaM/DVRoaRrGSVZ4tFJiKTuxvSlqaNgYdiRm5k7EtaCvUqa0AmJnPZ5lJ2qhlXsvEHvayXkerjAAHk9geDPX+ExgWu+xxh+V3DTtZSNxq4LOckyWYWUc+XcXRAjtw9iQbGF7DDh256gNhwlBU1emDwqSJYjlieWycTFxr6any9jYODou2ThbE3t0nS7HWO/vUnFgKdYQGeGfdCRWJV9dGct61gcoIKdfohH8NL+vbNdDoDR43k42m3BJHPq+WsV7PVHLDrOZ7wfFkdh1v7RqvmEtpHsFygfsHlWBviT8vUKHLs2PaHwDYXpVzIgBaDpNuaRUatVqktCCq6LJkczzVROrmRPGATgcXLybHoW6wHNPaNiynzQpvMWp2NG0L25o9uCgbS4g1K9ZudrsckhuoJcldrgYtm+7DfVVpG2rwzbnJ35JWqQ/STmXXxqx0ZLe0QnumG+pSaOrrkmZ3JN9f5ie5wQTzIA+CwfiCSKoiwQzznWrpGVZ6Ck5UwOmW+MTO1L1O7jZJdQjUWA+iMIL3mUzUjT29NwK/kRiRsNSzpBebnY2iRRwHZTDIw9rc0usA3QuWK9JLGwNadVitFGdB8QteFhl3U80BQV5oflcvfBJzZhurCWGRz5rt1dwHQ7aVXOfgLGhSCERfPNMZWYfxapKojTkca4PrM7rRqPjoxxONxDCJS47sAi4fuOvW2eK7ZqUSkxNBy/l5MZWcxGFkOaOKLY4Z1mxXnMssgkU2YJyUDiiW4pikcjuvmc3FvjMw4yzKnnPlw9Q+HQXf2cTpbqur0tZw2NiiEl+t7XVva6hOm16fbiaxVg/QuRq3yfjYH9J9O0E9kRvAlTbQKGpqZkeYae3gyaQWbuJCPhlrmdJXKjYdOGHtzWKwJbWpDM7hQjeiZIp7OtExbJOsJiIINzBJLpN0H1W9appNrNl0PWykhSPEC49OrTA8GMxFqrkVP6FZFmKJXqpOM4tikoum5JZvrsytb8z5Jak5Bj1ZLElvrWp103R1UTuxp7YYHRnnVBoCpjSyAV/NuPV6nuAKh25Pc31eN+3Jtmyhn57YMMb0gXZOTsihGCop9GQpXaac0cVppTV6dyIO9nmxznr5ZtwaKV8Lt428as3b2ttmU2VQ+WFJTIQEmjvV3bmZK5yYbrxV6eari1ZW1FU0ZW2RH47dLZjmaB4p3HYS5s2CIQzPdwzpUOI571yWzYzHnUaJwKG9QN6XLkvJBYqRDkG33rwtrWitxWd76APxOsEskiuyAwFc8nxrgUJmha+6Jy3ktFmErlBHF8NjwC1dvz8Glw1rp5FNRAWvAUy1kpKbxL1nWyqpQlm7Q4vaq/XZ3frpwWvP5ppC0TXZZ+x+op2rYHJk6e01XOnXeEJtzGa+kAXNtcmg6i7XuSDx56zX+/J6qZ3jZssfOGKGGfOa3O/KA+zdi52/9TysiURGJ2czVrCMlt3PFvgJj6fzWaxk1WkX06toWkZr1L2IF/0cCsJ8Haox2vdACNgBTvipmrs3fGesr3qiR3ZYrrFqVYL1oClK5knW0p0WWZe0gwU8gmxMfGb7rV2onbD3aPt8CngiX+eRSgmTNIbzAuvzG1Fg5lhmu4fFLq4ro7u6JK/IDSMfz5ewCPeh1jLb6Lgig9t2H2/kPGgJMZ3yJope5zebSgOZQOkC5MH6cLZiK3bLTOFmU2GyBBxzFqo5u1/WpJwCzcd10m7o2IhvprIoNFTYFXvOtCewhfN4pkz8A7CwZmlk0JAh2HaYvzhiC5TZ5Rvcr8XDup/uLZUhLvJui9O5oYqmaUj8TuoqNOM3FFZWU/ucA3cqXmdYmVB4GG8lOMPhWTczGOq4q8zSv1A42jr8UYkDVQFNXvOb83aXzMIZSlUOpfv9NNsW0+Vyvm8YklrY8orbMSFqXPpBMToqNjqJhUjUu8VBsgpJnsHW2R2q9LJ0mPktDmSdiBM4ugUmagtJHlCKEZdWp5ErG/e6SBNVQBL6YHoGjQq6PwsFlSM62Fqcg3Y4VEAVzPlWL3k7NGpKNJZb1DYvftyF4jzrL46wCZStEEAMw/QDkPUg8NJtdRgKpZnMudY94A436YPkUoINqa68SUiEJlEJXbzyjEEUsBlRZp3oLSHuX339okSOsOwVobwVl3l7DmnJTOq0do+pvJb4q+ktto6QT+y+x5alaO032y17zPhtcE41JSJVxcmMan8UCUc33FZPJ5MYmx0tND1TjD9oHt4sWXsln4LZtgdot+yDIzermwt5HY47OJcerNNWvURkrue4ecSxRU0mVRmsfNOuDy294EWcZQZJDztsZui92Fl7deWvlqtDXC9WGg12/WIpbBUiWUdMkfCOrB9LpeScxZEX/HnQR4ZyyjHH3fCCMbSNOKCK1TIgW8h9YVrmRZu7KPTPWTyvj/Ec+Kt6XlRTdR5GiuZb04OjmPu0Zo5poofm5rLlZPcIaOJgphdW4UHQLVBRSzZe3ai9Mt8dtvJB0ejlYtAnqwoMi1SnI0q7OHOHJ+qsWNvngGJnXriSiTl1C6KsqHBvorO5FrIMLosHd3KeFoGQ26WpZ4eFepxl83VwIofwuOPsnqNLWBFaqAi7600hm/mlZgMr2ly0wzTBlDzb78mBwDy0NKniQjeT/dWXgy03FdgGH7rtfAq4bqG1RFHWtLYH5yT07EN5QFdLfxG3szjGGeDmRnkLZzMiW0xsaRau62Q+A/G13ka16Qq2vK+tS9o725ZA1WqxrGK6mIrGyXO7/qAl26SgeacXNzcttIyi66+BO4twNJlNSdiIBmJ58+AssgTEYrUCC1skRUvhK1ay9kuer4eOmm2xgmFcNJKdvbnQJkxFlmuCqkr5cCo0cBIh+uSNF1TTkO/LvsPiLcXsTkDaW6bHOpcgj+oLae6CcyClN5vXMVzJbUnktuYWC5JwcuRrsGDiiS0Ix5RUkrkLi8ENJFBUcpvcTpPNdtbRRtWxGV1v0xq0p+OFWtW8hy/2Br0st8ahj8Kiwxpyytva8uKdhHXd5Nwun+7UgN5Ppy0r+Ul3sTYd3I8oTFtN84uGHSPYDqQ92288lI9vlErqTWSftuya5FhtfetPejKhwnwQqZrVvIrzk4ELeBTTDEwWQ9GMKoymsbikTwbVtsAxufhogizlrwsrRmcBGUtJLGMiT6xXm27dxOTeZdh6hWnq8bAP6RRw7jS0J4qWrIZhyQtbeSd41L4Rr4cdU8PYUWmdpcchP/kD3Aw0y3R5xVWpZULCrHppShM0tnZ5Wh+Wi9u63Yu6E+W8ZFuTa6VEcS/aCjmZYxyGLTSKsgwnOhtWe9VxgboxLKt3Zw/v4EivL1UlKYRTNWi8Qy2H0N40YrxLNOtwqGnbJXd8TEgo194WJ97D2Ci5KreYQYvkOHXj24wm0YzAd4oeZDw3LEjJqhp/u5Q7O1SO5uAPR4JnlZgikzbPZzOTBRfJ91VqR+2WjHVgZ+p+KqJ06u2K3mIjEa9lzml9QalWUpkwhlHvc78+XS1mPw0nm81pfWb9a3sTlzSw1jEIyPOU2TTkEN9kINBeO1U7p2S56QSOlVdav14JSiLDkzrtzXJZTaIrEBf5brB3UnLllhtwRfEZIa+OR2bnsLZYg6O0n2brfCqfJZM933qwns/tKLyYHY9qhXVRM+186mgxWFX7ub3nM3Tikiu2U5pYoI4HMKTn7hoMG1eRihlpsfvsuMPgxDnxLEXGbkpSm2gr06RnrYeaZP3VjVlsF4EV9jkcbPnk2qvJfE9NJv4+q6Wpk1tmx7SkevUG4ij57HR7hHPTOqkSsxUxnaFN0tzyKq5SgDUrrSeUNq/zGV7vdwULhNlmyk3FFXVIr6eCskzKPmtTGsJYTSupAfMAlRI8Px8clTcHkFNR5h28ieZdQ3XeUuckmkidEjTYeLCRYmYg8sxEqbCDI89Zn8PIVOPwBIRBQrGUzTBDoHCWTV7VizUP8CsZnCol9qoFIK9BTgBsfzoleCLVFTvPmMFFs2op3/LbvBPEhTbP4yJpq7rHuOMmJJZEcg0by9paYG9yFrvB5gY+710t5C3rOplglBDLTGPNKx+EDMfqEzrtkuG4xuZbocUuyUy4rYzG5+YgGlxOW+DLGZ7G04Y4ODf6yiyCTKsItZwrxhJjSaPzcnuPKjNj3keyTdloOhCbvJZP82t/EpuDFZ1O8nbTn6bhBdfymMFnwOud897cpbNOJ4tlsHXDw1zpC08ODlKp4SVZ02DmsO1ickOja0B3ztTCsDjahXUVWWHXHgnpJh90OrhOGj4TOx+CW9WRfrVDxUKQ2dQx8gI/23VLSKY1aDLh8RP5tGtb57zbwKY0T3qJERwp5mhgLOUzo68X4YpEt+Eew3UxzeCM4p4cFraGrmUMOjmrQnNtg1bVGKnDpcxWOXvVl9Pp9B8vn17GU+jnWfJfeIk8nu39fztifJwGvr1Xuh8jAzf4cpf15a8o9dOnl8qPoUqPo9Q6bcPnseM/HaR+/vfvI8b1t8e72fEV2LV5O3hv3HD886KXGA7mdVONCqXt/TD304vX1uNfOtTfnofWL3fDsvJ+Av4mEn53gyzO4/HN6bem+PY4RQYv418jjO92QBB/vwyfB8yQwQ3GKfbrbxRDfwNVOZr7fMsxRuEVfyVefv2/XYaju9wlAAA= -->
