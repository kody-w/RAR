---
name: "rar-cowork-cookbook-audit-merge-cases"
description: "Audits merge cases records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_merge_cases", "rar_sha256": "7b4b6740e3769c4b10428856f8e1d8730f7ea3332db15b32618102ff5021e68f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_merge_cases`. The original RAPP
agent is preserved byte-for-byte in `audit_merge_cases_agent.py` and in the RCI capsule.

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

Merge cases Completeness Audit — Audits merge cases records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-merge-cases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_merge_cases_agent.py` and embedded as the fenced Python below (sha256 7b4b6740e3769c4b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_merge_cases_agent.py` first:

```bash
python3 audit_merge_cases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_merge_cases_agent.py   # or on stdin
python3 audit_merge_cases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Merge cases Completeness Audit — Audits merge cases records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-merge-cases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_merge_cases',
    "version": '2.0.1',
    "display_name": 'Merge cases Completeness Audit',
    "description": 'Audits merge cases records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-merge-cases',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-merge-cases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '40d16db423886e8f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/merge-cases'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/audit-merge-cases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditMergeCases(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditMergeCases'
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
    print(AuditMergeCases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/7V6+Zei2Lbmv2LH+yGzHpkhM5h33bUaFQEREWUQKmtlMYPMkwL16n/vgxqRWa+q7uu7Vrc5hMo5e/j23t/eB+K3F7tro6J++fJy8u18xtlpGkd+PbNzb7YqbkWdgB9F4oB/M7fI2zp2uraom5dPL57fuHVctnGRg+1M58VtM8v8OvRnrt34zaz23aL2mllQ1GBvVqZ+6+d+09yFl0Uau8Pj+9jOXX9mh3acN+2s7lL/swMkeDM38t2keQXK/N6eBDQvX37+5dNLDN6/fPntxU3tpnlTLk2qV5NmsD618xBcKAfgXQ4+l34NzMjAV54fzJ6fPjZ+Gnya/ed/Jje7DpufvnzNZ8/X15fpz7HLZ23kz9rCbtrJHru0nTiN2+F1xqQ3e5icbLs6Bz7NGgBOHr4+dn6XVJSzf07XPj6UvIZ++/HrSwFMsCfovr78NAP4fH2pu+n96ySl/PjTa1rc/PrjT9/lNJ1z8d12Egasfv32/PwUCxZ+XxoHd63/BFIfQXL8ry8/ODe9HnZPfoKdL6+XIs4/PgSXdXH18ykkH3/6O7H3wKRx0/5fyf35ITjybQ/49DT8p093kH+ZQU+H3mX+vdoShPXf8QQsf1P3afYE6u9k3/H/b6LTGOTrO+J/Ke6vNkD/nP38t779qw2fZsHXl7WfxleQHU7qf5n99u10YFc/f/C+f/nhl9+B6P9RzKnoavcu4Vtm53HgN+23bz9/aO5ff/jl5w9dCXLNt7NvXZ3+lcy/wvWu5w8IPld9/ONeoF/Lk7y45bP3TJ/9VpT/q/79dabbaex9/775MvuxXqYXNJuceFP6gOCHmmmArT/g+NPL74ASAHXUnXu/DKr8P/5jJsVuXTRF0M5ObtFNvJK3ceZPxqtR3MzA36m2ax/g2sQA2Oc6kP9ThCeLi2D26/927zT42X3S4NyeyObbnei+3Ynu19eZCgQVdRzGuZ3Ojszh8DW3Qz9vJyVl7Td+fQX04Qyt/xkQz+fpzSzOZ7/+Sda3+7bXcvj1zpLxg3+OK2HingYw4+tkvxH5+dNaF7C23/tuBySmhQvUBzHgyU/Ar6ZIr4C7Jl+bJE7TmRcDSgbsPdxlAzy+TMJ+/fVXwLbR1/xBltjsQevNHCx4N2f2+TPwI0jjMGq/5r4bFbMPv/3+YfZfs3+16y580nEAPP1EG1i4Pcn7GaieLgPLQCBA6AA13NH+7fcnmkBMDvoQiE0cxP5jM8i+xPfeoD3xzGeUIGeODyAFcGZlUbeAgWdx+zoTgtm7vUDpdGni6KgADcbzSz/3/By0nzaygTvvSOZFO2tAijXB8GnWNf5d669OfW9MfgbK2G5/nUmrA+gIRQr+m8y8LwKbizwG8L8H/vE9EFJ/aGbLNxGvs/2Ub7PSru0yqu2njsB+xAV0grftQLg9y/3b13zqdv4E1T35H/CARQAZ9xnSz1PMp14KKt1r3nTf19hT31Lv/av+mjfPxLZr/96egSnDLOxib6L7fzxTqomKLvXu+AFLJ0nPKHjPqNxzUPqh069+7O73Zjz72qEwgs/+f44FkxUMxx1ZjlHZ9Yzdq0fzgc40qUwoPoYb0K7vyu6V8L2FvxHAGw9+zdMYhLoe/vFYecf0uebBLV0NlB+Z410+sAqgM8m959uUP3U9Zar9NX8j3E8ghHd2AZCD4gTJO+XMm8Lp6pulEajA6fP35vvEaUIF5NSs7ByAzCzwfc+x3QRYVU8184QZJJ8/1c8tit3oD17NgHQQYyB/BoyYYgFI+Q7dvgBugnIJ6iL7vjyeAgSs8DoXWAtGQf91ZoC0n0LfgFoDc8m0BqDw4S4KhBZgDEx8R7iJ7PJhzDQ9Pg20J56N/duP+D8vfU/TuyWT8UCm7dktQPI28aTn94+4vlv5jBQQmk3Zcd/0x2A/PZ392Bf+8TW/W/hOzaBe06ml/gDNDNRJ9sjFiW4aQBmZ/0wfkAf37vn6aICPDvtuy5c/Dcwf/72Z+t7StD/G7cssatuy+TKfP9rQWxd6BRUyBxkSl37z6Eif7zX2+V5jfxD0wOXL7N8z5g8injn8ZYa8wq/wdGkXu/6UpM8X8H31eWl+xqerX/Oj/z2oQH2RAeaasB5AC3xvFG9LQLcIaz+cFj8aRzP1mxtocXemBLB/zd8D/ywKQMR5OHW5pvihWO8dE4TxEaV3QgeX8hbo9qYJKvSn40Q6md/4L1/yLk0/veR25v/lMWKiaZCMwP3puAHKAowgbezfPwE3wIXYnt7/8Swk39/Y6SNpmxbYZdf30n8WwZPTPk3zZw5oY5r1p1704G1wQrG7tJ3sbIdyMuxxtJjGnPcZ6M9a71UKdHjFl6lYP82mefXT7H30/DR7OwzcD1R5B05DP09j7+QnWAp+vK99P945/ssvf2HGcwr+GyPiiSgmanm463vfWeAep9JuAdlpxx0wqXDvU8DU+Zrh3iH/7DZQWPtVB1qdN5n8HYPvphUPe36/u9I+jnq/vbzxyDN4z7EOLAcF+7mZmt0cZDRQCD4/cg9c+58HvucGQHRg/gA7KAd3SAqHfYwiFy7uIDCO0jRBBrSPeDSFwQHl2xiGoZ6DEA6GkgiNwGgQEDCK+CQdAHmPlP02tfB4MsKHAx9bIKjrYSRKEPgCoVB74dk4ZdseTNMUTAUe6AXftyaAJ5+ePTyZYHufPScEng7+9uKQOFjJ443APF6r+UK3qfPO2UfOoiYDprnQSduLesmhWUH2GFmX3f6y32c5f6LOR3d9dBNBSfqjKoS2dq5p7RYApMztIh139PIwaBmFBUTRV0jK1DHeLed5Hl5FmhqPLno2Tslp0AQNHymLKJJKrypBsRCjOc35eqTmpoqfTS8z7Y2hZbtGqaRhV9XlttwdhAb2eP/QusPFOik2matFdMpOrdJEwtE8Lhv9fAwgm1fRhZynvSePSO8FMd6c62ExX0jneu04Wy0JQfRGUTUsuPP9dijgrmDZTiEwRZr3upmL+obUj+6lFT0uTlAV6lnEJbVA01QxjpvLzoSCXZM0+npr6Ga9Iha0PbAmJ8Hr2OMNIq/SUy1W1jo+lunKIlOh6UK7orsGNQnOHmGsaS8KRuVbJ1XFiDJRoegkencTzeOp1+JCts7KPj8xkXWVM8Mu2TYSqYuJo9dAEk5ri0piNGQOSYiS2g01G4mAr2czMwZHba0E6W4B0m9gXr5cDrvNum+3ekLvWLtI0AXr8vxcCrulgq5Nf2+a7f4iYlmmZllqqAkfXxCbqF2sgqJa3u927L6CGVIhYsk6pby8COmLp1Ek7XEy5NqrfX/aHVb2NT94kHLcrC7J7hhD/mUTjt3JdBoIUo+CdbPR5qCdqrE1uTN5OJHstm0qZIBv8sKyTsImu+V9fKHROL4pVD4q9DBQ6ysXZLv+JEX6oTENbqFfYpepCBSKb+Jlr+bsOltgyGHnnrLdYQ8MXPDX9XIgsTG5RWNf8Ht9XBkpjA+j7ToWstUvqiMoVxjS61A517drD/Pz8ECvhXYsTxth3vE0sThcr1W/SHNu2XtVa+vounaGVFQvgRtjQhNLl+IaY8lia63rVt/UWTTcjrdijg37RjL7/eANl76FO0iU9+rerzJJOOTWkODEGqv5Q4is1f0p3YTiCu09u78O6ws0MBJ0McVwbMyQFYPYS048zdRhj1jkCmKtzHdHPfNlFmtVmaDE2t0VEHut403erozrIhThoDmceacwRm5AyKXULOrtnO+aUO2URRX7ND9ytt601sheF9JKRLFW3Ky7OQrhYn5Osa1nHs46J6fOzcSoQopPcYLf8qLsjaVhI0zHSMsNBI97GpPNNLB2KMVtJet2FXfrVdUhcZ6KSoUUsQd1NKI0xb7HGlOHvQ0t55fxtk/pK3+qjsdofilGfyw1C0YvdNuKbGxuSt2i3X1UG6SOawl9IzM0LbQuhKOGRKltr5I4o2UJexWDHCtd7ZgfTF1z0fYCY4vToW+KDXyejw5+hhUbPyKQMWclaOcQjGMvjO5IQ7Q6hgu262U0Og2JQtJQpprbxt03fU5ubDFRxVFuvKWgEpLO1XAdWAqTr4kTxhmbdcGmyoFftOJFb3topBUpMLQd2nDLuVzR+wW7TnkrNbPCzK+KQ3VFW0CKtdFspMQYweMtbIEn2DVa2DGt1uao5ma+VU5mpCKLtaXzfZJx5y69tAVxXMss7TYknoeooKGycOWUBQcJzJyAgphcQJt9zGrjWTQLUiTohQ/RvU4W9VY/G0bpplB4DlcFnSgoxxysokkgZn4rVtQSEICxbzb9iSmwnmM8i9VV2Woru0yZs9svuWN5lHH0uGpvxTD3WNke9MhF6NOaFcbLUd5InGJLuOjgMIWl5fq0NIb0VjLwoojg+UATtE5knBrlEk7O544FucZO792ELZVMHFW5u86DcitKWk3t4KynBHkjbPZcRMx1eg7Dy3BX1/LODuaREuUjKvAjKd9o2g+CerPB5/pmaM4iRx4RlClrrD+7ScgExpI/pfuCxhFplWhhtXFrXte2N67t4228PR7QmhlIRg+vPVPfjsKiq7aiy5V8yp8FCoYvoHt4rgXzOkdy1TGDGVrapMYmk1aBVumGle/lZrWgWFC/+fpw2IXN0lBlltfGY6k1rZlg1OBESY5sb8eDVq0J32MqnhuumGx4WwOp7FRC0s7mIqEv3OGcNL0Mhd3e2iplHVxiCRfaTu6USpAU3KcLtsMSrWoMv1XPFiITjnRYpHTDNUwmLI4KXHT7So2hAaH3/fnK2pttTQXbCFUawdCb85HowVvR3xWVv7OPFSXKowCZtiknqcycUGhrrpCNmDEWrZ6Hi6rzslCc1O2xvIroGY2YjSqwqVdKghgcmcJISuJcxZudHoDMYNFQvJgHfVntJQ1dLjWKZdBDRPNZv5aPw6ra7xPcDy/peummyBSlqjiN0oW7ym7qXoWKkfaUttdWnem1bVOc0ISNlo7MJK6RZEiboK7InWDWF7VlrQRnEZNHSRWhKBi5Wk12UYFDZW4O8+wg0YjqIkZprhccgrZxcuSpxL6wptL5K+xScgeGd4twsXYO6iqDisTLF9wpYTc9IVrkRdQaDa2tq1St00jlQmg1buVq6zVcHG5Ts2YVxbZWprAtdFHPGeV0FeHQt1UvphbFkECjsuTLFOLDG5rllLNHsygJyUAKVwtWtBrIWawgw5IMXcGhqhr44HrJUeN6ttW92MtxJ/iEEEMZKSlHvqYN17vWgitA6RkhcvpMohklnRmyU13HXNhrZcMlGLtaXdSYMtMNDmYEhl8ta/i2INGNlpocBB9YwzymIneFRP6C0J3ookXX7+VlsFdGa1H62521b+M+EoYL3F+JsDKrU1myRUZ0OwsBY2yZiAtlTqmlwuW7VOepfnRHiIGt1Va0/Iqw5bNoiGHYEUtUDs9BKdS8rKVjviSLzUgNYPLzTZFLrBzMdMwlumBKofBGORLdsIw3nk4sSVggSRMGcwXV4kflwiBBIeEaKJmC0SzFtW+Ui6/V6qZ0hNd00E3uFx6twdxhA+ZNarNY+YricjssPZmoqloUzs8hyJAra6iiQ0HeolNP6FEnOUOmbItrJ5/3qVXry8Faj2jOFFRgNzShQ3v6zI3FCRn9viQtagVnTqLqW/GQkkZFlZ4gQpZYG4K4OHA5qpycZIUbt07fKYfTIMI154VWh+w9/jznR6uXHG7HBGjSrD2a79TmhJCbfaTjEUPwFxklRdNYDuJ1a90aUNo6t3EgBqwuzvtt1Vlg1mkyAk2HuSts1laG19cdBXla3RsGXHDlRu6j0ccOpWYfGa9ZIoXiJkkKYexyd1BsqK3VAsOvWVrtCKE5qy2GUguiQLFsUJ3lmSqEYHtbRC2OUnq+z5oNm54jhqG1lewX1Mry5FgTNaowFCa2mpqRgnVOHc+qq+CiyVWIrAnhFm4i1mMIT0nheWTx6ohum0zzC0OgJX2ziqRjGV42tlGlUtOlY7qU3EIFVKFsmdwUDeE6rmW9tC/XeLfOogyvioSMHF1ciQUSMWRloaKxdDijNuUtf1uiKzcurl7JUUY32HYHYrvON2HvqMslZfGbZJetNYIWiIPIlKDFn/nN+ri48F6iyFWwKnRPQI7F7pbDwVIJSZobVMpemqaLsrwkWsGB05Wbp7HzJJPmcQpr/s0ExxthP4rnDAGtUNeiFXzcqsjYXUQkViukjmuibZ3Q5YwLVODHFMIRRO1A54blXddota9Hcprv2IjdrWJCT6RdN1QXg/NIeLU8YJiwJisnSCLDcPRwQ3KNRl9x0E+X+8tRuWag7xT+uIGU5uzpmQiVEOvkuRwnloxKdQvm2ty3LKyLOzGry8Fg6dVRVRpI3OIQhprezkc9rcVbHJKX++5wDIIz3aZBS9Ld9dja8GEcwDG19JsNhiyJYJ06iFO7/GpsoxuvSZXSJNo16ESrHMWdh6WW3zMOVuAMpbmFHtgkUfjSHpLl8TrPcY4sQ87Yqmtjn55TdG9LRBsWY2TB5IinWkHNAdVzrIxXa7M938Q60IlOFveKkUCHar7lYzdT+W44yK7jNZIHJXvFtI/JJid02BmORqbCFH2+UGYhIzzk5kKrrObzqzAGzbpkq1uDbRfz2FrIi0uXy8Z2ftX2IL+PSni4DK1XqsvR6bHNTTnAUC6fPTHvsBxayqLZKfss5Ha3KoCRrI2joDMPBS+wmHglCAwnpAXttlsHDCFhajbrDSnJ+spGCvKwvPVk41gKi+zKUXZhariwcIJu0Wh7tPzz4iBh/G556KtQ5ncdVafxYR6tA8/zAy2OroeUV0UmXSDI5rzDdlfP4hKJ2xw87bxCD4a3AIZwNb21d4WTFmiXlTbfw/Y6t8+kr0P5YWHi8yhE0CWs9SFnhrE/X8MytEjsdUNdUSkLSxJCcNwUSRZjOKUem5FDaGo3wPIFzTNkRQy05ru4lznzA2+fVWq1JzD+3IvNGUu3tFARRh6tMHnJUrFepFtUILosIAYKVKnJXFwk9q/XA5gHNu4WCdarQ7wrPQ92u+0qtJJbwcI0tRzMVZgtbo5odDKNR/SSKPdie9167HELTtsEVC1vtH8ItgsMI0M8EldBiNlOXjTR2WMN6bCm4OYWkOu1G4VVzdNY4dfxXlQ650rqXu8cS8Wft87Wc2kP01GhdOJ9TpCxauZ21iI9GlJbgsa2TAIPLC0XKnvwVhafmHUlQ6pBgPOr5fWJLEhUYqk8s1g1lrxsTFu+rjCJ3C1vpY5hNRERcHc6+qALJcJqyLO1BWpxgeKGt6/7awNOh169u9W4zpkmqaOSdET8hcLR3AU/Emtt7W8BquGGWLWDxy03DARlc8WBYVs4uXlxo5Oh4sq85XYs6xOUQmIx47Pe9ZqtQndu7K25DsaNND8HkoNg5wDpzuEY30Z8fl7XGibKmBzcjAidK1C6SHEw5WGhoC4p+WrLY4oe91l5Ruc+Nr/Z/RnSQKTdZXcFdKmslklM3SKVZRD81CFAG5Zd02W/FwuZteXInjtQwrctbfmRfVqZG/HU7XKKprXNsuTIW1OYlFfsybQbC6FB7cigSIyDL54JuHJ1mxMM660zjGAO04C1w1eq1oBRQEnIjMRaJ2kqEsP8IaU0qj7GhMbQ25NEVYFW+rmeMXwEQ3KctdWtCBLecOWQMTpWwLs9c84gDpxczuQFS/pqmatZxd4GescNZ+sKV+KRMtzrsaEGHicHul5cd3Dk4N3oF8w2SP3hbDqj20ZtlMCYQR+EE0EETTscBKrNBXWb7G+quFCV0s3MRm/T63wfbtaL02CSTkmf4xufeVK3xG/r1uLmFhqCI+Fa9bLl6gZjPoOvaLJkyfVtne2vGN1zOuXnhwhhLv5KReEqN0cIJNLmbK8pkWGYl08v013R5z3ov38iPN3q+392x/Fxc/DtWdP9RrBve1/uur78Cxt++fRSuzGw4HHftEm78HnT8b/dNf38p4cS0/Lh8Rh1eujVt29331s7nH6v5yXOva5p6+FbU6Td/Ubtpxena6ZfOWim30pxwc+Xu9lZOd2hvmuY7loD6d/a4tv9iffbxjifHuT4Xmy3/vNj+Lxr/OnFGwDasdt8w0jim1+Xk1vPZxzAG/QVfkVefv8/NrqnTRwlAAA= -->
