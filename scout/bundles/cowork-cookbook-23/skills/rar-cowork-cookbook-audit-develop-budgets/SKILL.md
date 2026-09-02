---
name: "rar-cowork-cookbook-audit-develop-budgets"
description: "Audits develop budgets records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_budgets", "rar_sha256": "3a0291a746a37eb3a42707054fdd1a7100a1a17c66bca3ddf0a79c694fe44170", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_develop_budgets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-develop-budgets:1eab232d23cd40ed4ee1dd61a2958330f749e56322fba54b8e03848b1b854f32", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_develop_budgets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_develop_budgets_agent.py` is
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

Develop budgets Completeness Audit — Audits develop budgets records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_budgets_agent.py` and embedded as the fenced Python below (sha256 3a0291a746a37eb3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_budgets_agent.py` first:

```bash
python3 audit_develop_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_develop_budgets_agent.py   # or on stdin
python3 audit_develop_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop budgets Completeness Audit — Audits develop budgets records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_develop_budgets',
    "version": '2.0.0',
    "display_name": 'Develop budgets Completeness Audit',
    "description": 'Audits develop budgets records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-develop-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-develop-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f66daeab2a0ff1c7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/develop-budgets'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/audit-develop-budgets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditDevelopBudgets(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDevelopBudgets'
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
    print(AuditDevelopBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/7V6aZPiSNLmX2Hz/dDdL1mJTgQ1NmaLJEASCIEkdNDVVq0jdF/oQlJv//cNAZlVPdM9847ZLmmZgBTh7vG4++MeofztxWrqIC9fPr8owMomWytJwgCUEytzJ0x+y8sYvuWxDX8nTp7VZWg3dV5WL68vLqicMizqMM/g9FXjhnU1cUELkryY2I3rA/i9BE5eutXEy0s4Py0SUIMMVNVdQZEnodM/rodW5oCJ5VthVtWTsknAJ9uqgDtxAuDE1RtUCDprFFC9fP75l9eXEH5++fzbi5NYVfVuAPtQTz+0wzmJlfnwZtHDVWbwewFKaEoKL7nAmzy//ViBxHud/Pd/xzer9KufPn/JJs/Xl5fxR26ySR2ASZ1bVT3aZBWWHSZh3b9NVsnN6seF1k2ZwXVNKghS5r89Zn6TBEH5+3jvx4eSN2jgj19ecmiCNUL45eWnCcToy0vZjJ/fRinFjz+9JfkNlD/+9E1O1dgRcOpRGLT67evz+1MsHPhtaOjdtf4dSn04ywZfXr5b3Ph62D2uE858eYvyMPvxIbgo8xZko1t+/OmvxN6dk4RV/T+S+/NDcAAsF67pafhPr3eQf5lMnwv6kPnXagvo1v9kJXD4u7rXyROov5J9x/8fRCchjNkPxP9U3J9NmP598vNfru1fTXideF9eWJCELYwOOwGfJ799VY5r5ucf3G8Xf/jldyj634pR8qZ07hK+plYWeqCqv379+YfqfvmHX37+oSlgrAEr/dqUyZ/J/DNc73r+gOBz1I9/nAv1n7M4y2/Z5CPSJ7/lxf8qf3+baFYSut+uV58n3+fL+JpOxkW8K31A8F3OVNDW73D86eV3SAuQPsrGud+GWf5f/zURQ6fMq9yrJ4qTNyO3ZHWYgtF4NQirifpM6l+VHb/fv6XurxN4dUx3SBFWk9STbWmFyQTmw+jxcQW5N/n1fzt3evzkPOlxZo0E9PVJgF+fBPjr20QNoK68DP0ws5KJvDoeIc2BrB61PMitST+1oyJoRPggGpnhR5KpIA3+bfLrn0r+ehfyVvSjuV8yiD+kTiihBmmRl1YZJv3EGvnI7mvwCXIn5IwyTxLbcuLJ+Kcp3kYM9ABkT2QcWAFAB5ymBpMkd6C1Xgj59hU6t8qTFvLfiFcVh0kycUNI7bAS9Hcmh5h+HoX9+uuvkLWDL9mDcPHJo0RUMzjgw+DJp09FCbwk9IP6SwacIJ/88NvvP0z+z+RfzboLH3UcId/fQYJBm0wERTpMYAY2KRxWTUb3Q3q5e+i33x/oj9ZlsKbBvAm9ENwnQ2nf3D2u4OGSd3/ANY8mgvKp6Y+4TW4BxGUS1hAtmMvV65dsFJHDoeUtrMA7iI/JD+jfHfzQM/qkemII/eSVeXofe4+00Zlj1Xyb8N7kAym4XOjXevRokMMS6YICZC7IYAGtA6v+5sIsrycVzI/K618nTQWXOkr+1S7vpRWkkISs+teJyBxhPcsT+GcE6K4ezs6zcHT8M0Ifl6GQ8gcYY/S7iLfJAQZjOSms0iqCEtbp+zjPekQErGPv86Fwa5KB22Qs12D00T1z75HH/kOvwHzfH9zL+eRLgyEoMfn/3VyM1qy2W3m9XalrdrI+qLL5CJ2x5xlX8miTYMG/K7vnwbcm4J0v3pn0S5aEEO6y/9tjpHePlseYBzs1JVQur+S7/DFvy7vcsIY+H51YlmOcWl+yd8p+hTBCxKuRfWBqxmOi5x8Kx7vvlgYw/8bv38r3E6cRFRiok6KxITITDwD3HtN1UI4Z84QaBgAYsweGuBP8YVUTKB06F8qfQCNGf0Bav0N3gJEPW55HGH8MD0cHQSvcxoHWwtQAbxN9jFQYbdXEhp68jWMgCj/cRU1SADGGJn4gXAVW8TBm7EOfBlpQahvCiPoO/+ctGHNjZYDaPhIKyrRcq4ZI3qALYL50D79+WPn0FBSajtFxn/RHZz9XOvm+svxtTCpo4Tcih43zWJS/gwYycZk+YhGWy7iCaZuCZ/jAOLjX37dHCX3U6A9bPv9T6/3jf9ad34vi+Y9++zwJ6rqoPs9mj8L1XrfeYIbMYISEBageNezTM88+PfPsD8Ie2Hye/GcG/UHEM44/T9A35A0Zb+1DB4yB+nzB9TOfaPMTMd79ksngm2Oh+jyFFDLi3UMa/SgV70NgvfBL4I+DH6WjGivODRa5O2Pdqf/D+c/EgISY+WOdq/LvEnZc0+jKh6c+mBXeykbOdsc+zAfjxiQZza/Ay+esSZLXl8xKwV9uSEbKhEEJIRg3LzA9YDNTh+D+DS4F3git8fMfd1fS/YOVPIK3qqFtVnmngGcyPLntdexkM0gf465hrAvZ943MaGvdF6Nxj03K2DB9dFP/rPWerVCHm38ekxbWRNj5vk4+mtjXyfu24r49yxq4r/p5bKDHdcKh8O1j7MeG0QYvv/yJGc9++i+MCEfCGCnmsVzgfmODu68Kq4akd5b30KTcufcCYxWq+nu1+udlQ4UluDaw/rqjyd8w+GZa/rDn9/tS6sem8beXdz4ZPz+agUeUwQn/uksbsXivrl9HadY4595L3aG5O+irBWNhrKLf3fLHluDrI1JfPkMGAq8vcPIYJ0k43HfDLw8ToO3felQoAXLJp2rsCmYw0aAkWKuL0e4Y8uB3CsbLoXsfP374/OeN7T+SwmcUWDaGYy6GOy6BAJcAAHXdOWphS3KB44hHEUtAznEM82yLJOwFQPAFsbBRe0ESHo5BzRWMjtR6ap6hI9bQ5g9A/2cd9stjEqwVGDmHs3ALwZaoRRFzC6eAjVsERiEUAnW6LryMIoiFWijlzOe2Y+Gu6yEWtXTmS8IDBIFSd6Ce7d7Dkq/vrfU7+g9C+Ap5Mw1HOzHLchYOhRLukrLmDsARG3cAiqEuhQOEXOLeYgEIOP9j6tMDo4Meix0DEnZ6sM9qRz2/PT06BtmcgCM5ouJXjxczW2rWnKDsLjCm5RyYYjSNVUXduUFlxPt6gzbNwerpLtobKn/w+UFYOQqQEoW7bo1N4u4FhuvpY6p4V7fRVrFsTdWijeUbESdD1V+cGS4FpytjHmUR58Nqt0mcAqtly7gAW6xFjeENvZQGqThr06meZVMkG9w9sENdOV11qzyVm7i9CNkVVHt2d6EkdOi9w1rcU6lYO9oZP6eXiDP41BDkUDWkoD8MBTFrqY7wWjslgpQCxyxdtM2pdWOeE0m60neLMrI2cW0AY6PVxdYU9nhcifh1a3dnDJ3rTSKx9lm5RJ1rTEMXI+Iiu+kUE6jXwiKAva+QmuXCm3Bxot0uPbW7gNYVv+TFQ9kbu/m6vFpi1TVBzXR9EhjC4UwasiG6pZFPD2jXzrmmCING3s63dRT7ET/0rdmHm9KUeZMkHb93TwqP7RY9b5SbsMPPZpoSxIIVVC1L/UFc09iOM0ntaPU+N5DpFT1XKlol6UnHhZnOeJHDMBqzrLFtvLwMg743bcSl+CNlrreCvXKxNEesDlSHfY+kQemjJUfLbXEIUfdMHdGBwYhAb0Tldhp6dntGqQ45EfMBPXZ4fe0IZ36hfQUnV22qHgChRuQ2i/dbv96jMckF0W4pdAsb051LlB51n0VNobZ1KVlkC708HCrZkHSMxfPEEnyRMAGGTA/5rSKOwhY5SmHDUx1HNotN1GUDvt0ER1PsPEIXS6A4GqIpxXRFlq6r9LhZXItde4mOa1y8we6Q6UTemYX0PgfAOaVlyo+/1+LQz4vkZhC2hCG7IXUMassRPNevEmsZ85Wf4fKM9yKSmrZ4ZaO+Y5hXVjI2aAV0TWDxVre7TEq2fXlUHZvICHDF12l04bown++P7s1Qhuic7MkruyUZgo5vMwlFNkczD3RDWJEXhM75oMKHPOUtBU83V1QUnLQy9z6tR9ael7HTudIOmNTzwcpHRMwT/Ntpv+lxIcWEhCVS+ori0nSj+a6HbQ+id9Qr2uKz1Tm8ENtOmmqIfHO82LMXC1S9is2R6jfHpcSvMIEwtPx6nMuIdG2X1nzt4gTWDUI2nxF6c0RQOQoMUYqniG/oZ1SJdm7FHVxrnVXymvHodnYSOcpN5MuUSC7TA2+ivCR1+kbmzheC2mVrQS9oAZD7aUtoveSUVy5M9TCnFtNZdFOuwa3lzqKwvC72tQJkPXWsoJ5pGb26Xq+nmxkfbGwouTW1pEMDoNpa4PhyEfQX6+Cfc7oXczVnF0uWIvyALNjrsOuMYE6Ul+lNu+GrYNpxwYyUdw3no+bsZnPhfBfoxBwz08sSyYRk7y8JytyUp9NWQKviRAUhXacidtBiyeyrQY301CxWOnMld/nOUHpTXO2HQ2RVq0EJwsZtNQZLg0GnjuSu0LRTdqxsbkoN6nLWpeYW1GJdEOxtDqM6W8rstURxuVnTN07FhwVs82mXpNPdzPTqdO/ZYs6fSkPzfe8IEQ95ze0VySnOoSIqa9OaLpHVUV1v+3PLWuhBuq1m0rDMVKqLG/G0tTe7rIuuS69dJQcaHIermKJVvz8u/ZbYgNyhhW6rWluM4e3ZitYWZnSJwdZgufVOwRZro7WPhVAsMMm1dXqgNjlJ54qExFpanNW1ThbIfm0VEN2Vo9GKd0CQ22m732y1BEbwfm9uY/WKbYLdas7qbDFLyQ7dD41UhZITz2d9uZk6xh5deut1fJZyXY85Y9ai62QbaDNjqm6WecT4DJARTpod8b5caTK+dw6Yaa4Wl6NBOE4OU3/W0fNWu03Vdkg4J7doWuOOvadrzioM1jqf3GjV9Rbxbb+KJVKv0njw6TDEjvGwCi6tc9gQ25I2rjurE6/YuFFYGxzgEyccGLm2UBqjC8VdO4U1Y8w8QmWZX6/4aYQuhnkRXhqawtxiy+jCbYOe+NXlcKWj2/ocX0HqOKSxNQC7kJJKsUh1qnae3eWCzOBag+7XPeA2B3FtO2nJKojreFu6EV2ZdfDcIpOkO85qiV93YYObl9UJC1qmW8N21FP4fkdtDGxp1KnQ7tCdf2pyxDfzYnEusvUJGUA51amd3XABo0zx9Ozl1Hqd2GsUYIJi7uSA0q42bl7bXTN1M9K3OPGa50Jfc2ne7K4kv1c46hyW+T7f7LHLPjIU/JxltM9EascoTYMo28ARqwItNRM7KJt2aJkA6YmaBwi/SGenc9SeOX59CWKUy1paTKisd2wZUpbRM1YybNhFa5F+xe8PnnHuL/OFmq9vN9fCYHugYWm/i3ZDxKxph1DCy+Hco3NLQsObsz5eho1hrVQeX5PpGdvR3oAP13DTQ/kJEl+8oi1Jvd7rZnLu5vtZgNoCXzhwA8OeGMQ8kxbFKqij14ucE2wtzcMIS2TMQy6M6kN/bdrYohI/RtzNQj+Jt32hscQWKfU177Dh7dKcYbE9K7KMrVUYDHVFn8TgeF7YgCVIanee1QwMZSuE1W8WdSfbUG/LGt8GcWY51/VGOBus6Zq7aVf1peaa2U7b+HvPA201gIYeXDO29i1dpjRZH1HLYCS1FUnb0M2FTHIt5TdIi1aHwdUjpjv2TYZdV1pirbmA70MP8p3lnk2C6S6r8uAkKUHqDLYptlxzq9fBjeV8LbrujbKnpCuITYfQrGElybZ5K84pfrHlNXuy02wXMUkpBLxybZ1EiqpOlWyfE1M8PE6tS+efCqe/cIwkJTS9TXg5UAXUzOS+ULpzvJnzEplGy6tSXbCdsoz8acwemG4VXz1ztwnrstIUU2nYGXOyjlUByNaKQt660DTFr6l5UWm1o247pmZWgtQNU3qKspKfrNnrygG3vSXTxtwmcd+g2NKxEVO/OA6j1Fai2rzDSL7iNBySXG0+zVSEP85mCxGcIXFtcHkZMGk0DEx0HBhCFfIQzXauKu7I01nywO6EX/GqIo1Fi5w3Q6WBAr1YesqY5zrv1qjuKAdwPpWeVLCaJqB2tzfq0E0Ou4g7hFLmmimnrjbuYo7yW7uy62TTcjgZ6VHqYOKWmR0lY6fypbMUVdRKxFQjglV3jKRaLE4iHWsLpw8ujnQpGwkX6Vo+WKKtmKKtY5uLSDVdtI313XFzwGxgGAguGNOqpk9HRgFLWHZQ/nqyAezbggMfHM6hsUxPSk7K5UJvUrmT3UMdG7fi1HJUs6EuM+Pkd1eX2FGKpC7iaL7FI7khJFUzS4xvGZMVT3kqRpWc3JDdvo8znjWZeNDZFQqEIxuL+TXKC18qne4UrjJVWcsIm+ArQ53yGs5FdXQuNOemHBi32LCyeSpU2K7UmnwozrXLF83ZERYF0sWO6xemsqiYuZ5cwVQMpTlHyi6/QxmkP2+xRcpz166ozhWDnA/6Io2Pq424poROo0JsZmHh1Wqk2alhr715aAN/ueHWORezob4ktKRdVa2oJ8vhJl50wbU2sFp3faCxqE6zbdMHK4TfZCnGc10pa2uM58XcqK5nkbvQx2kN2yp5vjNEXpWnFmTEzM5TJZDP8g7rlKjTXf6GnuwrKlyvYnZwaLC9Bq3unrTeAnyJMyxn85thvj4aSCVgyOVUycwtbzSaZeyCjYFpontnF3Oq6HuLvNb1DcnsKt4zkVttUziT9CpRnehht+2x4yUi/ThxyUYYXHU7GD3AEqF3qkjaN+ftyWCLEzo/UbOoskDFbPeHojcq4cDKQ1lxCB6XGaWdplxD58djcTLKWX3hkNk2bXPVbvetlhhg1mGohjrLeIldEmzpzzF0FsVsaayKQq2GaGu5SEgepn4R9VtYfVciySmkickbiZ7TbTfH7NliuqKcitZ7xBy2WN8vWY2ute6s5ZXFELMCwP4bW/bslXUucscaPjN4SSNtUzaPN8oW8+Klott+V1Y0QUWCjl1TuLFmpgl1krIEX0gnC+udzFRg8TwcsNbrYnJzpQ2cmjLGUsawM3F1ceO4MLyNzxM5FTMz/ModYgyPefZKpk1XIGS1LsPlbrVi0wtIIQVWBuZMeTVOT9aiqLbBQmlmG6G4EKGEqDF7CxY3m1bOEbZnnCzTJZ7GD72jyyHJHyzSuKAo15q+bR0InnYE0otg2Dm+HoTDjjiJ89bn8Iy2YyTwaoNdNLprD7ji3ewlQAF9xGTfM1KOYVmOqnOxkTMxGJSDYGrKEmbD3gSI3U9v053Oktau3dcFBqrc2nZoGTVzAyj4VD/WpngWzroVVEK9EhVhPR2OFkXslFaimlmhWEx2pTTY02iIWtFIoQsDpJehKvfm3LA8l1hH9TwXTMrFLgaHt/yl9GMGGbALQtR+r5KRNm9WkKH5C9+t95eRHrolcfRLfL5jbuIKnJAZCECvKwnKaQgvTLdWPqWEnkgGWhOV1aG1boK6StbZdXZRjY43tpJviD4yxxgNVU4SbFyPy9ORi7r5hreC2ZkVhLN5QdNmNlc32e3EdEVAzc48sznKc93TnG62d9g+BJnXZuEyWWwut/hwXHTU/lDB7W2Hdxe7OmSbuZrkwSVzYCIZ9u7S4OIZJHFc+kaNMN0eiXV5Ts3nYRkvW6kxthQRcuvUHZBDGQBar7KjbqCsF5W7+R7cNO3mZT5nE2YSLi5hsFiv01U973qL48obiWzLfdPfPI0TzW1modaWyQ8KPzicqjmeDNtD9nA8rTbJTIlorth4l5UJKavb7skNPmhFCNM6YgllJwJYqtetrA0XW58SgTpb1adlW/Usgdhcg826jTMflkOTAWdGHY6gJQMcnXp79QjOdOtWcKujHoT5jDI7Vd0uN3PTiliqqUwJuczNaymXyymNz9pVCGdTdGoOl2nCbfKBC9mW2XA+myWCjfFDgK8XDV3i1y27tZwKl9Zn/Dh4BHKR853KCUrSObOZd8p5TeD0Tbth4T5xoHiXdZVKT6OQHLu4FTpfxxpprABipYHNzuHGRTitzbN5UOYVshD180CBaXNUyTrAlu4BK+ypHCJKbXprAz9NqRClhYrwWIHfx6mA9yKesclq49+2zk5jEIzZ2nNRKTSvt2HjnpXJwNCHc0ufsNa8cpaK3KwiOQsXyio6bSHdbgcWWXl4ozAZfcHjlp61cHvjOOl2TkWkyol7MDPyHechhWGLUsqa+NxdUznCVXUTzmCt9A2txeMUWRyGFgSBGlUuBMqv2MTk2tNGiC2lCM01dTzteTfcB4JMbtg0St1lrPLWVmJAwE532+kuPhTkUfZu3Ol4PYY7JV6tVn//+8vry/0R7stnFCFx6vVlPIV+nvv/23Ngfwjh9cd0nCKJ15f/d4eXj4PE9yd/9+N4YLmf79o//xvLfnl9KZ0QWvE4Lq6Sxn8eUv7DQeynPz0RHqf0jwfM46PIrn5/HlJb/v2UOszcpqrL/muVJ839jBqi2FTjv5JU438bOfD95W5+WozPC+5a4LuXl8CxqvprnX99PlYIs/HhGnBDqwbPr/7zBP/1xe2hJ0Kn+orPya+gLMaFPZ85jae140Onl9//L1K2y1L6JgAA -->
