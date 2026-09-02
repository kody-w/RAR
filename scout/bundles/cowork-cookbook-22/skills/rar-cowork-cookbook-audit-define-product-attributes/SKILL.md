---
name: "rar-cowork-cookbook-audit-define-product-attributes"
description: "Audits define product attributes records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_product_attributes", "rar_sha256": "d69e6a86297e539d5d5fefc99cc4b11aba432e2c106ced12e3a23b07dd89cdfd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_define_product_attributes_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-define-product-attributes:edbb7062ac422133946bc7681aafcb3b1b1fb1433c2dbd8041f70c6729670e8c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_define_product_attributes`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_define_product_attributes_agent.py` is
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

Define product attributes Completeness Audit — Audits define product attributes records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-product-attributes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_product_attributes_agent.py` and embedded as the fenced Python below (sha256 d69e6a86297e539d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_product_attributes_agent.py` first:

```bash
python3 audit_define_product_attributes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_define_product_attributes_agent.py   # or on stdin
python3 audit_define_product_attributes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define product attributes Completeness Audit — Audits define product attributes records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-product-attributes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_define_product_attributes',
    "version": '2.0.0',
    "display_name": 'Define product attributes Completeness Audit',
    "description": 'Audits define product attributes records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-define-product-attributes',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-define-product-attributes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b8856383ba1faef2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/define-product-attributes'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/audit-define-product-attributes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditDefineProductAttributes(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDefineProductAttributes'
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
    print(AuditDefineProductAttributes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716eZOjxpbvV2Fq/rA96i4hVqluOOIBkhAIsSMk3I5q9n0RiwT4+bu/RKqqbs+1515HTDxVVIkl8+znd05m1m9PdtdGZf308qT5dgGxdpbFkV9DduFBTHkr6xR8lakDfiG3LNo6drq2rJunT0+e37h1XLVxWYDpVOfFbQN5fhAXPlTVpde5LWS3jxl+A9W+W9ZeAwVlDSjlVea3fuE3zZ1VVWaxOzyex3bh+pAd2nHRtFDdZf5nx258D3Ij302bZ8Da7+2JQPP08suvn55icP308tuTm9lN8y7K+i6I/JCD+hADTM7sIgSjqgEoXoD7yq+BTDl4BISH3u5+bPws+AT913+lN7sOm59evhTQ2+fL0/SjdgXURj7UlnbTTsLZle3EWdwOzxCV3exh0rjt6gIoCDWAfRE+P2Z+o1RW0M/Tux8fTJ5Dv/3xy1MJRLAnq355+gkCxvryVHfT9fNEpfrxp+esvPn1jz99o9N0TuIDawNiQOrn17f7N7Jg4LehcXDn+jOg+vCf4395+k656fOQe9ITzHx6Tsq4+PFBGLj16heTf3786a/I3r2UxU37b9H95UE48m0P6PQm+E+f7kb+FZq9KfRB86/ZVsCtf0cTMPyd3SfozVB/Rftu//9GOgPR1XxY/E/J/dmE2c/QL3+p2/804RMUfHla+1l8BdHhZP4L9NurJm+YX37wvj384dffAel/SUYru9q9U3jN7SIO/KZ9ff3lh+b++Idff/mhq0Cs+Xb+2tXZn9H8M7ve+fzBgm+jfvzjXMDfKNKivBXQR6RDv5XVf9S/P0NHO4u9b8+bF+j7fJk+M2hS4p3pwwTf5UwDZP3Ojj89/Q7wAeBIDVBgeg2y/D//EzrEbl02ZdBCmlt2E8gUbZz7k/B6FDeQ/pbUX7U9JwjPufcVAk+ndAcQYXdZC7G1HWcTzE0enzQoA+jr/3HviPnZfUPMuT0h0esDE1/fMPH1GyZ+fYb0CHAt6ziMCzuDVEqWAfL5RTvxe+Bdl3++TiyBOPEDclSGm+CmAcj4D+jrv+Dxeif3XA2TCl8K4BOAq4BW6+dVWdt1nA2QPWGUM7T+ZwCsAEfqMssc202h6U9XPU92MSO/eLOWCwqF3/suIA9lpQvkDmIAxp+Aw5syuwJMnGzYpHGWQV4McB8UjOEO88DOLxOxr1+/AkiPvhQPEEahRyVp5mDAh8DQ589V7QdZHEbtl8J3oxL64bfff4D+L/Q/zboTn3jIoBjczQUCOYN4TRIhkJVdDoY10BQSAHLuXvvt94cfJukKUPpALsVB7N8nA2rfQmDS4OGcd88AnScR/fqN0x/tBt0iYBcoboG1QH43n74UE4kSDK1vceO/G/Ex+WH6d1c/+Ew+ad5sCPwU1GV+H3uPvsmZU0l9hrgA+rAUUBf4tZ08GpWgfnp+5ReeX4Dq2kZ2+82FRdlCDciZJhg+QV0DVJ0of3Xqe931cwBMdvsVOjAyqHFlBv5MBrqzB7PLIp4c/xarj8eASP0DiDH6ncQzJPrAmlBl13YV1aCI38cF9iMiQG17nw+I21Dh36CplvuTj+7ZfI+89V+2FMz3bcS96kNfOgReYND/v25kkpBiWXXDUvpmDW1EXT0/wmlqlybtHh0WaAzuzO658a1ZeMeVd8T9UmQxcEE9/OMxMrhH0GPMA8W6GjBXKfVOf8rl+k43bkEcTI6t6yl27S/FO7R/AqYFXmgmlALpmk7JX34wnN6+SxqBnJzuv5X5NztNVgHBC1WdAywDBb7v3eO8jeopi96MDoLCnzIKhL0b/UErCFAHDgf0ISDE5BkA/3fTiSAbQGv0CO2P4fHkoIfXgLQgXfxnyJyiF0RgAzk+6ICmMcAKP9xJQbkPbAxE/LBwE9nVQ5iphX0T0AZUrzGIsu/s//YKxOFUQQC3jyQDNG3PboElb8AFIIf6h18/pHzzFCCaT9Fxn/RHZ79pCn1fgf4xJRqQ8BvMg557Kt7fmQagc50/YhGU1bQBqZz7b+ED4uBep58fpfZRyz9kefmnrv3Hv9fY34un8Ue/vUBR21bNy3z+KHDv9e0ZZMgcREhc+c2j1n1+ZNznt4z7/C3j/kD2YaUX6O+J9gcSbxH9Ai2e4Wd4eiXErj+F7NsHWIL5TJ8/Y9PbL4Xqf3MxYF/mAGAmyw8AZD8KyfsQUE3C2g+nwY/C0kz16AZK4B3P7oXhIwzeUgTAZRFOVbApv0vdSafJqQ+ffeAueFVMiO5NnVvoT2uabBK/8Z9eii7LPj0Vdu7/67XMhKwgToEtpgUQsDrog9rYv98BncCL2J6u/7hWk+4XdvaI56YFQtr1HRXe8uMN7j5NTXABEGVacEzlo/i+B5qEbodqkvKxvpl6rY9G7J+53hMY8PDKlymPQekETfMn6KP//QS9r0juS7yiA0uyX6bee9ITDAVfH2M/lp+O//Trn4jx1or/hRDxhCET6jzU9b1vAHF3WmW3AAcNVQAile69ZZiKVTPci9o/qw0Y1v6lA2Xam0T+ZoNvopUPeX6/q9I+1pu/Pb1DzHT96Bke4QYm/Ltt3WSV93L8OtG1p9n35utupLurXm0QFVPZ/e5VOPUQr4/gfXoB8OR/egKTp4jJ4vG+tn56CAO0+NboAgoAaD43UxsxB7kHKIHiXk0apAAkv2MwPY69+/jp4uXPu+O/RowXUGQcEiYQ28UQZIGiK4xwXJJYLmw7cB3UWTiLwFlgKOoinuMtYWwRkLBLkMiKIGF/6QIZGhAxuf0mw3wx2R9I/2Hkv9uwPz2mg+KC4MS0YUCsfMJeEsiK9HF05eEeHviBu1q5LuYsFrZjYyjiI+4CJkAhWyA+aiOoA5Oet1y5XuBN9N56xodMr+/9+btHHrjxCoA2jyeJEdt2ly65wLwVaQOiKOygrr9AFh6J+jC+QoPl0sf8ifLb1DevTE57qD2FK2gXQbN2nfj89ublKQQJDIzcYQ1HPT7MfHW0CYx0xMiZkUQQXpJ5Y5swrjneFvNvjVQtDs1tZ4t8nJq9qiuEkSK5xWaRqsXdwVuLzI6gZUQLzuRVivKR0C0yJhWOXTSpflvKfHANOG/YUFrCI1zmLrf7o60ujGTrH42a9TQDloYZYmnnS6p0LXLMvaGsV6umu64qMScstM424T4zL8g+UoUu4bGi3g8Dqw3tcpmNvUzP+Fo4bb3DwsrP/XEQMsZw0uNYu2uF8Oc1vOyECrE7gZ+N8cy+CjtYRuxYukmctyG32SmHBd7OZ8glsbQG004yf7ZkV0KZSq6NzNsvJbhMyV1sX+dnPRt5XQ6rnKOSBVWSJxz32OtW0bQwOWbnyF9YdLPltGgmJYI7z7QuugxJRO5xzVRdYuDqgiUuVdleRLWe+SxxW6wiAvXj9uYi7YUT1gKzHC+s4UX7eK3ng36Ew1I32HVzPUti3J/OTm72BI6wSi2f0xze0Ms07geEHfDbScqIuaVFJ8erubRdRIHizkSD4VMZuWGmjp4E2rIa+4BLMnlmWN6hvC4vl/bNb0ThAudRXS4uO1oItHpXI9Xg17Nt02ttc14oYaGxh4oc47JfNMUFZFBwTEp8Ma4VtdurziGv8REN0rOqlDgDO6cE9tgDieVsfw2sPpcxzzF3l5tm581awGW8NW3nHLdue1hfVRvWKKvpVy2/dGjV4uREBLILWFKzATIOxpVxZdcwN+153JSePohwTt8umT6sRxC4xTbv9aN99EfJ500rxjxtO5zPOJbuT4oLk7zoSLh4Ar9mO16G65HNE1pOh74OldNVuSKH3U2RmzUnjpy65dFuTfQ3+Xq99KssOOgxsd0vkuZk9rhlpPFsZV1ZlzCcfbMSezkOIqJ2NZtPA1Yey2YF+uM1K+qHK1G6Di5Epr5ekifFQOMsJbbwTt5nnnp0C8nb9rrGLsPKqXohXhR0RDGKo1o7edSiuJr1ucq5nCjS6YAdtkyvXAc8Uy0M0+nFgSyuUnuTEkybdWYe+MLKOKaBusFPsNYKS6u7Ooc4PkUb76rLBlEIibRMhPlqHQq2ytl9VgTjfDdXCdocFNjDgm1uzQL3dGIv3bVPE5INyUAla85Oatk/1Kxrw9nFCEw9oK6yK++cY6HyCAYi176F2VgYx+NGy1SNOZW5C1dtatSbXJ7N1C7EBz/1rcrnk4RczQWRu+z2S48qs1xYdguekBbbQt/LQ46Xampo5lbSbdC2LEZZ3ujZLtKVm+vFwa0tzNHq9qURCuelYpkhvmRPWxYfza2Ri6HLiHMjWV24imZ2JHI0+T1vcPNZVfRrdFB4Y49cjTqX5e6Mi7uBKguHai2Nb/3jUWybfL9D3B7b2nt83I+HjrcsLWWsfZ1flMqt+CYPrwfYZW+0yHUyvl+Ygq23OQ67Q3t2LpY7x1wel6PNzt3xmXXBbjlaSifUOPlytZOIxGz924zbZSg5jxdzHlaCzCPpmHO9ZM3oh5D3HA1NsMDhpEOu7NHisB6K/b7vhSS6ksiZ5g9nh9MIcaHAhsLOgoLcNwGrn3vNuhmXc3528NmKCVFyqZ/OCymzUjMgaZMTd/uMgjlJvjCwhm9XFJMBQ6nRPIgGTYl2PaGIikia2MWdmSYaERQtaLFY8YmohiZs4nzPJ46LNXzK7JVundvamSu30Xi8Rh0q7zw2FS6IHB0oUjfXtZzjIxKMndTEkgcvrik6LrFrUc+WHL8JtbNpStJ1JuPi/hDXM9DnC+SZ3XDjdhvhJDnzt/U6YAhSj5H1DTa4YHM6oSMys70goOsxGpruWK7cUoi2ylkarM4kh1LZpFSGVLTGitl81KmG0YTMHmxdothBUEZdlNhLuSZDzozRszvSasKOoG+82al/9lztqOmrPUwXWaGImMXZ863HCahGH7eV6xnreEhHoorxmF4hVsaqvlzWu3Q/q6ijZYmIxFyj2QmfeWPZJUe3Spi9PPfFbUXGWGNWQV701QDP9CtjXsXOShUEYP5NUcp8UwcaMiYbHD7AZFjkHCkW5joxWQmhRxjL4PgA8NJZxnU+blBZ9Jq12e4Qxtou7Ozga/yCJAOStHSPg/faKZ8Nq2V2Vpr6TKd8zORmigUrO1/l+3oog7pfWmo4ZwxsSzqy2R8vp7hkqzDs+vpyUhZaT6dZFS8v55O9GflDqM1m9cFYzGJEueLDcMK6rXBaY90gbyiB7X2CwrRzhTEiR254mVpzh6LJ3QZDTd/hb8toF9N5Ju/XlD5Yyum0NUFUuIN7NQZKWu4M8XgBXUQPGs8BwTbRwZGoNDd5KRCsdsvKdKmsisPRK/fLxCObgY0327kcSDl32vF9dnL7jGA5FK5t89JfoqRBZ9HlqCmMOzZ2otHw2Tvbq53udulhyMUBrA7q83GulwlPHGhuX9dijMaH1aFco8suZNhTHG9xUMCbEi+3w82mNnzZDLFWrleqKG5ic7ml95Kg0zVoeuoCjgh7I1Jyk88xfMcOyrxWWyZ1QWj1R8pTIqat4RQ7ILBVGQtgvQtJ+bNuE1jEylWRucLBxmmNbndmVpxW2gbzL2jTitK1L5pmHuwJTfZH1Ouxg8MRezNwQsw2S3u7TTg6lc2VE8AOx/RG6Ij0mM/xM4NsM3Y3u7Wb+LY+GN1uY1xPi8E1ZocBDy+H0ZA0xzlUxgDjLRbTlXgDHcZQ6bGtMTGMqjy28hFecBtyI82U+ckgzou9abPWsBa0ixul/eZijN5uv3D3SnO06EDTOyu8bJWdbpDabu/uLmnMyZvNXBFoxfCk2ZBqzHLjEjZPJ0TMFGopnev0yMlmtDs5cUy3HeZvDO7M1hjr7mUp7BRQ6xKbGgMs0UtS14MO0YPzyRs9dtvp0ppHEuqEgAqyDjeFl614rF2lzS2ILMK6DvtwzrNKJOE47uI5uWF0viyue+MSW+LgW65PilHBX/WxCoaTpztScyCYRT7CF5SzrJxDuiGuruutfbqRygnXRRPvj50vrrA0JEOfxhc+SZXRER1rJrSQvsMNexkEuWEr1nhuMQFe4m7tSnXusGIg61bmcsFMwfSr7hykJb7l0wPmi4lpE0k2X9uafjxRIt+F2pAcGgI5on3O2QzTMUZwmuOjpcWth2v7mLFWNDEDQho2TTlHStf3a2eb+X0xRMujzpMWTEgXAb9c4pUqbME6ZFW011Za6ImB3I6zjNkNvnx2fLEj+9Gqqb63MH3Ox/SmMjzLbfJItY/SsEGX/AY53jopH1edQGpcdBSIhVAImwNFmEosh4cc14hTf+iXy1WN74+n/TamEksFWm5s7na2BENLTodsrHgxTlU5k/IDptfbPWNmobmHVzoywkdESdxQ0zyxJcJ5e85i+pI65GJPtdnawPgUvkU+JfGG2WHZlXSaPK9L0I27WMoKdslJvdpv13jWuTMGle2wPa0ah810a6mzx1iZxe5QWi533Kw2jU7K4VlxpbVVtRF9MFExokcmNwQkcw/sghZmXbbGVGKPHjhB3Z2lDYN2dF7StaHkCM7rsCBl8SJ2LgvhcjkUAcOUfs22R5TO59Uq05YKVltRt9MqAnRdsywVjBZ08zF23Gz2HdGU9Sgt7WCTkU5KL45iNyhXQbzA8WpdMO5uGWy9MO/PpTnk7IDIVoGH+dHLut2oIvJVa4mzVmSmeyh5BFG9ykAZjheKeceETXgyjEbGRNAG9nMD9mg3V5F2WSEX9IKW2Lw1WGzeXa4HVFadsF419s2TZ0tpbda7LvNWIMwo/LTqyD0dNuR5KS7o/KZamxp1EsJ2tXrt7dozK7osvDxYF3nDDU3lz2UlnCGOiwT5fC2x/i5LkPOWwS56sGuTM5ZgqHZOWXSeHWJiHs0NzKDIC8aywQZURys6+h0HTGtJNinthpRUUXsp+6AZWsxOedLhfbpe76W4ubJw0rkOPBjFWbthTivDpdzn+KJj0BM6p08os1oz3WI2vxQzsaOpzoXVeXz1kMTxKFeLN14Qj4uFVcnUqBjRGlTvPMQuzQ7xZ2d1yBVtzTe7eDnkK89qz5jG5mBdMUTizaEZN5o5klvImsmp88PQmHS82ER2dXJgbwciap6IJbeORAQvpLOHK32ZIjwS8apFn+YCg1pJLBdHSkROLYkdtWDpr2XPo0+ESgV1JugCJQjXdt+pne0Tg8idjYu0rLpF6Tck6d2k/Wld2ULpZCXSpZWN9rC9LuzTzF7MxDnR91hCS0tmgRfUIaK3q2StO5iklz7azDnCYnY1cUrauOZGn+eZVmfPyLWw/FOE2QuXHIViPagVmiB8sVquIk9uNohiMsTeEYmNNlr8rL9sdRoJ+4PFLzYCbiiNirpNMNs6xzDEDk3ApaQbdcNuIGbqnqV2QbJTZZFxuy3V7+ha6yMcXhsDG3mIY24K18N7CksWGnEEKbTnSt0LKn3ur+kS9iJWLOXjto83gkhLMCFLSicxbHOeZTC/DXHYpPB17yeBrkVBwZ2XfYPMGbBo78Jb75CrRlyhPaoenaa6bhC9qCo+9lhtOKE23aDdxnUZ+8gJI0EftJWZpX7UdaWDSw5aV3023yhYOvrr2MbI8JjwNzFZqyg26wsVwMFFYufBkr8KKXxKmsCOqabchoipt7F3BcsXeyWQ+9osbG2pzbYKfPBs8rCme2+l7FesftNw0FaH6ZUYFGm1ynE5oeIwoPqg7CVH3PCSnjpXzVLXxogki8GWglXjORElMxKK7NRQCmqmmS86WgUFa4aSF7Q4zRY3utnQc2Tm77TSP9PXoOlJdDyMx3pejVp+tG10cHWapBrPJwoEEdbatZ2t5Xk8JgVVkmOHjfaQFSh128XyldkelPUp2icmPwq+N4N3G/gSYmpJbOtVRqqetGt0WNaVNVVp24U3l5MkxHiuNrft+hQ01tVokNVmm4+GgCoMYcLRhSERrkzGlFJhyQlSalZK5qZULFG7eXa35rP9DC2ykfDbq3hq626x9oZGDZVtMy+DpvKK7ELv1NtM0i7dRSnAasJ3JYUyde548/ab6nBwUY6oB2luIBVrURZG7nnqEOxXV7/auBnqZnZSkdmuJEamIuAFEbbLXXA9hptuQJsM2a5Owtk5W6K4uK6HTeefVttEHyTSGjaDtXYPw9WF9yc+Fyz9uJup560yt8TikCMBsTQol6yz246lvGJ/cyR4yxu2VqdLDpGykzqnTrujkBu+5loFyR+cAjU7N12JhUvu+MtyVqUrdumPlchVTEpR1M8/P316up8LP70sYIKAPz1Ne9ZvxwV/Y9c4HOPq9Y0QShLEp6f/vW3Nxxbj+yHifRvft72XO/eXf1vGXz891W4M5HlsMzdZF75tZP63bdvP/2IneZo8PM60p5POvn0/ZGnt8L7PHRde17T18NqUWXff5QY27prpP1qaSUQXfD/dVcqr6ezhzu9xBhGHxWtbTvu2ce0/Tf9sMp3d+V5st++34dtpABg/AD/FbvOKEvirX1eTim8HWdPe7nSS9fT7/wOGaErAlCcAAA== -->
