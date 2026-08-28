---
name: "rar-cowork-cookbook-audit-develop-contractor-network"
description: "Audits develop contractor network records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_contractor_network", "rar_sha256": "6350d64b206c945ba719b694d87a9cd270fab5c0186ce2d59fb12e6d01de2daf", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_develop_contractor_network`. The original RAPP
agent is preserved byte-for-byte in `audit_develop_contractor_network_agent.py` and in the RCI capsule.

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

Develop contractor network Completeness Audit — Audits develop contractor network records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-contractor-network
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_contractor_network_agent.py` and embedded as the fenced Python below (sha256 6350d64b206c945b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_contractor_network_agent.py` first:

```bash
python3 audit_develop_contractor_network_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_develop_contractor_network_agent.py   # or on stdin
python3 audit_develop_contractor_network_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop contractor network Completeness Audit — Audits develop contractor network records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-contractor-network
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_develop_contractor_network',
    "version": '2.0.1',
    "display_name": 'Develop contractor network Completeness Audit',
    "description": 'Audits develop contractor network records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-develop-contractor-network',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-develop-contractor-network',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ca251399bfa49239',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-contractor-network'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/audit-develop-contractor-network', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditDevelopContractorNetwork(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDevelopContractorNetwork'
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
    print(AuditDevelopContractorNetwork().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716adOjRrbmX9G894Ptq6qXRQhQdXTEICS0sO8Il6PMvi9ikQCP//skkqrKvt2+tztiYlSLBJl59vOckwm/vTl9F1fN26c3NXDKxcHJ8yQOmoVT+gu6uldNBr6qzAX/Fl5Vdk3i9l3VtG8f3vyg9Zqk7pKqBMup3k+6duEHtyCv6udcxwNTF2XQPeg0gVc1frsIwT2vKuo86IIyaNsHr7rKE2983k+c0gsWTuQkZdstmj4PPrpOG/gLLw68rH0HvIPBmQm0b59+/uXDWwJ+v3367c3Lnbb9KsvuKQn9TRDhKQdYnTtlBKbVI1C9BNd10AChCnDLD8LF6+rHNsjDD4v//M/s7jRR+9Onz+Xi9fn8Nv9R+nLRxcGiq5y2m6VzasdN8qQb3xdUfnfGFqjc9U0JNFy0wHJl9P5c+Z0SsNTf57Efn0zeo6D78fNbBURwZrt+fvtpAaz1+a3p59/vM5X6x5/e8+oeND/+9J1O27tp4HUzMSD1+5fX9YssmPh9ahI+uP4dUH160A0+v/1BufnzlHvWE6x8e0+rpPzxSbhuqltQzg768ae/IvtwU5603b9E9+cn4ThwfKDTS/CfPjyM/Mti+VLoG82/ZlsDt/47moDpX9l9WLwM9Ve0H/b/L6TzBETvN4v/U3L/bMHy74uf/1K3/27Bh0X4+W0X5MkNRIebB58Wv31RpT398w/+95s//PI7IP0/klGrvvEeFL4UTpmEQdt9+fLzD+3j9g+//PxDX4NYC5ziS9/k/4zmP7Prg8+fLPia9eOf1wL+epmV1b1cfIv0xW9V/b+a398XhpMn/vf77afFH/Nl/iwXsxJfmT5N8IecaYGsf7DjT2+/A4AAQNL03mMYZPl//MeCT7ymaquwW6he1c8oU3ZJEczCa3HSLsDfObcbACJNmwDDvuaB+J89PEtchYtf/7f3wMiP3gsjIWeGni8vFPzyHQW/vFDw1/eFBuhWTRIlpZMvFEqSPpdOFJTdzLNugjZobgBN3LELPgIc+jj/WCTl4tf/ifSXB5X3evz1gajJE50U+jQjUwtQ9H3WzoyD8qWLBwA/GAKvBwzyygPShAnA1A9A67bKbwDZZku0WZLnCz8B8A2YjQ/awFqfZmK//vorQOb4c/mE0tXiWRFaCEz4Js7i40egVpgnUdx9LgMvrhY//Pb7D4v/s/jvVj2IzzwkgOkvXwAJz6ooLEBu9QWYBtwEHAuA4+GL335/GReQKUEJA55LwiR4LgaxmQX+V0urR+ojusYXbgAsDKxb1FXTAXxeJN374hQuvskLmM5DM4LHFShGflAHpR+UoFR1sQPU+WbJsuoWLQjANhw/LPo2eHD91W0eRSwoQJI73a8LnpZAvahy8N8s5mMSWFyVCTD/tzh43gdEmh/axfYrifeFMEfjonYap44b58UjdJ5+AXXi63JA3AFl9/65nCtjMJvqkRpP84BJwDLey6UfZ5/PdRfggN9+5f2Y48xVTXtUt+Zz2b7C3mmCRykHooyLqE/8uRj87RVSbVz1uf+wH5B0pvTygv/yyiMGd3/dJNB/bAwedXzxuUdhBFv8f2wwZhmpw0HZHyhtv1vsBU25PG03c51t/OyaQKl/MHvkyffy/xU8vmLo5zJPQCA049+eMx8Wf8154lLfAOYKpTzoA6mA7Wa6j2ico6tp5jh2PpdfwfoDcPADmYBDQOqC0J4j6ivDefSrpDHIz/n6e+F+2Wm2Coi4Rd27wDKLMAh81/EyIFUzZ9TL6iA0gzm77nHixX/SagGogwgA9BdAiNk1ANAfphMqoCZIprCpiu/Tk7kdAlL4vQekBT1m8L4wQVLMgdGCTAQ9zTwHWOGHB6lFEQAbAxG/WbiNnfopzOztl4DOjNFJcP+j/V9D34P4IcksPKDp+E4HLHmfQdUPhqdfv0n58hQgWszR8Vj0Z2e/NF38sab87XP5kPAbjoNszudy/AfTLEAWFc9YnMGoBYBSBK/wAXHwqLzvz+L5rM7fZPn0D534j/9es/4oh/qf/fZpEXdd3X6CoGcJ+1rB3kGGQCBCkjpon9Xs4yvlPn5PuY+vlPsT3aeZPi3+Pdn+ROIV0p8WyDv8Ds9DXOIFc8y+PsAU9Mft5SM2j34uleC7jwH7qgAwN5t+BOXzW1X5OgWUlqgJonnys8q0c3G6g3r4gFXghc/ltzh45QhA7TKaS2Jb/SF3H+UVePXptG/oD4bKDvD252YsCuZ9Sj6L3wZvn8o+zz+8lU4R/Av7kxnhQaQCY8y7GpAzoLfpkuBxBZQCA4kz//7zDkx8/HDyZ0S3HZDSaR648MqQF+B9mBvbEmDKvImYy9gT8sHWx+nzbpa6G+tZzOeeZe6fvjVX/8j1kcKAh199mjP5w2JuhD8svvW0HxZfdxmPfVvZg23Wz3M/PesJpoKvb3O/bSrd4O2XfyLGq73+CyGSGUVm3HmqG/jfIeLhtdrpABLqCgdEqrxHAzEXzXZ8FNd/VBswbIJrD6qkP4v83QbfRaue8vz+UKV77iF/e/sKMi/nvfpFMB1k88d2rpMQiG/AEFw/IxGM/dud5Gs9AEXQyQAC+GoN+zjmojDubbC16xDIxsU3mE8SzsbzUQIOHXftwQiJewHqrzehi6AB7sOIDy6dENB7xvOXuRlIZpkCOAxWGwT1/BWOrtfYBiFQZ+M7GOE4PkySBEyEPqgb35dmAFNfij4Vm634ramdDfLS97c3F8fAzCPWnqjnh4Y2hoOjhKvE7rLBg4ttbU5uol9Vu6V13+H6Cnd3Pl1EttDrbkSLo3JEWlkfvVE2GvUQaet9SWyltlvaNLpUS9MhepI6OKow2C3uiXZ4Cw9BdaLiw0SqyHi6qmfdCFh7rccmu75yDtMXbDk4Lq/QxlhpOnE1BLv1NwAlkSWcjJsA36uqw6iTYWN5qTLkbsht+3i2D0GorrEyujEcVwo+bxjlJbYnzmDNZm+MtScpuKitSUic1qN/m2p8aNfguyRZ1O4R/tiztwNLNp3DZJ0luozZ1eblzK2yll9dD+6gFwhu9rlIu7pqp4Nv9VcbxbK6vOsTHWvX2rkE4ZSt+PSYVGfb01i2kG9sFJtqdPUurhb3xv1s6bBtb3zaMcqMo3uVxcc+KS7E4WbgTZMHMOSrjO8lAhagQsJyqUSTabHXu/iUpFY+bm04OmmWOVWd1x44pit6uzneyotNt36iurLMjKp7FC4ua2093LII1mBTt7PPg04HY4hEJWxRbS7f3LSoJcMjkaQ/njlvtSNb5bgXIhbV9EC4hKaTIxfNSw/1kBwHs6o7ZOnC0JYTjWaihezCwHFJB3zVSF1Dr8vsuspbSOiqNQLvorjgto2YEcgalXRHlVt0C0OWkgmiaNkHKV2OU8r7k4NWgiEXSIsd9PG2ObeWOe6TwcVuTmycCmoactxNMTihYRVSMS5hWxtypbNDnu+bYbioSMqrMSLwbJtgSkJUJzIlq2BZb43OMpzMIld5wiR2b11ir6D5wKZLuGQEdDKGcfKbrGjKDK+uCJNf7+lGbFnywBDYabPbLve7aTc2+n0fOyFBTaI3NcTSCS/MNgvL6qa3XYKht/M5I2OU8+F7qdbAq7e23rtL0hBZ9ZyFB1mrWh+Lk91B0NobXpEuwcWmJpBwH9erLXeGrVoUFR4fb5jIL7mkyPi1YqJaYu0tjz1S3rZl9vpSdMTT0RXdvQIn8InWdjJpcgxNcgf/UGq5eNxPXcBjK+oqpQ0+hHaHDUhcKB7s6mIijFMcEZSH82eRV3ZSKUvwMudScZlA98PxbqKpso3doEWXW4huNiE1xHkHlQdl3fkWxJzTjadfrga0WxPdiUFyYTvUEhCy71QNOV23WlRC9UFb92NVLT2zZYXOpi2Vxyr8SskTN4opaoiqiam0Tk/WElKk+xoNMrGug3OaEhBZ7jNjlwdirasTR7bICRMRo9Su0tivK6XUVZMRtRRU1XySpL2WH2NLHQ34LJ0bsetH0rjU1HG7jvJ6O2HijRXdomU73qVPe7evSoIxtF3GoQneGrp6VaiNfqOPWBaNldGJN4sPwrAeHTvb1iJKOWO26zfo1XVSXhfbdTmwsDIVRmF7KjrlIjUa1tmI1bWvsfY2sNulEKkAtdxJwCsTXrn8VG0yJ1oZKn4coHQMdyfpJGr0ZMS5cKM8pMd6MlRZH7EDmMgEOSh3QwyFZAXHG/14P7LylPmJn8fcykFbJyUqZsgSxiJrqtRrxe4BwgiQM0W2nezOx1Lp0UOWULiWQTYykYN7OKmimqv7SQpvVqQdYjdziEONEHwyrS6csu0xvTrct+NGOeDaScL25q2JgArjiF82Oz2lErmET/j1Uggry/GiQdrD28MhZ9zE3jsN21Y+rBSNcLAH2TjpcupLPLyPFKWZoqZMtZvYY6osprYI3wHQYb5LbsRAX/qD0SqT2N9IdAhKe9yE5Zo5ZaxBq+sB2Sw357OSGSECZYNpS/fqEFWZJEHhdG9km1xZFw+9e8cMDUk4EI/ltFnvrxDGwCTwILHfXmqX2SknB3GWDTycqHMXKXCdOBIvTIQcJWe1yfXpuhNoFOVDLWVFfVnRXCWY9E2W08FLCtAD13uzDPaGlyxVRXCI7Wrbj/4+tB2LDk4poijGsebP3nG7vN6vdkyY+Ro9G7umL3bh6hoER49Z0xt/RZb14B06X+X25nJ7ulul2qTDtfYdmy0aXRC2dUCanSRTF305m7xC91OomgAc1wgPE1FdnCYhNvepeTDR7bQijnDCF+3Z3dBcMe1XN8G7MIgj6fRZRc4Qy9CNujwSxAombEk9ZXio98s1zZ8dlXd1KqsL5XAoGdmZBJc0rByDLtod2m7DsblnJ3iJcLV+5O/CcN5uTmuzt6OCnmxW9wlDFmH2xFo7AJAAa28kw9WRRhfJ0LK6GBLB/khTaz9a6qxeKDuYwen1SS0OR1m5ObTtTqAamFqMUDf9iLDFhZFuVyLqMU6Q7KXdbrwzSQeXvnU54dK4vn1UmPh+TiLUOzOSmfg4mpp8K0pazIkX1pWdNbpe2dmOqxo0DARa7k335qCblCNZ63bew50RmztI6fzmUu9tc32shsOeawcnwlnRAdtakOpum1PGcl0FpU9rmb6954pF7FokOndUH+Y8pZJLXU428ZnJjx3VmjuFzi+tmain00nxmX2C3pktfvC04RZJoJjA8dLZdyc+Ox5xe7W8y+GUdlnmpeZ0NyhLjpdxBVpAEc3sRs9RC+M4OujT4229JD0FXd5tSre01f5oxp2lBAAFE6TrBBEamlsrqc115PzJtSeMtEBuqp4beo51uhyYaU/3N3O8yXUU81uZ8k4HyU3rnNBlo3KHLdxzW76TN/xZ2UiNgaolwptifxdgku0KtACd0r40ucM+ZY/u8ZCLdX66lpGXSVf00pVdqpUaNxyhTshjPfevoHixVpLei/KknDUWESZlrM1R3zPoKUCy3XXNbvxdduaRIbjSTsxH2oa67OlBR0in489UDNUn/qA5zsErKjgRCycW1J3fqQaLXrH00lkxRRd5TUYQm3IUn1P6hTuQNCJGiC2Ra4TbJAgqwJ61ji5Meb0LEbHf7AJZ9g7cKlflQkttYr9bLyHaMMT7zYhpJBsV4cYfeSJKFdvnNzadWtM2MXZTs4p1Ke3MwGuWFs6mNny+eavWCfLlwJz79R4xPUskq1hdIip9u2rXVcLfpqHeZPtOJAv+cmOaC+/x+qoplMheDqJhheQtyLjAvGgURHA6TvCSrRLF6uivbO3MaCdZdDFkpXm8tl8zUilcUDMpcCjqVntbnTxTrg9tPBJoW2zQPEWz/kqB+iRD5QrGaqtvhbMsqWoARZOOnGrZVSi/3wq8WtxrbqMd+nKtWjDYDR19g4RrJTznI+71/Wq1KkBTqFzdCwupW20jHluhd1aBvyaHqMKumzNFjdRoseL9amly27EgQdyIytwAc477DkLz9bBXlvmWrad85Cm/OcnH6GB4a5/HBm8ZiHchvzYZHe+VtuG9c3LmLx6bXW3jKu62SG4O6qkcC+3gnVA6jzgV5nI2qMHOhiNOSa+cz2JVrOXIrLRBHlRkg+fRAY2vQjYlF/kWHfdXrrxoq2W80jQFWTmy5Jk7puP3xwtGJuers9sj0NRwDmU7m7t1PO4GRC6EShGv1u7EGJxxgQ8kjvOULAdBc2k7RpBMjY9AV5tn1tTB8s6K3XvPhKOK72j+AhKgAllkXatMZRRQ/hHhPK3Z3inQRLuiDVsKXHOksWvObJyBtohcYgJcvbjKSgwvNR7YsYg05/1wYml1MLOW610ybXbFYMdwjbn6DsrjZry7An+VWy/VtmFU3Tm3ZlIlSnOe6Tpx0sYYK7CmdcvRs/xjfUeb8JCf147awTiBbTPmTtRCqG+1tVhUNtVNjiCJOz2+Oiqh7mJ3raFcx4TWeHN7SbFca1m33h6iEO+0Kp3jQHjVyrgtVQKPyFs8dkSOmtvYRkdsaqnunk31KkVOPIznBY3p9FLyLlwFUSs9uBil7eBU4AhLXpxuUAwfPf2ucSfqLgqDVcLC5YC7jGImU6V5oBHc3ZarjRzfub6RM4ekTuuNJcB4xWxdh8IbEvXYCdv77p3Ehs0qqAPn0KRHmacqnEUhV2WxIbRO+qbhdtsChsZqA8ZXGOT6Ian4JEcKLOESSwuausuJmYpE2hhID7vNdUd7at6Qqtg3whkTHZqhLiMHwxbjx8G0Gui7PtKyI0T78HpZtYrQSJQMj54c6Fq/u7BpJg22Vq3xcU1Jdm8kE2lWe9diiSCuSI46esVtS3lSb+2JKS1PB1ADBhHm2ObEQuvIJPhAIy/V7jYitzC9KhCNuUQTsdC4323I+GJfzq7vx8YoTPbKVOodfdNWBQO3O6QM3WI3qPeQG/ytJ4grrNjpS7TxPEKFJvM2rCBTlPaX8zoKEP6yLU6nsr/gbriF/S3ql8RRo+RN6JA+z9hgX+uejOQyHRCS4EZolZpNGSgeFjiS6AUTD5Vly9WbuBip+9E27JucmMROQFu5uvTk4ZyCNE2tU5JfeSJvoNFV2/3xHKdrvnQzAZYhyxjPl5FyYQev15XG3K8HgFkOykti5BQyfGhhByuItOGlkvKuK7XGFFVjEq1Z9hZxx4RDylNTtx2rnndSu6LNcliDmovJyFFC+y3VHsVkPFYmBxOjo3PwenfqpcK6yyVtoKeC8+PuKvVLEac5PxewfvR8huOnaDRHdC0LxQbeZImmxtsglLnEauR2QwoIwoVnzYT8nu8w+rgvEIw/NyW0RYUjZe75I1QyB4FJMDoj3A4iCqoA1ZodN81pO97NnV2LK664m77RoDev6J1Nwg4urO/kNdKA9urIEAjl3i9SzGXHSqS9MLK3Lsm5+5Gn2S2065Ypc65QucIlZTuc8xUi3/CtyZ6WWzQebnsKZolQFQ/RkuxwaLO8CPsWJ/C2LwMfwvbUgVSPoYtDPhuvZXG5naQ29IibCa0KwbHdmtDOAy9144DgraSZbSdCK2wPLRGa98ZbG7ip0OCm56d8eBLJk65QoHe/3i4Wj66PK9DPsPVmOKRV0SCucISxJbGMHZW+MKzacyWB48Z6Wwv4vasuhM91eFas6qxFndjEtisdzjYXI1CYY09ilBgTNklJyFa9l3S6vZq71LrbfGOZMNmH7qqzk03nL+9ub0Q8fepKfweVXLbs7hQmHgdYRzbqfkdmxLS9UzRu0yLXyGDLCnCVMYBh8ANymqodf7RtdrtbG527YXdZv844OZS8CDqasiWhYEPP3BKiw1sqX5qbfX+/NbG9czmuFnOiv2+mMYxaZ6kgbg9ai5OWFsZUxOogDgR7qSD8DLbexJZfF+gEGUm0K32vpzB5165NzkWj+JSqoVduxQmWRw1L7lhNjvGopSKEr1MvJJiJkWqATZd1V+WIIFWWgA/SwW1riqL+/vbhbT5EfR1g/8uPoueTwf9nB5TPs8Svj7Eex8iB43968Pr0r4v0y4e3xkuAQM9D2Dbvo9eR5X85gv34Pz3+mFePz6e789O2oft6zt850fxq0ltS+n3bNeOXtsr7xyHwhze3b+f3JNr5VRoPfL89lCrq+fT7wXCmGjS3xAu+dNWX17sdb/NLDPMTpMBPnC54XUavE+kPb/4IXJN47ZcVvv4SNPWs5etpClAOfYffkbff/y+zmvwE7iUAAA== -->
