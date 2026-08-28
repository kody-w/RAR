---
name: "rar-cowork-cookbook-audit-insure-assets"
description: "Audits insure assets records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_insure_assets", "rar_sha256": "27018a2610fcc6d3c6ef950ecc82e59653083c113a65236050bc08ec23dd4390", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_insure_assets`. The original RAPP
agent is preserved byte-for-byte in `audit_insure_assets_agent.py` and in the RCI capsule.

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

Insure assets Completeness Audit — Audits insure assets records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-insure-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_insure_assets_agent.py` and embedded as the fenced Python below (sha256 27018a2610fcc6d3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_insure_assets_agent.py` first:

```bash
python3 audit_insure_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_insure_assets_agent.py   # or on stdin
python3 audit_insure_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Insure assets Completeness Audit — Audits insure assets records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-insure-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_insure_assets',
    "version": '2.0.0',
    "display_name": 'Insure assets Completeness Audit',
    "description": 'Audits insure assets records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-insure-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-insure-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '05d7a5efc476e910',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/insure-assets'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/audit-insure-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditInsureAssets(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditInsureAssets'
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
    print(AuditInsureAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/7V6adeiyLLuX/G+50N3H6pKBgGpvfZaVxFEBEUmh669qhmSQWYSBOzT//0mar3VfXb3vmevda81KJIZGfFExBORib++OW0TFfXb5zcDOPlk7aRpHIF64uT+hC+6ok7QW5G46N/EK/Kmjt22KWr49uHNB9Cr47KJixxNX7R+3MBJnMO2BhMHQoCuauAVtQ8nQVGj2VmZggbkAMKH+LJIY294fh87uYdmhQ6a30zqNgUfXQcCf+JFwEvgJ7Qc6J1RAHz7/PM/PrzF6PPb51/fvBQt9W35zWPxxWNtNCN18hDdKgdkYY6uS1AjRTL0lQ+CyevqRwjS4MPkP/8z6Zw6hD99/pJPXq8vb+Mfvc0nTQQmTeHAZtTIKR03TuNm+DRZpJ0zjGY2bZ0jqyYQAZSHn54zv0sqysnfx3s/Phf5FILmxy9vBVLBGeH78vbTBCH05a1ux8+fRinljz99SosO1D/+9F0ObN0r8JpRGNL609fX9UssGvh9aBw8Vv07kvp0lAu+vP3OuPH11Hu0E818+3Qt4vzHp+CyLm4gH53y409/JfbhmjSGzf9I7s9PwRFwfGTTS/GfPjxA/scEexn0LvOvly2RW/8dS9Dwb8t9mLyA+ivZD/z/m+g0RhH7jvifivuzCdjfJz//pW3/asKHSfDlbQXS+Iaiw03B58mvXw1N4H/+wf/+5Q//+A2J/r+KMYq29h4SvmZOHgcANl+//vwDfHz9wz9+/qEtUawBJ/va1umfyfwzXB/r/AHB16gf/zgXrW/lSV50+eQ90ie/FuX/qn/7NLGdNPa/fw8/T36fL+MLm4xGfFv0CcHvcgYiXX+H409vvyFSQORRt97jNsry//iPiRp7dQGLoJkYXtGOzJI3cQZG5c0oRnQFH7ldA4QrjBGwr3Eo/kcPjxoXweSX/+09qPCj96LCqTPSzdcn2X19kt0vnyYmElXUcRjnTjrRF5r2JXdCkDfjMmUNIKhviEDcoQEfEfV8HD8gwpz88ifSvj4mfiqHXx5cGT85SOc3I/9AxI+fRhuOEchfGnuIvUEPvBbJTAsPKRDEiC0/INtgkd4Qf432wiRO04kfI2JGLD48ZCNMPo/CfvnlF8S50Zf8SZjU5EnvcIoGvKsz+fgRWRKkcRg1X3LgRcXkh19/+2HyX5N/NeshfFxDQ9a9EEcaysZ+N0EZ1GZo2KN2NIgeHoj/+tsLTyQmR/UI+ScOYvCcjCIwAf43cA1p8ZGkmYkLEKgI0Kws6gax8CRuPk02weRdX7ToeGvk6ahAZcYHJch9kKMi1EQOMucdybxoJhCFGQyGD5MWgseqv7j1ozyBDKWy0/wyUXkNVYUiRf+Naj4GoclFHiP4313//B4JqX+Ak+U3EZ8muzHmJqVTO2VUO681AufpF1QNvk1Hwp1JDrov+VjzwAjVIwGe8KBBCBnv5dKPo8/Hioqy3Yff1n6MccbaZT5qWP0lh6/gdmrwKNJIlWEStrE/Uv7fXiEFo6JN/Qd+SNNR0ssL/ssrjxjc/KHi87+v8o+iPPnSkjgxm/z/bRBGTRbrtS6sF6awmgg7Uz8/ERq7lhHJZ6ODyvZjsUc2fC/l34jgGx9+ydMYubse/vYc+cD1NebJMcgIH+W4/pCPtEIIjXIfMTfGUF2P0ep8yb8R7wfkxgfLINhRgqIAHuPm24Lj3W+aRigLx+vvRfiF04gKiqtJ2boImUkAgO86XoK0qse8eQGNAhCMOdRFsRf9waoJko78jORPkBKjNxA5P6DbFchMlDJBXWTfh8ejg5AWfushbVFbCD5Njij0R/dDlG+oPxnHIBR+eIiaZABhjFR8RxhGTvlUZuwkXwo6I9/GoPs9/q9b30P1ocmoPJLp+E6DkOxGtvRB//Tru5YvTyGh2Rgdj0l/dPbL0snv68PfvuQPDd8JGuVsOpbW30EzQbmSPWNxpByIaCMDr/BBcfCoop+ehfBZad91+fxPzfOP/15//Sht1h/99nkSNU0JP0+nz3L0rRp9QhkyRRESlwA+K9PHZ5Z9fGbZH0Q9kfk8+ffU+YOIVxR/nhCf8E/4eEuJPTCG6euFrOc/Ls8fZ+PdL7kOvrsVLV9kiL9GtAdUCt/LxbchqGaENQjHwc/yAceq06FC9+BLBPyX/N31r7RAdJyHY62Dxe/S9VE3kSOffnqndXQrb9Da/thLhWDcWqSj+hC8fc7bNP3wljsZ+IstxUjXKCARAOPmA6UGakeaGDyukCHoRuyMn/+4N9o/PjjpM3BhgzRz6kf6vxLhxWsfxl40R9Qx9v1jTXryN9qtOG3ajJo2Qzmq9txmjC3Pez/0z6s+MhWt4Refx4T9MBl71w+T9zb0w+TbxuCxvcpbtDP6eWyBRzvRUPT2PvZ9u+eCt3/8iRqvjvgvlIhHshjp5Wku8L8zwcNTpdMgwrN0BalUeI9uYKyAcHhUyn82Gy1Yg6pFJc8fVf6OwXfViqc+vz1MaZ7bvl/fvnHJy3mvFg8NR0n7EY5Fb4piGi2Irp/Rh+79T5q/1xREd6gTQXNIFifmDskQeOB5jE95DAg4GgeeNycBzTE0hc8pjyAoh6FJisFp3PXwOfBIyvdnFDeq8Azbr2Mxj0c1SMfx5h5LzHyOdRgPULhLeYAgCZ+lAE5zVDCfgxlC5H1qgtjyZdvTlhG49z50xOBl4q9vLjNDI6UZ3CyeL37K2Ug3xdWXLsYyQUEETLckO3q4yAcG66F66Fe71DpY5b4TV8eZKTYVSZO6bFnNFez9LC5AGAeJEZzZkm0IeN8vL0G63EZLlzpRzEnh7slZDderXjNtq9icCb3UpZw0L5q9TY3LuZtVpOzHKYdhTYqpiUxx0bkaivoci/Yx3kacWTn9oOwEnbqxJxXiXZURvZYaoniM5aQpbX6Ir+eqNc3wnK8I1s/znt3fiV4P4hk81QPGrean6uqtQrG3lU3V9ElksFQgHmncughq6Su5v7gHfNu3Xrk7GjEtGTpz9KJ4yuntaZ8KmEGdLcFK5c1VpP0kTTpfqTJ+aMO7OO+3Qoxv6mG1Og+pcUv5XDoUhWvrsV8ailxkrafUGrNPayJYMwnpr6ibGrW2WvLHntT18DI7xWQkKqKxTdktsyzmoaWofMLc7U0K5dPZlY44Mw+jg3K7CMfZYgmTLWkw60Hs88Tg/Ng+mu6lVjOIrbB2Uy9o/GxvIzNwDb1EwMfVRYY6BcNpuZBjh+Tddres7fieuHkq822bmZYcX32H9QumxPx6rbQH2aEjsYhyQd73yt4OlzSZw1OZs3Z0p/FuFaa3YWmy5s5hzOt92F0PxzRjvBWdDK3h+RAbDN2gYwI/e4XtrolrGRTcrtogTe172oQc01Wb8OjzwXqrcY563686ZR/RaYrf5pf5+WZvBtHjuujsktlanvJ0xuJqW90XJfpbB36MEwLdDneVgPuCmp335j5CUbMN+iU9L1X5cLJ61TV79WJmtGwPyX2+y1xHlO/SHZqruSDNFnwTMFas62wxTbR+Pr/lVIJj3V6JrKsp9qjzskvj3LBze1Dw3mKUDrdYLt34QX2oiHI+k5szlOereSCq8SyNDlwV3m/U9X4eTga8R7HtWFYeJxoJwXF13KnE9uzyVlqHDBHzVNQkfLHTQxis+laMNxYlsBte4BedeRmyRRYmSoadzUtmKfF5fT9ZbGoflwR2SfB+7jodlnLnqYHBaRG0153qSadGaG+adiapQd/PTnnrSKGiYiXTrSUPn4pJzZW+s2QUNqATBQv4/LSswC0Kr1ceup6CD0ebN1ceP6yHeVmcs/my3OSdcqdWPUkAHIV06QGJWZNp4c+HI70a1EorKmtWHsUjnFkShvXVnj5eJTBEZ510+2YAmsjUm4jSJKswOYa5nxOCb9T7SUGbY5lUDkVzVJZnC3B4XJPMzI5d2POl6SVkPZAmwyzsYyKQ2yDvjohriH1hW8GxO+wpzpnGlzOF9v5XvTPpJCSxkzbfljOgi6eCp92kHOic2h4O25M/N8hiczwzW6NE+zmBWvEXKKbLY1sLeNof90UiY0d5Y8/O7WoV853S7XgMLv2LGWOgja12l90BHThi4XCJfAXKVQPUXfPOLKw3lbBrZqtwT6xO17mSEHq9zz1BPE/b6XRBcNgKWueqKaTpmc9rkC6Xw7qCyyudSkQUgNmBJSRDvXXFMim2UrByevNA8/OLwNbrcIN50qzVbhyYLbd7Io4V0txjwW2GqFsRZZzbQ1mFZnC+Y0tjm3X3/dXaxiS/2U/D3QYF/XnwrkZ/jQVZBiuJKiWVsoxa39fKoZyfkoCwZM1xnN7ayvshEKZ2xB3vUBW0bWh5uw1u6laYoF4uqklJOWXwUF0uUO52+PHadFlJU+wq8mXUbxm1vL9RJdJNionDUdelo7k+EBduOndtR9aH3L9kGa5tl/d+08sMcwOS23UdU9Epyc+EZOPNwbKfbiOstgNTLvGpRfUco1NrKYzKPQYMNklxnl8cOKuK+Wzg0nNkRoXINL54SOnTbLbvzJ3Ob3RQ+G7I37Z2OAfaJZmDVU9zckS629a4KjDk7TLxZoZDtzhweG9BhsmyPth9d9uJydHaiKo8jbC1qZbIsTJG7dItAOocy/iZGAizpKpDV6Luphtf96SjJIcQaux8d9nO9rPmtA08psP3znlPicNxfadRFkx1UvX1BUOeHRpPei1v1I28hC15UGeb8+G2SHnK7JV0K6f+sWb3JblVkuQS2Mu6axZB0c+tXAEbw70R05V/3PWrQ7QLXFrV8Eu8ipOmFY7BIjqv022/zYZTSmnZTp+eyaG09BSaJ2ldNEYBI35lAIzYWKXcC/OBPvsoD212kez7cGHn7P4ousU1XeNl5Pa6SrfcXPIlVRaKdJodgGnQ+0N8kbxqH8q+Pjvn+aYU7XWGe1oQEVFhGExnpBQDDRHeBEL0CmsqVIsmFM6cd2zNS9vME6NNNvE6X6NqZ1yyuNbLinC3YYqVYrS1xRJ6hndPiTyk8GHuFJHXSFLZ7M4nG18GDlc5tVUsBc6Yo+az3CuJu1qcw327v6/krN1mtC0I8m3OdEUPApzZDGC1NOfbYSoS5NUWCjtjIVQ7KdVF/spmlw2hS7vQrnb7WrzEoV/YS9DHF9EYwmJ9KDyPMMo5DrBEcw9pucTKDGv9Dp5dCmcccd0NcE4fLqjB2d6VmkWVm7CrYzaka3+btRE7pQmuqQmq6yzV2BzozQzPK1oKqR2+hlxfsY3H5hIOMQiphCMt1o27m2ztdzho5DnPGv58uTxZMXPRxQ41IwtJABE++OxuvbXaFWtIsaJu+osSdVC6EvN26x0LJlJEfg+MYTBNQawGklOOYbjQfItXHUvidzvStofMQG0rKd09vrb2+GJx1TczEKf6svWK5aHZHIYqdrZn7CowLV/AY7kMYrPyCm3Iac+6GxL0pMOVFvLtypG7sKg8G8hGxWOD6q34MmBu1Pquro0ougpSHV/zOgv9Mtrd+I0wU3VueQPXWyjYS3Nz2G8uaEGSUWONUpqIamVCtO/3IOStWkl9mHYbJpLJWeAcy5Z3fO0QBhpF85WFp8QO6k25yO7snQeSs1TljKC93lYDYStb9v4GtgfaISFO29hu7opmYYMLcXGylD1vo7JPaMPovWagL1CCaYn61At+sWs3IUyePUSUi7cn7niI0Ih6tnY9s0oJbIFT/n3bhweJLV0BAqFO5Bi0px4qN2sjbOCFovho1R11CzVRQlomd2uggm7dC6nnkVlxJpuGHy75+boGs9NWA7veBafTjJJPDGyWB40fQB/dj8SGPLhg4ZPRIY2GU3zivMMMByGB1QFymKsyM0OZzcr02kxzcDxSjLU7yyys/DmuDXJgkJ6nkmXn1jbYiAt9caOFazWIOKnIvJ2fDWNhGG3fbVtZmjqrLV9g28OiSjenDdoR4NECLC62KeJ9cZepO4n6bwsUtsZvLHFILV0OY3EDUG9QiG5ndaKjeuxVPcqFtLqGYu1dZpF2JpqA7lL5bnCxWC3bxFpXTawsnai9CVmJx3ERYLtFFwWLPW+dwCy9UT6s1jVc4y6cwbXszTqt3hAtT4d4citF+XKQFDNtPA9q0lEIjpE3Q+1JaB8a+9qdlEA/rPnV9e5eVrC7VIMjCPvDVjeCPaUvdqV4g6EydZSDZS6vO4Wzbb9dXESnSuR1X1vt5l7i62rlG/3OPskq1/FdaRHMvVmf5JKscm+j+jA/acWBC4wud/WU7wWFj2lLUOX2utfp6Go1HTz46rCcMjFxOfuMQBwUtHfaGhQFxbpI+yIU79W6L8m7jB3gWCC3gOTiy73PT0mlZju2FdaduSwP3Ey/sFe0y2z4bLVt4+BWetjhQvRSQsE6QyGJGrpFjklhYOZcU2r91OZheXVb5RZkpz21JAmb8vzZlLykOHdgSOJW52vRjcziVF5Xq8q3Knq31xRyc11i0kKaX3OvZg9mvpjNqI52d1Ms6PzqtKgvxlkZGnXe9lWf65699u7HEGiMy0sadpt3REitLVeusIXNzhutJ6JKSIqey2ntkGfDhqD02f26zOb9ivOrZXDkCuk01Dcp4ZtGkkkh31R306+p+WW/ckKRw6ZhOrV8L92vc4+4T0WKcOd7Zk/PbjQT9e6ukfiF017qxvFad2nMbsYVW5RURvE42rUGVxOPVctf1jzfGTmnsFAWUilTWJ7XtUHpl95ya2iBphvAO88KUbuHtHoV+4PopL4UHIBfLJtiMEMC5kiHed9Pl+p1l9jn7GxPeW3X8/hpZnucJE8DzD1fp1lwuFGejQmqygQqqy8WQUvCO62eO5ZT8TSsrNYJYienVQy1hTExzzJ1yjCV3JQMiJtmHdFthOW2W13ZoyYaOyE6H6tLaO7CpVmGbBAsDZ+jfGSNaemcZDR+ol94Fzc3ItFfdg7ppw6Qhtpmb2rmaYe1cpLgvZrNudLRPAs/ePtAKMlgeZI6WKfOUlDAId4QAnvZXFUdm9PTSKFohu9kgTOFaRCB7XFIe8nGVRlTXSuwEtqr2AWiyNA0e8hbgxztaHi0yLlJ96vZajAYG3ljKNfSNjclBhFCP+N4qB2CapXA5CATWcsxrmB1uhj7BoXdwoUC7ncVY1h+qnirIQb52E9y6Vy89MJOu4Vc2pLekXVYId/163vC6Qx+gPd2hbn3JtVOSrbZ8dX5Gp4anO8V/JrpGMMwfJ1wt317XLOzWBLWPoXv6hBbHmGuHU/EKrjWW0YBnW13VN2zNC7JtXI5q/Rh4eHSjdxeyxsGV/XFmQ/U9ppll5DcWXFHLGtNvXT+zu45qe5juWEXi6JlPG/DSVsm0UNw0ITzLZG0nVPJudypWrQoIqZkzJYTTzuxcdlY1OY8kdH+RUCRd9S8Zlp1GJGzpb9HbpjTgNPuK+06n5OtNy9kj52KW6kkr77Epp2F32+Rk6whyUF2sWq2NkhPLpRuU1USyXVAXb1uTWNos+FtWsv0BMddrKe8dYQys9z7mJNLVtXN9GJgT+xi0DGS6sshN601byRsNcd2orTsEIpQ2m5b9ixqFiR9obs7lVjmRDtLYq7ggY5aSeKwbdfNzVpgxT6TF6HppKhBOwu3Mh8w1P6ldzZomO2pNnP82hAGF0L75K+wRElmTaef93nfpTYGhBUnsKdrshCv0aqVtpF5XUkKszNoOxjulr2r6Y42StUK+L4BtAXKwARVeywULbD221sYk8g/4XIKZsXWk/PAmEsYm+XHfji7NdTojXffsZwX4uS0HDIctaZCf7Nm8ulYaaLrX6alxy/94/TiKFe6zi6cyef5gfZW/hKuWmd3gyvhsNPUaMP7QQQFQK8P+xSH+U6ayX127TppbwCkO3/hnEIrL9oyILqOnuqwXCwWf3/78Daei77Oof/V0+HxsO//2Znj83jw2zOnx2EwcPzPj7U+/0st/vHhrfZipMPz9BSmbfg6ePxvZ6cf/+TxxDhheD5WHR+A9c23c/jGCcdf+7zFud/Cph6+wiJtHwe2H97cFo4/Q4DjL1U89P72UD0rx5Pqxxrju/c4I/7aFF/9GJYFBG/jbwTGhzrAj53m22X4Oj3+8OYPCPPYg18phv4K6nI07PW0YwR4fNzx9tv/AW1SHoE0JQAA -->
