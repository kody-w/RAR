---
name: "rar-cowork-cookbook-user-access-review-audit"
description: "Audits Dynamics 365 user accounts for segregation-of-duties conflicts, inactive accounts with active role assignments, and roles granted without recent login."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/user_access_review_audit", "rar_sha256": "d7a577ed1b3e191fa31facdf299fc2f34a4261ee0c4168e1b1c8968b2d432d18", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/user_access_review_audit`. The original RAPP
agent is preserved byte-for-byte in `user_access_review_audit_agent.py` and in the RCI capsule.

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

User Access Review & SoD Audit — Audits Dynamics 365 user accounts for segregation-of-duties conflicts, inactive accounts with active role assignments, and roles granted without recent login.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/user-access-review-audit
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `user_access_review_audit_agent.py` and embedded as the fenced Python below (sha256 d7a577ed1b3e191f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `user_access_review_audit_agent.py` first:

```bash
python3 user_access_review_audit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 user_access_review_audit_agent.py   # or on stdin
python3 user_access_review_audit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
User Access Review & SoD Audit — Audits Dynamics 365 user accounts for segregation-of-duties conflicts, inactive accounts with active role assignments, and roles granted without recent login.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/user-access-review-audit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/user_access_review_audit',
    "version": '2.0.1',
    "display_name": 'User Access Review & SoD Audit',
    "description": 'Audits Dynamics 365 user accounts for segregation-of-duties conflicts, inactive accounts with active role assignments, and roles granted without recent login.',
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
        "upstream_slug": 'user-access-review-audit',
        "upstream_url": 'https://coworkcookbook.com/recipes/user-access-review-audit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '37bcf4aff678f487',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/user-access-review-audit', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Email'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:audit', 'word:review'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class UserAccessReviewAudit(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'UserAccessReviewAudit'
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
    print(UserAccessReviewAudit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816abOjSJblX2Fem01mNhFP7IgoK7NBCBBik0ALIqMskh3EvglQdv73cSRFRGZXZVWX2XwYRbz3JHC/ftdzrjv69c3pu7hs3j69mYFTQKKTZUkcNJBT+BBXDmWTgj9l6oIfyCuLrkncviub9u3Dmx+0XpNUXVIWYDrb+0nXQuupcPLEayGcIqG+nSV5XtkX4FZYNlAbRE0QOfOcj2X40e+7JGhnwWGWeF37AUoKx+uSW/B92pB0MfS62JQZuNO2SVTkQTGPn/Wcr7ZQ1DhFF/iP8WXfQU3ggSFQVkZJ8Q7UDUYnr8DAt08//+3DWwLev3369c3LgDig/hGoynpe0LZGcEuC4WEOmJU5RQRuVxMQWoDPVdAAO3JwyQ9C6PXpxzbIwg/Qf/5nOjhN1P706XMBvV6f3+Z/Rl9AXRxAXem0s46eUzlukiXd9A6x2eBMLVC365uihRyoBU4uovfnzO+Sygr663zvx+ci71HQ/fj5rQQqPNz5+e0nCDj481vTz+/fZynVjz+9Z+UQND/+9F1O27vXwOtmYUDr9y+vzy+xYOD3oUn4WPWvQOoz2G7w+e13xs2vp96znWDm2/u1TIofn4KrprwFhVN4wY8//ZlYLw68NEva7n8k9+en4DhwfGDTS/GfPjyc/DcIfhn0TeafL1uBsP47loDhX5f7AL0c9WeyH/7/b6KzpAAZ+tXj/1DcP5oA/xX6+U9t+2cTPkDh57d1kIGaaRw3Cz5Bv34xdzz38w/+94s//O03IPpfijHLvvEeEr7kTpGEQdt9+fLzD+3j8g9/+/mHvgK5Fjj5l77J/pHMf+TXxzp/8OBr1I9/nAvWPxZpUQ4F9C3ToV/L6n81v71DJydL/O/X20/Q7+tlfsHQbMTXRZ8u+F3NtEDX3/nxp7ffADAUwJree9wGVf4f/wGpideUbRl2kOk9gAXAUpIHs/KHOGkh8H+u7SYAfm0T4NjXOJD/c4RnjcsQ+uX/eA84/ei94HQxo+MX54E5X5oH6HxxZtT55R06AHllkwDkcjLIYHe7z4UTzWgG1qqaAEy8ARRxpy74CPDn4/wGICf0y5+J/PKY/V5NvzwAM3mikcFJMxK1fRa8z9ac46B46e4BLgjGwOuB4Kz0gBZhArDzA7CyLTOAxN1seZsmWQb5CYBawAnTE4z74tMs7JdffnGdNv5cPKETh55k0S7AgG/qQB8/AnMA9kdx97kIvLiEfvj1tx+g/4L+2ayH8HmNHcDul++BhltT1yBQS/2DGqA5kAAoHr7/9beXU4GYAnASiFQSzswzTwa5mAb+Vw+bG/YjRlKQGwDPAq/mVdl0AI+hpHuHpBD6pi9YdL41I3Zcth3kB1VQ+EHhTUCqA8z55smi7KAWJFwbTh9mTnys+ovbOA8Vc1DUTvcLpHI7wA9lBn7Naj4GgcllkQD3f4v/8/oc5x9aaPVVxDukzdkHVU7jVHHjvNYInWdcAC98nQ6EO1ARDJ+LmQGD2VWPUni6BwwCnvFeIf04xxyQcw7q3m+/rv0Y48wsdniwWfO5aF9p7jRzKDwA+2DRqE/8Gfz/8kqpFrBy5j/8BzSdJb2i4L+i8sjBmYehJxFDTyaG/jdklmvoQcjQ5x5DUAL6/7vZmO1gRdHgRfbAryFeOxiXp3/nDmoe92y6AP0/9HzU0veW4CugfMXVz0WWgGRppr88Rz6i8hrzxKq+AaoYrPGQD1ICOGKW+8jYOQObZjbc+Vx8BXBgCvRAKxA0UN4g/ees+7rgfPerpjGo4fnzdzJ/RLjxZ2eArISq3gXehMIg8F3HS4FWzVx1r0CB9A3mChzixIv/YBUEpIMsAfIhoMQcTQDyD9dpJTATFFzYlPn34cncIgEt/N4D2oIWNXiHzqBw5uRpQbWCPmceA7zww0MUlAfAx0DFbx5uY6d6KjN3tS8FHeiJk7/3/+vW90R/aDIrD2Q6vtMBTw4z4PrB+IzrNy1fkQJC87k0H5P+GOyXpdDveeYvn4uHht8wHlR8NlP071wDgUrL20cKzoDVAtDJg1f6gDx4sPH7k1CfjP1Nl09/18j/+O/1+g+KPP4xbp+guOuq9tNi8aS1r6z2DuBiATIkqYL2wXAfn3T08enmjw86+oO8p3s+Qf+eTn8Q8UrlTxD6jrwj8y0lAfUIfPB6ARdwH1eXj8R893NhBN9jC5Yvc4ARs8snQKnfGOfrEEA7TxgJ/CcDtTNxDYArH5ALvP+5+Bb/V20ARC+imS7b8nc1+6BeEM1nsL4xA7hVdGBtf27MomDeq2Sz+m3w9qnos+zDG0C54J/sUWbUB5kJnDDvaECNgP5mhrrH/gYkHoBZZ37/xw2b/njjZM8MbjugndM8cOBVEU70YJcPc3NbAAyZNxIztT1pAGx/nD7rZm27qZrVe+5b5h7qW4P196s+Shas4Zef5sr9AM3N8AfoW1/7Afq603js2YoebLV+nnvq2U4wFPz5NvbbHtQN3v72D9R4tdh/okQyo8aMM09zA/87JDyiVTkdQL6joQCVSu/RVMxE2k4Pwv17s8GCTVD3gDn9WeXvPviuWvnU57eHKd1zH/nr21dQeQXv1TOC4aB6P7Yzdy5AXoMFwednBoJ7/+Nu8jUPgB/oauZtK+2QNB34qIsHKIOGDg5+PD/EGCb0sBAnHAKj0CBAPAKllgHqot6SoZYu5hM45qNLIO+Zv1/mxiCZdQmQMMAZFPN8nMJIkmBQGnMY3yFox/GR5ZJG6NAH/PB9agqw82Xg06DZe98a29kRLzt/fXMpAozcEK3EPl/cgjk5FEG7Y2zBDRVc2pTLDuZB9hxq3yPWmSLQRtqIauerEcZe22Q1bgnqJOWp3jcccZ74XcqFarrwKFu05aTbuGbHr666suHzQ3ZvOpg88vx+rRD3OjYKz5lU3g5ro+47WOqI/LA0bPycyIuNcrgv3ANyWWLn01Ri6nV3o9sjujmoRrEJbDR27Nwa6vhUn5wJKVJssoNDJVOImih6i51rYlmrsUemlp66qEG7VF52uKpOB1pIrgKZiaRlhFWaLTRTOpn53UzOyx21bI5OeTkjptPg+/M6sosDyQTWdWAC3BoNYViGuEXuJwCkhuVbGt+fA21fO63voXmn2YkZn+5ltqXjM2Fp/lmsj22hSdpZOVYObeDu9ViqVTccXapJanOxGgPL3ZKypZfsMampbr+TO7bnxq1zLS4TP9wyJ43iJjaqi3AeRGZ59bUTno2bmqR33cFo4Iw6whdctleXJr2qNx5VeFZdNCtjX2VpmXFjFkaTvze1mD3bRJWaC8Gv8StjE0u2Oigbnz9fJK7NRWZre8x92gbdqCiqBqO5KZQ1vl0c1TD2alQWiFuPxqrS3KVEMG9qR182xH66pFpUU4e9o11a1BEq53BTxhxN9mWbaajP07vTUNcpZhztUiBWV9Ge+FLvuhWZ1QmOloTmLwlEUpIVUaMGU+INqWqVMw0lfhgcVfQn41DlGBVUlsq1zYHkK6/WLhaj+JbdjesmlHXQdG66IKNF7h4duOhKYFf1zgcexRV9SDJ7ZZH4grI97EZBCEvNO27knYOnSqbcnKS5rfdFuSv8W33KLxl6iu1Mq+58eNUwUlUJ/LhI1kpl2sfbStuqYTvKFS4lmdjDZmvnbtLhm2MVrD0/ucBcDPNrej11R/eyt2h8BcvhYaQX6i7lE0JT0FN5PMGey7JiFSTeWcc2yTEOTnlYdulptBthtR2ly3hxxTWDSXZGKucVgZ+s/Z13yLwThPWK3OL77WYjJZottiJ2Ju3jcFbL2toiLPh7clceS7G2QUrqlLRm1a+wPS+JW3TBFRfO4Y6xK8Rabu/7beRqwSrY180wwd3OdANJnPhpVcZt6kgYG699hquuSwKOWWmxbJcH91Id6WS7gzWExbejeSpznbgt8e2mz5v90rzRC41b4KRZE+ohW2rs3kMXIm/lh6kz7Xt8Zger22/g/a1jFU0Kdt5uczhtjC3mKSEfYXqniqpBngIbeE8SkXKtywFplfcikEgvLQ6NZ/gr0BbEV31z8kamXkxe6k++RyCWAldbT/BW4vlOb1j+5u/rZQA24dmuOVaZZB+8FHeH0XN4NkBTVWI2d4K/TZOecWKMuypbeOgVVgQEMzn1uLD2zpYvEakOqS3Cc2XGn6vJWdGYx4rIpOqaJxB7b4+VrHWl8/OyLdECX3O2xIO+gOTOenNEBPqk84NigMw5lfs2v6bq4BI7RU/5A4Vf4bq+n3oBu8OTpplLLYhYZMcs8j0VFnpqo2juK6KPrSqGXFsH7GAGqVXQ0e5SEmEQMiHt7doS25Owyq5wjTrzo+rWQ74b0tCSeoaKyVhNz2RiHtYW0hOi70SJmS3H/kheWXFJ78ZADVccHSMSfo83eJpjwW1fU0LIu3mzxrctvscjPIgvbROTdaxPEZIQGcNy5CLJL1Prqqu1uZHgQDZw3ddSMrFdDGnWwtCWplGZm3KT3LTYMM/6STEHM+LL7WmJmBfBlo4BmsW+KG4cvdvLRtAqvFqKTZaKFXXLQ5UyFU1AddMPG7Rd6Ao5LW8JZ8hVN5aT0tB3KjKvxxq+u9rSQ9ZxstYNRNAXO3zsIsHGN96ujwaBnNQgVGAl2+IyudDvd4V0wnAnkt5o4LKYDNkRhhs/yiLe2kvDset3mVylF0Pqm+zY+ui5x8QW2REH7mjWeEBwwmgQxW1YKrtthCyL9R3ON3ZPSb0mbnlx40pihNB3fw8TfLpu40k5S26mtUXm56aaR6vQ2GbH5bJUl3QwZTdcWZ5W7cBWo34HQsVxUpdevj1agjpOntlukGNAX/LFtg6I7lxZnsohZyfY4un27NzJKZN2dHThxhE55OfaqyaLpa+i6IfrXWpwooioMme4HSFS/ZHJFuwGVZtbFqZogO69m6WY5RmTKJNf7fKcaEbeUhiXxv3rck+YeRwvU5rajfF4tHayoh81cXVzbqZTYluGJq+8k+36OuEKSxnje3Mx6+0xok7lLZYzynHGHYufaX1Rn86kRLIXFquWh+zGpizrFQa/F9fnO7ZHF92wD2pLtnk726YLfZ1qeaJGGSFa5zTgbPN8DkesE9cd7Eu6dNKPZw5uRK61+JHhD+pJQXn45G0u/pnrL8zU1xeO46TYsHS29EwH7DjCTlr5chQvK6HZ8jdEzP379sAbwTq878Y6EaalX2cYYocWB2gIy5pbPRHizVye5/2tkrpr9hLpvX5fy2bP9ORR5Le3pJnaUdQon7d3q6jWT9khEXFTqI9KCK+O8hiYCchiELJTk+xctlHFxOBQQVA3zNHidle+ttQVO8HKdUVXGqYssFgxNwAiT/piHHqtXi2wwlEiQkCLpNyw6iZ1nZ1NjXBnpqgvcPlpOJsxvWBgpq1RuBx8zq/odH0zCbrCeJUaUVjXdQJvL2VwtVC6mM7UVLjSSVp2B8oyaERPZV9pBv5kXO5Mb0ccu19FbYTmN7G3eMzMUsdlYYNci7oUwEIEX7OE6O5OPoltapJku9kSUSvIjD8IcXTjJZaW4/3BrPKxqiblVCGAXrukxdUcFTqW5ZFO35RVuHcLeQVggVfrMk9yt2R0Je0Vod5bREoWMr+sttZWRWJ6s0Ik2NhOkWSyUi0nrkVd5Ps+ESJEyA4rLHcP+7PGLWOmZf0u8DLfJ1sCMCsrh3eVjsLOcEqV5KxhLbQcVuzhMSe9pQiPAdL2/dbgktH2RvE+nAhENYXr9n4S8rK6IV2+Xgqa7E91tqjEfRwaBNlZwn6U+MkZmu1lxRDdaetUI9WZm/sZyQtzgWJXsffZBhcbeUC2DY9qtZQ35l6xaVXoRjttaUVX9IPcKHwuX0xXOBM7YSK0Kdv21k5h727iIz0+nGEisM/Nmu1chc+KSVdrzdFNuW4i2Q14c3nxJByX7uvb2TSNjcZfq/yeTkzAYlf+dA7WWO6suyKZxsa+WxSRU6ujvnJDyyKYbQ53tX1O63bKcXI1rYF3+nR3anUWMRfN1S0J6kBmDmVvDjaC6YYeZbczQNBjBiMc5uXITl5ZJuLH6nJLK+hmIXqldLG43rjbXOqyvH06xM32uOWRy2Bb6ZWpK7TGLI/kCzcrWck8aDdWgrc92a5SeEmQSYzaWWUHQ5hEvVonawRQwjqNlWx/C8SGrYzo5NnmqHKd57FLzpRSLxG7LtePzM5ZlaaPgCRBx0O79OSjgNLLQYxOx9zfSJ56i7hBvuAXk7zbDLpH/BpLfCyIhiZesZ29uUVrTUTipQRE7Svdx5sIiUt4e60xuhB0GeFbvrosqPFMLPAoTZfi5LtL8dKeK+7Gc/lxPWK6xC2l06LYhrThcPkFtLIRqtHyIdtcj9n56OaoZhbDWdti6P6QY1VdEaowcr1cxaF3u5iJdmQMN7Z3PW+OsF7EFJbSdjud+dUgHYWhO2vV4b5rZVdI88NurSbHINXOueLFgiwyx9N9CqgFq+0zvVNYLTPR9ry0d7KEuwXfH6R7S7RpuxRWNegtkgydWEkpMFZeSEExZd16v7prMUopaC7u1h6dtyVdu73blf4mMEqdbm+g321JPFq4YtlcF4EVUPJAI6CTtsg7foAp7Y6XGx27Md4wZZ58M2kWQfPiJLfXPX3X8ssQxsPqLhG4wk0qiYD2nPD9nIaVQUcOCwrTck51XWXbOq09WoKRtgCO13B+jMGmEJfUUusykXNukdAvFNPzL06sSW1owwd0S3qJ5iOBSiD2yF2AjpGF3pzVfVnTKLlqXGMKYyszLhWD48tKX8mLcQGHabHgj1kGy6l3Wiz4zZIWdU4l24akJsxRu92KrWuzYc46XJMGsXMSnO2QU7FaCFrUX6/LeO/Zq2Y4D8lmlBWmE7MikWhT3++4zX3VCltzd2mNxKfHkd2Fmy12ERWQ1Y1K63XE4OwO12yZLRzfkuj7ulBVZGleLFPIs1YIW/TueV3GoN7uDtvoTdvKi1WI0hnBL0aNhW+IyoO2gVZSrd9s9LBqhGPZsIxwCu8XpsYF9LpUW2GJZp7lHlpGuGDa+nraMHDfnm6MC6PRuM8MpxZJEWFHKT2QBIyiA9IFPu4zBo9sdrfurMtcnwnDOZUJWh07V59u2rrygScjU8dr9nrtMFIhYIY8ah4/HDywj6/OB9baEHVjm2teMY1EQsU1yV/V1cLzQph3AUITbRlWlNvtcUEmKTiuZXYT5kp5U46hLrhRvWrM7fVecsdJjjXMPvOLYOsNiWfcFV8t4pVxSa9+WIFcXK8Gwo9FrdzNisrqibofLkyWSMS+nqopWCqtst4M9P0mt+NCo1ZLry8tVaQXpyMnmOhmrPHQlXG/9ScrJ642FpQELZ1tfHXTSHTKXfSubsaTZA80jnHjGkdzA6Zkah3auEdXiOsnbbCv7sbhDK8pNBj8bns4dTB7o4mEilFv1YddgiPB1RuchD5duTVrMRKlYSVF6/6qGm6+7WbW4Rpd8c6LBnSVS6ox+vQho1r8yt8PCLuyQ8QcfIryUXnNwlHAjmG58BztaOiHyL1xtrE+HbArM+n9UrnguCqFhNZ01IRIYbFqwY6Ja2H7wgz4UV8uSHyQpaJYXEjC38DksGG28saC6QEX7wvhfvA2Iiyfdjx96akD7V1b/hRkMH7ZhX1w0z0Jvp2ZWLuSyo0Z9l4pEhIyrTSYrbqLqyEqzlx7vTyNSGJkeo85acwweLJG9bz02HSLn8jlRd2tYylhLiZ68qexDzK7r60xPx2Vexh61+2G2h+XiTLQTcQTmhu0KwbQvGlwOaqsEDPSwsMuW1JEB6AMppHjzSrCSnRrgVpd+hu1oVVrOzpRjHi7ayY3bbqlKQ2/bSRW2XCip5+4FON0C3GyqV6kOdE71jW7Z9ylgoWrwyQlY/ZFUPfnUtHh0rPdVYrbEhZtFz4uyd42X6SEwhz9c3tFEMySwvueTNwb2q8PCnyVaT9G2XBDr8urL6bLU3fPR5uRBeGwSOVMx3o/R1vdc6/VoB05WrcTHI6kA4DNOz9sMbhFDJo/cVQyyYW2IYyxvhKE7qUMt/GOOxhl3eME2thQb29CU1Ysy/717cPbfNj6OuD+l4+v5xPE/2cHmc8zx6+PtR7HzIHjf3qs9elfq/K3D2+NlwBFnoezbdZHryPN/3Y0+/HPHoPMs6bnE+D5advYfT3v75xo/prSW1L4fds105e2zPrHofCHN7dv5+9OtPPXa2aJbw8j8mqW9lWq4+dJkczPZr905ZfnSXTwNn+3YX6IFPjJ94/R65D6w5v/epj6BafIL0FTzQa+HqwAu7B35B19++3/AocZgJwwJgAA -->
