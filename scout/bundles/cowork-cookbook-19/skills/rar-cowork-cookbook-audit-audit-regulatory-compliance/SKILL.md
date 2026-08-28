---
name: "rar-cowork-cookbook-audit-audit-regulatory-compliance"
description: "Audits audit regulatory compliance records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_audit_regulatory_compliance", "rar_sha256": "a3d4654abc82bc8240fd371607bbbedd9ce9ab36328d20fedf89982301b3f7fb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_audit_regulatory_compliance`. The original RAPP
agent is preserved byte-for-byte in `audit_audit_regulatory_compliance_agent.py` and in the RCI capsule.

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

Audit regulatory compliance Completeness Audit — Audits audit regulatory compliance records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-audit-regulatory-compliance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_audit_regulatory_compliance_agent.py` and embedded as the fenced Python below (sha256 a3d4654abc82bc82…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_audit_regulatory_compliance_agent.py` first:

```bash
python3 audit_audit_regulatory_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_audit_regulatory_compliance_agent.py   # or on stdin
python3 audit_audit_regulatory_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Audit regulatory compliance Completeness Audit — Audits audit regulatory compliance records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-audit-regulatory-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_audit_regulatory_compliance',
    "version": '2.0.1',
    "display_name": 'Audit regulatory compliance Completeness Audit',
    "description": 'Audits audit regulatory compliance records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-audit-regulatory-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-audit-regulatory-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ef7e1f9165d7c161',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/audit-regulatory-compliance'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/audit-audit-regulatory-compliance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.556, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditAuditRegulatoryCompliance(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAuditRegulatoryCompliance'
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
    print(AuditAuditRegulatoryCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716ebObWLLnV9Hc94ddD/uKHeGOihgkoQWEQIDYyhUudhD7JkA19d3nIMnX9uuq7q6IiZF9JQF5cs9f5gH9/mJ3bVTUL59eFN/OZ1s7TePIr2d27s1WRV/UCfgoEgf8zdwib+vY6dqibl4+vHh+49Zx2cZFDpYznRe3zcyePma1H3apDehGsCgr09jOXR+cdYvaa2ZBUT9O+62f+01zF1YWaez+QG6Hdpw3gFmX+h8du/G9mRv5btK8AuH+YE8MmpdPv/z64SUG318+/f7ipnbTfFXm/ia/abJ64wyWp3YeArpyBMbn4Lj0a6BVBk55fjB7Hr1v/DT4MPvv/056uw6bnz59zmfP1+eX6Z/c5bM28mdtYTftpJ5d2k6cxu34OmPS3h4bYHPb1TkwcdYA3+Xh62PlN05FOft5uvb+IeQ19Nv3n18KoII9efbzy08z4K7PL3U3fX+duJTvf3pNi96v3//0jU/TORffbSdmQOvXL8/jJ1tA+I00Du5SfwZcHzF0/M8v3xk3vR56T3aClS+vlyLO3z8Yl3Vx9fPJj+9/+iu29zilcdP+R3x/eTCOfNsDNj0V/+nD3cm/zqCnQW88/1psCcL6dywB5F/FfZg9HfVXvO/+/x+s0xik75vH/5Tdny2Afp798pe2/asFH2bB55e1n8ZXkB1O6n+a/f5FkdjVL++8byff/foHYP1v2ShFV7t3Dl8yO48Dv2m/fPnlXXM//e7XX951Jcg1386+dHX6Zzz/zK93OT948En1/se1QP45T/Kiz2dvmT77vSj/V/3H60yz09j7dr75NPu+XqYXNJuM+Cr04YLvaqYBun7nx59e/gAIAZCk7tz7ZVDl//VfMyF266IpgnamuEU3wUzexpk/Ka9GcTMD/6farn3g1yYGjn3SgfyfIjxpXASz3/63e0fJj+4TJed3BPzyeP+Gg1++AdtvrzMVMC7qOIxzO53JjCR9zu3Qz9tJaFn7jV9fAZw4Y+t/BED0cfoyi/PZb/+W95c7m9dy/O0OqvEDn+TVfsKmBgDp62SfHvn50xoXgL4/+G4HJKSFC9QJYgCrH4DdTZFeAbZNvmiSOE1nXgwQ/A7qE2/gr08Ts99++w2Ac/Q5f4ApNnt0hWYOCN7UmX38COwK0jiM2s+570bF7N3vf7yb/Z/Zv1p1Zz7JkACsP6MBNOQU8TgD1dVlgAwECoQWQMc9Gr//8fQuYJODNgZiFwex/1gMsjPxva+uVnbMR5QgZ44PXAzcm5VF3QKEnsXt62wfzN70BUKnSxOGRwXoR55f+rnn56BbtZENzHnzZF60swakYBOMH2Zd49+l/ubU9z7mZ6DM7fa3mbCSQMcoUvA2qXknAouLPAbuf0uEx3nApH7XzJZfWbzOjlM+zkq7tsuotp8yAvsRF9Apvi4HzO1Z7vef86k5+pOr7sXxcA8gAp5xnyH9OMV8ar0ACbzmq+w7jT31NfXe3+rPefNMfLt+dHOgyjgLu9ibcu8fz5RqoqJLvbv/gKYTp2cUvGdU7jnI/ItBYfX9cPAg/NyhMILP/n9OGXctt1uZ3TIqu56xR1U2H96bBqHJy4/ZCbT7u7B7pXwbAb4CyFcc/ZynMUiFevzHg/Lu8yfNA5u6GgiXGfnOH2gFvDfxvefjlF91PWWy/Tn/CtgfQIjv6ARCAooXJPeUU18FTle/ahqBCp2OvzXvp58mr4Ccm5WdAzwzC3zfc2w3AVrVU0093Q6S05/qq49iN/rBqhngDvwP+M+AElNsAKjfXXcsgJmgnIK6yL6Rx9NIBLTwOhdoCyZN/3Wmg7KYUqMBtQjmmokGeOHdndUs84GPgYpvHm4iu3woMw2nTwXtCadjv//e/89L39L4rsmkPOBpe3YLPNlPuOr5wyOub1o+IwWYZlN23Bf9GOynpbPv+8o/Pud3Dd+gHNRzOrXk71wzA3WUPXJxgqMGQErmP9MH5MG9+74+GuijQ7/p8umf5vH3f29kv7fE849x+zSL2rZsPs3njzb2tYu9ggqZgwyJS795dLSPj/dvNffxWxH9wPjhp0+zv6fcDyyeOf1phrzCr/B06RC7/pS0zxfwxerj0vyIT1c/52DIfwsyEF9kAOkm34+ghb41lq8koLuEwIqJ+NFomqk/9aAl3pEVhOFz/pYIzyIBwJ2HU1dsiu+K995hQVgfUXtrAOBS3gLZ3jSRhf60W0kn9Rv/5VPepemHl9zO/P9klzKhPMhV4I1pcwOqBkw4bezfj4BV4EJsT99/3ImJ9y92+sjppgVq2vUdGZ418oS8D9N4mwNUmbYSUyt7wD7YANld2k5qt2M56fnYuUxT1NuI9c9S70UMZHjFp6mWP8ymcfjD7G2y/TD7ute4b9/yDmy2fpmm6slOQAo+3mjfNpeO//Lrn6jxHLL/Qol4wpEJeR7m+t43kLiHrbRbgIVn+QBUKtz7EDE1zma8N9h/NhsIrP2qA53Sm1T+5oNvqhUPff64m9I+dpK/v3yFmWfwnlMjIAf1/LGZeuUcJDgQCI4fqQiu/f158skA4CIYZwAHG/NwksBtx12g0x8OBx5GISRMOY7jex7t+rTtYCSGLjwUDnwvWND0AsVgxMECKnAAv0dGTzKyeFLKB2QYjaCuh5EoQeA0QqE27dk4ZdsevFhQMBV4oHV8W5oAWH1a+rBscuPbaDt55Gnw7y8OiQPKHd7smcdrNac1mzIOzhAZ9I0MzP1lUXCKXJTU+QaiJ25YbZAsAd+1aclVxz5Z6f3m6K4YOTxk2z2cNemaYPIbt8YwKiYhRWgHGLOzretmjdNiFE1K7oL2BCZewXrmkWx1JqtStCzdEIddno0HTSg6TeRFqUp5S0gcM3bm9KK60tZeWVioXuL1IFw2l7Q0sKZ0w4Y96z5Zh5ihEVwuJ/sKERDjXF3YaHvVjKHt211Bi7kaz8W8JOfidVDzG0J78+WK19BuM8hJoqWrWO/8tM7theYYutwoY8J2Hnw5Lqrbijgkg8bXiVUapTXmB2xgCZfUVIK3otOAaJ7Z+Qe4b/Q1oZ1HnUM2ZplvTopRaibeo+FFoBClLIs975EV3IULFk18Az0iqRo4sH0x3BE7ZjVuWAGhWzLsJGdt62/wqykrwzkGMq+hLSabVd854iIZuWClo/aAXn3IlRNmpE6UzTCdogbcdWkJ9C1fQRRbNSNGKarrcYoZQMml2uV6ea42R+jKaQktoHwJ58PBxdYL4dQo295wuEraNluzXZEtZ6TkzY72CoZWCOVVbp7Ol6itNw2D1qd1uc7YIeHOnoOuhwOyxxCTFD23h1knDnWfxYLOJxZhzG9yRr9ko3tBksFPTMyi0aRKMTBY97RcGdyFGeca6pxlEhsvxkFlKCz1hrBAWWifBmh/zhRpAdnL3DdIepDmMcnrSmbE/EFVmmHgd+fFxSs1Sh8Z77bm8oBWYWQDdRXfDAswChGmf9MjN95sfW65WdSCyEMZ3S3QjrTaLldTPZKOg+mXSGmEeO52u8KU+tA1Ia3exd1BnZ9cKmfRObTdkZt+FA+pWuvZCAxX0tE3qcbrOZbwyUq4CSqeJ4h8Fk+ccKFLhosHbLUVJDMV+rnd3q5JvPFHaOCzU76Am1QWQ4KAb8VBbcjxutxvT0i2qWXh6Gpeb4bMYgvr8m2BFyyY4r1E2a2YW2+txHV3inhdllUt87ds76oiQXEX91BAO6nO+By7SNrWkujuKm8RLAqplUuKnCirusRHAUEUZ1IeN/PEk8Kh3445r7dBuzhArMlDq7Vq2HNXXN1s6EpwxpJsmgGuoS2K+fLoibZ6UfxY2o7Hsj7H+PIkBGRqzWOcV2qS4+F2WMYrE9HOZ8tY33wdwQuXLIbBiM92Afm0EbNMLrb5kr4UKGwtAgkvz7rZG2olmAuSDo+XUrVg9LKwWput5E2qWQsHbLnOqIfjsX8mE7RV0HOcOmhajLDtDGd+ywUbfhnAkhQD6MS3DVSbZXIIyxxPjMtJ28uneWfsZU4urbOEsgvWJVP2zFFBld4OObayXTVpBA6FGb2pPIAsBWpRu7UnlF2kx+V5bG+638B7VxaUGq1Opdvn2/aExfbpYjJZPt8tNC2rFbXNCNglG9OpOG+DBwQlRcku3HGRlY7p8cq4eId3i0DhVST1YapGCj9fI9AtoDE9os87fHdYRmhHHJU+pS+1L8r0gsFHj6kDNzRWetHm7FXczq/Wie2RqAkPSH2NODOWmps0DKfFKsOYbMDy1TmQjg3iRudxEySHtFDnQoO5sOyMS0E87QOCV909m0LL9IavGjq2tsZth/uJyyoCFDOwqm9A6z2nW4C4IcfCRW3a+5teaAjVxMeNWfXNYc0tlX0e37iNzp6rPcFTPUbll+sqOVSccT0yh6zb7dbHWw527gqmBuvs0ixIKMgtdH69paKZsOaiOlrNZd6SinJha5/YZBBqHfs9XxfwWphL2NAy2yW2cwMUN9lY5mHo3NNGgGE4tNmNenDrG3tBOunudFqh1yuf4Nx+KTYrMRUclVAqa8ueLxVyrnfeqewzaHGx41JWc4yRvWV1KMl1mnHJGQkSZB/CFB7WyY60y4tRiL1BqmFKHxxGHRIvzVMvU9fGEg8qeKxcERl8z9dO5DqBnPE8Zh0BaRBemJlvb9xLCHXjot1Ag7eqgj2C74br5lhimxjhb9EVTeszt2Ojaq7hhxAvaYM4hct+3RBTG7Lgtm2HNTtPs9vWYNXt1rKsBSGJjs4b+rYls5TyLmMwGtTpupbJUF2Z5WnwdP54oIKl4aquudirRkUr3iI3e7Y0h0YVvIYSwniDXtfNucKrHVUEgifsVnbNyKqTnZlWVWQGX7DSkCrE8WiCfCHs4sqnWqeIp4xZVgGnOUh3WZ+Y5MaE/IWoHR93Ib1njuwA4csRbfggDEd9WGnhPljumvMNbG/ImPbEXbWn5T6pPKa0IYdfodh+WBBDxqXUNuSXIR4VPXJbdgiW8jp8Sfi11Sd1DAq2bbeLOE0a9TxseN1eB3vMpwRVGMMrkZIwscJ9EebdrXAlkltgcxXYuRVL6OaTeqRzN3o8yrGwz4OjvUwPu27duScoOiaWr0H7vZ97vJo4VTQujaBYpcLGq7c1dmBII7WKSgsVz5QpkyNCWOf0IingbLk+G3KiHapViKxVrkfQHeXdSBWy2XYvuLsDaWFQzwSo2qaJe9FvvbZOwNQTlTDqimjigcoSDGW9TKVApSWYCLozGbiKvPR6elgipYv0cCzuipaqVHUYCUyXasKzqAZsqSz/th3F0gAw2h3rZHWJh3BJYLVvhMmeybYFs92ujfJGWZV4Tt0dxLKJbw5Jf5CHzQGB3BxhKYEw0xU37DivhYTbJmsyXGbgjNhDlXkWMuHoae7oyr4kXRWt84RqeU0kBLFdsVSg0008LYlDvrcEmU8FSSZbgzvrfBN2JYeJp03Iweswt01KZfpzKnNkKI1Ls+JjyyDPlXwNL7vTiAtXXWNpC/jXTcslCRcQuSgF2zGcPl6KyxEM9H0B42uJOSIruV63t/AoXvCLN1JWS8fehaRwDowbNZezOr/a5Hut3aa2Ta4vFsXucPK4ufB5WJUOKTf7c+P7xXGo3UThjgRN9AWvHa/n9SG5LRux9SDfcxzlOBwbir0Vjm5Jyhzsi3L34tAcv7jubLHRfB66CvuKErY5pChOvMZ94mqbrb4/d4SrnNciesT4+nZxqIRI+fS4lsKrgqocjey6S2Mh/lKMtEXEEFKsA6w2M27kA87uhazNyE6ruz2aLEJdLrsmUiioyWgsXWOuqTHnHK+7Qz2653qub5NwV1o7pydiOzkXUhGKGLMlLNd0Uwg74lZw0mjKT2Xc947k2Rg5Q8yda0cfb0VBHOPaFbZSMtJRS+kUkh+zZsOmeSQwi/NquSioleVJq0qovPOaZzgB1cJRqlS6qg8Vn6TsEiHyPduzuN7HYuh2tmIHN2GJQ/SoFPX1zLGRuF+EeLI/42p8PGhKdrJUe8zEVaFKMheeGbVZ1ittc7nu4UZGkDyi1Nv54ire6cin6+NZ6UPPR7xVCwrY0BY5e8GZKM7xbI8tXARC4JOKIAeSZTxdXZYLc3dNlEW0iAdxnuppy7hXnzhc4qiAuEsG73NtF8GrLqkaf0XYpMSEJ88/OGKLrAV9LUQRtsrOu1sEMztNPlCiMh8vsB735kE9mKLKGxW2Le2qWG26TMkL3dtqNYtpsQE2GY6xBRCgH8m03RqH0tBUbw+wljak8EwH+z63hzQ2w83Scitlu8FkX0Oii9v28Yk+kkuIDBHC9LaZZiqZjAFDeWGFjrIJm3tCPdjwTS7mhc91/G0XQPNlsOnRVtq2Cm6HLcJT5DLZ9LhzDM7yhThlRclcb3YrKWs9qkfLq5dKC5XUEa0AhARdsCsMz4Daxt3MN5q7x2plN1BuielXaKSoEL9GY4t7aLaMLHTELyFrhJptY7m2F2Bqk21x3cWsq3DMgvBcST1/axyNkdpsvsstbN7f1p1iHlJ2f2NVFybatXaRVItfXDKaJcKT5QaBqpxX/aEhB3GvJeJtzbfuMvJKxUViT0I4ct0NuLdgCCraX3GzI4dkvebFuLlum0vnOgAnxD4dcNSWWjm4DOPa5a7XObmS0OWC10ybnhtzPFns1txN3YnoHKs4QhiQ035t0bXhnPMB3jgxUZj26hZeu6LfWdScScCYjm9r87Ahl0eSw7wkMn0zCBV5gFR/vw7F0ZpvYGNz3Qb8UltQmLHvq7PlWzsZPu7ASOZUcBIeY29Ec/9skstsUG57UhX4a+SkReuUnW8wuBxgUrblpJQSjgO2CaLNWrIPInpiDtS15julczwitU8jcDiT4zk3jFKJMngbcOlFiCA7thU3L647+dppRUBgGlnP6x3WCeyxPwSiu08LtmhCT7r2nRhR9m1xa7N9dyl9CGUajSOv8ArFm6EJRHRxPYZYVWK54a+Ti1rvGlWiCGpLBXuuDYslxac4vR6cmMW2xKpQ8MHMTcWT96K8PcBqp1/nqyPfn9xMkEZ6AxdOkTAildhyw2BpR3FEyR6WvsOFa2dodseQj1VYahAbT7EdegpEhtC6jdOHWcexeTCYEnbpSduLtsdC0jajvt/667LsfWVgXfYIdo07N9XXl5OpsqBP2/MMWUEig1oXrp1vrdvWWxkraiE3Ko0NmK2Z8fFqomoO+lLsbZVex+xlY3S3prHNUc4vyMqMKIw6mGvak7HRxq6GcTl0QjSsU1IkLqEYxcLuBAlHQw0p1GNDXK9xfqDnC9rgJWlrQgiytE6HZdOJaEMudG9ZItemakmrrIcDpWUnk0xHV5AHjw55eqv2JyIimTC8kqeTQrMZLV2YOAyYISiGhrKLk7vD534yXqgyL7cUwroM5VLYau+zx7qNb6wbbGlrTrjsArUsmjC0q39dHHqD3a+pZjFH09MCXvtRzh7wHRhVsflpaLsUSjwBY3sId3ZGBdOm5tg0du2X2BxmT1QanDpsodVkaPon0OA981TFzBkqdb3vCPomSSdii6hEfNypRywmRm6kIAcN7dXK3FR2d9hh0EIbVqVoA/Q4UV5NkJlOlVmD2pEPL7ENnB0L2Zc382ZRCGJ0kGkmoJdKeFmlUaWt1+poLa6GnsBt4FBXS6E7D2KtrjrZ7KCK5O4mGiVihUvcl9Z4WdvNgSKWSLYumE0drcTD5bQhrstM3mhQSROCHVowUS0F4bqKmg45+ulaEZH80DuS22MbvbeCVtOLw/yIUZq5PuApztG1ZyxGFkWNk3eYW5GTb+dLLYUGxOr6lj3tDlJ9Oa7SWIuGbPDmfLIt5nGq5o4q3YyRET1kxNcRI95Ss5XsFRsfj5sxZClJOXBSfFhX2Y3fcSJO0NjugOV25+K0lLvU7hgLUIvTK8iL+fAwrhKGYX7++eXDy3Tn9Hnb+j9/CD3dDvx/dlfycQPx6+Or+81j3/Y+3WV9+hs6/frhpXZjoNHj3muTduHzRuX/uPP68d8+95iWj48nu9NztqH9eoO/tcPpl0kvce51TQsUaYq0u9/8/fDidM30K4lm+iGNCz5f7mZl5XTX+y5ruhNeAO5l+6UtvmR2nfjTuTifHh35Xmy3/vMwfN6I/vDijSA4sdt8wUjii1+Xk5XPpyjAOPQVfkVe/vi/y2J+n+0lAAA= -->
