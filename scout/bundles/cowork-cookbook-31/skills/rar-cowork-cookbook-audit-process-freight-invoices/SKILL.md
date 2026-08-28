---
name: "rar-cowork-cookbook-audit-process-freight-invoices"
description: "Audits process freight invoices records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_process_freight_invoices", "rar_sha256": "8459abecd6fc7e6dfaeccaf979eb32c96e1a4399716389f5614ac4468880dc92", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_process_freight_invoices`. The original RAPP
agent is preserved byte-for-byte in `audit_process_freight_invoices_agent.py` and in the RCI capsule.

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

Process freight invoices Completeness Audit — Audits process freight invoices records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-freight-invoices
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_process_freight_invoices_agent.py` and embedded as the fenced Python below (sha256 8459abecd6fc7e6d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_process_freight_invoices_agent.py` first:

```bash
python3 audit_process_freight_invoices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_process_freight_invoices_agent.py   # or on stdin
python3 audit_process_freight_invoices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process freight invoices Completeness Audit — Audits process freight invoices records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-freight-invoices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_process_freight_invoices',
    "version": '2.0.0',
    "display_name": 'Process freight invoices Completeness Audit',
    "description": 'Audits process freight invoices records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-process-freight-invoices',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-process-freight-invoices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a65d62bbf9b4eaa1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/process-freight-invoices'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/audit-process-freight-invoices', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditProcessFreightInvoices(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditProcessFreightInvoices'
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
    print(AuditProcessFreightInvoices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716ebOiWLbvV/Gd+0dVXTJTZiQ7bsQDlBkURVQqK7KYQUYZZKhX3/1t1JNZdburb3fEi2fmOUdh7zWv31pr429vTtfGZf32+e0QOMVCcLIsiYN64RT+giv7sk7BnzJ1wc/CK4u2TtyuLevm7cObHzRenVRtUhZgO9P5Sdssqrr0gqZZhHWQRHG7SIp7mYArizrwytoHN8oaEMqrLGiDYl45c6rKLPHG5/XEKbxg4UROUjTtou6y4KPrNIG/8OLAS5tPgHMwODOB5u3zz798eEvA+7fPv715mdM075LsnnLwTzGklxRgb+YUEVhUjUDtAnyughqIlINLfhAuXp9+bIIs/LD4z/9Me6eOmp8+fykWr9eXt/nfvisWbRws2tJp2lk2p3LcJEva8dOCyXpnnBVuu7oA+i0aYLUi+vTc+Z1SWS3+a77345PJpyhof/zyVgIRnNmmX95+WgBbfXmru/n9p5lK9eNPn7KyD+off/pOp+nca+C1MzEg9aevr88vsmDh96VJ+OD6X4Dq03tu8OXtD8rNr6fcs55g59una5kUPz4JA9/eg2J2z48//RXZh5OypGn/Jbo/PwnHgeMDnV6C//ThYeRfFtBLoW80/5ptBdz672gClr+z+7B4GeqvaD/s/99IZwmI3W8W/4fk/tEG6L8WP/+lbv9sw4dF+OVtHWTJHUSHmwWfF799Pew23M8/+N8v/vDL74D0/0jmUHa196DwNXeKJAya9uvXn39oHpd/+OXnH7oKxFrg5F+7OvtHNP+RXR98/mTB16of/7wX8D8WaVH2xeJbpC9+K6v/Vf/+aWE5WeJ/v958XvwxX+YXtJiVeGf6NMEfcqYBsv7Bjj+9/Q7gAcBI3XmP2yDL/+M/Flri1WVThu3i4JXdjDFFm+TBLLwZJ80C/J9zuw6AXZsEGPa1DsT/7OFZ4jJc/Pq/vQc+fvRe+Lh0ZuD5+kLAry8E/PqOgL9+WpiAalknUVI42WLP7HZfCicKinbmWNVBE9R3gCXu2AYfAQp9nN8AAF38+s8Jf33Q+FSNvz6wNHki056TZlRqAH5+mjU7xUHx0sMDQB8MgdcB8lnpAVnCBKDpB6BxU2Z3gGqzFZo0ybKFnwDgBoA/PmgDS32eif36668Ak+MvxRNGscWzEjRLsOCbOIuPH4FSYTYL+6UIvLhc/PDb7z8s/s/in+16EJ957ACav/wAJJQPW30B8qrLwTLgIuBUABoPP/z2+8u0gEwBShfwWhImwXMziMs08N/tfBCZjyhBLtwA2BfYNq/KugXYvEjaTwspXHyTFzCdb83oHZegDPlBFRR+UIAi1cYOUOebJYuyXTQg+Jpw/LDomuDB9Ve3fpSvIAcJ7rS/LjRuB2pFmYFfs5iPRWBzWSTA/N+i4HkdEKl/aBbsO4lPC32OxEXl1E4V186LR+g8/QJqxPt2QNxZFEH/pZhrYjCb6pEWT/OARcAy3sulH2efzxUXYIDfvPN+rHHmimY+Klv9pWheIe/UwaOIA1HGRdQl/lwI/vYKqSYuu8x/2A9IOlN6ecF/eeURg7u/ag64PzYEj/q9+NKhMIIv/r+1FbN8jCDsNwJjbtaLjW7uL0+7zW3PbN9npwRK/IPZI0e+l/130HjHzi9FloAgqMe/PVc+rP1a88SjrgbM98z+QR9IBew2031E4hxZdT3HsPOleAfpD8C5D0QCzgBpC8J6jqZ3hvPdd0ljkJvz5+8F+2Wn2Sog2hZV5wLLLMIg8F3HS4FU9ZxNL5uDsAzmzOrjxIv/pNUCUAfeB/QXQIjZMQDIH6bTS6AmSKSwLvPvy5PZQUAKv/OAtKCvDD4tTiAh5qBoQBaCXmZeA6zww4PUIg+AjYGI3yzcxE71FGZuRV8COjM2J0H/R/u/bn0P4Icks/CApuM7LbBkP8OpHwxPv36T8uUpQDSfo+Ox6c/Ofmm6+GMt+duX4iHhNwQHmZzNZfgPplmADMqfsTgDUQPAJA9e4QPi4FFxPz2L5rMqf5Pl89913z/+ew36owwe/+y3z4u4bavm83L5LF3vlesTyJAliJCkCppnFfv4SriPr4T7+J5wf6L6NNLnxb8n2Z9IvAL68wL5BH+C51sqYDNH7OsFDMF9ZC8f8fnul2IffPcwYF/mAOBmw4+gbH6rJ+9LQFGJ6iCaFz/rSzOXpR5UwgegAh98Kb5FwStDAF4X0VwMm/IPmfsorMCnT5d9w31wq2gBb39uwaJgnk2yWfwmePtcdFn24a1w8uB/nElmZAdRCkwxzzHA9KCfaZPg8QmoBG4kzvz+zxPX9vHGyZ7R3LRARqd+YMIrO15g92FuZguAJ/PgMJevJ9SDccfpsnaWuR2rWcjnnDL3TN8aqr/n+khfwMMvP89Z/GExN78fFt/62A+L98niMakVHRitfp576FlPsBT8+bb22xDpBm+//AMxXi31XwiRzAgyY85T3cD/Dg8Pn1VOC1DwuFeBSKX3aBzmYtmMj6L692oDhnVw60B19GeRv9vgu2jlU57fH6q0z7nxt7d3gHk579UjguUgkz82c31cgugGDMHnZxyCe/9m9/jaDeAQ9C9g+wonaMcNPJ8MPSog/dAJPM8JaYoOXAz1aDJAHByjaQohsRUdEiSCOx6Ok6vVCvY9GgX0nrH8dW4Bklki1HG8lUchuE9TDukFGOxiXoCgiE9hAUzQWLhaBTgwzretKUDTl5pPtWYbfmtkZ3O8tP3tzSVxsFLEG4l5vrglbTkkTrlDfIZqMrhoVwjO4eRIeRdBKQK1Xvu1j4sbzbe3EcpctY0+yhJ6lrrUhmuFPHHMLj2EWro0KA/idbQ4ey1j3baquMnNbCKyEVoRaBwlzOVuybxU7/PDeE6dDB5yd3WXZbJvUNm0b9Jhe0ED5JY3qAAtl0K5dCw3aI+jXPFMxUY1n95wqbgFjbpWbGo7TGOobzSVSrTWs47YMa+u4lnKz/IpMc/beNTNDFp162HphXW+FFp0eVd14rKKA0o7neRhfWks/OzAqgycjoIadljBh/Ndvth3Q8PGSqvT1le8DVbCk5Dc7v5xagfF3MUVynKFdUD6hjxXhC/seOMwlolleVGnRPHp0Ml9qJpxZ/XK+QhfbAji4VqVTtYlRZDY5z0E1bc1cha3dNVBPSp2+xzWXYHg+X0RB8PEKKf+th+uIxGnpJGylUvAx+6k8ilKWRpSY5O2iU9bQtVLhiEq/ZpreqEyXahaGKs2p7Q4YJJKp8uaFW9dvJdiCBX1MbgRdi1KSYLpfSiK+3jtcnqEiuZJQE5tcEphxT8hR5xY4+eyahHIhUPGKhSEiAVS40hjiHfboyWiSLyaeksk+1CAUM8Z2d6g+Ai5H3xyRYkKD3Q1OTK8lmN+31iof8V3TYuv1QClc846so0byIVWT5bLD/e4jCxIRW8Wpyda44f5hdxJosrf10V14nVvWOa6WPfnHWq0jXTa0BK2wWN/bG1+OMe+Kqa7jMYQfWpv5O3Y0EWzMhpTH8mNmvbGNEnHLrIregSF6vD4gVrzxtVnNHf1HUw2dW+c78Ua1kTc2Gk7Sadv68gX6ShWd1UzQMUZlXufy5w7qtaXRqsPhhs256voK3J6CnK7GNQBOd5k/ohur2ILn7a40Q9XocpN6hjoVNYXct6Baffg94fEZ0nzmh66pgrW112CV9Ua2LRN8WxQsKg3mF4vwVhNVPthQ12mS7TdnBJmvFxEb7iU58o2yxWuyT2e+9epEHBxv7LCk4Ls7nzXKaOaJt6NlO7cXXDrdJLSDN8LLjwh22rEp7uULKENzKGbg9CcbQxfDkUD3ZE21sVTMdjXsMB4a7jV9cqWoH0dYOmJHIWSnIorNxRCK4Oaqx6n3UrkTet+kE+w1teMlRpd2d3KsuT3GYGtyQJhnWovrwlqvG+KahtQOYvnwbWc4FWwhxULxy1TacQV75n7xqxq4XYOEXs0VOWWaptAHEwbuSY+BJxwd2755pqaUJGSmKMOFpeybnFjFXi3ixT8hgmHvt4QzSay76Rwvlu8pBjLYLzt5b0yiEtE66UwcViFDTCS9wYCUjJZVg78hnJYdbvXa/JW6Vk39Nj+tmPu+7Ngn+xsUlXuFJmy5Vk3XuVtPTvqZH6NUE6udsNSQm+DY/jNUrvmVrWmfbm4r5e7aiVFfkRpNW8JG2jJjhCeuAQt2UvgohbelVFwDotJxPDQYHEL07ZyzI47rZL63kI6KlANWtvgI8FLwSpVFDy6YWl7F8KrbRzLPl61UomBTn2vuTbQFZVWWi6XqCldz8Oqw/icZnsRgVjTPgV8kaP5uDv0MqPE6+mS6GW0C3G53jEZdrnG2RGBRFniNr5Y9fAKy9ykmirbDkSJ4VpFQtObhmxZZ++mVy7X9Snpb4ZUcejWruQoSU6ifuoEyvN8WDG6+tJt+nWbXbbtyS52drjFb6NkY+YJNb2zDXn3MwGZB55LjbRb63foZMnyfmXQ/DmfUJntJcWs4Ulb7TC0YhAUE5szEmmSSBOiSBL8xlOXq0M4pngIRdxwgBWh6hFloo9ycmAOFHOVTQ4OPHxSjSggzlKVTuW61jCsMc2romwgnJNL/eTd+6M2NLe09vJqkxfhJjtGq4OvOZgMcz4ZbLrBtUwjs/aWWDUHWFq3h8IyRaRUqdJUzgcwRWkdB4vl2iHiPvGssi66ZDjaPrvyc59Uy/GsOH1y7gthBZOEd9pZ9dUk4MFJ5SpTzze0hQ2ipK98H7G9voKyOj9ZcC+3A1OurJzaVLLQa9zqnGNbL9xUvJ1iV/fcolp3EKChIXpD2iupI2mWYwep52IdJKN9h++lY3736UK0uT6yT8NVmgT0et0357yZTks+I447XIN3Q3/Z3Dayou/aA2WxU7r2R2Nn+4oFos87hfZYt86NRdnBOBg41HpnRWOZAdO4PQfneqfEFO0ysdCLbiPeqlMqS0x0NyyX8/o+57bUhc3vK9RsCU68AWfFx9yJMmVVBwoRaTDd2N2AMEmkyDdq8ios8TMkBX2DWOfSWl5lRx9VcNBYXbieoLdSRxgVzVKFXehdr0FdV+k9Kh9op2PXIaoBADnBmZmgZ/6yowWLbBLNrl34FG3K83ZCIu52oRsfacQ0vivcztHFarlPZZb1bO8E7c3gwoUHdervDFlnB4cLNHnbSX4jrHpnfwRld7OOhkRkkSo9YLHEm8jhsosHCPGgVDeNqmR3KbWkmBWKi8uDX+bX1ECDW8QYmwPdCs3AYmis37rmAFx5WS+xnqY1rG6OmGMnSX0JcIZCW6fX9qKKBX4rV5et5mcFgZydA0We7fzOxnZhHybKIsWRXsdS6jJdRqJ+L2g9G90MPYk409ObweXG6xq6CPn+wha385Qo53pF7kj9ZDe9pciDKPstdiRtZ8jxPQPnhLRULscu02TdCtw2orvl1bG63EuMpRRSt1ZTMtU2DZzBkOOWQe2EV2zo2jqdZZyUJuoqHgXhcymcC2Uy+DHby2R0OLCXm5KoZ/SSGGF0FU3zot1Pxw2ps+bOSyuWhEvK9o6e357VPmXXbLbcm/EeggWIcW+b6SC42Mbxxc6hkHF0KYHaumVvjdfeFjDpKiCdJAXMhmru8p4H00S+Xu3Eq4yYuMozZlsxmUlh7LQ7SnBuBruTVyG64WZMT6zwy5ql2AI0SVncp6ifuLBeb4vKaA4jNe51pOCnUFCO92QbUWNOtn2iNis3JGTZZOgrVNMXdK0yvA/haSn4jQkayR2PVVcszY+wBnH0rjOl8zEgxqG2iM3onMfNOoX0C4yvmX67PxOTwGclkXc4BTwIp4gObw9UeWzWrt75tQdVTRAp1zjGEBrSSB6vzeC43kTF/aJh+ihYQmqILhNCG7lRDsvLxFprlQ8PSAUHdjEFGb/Kz1OFklQYBo7eQULVRjUt8TsYD3qUqH1iWUwCd01qOGXWIOe8kuIqX+dG+ObDcsdw+7aOG+9yXjpYsdnrznFzK7ZnqWfRJmYCxramDJ5AU7Ba0VGlWmdFTpirHRi4uXEu/cVXj4erBedypfqZkYScrdn99cKdmFY1umOFZ+0Nvzc5aHrTlEzcjGOdeMevefWM3U6M6wglMYHiyEGMdyg7P96Fq7Ov6yKvVwY9XLQTaO7863VUhGnn4atzFyB7p6dAdVJQCs+1ehO3jM0bJLFXKlKVYizcGxFoYyffFfhLe3M4M99o+LnJj5posTuozdb4nlRjTVL3mrS1Oawr8iTeH/cAQ+UzrG7zDknc26DeblobbrgyqIX2hLGFWIFysTKk2lY79VCRyTmGslQ9thuVS3Brs1E6qKnqabty9pucclOWtvRuZDpVv8GJvl5yOmNASs3qSXxsQTOfNifMmVjtRtWXQ040IZjBYExUFQ72qitd3qhjdd8wh/PufuQHm7uX1SXslUzfT6uyUgRib7YX4tpmd9CkDUu/1GPKtwL/HiQTc14xiJeENO7x/OkeAIAplx2bdJSOhuu9jQ6lW691IxlksztfjjCOHATSJAdNwnX53kzHrbZPqxPNBSVLNyjeLPWloDH0zl03/Yntjyi8dU+IIcZdNthDwMCjVG93S9OAuVZtFFsz1IueFIjTr7na4omaIUPSLEX9OtAlO2GMFTgJVQmRppckN61qRyfY2rzi1PqcU5dyi4hQKEqt4SyXYakuS7W2raTC/HCZUCtfFtmth5vLoOxQ8+wZ0fkKt368tzEAc2oaxZKoHWidZV13pxG0ocp6BHP7i78mYwRjRatIJPLoGcFx6tYX9ZruBluMMSxLNuGk1URRtnsRzCsoLe5xYbPDW4djcNXv7CkXg6Nmy3ril4fjybCXk9GiF/xKIMba5akA4o/Fko8m7GzYUHoRCdDHjD03UtShTtWc6prrQeCV651zWwe4G8K8dZL1+GlFCoSj1zJ3aletACbqbJm34fUONV4g9WbNtBoR5cco6Ya4alfCAO9cNEx9bRBhWkXQngfdsYVHJ6LQXHFq7+p00cmbTyBYREgwOVCbCYKCocNG1r2ojM/rOW0Ol4ZbXhBTjijmUmggT/nmJp+kqTvtKKUle8MTuG168O8GZq8RPZQzk+HucVEV+SXoLKZfswWYGgl0nY58rJPJ6Xj3fHug8fVgkLbLKqNUmq0pm8vTmsVXQXziyx3CDslRVNkOxnfBpdlyXIMHPiZbEQ4Lm2HNnq7hFMShuHHgOMKWY4mbQTQOan9oaAQeMP/sany3ycOimn2RO/1JPKybIq8agI+WpPZkrBk0SWTNHupKitDdoq6HDBMMPJ5oEe/78NgJ6yYQhHvZ68tdwlzUbMXb0KoOzzKlCTiE8INlqHHUbNGKWuU2W8HY/QbmzKpGNhR/3/f8uhibiYGt4x2W7ywDBn3mACY+nWZg6d7TzUFitFpccRjZKLow7sSB5LZyk0M3DruZeJdgWLARVpc1KFyQggcsNS7LpVhF2EhV93pL+AS2CnvGHS728g6m0JvYrmtppzmjPjb0mXYvw/wVDUsTNTCJUMLZSVc6iCpqFybr+1KT4qUCRfRdO90rnYW0YVXiPesLTEUbud76IxV7AUvqN3HaOF3u3vkjvJvuxN1hS0mOTtUN78KQIs4bJZ1qBYvXLQrMbLtdzk32beMaoqceLDTmEeEITWPUk5tWhNklzCucpmyF6qjpO7kYad8xDwh97+hMRQkM3yf4iVmpieAju85rTYXi1v3KA3PhEcFPu3F91UQwMVQbCe905pyvBHtjnckCK93jenvVDDtL8Y2eocQdLhWDAm0/29DT2gMxh0Bw5kT3FWa3VqTdk3NUoATiTpLpghYevtM533nuir+G47b2x005bnCi9QhQns0mGHNlB6WGcoV6c2u3zRIJJYbAzioY1BlqayUwXUoH0HRgcm829LpJIanZKqFWeik+7SAY7zr6QExXePSHxstVkyyusIqj4oXejorBMG8f3uaj09eh9b/42Hk+D/x/diz5PEF8f2z1ODoOHP/zg9fnf1WgXz681V4CxHkeuzZZF72OKf/boevHf/6wY947Pp/izk/Whvb9VL91ovnLR29J4XdNW49fmzLrHoe+H97crpm/C9G8y/n2UCiv5tPuB7u3+TsJQMH56e3Xtvz6+gbH4/L8vCjwE6cNXh+j1xn0hzd/BG5JvOYrRhJfg7qatXw9PZkPb+fHJ2+//1/HZd7L0CUAAA== -->
