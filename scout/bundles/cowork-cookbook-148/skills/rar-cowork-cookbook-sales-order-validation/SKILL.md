---
name: "rar-cowork-cookbook-sales-order-validation"
description: "Validates open sales orders against policy: pricing, credit, customer status, delivery terms."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/sales_order_validation", "rar_sha256": "bb8d0dfd8674a39fa2e8f3b14616b168f209445bdc870d6c54d5cca7015c0e63", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/sales_order_validation`. The original RAPP
agent is preserved byte-for-byte in `sales_order_validation_agent.py` and in the RCI capsule.

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

Sales Order Compliance Check — Validates open sales orders against policy: pricing, credit, customer status, delivery terms.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/sales-order-validation
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `sales_order_validation_agent.py` and embedded as the fenced Python below (sha256 bb8d0dfd8674a39f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `sales_order_validation_agent.py` first:

```bash
python3 sales_order_validation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 sales_order_validation_agent.py   # or on stdin
python3 sales_order_validation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Sales Order Compliance Check — Validates open sales orders against policy: pricing, credit, customer status, delivery terms.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/sales-order-validation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/sales_order_validation',
    "version": '2.0.0',
    "display_name": 'Sales Order Compliance Check',
    "description": 'Validates open sales orders against policy: pricing, credit, customer status, delivery terms.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'sales-order-validation',
        "upstream_url": 'https://coworkcookbook.com/recipes/sales-order-validation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4e4ccc9ad4063bc5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/sales-order-validation', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.556, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:check', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class SalesOrderValidation(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'SalesOrderValidation'
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
    print(SalesOrderValidation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/7V6+bPaSJbuv8K780O5GttoX9zREU8SICSEJEASgnKFS/u+b0g19b9PCrBdNV01PR3xHtfXIJR58jvbd06m7q9vVteGRf326e3sWfmCt9I0Cr16YeXugiuGok7AW5HY4HfhFHlbR3bXFnXz9v7N9Rqnjso2KnIw3bDSyLVar1kUpZcvGiudP9auVzcLK7CivGkXZZFGzvhpUdaRE+XB+4VTe27UgveuaYsMLNu0Vts17xeul0a9V4+L1quz5iNYzbtbWQlkvn366ef3bxH4/Pbp1zcntZpmBj8vp8yrvXDMoN6/pVYegLvlCHScr0uv9os6A1+5nr94Xb1rvNR/v/jb35LBqoPmx0+f88Xr9flt/jl1+aINvUVbWE3ruQvHKi07SqN2/Lhg0sEam0XttV2dA02BBjVQ7eNz5ndJRbn4x3zv3XORj4HXvvv8BkxVP7B+fvsRGAusV3fz54+zlPLdjx/TYvDqdz9+l9N0duw57SwMoP745XX9EgsGfh8a+Y9V/wGkPl1le5/ffqfc/HrinvUEM98+xkWUv3sKLuui93Ird7x3P/6VWCf0nCSNmvZ/Jfenp+DQs4Cb3r2A//j+YeSfF8uXQt9k/vWyJXDrv6MJGP51ufeLl6H+SvbD/v9NdBrlIJa/WvxPxf3ZhOU/Fj/9pW7/04T3C//z2/qZAZadep8Wv345qxvupx/c71/+8PNvQPS/FHMuutp5SPiSWXnke0375ctPPzSPr3/4+acfuhLEmmdlX7o6/TOZf2bXxzp/sOBr1Ls/zgXr63mSF0O++Bbpi1+L8v/Uv31cPBL1+/fNp8Xv82V+LRezEl8XfZrgdznTAKy/s+OPb78BXgA0U3fO4zbI8v/4j8UhcuqiKfx2cXaKrl0AB7dR5s3gtTBqFuDfnNu1B+zaRMCwr3Eg/mcPz4gLf/HL/3UeZPjBeZHh6kFwXx4E96X/xjm/fFxoQFpRR0GUW+nixKjq59wKvLydVyprr/HqHnCIPbbeB8A+H+YPiyhf/PLnAr885n4sx18elBw9mejECTMLNV3qfZw1uYSAcp+4HcDi3t1zOiA2LRyAwY+A4PdAw6ZIe8Bis9ZNEqXpwo1qoGIBaHaWDSzzaRb2yy+/2FYTfs6ftIkunjTfrMCAb3AWHz4AZfw0CsL2c+45YbH44dffflj85+J/mvUQPq+hAtp+2R0gFM+KvAB51GVgGHAJcCIgiYfdf/3tZVIgJgcFAngp8iPvORnEYeK5X+173jEfEJxY2B6wK7BpVhZ1C7h4EbUfF4K/+IYXLDrfmtk6LEBZcj1QsVwvd0C5CS2gzjdL5kULKlkbNf74ftE13mPVX+z6Uc68DCS01f6yOHAqqA1FCv6bYT4GgclFHgHzf/P+83sgpP6hWbBfRXxcyHPkLUqrtsqwtl5r+NbTL6AmfJ0OhFuL3Bs+53Px82ZTPSLkaR4wCFjGebn0w+xzUK8zkPNu83XtxxhrrmDao5LVn/PmFeJWPbvCKR41N+hA8AHi//srpJqw6FL3YT+AdJb08oL78sojBh8lePGowaBlABCjWcaCmzlv8blDIBhb/H9tEmYQDM+fNjyjbdaLjaydrk/jzI3LbMRnrwPq9gJEyDMRvtfyr0zwlRA/52kEPF2Pf3+OfJj0NeZJMh0ABjL89JAPwANos9xHuM3hU9dzoFqf86/M+x548EEzwOIgN0HsziHzdcH57lekIUjA+fp7FX64p3bnTAUhtSg7G5hp4Xuea1vAwG1YzynzsjOIPW9OnyGMnPAPWi2AdGAxIH8BQEQgCQA7P0wnF0BNkC1+XWTfh0dzbwNQuJ0D0ILO0Pu4uIConz3fgFQDDco8Bljhh4eoReYBGwOI3yzchFb5BDM3ky+A1ky4kTf83v6vW9+j9IFkBg9kWiBsgCWHmStd7/706zeUL08BodkcRI9Jf3T2S9PF7wvE3z/nD4Tf6BmkazrX1t+Z5hlbD36c2aYBjJF5r/ABcfAoox+flfBZar9h+fRP/fO7f6/FftQ2/Y9++7QI27ZsPq1Wz3r0tRx9BLm+AhESlV7zLE0fHmn14Xsl+YO0p3E+Lf49RH8Q8QrkTwv4I/QRmm9JkePNkfp6AQNwH9jrB2y++zk/ed89C5YvMoBqNvgIauG3YvF1CKgYQe0F8+Bn8WjmmjOAMvdgS2D7z/k3778yA5BxHsyVril+l7GPqgl8+XTVN1IHt/IWrO3ODBJ48w4jneE33tunvEvT92+5lXl/vbOY+RqEJbDBvA0BCQK6kjbyHldAF3AjsubPf9wkKY8PVvoMX8BjuWvVDxJ4pcOLBN/PLWkOCGRu/+ei9CRwsGmxurSdwbZjOaN77jbmzudbW/TPqz7yFazhFp/mtH2/mFtYwKdfu9GZSZ/7g8dGK+/ABumnuROe9QRDwdu3sd/2fbb39vOfwHg1xn8BIpopYyaZp7qe+50PHs4qrRbQnn6SAKTCebQDcwlsxkep/Ge1wYK1V3Wg5rkz5O82+A6teOL57aFK+9z9/fr2lVFeznt1emA4SN0PzVz1ViCswYLg+hmA4N7/sgd8zQK8B7oRMM22KRdyfZciSMxCad9CPMpHbRgjYMKGCcpHIBrDcNt1KBJyCQfHXNxxLBKCcQfyCBTIewbvl7mgRzMSxLIcyiFhzKVJi3A8FLJRx4MR2CVRD8Jp1KcoDwNG+TY1AbT5Uu+pzmy7b+3obIaXlr++2QQGRu6wRmCeL25FGxaBkPYptJc14V1xnziim0rPxitrpElP1GUnJ5zNJqRV5MzWTSKlFJIS/IQFEsgMighqxvs3iZq2NJEoCowsCYW9wJ2TaWq+LCFpe9RYgjPVkLf9anss3HTbjNA0quyuuUbKmV/Z9UQuBxINMh3GQx3m9zmfTT2xprN+A6dk1l22aXJok/6yTxOhV+GUM/alJHEkXJr3k5W4zqW+JPRtH0u4UQV0hWkWkTOQkq8IWqlHws/qcVwB/WTTmJYbUjb4Zq8Je3xrxrJvlCk3IrVsFEYEJzfQTSvn+6QENzU1r6boEXoh9ic8O2wNnxRROz5nNmdTPK9UaeUcLt1UUQfPZJS+iJp6IyE1I4bl+ZRgxKGdlsbeUtcqf4uNpglvRnRElS1kTOYFIvrccSQknAi9QovasbacyG7LSN3QO29L7iCWtbnbjt8JVStX3JHv0ex0xq/NZU/G+oCoZnLdg36oOKBMsJ8GC3fXN4eSRtHrEb0wEPQ6iVudowkXZmIMPRbZ0bdX4daQ4TpNmiYTd964XiIsG12GnVtWMt+Y9fpMtWJhTaVyjpbpRTJhLaHNoSvWEXEC+S7c7uuYYoUlkuxy71x7F61B0HWuBQp3MQ+WQ5x6c3R8oXDCqy6Vy0O8dyjNLBE5WI5ocGhIm2gEfGM1V3d5hTN+FdnU3b72VmgIFTPdU8JS7y2/7VlEWIZb3Z02S4GWzaDyGsLDjolIhp04cHhqj3bUcZWhHlXV7iv9Ym9lozTIA44leCaF09UQG3zF7C7HgpaHDXQAvx7SxhwhIpGR0ZIc9xjhSoOWt0EOnfPCyi9quheLvQP1yJpivWlCl1fV0SJiU0F0oxn30/WQWBIqydiUn4FP87proRPVG7dIuzXx9X5107zHpPJ233spBcuxc9K5EfNTS1BvMHRMD5vCPVgctBmXN1zXeLm0Jw4+Z+GdrS4cxp6KMR6FU7olhcmNk0g4co7tbZXhKuyim5ZM5GEIHY2DiSn3uWpUVFK9ZLt0urDy5h6cTha2vytLSz8BRyRqTVGwVh06lRxFhV5PmX2ghAqSd6RO7nQUyd07usa6+yTkxAq7dCpEn8J7zPWG2opbI23kxtw61sDlcMgHYrPtveK6ahFj6682Vi0LvlGnxuZsMKe8CJylcE4SllqhWdtxnk1W20vmxQVEeapQ7faUK94TZL3qUpZMKncqux2iOZCYEuKeiw4TSANTr05L85qgrXEcWir2k1ST7vF+OApVwCiaRi2ZyalEfJKMQ807O7vrfeTa8LCuIgmmUnvRGIgO9MtrhbpQWysS9KW/7Vc+so8YkuwiHmY5yq7Lc2yEEdtlB+hMRfwRj/eTrMjWLcpCM6jLql3j/ZC4B34VD6dqxekU5RNGdbigJqniAtSK2IZV4wFFvWlwlg5yymtNsjxmhblHGl/pR6KiXYiMg2gXoyN267uQzuLTumFXUJJjBySLBVa7TDA2rsdxl2eoQp+IqBmEA76/3XMMLTbE4ehL+4Pc6huf20RDjyyP1CHFw0G71vry4JsTTGzLfH0nXCVBttnpNjB7zg03K0YUqURsBa9cMcpxubs3Yy+J7DraiZTHyWgLQwlk2TBfS0y5uukaBZW763k/6fvSkhx9BYeGAzc0qyiDjk5bvlD31p6u1+tbxyujfI31RuMNNh7bnVbLElpl+cG9bRxahPvUnEasy8klJYr7wh4KgKNf+oS8l7l6CRpNiTzyW4HAN8dmRa96Dg773nGPk80O0pgIfnS9CclquS4HWt3llC0KS6cg0/UR2yf40sJGKdg4QYiV18NOTqdJC1r2WKfXsbLlSoUx55j5fHL06AEygyiWDOKq7hpa3jWD50MF3pq37V3A98GRvG2GTTahjtqudwwpkBG83xDMrsqiSj1fNwUn51V15U+s7/a3YxzHDlOoaXDAb+LKgpTLlRZ98aqFA5Q5+9bw+3O4OdtnvMakXQYXlrk0PUpy2EnfbFF/5IZ4l612cs4raz9an9PdNuxNycVyod6ePIn20CuCVRoB2JOjuK5yhd3NEA+Ah1aXispIkTxv4oiAQBE+lZK+2+LSesudNDuOyb4kHSwXx2rSb66+32XoMo1X+m6j61WsIaJ7Ji4VoHy46f0xO/Vb5qBRW6ePoa3sFkHKWfhJMy/RvSkaSY1rJtiMpCg4qUBl+hGKG32LbW+n0NzlNX+A0QywjBb0jDGexmRKd06/hyP6upP9kJpu43AWNsndpZcK0bpINirBPi7Xa/ZKnM9Oqdu27V7GAVsqmwYPKlhNc2fUJ9gfpCXtjHXYBCmPOziPIjelc+uz0UmGYwRBcTPHUTIE04uhY7jZLq1m0A1gaGvPni30Zm0qOk5opXJyYdit9lGPyFo1ans2X5ICo6RYFbqSp0t73mKohs9C8X4tt4kzpGOLiNs22bOJMObx7ejLUleaS0i0jm4loCW83EbBcpuDXTrCp3leHeuA0ydPzrM12iCVITvpOb2Hkq/RPUX7nWbbx81+D4d1Evdnsw4va2elESOS5dF1QhW1vmm3XXcjO7y5iIlniEo7uK6YKCZ3otnGP1Ok49yu5/LKSFtWQEbLiJBNeQGh7ArRoPFJYzJ6b97vnr5t77egNraYF12m/kxtqzHmJRf3MmxvHctgvJ43VWiJiojVh96WJDkzgx2358TgmnpjYbOsVSzZSyqcTpoM8/1pvF1Ga7MlBA9P4qTSDuUont06Xm7WQogFGqweN8zJgKGqPYg7dhUKMp/oPY26p2EjK03QBmuXPlr7ZUnE19QMGSZT8NV6ZQXkUc4YmVGUq9EKAYVLoF+W6BDuZEKQDpTFiJcWdCDhhUWPgoLuyHMquJpWkOsTRXvJhI/oNQs5JBlNpT+slegoBk2X7y/Mjuv1rZSgXKOAMrNX0pXoLsNVz1T0VI2QvD8PrHaAT6yOYhVPUznEXXTU6I6Gm8c+IoqX69QokCXxQ3Zl6j43bszkx25T+RhCH1jKmfh7NJg4Pt6uN9ZO1lFWO2UythuBF6kbXoZ7MTpEeZxBkhRqsn+38EiuxLqM99ot3iNZLeYufrhAbKnhZTfZFbHM8P0KTguBxSwNbZQrUvLDmsTWnc7YG7HqzqvkLpWdbq22dZlYg6nZ5Zba69IdISfF3tDVaqXLksyLZFS7B0wdL2phe3JmJZgMV/3VGYSggZmoPMsoYq+PRS6cneAQWK5KdGRNnrUWVPFKY6pYMa8Dg2zStcec9CmFhvhG4zi5jcWtKW61IbqJDg4K/3UojqIO9YYh6fAgnuRzHaspiABuFW3pimoSkcha4JYmVCydO7tHGYoY2uSje1bY9V1k3JbTrTZjgsQHoaCbypD2xaqvsrjykl2PNdzeuh7UU0hv12LZC9p2n7kFl5ZI0YFthAortwvrEcXhGBpDaMSDee8LimNZGGujFLlu7rZ85nlhqwpq7hcBP3Hm3dn3o0awyeHqn7G9zYPqWyTn7dkIL2hwzkdTPiNIoFVIuY+VyjhxnZXGPu+c08K6YeGdmyaHM9bwVl3TrXghr8fGWgfHQA/JzW2bZ+4VGsUDEh/WVOU7SXi52Ea4JXh+U3kdbSwZi2856MoQxt220UNCFZ3bHmzlit/KaTINWdHaGiJ3YgeSy1S761a50mpOXodgfbHX+Xg86odpjCsLnXq8F3vpTrlXvlh5KZ32Hpr7MUlZQasuqYxz4BNyN33HTClF663dBePZ3DZjJeA659zl3rQXbyV1kiBy4rL1/rrrcMYoHM3IbwmEqQWC7nK8B4SudtwgXyU2v9irndRYhVp3XNBu4xOVwyIe9xR6uTqZO9k5rwpcpZpk0x5PYVtBTjm6Ki5mcXvHXOqI2e3+kmWpVRBcuEVPClpfPJNXSZzTGvZqwEhNmDl2dw6rdS1Nq5ilDddopQHekdR5dYeEA3ObbiYmTw1k1cWaNY44igU0fdlrgwKDghgL/fpI6whDKquDCWWH81ouuIhyc1oV62uR7ZA1xo6nw2jfOSfkNdXJpbOC3bAD55jseONPVWjYqbsLMIe25UZYN/fRiXNFoYYb2B7zJFPcm6FeZie/gUstgocDZNIkjkcqbUwc5d5N7DjY1xT1BGanNnXTHTMyojRavupRiEx0DFNljJBH/dKj58FkJuPk9sqUhqBpVmXIh8aauvjWnapPRUBwpCmzYsHu3f0OMTEzZ+7wbeWi8EY7QqRvbS5GKqtUbt5yweantpYGytjXLg6hASFABEgI1zfzRjqt4ixihtXtgPfH6ELyMtIfi2uHGZt7EuvyOjmP9JaM69WgnQsBdFgxccjIRIbPjdcX5yhg8+EOm3Co5FwHSDg+3mOy5DajGMp4eNERSsPva2w9ngnDZrmxFHf7bNotew0aHHWIOciH2TEyeGF9Kgevud8c4XTVcX4lUWuOOa6kAmwSV3XD4jdVa3b4fUks1xSm8bulZWQK4iukRd6SFsmmgBZx6NhM3Rq3pTo9oHaKydb5bAw1irFYSuwlZuW6rmaOF7RHpdCmTutIkzFFrsOOvTQ5gwCV/djeExI7GMYA2XghL5Xz6aLc3fjI4oXENnpuh5qzUwoYz5fGRQZtWrOntwykuMItY4tl5xWTJ53oyWFgdji5FFXI/rF2tIER6h211okaSte4ckpoYcsohmYc0GKLdWXnUYd2xfAdahN00DG7+6rqSdaXGw+ry7xXl7Y/2Qrj030eQuddztjo7uDR/cSN7QqDLtC9ipf3mx7QmXlArQPdnPTSREgWXQ0g88NExlB6u7emVkD3p0jdmN5m7zO8ujf5hs03nUcbO/VSHal5+6mDOnBy5VUvAR4vDodUNA2SIvbKOtwE7fUCGS4yXrySbK39KYN1YVInFy139jEZwUZtqgIdUm0vWNNHozmHbAJLIghu1tXUdgViUMoRhISg3Mj7kpfuFhtQJ9ONyUzSoW4IqEN+ohJY8bZrWsDNdcFsk3HrdC6TZIpi6lY+8qsEOTlIkK/TfXI/URIPk+mJSGmZqHAraGj6iFVLTnKzyWJyGk2Dcri4uDSYpGhpu40Ydh221MOJQ3sY8A9K8wYyMbcgk5fJXSFklpTsoh/BvmWb3lK7Pazga8HgqKkFVsEiDsk29FHPQPvNi4HW0BwUIEK3SXeJrljKjUTYQ1zgdw1sZO5HFD7cW1Uk1BXT8rmGOfz+yDBv79/mI9LXqfS/eFg8n/v9Pzt+fJ4Ufn0O9Tga9iz302OtT/8KyM/v32onAjCex6lN2gWvY8j/dpj64c+fWsxzxuez1vnR2L39ejzfAr/NWKLc7Zq2Hr80Rdq9ZthdM/+FQjP/EYsD3t8eCmTlfHptdW40vz8ht8UXx2rCt/kvB+YnPZ4bWa33ugzqrxDcEdg9cpovKIF/8epyVuv1/GM+jZ0fgLz99l84nuPUTCUAAA== -->
