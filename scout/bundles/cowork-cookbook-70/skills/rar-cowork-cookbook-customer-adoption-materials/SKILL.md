---
name: "rar-cowork-cookbook-customer-adoption-materials"
description: "Build a role-relevant learning curriculum for a customer - structured, sourced, and deployment-ready."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/customer_adoption_materials", "rar_sha256": "e8acc8ad32ef6f2349f4d9dfddca014ce0bf0e75b7bd70c77dd299be70b80392", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/customer_adoption_materials`. The original RAPP
agent is preserved byte-for-byte in `customer_adoption_materials_agent.py` and in the RCI capsule.

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

Customer adoption materials — Build a role-relevant learning curriculum for a customer - structured, sourced, and deployment-ready.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/customer-adoption-materials
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
      "description": "What to apply this capability to.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `customer_adoption_materials_agent.py` and embedded as the fenced Python below (sha256 e8acc8ad32ef6f23…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `customer_adoption_materials_agent.py` first:

```bash
python3 customer_adoption_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 customer_adoption_materials_agent.py   # or on stdin
python3 customer_adoption_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Customer adoption materials — Build a role-relevant learning curriculum for a customer - structured, sourced, and deployment-ready.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/customer-adoption-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/customer_adoption_materials',
    "version": '2.0.1',
    "display_name": 'Customer adoption materials',
    "description": 'Build a role-relevant learning curriculum for a customer - structured, sourced, and deployment-ready.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'advanced', 'read_only'],
    "category": 'general',
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
        "upstream_slug": 'customer-adoption-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/customer-adoption-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c4f7910726ce044d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/conduct-post-sale-follow-up'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/customer-adoption-materials', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'general', 'checks': ['The outcome is independently verifiable.', 'Assumptions are written down.', 'The result was checked against the original goal.'], 'confidence': 0.0, 'deliverable': 'A completed pass with the goal, the method, the result, and the assumptions it rests on.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'What to apply this capability to.'}, 'refined_by': 'rules', 'signals': [], 'steps': ['State the goal as an outcome someone else could verify without you.', 'List what you have and what is missing before starting.', 'Do the smallest version end to end, so unknowns surface while they are cheap.', 'Check the result against the goal as stated, not against what turned out to be convenient.', 'Record what would have to be true for this to be wrong.'], 'subject_label': 'task', 'verb': 'Run'}


class CustomerAdoptionMaterials(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CustomerAdoptionMaterials'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to apply this capability to.', 'type': 'string'}},
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
    print(CustomerAdoptionMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716aZPiSJbtX9HEfMisUWZoBUnZVmZPG6AFBAKEUGVZpvYF7RtI9eq/PxcQkVU9XT3dZmOPiEyQ5H793O3c60789mJ3bVTUL19e9r6dQ0s7TePIryE79yC+uBb1BbwVFwf8g9wib+vY6dqibl4+vXh+49Zx2cZFDqZzXZx6kA3VRep/rv3U7+28hVLfrvM4DyG3q+vY7dIug4ICiAc3mrbIwEqfoaatO7ftat/7BDVFV7vThwmA55dpMWR+3gKJtje8glX9m52Vqd+8fPnl108vMfj88uW3Fze1G3DrhX9KZb3iDmxtt34d2+mEN7XzEAwpB6BwDq5LvwZQMnDL8wPoefWx8dPgE/Rf/3W52nXY/PTlaw49X19fph+9y6E28qG2sJvW9yDXLm0nTuN2eIXY9GoPDVT7QJm8AUoCzYDyr4+ZPyQVJfTz9OzjY5HX0G8/fn0pAAR7Av315ScI2OjrS91Nn18nKeXHn17T4urXH3/6IafpnMR320kYQP367Xn9FAsG/hgaB/dVfwZSH35z/K8vf1Buej1wT3qCmS+vSRHnHx+Cy7ro/dzOXf/jT38l1o1895LGTfsvyf3lITgCbgU6PYH/9Olu5F8h+KnQu8y/XrYEbv13NAHD35b7BD0N9Vey7/b/O9FpnPvNu8X/obh/NAH+GfrlL3X7ZxM+QcHXF8FP4x5Eh5P6X6Dfvu23Iv/LB+/HzQ+//g5E/49i9vfkmiR8y+w8Dvym/fbtlw+PnPvw6y8fuhLEmm9n37o6/Ucy/5Fd7+v8yYLPUR//PBesf8wveXHNofdIh34ryv+of3+FDDuNvR/3my/QH/NlesHQpMTbog8T/CFnGoD1D3b86eV3QA75g1mmxyDL//M/oXXs1kVTBC20d4uuhYCD2zjzJ/CHKG4g8Dvldu0DuzYxMOxzHIj/ycMT4iKAvv8f986Mn90nMyJvZPbNfvIOsO+TeL6/QgcgsqjjMM7tFNLZ7fZrboeA1Kblytpv/LoHROIMrf8ZUNDn6QMU59D3fyL1213Aazl8vxNl/OAknZcmPmq61H+ddDpFfv7UwAXk7t98twOy08IFQIIYsOgnoGtTpD3gs0n/5hKnKeTFNVC2qIe7bGCjL5Ow79+/O3YTfc0fBEpAD/ZvEDDgHQ70+TPQKEjjMGq/5r4bFdCH337/AP1f6J/Nuguf1tgCFn96ACCU99oGAhnVTRUAOAe4E9DF3QO//f60KxCTgyIC/BUHsf+YDCLy4ntvRt6v2M/4bA45PjAuMGxWFnU7laS4fYWkAHrHCxadHk28HRVNO1UfP/f83B2AVBuo827JvGihBoRdEwyfoK7x76t+d2r7DjEDqW2336E1vwVVokjBfxPM+yAwuchjYP73EHjcB0LqDw3EvYl4hTZTDEKlXdtlVNvPNQL74Zepgj6nA+E2lPvXr/lUC/3JVPeEeJgHDAKWcZ8u/Tz5HJTxDGS/17ytfR9jT7XscK9p9de8eQa7XU+ucAH5g0XDLvamEvC3Z0g1UdGBkj/ZDyCdJD294D29co/Bt4oMvQUx9B7E0NcORzES+v/SOkxY2OVSF5fsQRQgcXPQzw8bTW3NZMtHJwQK+X2Zez78KO5v1PDGkF/zNAYOr4e/PUbeLfsc8wMUyHb9Lh+4FeCd5N6jbooioBSIV/tr/kbFADh05x1gI5CiIISnyHlbcHr6hjQCeThd/yjLdy/V3qQ6iCyo7JwUeD3wfc+x3QtANRnhzd4gBP0pi65R7EZ/0goC0oGngXwIgIhBLgC6vptuUwA1gTOCush+DI+nZgeg8DpgeAj0jf4rdALBPwVAAzIOdCzTGGCFD3dRUOYDGwOI7xZuIrt8gJlazSdA+xmT6R8d8Hz2I1rvUCb0QKjt2S0w5XUiTs+/PRz7DvPpKoA1m/LrPunP3n6qCv2xZPzta36H+M7VIG3Tqdr+wTYQCOWsuUfcxDoNYI7Mf8aP/4zI10dtfBTfdyxf/lt7/fHf68Dv1e74Z8d9gaK2LZsvCPKoUG8F6hXkPAJCJC795r1YfX7LyM/vGfknkQ8LfYH+PVh/EvEM5y8Q9oq+otMjNXb9KV6fL2AF/jN3/kxOT7/muv/DvWD5AgCbyDIdQHV8rxxvQ0D5CGs/nAY/KkkzFaArqHl36gQO+Jq/h8AzPwAz5+FU9priD3l7L6HAoQ9/vTM8eJS3YG1varNCf9p9pBP8xn/5kndp+ukltzP/f9h1TAwOAhQYYtqngFwBHUsb+/er9+5luvjzduqeRSD9veLLlEyfoKnT/AS9N42foLc2/r4pyjuwj/llalinJcFQ8PY+9n2v5vgvYM/UDuUE+rE3mfqkZ//61yDsskyH/8aIbTEt/XfSgLjarzpQbrwJ0A8NfyxcPFb7/Q60fWzBfnt5S+KnlZ7tFhgOsuVzMxUcBAQRWBBcP9wNnv07jdhzKiAc0A2AuT5tuy5tewTuB/MAJ0gmID3GCzzPtQHRuD7qBKhPzRzK8SjUpSjPwxnG8SnUoVGCwYG8R7x8mwpqPMHx0cAnGAx3PWKOz2Ykg1G4zXg2Sdm2h9I0hVKBBzj5x9QLoKunjg+dJgO+94STLZ6q/vbizEkwckU2Evt48Qhj2HOSdNqbCddzL5RH+HKw9zrlFLKS+6oj2Jo9cLjgta24HET+YAh7d9CiTNs3lDI/8ez2sg/WF2RHyZpb1ZaG2pIoJmmgDvAq6swx12b7ROFKz2jsKvf4tTWv0GNkNLc5sbt0/hIJxuQAD+q+O1skOtTmekCH9XGjDqPKef5CFc5N7exPtmWYGmWdREnhpCWyTDaGYYPYbOLLWLVSGfjc4pbI+qyrriJ5Wugy6ZHtqiDbbMRQODCdGwPHBgX3ajvHmYTJz/VJKZQYO60Nwq5bdbfyyMTbN5u92SvGuLyse+zS1JfCVbZRl647Y9bX1xvPuAM2HvdYtcG1TsVQkk6vp6PsrPa3bphFJ8Hdc8lSH1t/UI/XxaUal3Nxs9x75vxg4Cfm6OqUhuVp27W9TlXeaaOsYp2vrEWV60vsNov6RZ2uM6OWHMk4zOFIZIgAd9JddOKqMbCc7DSjGHy5q1n6kqEiZweLxKS5i3ozO+4GOgGvwmJicVBNDjaalevwHRpvLsQJn1t1WAtGLJs+VglzEvYk9Xxolihuh7e6rUc0iyOGMg6Jw29CWZ4RyZE8BG0SrxRXUHZYudW0U4Kcr365lBlmridmzW0Y7sbRLVUje2Y5zCXCmzmNWs7WuVLRO9TCDxdkRC5KkKGba8SjGrzllVmwaE8LR1+K0uK24gXUSiiJoHA+Hs5yoBCBvq/8xkAy/7AhJZPiMu2y6BUeDV01XiA2lVX1Rs0EQUVQMzDCDG9VF4u3F8S7JYcmxjQsG9ahxefrXpwfTxZGNoNz6yKFcXWnaYfcSHWO92jRv4VIzM2S2amy+V2ypblr6441RXr9+XyZb80iP1ZJ6uz2loIJ+A07847R1HpmxowML+3kdj6fZJok5JjcxktuTWLsgCjRLVjHgrfu1OTAirxMoKXW7VYU7pCbeXyUz9aBO5503N2TiXU1rwd2GRtybkXytaEs6hx2opWi8YxXFvG47/lbfijRmRPdNog5ct5VGUkaZva4jR1uBSKrx+DSnLckxRInmce3pLRZMU6SHfR0DBlZDRrhtCkb0ZtLO29EOIOoGwItUGeJqFZSIZbVCysrSKzVGRXXgVhth7gih7xWb1WisMdsvQ9FWMnH/TKh+j0ae2HqcdEg7+L2nBqD0yqn41LYqk3UrMdiDWduxUtIIgcRwelLgo8YaY0KYnusershC2MRlyZr7ki1rUIpYXZSS6TGnp9pEllYqDlasMKaYXUMOeaw84PjLFpjzE3C1sGALc5wtKAwm5uNKrk9ysxFzBZNjwa0VM6wan+K+yvibDsl6FY31mO9SKMjHt56ygWfH4Q4WFthkjJcFXfuwIzyURVp/VB2pn2LV4BStahf0ywFS5l0WMFG6sV4Q82YM4glZTE/HVjYbF3RO9DDoRoaTyTVLcnNiCOOBbpyMG5dPvQY66/UQL0hhDIIeKnpWp50DcVTCn/Yb1o03KRDkO3PFuCTLT5irE0a3ICrkW8aLL/T9LokVoJ0Yw/pLGhinLaEfFVmdr3W3UqdAQ7TMaKCu7SipHFvncUzO4QFJ/RStCGjdUAuRIUG3tgK9ZGpTFnmxdXC4mazcp5Fh9OI3iqxoZbiLrFj+nYkxaoKZHatme1oDviOLJdXzrLUy23NG0SwMEnHQwY8tLhqFtxSVvSdUHTGYUYis3nr1r6FYkhujgMc9Pk4YsuNWJ1H0dwhSGbs9+cgpQw78S7n3YE+7s28DWryRq9ZDe5IJoRlNd4F9QhTa3q7IkZ8vtkct6uE1tiOExNrIZjzee7DLX+9hGJ3k6pd2/YXReLj2BqCk82HLOt4y9VgDQnSmhxXjyIitrv9emyUS6MdjkmdVOF+vrdK3IoLq+BititFBTc3mcQzXOdbxmG9HZte0xrAKXSfdap/IeQiGvpxN25595gKUZ2GcoBdiM2iq1fcDTVKQ2tD2CslizxWdLk4rbTVpTIlHL3ZuoLPVmenDM9KcBAwyV2xO82yZ0nuzQUrRDehwS/jkFqXHiObNo9gCut1jHQqDmZM9LTSEdt0l6MZFzJSJSaH7QajztpFol1kZ6gNn4QaoSn4otGccFvd1Pl+ebEU0si3Z4YxdhFdLGxPmqslXPMlKuOcytknR9y1wT7g8sMAtjMYvziyx0ukh+LSGzj9RNo3qWCsMevjfOfMtEXHd5w/RMN6TuLtusrPvXIWXOSc6ba8Qhn+FAlW1V8N76qLbnZmhTDWzc35wrYZYexzobgymWIT3HWd++SaWlqLbeWcTqgtll63w9Oa0sziFrbynjHtJmFguPKWxpyOL+c9hZ5Csdh1BEYvDEnRPLuhLnV6sJuYKeaSvNQ7mVEutWpWnDGEJ7uy6eNO60osE5xDKRO62kboSafl9tzs9zqpl/I6WSemy/HVzNG5Qd3gaoCt9rhss06pbEkyX+Ih44xdgbrhKsEMyXNi2nHI5dY6EpWdK+sqWKaHER09uiMKB8Zwo+dKUnL3rt0zbCwdonniwSjKDK3QJnPYMRWh3jLE6nKjD3V53nQJVcARjGrrcI3TDtemesquFnuuQZXl3GoliTwdyYDiQGTEy3mkbC+J3+cpuUdvzCicyiOJLgTuvCR0OaQ35SIVVan0TGSPocGWUWKd5lJV8Y8VSh5vmDuPWFI62t2oR6wqu4ez7SzqK5ad9mwwH7Ze2XvXK6ZHXdV7dhnTZyOTBN9XNuQq6c677dDL5kI9Rms0zDl3tjkI6Dq7wKExWAs3Pu2XTcnHSdzV4sXSS+fYkdatGjLzcGU2M2zkiMUxON4OJxNk8U1xo3ajmV1Imd45R7S4MXaazYVUbYfWaXc6zmZ1v+Uq2+6PAirvUO9Ir3ZsvDszUQ9v5dg4DLAL+HNZXId2JbF1JyIRJS+dEHzaOJwSKxkjVkyxqw2CC8yri9r1Laf1Mx2x+VH1qpoNZCIQQqLXlEQB7UNNrLfJ6uKc0xYhD62y2W2W3kZyiuFYhIDObxFoL9ij4fTYATZ3LMq7tT3LsdVCm924kXFjrDCwK+iILawsPZeW/TAZi3nL3VxAoG6fu5y6zsbVyUHD6sTI+lm1N1rZzYksV4OCxCVmvVP8fsVtxHEQ5eMxn9sMzXSUQVk3mThR9CmxuWJFOzS+IOuuuowd4mVses5XG+1GCOEyErp+tU3FmOOXfsPXGROrRyEC0W2M6EWOroKPkkxSo6Zjk7K+OnNV589EzlifuuRAyyVHhJSkZvBint6qLeVu9ziwK4YwjJQHds7NMZohiahK4NlKoxov2AuJhc/Iw9x0UMC/ZtGawma7FoPt0i1n6qzw6yu/lFq/pXCux+ld4I+1tdoQGxK9tnPeuO7LnRiM3nW9PGJLNSJF9ITBOHE92hrYeeArPsbXhNJriMMNu+7g8TpwdjIbt+YtCe3lTRv7Hi/4slndhkXv8ujaW25niaYXqwjZjocEiYVLaSTlNUOQmIKBU1ufN69p1zC4EpRA52gQzJ2w00exOGHkCilOx3LF8ZutwaD5WhXRZc57y9nMTFX5ijc7NaEWNFsucoyLlqiRrpH4mlsU1rodRqjFzK3ZE1fMaE/YWZTGSsXYcbtgDof+0Z1xBHzJZDqyPEc3r/XCiXCk4+pwtlU6Kz1Y5hxsNvyuILrd1VtlK3EVOFRdKJFPddtLm+yrdQYYiMxrBd7SghBJ2SmeL2f2Jp9pp5b2lteZltKnNEgCGHhIQs9ZgUfamcskKe/ImRnouMfhQU6sDhIoBDbsrReW5pDtRZn5VmLDAug3Vnpv1nbkir691bxgVJCcoBULCTMp5JGN2psXXWXCjDpd/DXhy8vxkqPU8bxr9NFrEMwYnWtErne2jCL+zR9O8WK5U3BRRDT7wpJrj53B4nEl0LwnLFf5uUvkjmwJuY+DrnOvgytfa0XLywXH85LWw53fCyFqr8mkR1f6MFykueDVjRJpUqvxiqbl2zrxb+tm1cXXlWQrKAU7x5WJLU1l0WzJqrvEZUlsgn6b+YWmUQplXVo8u7oMKAgODQDOqZ2X0bBO3cQSjfttiW2TcaEWiOB5e2I4YT1BRarKRjc58SfuPZ27WXNWhoglaIbWo8YUfdPxDWzr8zFtJI6DAr+oXIv259l4trQ5szG7g7GBb86+nStCcaRyChaKKgqK0d/La4XmYi4smaOijgWqs9Z+S+8YZVFulsMmt+acu5950XGEs9nG5FzQ7bYkSHvCmVskLK9wpA6EYW47HkpQO6SrKHphSVuS1rarE+nbOqJn1GauELsNl+PzmcPAxco2+2R7E5olDedUkpU+QsxVhFYS1x/6hiI0B0dbH08U+EiB4Bf0yLDZpYOR5lX2KbkSymUi2R3s+/olpW64Bi/LYhEeS37Z9cnthrqLdaD7TEmuiqKlxyudZdIJNAJywteG3+4iY9VrrFAEeMCym53YyGR59XWhPxa8dfAcvB1OhudQvbWnfQ9DiP0+vEp7mij6uOXzvOJW+hXWhqyrdhkiazTqXtmmYwt9LsqHs0gGenpIDbhu92ucHcvhuN+dYcOx6stsfvR4ptbMzBQI3vXASHg8GGyOEP2uDpt+CLkt3SuRJThbtdRS0r8y43C9WSiddDgfNtmOEFBn1JrYiPCKLhAb9BUBIrtWh5On3fVaYo3Ghl6xQAMVS2e7c3wo47PC5sEcY4PbIp3pi0u4z7sTA8uIi2TluPD2BaHPRqoUCgfR+4JO3SbkjyzL/vzzy6eX6cjxeXD4r3zDNx0W/a+dWT2Ol96+NbgfGfq29+W+1pd/Cc2vn15qNwZYHqdxTdqFzwOsvzuL+/xPzpmnicPjq7LpK41b+3ag2trh9JcdL2APB2bXw7emSLv7QeCnF6drpq+am+mvEVzw/nJXJSun882ijfz6caMpfbf91hbfqq5ofXDP9vpJ2enUbVL2W5GndzWeh9MAPf6KvmIvv/8/FhX38g0jAAA= -->
