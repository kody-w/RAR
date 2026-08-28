---
name: "rar-cowork-cookbook-audit-maintain-product-costs"
description: "Audits maintain product costs records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_maintain_product_costs", "rar_sha256": "8ef9c5c37c5e9364b17ccc9aec0fcdecc66077c2f926bd21bd6b19ed5bd6545d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_maintain_product_costs`. The original RAPP
agent is preserved byte-for-byte in `audit_maintain_product_costs_agent.py` and in the RCI capsule.

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

Maintain product costs Completeness Audit — Audits maintain product costs records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-maintain-product-costs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_maintain_product_costs_agent.py` and embedded as the fenced Python below (sha256 8ef9c5c37c5e9364…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_maintain_product_costs_agent.py` first:

```bash
python3 audit_maintain_product_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_maintain_product_costs_agent.py   # or on stdin
python3 audit_maintain_product_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain product costs Completeness Audit — Audits maintain product costs records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-maintain-product-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_maintain_product_costs',
    "version": '2.0.1',
    "display_name": 'Maintain product costs Completeness Audit',
    "description": 'Audits maintain product costs records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-maintain-product-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-maintain-product-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '44111ccd0129869f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/maintain-product-costs'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/audit-maintain-product-costs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditMaintainProductCosts(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditMaintainProductCosts'
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
    print(AuditMaintainProductCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716aZOjSJbtX9HEfMisITMkgQQo29rsSYhFQoDYJKCyLIvF2TexCEG9+u/PkRSRWdNVPd1mY09VkSHA/fq527nXnfjtxW6bsKhevryowM4nrJ2mUQiqiZ17E6roiiqBv4rEgT8Tt8ibKnLapqjql08vHqjdKiqbqMjh9HXrRU09yewob+DPpKwKr3UbOKmGtyvgFpVXT/yigneyMgUNyEFd39cpizRy+8f9yM5dMLEDKKJuJlWbgs+OXQNv4obATepXuC642aOA+uXLz798eong95cvv724qV3XbziEJ4rjAwQ1YoAzUzsP4JCyhyrn8LoEFQSUwVse8CfPq481SP1Pk//6r6Szq6D+6cvXfPL8fH0Z/1PafNKEYNIUdt2MyOzSdqI0avrXyTrt7H5Ut2mrHGo3qaHF8uD1MfO7pKKc/H189vGxyGsAmo9fXwoIwR7t+fXlpwm01NeXqh2/v45Syo8/vaZFB6qPP32XU7dODKCVoTCI+vXb8/opFg78PjTy76v+HUp9eM4BX19+UG78PHCPesKZL69xEeUfH4KhO68gH53z8ae/Ent3URrVzb8k9+eH4BDYHtTpCfynT3cj/zJBngq9y/zrZUvo1n9HEzj8bblPk6eh/kr23f7/TXQawch9t/ifivuzCcjfJz//pW7/bMKnif/1ZQvS6Aqjw0nBl8lv39QjTf38wft+88Mvv0PR/6MYtWgr9y7hW2bnkQ/q5tu3nz/U99sffvn5Q1vCWAN29q2t0j+T+Wd2va/zBws+R33841y4vp4nedHlk/dIn/xWlP9R/f46Odlp5H2/X3+Z/Jgv4weZjEq8LfowwQ85U0OsP9jxp5ffITlAEqkgAYyPYZb/539OhMitirrwm4nqFu3IMHkTZWAEr4VRPYH/j7ldAWjXOoKGfY6D8T96eERc+JNf/49758bP7pMbp/ZIO9/e2O/bk/2+3dnv19eJBmUWVRREuZ1OlPXx+DW3A5A343plBWpQXSGTOH0DPkMO+jx+mUAS/fWfif12l/Ba9r/eWTR6sJJC7UZGqiFzvo5anUOQP3VwIcGDG3BbKDwtXIjEjyCPfoLa1kV6hYw2WqBOojSdeBGkbEj0/V02tNKXUdivv/4K2Tj8mj8oFJs8KkA9hQPe4Uw+f4Yq+WkUhM3XHLhhMfnw2+8fJv938s9m3YWPaxwhjz99ABHuVUmcwJxqMzgMugc6FBLG3Qe//f40LBSTw5IFPRb5EXhMhjGZAO/Nyiq3/owu8YkDoHWhZbOyqBrIy5OoeZ3s/Mk7Xrjo+Ghk7hDaeOKBEuQeyGF5akIbqvNuybxoJjUMvNrvP03aGtxX/dWp7oULZDC57ebXiUAdYZ0oUvjPCPM+CE4u8gia/z0GHvehkOpDPdm8iXidiGMUTkq7ssuwsp9r+PbDL7A+vE2Hwu1JDrqv+VgNwWiqe0o8zAMHQcu4T5d+Hn0+1lqY/179tvZ9jD1WM+1e1aqvef0Md7sC9/INofSToI28sQj87RlSdVi0qXe3H0Q6Snp6wXt65R6Dwp83BdSPjcC9bk++tuhsvpj8f2omRmxrllVodq3R2wktaor5sNnY6oy2fXRHsLTfF7vnx/dy/0YWb5z5NU8jGABV/7fHyLuln2MePNRWcHFlrdzlQ1TQZqPcexSOUVVVY/zaX/M3cv4EHXtnIugImLIwpMdIeltwfPqGNIR5OV5/L9RPO41WgZE2KVsHWmbiA+A5tptAVNWYSU+Lw5AEY1Z1YeSGf9BqAqVDz0P5EwhidAsk8LvpxAKqCZPIr4rs+/BodNDDYRAt7CXB6+QMk2EMiBpmIOxhxjHQCh/uoiYZgDaGEN8tXId2+QAztp9PgPbIyRHofrT/89H34L0jGcFDmbZnN9CS3UikHrg9/PqO8ukpKHQMsoeP/ujsp6aTH2vI377md4Tv3A2zOB3L7w+mmcDsyR6xOJJQDYkkA8/wgXFwr7Svj2L5qMbvWL78Q8f98d9ryu/lT/+j375MwqYp6y/T6aNkvVWsV5ghUxghUQnqR/X6/JZun5/p9vmebn+Q+TDRl8m/h+sPIp7h/GUyf529zsZHh8gFY7w+P9AM1OeN+XkxPv2aK+C7f+HyRQapbTR7D8vleyV5GwLLSVCBYBz8qCz1WJA6WAPvVAo98DV/j4FnfkCmzoOxDNbFD3l7L6nQow+HvTM+fJQ3cG1vbLwCMO5H0hF+DV6+5G2afnrJ7Qz8D/uQkdFhhEJDjDsXaG3YwzQRuF9BheCDyB6//3GHJd2/2OkjkusGIrSrOx88M+NJdJ/GBjaHXDJuFsay9aB4uMWx27QZETd9OUJ87E3GPum9ifrHVe+pC9fwii9jBn+ajA3vp8l77/pp8rabuO/N8hZup34e++ZRTzgU/nof+75pdMDLL38C49lG/wWIaGSPkW8e6gLvOzXcPVbaDWRAXTlASIV7bxjGIln392L6j2rDBStwaWFV9EbI323wHVrxwPP7XZXmsVf87eWNXJ7Oe/aFcDjM4s/1WBenMLbhgvD6EYXw2b/VMT7nQiKEXQucTAJ/5S5djHCXYIXhC2dOuK67soE7810PuC6OzwjCRf0VijseOnc83JmvgLeEX5aLpQflPeL421j4oxEPmPkAW81R18NwdLlcrOYEaq88e0HYtjcjSWJG+B6sFd+nJpBHn0o+lBot+N68jsZ46vrbi4Mv4EhuUe/Wjw81XZ1sfEE4t9BAKhyYQowkmqrxXikFidMwYtmKdr9B44Oh7cRgN+zXrgqkVOUubMN3LVOH2+U6H/ZHTDK4SPPa2cwxaVuLbjerxl3J8q8+C4rdOmQHIhb46cCp6TnxTvytFKmT1fpMU9/ovcGHotZW+jy7YRixnBuE6nANmSj7fXE6iKfCoJLFYp1fQH3Y8hYhzYfeF2nhgLMUM7udzl7E5EKjl1atcHzTrbiCEDKtX9S5hZPtNTONYb7ypmHUn27t5qYlyakYjLltyXVzgUR/EefUEO7NVarU065yD0nbqCc674g+U+tWLKZNKBpCKCJUZK2ReRkuyXZQewHwQZrehOJi0aubyOM6s423ttAMrcLjWXyQsOCSWhY7VHTU1k5xydp5MZfa5cIotxjKZk2/w0LCRHdFK5CHXjIVFaUjXgTGTszVdShajhTN+86sTyi7TGvQemHCD+h+32zWxp6r3SasW5cZSnBF9eKEYna/P3imOOOO8WkdWdtVLTHJCoo4nx02lrQYQddhdO44p7wc2Zqrtire7AsbF+2wU7HZ5YavLm5+mYaOoFcOK+q7/SyMeUAuLoLn7PF8UWJzE5c8t5vRehJa5VT1cJLgeOawO2sU7sddn13pOerFi2PdLLYHgK4y6qQztQP2uVANhsMw17AITsgBvZwoMRJqy89M/Lhbl8x1m5eAEd3bNJO0dHHIiXWGJgcKJFrkyu3yLFzwSm4TrT/2CIEnDDpXThfFH8B5d95nSxgMvbm7LRPeV10ddUSfPYgG/NHYPRxZVQcxvs7woupMow3imcAt5KNw5BttrTLltd7Sy+F4vZa3VZSwyhJEK/WCHiqbTDKtPZpXTKM8Pi3PAOkTxcCR01k8Jv025EJEB7R5Cx36cuaGM/CwTHa4CGHygk8xTU0Wy21cKUiQT4crH5m3dANM0Ohy09nToF6bvFCQRWIpoNcxcyjoHc2m7G1Zs9RmkelLAakEF+wDu/aGa6ibnLEqfe0waBUrRYcu3rVgB3FExMYk6NUBV4ZtJE9JMnUqAdkSfReTprGpN11T6ZRP+p2N+Zhrnh1/IIq6vVbT0DanxonlU9CRU0LdeJZmupa2ShZVpScrN0ooH0+tabQ4qFf8xs8sdBNkiVSTl6LcRXpxkd1V5/PqoFInqsdW/g7h3SUnHwOyoRVsikwP4u7C8aS3LtLsQLbzPS7NmVzjj322LBSgq2dG0uB2x54PxyOtpVyoyZ3rRX7X5OfBQvhEDw4CKZ/PwZJkDYY9DWdGz8SrvBWnery67DbT5XZFUOU2pUva9/WhC7GwmhUM4ZenHsuxWk/8/U7QmkKvLbq9JpcEVQhu67A2STWMa6VWZgh1vTc2Qnq6neAwOZk3MhbZwtZcZ/6UI1O7YpoNOpC9ZJ2T4zzJLFISkLyjNm0My9tJNzWC5HZEtL/mszBfWdUZk4Gr3ADiE+SxA2pcxO3CFKi51CdxKhrnfbj040WvbQ+Zeht6uShjqgRqX1ukaGyUGPp4xsc+vZ4zN7/GEaRkQnopIarF2mcuR1fMqWh3+LXlzcuwKEi0J2XrvKE37s4jaLFJlGq6oZ0FnRE0KRTZUV7uZTPerXg2z8jKObHHw37bWWvpVCjSLFGyiqqN/TEVdDtnklmwUZlEwDRts57VwK5dsV8siGAeiurNtQLW4GfeucaOoMO92zxRBiSrSRTx85QkfSzd7BJ2T0Xz2/yKTvfLU3I63rxE8Z11l3LropCOvj90K9euOcNxz53PUCF1vGKzhStxqrVDwDEuImJFTmuD35ilw2y1hZ3ayGV22633YqDMSmAfBXEg5MDeq1WqD5ftnkIlQVNiXiyQgjoU4pk6yv71JkQo7HlL+pwD+uRGuKqI9rDBNnXv0cCyRcoL4rmiwBQsaCbo8rnBDDtuWceS2NeGcjY2xjakPNejVg15yHOL8BMzPSzmFF8IwXaax8pFDdtKvBj71LCz5pg4blbFWq7re46g5bUqsn1SoefzTE/bW5C7ejZwZcp3gtvJWSeCK93QVj1tt0Y4FxCbHaxyZQJ9V6obBvacgqzuPYLwMcLSvN2MV40M6Vdkasp1ZW6STaRmUrLwPTtbZXzVF355Iy0sWPb6gmmc4/kWXrRowaqBL3XORVPqUKL6k6SIB08FNEvzxpFlDjyhnEwuZU98fHN5SHWDR5/4dd8EK323SBStoHEFLVSWYmU5tvSlc5MSEtXCBXnit3y63W117GZ1Z5LJsOtZyNwrjWxEgTOalL1OvRJuPPrZgg53jkRnmb8Rb4533Zy5bdHNc4GxCs6tXKLGGTBjpscrm+6Mw/4mOvYtRRlm6CHek3kKpjPHsFFeYdJWwQUlpAjhXEh2nCiYvT5rKLGXGb/luRJTkiWzdvf6CSwceVirdseSvCkBRm8DNaa0KuKcTRGwALYpJkMnch5Ftr1nmwVF6cQ52c4pvzGO5Vaf8fbaKsXprZPEIJyilYUUS1rML8UaDbelc6hYWRMLDfb9dAHblPV0RR7BcMKXVxGPlCIFXEsJ4gW5NvSmX4W5YeN6FR8tCwEnNEFWaevAKnW2UL1G5huUrOQm2rMy34KmmyE7UoUpskZx/iYyeM/UW144zkN7z0TsLgRSUbrXQ42X8i0dYEnISDdAZ0u1TAvoJHqjEkXilans07OEScPrZSiXiKM3t6GWCUihnmzFenkqrHwn+HzZsxqtlho7c6pTV1K3U8Ks9tKypWAeryCZ7tyyAxdlEZCy7K1rZqPYBMFvRMqYJex2m0qVtNXtG6ctZVBuJOQyZxxDudV6JQcbrSVJ2W+UQ8CoAUUzMbKxc1mRcsRbpEiHExkuHNyepLSVzdZeLG2M3U46cIQaHuJ9Wa+o7ZQguKPGo5pOhTyaUMbxKnBCLvuqJdIrq8/1YdPq222OhYkUNijwKkQleM1C91cZrXGQnrvVobJo7OwaImmWKrK3qSvvXDBq1w63ZpokqWssjudDbqYJ1SKeqm8lVMQu1SEmZkN+GySHPW78PN+nTum7sXmtFrYlVCW16Y+sh8PNkMntLmSZb/vEHAwXXBeardqXJbFnMPTML1MM9K2bdJrsn659hU+nnMWTp/LKK5ms5cXRQZdbPj7vtk0g7SkabSyjtroimOstQD0pziPELoprot48CfMtwiG0RjPnYs34ZRCSeYyyWOy0iYvane6eAd1RVqDwDGcah7LQz6lWh2JHqWLl7uJSnzoR0kbcSl0352V/o9fSPNnFiy3f6m1GngT/eLSAmp760Ax2qK5L9I3NBJZT53Qxz/cA9iBmSWtLrYwFmtioXVqaTN8c9VV9Y7yENzg9yXUHFPLhvDcDu2SRldodLHkuqpYi7IxuG5wYot07CCD2JWz8GpaTDpsIbaltrbuKjFhOfgyaAS0O56PV30Id8+lbaibHIl9fOINiTkfFoZFhwdOcFqC2Y8oa0wym7HZlSq3K03Yzl7VpVcoIDaLLQFEzhd36QUPo1mVtp7TSVKq+ooZy3ZgZ3qj4Jd5j1+7CXW7VyeusG25Z+pWWePTkhLMLKNKFX1rU/KBQXdEyyoaqGtg2k8OVhTuaFl2u/ZPm1MmhH+xml8uLrtog3M0w9/WZZ+pbWDcharXmnjE8J3LRNK5IC2S0tdQSpU9Sp5hj4dY8BLMIIMU67kVP7ddENLO9gLM0eXZCRS7C+vzCuQfkGkpX145btCI1k9wg23autJfZcegXHLgCdI7NN0t/mzrzqnY5amjCLjcZK9z76tVoJau88QIzU5jaLjtf6TZtQXQV289hpa4PC8vDHGS7kLCys8+SEpOOWom1PRO7TIobJpavPq5H2wrBVrLfHS7VMbHJNUesrnk5V3gW7TY3Y7kg9ZwSCCxc3uKq9VRyBvt1KTAVZXZqcDQ53WKklROCPbNbr0TSPSIYzLVDcWS6oFYLo7BPaI6trtPY6WQuF2kfrTCvQA2Z2y7CrbGoV975rHXCjGHlW2KUVcs761V+zWi5TOigcza7q1BeT8A5S3RYJmRAFprLdnK+87Mh3w+zNKL9QaiYwGwUFu5Z0BWnLFj6uNja1BojvNYaMg7ogrEXI69Q9bN8mg5yg5qzeDmXt0ZKAGSr51MmGDBDPiGJyS2W6qzvqJ4g1CpxMqetY5Vl2BhSTmNzlYRg7jZKO/wc4ezSFquSPzekxwZLNJ1mjR9fkdoFu06L13VrddudrPhmN0ORbYJzDXHspUwOcSRdEOalF7CwlSv9lonVEjXSBWAbQyL7ZUcmtrdYRdbUP5qGRmzEhAmkKBtASNeo6td2qHdeIWis6ikIotAH2sMO3DRE5/pO2h64fi9hO6cOUdhGq2GwwRa3mTbQ+SGUBamzZ7UJvPVcCAvFi+fhHuOAK0u7ld6mRhfU0Z7GDFyfYkFni5ypxPZ2rrhmSvWy2kjxkBziIKzaY+pRiil5EJpMGgU2mxXGsmf3giNeu0qiq2InAAR3KN8jvdnpTPDOTUyWuK2auZLU6QoNHJEwuc06S1WKRAKNvuqhxRVOdWERLVvhuGv5N1raC1iwyNrDgjF7dwut6SESK9iHTcdYPUZMt+LNzSLyFBKqzKVBzfaq1x7FrsYPRukvPXNGyKcIWxRsGFeGJdtSlV82UDtAGcJRFuh0akcbLEOx/cyk9S3OVit2qylFuO9BvOo1vrAzMLvUqkIQzTYGu81CQRHSPGyGlTm/kvOO31tzuKHwAIlPyYu/BYftMV65UiOTxdFdLWP02J6MajqPWVHIZ0QJFeLQvdlPdS5szujVI8i1N203tLQ0ZlyzzOYr2IPcsmPCnWm+CJjjRT/VVau52mBLSqOHZqzMBm9RZlfcmXpTWdxsBCrdw4Z4iiD8OtDTlXkmBa+d66ses2bt2RHlypsSga2CZHctouAIdIqT5zUSHPGglJVQCeaH8FYuhNaoKhUY12aJ1kuAStOzaFAdGwr60JarPsW9s7kGnLbAeRutKASRPavD15uTEHLMvKDq4TaY0cXntyBsZAEXbkp21gITNZxsqhbltrH6FTtgUMUT3FhA/1yo6eCd5+d1P90DyncwfQFrXpPOOJU8mufl8tqdxekOb7Cdtqc3w4AvB7k0U9NLJd2f74LTcRpk+uAsseLW7W+tZKzdYj9zD0xDyGamlIdaW+cObiscyViJv0nOiruslpjrJETQesmKyt3qyFx09JKs2On6kMUD4a14eb1++fQyHpw+D6z/pVfN42ng/9qh5OP88O111f3YGNjel/taX/41OL98eqncCIJ5HLjWaRs8jyj/23Hr53/2imOc2T/e2o5v027N21l+Ywfjnxm9RLnX1k3Vf6uLtL0f9n56gRw6/t1DPUJz4e+XuzJZOZ5y3xd7nHZHQf6tKb5VoIkq8DL+ScL4fgh4kd28XQbPc2c4vofOiNz6G4Yvv4GqHPV7vi+BaqGvs9f5y+//DyqsISe0JQAA -->
