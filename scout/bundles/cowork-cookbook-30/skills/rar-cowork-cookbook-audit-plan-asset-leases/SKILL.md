---
name: "rar-cowork-cookbook-audit-plan-asset-leases"
description: "Audits plan asset leases records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_asset_leases", "rar_sha256": "4f430a7d962a075d93604ed97bbe649eb12413e0ec015944225e028b0b610914", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_plan_asset_leases_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-plan-asset-leases:79cca98ad4e47529d39b412c6d053a712c415ae5c184a64c888dffa66d0c0731", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_plan_asset_leases`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_plan_asset_leases_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

Plan asset leases Completeness Audit — Audits plan asset leases records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-asset-leases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_plan_asset_leases_agent.py` and embedded as the fenced Python below (sha256 4f430a7d962a075d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_plan_asset_leases_agent.py` first:

```bash
python3 audit_plan_asset_leases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_plan_asset_leases_agent.py   # or on stdin
python3 audit_plan_asset_leases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan asset leases Completeness Audit — Audits plan asset leases records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-asset-leases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_plan_asset_leases',
    "version": '2.0.0',
    "display_name": 'Plan asset leases Completeness Audit',
    "description": 'Audits plan asset leases records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-plan-asset-leases',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-plan-asset-leases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1886312d97607e39',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/plan-asset-leases'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/audit-plan-asset-leases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditPlanAssetLeases(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPlanAssetLeases'
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
    print(AuditPlanAssetLeases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/7V6eZPixpbvV2Fq/rA9VJf2rW444gmBEAghEEgguR3dWlIL2neEn7/7S0FVdXtsz703Yh4dXUjKzLOf3zmZ4rcnu23CvHp6fToAO5ss7SSJQlBN7MybCHmfVzH8ymMH/p+4edZUkdM2eVU/PT95oHarqGiiPIPL+daLmnpSJJCKXdegmSTArkE9qYCbV1498fMKUkiLBDQgA3V9Z1HkSeQOj+eRnblgYgd2lNXNpGoT8MmBFLyJGwI3rl8gS3C1RwL10+svvz4/RfD66fW3JzeBDN9F2EEB+JH/5s4eLoIPAjhaDFDRDN4XoIKypPCRB/zJ292PNUj858l//Vfc21VQ//T6OZu8fT4/jf+0Nps0IZg0uV03o1B2YTtREjXDy4RPensYNW3aKoOKTWpopyx4eaz8RikvJj+PYz8+mLwEoPnx81MORbBHK35++mkCjfT5qWrH65eRSvHjTy9J3oPqx5++0alb5wLcZiQGpX758nb/RhZO/DY18u9cf4ZUH/5ywOen75QbPw+5Rz3hyqeXSx5lPz4IF1XegWz0y48//R3Zu3eSqG7+Jbq/PAiHwPagTm+C//R8N/Kvk+mbQh80/57tGGj/jiZw+ju758mbof6O9t3+/410EsGg/bD4X5L7qwXTnye//K1u/9OC54n/+WkOkqiD0eEk4HXy25fDbiH88oP37eEPv/4OSf9TMoe8rdw7hS+pnUU+qJsvX375ob4//uHXX35oCxhrwE6/tFXyVzT/yq53Pn+w4NusH/+4FvLXszjL+2zyEemT3/LiP6rfXyaGnUTet+f16+T7fBk/08moxDvThwm+y5kayvqdHX96+h3iAsSPqnXvwzDL//M/J0rkVnmd+83k4ObtCC5ZE6VgFP4YRvXk+JbUXw/yarN5Sb2vE/h0THcIEXabNJNlZUfJBObD6PFRg9yffP0/7h0hP7lvCInYIwLdg+PLHQO/PDDw68vkGEJueRUFUWYnE43f7SDSgawZ+TzwrU0/dSMrKEb0gBpNWI0wU0Mk/Mfk69/Q/nIn81IMo8ifM+gDiJ+QRgPSIq/sKkoGiMcQk5yhAZ8ggELcqPIkcWw3nox/2uJltMMpBNmbdVwI4eAK3LYBkyR3obx+BEH3GTq4zpMOYuBoszqOkmTiRRDfYUEY7nAO7fo6Evv69SuE7vBz9gBdYvKoFDUCJ3wIPPn0qaiAn0RB2HzOgBvmkx9++/2Hyf+d/E+r7sRHHjtohbuZYOAmk/VB3U5gFrYpnFZPxhCAEHP30m+/P+w/SpfB0gZzJ/IjcF8MqX1z+ajBwynvHoE6jyKC6o3TH+026UNol0nUQGvBfK6fP2cjiRxOrfqoBu9GfCx+mP7dxQ8+o0/qNxtCP/lVnt7n3qNtdOZYOl8mK3/yYSmoLvRrM3o0zGGd9EABMg9ksIo2od18c2GWN5Ma5kjtD8+TtoaqjpS/OtW9voIUApHdfJ0owg7WtDyBf0YD3dnD1XkWjY5/i9HHY0ik+gHG2OydxMtkC6A1J4Vd2UVYwXC8z/PtR0TAWva+HhK3JxnoJ2PNBqOP7tl7j7zdn1oG4fs24V7VJ59bHMXIyf//LmOUiF8utcWSPy7mk8X2qJmP8Bnbn1GbR8cEC/+d2T0XvjUD77jxjqifsySCJq+Gfzxm+veIecx5oFRbQeYar93pj7lb3elGDfT76MiqGmPV/py9Q/czNCW0ej2iEEzPeEz2/IPhOPouaQhzcLz/Vsbf7DRaBQbrpGgdaJmJD4B3j+smrMaseTM2DAIwZhAMczf8g1YTSB06GNKfQCFGj0B4v5tuC6Mftj6PUP6YHo0OglJ4rQulhekBXianMVphxNUTB8AOZ5wDrfDDndQkBdDGUMQPC9ehXTyEGVvSNwFtSLWLYFR9Z/+3IRh3Y4WA3D6SCtK0PbuBluyhC2DOXB9+/ZDyzVOQaDpGx33RH539punk+wrzjzGxoITf4Bz20GNx/s40EI2r9BGLsGzGNUzdFLyFD4yDex1+eZTSR63+kOX1T134j/9eo34vjvof/fY6CZumqF8R5FHA3uvXC8wQBEZIVID6Ucs+jZn26Z5pnx6Z9gdyD+u8Tv49kf5A4i2SXyfYC/qCjkObyAVjqL59oAWETzPzEzmOfs408M21kH2eQiAZLT5AMP0oGO9TYNUIKhCMkx8FpB7rTg9L3R237gXgw/1vqQFhMQvGalfn36XsqNPozIevPvAVDmUjcntjRxaAcY+SjOLX4Ok1a5Pk+SmzU/D3e5MROWFcQhuMGxmYIbCvaSJwv4O6wIHIHq//uNdS7xd28ojfuoHC2dUdBd7y4Q3ensemNoMIMm4gxvKQfd/TjMI2QzFK99ivjL3TR2P1Z673hIU8vPx1zNvnOwo/Tz762efJ+w7jvlXLWrjF+mXspUc94VT49TH3Y/vogKdf/0KMt9b6b4SIRswYUeahLvC+AcLdWYXdQNzTtQ0UKXfvLcFYjOrhXrT+rDZkWIGyhWXYG0X+ZoNvouUPeX6/q9I89o+/Pb1Dynj96AkeYQYX/LN2bbTGe5n9MtKzx1X3pupunLuLvtgwGsZy+t1QMPYGXx7B+vQKYQg8P8HFY6Qk0e2+N356CAGl/9awQgoQUD7VY3uAwFyDlGDRLkbJYwiG3zEYH0feff548frXXe6fkeGV4VzX5ljbIwHJUDjnEZxDYrhLeyhF2Ay8IjHKBpSLsaRNky7Lsp7v2zQcd1GGwCDvGkZIar/xRrDR3lDqD6P+qw3302MZLBo4RcN1pE8SqM14HI3bKEN5HEGjJPA4xnEATXLAwXASIwAKXBSjOJLEcQqgOOugDo2hHEaO9N56v4csX9777HcPPHDhCwTQNBolxW3bZV0GIyETm3YBgTqECzAc8xjIh+IIn2UBFOHpY+mbF0YnPdQdwxK2fbDp6kY+v715dQw1moQzJbJe8Y+PgHCGTVMbR5s5U4b2c/HIsjxjuuYmplSsUcJo6ZTh7BAzvL51wsUJL3cptUjQA5aQBW7LIS2sp9qau7RZixtrLjr0m/k02Od4w1wormqm1CAu9IvFZHU4P5yS0+a8SKtqHlRb7NTaiZ7brFHE08RGdtVtM6WPoncGfrk7oKl2qhb5BW0p63Q6RHKmek6D3TZmowvnOPFOYmVahXu0QBCvErTy1tWS5JYFyfpnqkd2GUYhuU76iDOQVWN2Yl9JAsXXmj2UcDOM+qdTRVdnPC90I5MLlyiXzk3Ht9SpuViyo9v0WSuqZs941+KsGE06m8ecve1d9FxcPUWK+qLHNUwy62y7D5x8WLrSEotzw5exUAmvhyapBHITW36x1Zmzda69am9OMU5u6TNE/wSUprz0LnFwWd2uXZII8klIjc3JoOcWxa9OSiLip1DbxIct3npV1g2CyOMnetX0/MzKq77IN+tsDfZVVR/lZN15VoylvY9ZMbnZNcdVKTbTdn1KuXopF2wnL7l4ziqaclj2Z88qt6f6bDYy661tm7a2+1SumANNg9LNEmSGL5xTu7Ks1ZqaHZf2kJSKQ29uK2zZZFfKZJxrvifWfMeu06nrYGxwGcQLf0pw0r1Q8RXEJmNxWdwmt3l1DKeRkToXSUDOV0c3aEK+dBufZ1LjogcnT/CXwo6xlZsqoRs1tE4G2bEOS4JSCiiSu4amg6fquheozKGXxjFhTRBMTcLXu+3VKVv51vo3YzVNd8VNOa3DWYbsE2d1O+gLrLAimH/X7Vm/YuUxE2/KuTPpcNOfu+a86f0dGfimeiqOoUEVPrtDC24rESiBHOuTdvVKC5u55xMVV3p2PDGSKxS1ffYMHEZfzLaVXAqdnW1mniNeG9K5mtfyFHOiWHkzVqCN/GSwhWquMNVar0hrsc1WRYTLSmGfhN7Y2oy6VUKvP+/hzqHV18IijdGDG21rTdBEK1fCpZYp2tJIDB23slmeXiKj7qiFFXr+QCmsi+LKzloJC2e9HObXbRIwCkcxnqTN0RAhz2m6cak6RudE088KgJnU8VzS/o1Gw7z1FG7pdezU67vEPiep24X9pZrVpld0ppJyq0snLi5rsMVcDfCttmYtANFHTcs2PXqzig+RQ6aFrYEtDeEQDU1eAjpXZ0ZqmkQIuLM7X+9UrhHQY4kNpuv71B5mJHrOSl2f0pxcD6dQTT07ybhyvRQNPe3EIN76Ke3wMTOfyUtHWpcFqTmr5hRtDaGdGYUSzLn5jc5m12pWESUmJQy1AdMVRRP6bLqRiB4E0qzndrkE5gFLJPslsTNuycbv9iRpTjds1gSLZrYIOoeCMKLKS9o6NkKzPlAkk9aNSGmJYC4dvDSv7FFaUAFRn1YuucCtncQWp0y3Nn7KRS7tklV5dRPSx7geMaVM2l6sdN3jXbDQWhIIfig7W8xDmZA2d9IlZQzAzc79Tm/xoN/VnqjOtqq7LDwrX+2lIshOlzw50jHX9+sFacZ7kpg7gRAs8108O+8cMfT70FFuLAiYQK9JZ6sMZo9QdJ1tUrW1YlGnWJTZrBpEJY02B3FOqodcqVGRR3jfXGxXaEwtMYEwVweblPy+Vy2uq/HUco0BX4Sr6ZBHBpYz0iGXyLIcIKhD7OrLBV/OAtIupCSKZutmsxGsVlVvNsUXYjpUh2tA1+UFU4faYjtLiaZnhVpjXHdc4356E6feYpEaO/toxIRPdcYqWW6M6VlzMisn5nyCXvKTF/gIHsyMzPV6xA6DDZGhKIsgHXQ3s9ntuozsD37Zs1M2R8K5braVv1tjtwM5W69WQD4dZzfLHRoy53WbO6kpNvDbhJVu2A12e6YkkDOD2F3nGz0xLtb2qFvbaKeo7b4MizRxIkY7rlRcj7d2qPIibdbl0KRbmZ8xi4LQqflBmNLLIdYkaQfBmrwuxMxC6lm75Jm4VWLeIyQWJQX21GFNu1rh9sncJn11shFqWEkOQza0pPj+VWSqneADh3WLoyi216I/XmdRtMHSmOVAMRQ4uj+l54aJZP2qF4t1seV3uaXE1baEpdl3VJUZnGh+2KOsbxyRi2kLGG+ptJpl/P4oYDWRZK7T2uXcYZg5dwxRXVYHfBvOLzosnmchzMKtb6e7yt6XkpuepSOJDidUngkw7Qr5mgQ4uV4b11l8YgxC0DtkU4feYm6RLcWTjRQTh1nsYDNc2wyKHbPswknqKDs2tLv0DtPD8dC6OY8huiLGhVWKQmrGZ/nIp2kX4IPjYdtpPRRDHQchfwaL0i3luCQcgzoM59nlqm1sj9fjTcrdxGsanFlmbueh22a2xW1PZ6yf+bZR2Exazvyjz7aFWaib2LnsYacTubfb+jANSkpH+VVnJ7IOBebUSM/yXs/ktrwaXk6cZZFqmc0iCyknuNq87MTzzYJRlshsnShVfNjbhY4fJDE1KpwP1mq4FlhGahkClXB8be+90t6Vt46LommdtoXWbrPdTl9rwlKoB3x57VGg00lTJvvsUGT5CUE8vzpwU1VZXBPaXfMMurrQWUCo6KlZrCmsdZlMRN1pN+A901npVdR2UowsaeLUSDOv0KZ8IJdLwFwTdD/kK3Exa9Db9uadSt2dO7Y0KLl+peYmmUgD2WXU0tF9E0/2l73euzE6aHZedRoWrYSIMHgvTWbb4xGmglvEbZbdQjRlQ2zZLXYkelKlfbFDrazk99tCWBj6ITweUTMzWGs2A6nYbhWxjBEZaMOxUfxbYPbaCqX2jKbU2FYbKkI2+g7V5qEtbpDTbDG1goOubM0AcfU915RzLF3Q7Io/hn7GbrhyyfErU1rwJBWe0Gg+rwm52iP4krupedQCjxUOcyhpFdczab9WiQ1zMMT2eAuZhYQtpvotwYC5rwvFP+YCDSxhtqIStJDxU7q38PiawCKAyQwMXBwt2azdmpWyvCiDXt7moies8Go4Vevesg2BRnlcQYmQFc1TdTTWK29Q3N0U54Rkt6yyq7BXCJJw5HKqdq2DH9t9vTnJyKpQl1ZsTS/TJdWsur3Mmu6qmy5PS5An8SDb6/NRybZJOj2oipZoVCRvi1BVSxn34h09D61cPBCoxrqIiO4bxnaEQF8srrgA0cSMc5TliXyenmdxo5S0iRwzzjiTW299QXrOQZRmH00dQFgEQbRVO9C6Z8qM3CJ0LPXrziY4WsGr3k91sHD6vq8N91IdkqCW7XzphetNuMJrabYhVZ8JHNjVigcgHcU5JfBqG6+OvbAO3WmiWLugU0nbUgtun4OF2d34KI+02VIOOE2jDuW5jbWroYjcut6k7tZd7wW8OkSHLAKtOiCDSYVhsUZ7YpizW8AseOys97Kl22EBK0G0ZXkzPNrZ8hwqNlfS8prp6XnUK8U6Qul6zsjrUzQN6kNnbUmyldY3kUJsdi4dy7MaKmjugNzg53rUEzvzGqz4+Y1zkrkW3Y4xvlq5gR6hLlhSsw21mia9Nt3u8tU6R9SkrsvtDlMvdgzbipBPdlFtl0zBZ8fwiB1v2lYTWidJEdMZEtz26Is2u91cURS2Ij/nmvWJJhXXngf7Xg8Z3pNhW2uiU3GDXZR5XfognumnlpnJ6FaBiajOjalgzwUP13na2Bhod43ZvHFq9rZWnLQb9gfQZudFDBhLvt2YUBNFfJGKfrwTIHRVKx5LrwwbS9OLlAXeUWA8Zk1tKXU3Zxao1OBnDOeY05FVBqMUYoQZTNUxJFfzuNA995TKRZ4fmEuvAStmBtuGxFlOZdSmjnh5ss5sml4Eh1Gp+ZE0D9hyukFXuwInNhmF9Dcr1649tpcvTtH484TYtit6U2drVUHy9bxXsrxGaV5SfZeKWD6tuC66YoEseqdLptxCbq30XtvNm0Cac8xARFMsKnKaP3kx4TJHnO4REJBMcBJdrpwm1+nOF7qeHliEvHJle+2zykfoBLmcg/2s24pIcOamwdFRPFkW6KlRNKWmMFF3BeJK0DZR1abC5owhi6xQXHR52YvznNvRM8KKDwowkVo7zOgjsHe5KliMEftSd1JXsxtJETflqsTri1C59PJyg41xYx9MoU3Y5kakS3Vv5aY7dIubUNEatpRPA7PY9F7eVcGm0n38hockM+RyeL2YIgFgNFI4hp9XR3zeorfDab6ovAWxpFRZ4zxSmm+udUPFWwx17OOCk2xb5G7ehm2X3TnDa7Be2Dt1n2K3mYLzoprOG44Tr+jOa33U22oSyskYvhdjqtPc4HwW46ZycCNhapk7N8Lg9NzC9FzvpnaXW5t0Xn/UtCvHHjKKE4VOcFuDWuwbSlhd9H0TD+C63GI3REpyXZeCfkanxRR2vXonViWo8r3GmtMyrOe3oap5TLFn227Laulste5AMqRVuMskItit54XRiDc5jtnS2nVp78JeLggu6Y4IrM1mkZ/NfIenV2y9mJERJvoJx2vmDoiBcjbPFNNb+mHBzKf1uevIq6pfiym7qWvshhGO5BZiu8K5c6Gqg5R6sb3RPLfAEfcKmNPhAESA7DeLbrAsZtNVpTw94hxNuY4frdw9BS5nk9zURjVDd8lcR8nltIt4UzI4yWIylJ2jXVq5BmzW417scVUCGM3uLL4YiK5mrsfbicrxrRv12CzTFKv3tsmNk5xrsK4lfpW3NO/K3GZNr28LNlBXVyRcehgmbqhdSHJri8cN31gQeUK2TeuxSoPwy7Y7t/7MlYhLd/YZBXFMDiOOKcuKHBNGpIi0EKE1ErgaooGQQzJYGhuEVc5OThTEcW6YKpVctDbagUPZLBGC5pGpICgA7Wob9uw3bqVsVhZYqexKB7wK9HRnXlqJvQ2sChp9albHJC3qi9u4DXJZJ8sAZk0i+yLHcd7Ahnrcmaqie2l5ANTFRXVpW+Zm6me34qBew1WyNaaSJxS5gXLBjgqM62ahHvU681aBKCohQTqR0h4dpzsevAMIY6Mt9+7iIFdVJ1yn2SXlpZBkd3Ha3PqmyyWbdHm+dVfngUIF2+wpTyv9lTMFdmQlc1WStbVwofUm38pzTKYbPKdkpXbs4mpwitE6m3yOtGQtAmEAAixMWJtPNcE5byJVROq+IaLbrEimGuZNYYLspRXM3kZIOCO8njALUYYoRyLslgEc4EjMu0xV9FuXb1lCM0u3U+bSYTs3Q1P2fQFyWcv7Nq73zuU8Ndyz1l8kxQ2HsC2tKQnmOUA0t9EdXlajmOf5n39+en66v899esVQiiKfn8az6Lfj/3/hNDi4RcWXNwIEM67/3zu+fBwlvr8EvB/LA9t7vXN//aey/fr8VLkRlONxbFwnbfB2UPnfjmM//c3J8LhoeLxzHt9MXpv3lyONHdzPq6PMa+umGr7UedLeT6uhLdt6/IVJPf4IyYXfT3cV0mJ8d3DnM36791P7L03+xYvqIq/B0/jzj/FtG/Aiu3m/Dd7O85+fvAF6JHLrLwRNfQFVMSr39gpqPLUd30E9/f7/AAHBNwcWJwAA -->
