---
name: "rar-cat-agent-skills-power-bi-model-review"
description: "Review a Power BI or Analysis Services semantic model (TMDL, BIM/JSON, or a pasted table/measure list) for relationship, DAX, date-handling, and naming issues, with corrected DAX for anything flagged."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/power_bi_model_review", "rar_sha256": "29cae30baa09510e4c1adaf840d54147afc9476821ab7c5a1303194987097b7c", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Tim Karlsson", "tags": ["power_bi", "dax", "semantic_model", "data", "review", "fabric"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/power_bi_model_review`. The original RAPP
agent is preserved byte-for-byte in `power_bi_model_review_agent.py` and in the RCI capsule.

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

Power BI Model Review — Review a Power BI or Analysis Services semantic model (TMDL, BIM/JSON, or a pasted table/measure list) for relationship, DAX, date-handling, and naming issues, with corrected DAX for anything flagged.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#power-bi-model-review
  Upstream author: Tim Karlsson
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
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
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `power_bi_model_review_agent.py` and embedded as the fenced Python below (sha256 29cae30baa09510e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `power_bi_model_review_agent.py` first:

```bash
python3 power_bi_model_review_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 power_bi_model_review_agent.py   # or on stdin
python3 power_bi_model_review_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Power BI Model Review — Review a Power BI or Analysis Services semantic model (TMDL, BIM/JSON, or a pasted table/measure list) for relationship, DAX, date-handling, and naming issues, with corrected DAX for anything flagged.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#power-bi-model-review
  Upstream author: Tim Karlsson
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/power_bi_model_review',
    "version": '2.0.0',
    "display_name": 'Power BI Model Review',
    "description": 'Review a Power BI or Analysis Services semantic model (TMDL, BIM/JSON, or a pasted table/measure list) for relationship, DAX, date-handling, and naming issues, with corrected DAX for anything flagged.',
    "author": 'Tim Karlsson',
    "tags": ['power_bi', 'dax', 'semantic_model', 'data', 'review', 'fabric'],
    "category": 'pipeline',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'power-bi-model-review',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#power-bi-model-review',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'd7479319485ce4bf',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio', 'Cowork', 'Scout'],
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:review', 'word:review'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class PowerBiModelReview(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PowerBiModelReview'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
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
    print(PowerBiModelReview().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/91aaZPiSJL9K9qcD1U9ZCXoQEeOtdlKAiRAgNAJdLZV6T7QfUu9/d83BGRW9U737K7ZfloqLUtHhIf7c/fnHkH+9mTUlZ8WT69PShBDW6OIyjJNnp6fbKe0iiCrAnD3+iQ5TeC0kAGJaesUELOG0gKiEyPqy6CEZKdoAsspodKJjaQKLChObSeCPiu7hfAMRu+mG/mwfx4nGVBmlJVjQ5VhRs40doyyLhwoCsrqJ8gFAwonMsZVSz/InqEFfXqGbKNyvvhGYkdB4j1D4AJKjBhcQ0FZ1k75DLVB5UNWWhSONcoGs26yjKSv/HGcGxme59gvwDCnM+Iscsqn119+fX4KwPXT629PVmSU4NHTzT4m2I36340GUyIj8cC7DAi7YZM5BZAeg0e240KPu8+lE7nP0N//fm2Nwit/en1LoMfn7Wn8J9UJVPkOVKV3ACwjM8wgCqr+BaKj1uhLYHtVF0kJQCqrAuj9cp/5XVKaQT+P7z7fF3nxnOrz21MKVLhh9vb004jx21NRj9cvo5Ts808v0WjV55++yylrMwRQjcKA1i9fH/cPsWDg96GBe1v1ZyD1HhOm8/b0g3Hj5673aCeY+fQSpkHy+S44K9LGSYzEcj7/9FdiLd+xrmMA/I/k/nIX7DuGDWx6KP7T8w3kX6HJw6APmX+9bAbc+r+xBAx/X+4ZegD1V7Jv+P8X0SB4QYq8I/6n4v5swuRn6Je/tO1fTXiG3LenhRMFDYgOkGuv0G9fZXHJ/vLJ/v7w06+/A9H/rRg5rQvrJuEryPDAdcrq69dfPpW3x59+/eVTnYFYc4z4a11Efybzz3C9rfMHBB+jPv9xLlhfTa5J2ibQR6RDv6XZvxW/v0CaEQX29+flK/RjvoyfCTQa8b7oHYIfcqYEuv6A409PvwNWSIA1tXV7DbL8b3+DdoFVpGXqVpBspXUFAQdXQeyMyis+oEDwM+Z24QBcywAA+xgH4n/08Khx6kLf/t0yqi+G5yTVl/IaRFE5zcbU/GoGX2+U+bW4cc63F0gB0tIi8AJAspBEi+Jbcps3rpQVTgkoF3CI2QNmBOzzZbyAggT69qfyvt6mvmT9txt5Bnciktj1SEJlHTkvoyG67yQPtS0jgZzOsWogNUotoIIbRCPRgpXTqAEkNhp9MwGyg5F106K/yQbAvI7Cvn37Zhql/5bcWROF7uWknIIBH+pAX74AW9wo8PzqLXEsP4U+/fb7J+g/oH816yZ8XEMEnP2AHWg4lhgIpFEdg2HAI8CHgCNusP/2+wNRICYB9Qs4KXAD5z4ZhOHVsd/hlXn6CzLHIdMBsAJI4ywtqlupqV6gtQt96AsWHV+NZO2nZQXZTuYktpNYPZBqAHM+kEzSCipBrJVu/wzVpXNb9ZtZGDcVY5DPRvUN2rEiKA1pBH6Nat4GgclpEgD4P5x/fw6EFJ9KiHkX8QLtx8ADpbUwMr8wHmu4xt0vYyV8TAfCDShx2rdkrHzOCNUtC+7wgEEAGevh0i+jz0FVjUHK2+X72rcxxljAlFshK96S8hHhRjG6wgKMDxb16sAeef8fj5Aq/bSO7Bt+QNNR0sML9sMrtxj86C9uFRh69B1vNTKDMej/SxcyGkpznLTkaGW5gJZ7RTrfHWClSTU66t6VgdbgJuCWbN/bhXeyeefctyQKQDQV/T/uI29ue4y58xiwzQYkIt3kg5gB4I1ybyE9hmhRjMlgvCXv5A7Mg25MBrwK8v86IpV+LDi+fdfUB0k+3n8v9LcQKOwRIBC2UFabEfCF6zi2aVhXoFUxpuXDpSC+nTFFWz+w/D9YBQHpIIyAfAgoEYBEAwXgBt0+fcBZpPH34cHYPgEt7NoC2vpO4bxAOsisMbpKkM6gBxrHABQ+3URBsQMwBip+IFz6RnZXJi2u7woa0J1Cf8T/8ep7Jtw0GZUHMg0QJwDJdqRj2+nufv3Q8uEpIDQec/c26Y/OflgK/ViD/vGW3DT8qACAEqIxcn+ABgKpGJe3sBwZrQSsFDuP8AFxcKvUL/die6/mH7q8QiytQPSd/m5VCfocv9e7W2lU/+iTV8ivqqx8nU4/hr14IPZr8yVIp/9U4v52q0lfzODLLSG/3AH9g9w7BK/Qj5uQPwx4BOMrBL/MXmbjKwHk+hhtj88rVCcfhPL5h+uHs27OcOxnQH4jU4JQGeOy9B371oFIzndvAmXSGGT/CHIPSuxHEXofAiqRVzjeOPhelMqxlrWgfN5kA7zfkg+PP7IBkHzijSRRpj9k6a0aA//d3fNRLMCrpAJr22Ob5jnjtiUazS2dp9ekjqLnJ8A8zl9tV8YqAAIRIDbubEBKgFanCpzbHbAEvAiM8fqPW7zD7cKI7gFbVkA1o7il/SMBDO9WbZ7HPjcBlHHjYFDq7mUB7ISMOqpGVas+G3W7b2HGduqj1/rnVW8ZCtaw09cxUZ+hsS9+hj5aXEC7j03Hbe+W1GDX9cvYXo92gqHgv4+xH7tW03n69U/UeHTbf6FEMJLESCt3c79HjnF3VWZUgOhUCZQSO7VuTcZYScr+VoD/2WywYOHkNaik9qjydwy+q5be9fn9Zkp131L+9vTOIQ/nPdpHMBwk65dyrKVTkARgQXB/Dz/w7n/YWD5mAaYDPQ6YhlCW4aAz0zBm1ByeOZgFg7VdEpvZcwzGCMO1KIzASQQ2TMKaGzA6Q2EKo0hiRhHgCZB3D92vY5sQjJpYgOZxFJ65hotbiGEQKOyihD0nLdchHQpIQvHZjJx9n3oFufkw727OiN1HjzvC8LDytycTx8BIHivX9P3DTinYIC5C2DEnqsDdNGAmSCuLzTII2P18H9iJ5cUk2++VepnRxslQm8pSDv1GyCPSHNu7nMfoaH7NOqLuNaFMDOYqtp4Oi2ctcd0mmU2HEEElKeBaoyIzrMMm1w15la18Jbm5ltf25BDz/KRu1FBSrEA87LKkLkwzqJQteoguui7omm5EYamrDEaWTZKQk85pm0tCEVPnJGxlRE4zFtHW13QuZ1qJI3IVbrbZPteXBM8x272sOylZdpWt7E5DiVIHSd4ItrmV9IuQE3yak0vtCjqv5hhV5lYptQMM19KmNVNkK4eaWsoIcNdVHOA8JpvoslnRUpKgMGK5xAVxTnML5SdkIwSnOYehrFcOaq5F6kafy2e0robBynt4nRmr0yFWk3p1CqxIO6t1OF9c1pSVrUt0GmzyOZzXaRavFqvNEdeDdT2w3bmxj6Zw1Xxbqjcr1uI5g/H3TMgap6AysTgMND8WZlg5C5HpWk7igT+juhPjV9ReNG0towCIS8HRaLIgfayVsFMOyzXHVRpAjjzCMy+Vl6dLEsWSMNfrFjlU89kQ7DzE6TZVSrN1qfBCKm5ONchw1nT5wAyz5cWf4vI2dWzQiembYnD61dbcFqsg2++nEs90024tLLWSQ2SbPsPx/IopymY4IsUm4CQM7yILzSaFTuPyeR6tVD9hN7s12yXlWdyV6sk9hBiMoKF6rNcnP9EO+NCckhYpEoHO55t2VWzy6aarB2K/VVvTjhbRLisFy/LShueCKzLRlLmBiQ65Kzh2OEvYoJGm5JgBYsfRgRM3BULN4ijt0Lo4Az+4USfupnhR+GZyjjjNnxP7y66vcSmTTvksTEo40Df4EAW6dilRayuXvRIphA8vqs6Pe8E2HDeY1dTqNDltChUZqCIUm0WMJfxsy+fLqzWRZr50nlaUpTFJjAs6x5NGRUyOvp2utlmwUZwlzhyPq3Tf5xdmx60OoXfUa8mcL+yLHVC6g6zCFGvkAcSJ3Mu5alszwN9JteI6iaDzTRdxC7D1m8xZkT6iJ59eIyaiBs7ZJ+dRy2rI5XLyciE1hiWcxlzN1djWU1rGqqLkLAqZ4mlUy9kHQemYeqkMVy29rJaYR1JekizyzluxbH4IFYywWnt+LhpZbszVDPXD+cUm5ErcUGVyosQ98PtBm+jn0vYP+7hMtjqJCZNTy+JihgtamF0OMFHMtI2jY50d6ikR4pcg2nnEJA9EfDk0zDXbJIR66jiv0mYmn2LqiZk6GU4NpWFW7KrNE1XUdBR2ZIvzL8b1lPtL1guFKWEZh0lBSJKdx70Ob7KZGyTqMtgKtLmcTcV2ieU+omZGvjO6ZZNnBOafFueMx6JSJK1qucZNwez4HcvNFW4Nq/huC7NTMkmYdm3LVMnC19bZWtdY3XHn1FGWpAS7tCipuX2Y54VsqOs06tmsJwNeRKxDxLsZJg7yhXUAW2Rb5UiFZjOXZxSbJt02xLAITkSHsXQmv2hbY2KUHiCduKoSOatUuEava8GzT1PWNpupKHSmS2P8Uljwvix7fomoZ75hkHO5HfiduFdiO0dUovClLeCvgcDww24qNgTmDRTFbUtRi8uG3HIHKc/DdruUJ2YMH1vZj2jmgAkCpjGVmZRg6S3muRGZlb2rHhl0jaO+pZ2N3N/h62Llwfac2zQdIvkg2fLlRaX1pXfSDX3JDtezwSIOu5J1/dR1ZbXgawWkDpGu+MWkzls5OZcXPmSFeJ2cLA3XMFtRuNmUt7OSzOTZdUcfTWeZlLs8rRkU2OMLuCxwsrfokCwkB09S52hGqFmw6kjQ+8nxrpFyvba9I6aEKN41qUSG7fJ4XGyszqSbnXGqu8uSFWaVFR222VReq710tIllLgfpRjMKelgQ+7xv5/vWiBJZnZtdqw+b6ijvJUPYWPgM97sz3sjURaK5AgfVS7nuNu5kdpHXl5z2ZqXbnYXZcdmlk5V3rL2ysLTLchE5Zbfn7JPeaSs56M+oqMAnkqzFS8QVa0ZPG4ZGaVag1kdhaW/8q73TNW2oSldW4mG4JJMuJnZ5NCMjDOnmnXxc1oFKM5IAKiJHtI3SBJ6/AFlU7dxtJyueSRx7aR5yGk2w/rlJ5vA07bFu6RkYh8wFSkrRYM4udhtEoldD6AHqodaJRlfhSduYNLveB/LEsZDUX1CyHYIkYUGGptF2SzJxi9b07MJuzEO6WW0pm9vly6ieMwhXB0y1WBHKtTewqUony6Mvybq0RQROymEl4nzhoK8kJPWYOt1O0hRfymieBTQD5rDXhGNpionttduq2lKliv1a5soDeqDRNMo0IpkuCWI35zWqL1tQL85cj3ZaqxJeMKft5opomULJsime00kGiKq89glj9kfeonILXZpeIF+qGXWhebiw5uvLhThdLpXh2oKp2/C+xFv4rJO9HUmppPWytNev2eTEzI+X1apb25QfGnwSCENJGuaFYWJ+ORy0tBDVqxdWhBK7qcwHC7LCj4y7SxwlV0vBYSkhO3DcMNgMmaX4apBXToqSR8xsYnHKNqAbuQiHZahdBx1HJh61X28T24ubtBGLDC3rSR3TmFpelWKyV1cOMwkqO5O3AXshGHyCLo2Q6S/bkkExCinE5bEhdJCYp9netdG0LcWrH21WhOwiSuh1kn+mSnk4gvxjmmA6y05WsI6wYy2u2JRj1NIOV43mXMU1c7WvqbmbIMV8vqdzUEeXis3Mau9I25sdQ9JemojRjjOR9EzuYS83VWPwyGVtXYQlS68lJUk34lbUyFXGKCFdccwQbFZ7UON0NZbSltnXunwWN/Bx6DgUUIR00TAxvzTGmWSuF7WIq9a3pzTDqdOojVFftGftjHLlOoxpujWljVtc+CYVdvp8wLTc0I69eFpPk943JpswQpbi9pCne3fdDoWkTas68Hc1tr9yJ6U+YLt+udpxl3XDq9kw3/puW++n4VHX5+fd1i88o6iL4BKkszQv4VoztnZy1CxH8ChqAS96U21sZgg1u+0Tm534RMYwUaC5MBOde3I/KzMj5AIiceWzd0TRQZuUO3MoMHmR1UeeV/WpwGIZDcuoguHM7ojzmnre1MuY8vCG43rY8LMSoFCDoj3XzSJ3zMlAI4fF/HSKYHEWodogXSeJomuzvTSZmKwPF4PPoZv0AJJRz3X8hNtcd8xFT5FPRBOJRxwxkKXiVovGMWaouXD3qn0SpZMdFhpaCrrOkzbWn9m+8g8std2pMz0Kgy7ZY6aCddcUbkN6lmge78oUT2jINJiEloZmvATYjoO3HbXQF/vkvN0lic1byMbd7qfDeQXcX/VtLGgztjzBDs34R1xbd759mguMlJxJnacP5rxTCm9ueoMaYoLep/Zis3LOYjZfJhepPdr1nrwmXu7ORXGK0yLFIisW7OemMTHhSsbjHWM+wdADIfmVpy6lddTAGwwvTnw6xwTTV9KiZnfbkz3lUJg2MGLBU91MTyjBpmxvEw4MtdgsFSsmz0og9JeBc+zN2efRMJruwlVOG1pvd+mMb85H09hfPcZye7xx1HLOxL48rJHjrm7aAb7WRBaFp6l+dMXV0e5OmxMpTJq6bk+l7DWJTzMN2/vEhUUXitvYvMwtNl5puIERrq6u6TBtT5pCfaEsipvNYFGaHMKzVcjTISjgZqqLh9l5GXqas8Mu0XpdlK29c9tr4trxfNLP2qWoIc1CCgShAvuwrL+ExoSKOpeXktNg+DbmqHxx4OYxNXR1NHVaRfL7MykX88mKbVinhvPlkQIV9oDF+FqmgqXZ+ROjxieYTHvKtVQGaolloAcA+/LzUSHP9RXOpYFQOXqy4DwlhEs+u27YPQWILSbxIVy1i0jGbTfY4mvvZLvZnnJCELUUrzryROVXF++swIe4woWliq23nY8h1LbcBkmLr91t3k0POJ9jlZQIKDHRTp4+I2ZcQ0Z9eOIFG7aDtTMPzYmDRfqmvhT+uVof+lptqfM1jaXEh9lzMMXg1vKR5ggaAOpCIelw8taWZaDNMZ6oJH/OOKdsvP30IIu5oPX80BJN73rOZT/HCH6R0IcTixZCl5pwvSqOOJETW4baWYKnE1p8PBsRwuykzraPW4qT2jXZ5XTrVbil+k1KY4nkSUfxarqpUxr72Tq+TphkWZ/OGju1uD6LUR3nHfK4ODZVu8KQBd+jRZPp5p5sDJjcNyfNmYKGmprwCzGcu8j+OM2m5opodEM8Xf1BJ9pKvarWwG954kDwSUgXhJtS0/WskfDDpGGn/j6aC8JsuzqxfMOudsfFyd8q+mpoJxc3aOccrKyCPa/sT9Kq73p4sh+Oe2ZzYOG9u7IpktqmobpcmQdreThlnJuFNbFNVkm6Kyl3u1oP+rpZB8jOmR2EY+hNPHHwj14QRH6urUCH0mu2a8bRoFOmYTemYhs2ui40WSz38o7Imt0cvyrITvB7A9BjYJKJ0PlzjzljdOHj6kY5r8+gES16dqrFanUId4DIe4tZXMwSwQ32uie2emseSN85lO3E4TlquSAFp7n1TIS9tcSJ2Ba9qMhzW8KqMF7VJHpelw2iFiLCWwzplptgPzPkjY4e3BXftmtYoa55Ji6soWnOKk7wvHewNh7wO4F4/pbJQErQyQXPWmo6k1dwFXV4Nl0WsMvTKwu75skBu57QvIyv8pQpuynlW5tepWn655+fnp/GI7LHmeS//gZyPPb5Pzt9uh8UvX/xcDsZdAz79bbW63+jx6/PT4UVAC3uh2llVHuPQ6j/epT25U/Pr8c5/f37u/GrkK56P5qtDG/845IPHMZjSaMbhz++l7ordHtcGeOJ3Ls81zCLwBo1exx3jxiN591Pv/8nkdhQ+qkjAAA= -->
