---
name: "rar-cowork-cookbook-audit-configure-and-manage-reporting-and-analytics"
description: "Audits configure and manage reporting and analytics records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_configure_and_manage_reporting_and_analytics", "rar_sha256": "c401c039e10289d577c5668200d1ba1561ee90745becd4f3477b1892265573a8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_configure_and_manage_reporting_and_analytics`. The original RAPP
agent is preserved byte-for-byte in `audit_configure_and_manage_reporting_and_analytics_agent.py` and in the RCI capsule.

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

Configure and manage reporting and analytics Completeness Audit — Audits configure and manage reporting and analytics records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-configure-and-manage-reporting-and-analytics
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_configure_and_manage_reporting_and_analytics_agent.py` and embedded as the fenced Python below (sha256 c401c039e10289d5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_configure_and_manage_reporting_and_analytics_agent.py` first:

```bash
python3 audit_configure_and_manage_reporting_and_analytics_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_configure_and_manage_reporting_and_analytics_agent.py   # or on stdin
python3 audit_configure_and_manage_reporting_and_analytics_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage reporting and analytics Completeness Audit — Audits configure and manage reporting and analytics records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-configure-and-manage-reporting-and-analytics
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_configure_and_manage_reporting_and_analytics',
    "version": '2.0.0',
    "display_name": 'Configure and manage reporting and analytics Completeness Audit',
    "description": 'Audits configure and manage reporting and analytics records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-configure-and-manage-reporting-and-analytics',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-configure-and-manage-reporting-and-analytics',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6559c7cc2bc97862',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-reporting-and-analytics'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-configure-and-manage-reporting-and-analytics', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditConfigureAndManageReportingAndAnalytics(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditConfigureAndManageReportingAndAnalytics'
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
    print(AuditConfigureAndManageReportingAndAnalytics().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V66bLixpbuq3B3/yj7ULXRLKgTjmhNICQ0IJCE5HKUNc8DGgDJ7Xe/KWDvKvex+15Hd0SrBlAqc83rWytT/Pbi9F1cNS+fXw6BU842Tp4ncdDMnNKfMdW1ajLwUWUu+DfzqrJrErfvqqZ9+fjiB63XJHWXVCVYTvV+0rXTnDCJ+ia4Uyic0omCWRPUVdMlZXQfBGP50CVeC8a9qvHbWVg1YGFR50EXlEHb3qfVVZ54w2M8cUoPUIycpGy7WdPnwSfXaQN/5sWBl7WvQJrg5kwE2pfPP//y8SUB318+//bi5U7bvknHvMlGlb50l0x7EwyMUG9iAWK5U0ZgVT0A25Tgvg4aIGMBhvwgnD3vfmiDPPw4+8c/sqvTRO2Pn7+Us+f15WX6o/XlrIuDWVc5bTcJ69SOm+RJN7zOqPzqDJMFur4pgcKzFpi2jF4fK79RqurZT9OzHx5MXqOg++HLSwVEcCbDf3n5cQaM9+Wl6afvrxOV+ocfX/PqGjQ//PiNTtu7aeB1EzEg9evX5/2TLJj4bWoS3rn+BKg+XOwGX16+U266HnJPeoKVL69plZQ/PAjXTXUJyslfP/z4V2TvXsuTtvv/ovvzg3AcOD7Q6Sn4jx/vRv5lNn8q9E7zr9nWwK1/RxMw/Y3dx9nTUH9F+27//0Q6T0Awv1v8T8n92YL5T7Of/1K3/2rBx1n45YUN8uQCosPNg8+z374eVI75+YP/bfDDL78D0v9PMoeqb7w7ha8giZMwaLuvX3/+0N6HP/zy84e+BrEWOMXXvsn/jOaf2fXO5w8WfM764Y9rAX+9zMrqWs7eI332W1X/n+b315nh5In/bbz9PPs+X6ZrPpuUeGP6MMF3OdMCWb+z448vvwO8ALjS9N79Mcjyf/u3mZR4TdVWYTc7eFU/gU7ZJUUwCX+Mk3YG/k653QTArm0CDPucB+J/8vAkcRXOfv137w6in7wniC6cCYm+vsPkVwB1Xx8w+fUdJu+D7zD56+vsCDhVTRIlYGymUar6ZVpQdpMUdRO0QXMB+OIOXfAJINOn6cssKWe//n1mX+90X+vh1zsIJw8E05jthF4tAN7XyQJmHJRPfT1QNYJb4PWAZV55QL4wATD8EVimrfILQL/JWm2W5PnMTwDig+ox3GkDi36eiP36668AzOMv5QNu0dmjrLQLMOFdnNmnT0DRME+iuPtSBl5czT789vuH2X/M/qtVd+ITDxWUgae/gITCQZFnIP/6AkwDrgTOB+By99dvvz/NDciUoA4C7yZhEjwWg/jNAv/N9gee+oTgxMwNgM2BvYu3Ipd0r7NtOHuX91n/JpSPK1C//KAOSj8oQXXrYgeo827JsupmLQjSNhw+zvo2uHP91W3udS8oABA43a8ziVFBTaly8N8k5n0SWFyVCTD/e2Q8xgGR5kM7o99IvM7kKWJntdM4ddw4Tx6h8/ALqCVvywFxZ1YG1y/lVEyDyVT39HmYB0wClvGeLv00+Xwq1SC4/PaN932OM1W+470CNl/K9pkaThPcqz8QZZhFfeJPBeOfz5Bq46rP/bv9gKQTpacX/KdX7jHI/J1Og/m+u7g3A7MvPQLB2Ox/tW+Z9KA2G43bUEeOnXHyUbMe9p16rckPj/YMtAx3Zvdc+tZGvIHQGxZ/KfMEBEsz/PMx8+6V55wHvgEFfQAg2p0+kArYd6J7j9gpAptminXnS/kG+h9BENwRDjgNpDcI/ynq3hhOT98kjUEOT/ffGoCnnSargKic1b0LLDMLg8B3HS8DUjVT1j39AMI3mDLwGide/AetZoA6iBJAfwaEmJwFCsPddHIF1ATeCZuq+DY9mRwEpPB7D0gLmtngdWaCxJmCpwXZCnqjaQ6wwoc7qVkRABsDEd8t3MZO/RBm6n+fAjoT1ifB9Xv7Px99C/S7JJPwgKbjOx2w5HWCYj+4Pfz6LuXTU4BoMUXHfdEfnf3UdPZ9bfrnl/Iu4Tv6g4zPp7L+nWlmINOKRyxOgNUC0CmCZ/iAOLhX8NdHEX5U+XdZPv9Ly//D39sV3Muq/ke/fZ7FXVe3nxeLRyl8q4SvIEMWIEKSOmgfVfHTexJ+Aow+PZLw03sS3gffk/APnB6G+zz7e9L+gcQzyD/P4FfoFZoe7RIvmKL4eQHjMJ9o6xM2Pf1SasE3rwP2VQHAcXLGAMrwey16mwIKUtQE0TT5UZvaqaRdQRW9gzHwy5fyPTKeWQOwvoymQtpW32XzvSgDPz/c+F4zwKOyA7z9qc2LgmlDlE/it8HL57LP848vpVMEf38jNJUJEMrANtNuCiQVaKK6JLjfAR3Bg8SZvv9xL6jcvzj5I+TbDgjtNHfgeKbQExE/Th10CUBn2q1MtfBRN8Aey+nzblKiG+pJ6sfmaGrU3ru4f+V6z3HAw68+T6n+cTZ13B9n783zx9nbdua+Xyx7sJ/7eWrcJz3BVPDxPvd9e+sGL7/8iRjPPv4vhEgmmJmA6aFu4H/DkLsTa6cDUKlrOyBS5d27kKnytsO9Qv+r2oBhE5x7UGr9SeRvNvgmWvWQ5/e7Kt1js/rbyxsKPZ33bEzBdJDun9qp2C5AuAOG4P4RmODZ/0DL+qQIcBQ0SICkh0GwB6GrAIaQ5crHSdLDCWKJQJAPuw6ME3AQrCASw93A87EQxUjShZcrBCFwnESdJaD3CPivU4+RTFIijuMtPRLG/BXpEF6AQi7qBTAC+yQaQPgKDZfLAAMGe1+aARh+qv5QdbLre/c8mehpgd9eXAIDM3ms3VKPi1msDIfASPcWn+YNEVhtOs+Oh6PoF32Zud0arnvZGWgk3Z2OWznasswyddyrfjjJ22FeJ9HxxpUprUL93CuCtdzGULmzKqsgBlNC1eK0W43VcVQ3OFoi+rkjYFGUuAsntyPTaYd8p4qD3hUOPxfs/rzSG8nALwl8ML1cchJUITLNwOogDFMn7LbRIs73NUbepG6d5sIeRwZZRLbZyriwoWrY6braRYrhWI3uO3XJmXFeFVt5FOfwBa981cWWwWmNkcppDc/FBPEuO3KB3rxeFjY41WpCfDLRQc8N8nJuHJGlnHWxyfTyvLkMddtEnZ8fd16ab43c3OAhEiFNvj+jmt2eFUmEklOy7IfDYEm5eRRsIyyTw/7E2E6W2XRMB4156OuzqO8GrTZsXOi2y0vr1mIx7yv4xOODq28WZ1JUJVQqlDi18O12kJbNIFWaM2RHcXu9RLZaCcx10UjLbBDCxIc3N7sPVErUhxHV1gVDpcLxIp3T1tyTuCXIRmEu3NFqpOjSH5XICTdwLp7QAWX0sik0Rzuqkk9aPGYNVtbFInHUHdm66MWOupbBqZSbrRnNOVc4AYVW/FW2cD+Ozd6ig619k7ZZI+00Nm1U7lKayI6Px7ra0LswY9ChcOFrUw60ujVlmgibOGELVoR2vKu2EHtQrM43+fPmgMsWcTr3NyeBkHnu266lBstdIQnlvrxF6RJJmeueHcYqsPFQW8TqcU1uJVpRPctkVnWaeFRv97CmnQIzVyNedhe9aVaxbGgGIdkLPmQZBEdH7hqP84o61/jArxHiKnQ3gJd2fi3GU3yL5q6ndIHNHxCOXvAOHjB+kKx75RIug1WEm61xQAVrfp2Lir1czUsSMYZB2RVG48CD70LSNV5f0G1X7Xg7OJ/Vo+fuS2blnnVnVXmtVECn+RjDcLqpzYOqB5Iqp01ytJOutklGF5BIOPHbi2QTLX82cfu0N6XqfBKgKltf2HOMRR6953b5wO6FQSxunICZGTWyLrRut82VEC3p2I0H5SaPp8p0E8O8wUvrsES8s3XDo9ZaUqdISPmCuaXjsmV5FRFA2CbmeQUlMFkWiS9sNvMl7c+PHd0PXJOGZJeHq9OG95abYJn5KamoKxQX81tT7jCHgoRzIFVziM+dDEvTsxbzneFyp4jRk8XGLXs+7c5ppSOJHl0XglEYInULGDFaDFGJHNe5tjEZ7giHOZnqxk7tSnaf07ul4PGrq2wD4+f4odksSiMgs6If62JDrHz4IFOWwZ0Hkqe4ztgOXtDn4Rpp9L6m7GK17QsjvepbRmwky7SCIIDn+2ZJxKZmupS6a+F0vsMhOFl6pir3LZfou9Zgl4lD05xtbJj+hG862p4P3Gab7XZcd2bWhQJaEVeUffl6Lch1vj/W+tnhbPhQywwfHQ/rEJfbK7ZvN0vmeElpChIxtdy1tXv0W7Rlb/su3QexPJIejNnSiAYKKY67nHXmNDonY/w2p2rUdMYGXTr0MpcHvg/TzgzYKtZQqfcvNC8TOnfGm2qc8wQXmtQ86OOVLWayFofp7oIo0IZr29thTQxbDqJpakmot0C9xAEWS9JqjFXkTPjq6VJ7HllK4+pE76TFYbHfBolXtRqSRExyRhNRWFCw7IkmT53TbUQdeMEK+PWYwbB+5SDD2tTO+qZFnVhuXeNoirmGzU/rEriv4DhrRTEG1xO+ALBPpBW5Ydmy36iKbKU6Z3catSLNdYcW+AiNIyFB6dzKiMXYCHPvNMK4x3HZcM6dvR8u3DMtymI5uPaiRCJpq8mDEuMIsVhAFYuZGBn3EMvwJagOF1TFlotkLpN6OOI2uiI9aUkkKZrJp1QSViuTpHfUbp5oVIx6IW0WZiyK584QbyfDIb1gt1/G8p7Qahyl6F4UsgDs1aNV5i/kIef9ntj20kbgNry7XVOGO/rXcC9JLJQWrG1HtMDoio3XXqDv5SqTxMtQ6C0zLPFgSE8XNG0uqmyQC7lRjFTM2GynqkN9zpHbctm4FG7zt6pWOnJ9hndj0iLlaN74SDPidu7Vo4peqWwrErFVIh1Ua5DHKorlw0tl7maC5O6t9nDuT5E7rLRqDMoFUVieV/JKVzEaVRxCWiw6LNa2VjOGp51/XGrYIbnERHkitrdY0F2BkBUt4zcFfsxGups3MDzYEsHZWrQOzl5zJE0r12MiK/TzfNsYZl1xCH5OzuypO4xozMDHraDtSngjqzFnOJmLVcGJEda7JUnFo84dbAWnuLWnS4yS+UnCqDnMS0niJWzQtmgeE4yw9XoH3otO461vulRUPX7GwwLLdAlXgQLZBmIDuM8IH9KsdH+LTJOLPdngDyhrYlyD6e02qjWO3K0b7+attuuFelLO29PuditcRMtXXjrCRscaobHfgsYjgndr0ffZ1kl1Grqanh0iEAsxeRHL54OK1fxKSaSyumYLsa9uawlqnJwzF53Bxoe5yHWQwo3CRtyu2k0U7QSu4faHLQ0fV9yAHtf7gbMK3tmruNDj4RzSnNA/0+tqPedBreuVDeIiPr9VuLlBkUGFblAC49akAx/OxFWE23RvznsitIdFJ2y3sQCtoagbtHV3Q84oo5yidk6GRxvScP5Cpkq2gFsZ8Rq6ckqob5CK5k6OdIy3Q1qUjZ4yEG+xmk25LNVgOzw4IHnVsjCXtR5GX8arttzs8FtYwmtEvt5Eo9KlRroRkcWackRxMq0wgdOJnFQgrbg2eZQ9bAV44bDZcdthFLU519fVemeuPFzLbVdvOqqt0m0n4LCX763uwCy40qv3jCEVuJ1kqm2p8W5QFY6/7DV6D7l0nHuN5XM6aEwSuDfUYisKN7bheLKICV0WoohDltvoGIk9JZEZcB1DhcT+6l1JZ09HSMVePAThA6zUzZOqFLRg9n2ojyrNnrlyPyqGEhzHnsRW8+WiYq+1jtQpY3TbDPFBPtWIg/V9KbFEYUiVeNr1621wuHoRcSIKVIdvrRHEkH0+5IqF1QTNoY5mDgHj0B69Yo3k0oxbui/YEyIIxtVeHjq7OI42nGxMvIU9Vu7r8bpaVBYJHSk42vOkrefWshmlsabb1RgZTqVvte14CRiLom1Z47xl3EmDRxwBO1fSDA2PRK0OC6eRCzlTajKGq+CKrf1VEKZQHhIIuqauWwFXxtCrkCVFVmxvbG5CcVpJHq6LLTxnT4fqFlsyk9lX22t3u0uHkqjRJV1RBkx/TauFsJ1HHQb5ClzBG3F5GK8JFYhrCsnCXio2sW3qOUvnVFZYjNVfyHgOVWlS28yZItqRYyzGkzFtvVdclZZ5MiklX0JyatMolHZp0m3F7Jg1w+HADEZT400kFtaaZ8KzT9U8b4km14u8koO9egOrLBLvddRj/H0n5ax8Sm6UH8gS0yWm4JoHnksxaqSVwTM8LLKEk2bIrrM4n+ibJZnoNQpNTSNYnI7FBeOrDiVY9k4us7iaC0kF7UpDTXSm586twjjyiqesraLKl0wZmSK1q/0eZ4U1tmyVhHEBCdAZLfV5LBUpi3mxe4Wq1RzLaeBIQ424erlObU2uOAIgyDmwa2/fFLWFjiDlu9vpkpkAeNwUqsyqwsKuBriZ0PG+FTcMt7OO0tIbm022F0BnSoX50fUycRidlrpoYnZpefxmYkK7EdbtELdtCgXqwGXNBSTJLXN6+2TD5ZAzF/kA+xXWFrY4SqXrn5HeT8cL1/O0LXrD2TD0kaWGFs0sgbZDm4R4DyXL4xiOIZ+myBpW+foknNjj+aZ68I7BHbkO+Wwk+loVzgsy8cpkkJdXl1eGlvWWt40kCYcV4l6PxyYX45oRziPhojW2x3XqxDpDNURBTc+lOekt1vNNsPapQj0zutsI2jLo8XSgElxY7oPlWOdHBVus5DzaYchtXOOMsSd7ZUDizQZJNagU0DDDHQXlY/LGxohXp1d/R2uQTO2UxL+Y0LxvT/CAgSy6HeMOXXaq1tj4XDmV5YJhnZRdH0x0seDUpS+y9KZFEFr2SJl3COq21h1jsVNDo+eWi17zyursjBHftmN5oBf79CxfdM61QpbMZaw8Rrcbv2rLLZ8z+MVccviiNfWbErTenkVvg2fSiS0wBMjws6My1xjN3M1ezBpjMJdXfGSVhivWWWznboCSsofybB2mBrWYm50DO4cQTUHJCwJleRAsvtgxCp12MLIhmWN1spuNXpXJfK15O2tVo/AtWnIdOSyN/ck9dqv1HgJ7DJ2XkUubN3N3Dqc3ldZygjMLsHXYcicCUxAUbfO9j9gLDYI49YQ0vLEGm9UlfFh7XmEhXWObpxiq4Dl+FXY7sNG6DWM7zNU+MI4nRcbRzeJGWCa6FubiGdfLGwVlViJrGWIIOy68KCrpya4eeZu9CsEKemmSGOvSg2FQzKLYnZuY8c11GG3iBsQ9jtCize3Pi3nKuIHgYbFHk4LPXC6KrV/z7lizC9NXFmE/d/GLmtNDYjAYq9VIEF9F8prc6kpYGBiLUzfC3MN+vGhaGrd3x1YkbnNivmzxdCOE1368HF3e7/zEMbHEQQIMIraFjQZel8NDb3dQxsmGZ18bFKOtfDHsqIXv+8fToKMXdBe7S41NjjImyV3a00VbUogus2HaiMSOvtoGipY4GnlekyzthDxE7MgXrIUriIMsFZ9ucLXtO6erbhY837Gc4ldaw0LGSYXsy3qLkKDCJWTNrEZIvpBGIWCUZKaL69lHzvvYK7fDPGMiXmzOjIs4bWhifcBtFhF7crvFZh8yrLWAL/vD4Fgr9GT1yxVOkvqWcueWjYV8DA9kx5PCibjcdgq6qAOuF8zCX3V6hBcnrXDbVc00UEP6F3+Bx5qxOChLt9iiKlT7R42OYjKKjxgFY4cKziQyGU+wjhO5ySfyRncQdxjALnsuKbpziK6Dnneny5hlmMIdRDhxNQ11VZvIe7yiN6G+T2VGIYJM7jbasL2wypk+7vGOoFSYNm87TDzqbenvqLUh9SjZJFB/ct3L8eA7QZ9Zl6za0Le1D6mFBR/3JMNeB58fjjqO6SqU5p4SUSeF29meA3Y8S6+vQGthhLysSUNcpqD809pqh0BErg3FqkUqXGw70qkHY4XopF0goD3qSNqNWhS60OFm1Uoe2OoQZIofeGnnzy97xw0h++RLdMFYqONzbgXxSdcve0EV9udziJn1oWvKIOWpcoMRLWtQ/Sp3u0vFcIO8xm57xr80w1q5rffnqmXEUZuzbZ5hS2eOj9iuObsmtJJLAZEWkVILwibsmIqiqJ9+evn4Mh3BPk/D/xvvx6dzxf+x483HSeTbe7P7sXTg+J/vvD7/d4T85eNL4yVAxMcxb5v30fMI9D8d8n76+29gJnrD47X09Arw1r29auicaPoZ1ktS+n3bNcPXtsr7+8Hzxxe3b6cfgbTT74Q88PlyV7yopxP3uwjTp18kZTK9MP7aVV8fp93By/QjjenNVgAw6P02eh6Ef3zxB+DTSXeUwL8GTT2p/nynM50WTy91Xn7/v5BsxebvJgAA -->
