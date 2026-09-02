---
name: "rar-cowork-cookbook-audit-consolidate-and-eliminate-financials"
description: "Audits consolidate and eliminate financials records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_consolidate_and_eliminate_financials", "rar_sha256": "6964711aa692de3abfc84fb989ae34a461863af5d63e00e8204b6a583449d291", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_consolidate_and_eliminate_financials_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-consolidate-and-eliminate-financials:8ac02898e074a92c9e504b071b9c2da41a344d71d7d5a2c39c0daaa135948b62", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_consolidate_and_eliminate_financials`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_consolidate_and_eliminate_financials_agent.py` is
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

Consolidate and eliminate financials Completeness Audit — Audits consolidate and eliminate financials records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-consolidate-and-eliminate-financials
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_consolidate_and_eliminate_financials_agent.py` and embedded as the fenced Python below (sha256 6964711aa692de3a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_consolidate_and_eliminate_financials_agent.py` first:

```bash
python3 audit_consolidate_and_eliminate_financials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_consolidate_and_eliminate_financials_agent.py   # or on stdin
python3 audit_consolidate_and_eliminate_financials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Consolidate and eliminate financials Completeness Audit — Audits consolidate and eliminate financials records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-consolidate-and-eliminate-financials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_consolidate_and_eliminate_financials',
    "version": '2.0.0',
    "display_name": 'Consolidate and eliminate financials Completeness Audit',
    "description": 'Audits consolidate and eliminate financials records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-consolidate-and-eliminate-financials',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-consolidate-and-eliminate-financials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0ec9840f8ea69c87',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/consolidate-and-eliminate-financials'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-consolidate-and-eliminate-financials', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditConsolidateAndEliminateFinancials(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditConsolidateAndEliminateFinancials'
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
    print(AuditConsolidateAndEliminateFinancials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZPixrbnV2Hq/WH7Ud1oB9UNR4wQktDCohUJt6Na+76gBUl4/N0nBVXV7XftN753JmLo6EJL5tnP75zM5Lcnu2ujsn56eVJ9u5hxdpbFkV/P7MKb0WVf1in4KlMH/J+5ZdHWsdO1Zd08PT95fuPWcdXGZQGmU50Xt800pimz2LNb/07Dz+I8Lqa7AHwVbmxnzaz23bL2mllQ1mBCXmV+6xd+09xnVGC6Oz6ex2AGoBPacdG0s7rL/E+O3fjezI18N20+Ayn8wZ4INE8vv/z6/BSD66eX357czG6ad6nobzJRhce8S8R+CATIZHYRgvHVCKxRgPvKr4F0OXjk+cHs7e7Hxs+C59l//mfa23XY/PTypZi9fb48Tf+Urpi1kT9rS7tpJzHtynbiLG7HzzMq6+1x0r3t6gKoOmuAMYvw82PmN0plNft5evfjg8nn0G9//PJUAhHsydRfnn6aAbN9eaq76frzRKX68afPWdn79Y8/faPTdE7iu+1EDEj9+fXt/o0sGPhtaBzcuf4MqD6c6vhfnr5Tbvo85J70BDOfPidlXPz4IFzV5dWfTOn/+NNfkb37K4ub9m/R/eVBOPJtD+j0JvhPz3cj/zqbvyn0QfOv2VbArf+KJmD4O7vn2Zuh/or23f7/hXQWgzD+sPifkvuzCfOfZ7/8pW7/3YTnWfDlaQNy7Aqiw8n8l9lvr+qRoX/5wfv28Idffwek/49k1LKr3TuF19wu4sBv2tfXX35o7o9/+PWXH7oKxJpv569dnf0ZzT+z653PHyz4NurHP84F/PUiLcq+mH1E+uy3svof9e+fZ4YNkvfb8+Zl9n2+TJ/5bFLinenDBN/lTANk/c6OPz39DpACIErduffXIMv/4z9mu9ity6YM2pnqlt0EN0Ub5/4kvBbFzUx7S+qvqshL0ufc+zoDT6d0BxBhd1k742o7zmYgHyaPTxqUwezr/3TvMPrJfYPRhT1h0ut3QPkKYO/1AyhfvwHl188zLQIClHUcgofZTKGORwCHftFOrB8g2OWfrhN3IFn8QB+F5ifkaQBc/mP29e+ze71T/lyNk2JfCuApgLuAbOvnVVnbdZyNM3tCLmds/U8AeAG61GWWObabzqY/XfV5stYp8os3G7qgpviD73agAGSlC1QIYgDWzyAMgDhXgJSTZZs0zrKZF4O6AGrLeC8DwPovE7GvX78CyI++FA9oRmePotMswIAPgWefPlW1H2RxGLVfCt+NytkPv/3+w+x/zf67WXfiE48jKBZ3y4HwzmaCetjPQK52ORjWzKZAAUB09+Vvvz9cMklXgCoJMiwOYv8+GVD7FhiTBg8/vTsJ6DyJ6NdvnP5ot1kfAbvM4hZYC2R98/ylmEiUYGjdx43/bsTH5Ifp373+4DP5pHmzIfBTUJf5few9JidnTiX384wPZh+WAuoCv7aTR6MS1FfPr/zC8wtQfdvIbr+5sCjbWQMyqQnG51nXAFUnyl+d+l6X/RzAld1+ne3oI6h8ZQb+TAa6swezyyKeHP8Wto/HgEj9A4ix9TuJz7O9D6w5q+zarqIaFPn7uMB+RASoeO/zAXF7Vvj9bKr1/uSje47fI4/+O90H/X3HcW8QZl86BIKx2f+XHmaSm+I4heEojdnMmL2mWI8gm/qtSedHiwaaiDuze8Z8ayzeMegdnb8UWQwcU4//eIwM7nH1GPNAvK4GzBVKudOfMry+041bEB2Tu+t6imj7S/FeBp6BwYFvmgnRQBKnEySUHwynt++SRiBTp/tvLcGbnSargJCeVZ0DLDMLfN+7R38b1VNuvdkfhIo/5RlIBjf6g1YzQB2EAaA/A0JMTgKl4m66PcgR0EY9Av5jeDw5CEjhdS6QFiSR/3l2mmIaxGUzc3zQLU1jgBV+uJOa5T6wMRDxw8JNZFcPYaYe+E1AG1C9xiD2vrP/2ysQnVO1Adw+Ug/QtEEQAUv2wAUgs4aHXz+kfPMUIJpP0XGf9Ednv2k6+75a/WNKPyDhtzoAmvap0H9nGoDZdf6IRVCC0wYkeO6/hQ+Ig3tN//woy4+6/yHLyz+1/T/+ayuDe6HV/+i3l1nUtlXzslg8iuF7LfwMMmQBIiSu/OZRFz99l3yfAKtPH8n36Vvy/YHDw2Avs39Nyj+QeAvulxn8GfoMTa+k2PWn6H37AKPQn9bWJ2x6+6VQ/G/eBuzLHCDQ5IQRoPBHpXkfAspNWPvhNPhReZqpYPWgRt4B7145PiLiLVsAnhbhVCab8rssnnSa/Ptw3wcwg1fFBPne1PCF/rQoyibxG//ppeiy7PmpsHP/X1kMTSAMghdYZVpLgTQCjVQb+/c7oB14EdvT9R9XgIf7hZ09grxpgbh2fYeKt6R5w8DnqYsuAMxMK5ap0hTfN1GT+O1YTfI+FkhTs/bRyf0z13tWAx5e+TIlN6iyoOt+nn000M+z9yXNfbVYdGBN98vUvE96gqHg62Psx6LW8Z9+/RMx3nr5vxAinoBlgqKHur73DTXu7qvsFoCjrkhApNK9dxdTXWvGe/37Z7UBw9q/dKCie5PI32zwTbTyIc/vd1Xax4L1t6d33JmuH+3FI/DAhH+jGZwM9F7EXycW9kTo3rLd7XX32qsNAmQq1t+9CqfO4/UR0U8vAL785ycweQqeLL7dV+xPD7mAQt+aZkABANGnZmo+FiAhASXQElSTMikA0e8YTI9j7z5+unj58077byHKy8p2IWRFrnxoidkk4pI+DmEOtIQd0kU8G4NtFMO8JewtPdxGXJR0Ic+2bRjFSWzlEAgQpwFxlNtv4izgyStAkQ/T/1+sA54elEBJQnACkCJIAlvCsG0TJOL5qO0E7goLHHJF2j6K2RgBrwjUDnCPQH0I8lcIUIWw8RVQgfQQEp7ovfWfD/Fe33v9dz89IAYIl+fxJDxi2+7KXcKYRy5twvVRyEFdH0aAPQALnESD1crHwPyPqW++mlz5sMAUz6D1BI3fdeLz25vvpxglMDByizU89fjQC9KwCVRyhsic34jAKhOSF1RQqSTOgVi9iGNxWaSpm8x7KIUZjKAEK426NSX1Us5ZcN5kG5wqbsIRPZgFlQT6FUitJgotIOR8xIPOpdcp03dxNJonecTPRnhk5ufxoJzwq1JFBonzRZ4j+mmQtL0SG0N5c5e1wToNjJOLxiSrrO6PtHpS5cvJruULSw3w6IkSszop1wLqXEqA4GyZd7lY3nZWh7NxJu1jEYd8tvSOS2zlmRm22JkZPB9Gwr3WBcYjVrfnaZxqTuKqTmw2bU3fZI1WWCepYJGZ0iz6iyvlXasaTNEvx1xtun25aNetuYv2c/rm6Kqh1+h2gIPc5MPxFG3Y7Bz5g7B2BVGVmbOSdf6ImzJ8VgYyLUvJ6tyzbowhuTcgY9he8OVx47nOPBsvWGXyibc+KYSqMOeluTtrtJGK6U4nu369KyvGufpnRjIuN8uJD5qmr/x1U120pXzm6E3CSo0rgiZTlvDVzbAviGQ7wjllScKDqQRD5TKXA2cRVUfDbeAoHawlIh/HgXdVhKqrvYLBMWnZZlbtaVRJTgc6nqe5ZMJaSpqro0XHhAKwlz8Pm2S1TudIui18tfJPtwZBN4UWHuhTsONcQrmaoxvw+iqydKmaHzaiu9LMCtmH8xENd83SISzBkE/zFsvd4brfN/ppzq3WpnW1K50n+HHA584xqhgWayjezxh9f9vOLfxYhF3Q7GxChgQiOuwHGs+ssb60NKEc5YWIXy+y6RjsqWIXe9wKsXyZjfxJSDZbRK5IYdCKHURYmrPRnF1+485tvtWvjVTZDbVIGv26PgQiHSiiH108a26UeRjdjIW1p6X8HCySzZLlu0QktzbHuuYJxgX9SviD2eXMaEpqsyCzMr7C0KWxzX2qiebGDcnFkPCdoHU7LiF7/cw2voSd/LDceJZoDDR3O12ua6TIfIMZEtEme0+t1k4I1+uSJnRFw3c8FHvNuVNGhSkppjkNGAjZNXZysd0B3fNb5gZWowRKXa6JRIzsucUZOB6UYeyVjk/tBlLbk2sfMnZX6k67Fa/mUScKKTmskoA0gNInrpA2hJcFpIls7BUikuk+wXabBYSP3RxOIvIonxn4SPOBLEd2JLRHzky6va0ifEdZYTaHbsdVp0L1vGydyqGHTL1cwKoXM8bkph0shhpFA+I3iyt/vh6auto2thxby/mqW88FVsbN5MIx3RCwSHXkC/Owp8ZFvckjM1MEy1W5m2+IcatexQU3Zmldqgf1qkrrzFoqKkUZ0RphmE2NhR4+bC6aOOwUEatNMr/hF5dxhEVnyWqlSJEeIFItpVzf1zvyfPB2c3zDID7PpV5DwyV/gTHa4KAew5zzbR0alVTspB2CZVkm5kJFd3EFpSeVZnY3Z5QkxOl57wbPy1N6c/ZOs0hrGdqmmjnfrgNugMj2lo8NbJ0ds5farXX0A5g5XK6md1iSKwC1uRkEi25LBVc13lTDCioZrRnT5LI/n8yBSBNi2KIJdKzPu/i4OrrnHTGgPdyzp4N83fD0XtJ3x4MThwWKU6tdJtSixifGnNwhGkswVYH26h7L5kannYOQOSoCa/BrRYbEsC07JwgpMmCVcLxKAkbRW0H2ORiNYThdjc6am0sMTAYlX1XqAUqN/KLb0Amvxpq/VOS5BIZfm8EBgnrZrlnOqKIB3WwTLtUuiBAdqVVx2jRJzt7Q2607NPHBTYnFrRYG39RwMjhd+4oeoYhYEKiu6jZrkh6+M5FwxyvkKEY4ii/mwo4rWxje7Jvt5ijKOs6uFm1eVMT1uN4uej+QziaOJB2zX1NLNMcPV7GjtJ4uLmlPWWgyp+MwW2s1wImLs78cYcyVQeanZk72kBnGVykkHGjbkMdlg15R2/URsDzBGL2QeaOJd6J5XuYsvs5in1EHp6eDJoEVxdhWu87ladTuL+dwec1wuM1Y7rCsyuJkM0tZc+v+dFGIa7Zc+4mKRylmdIo2bBPlBnGQ0cESA7Ftltd052tGVFmH+bGUc4oiN7J54fAsEw5Oe+C3bdyhVrUukajEY36BZgSkpEbC+h3poxZCXGxxX+X8WuRYGfJPusoV27mXH13NyxyVSWICMREpqiR9y553N67ae0IfVxfGPh+rQp+z8EYMvUslN9wNbgyixOKQ0o35qMBCZa/Zgy1252xpyD4kHsRgsxVWB0xJD9s04Qtvv44tbxcHhc2IYswt1zBvn/mYKjVo0xo7SzgrgcMX0mEPF3nvHi2FCvUBFMAhI4KdGMU3C127c3dhrSgVY3UyEDoXv7VjOnYln7hbDmiuiJR4UUFjBbHRbeWuz7fIIVjpgKf7Vnfme/dWD2WcIYNb5EvoLF9qZ1RaybCMsE9tM0Yk42i6iW4lDItYTX/2TNf0RR2xUEEsmnhRQaDGcXKBGXA+OOTaO4cSiRM7mtt2FcuWqrxK7TJBepuiLqzanBRN2LoKvG930Wm3XquLpbwmhT0iLZBEUretDNDy2mNmDg09XNheibNwcSkpMdt6SKI24W2pXzLNFKzKt1QUWmiLg7mMlVDnjJa1aJxfQuOFaKPtEfI7o6pG7kDeABroiLLM/WXnsPF5m6la7W632n4z9H0gnwqkFaB2xwh5Q61jENj+/rC2aea6QfhDplhCovJOJG7r+fIo0siFGQwiuR2ZDYgEgoYN0O4lshxuu8uOPYollqfKbtiT7twPOEPzmiVjQxSlaeSOZIXDRsVla6x4ebzEtmj5qU50oFRLUNgOAnrU27NcaPpN3TbuVk5wphBpgafi0qYv/ZhqMRJddHivmloIbXcu7MUbuFcQZF6GSz/fRizNrcfFpnATslTYNckboNS0pQ4R6xBGl22IzlmEX5Y9P2RWk9hGcoLnMu/3zNK/CqzZVtJRWx2X5BqXWcqFUmlJs/tt0bEnh5PkWFMM7yAI+RkEY+V2mBFhEjUmVTB6nmYeBp3YGnlln9bxiB4ZzTsPFowparYyEF41z7ADHQzcgkg19rObJq6A0xqhOwhOdjP6HQIK7OY2h2tVPUqHNQD4TDS8vAG19mhj+2Ij4nIox0Ph57Hl06Md8+cea7kVDm2DFdMMrLFDcnXP+eP+nMIN3sS5bjNMJ+qBGcDkWVu1Hq7uaNol18sTytu641MetEbE2AvTEykGo8XadXHwT36uLAdvz6ZOX8nXrXPt8Ja8IC1kFZ3YQrdwIVjzqMXm9kYL0dOFjDQqpm86LWk8GpybPR27kTBS47raLYUeDq4bLz9znlqyuoAsOYrrUwxAoxi7HULZx8X2YEFefKn42mc0XioOZbyhWVo55NnlUiWnjhLPne4KqwoiwmhFXffnLA2POtwioPQIN+Wsapd1l+rcpYTMHbzxfGFHt+UpHlqKYRKMGuIcR5jrShHpurwU9VFCgPO6fKNhVqDIgy0R9CCSmJFdqabahRl5689jqREQb2abJKUv20ujbnwS5qiSOh5BC3pIuLwWGlk+U/U56zEvZVBMw0xawoquH9acgUGj6YVnxxYYRS+s7LJgzlB+M4eu1JHuMpajx1pqzbVndF2wlUy3Pr9SGhXdZjKpaT3qqFkMMxIdYzrD8N3AmfhQnFoq1shmpBZ0jp55I+NgSznEbNSFxyvrhPlgpaebyI3I9tzjYZp5eCfczmq5Q0NCWToI69tJ1dBuSxXO2WdCWsRWdBiNAk7Kjp1S85ulhQx72LiwvMwTbolomFNYwXWYaxjJOc2VbOub05egfsZ5tvA1+kRg2LFedNI43wpoqHSuRN/2yVAAWDlUqHKNW7HRUTFXT0Z0W8O7DeqGq9VeEW8tQzRbbOkAoEZXZ7hAFYtrxHA17DdJhbQuOzcF+USjoKMRdXV7Ja+7aEehcz2TYYwCojXpAEcXBiIHssCPdlGOPIwq2C05F/Mq91cwHVWE7AepCdJ875yPWiP4ORsXS/OKj24Ib6TFfJXs5zrF5gex8IbbgtF6Vy/2rMuh9E2+HYrDfE3BwWmPsIfFPixcs1KF0B0kCHbZ9trcgpFjhYYLPYe2At26zkf75PNJy4AuiweLnF7PeDLuC2EJJzHl3dyCDS2QrqfOQDxNwRDmsEx8ijrHvoktb5uCYkerGTtmc6gxjsT7E77vTIyUj7esOJEyVK+2PdqaoUam/ZbEoz7shzlBbKTifKsaKFFPbHiNd6Y6P9oe6VtHVlqvrqzOItDSH3d7zSLg9c2TFnt7wS1aa6XzutVFiyqjduOanScbZ4mJWukvm0VJ2PS2Joyki2t+AEs4utM4GWkL0HNG2AX2lzeh2EBKBA/LHTE/Hu1TgrJ7RgjBWnbw18wV2Tmtv7ZunhwLicBdmi1fZASFbotFxrGhelhuthDOorxzSUOvkLOMXx+jurwe4+DA6jdvw0VJgcpMlSr0cu43Qoult5jtt00GXebUOVORA7zPj6RfVFezjTiw7halghH3FqdpJYnHPSZfRhBQK906cFQ0N2VDvi1QazOOp8yCnISEVywuxzt1NUp7sg09BEZugtPuC4EAJEA4ueyImKaIA0Hk4JQydWRe+/VQI/kpmmME0V3TtvA6VASLgi2T173lmIy/ac+HdVNaXHCci/Z23bPGCJlj3/O4wVpLFgmobR423KB6XbXvXeJmdgFuWPASwFcN6RsZh9d5ySUETiR7rN2i+36jb9csulRD0Ha1w5Gi4iboBVQpAK7yo1uUW4sdL2JZkJLEGr6ERNkVo+BxGZxXXC/PD6QzjxsuPngG2V+Dk7uYW2tuEW8DE8e8XYTL3Hx3E0A/iyzqADtu290Csqrqsjs29sgv7W11ubTcAsW23jwfZRe6Nqdzsi+Ic5MkO58/rHjdpw6+fj1am8PVJaH44Ld6ZCVallcQkjeEuzhtxf1atXBR7iR0CUE6S1e0PbRludznK/KGgqpQ7y+lk4c5BKvhPBLYgxFtPboqTxAZHolQkgs6WV9OWl6E8ZgHDgoPRLBv92hddckxGHdGrEsbLO6WW3R3qgQvWWPnQ4ILF3dF48QwNtuelwRGxF17Le1Wblca2+x4TWFlN0ZF0vLpWiElBCYyZczJ5lTiYtM6djUYK1ZfnnJkfb21V7AAb1CoXgeXrN6BFQNHLBNc3e4kb97J+mFRjqAp13hmWPQ58FN1FByP7U4BS10uwULYVR18uypRqCWu160vIar0zQlF1vGZS2W5XB9QdEMHVsyfdF9x8RLPmihduC55HpnjhXDmK7yJBGS3CA8cUXriYQSrLernn5+en+5nz08vMLSC4eenabP77cTh39tuDm9x9fpGE12usOen/3c7n49dyPfTyftRgG97L3fuL/+OuL8+P9VuDER7bFU3WRe+bXv+l/3eT39/N3qiMz4O1qeD1aF9P8hp7fC+bR4DDGjaenwFpLr7pjlwQtdMP7Zppt9jueD76a5oXk2nGnfW067vfTP+tS1fH0f/T9PvYKajQt+LgQhvt+HbOcPzkzcCR8Zu84oS+KtfV5O2b4dl06bwdFr29Pv/BopnP51EKAAA -->
