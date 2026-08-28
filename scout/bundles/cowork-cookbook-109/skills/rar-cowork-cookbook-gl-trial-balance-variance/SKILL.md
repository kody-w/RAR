---
name: "rar-cowork-cookbook-gl-trial-balance-variance"
description: "Compares the current-period trial balance to the prior period and highlights GL accounts with material variances."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/gl_trial_balance_variance", "rar_sha256": "5446fe5182425ee6611569eacf899a61a58d7c6280c2a8597de0e8c39131b129", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/gl_trial_balance_variance`. The original RAPP
agent is preserved byte-for-byte in `gl_trial_balance_variance_agent.py` and in the RCI capsule.

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

GL Trial Balance Variance Report — Compares the current-period trial balance to the prior period and highlights GL accounts with material variances.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/gl-trial-balance-variance
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
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
      "type": "string"
    },
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `gl_trial_balance_variance_agent.py` and embedded as the fenced Python below (sha256 5446fe5182425ee6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `gl_trial_balance_variance_agent.py` first:

```bash
python3 gl_trial_balance_variance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 gl_trial_balance_variance_agent.py   # or on stdin
python3 gl_trial_balance_variance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
GL Trial Balance Variance Report — Compares the current-period trial balance to the prior period and highlights GL accounts with material variances.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/gl-trial-balance-variance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/gl_trial_balance_variance',
    "version": '2.0.1',
    "display_name": 'GL Trial Balance Variance Report',
    "description": 'Compares the current-period trial balance to the prior period and highlights GL accounts with material variances.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'gl-trial-balance-variance',
        "upstream_url": 'https://coworkcookbook.com/recipes/gl-trial-balance-variance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9b20b898873061ce',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/gl-trial-balance-variance', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Email'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.333, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class GlTrialBalanceVariance(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'GlTrialBalanceVariance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(GlTrialBalanceVariance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716a5OjSJLtX+HmfqjuIStBvKmxMbsSAoRAIImHBF1t1bxBIN5Igt7+7xtIyqzu3e7ZGbNrV2VlAhHh4X7c/bhHkL++uH2XlM3Llxc9dAtIdPM8TcIGcosA4spr2WTgq8w88B/yy6JrUq/vyqZ9eX0JwtZv0qpLywJM58pz5TZhC3VJCPl904RF97kKm7QMIDDLzSHPzd3CD6GuvI+pwKMGeo6YlkvSOMnB/66FRAVyfb/sC3B9TbsEOrtdeBdyccEXkNK+AQ3Cm3uu8rB9+fLTz68vKbh++fLri5+7LfjpRcyNacrisaz1nAimgfsYPK8GYHkB7oEOUdmcwU9BGEHPux/aMI9eob/9Lbu6Tdz++OVrAT0/X1+mf/u+uNvRlW7bhQHku5XrpXnaDW/QPL+6Qws1Ydc3RQu5UAsgKOK3x8zvksoK+sf07IfHIm9x2P3w9aUEKrgTrF9ffoQARl9fmn66fpukVD/8+JaX17D54cfvctreO4V+NwkDWr99e94/xYKB34em0X3VfwCpDwd64deX3xk3fR56T3aCmS9vpzItfngIrpryEhYTjj/8+Fdi/ST0szxtu39J7k8PwUnoBsCmp+I/vt5B/hmCnwZ9yPzrZSvg1n/HEjD8fblX6AnUX8m+4//fROdpAaL9HfE/FfdnE+B/QD/9pW3/bMIrFH19WYZ5egHR4eXhF+jXb/qW5376FHz/8dPPvwHR/6sYvewb/y7h29kt0ihsu2/ffvrU3n/+9PNPn/oKxFronr/1Tf5nMv8M1/s6f0DwOeqHP84F65tFVpTXAvqIdOjXsvo/zW9vkOXmafD99/YL9Pt8mT4wNBnxvugDgt/lTAt0/R2OP778BpihANb0/v0xyPL/+A9ok/pN2ZZRB+mAZjoIOLhLz+GkvJGkLZQ+eKwJAa5tCoB9jgPxP3l40riMoF/+r3+nyM/+kyKROP92J7tvT7L79s5Xv7xBBhBYNmmcFoDH9vPt9mvhxoAlp8UqwJxhcwE04g1d+BkQ0OfpAkoL6Je/lPntPv2tGn6582f64KM9J01c1PZ5+DbZc0jC4qm9Dxg+vIV+DyTnpQ/UiFJAn6/AzrbML4DLJtvbLM1zKEgbYGjZDHfZAJ8vk7BffvnFc9vka/EgTxx6lIAWAQM+1IE+fwb2RHcu/1qEflJCn3797RP0n9A/m3UXPq2xBfT9RB9ouNY1FQLZ1J/DqRpMrgRUcUf/19+eqAIxBahZwFdplD5LEIjGLAzeIdZX888YSUFeCKAFsJ6rsukAI0Np9wZJEfShL1h0ejRxdlK2HRSEVVgEYeEPQKoLzPlAsig7qAUh10bDK9S34X3VX7zGvat4Bmntdr9AG24LKkSZT1WveVYMMLksUgD/RwA8fgdCmk8ttHgX8QapU/xBoK66VdK4zzUi9+EXUBnepwPhLlSE16/FVATDCap7MjzgAYMAMv7TpZ8nn4NafgaZH7Tva9/HuFMdM+71rPlatM9AB1UdoOID4geLxn0aTLH392dItUnZ58EdP6DpJOnpheDplXsMgnp+r8XQsxhD79UY2t/hhr72GDojoP/vTcSk3FwU97w4N/glxKvG3n6ANjU7E7iP/ghUdQhEziNBvlf6d554p8uvRZ6CCGiGvz9G3qF+jnlQUN8AZPbz/V0+8DMAbZJ7D8MprJpmCmD3a/HOy6/As3cSAp4AOQtierL9fcHp6bumCUjM6f57jb67rbkDA0INqnovB2EQhWHguX4GtGqmVHpiD2IynNLqmqR+8gerICAduB7Ih4ASKYATcPcdOrUEZoIsipry/H14OnU+QIug94G2oJsM36ADyIYpIlqQgqB9mcYAFD7dRUHnEGAMVPxAuE3c6qHM1IA+FXSfvvg9/s9H36P3rsmkPJDpBm4HkLxONBqEt4dfP7R8egqoep7y7T7pj85+Wgr9vnz8/Wtx1/CDuUEa51Pl/R00EAizc3sPx4mFWsAk5/AZPiAO7kX27VEnH4X4Q5cv/6Pn/uHfa8vvlc/8o9++QEnXVe0XBHlUq/di9QY4AAERklZhCwrX53uCfX4m2Of3HPmDwAc+X6B/T6k/iHjG8hdo9oa+odMjJfXDKVifH4AB93lhfyamp1+LffjduWD5EiTxRJ35ACrlRx15HwKKSdyE8TT4UVfaqRxdQQW8EymA/2vxEQDP5AA8XcRTEWzL3yXtvaACdz689cH34FHRgbWDqeGKw2kTkk/qt+HLl6LP89eXwj2H/2zzMZE5iE2AwrRXAVkCyKtLw/ud2wfpBMV0/cfdlXa/cPMpkcqpME7M/UGbd7WDBug0ZV6cTvz9CgFVY8B6kyXXKfum6u8By9oW1NJgUr0bqknXx+ZkapQ+uqj/qcE9gQHzBOWXKY9foanjfYU+mtdX6H07cd+ZFT3YT/00Nc6TzWAo+PoY+7F59MKXn/9EjWcf/ddKPMnl9W6c602FaDLxT2wC0pqw7kHlCyZ9vhv4fd3ysdhvdz27x07w15d3/nh66dn1geEgUT+3U+1DQASDBcH9I9bAs3+9H3xOBEQH2hIwkyQIKgrJGYMRGBmGFDWbkRQbun7EsKxLzVySCWifwhjUx1yGZOkgREPGx9kZPvNmGAvkPUL121TZ00mZEI1C8BzzA5zCSJJgZzTmsoFL0K4boAxDo3QUgFrwfWoGePJp4cOiCb6P1vQeoQ9Df33xKAKMXBGtNH98OIS1XPqoeLfkyI5UZJcnVlrruwxDMRcVzKJNZbrIMv8E787ZjCeo+drOkn4xl67CWuHdMdwlTLkns4qkA0RY6xnt6ocobfcbGVNm9JZh2GAotgzqXi6JcuFS1GBM6bwpMRMWvHSPVNfmIrfyxrxsEbQ1GlVV4i7fK/lBqmt5Vx9zRQiF8bzeMz29o3ViPFbbk6WvfK4qRLueHamrgeipei3LIW345gab7tGlxX11kJIZTJYEwYpr4JbCgVmtyHG2NokQ2fbIqosusja2tMFj5vpAGoBZlMzSyZvRNOY+8295vVCpqsZS60DLu7ZQZVVIJPvS+XR3rfeqpTAiJ6d1s2uPKaLp/s3sg7pUBKqTjg3aSkpcqhhsldJMYy3Z9bn03FsHAc1BnKUUdRVx73hjV96hhWeqeKE0HR5c8jAk19Jydibt2EZhOadS5wYrzTbO0eQLXTo5JHY+yBXf3fyZu4f7cLuT9XTA10K+mF8J3DEAcBc/j490qQ+D4nUSaIRd4RrlNwFdaR3XHxSadQeBP1hiItZrpU9UY4GMksLvWxFn3OTWCIWCi7UuWGF7LgyYRmq/qBnzKAXxLbcFNCk4h7spmlcvRla18aAk1K4mUX4pLPe3S8xK26bZbHsMuxIrY4w2ujvsj+RZ1KL1cs0fhA7hNMO8Fct+bdTs5iwHnmMoQrtja6KSroeAO26Xq33Fg/hC1a2PDfVtidy0PUBDZ64J7+JnbX0dTJPO5JXlZBYZzweEPW9nwtAOo4QzzHaZLgPRq5jIcbolKW213Mj9tbHpKydrKisPltaMnJ2skQk6k8qqa2i0RwO5npBrcrl08r5sbmiELREqHAWW1hBCO5ZHxUxuAe/I+cFoaD/F56UhGOWl9BKPb09Wnc+bQ3K7OtIQeaQIh9JsOYTYad0PPSfLM0OIZGMhbo0zpmv7vSAOO15FsdFMUkbPWn916KXDIBCrftEI8/3M2rkLbeHg0qhwG5Z3ufCoJlYkbdfwTSvDK7a+uCxV+LJyDSKMX27q9hSnMb+SjvO9LpbluMA0EkfcrWqE28UaMcbDOkMytY7z6Joczzguw91qjSjMyXOx1ajfdMKLcqvBkJzrl7gTnKzVWZBFZpkNpnU2DmFaCLboc/VmJ8452XfD0t2e6SEziOPIrbD0Mj/JiphGlLOXD77pDp2PNOTiahQ6k/jdzJHWRYETes1JkULeRD5wL+15rajFEVMXNdIMu8SaLerb0T61RV1Z1oAorEHr6caMzfoyeGuBpwV/7hc6x2OLougiUyKCpFPKgXNhkvTgg3frfJU5Ivhalex45jc0I5BSMFhMHC/0aNUuPHUcCyLjK03kvYGXO3Zd2ahll0Z1UrNttBfMvVJYqWO7B+O8mt+S4pDTTL2UrxcZw+UbFyxMhaQQeShnXoA4rC2eLVhdDPYNn7HmbLNJva3eN1ItCidmcQpm265g5tnMbrCtnTohHrCwMt/aFyHs9zPJFpadkpXS0cZn+xJrQpZYBZHSwSdSXKDmVbZOp/B0vJoSmjDVCNaMRaZfoZYyEsd+vlO6a5mOuXIpaHY8h5xJB47XHkaFxzAf3h1dYSGe1+r5trNnzAGOowDDD/a19bxiqfMlQop6EMhO1aGo0l30xImXsWijZVxz7bxeyUyK3wSt6+wjPzfjMnNvZbHka8D51l7Ew7Qr5Z3c70txt7SGfmUSh+xyLoMkKw8rR7skFsVuR5b0C9Uk7HHf4hGJm1kuygd4VNVLq6upYRwM1PbwEGH5eQMTdBziy/nhKJHwyigRbhxHhKZlZHs6kSx61j0M3s2GTUl7aKdx7nyP8EnOYbNwaHflNdPZo1aXett0oUIopZTzLSgaSrk4zDa9VhQEpSFVxl52ThMk5npn4tK8pexCM4vQy9XwpM2VcpznmEJejW7nCHm1zw2Znl/VtB/P5nbcH3xHtQe2vtLBnJmf9JKqW+6WubWeR+m4dDJyJ423aqa1CasoPplfT57TVdzJPZJB04vOyOjq7NQTwmpcWxrfKbSXXBNRzc/jerY4iQI6aK6Pm3ZdRlahKwh/zkeajta9t5nFK0Ym5/awQQ8L2cv0jAnV/lLB8h7dl+ZlwTIp73BocsN1Os2T2E6UNq1ZsMMRYHwjK429tPN6uxXpdbfU4wxbNFJx7BsuVzYSdbBIFulkwbpwCXfeVQcytW0r4S7XvvJK3D3TnhjRIS/Y2dBYXMet1X5HLsjYRm/a9lhKStqZSZabTrO+IuvCXS3JZbnY09eyniUF0SzOihSl84tesLLTp8XawBmU0uFYSh0FBBmhdxiVNhpqily5jvQdYRGiE5vKxZNtUioV2MldOmn3AmiVIlC9bhJSuSi7bg+7mi/VlVVnSUseCVTMVmWx9Qfv1FC4zJu7M0uIBbs4oXQ5mHGCRms9kvC1kos2YlEctbGKvb0iY+7o7JSdR8Y4ehPLKs64QqxupJ3rw15a7traV60FjLpwtlUioVrsYgw5ILhjb283GOfVW+OQXDYS8xmHx5QS34pd3+3N0CHLGz4gMBOttTHsNzOaF1U+8VrYpzKbWvPBxahmWNIJ15SaRUfxeAsKZwSFe9PwlMDAOCjm5bXR16udXITdSmOlzSBwyRwT5YSEl5Z8AJ3M8iYUvOcmY3Q+EZrSYXqhrs+qE68R6yruHPVmNtloK0kxrjPzpPpjbwEELb4ZMiaR7WWq255Cn8teDvvc2+ULfjXbdSu5tVfZFvdnwoZLQQ56VKVyCpFqsuYkgGKuPmj8JNfMNFe2BA7n+JJP2zkTzy1jH/Ubd0jNSrfPxtb2YR8Ot+42LG+Si4qxdTjmnCqEngpg4OgzKtZaVohYiy0MfRGWZkxXQ2sZgupoSm2gBK0naZOf1orgz8rQ783aPLCY4fbL3SLZctJ1qR5q7mpfCd5L4bnuaiK6wpGlRCYbaiVlJSZr1DHVFNlPqKVaOSthLVjq3PLKVKcWYYyiCezPTEo5tGVdcKsbv+FbBlfiVBxuXWFlCZquPDrRxnKPzK1DsS61W6Oncz8vZ8FuXNfr5lRcVEErs649Ksihm6OE09OiGpXjfimdfbgHQZnItQTqyO24Ek8yi+7GhDNrtjtSR/l4xqrD7aSu89kO064WV0i060gWY27bE7eWY5hHLS5R5iK2qGL9vGa17uJUurSQ4VBBsxlL7ApF4lyVi4txdEs1KAVDqCoryEYQrEjtaCeU5EAlqR3vxrmtgO0SCThUXQloLA4HbIaQ0shv7ItMjp2UnwwzmWdmZV8ksqJ3u9LeJOdgBB2OCfbMqusdOCSdo4AOVWNXegVXtk1WgYlB1lkS2sWE3GKOXCekBqpDdK7rFQfLM2XdVktP1JdEvgtDNPH1akZktFGjV5oxHbsIFaoQ8nWdnXqktOR1Ozsyp53EpmDvlKTucHGdw3Uu17CNNzaJwkaPKdLKPl0O5UGtbcXzLnxDoO02CIP9cVVpGOcVGlGcw/RqssXSZq+FjdSquSmJDUZEWj6yxHl2zl3ctmd4jYA+ar+b05em8yKqruO9FmJgSzHSgQyflEt7ERgtuDh9dPU9rYd5eHGaC8ulzM49kjQQTPAaYljWJo5b2GI3lxgd7xDU3i56fFWQKqMIfSu6wK3SjFmSlw6tFX4cewd1DSzX2wUiEmmUJk0Mehy5ZmYX95rTglgnMCrMVqUxbPfKhUWNBa4jQiRFpibObbqlNXh0cnkYotU2ZRElcjATKWKSP3U0wiCLLRzXaKYdLQSGNxFxhgsMxNpKPLB9u4pto7IMdLzqIA5FE2W6m2eucNBBgRLpDL6FxDt9VWTLc9F2GVHu5qjoHTQezjMmZsollWp+AC+MbbRSdhjlHoM+YNaMLuzibk0Hlz0h8ttbZ2/wlugrPF9ppnMy2wGWDocDgEc31Out867+deull9QzmABmCS9XGhbwpkIRe8Ibu0vf73pKJHRhS8wOi7yQN+gxjFgYXQh1uunIeIubR+VUsgJPqcHIrkitxk361kYuYV98utkV/nzk+SMMen0cb1e7AHfYG4rySoSV9JE/oHsPE6zgzGPtkfQPvQljlAZCAK+T0ynHnY4JQ+Ykaox+Whgw3veev1sRF6XSI36lj6mk8kffpHn7YszZJpqhc3MRsu51u8Iv6dimJU/168ZN/MrWOM1LXHitx8esLnmUofbxRkdSZRX264QZnYVPsMoBry76kSLMXYDM5sHKmLHUpYcRc1GuDtX5pmKLLCEVIkT3TrHeEe5BW6XXa0Qtl3YV180KxkutOW+oXe1dsDy4KXttw0Z0kJDtQqN1mt8F5Gr02V218S76YRgoPcgZkl4sU6KUqMAqxJ5q4o3V9yVNbZuiofcdXu/QZOz3VLtZ7o/NlRaXSSNuFpGBo6JIRqEbtYIqIQgzOCntxirpjYsuy+jesD2tVdsjfDyoITo7qLCy5LVAv8FiyXRhefIvLLUnl+Yy1I7oyWARtUvs05yKQ2TPjIVJuNLOX5VXxhxqqjl2mnWhtjZb7mhyruo9gmuL0rt4WofkxuzSFQfEOuboEcGsbn/KEvoCY2pGzdThRA84AV9rWIQbpIoDxPLG9eaI7JP9eatHjksts+0+wogQQU7eDSd2eBFJ4sDkOL2MuVOsHjZyGwtb19w3SuX59O3Sjm4V3MRTeW5QZ7itaPNyS9xFKa3TQ0URbRR5hsEvV5wUbB0FufSLDNZFOpuNKSY2REOsSvR8mVV83iNDPKdWXXGdIwqcL1aUju8XBV0sSp3y6ijvjYFuoqDuj6dT369pZ7fcJcoYJrAuYMGh5IPVkrZliq64Pax3JEPOFy6xG1MKXeo2Yvt7KzpboAWuxIBzLoayvkYXN+hx/eJIocPNaO945olhYBW2b26JR/RIuJ2vI6G8Ka2CIJuETbIBPzCYdCBv4SZ0tllwpDMhG3iiyv2qNHujDaUebNzNWFiw8m0TdAyiRtKcxI9erPEcjQk9ipSSLqEovp4bLSu3t3ThO3WwiX1+dcLHwd6uFrkPL49BMEpb2rYCY0ktMQRBryYhz+fzl9eX6ZT4edb7v7+gnY7Y/p+d9D0O5d7f8dxPWUM3+HJf68u/oMvPry+NnwJNHueXbd7Hz0O//3Z6+fkvXwpM04bHW87p5dOtez/97tx4+mucl7QI+rZrhm9tmff3g9PXF69vp78QaKc/IvHB98vdjHM1HQc/3rreL6ZD+W9d+e3jp7SY3qeEQep24fM2fh7ivr4EA3BC6rffcIr8FjbVZN3zFQMwCntD32Yvv/0XA+jIauYkAAA= -->
