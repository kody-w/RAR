---
name: "rar-cowork-cookbook-audit-develop-leave-and-absence-policies"
description: "Audits develop leave and absence policies records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_leave_and_absence_policies", "rar_sha256": "3817f1fb982aaccbfcdda22b781d5a1afcbb0216b0bbc6079bed3c15e9fb647f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_develop_leave_and_absence_policies`. The original RAPP
agent is preserved byte-for-byte in `audit_develop_leave_and_absence_policies_agent.py` and in the RCI capsule.

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

Develop leave and absence policies Completeness Audit — Audits develop leave and absence policies records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-leave-and-absence-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_leave_and_absence_policies_agent.py` and embedded as the fenced Python below (sha256 3817f1fb982aaccb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_leave_and_absence_policies_agent.py` first:

```bash
python3 audit_develop_leave_and_absence_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_develop_leave_and_absence_policies_agent.py   # or on stdin
python3 audit_develop_leave_and_absence_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop leave and absence policies Completeness Audit — Audits develop leave and absence policies records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-leave-and-absence-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_develop_leave_and_absence_policies',
    "version": '2.0.1',
    "display_name": 'Develop leave and absence policies Completeness Audit',
    "description": 'Audits develop leave and absence policies records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-develop-leave-and-absence-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-develop-leave-and-absence-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '90daad5bfa490e56',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/develop-leave-and-absence-policies'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-develop-leave-and-absence-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditDevelopLeaveAndAbsencePolicies(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDevelopLeaveAndAbsencePolicies'
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
    print(AuditDevelopLeaveAndAbsencePolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6abOiWJfuX7FPf8iqJvOIMucbFXEBBQEFUZmsrMhiBhllxur6771Rz8msfqu637pxI645KLJZ61nTs9YGf3ux2yYqqpfPL0ffzme8naZx5FczO/dmbNEXVQLeisQB/2ZukTdV7LRNUdUvH188v3aruGziIgeX060XN/XM8zs/LcpZ6tudf5diO7Wfu/6sLNLYjf16VvluUXn1LCgqIDIrU7/xc7+u76vvq8bH97E9XWeHdpzXzaxqU/+TY9e+N3Mj303qV4DBH+xJQP3y+edfPr7E4PPL599e3NSu6zdMqwei7QSIzj36AWf/RANkpHYegsXlCByRg+PSrwC0DHzl+cHsefRD7afBx9l//EfS21VY//j5Sz57vr68TH8ObT5rIn/WFHbdTBjt0nbiNG7G1xmd9vY4Gd60VQ7snNXAj3n4+rjymyTgt5+mcz88lLyGfvPDl5cCQLAnL395+XEGfPblpWqnz6+TlPKHH1/ToverH378JqdunYvvNpMwgPr16/P4KRYs/LY0Du5afwJSH/F0/C8v3xk3vR64JzvBlS+vlyLOf3gILqui8/MpTD/8+Fdi78FK47r5l+T+/BAc+bYHbHoC//Hj3cm/zKCnQe8y/1ptCcL6dywBy9/UfZw9HfVXsu/+/2+i0xjk8LvH/1Tcn10A/TT7+S9t+58u+DgLvrys/DTuQHY4qf959tvX437N/vzB+/blh19+B6L/VzHHoq3cu4SvmZ3HgV83X7/+/KG+f/3hl58/tCXINd/OvrZV+mcy/8yvdz1/8OBz1Q9/vBbo1/IkL/p89p7ps9+K8t+q319nup3G3rfv68+z7+tlekGzyYg3pQ8XfFczNcD6nR9/fPkd0ASgk6p176dBlf/7v892sVsVdRE0s6NbtBPX5E2c+RP4UxTXM/B3qu0KUElVx8Cxz3Ug/6cIT4iLYPbr/3HvjPnJfTLm3J4I6OuTE7/eOfErYLmvT078+saJv77OTkB+UcVhnNvp7EDv919yO/TzZtJdVn7tVx1gFWds/E+Ajz5NH2ZxPvv1X1Xx9S7ttRx/vfNs/GCrAytMTFUDbn2drDUiP3/a5oJ24A++2wJFaeECVEEMmPYj8EJdpIDcm8kzdRKn6cyLAamDtjDeZQPvfZ6E/frrr4Cvoy/5g1qR2aNf1HOw4B3O7NMnYF6QxmHUfMl9NypmH377/cPsP2f/01V34ZOOPWD6Z2wAQvGoyDNQa20GloGwgUADIrnH5rffn04GYnLQ4EAk42BqR9PFIFcT33vz+HFDf1pi+MzxgaeBl7OyqBrA17O4eZ0JwewdL1A6nZoYPSpAi/L80s894PYRSLWBOe+ezItmVoOErIPx46yt/bvWX53q3tr8DBS93fw627F70D+KFPw3wbwvAhcXeQzc/54Pj++BkOpDPWPeRLzO5Ck7Z6Vd2WVU2U8dgf2IC+gbb5cD4fYs9/sv+dQv/clV91J5uAcsAp5xnyH9NMV86saAF7z6Tfd9jT11udO921Vf8vpZBnbl3xs8gDLOwjb2pubwj2dK1VHRpt7dfwDpJOkZBe8ZlXsOrv73EYL9fmy4d/nZl3YJL9DZ/4cxZMJM8/xhzdOn9Wq2lk8H6+HLaWCafP6YscAocFd2r5tv48Ebubxx7Jc8jUFiVOM/HivvEXiuefBWWwHlB/pwlw9QAV9Ocu/ZOWVbVU322V/yNzL/CAJ+Zy4QIFDKINWnDHtTOJ19QxqBep2OvzX2p58mr4AMnJWtAzwzC3zfc2w3AaiqqcKe3gep6k/V1kexG/3BqhmQDjICyJ8BEFOIAOHfXScXwExQXEFVZN+Wx1OAAAqvdQFaMJH6rzMDFMmUKDWoTDDzTGuAFz7cRc0yH/gYQHz3cB3Z5QPMNMQ+AdoTh8d+/73/n6e+JfUdyQQeyLQ9uwGe7Cey9fzhEdd3lM9IAaHZlB33i/4Y7Kels+97zj++5HeE7/wOqjud2vV3rpmBqsoeuTiRUw0IJvOf6QPy4N6ZXx/N9dG937F8/qe5/Ye/N9rf26X2x7h9nkVNU9af5/NHi3vrcK+gQuYgQ+LSrx/d7tOz9D7dS+8TUPbpWXqf3krvD/If7vo8+3sY/yDimdqfZ4tX+BWeTm1j917szxdwCfuJsT6h09kv+cH/FmugvsgA/U0hGEF7fe82b0tAywkrP5wWP7pPPTWtHvTJO92CaHzJ3/PhWSuAzfNwapV18V0N39suiO4jeO9dAZzKG6Dbm4a20J92NekEv/ZfPudtmn58ye3M/5d3MxP/g7wFLpl2QqCCwCTUTKemfRFIS0C49vT5j7s35f7BTh/5XTcAq13dWeJZL0/6+ziNwTlgmGnLMTW5R0MAGyW7TZsJezOWE9jHDmeatt5HsX/Wei9ooMMrPk91/XE2jc0fZ+8T8MfZ257kvtfLW7Ap+3mavic7wVLw9r72fUPq+C+//AmM5zD+FyDiiVMmFnqY63vfCOMeu9JuAC9qhy2AVLj38WJqqfV4b73/bDZQWPnXFvRQb4L8zQffoBUPPL/fTWkeO87fXt4o5xm853QJloPa/lRPXXQOshwoBMePfATn/q/nzqccQJVg3gGCEHJBBIvAocilbbuuE7ieZy+XDkEuPMxe2IHrOPBygTuw47g4TFCO7yHuAvOpwMFRIgDyHtn9dRoZ4gmbDwc+Qi2WrofgSwxDqQWxtCnPRgnb9mCSJGAi8EA3+XZpApj2afDDwMmb7yPw5Jin3b+9AKVg5QatBfrxYueUbhMW4ciRQxF4EF4vJAlT5bjMYGkhp2dvJXleqMD2iRGbMc6ipNxSYng2dFG0j47fqwwVr7AoX5723fGQHk0bWqZwLSehY4xqt4Xmm9b3jperWFCSgWtmeo71m8iPepKoGdZIpZDaF8mUPNswOcO5lu7CLtVFUZ3ERllAe8REqD6XCAlhb/R1qy2ywS5goYWlgkpIG2p9G84rTDQ1EBXONoWFqV2rXcm3ulk2KLUpKKXttiQ+3+eLYX7V0GBexWjtWR0XVlsWDeuDPV7BLhAODKPBK3NZlJqeS6WLXHnnpmUyZjSXs+RoNm4eyqoRbt5Qmju9zBg2oWy5d1GzHNx6ExdlvxQXG6vOZVV1VNQ/FShcU+vq7MdS0nIbHq8E1T+nvoXoXtN0B1tmblt/aXdgsOy4NbehqnPM9mPfyRlrK0Kqb8/a1TFhOjnuqjOuHc5SyjZDSzllC1KTdtPsSAgcx67MdOtyp70ND/tMkoj1iBkWYpxlp97MjRLoqaxRGlSqOupWV3EXtnRcmCHdoB7ZQXOYRs4K2ab80S2vGlaWeoIxaEHpzQJy4DldKXK15eVrz+LqEO1KZbGRERZLjMy8JHPQ7bAFvAqjTGIW86OHk2QucVvBOLF4cDrEN1/Vl+eIyiFvZJ2gJVjuej5ZLbkRPZNrh+0lkA59R5oXK9Md9rzezTEL74QNl9PMDa5GqE7nkby5YVo9yIGl1jK+3azRyBsaaiuVx6WyF4I90V2DzEoRkGXI/hwn3Wm/xPlt0qu3W3FssnPJjg4UHx23FOXaCzSRSmCRS81uu9fM7RhEKSzui1uOtntUDXpaoOZFutnbc3SN3a72PsAGKK43h8grMZ5rTX6RVrtuYWy3AVsmZ7M5LznJysj2sr3GsZUTbOjoi2a9Q+1BMtNosbaZG5rCW6uuzkevP42ejp8uia64N2hbFGNaWitGWzQ1Cg8cwqQDRzulmghadjqIo9AOa0+oJDq1ljssFsb6es2qHboTUTRzqlHlUfNAHgJlT+1DQfG1YVWnFhg8YTYYTknGauTZT1ZuPgbFmulgdL+D4MqUsJMr8kEf74zlRlp6ZUetIBrDWTG+UUe0g+OdNHbY2eTwuh4KiWO2fH8yIEveGD259uXUuhll2rOU1g3b25wZNMqEj6frKd5zNo+Z2tkQtYs2hw+Mr83Z6sRuiX6uFgPu65lBREx5czB86e7XS+NKulKVLLeQbmRLT1opWep45lCKhhhoRsdHlt3IGsSIGb/Stv0CroXk6rSRG1PnS6puUc5XOT/CKNVcoyG8WOClcCHT3RzklK1F/DZHYO94kuROiuaHRAhVbUgLbjkf8jzYt8JaJUrUOnSCeiHAtcT5fOKW2Zo4lwPdeD6WbKPWO/fHNPP4SumscpCTDaYvJAUwN28R+RYeL2IF0vQ2P2QnWdviCA/NZdYKxxirV7uhVWFSXQqAJzVC3FvdNos9n5Tq3ue6DdJRsHkLqQbWhEPUnupSRMblLbWYTIV2ST9ScOGSCb5OespMxpy3VtpBt9CYtPa6AxVioZzq0wUhtaVwPCkxfLtcuS4nRiE7gYytl4tALwzItBWcVjqpXPPoislC7IRxGH1Z0/zmtDVWdDQew2h34OHtsekMAkzsyqU/SLS/PcZVpfN8TsO78nokTxteJ9GLQGvhgm7rtD9YQr6sNqu4VfZrqY/KtO1JdmAJMgqXClRjHuHsRsjY3S4VgdX5GfL2OTaqx0G6wnwWePMLX4qSYlTkNUaUQVQYxvWU6Jwx0LwR2BuEYhdoyTDrYIuF8E0iFG4UT3NqLnA4JCZ7bksWdsqbOoFfleOR1h36Ip4MGNKqTI+4BG90qYRh5Sp2HbqsW83AVj1rqnaM+2G1iM/yXsPk41pWIOGKsbvsai+MVc9xCSnGA8KvQT8q46FScGdUGXpeuW0ZzSPuPEh6Qss3VCrYfnVtKNfKzRBxzvSxqpFAGEONSHGhZDU92itzbbOiDGdslGyx0O1cQZPOsBEvNXFqMdCOUG95v/POxIn157x0HnSnPrs6qVpDmo+9SwXlsUTkMM06p3eOS0dy+K21TzbRyLG6HWNBuTeczqTna4NUCy3rzLmEjHpEj03MHdwrJ295Iaqd0WFl07Mu/ooIc3rNX3utX1Ipe9Pgpt9zjECetWVT4hm7SjcGgpWpnBxPyUjL1029PTSww7MyY/CMbsomvd8gaUevml3QhL6USgEajTLONolKrgShzIvIlRMDp0B5kax+1a76bbeb57I5WHGahspqP+xpTToc9sG1yw0yP3tYdeQOYhnTIwT4CD6g+rJqdfUIJfGQ0rbMOrmTY2nJd0cEXtL2uvTbQNNbwtV2eAq4gmx0kNJzHewchIh3IYorGIm7mXVj4UmKRagqdHYqaWi3oZRYy4teC6/tdXC8YoMoHNMp1bqIcCcc8VXpJJst5+z4eSRxuyo5qjbFRuLlepN0hFbjbkwif35B9BuuLuQ4Czf2qZvXK8JGA0KsJNi9cLdhwap9HDblshRkHsZyTY5MqzIFH2rXQTnOyVxlL0fPshhzvcmyTSCPAurXSF/K+2FbeRZU64vMWObNbb+0WhHeNfjSH5eDum53PL0WfeJK7Bl23S9opg/PnoIElh4neTiHo/qy5XblEfJFlQyQM3SIkL3BFH1bMLsq5fPTxtSQ45pPcnFrrqTLtUyvUtUebQdDyatWwYKuVthq7m0R5qrVurwqVtlNRVfnTNDK3Fa5K7YL0evI4kl+JGhLSq5uQhw3Ermxk+tuv+YRdcuoGtXOx9SQyLWLGyKT9zUt2gQLoqofV1R52Cyh4mC4ZtWHTCtJgdCNBdGvdJXP2CEyGPFmcHqGUXVDxd4Nx9FLbfpbMdq0Cr7ZhRG6O7USjJA5f1sKGwIlV8rVP17zRQlY6ThgfHjjqTEVEiRHclEb4SWj7lq15mkiRbDFommkTmzAQHJbWTdxaTip6q61wMe2ZoJihs6GsOC7MBxpsms4J0gU5f5I7hrUk8xDlidD6e4IMCxeA1vpIEXRfKvd+fQ8Xe9X8iKA5DpA/EGJdDKisX3YUFDS71aJDh2H6Ow5O7luTZdpRMyuk9PBEy/FGpPnTSVkKHZlRGXYuyYC94VZ1rKo7o8jaKQ3bbErVedAey2jxCM2gnG9pRk7UHUK8dMDBnkNpJnj2VQ6osUIBzmZAwFmIS5Iw4HMTVJsbYRk8B0SFklBiuoqDlUwAhXmtrR0vTlB0Zleicu0Fm+UFhBHgotF/UhfDJDWa1pZJMIFXUmRBmXkeafuFUIZqQMeWbEwmAmzHkDwwOiMX9VxjZ/BgDLorAiJ9SphvVC0Rrw4YkYeQ2097nFnC9LmdGUarRDsi7FeXZUq1GoJpLvFusd9yPJSEKMXS6zMuXlg9oGFWiqzOO+MfAh9TA13vsWLBH7w/R09LpAlpEj8BUsVU409zd+oEn649sI2bQqSZZgF2sRYV5yjxTkRFFQbB1+5AV/q6y7uges3hayHPZT5qttqraXv1W1csZfreMwj3SOqcp2fInNhjp2zYdE2Nak04k0nW+kSfrTskW7VouD9c6QscnE9CDx7Goyk3s459lKtsh6L6hJ1tNWc0Va7jXrDm3WnUnHeMmvGtMRakTbny+q87sxqvj5JLd6uOzlNtpQHFY6FGdkhP5Ut5A6nEZe9JrBSRQBjaE8zcSaUOrffrKGV2zTrgJOP1paClbRrFN+HDKpbE/Yq9DubaJG5bqlOjNiQvodqZWUQQYv4TBog9GDKGWFFdU0Ivby4bcA+7LgjvKXWKLKWtoldZ4fNAdtTvH3BWHljm4fTgt4PLSLn2L6/FeERReWatxAOpOSivuFgrKjE28lHVTExA7LDF2K4KYNEj0n6alNmDxOFzLY4MxgYSWqFuiOQiOov1TwY56FS3Ux1Rxe4BFFI4g0h1HADsqsPHHGipBXpQ7oTURQFDTrVd0NfVcEcD+Y8EvYX33ZQpt1iHL90iXHNklBaNld9R8Td4K53B4EbdEQXNxU0D09x5tqrc8FHlJVTDNGNdLbfBbAgFHOx0zl4I+7mV3x/QS7bhMYhlyASi7KFITrU3upALAseb0R2dc7JpkJSXhHOveaOSnJjK9xY8JIyOte0V2qTGjeL+ET4t5PrDQZ3UG9EjDQJzUIEMVYJgTD+eZnseH0VrREeU/gD1aCb1XaoGyyRb7BzPK2pDW7L1NhsyZbvzICySOIQ9gbTnm/MrqE5OVuVFLUZ4L3TBom3GzYwtV0sey7EOtMNDYTLmopYmilR85QpsyPRk4ntoUR8ngcKap4IVk43a+RgdHnibskz2HWsdRa0yjXBHq5XZxQGP1yMGMRxkcWu6iHygwLicm8dOQt3BQqXh+t9s98LUS/czgnrQNvoZrFFQu23suGLi4FKNrdQAdHTKIHcxoczQi5WA0ruktw9jMRqcXDTK1OGc9vdJDVIupVBdqYp6iEJ8+thxZhGhzVqcQpl3BqDYMi8Mlexvp1L5ibwSG+ZGkJMLOQaI+yjlQ1JwzXL0JHnGMGt82SUSCg8rTu0PBNCUF156NRSOO6eg2GtCC6i9hnEobxFuiurhz1IwXf2lum5M9IElz2djvltkSlE3NcF1y+Njb/Aqc2ZKZdIdyX6283HjrVBcdF1o3CHagUbWgfLHUMv1z7NxnjBUAd4390QKznQ5+OeBKfPmt8kyv4C6/Xx7FHaCYrT+BpETuESAy2DMTFQVnQQGJQzp1yeNL0zdQlM3vO5nDEEdQMR2LyRIiziKd4XEDW/nRYdNawugUIp+FkRIwLxd+3ygA4ShBBgAjvth6MYzSUI7EfQbQAXh12YkgXaMx5Pl5S6bBoPnsduzOBgGrxxdts6Le8kOTcnEZmG1wm61Raktt9TfRXLagTc3UdLzD7NZafNmdv5unZUk6yO3iJac5wB3cawx9feBmbmtbRbuxoqH1HXZlaCjmdwmOIb36sUs7nU4sUbjis12lobdc6dsH3u0soqIgG3BUa0DUSF7F2ablzhNHg23e1Qdylcq/GCJMOVyU9Zse5HUuLHjTbgmixWhtsxNTEyKD7GW8Q3r5cuJCgcptPecLBTGFzJxWYpnY5UMFjRPOMyaCnsum65K/cKc2UBqXnr7RVeH7t2bIuOKU7X/LY1lz6O5SrZl4ta2dOBdbJQQ0EaJj7zmTGorNdV2LobuIg6cEke5+SRnF8aIk1aF10luQfG2xhuG5TiSWzHFtFqLGia/umnl48v083W5+3uv/1ge7qD+P/sRubjnuPbQ7D7bWff9j7fdX3++9B++fhSuTEA9rh5W6dt+LzF+d9u3X76Vx+iTFLGx7Pj6dnd0Lw9LWjscPo51Euce23dVOPXukjb+03kjy9OW0+/yqinH+644P3lbmRWTnfP74rBexRX/tem+Fr5Dfj0Mv1cYnoW5Xux3bwdhs+72R9fvBGEK3brrwiOffWrcrL0+TwGGLh8hV8XL7//F6GZD2tmJgAA -->
