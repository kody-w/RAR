---
name: "rar-cowork-cookbook-audit-forecast-cash-flow"
description: "Audits forecast cash flow records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_forecast_cash_flow", "rar_sha256": "36ed5d139bf28ffd912b5a70b302a90d555a94c2714ac9c62613b1a3999a10a6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_forecast_cash_flow`. The original RAPP
agent is preserved byte-for-byte in `audit_forecast_cash_flow_agent.py` and in the RCI capsule.

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

Forecast cash flow Completeness Audit — Audits forecast cash flow records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-forecast-cash-flow
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_forecast_cash_flow_agent.py` and embedded as the fenced Python below (sha256 36ed5d139bf28ffd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_forecast_cash_flow_agent.py` first:

```bash
python3 audit_forecast_cash_flow_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_forecast_cash_flow_agent.py   # or on stdin
python3 audit_forecast_cash_flow_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast cash flow Completeness Audit — Audits forecast cash flow records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-forecast-cash-flow
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_forecast_cash_flow',
    "version": '2.0.0',
    "display_name": 'Forecast cash flow Completeness Audit',
    "description": 'Audits forecast cash flow records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-forecast-cash-flow',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-forecast-cash-flow',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9973d8fee01e764b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/forecast-cash-flow'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-forecast-cash-flow', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditForecastCashFlow(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditForecastCashFlow'
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
    print(AuditForecastCashFlow().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716ebOjRrbnV9Hc94ftR1WJTQiq40UMu1iEFgRIuBxldhD7JgEef/dJJN0q+3W7+3XExFB17xVk5tnP75xM9Nub03dx2bx9ftMDp1iITpYlcdAsnMJfsOW9bFLwp0xd8LPwyqJrErfvyqZ9+/DmB63XJFWXlAVYTvd+0rWLsGwCz2m7BfgVL8KsvC/Ag7LxH0OARF5lQRcUQds+eFRllnjj83niFF6wcCInKQCBps+Cj67TBv7CiwMvbT8BnsHgzATat88///LhLQGf3z7/9uZlTtu+yyC8JGCBAALgD1ZlThGB4WoEqhbgvgoaIEwOHvlBuHjd/dgGWfhh8Z//md6dJmp/+vylWLyuL2/zv2NfLLo4WHQloD5L5VSOm2RJN35a0NndGVugatc3BdBs0QJLFdGn58rvlMpq8V/z2I9PJp+ioPvxy1sJRHBmO355+2kBrPTlrennz59mKtWPP30CagTNjz99p9P27jXwupkYkPrT19f9iyyY+H1qEj64/heg+vSYG3x5+4Ny8/WUe9YTrHz7dC2T4scn4aopb0ExO+bHn/6K7MM9WdJ2/yO6Pz8Jx4HjA51egv/04WHkXxbQS6FvNP+abQXc+u9oAqa/s/uweBnqr2g/7P/fSGcJiNpvFv+H5P7RAui/Fj//pW7/bMGHRfjljQuy5Aaiw82Cz4vfvup7nv35B//7wx9++R2Q/pdk9LJvvAeFr7lTJGHQdl+//vxD+3j8wy8//9BXINYCJ//aN9k/ovmP7Prg8ycLvmb9+Oe1gL9RpEV5LxbfIn3xW1n9r+b3TwvTyRL/+/P28+KP+TJf0GJW4p3p0wR/yJkWyPoHO/709jsABgAgTe89hkGW/8d/LLaJ15RtGXYL3Sv7GV2KLsmDWfhTnLQL8H/O7SYAdm0TYNjXPBD/s4dnictw8ev/9h6Y+NF7YeLSmSHn6zvqfZ1R7+uMer9+WpwAvbJJoqRwssWR3u+/FE4UFN3Mq2qCNmhuAEXcsQs+gvUf5w+LpFj8+lckvz5Wf6rGXx/ImTzR6MhKMxK1AC0/zdpYcVC8ZPcAoAdD4PWAcFZ6QIowAdj5AWjZltkNINmseZsmWbbwE8AOAPv4oA2s83km9uuvvwIEjr8UT+jEFk/Eb5dgwjdxFh8/AnXCLIni7ksReHG5+OG3339Y/J/FP1v1ID7z2APsftkeSCjrO20BcqnPwTTgFuBIABQP2//2+8uogEwBShTwVBImwXMxiMU08N8trG/oj+iKWLjBbMYFqBNl0wE8XiTdp4UULr7JC5jOQzNixyUoOn5QBYUfFKAkdbED1PlmyaLsFi0IuDYcPyz6Nnhw/dVtHsUqyEFSO92viy27B/WhzMCvWczHJLC4LBJg/m/+fz4HRJof2gXzTuLTQpujb1E5jVPFjfPiETpPv4C68L4cEHcWRXD/UswVMJhN9UiFp3nAJGAZ7+XSj7PP5/oK8t5v33k/5jhzFTs9qlnzpWhfYe40waNkA1HGRdQn/gz+f3uFVBuXfeY/7AcknSm9vOC/vPKIQeHvmwD2j4X/UacXX3oURvDF/4fGYZaJFsUjL9Innlvw2ul4edpqbmlmmz67IFDKH8weefG9vL+DwztGfimyBDi+Gf/2nPmw8GvOE3f6BjA/0scHfSAVsNVM9xF9s4ZNM8et86V4B+MPwKEP5AEOAKkKQnmOoHeG8+i7pDEwz3z/vTC/7DRbBUTYoupdYJlFGAS+63gpkKqZM+hlbRCKwZxN9zjx4j9ptQDUgccB/QUQYnYJAOyH6bQSqAmSJ2zK/Pv0ZG53gBR+7wFpQc8YfFpYIAnmQGhB5s0eBHOAFX54kFrkAbAxEPGbhdvYqZ7CzG3mS0BnxuAkuP/R/q+h70H7kGQWHtB0fKcDlrzP4OkHw9Ov36R8eQoQzefoeCz6s7Nfmi7+WDP+9qV4SPgNr0H2ZnO5/YNpFiBr8mcszuDTAgDJg1f4gDh4VNZPz+L4rL7fZPn8d531j/9e8/0od8af/fZ5EXdd1X5eLp8l6r1CfQIZsgQRklRB+6xWH99T7eOcah/nVPsTvad5Pi/+PZn+ROIVyp8XyCf4EzwPqYkXzLH6uoAJ2I/M5SM+j34pjsF33wL2ZQ7gbDb5CMrjt+rxPgWUkKgJonnys5q0cxG6g7r3gE9g/S/FN/+/cgOgcxHNpa8t/5CzjzIKvPl01jeUB0NFB3j7c5MVBfO+I5vFb4O3z0WfZR/eCicP/sl+Y0ZwEJnACPPuBOQI6FW6JHjcAWXAQOLMn/+8g9o9PjjZM4LbDkjnNA8ceGXEC+A+zI1qATBk3hTMZeoJ6WAr4/RZN0vbjdUs3nMPMvdD35qlv+f6SFnAwy8/z5n7YTE3th8W33rUD4v3XcNj/1X0YNv089wfz3qCqeDPt7nfNoVu8PbLPxDj1S7/hRDJjBozzjzVDfzvkPDwVuV0APmMowpEKr1HgzAXxXZ8FM+/VxswbIK6B1XQn0X+boPvopVPeX5/qNI994S/vb2Dyst5r/4PTAfZ+7Gd6+ASxDVgCO6fEQjG/sed4WsdAD/QoYCFGBH4Kx/BKDdEyTD0KQR1V84adjEYdSjYX61WDoV76BrBHY/yCJRAMBdxMIqiHAR2CEDvGb9f5yKfzLKgjuORHljgU2uH8AIMEPMCBEX8NRbAKwoLSTLAgVm+LU0Bdr4UfCo0W+9bkzob4qXnb28ugYOZG7yV6OfFLinTIfC1O8RnqCGCS3uF0pN+UvxcKVK3E5CqR5yRGaLmfJK0SFrLtKcHu0yXy/MIVUl0GvjiyuzhHvLyQNCsa1ehkSRvhFsyyfcVAlGesl1OxxSaDqk1NvQJQsvYTHuMD1xX4xGrMmUr2ynd9XzJwvDW2CHbCMSNpjf5UZj4NiFiwnL0aVS1zRG7TudtiRqp2FfGQJdEetIOWV5b/MEVTPS8zGOY6id75VlTi3jnM16rAkH24ZITahxj8ePBUMYN6NK2Zt81k+mbYgbRSUYIO4LJIdOPvRVqmoqa+vKpbG1VWLociAdF9YR8LEui7L39PkN168TAfX1RFYJszYmvybKTpG1JIFvKqE3EPEqkeTErb6Wn1umoGauzdd76zamENITWQg9S1wqiWFZylShVYrfLhufLo0KcE4N3zzidGpfOHvPaVGy2H1AoLuGVtok2yiBTJcvJdNVmsJK5mCQJECHUbYKuHVey8tjbUN4RYqby3mQJRGJpo4NNp2zYXNhGYXyVEx1lm1o74kgy4tiW033b89BWNxmypqy+xjTiVjoDixSxmDtMQF8G0euUa+EegmPd+KSz486hpbEsLpvLaIthV+uW8sGhtFm4vG1w6LJdp/nG3XcprItbsW84RKwueeup1Kby9RRFTdt28Y3frmtJ2Bzygb9BKMeOkRZM5c63/RhLwklY1dahLnpe4QJ4GALe2hZBfF83SnKTeE1dNhYIJi2zzAy/rfY7hUtPWCENbk7SgV9jUq84Va7WcS4Ih4mty37n7Ow4jLvNxqgs1feT/Q3ah2RgNms91RWs21PMcr+304HKC1QefCVzEkitXbZtTqC9TjD6NtbXQ2Ced5ht000XCFa3zyMaOUG3NMDKLjvzlbOZTKubQFBaOmH2hrHqE14uM+54PaBRjp00peMTx4LvnTUwTYq4O4/peJvBJWlkt3rVM/mRF3BZ1DLFHUXy0Lurq5bbB1S+OZ196k3zsjlT8ZoTJuYqiKx8P9JXmT3wlwuKa1Z4PqG0Xhz2FwrJdX/cTFf2dq+2OblXCE3Sl9clXa9vNsRoPtS15Fiht5Xa8ITTDoemF93QZ3LdQNiTAnBduGSr5sLiNMSHRGYvE3zSb4QswcqgxZJgHm1anhS2IHLjXoWC1ePpsofiyrfHGx8knX0Uz9NIiCLYUI9kRw8Cqi53yRWVEa44bfdjnpVH6+AYZnJH1kRlWq3Z3hC5cwSi3Jr72mKEFpXb0oTZXkvpa9mHnrDzL57eWUfy7O7dGzpBqssE2ZKER4eVNPtO7eqQ3DB4KPPni0KElTIMG2zP3/dk1+pIKRkMkThdeR8kbBLt1pRZa3fl4TtSFltLiLldWmPkhY+H3UWbhGStQbwqE0slLxHXD7fLlDvBRXSQoT0XeuuJQVeTLfq+rJ6Gvc1d9sEJ5ldH4DB78qFNChvb8NZ3HLnpDZf2xHXhRxHnZYySZPDF4uBk30TnHXUgsc0op3fZzur15sLRnXGRWcjGHAeKuMAr8LbY32PvnvGufdqsRy3cn5eZBzdXfmwzLKvPchhtboee53SjNUTPsPiQvx2kvYrwg2gmriXph9VmmvTenGxZi3LCrtl7YJImc9FqGxP1CJbGpUSZui2inkLTSmR4mgGf4kOc5nEa+xtx4+y6g3PYoWaUGWLVHawKwq77fM+Po8cT49RQRFisB7y3hLt9IZXJTLGQKkwpE2WfAk35hSo3HJ8bwJ/+7XYbCcZsPP++dJmIm1KSJJfQeIJYsl4Gy9C0cRLiHPSK8lpAEx1JZpigRnwrJb4AS4pbTVIl6GJyrhHYZEMzbO54vIX4tMqmnmY8IyQICuKOa23NoZfdphM110RPXsSeynQLH325xnZk4tNnuWDUVJzo4hyNqloX8jbwWBpVJsWOXTVbIV3Gort1qdpGSZcMhZE6HfUn26GJ+2GHbwM1jJy4s+rQw0d451xkVBgsESmJfl/07Tas+KisGszSea3F8HuCjqp9PUVdwskZl/VucnYOukRcT0h31qyNko1VzenRPgrLMTWKzSid1mFDTW59jvasgZA3I4WO4lZWri53tO9iNMhik+YX7bbx++Yo2KeszumaQGV3A5WIUvYDa+pBQJSywTjemHmBa8Xm+lBKFbk9ZE3DiDB+ZNXaLFXqzFYcR6JHgS030uCPHOXs5TvPVljN3clz6mryilCPml116gbGNclu07rnB51Tx/4CBiaTOG0Hr5V2O01zXT/t1zdfTm8lW2b0QFsWX/tNnWKum1AGfxsk3ivZ20GwsW2zzY4urqL+TjMOPQo2F2ifqAnB3jQL08zKotljFXCXzij9cXdMtodzyNjHtHNlLFRYRcRWcpiwJ5goR+/KhEtFWfLIron50vPXecRPKl6y1wNz2pZ2yY135y4Vph7pzCnb6Eyl6bLeXlgxI9CIg3W3Py/rbbfvEVo2sOWGxdFxs3b8wrmmZzFQ0i1vXDBbkyzu3EJlpwyToFwVACzr2wqi2hxelbC+NeMpvd70a1dYnLc8EbCVF8Rhwnb7RvCP7s1etytrAlDFgDpy9/3aYM5sTDFiaCVrnxQkHbnQqsDg5KC5dW6U3gblN7yFHxM9n0jlXKzWnrHSRiGy6m3qbeQsyC+qaWqkqDEsDRwvXshaTR2XV5pMF0hoqbEpLgSlL0l0zjEjlbE7yqN0jnEOsWDysIH6oowEwuFw01lMLAxKj7K9h8t5vl8dtjEAop2xp0+McDICh9QF0IjwBzwbs2XN1OH2YCQTZ0l7TOCbs8meJ9YO+IN8n64EByGbJhIldjx43n3tHJgCcZTQQ9FNgBeGed7vHVq2+t7kxyt9rfnCjanKKVi5wnxyIKGQP9on/WysjyKasu6+2Mp4JfF363zKJsEYvHuZHT3CxysuujrTlJ1xbPBMKzZWxTErHaeKdbEQT6asCiOmZrso3p03Zn0QghxkoSz748ljvLNSbWWbFTEtv0V2N+ys85nkTv5qexUZOuyzVh/wQDxslMbO8ntNHaJDMhSht0v3jC2c+BbXrdzdjVy25FxeN6spd+xrng9XOe+qrePGZbk0MAFsK8KTl4XECAs0qVTYdudYK2jk3DvXp9rAb+RaDpHhhri1FkYInGhLdVV7CcSqwsr1qaK7dRYiWHqAK+twx5EZR4jI1cYYEHBOM9AtKwlrKfWDYw8Pl0ypRz4txVSNbEGL6+WGX2eEQqR3pTzl6JbWYvmARbzJr7qthIY7yBsuRJDASYfHLNkbdSKByC+5TOMy6+aLAGzka+HZY6MwNL5mnEkILi6scUbnVY4Hc/crEZ1qIc5LOyGtUq0GOTLbGlecHY2nIS1uDUwasvW1vzl9UgewXlxaTiEu2r6hoTamYQxWk25SKs5ibejSae4tuhBkgsNcmnENwtZc2bJ7nxJYrryrmtZF2rUy+dMlikYoUOTjwU/5ZUooS3Z/vIZMrPFMCQ2WHeGO4NSJLE6KEUhTtcxr1tfBjuEslBTM3jNDI6ZOPDM1WxeetPW3yVktD36o3wv3mLExz7FX2+C3Mtrujnh8NbR7e6C2I7MkEsS++LloXrjdsRCR9frOIuQBhy/SymQc51qOobGRsNy+FhqK075EsGRS1KORuwWK6dRpusGRRUk9NUC+ZjBXpoBX971RX/cpAV1ZlzjB6k0ON6NRLTdl0w0QTN5IN5ssQ57Q7B5yDbSS1nW97JkxWPMoxETe2iG1iVOoe02o7XTaOb5RU9oeU1H5GlAbekNeG6/l1GvBrCRQsNbaEjof/N5kFDu5aEO3bcehHgrbM0VPtWJvTxjs5kxiwcG/u812lyIh3fiQVeH4HWEdC4cmskiP02rruhLpDMY6AUUS1aLSDmAuW6FYNV4D9MSvybPg2RWErKBto3Z3llwu8cOy3pF6wU4dMi354o6LlrK3pRtFxIjTrUWaQbz12UmXPrrVpwDh+eDaaL11G0/iclOs6EhClweRifl9fT7bR43DtiHKGkmQblJqTR6KAHJOKYUPA70Lz8x4Ebk8VjNl2sUluZY27jEt6KY6q163iq+56Ijcthm2kwKhvZMc236oSTFQCdIPkM2S82/Bbql4uHdBqwBLaBryuy4b+VWy7iQ4i2qjJ8LEKbItBF3YCIGyDrlvEePsAiGEC6Fxk78B7SxmLqkLdIzuYXZ06vyewjSipBy1gogVvPWtEPWpIw9rOwyNhUwOj0S0OQmpX1zQrFoFTmy0JGTfNcn1vcOwW97GXGih4WoFwwAbBbLC9aU49EK1OnQDLV0vemeg1rCR4WEp3M52q9BpiG45hCLw1lUKrzsf4AxnupNPnLNBLVmTtGitEJfSRGd80RT26ThkU7K5b9IUJlDSJdKydY67kJhu2Pl2v4P8JHFR1/FYd8GGEka31Y3d83nVkA1oApnp3sbEml1uPG5MrOJyEK4UQq3sgdcO+8TM+jzarZ01n3YDj6TUcQUftlNPrVy1ybaoCzqgpL5co/MNZgcVv1tHAlzJLV3dgv4sYniy4XP37rsqR7GdvWPa0hFv3NmEdS4aQU+6gZHpvjsdrd3gXyNm1UxMa4DqM3mbXY2sCsi0tACLWoUS4nqzy6UpJpSmILZYwp98jN4dfTgnTUI1EWXiyWinHkMcCxxKOuxOqR3qzIHLzkghEBq6VV1sQ3MhzjQdCqHS/sq04UpdpubU7EF37GIFpnXkNqT35HK6EzIzXan1jdy0flG7SHjfc9NJpKT64kzqCG8vO3hARpPqsX7prcPLMuaCbkm7m9EKiza2pQSX4JHRILrqLq6mbNcQ3+9Kc4CTY7brczNNKApLOGSXlx6dymtzBbb+ey6WEuqiI4Y/Dk5Q2W29i/OMV08h1q7kDXEwvGS8L5uIxzU3AO0x7Xd6QBeIysB6pJ1PakYSeKVmKLSGjdu5cCtRzYC9W9P0OSjXUly7H/BdMdwzBNJ5juLX52tKC9eYQzdKrJ+4jUpo+soMx8k4a6V8XwF0NkJ26HYrI6jOxwI5y0Z2C40dC7YVmH1HI3npr0rFE3Iow9WV5R+ThIfz8zZUD6vYvWUQd1Khq7Lu4m102lBcmfliSprdkEI2qQjCaZlK+Q6FwuxS0ivsfIwcnEHbtd9SByM/Vk0uR6eWUtoYlXoeEdMDwKRhPW3z4e6t5DWu4rhL1oe8TClxSR841biZknKg6bcPb/Mh6etg+l++Qp5P/v6fHUA+zwrfX0c9jocDx//84PX5X4vyy4e3xkuAIM9D1Tbro9dR5H87Uv34V68v5lXj8y3s/JZs6N7P6Tsnmr8q9JYUft92zfi1LbP+cZj74c3t2/n7C+38FRcP/H17KJFX8yn2g9F8UPt4e/C1K78+3xO/zV8tmN/7BD7Y9Aev2+h1rvzhzR+BAxKv/YoRq69BU826vd6FzMey88uQt9//LzXjcK90JQAA -->
