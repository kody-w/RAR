---
name: "rar-cowork-cookbook-audit-maintain-open-service-requests"
description: "Audits maintain open service requests records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_maintain_open_service_requests", "rar_sha256": "4b11d7cb0b31cfa00c7b0d7230cc4f834a526f5a788be8a520dbcbfd2d52f3dc", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_maintain_open_service_requests`. The original RAPP
agent is preserved byte-for-byte in `audit_maintain_open_service_requests_agent.py` and in the RCI capsule.

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

Maintain open service requests Completeness Audit — Audits maintain open service requests records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-maintain-open-service-requests
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_maintain_open_service_requests_agent.py` and embedded as the fenced Python below (sha256 4b11d7cb0b31cfa0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_maintain_open_service_requests_agent.py` first:

```bash
python3 audit_maintain_open_service_requests_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_maintain_open_service_requests_agent.py   # or on stdin
python3 audit_maintain_open_service_requests_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain open service requests Completeness Audit — Audits maintain open service requests records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-maintain-open-service-requests
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_maintain_open_service_requests',
    "version": '2.0.1',
    "display_name": 'Maintain open service requests Completeness Audit',
    "description": 'Audits maintain open service requests records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-maintain-open-service-requests',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-maintain-open-service-requests',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1827097505563b96',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/maintain-open-service-requests'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/audit-maintain-open-service-requests', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditMaintainOpenServiceRequests(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditMaintainOpenServiceRequests'
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
    print(AuditMaintainOpenServiceRequests().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716ebOi2LbnV/Gd90dVPTNTBhXMGzeiAUEGkVEZKiuymEFGGYXq+u69UU9m1bvDu7ejo830KLD3mtdvrQX+9uZ0bVzWb5/ftMApFgcny5I4qBdO4S+ocijrFHyUqQveC68s2jpxu7asm7cPb37QeHVStUlZgO1E5ydts8idpGjBe1FWQbFogrpPvGBRB7cuaMDlOvDK2m8WYVkDcnmVBW1QBE3z4FeVWeKNz/OJU4B9TgRINe2i7rLgo+s0gb/w4sBLm0+Af3B3ZgLN2+eff/nwloDvb59/e/Myp2ne5RFf0khAGO0pi/oSBRDInCICK6sRWKAAx1VQA7lycMoPwsXr6McmyMIPi//6r3Rw6qj56fOXYvF6fXmb/6ldsWjjYNGWTtPOAjqV4yZZ0o6fFkQ2OOOsddvVBVBy0QADFtGn587vlMpq8df52o9PJp+ioP3xyxswYe3M5v3y9tMCGOzLW93N3z/NVKoff/qUlUNQ//jTdzpN514Dr52JAak/fX0dv8iChd+XJuGD618B1acj3eDL2x+Um19PuWc9wc63T9cyKX58Eq7qsg+K2Uc//vSPyD48lSVN+y/R/flJOA4cH+j0EvynDw8j/7JYvhT6RvMfs62AW/8dTcDyd3YfFi9D/SPaD/v/N9JZAgL4m8X/Lrm/t2H518XP/1C3f7bhwyL88rYPsqQH0eFmwefFb181maZ+/sH/fvKHX34HpP9HMlrZ1d6DwtfcKZIQJMbXrz//0DxO//DLzz90FYi1wMm/dnX292j+Pbs++PzJgq9VP/55L+B/LtKiHB5g8Yz0xW9l9R/1758WFydL/O/nm8+LP+bL/FouZiXemT5N8IecaYCsf7DjT2+/A4wAWFJ33uMyyPL//M+FmHh12ZRhu9C8spuBpmiTPJiF1+OkWYD/c27XAbBrkwDDvtaB+J89PEtchotf/5f3gMqP3gsqV86MPl/fwfDrDIZfX2D49R0Mf/200AHtsk6ipHCyhUrI8pfCiYKinflWdTDvAIjijm3wEWDRx/nLAmDrr/8K+a8PSp+q8dcHuCZPlFIpbkaoBgDqp1lLIwYw/dTJA/gf3AOvA0yy0gMShQmA1w9A+6bMeoBws0WaNMmyhZ8AJAd1YHzQBlb7PBP79ddfAUjHX4onpKKLZ4FoVmDBN3EWHz8C1cIsieL2SxF4cbn44bfff1j878U/2/UgPvOQAby/fAIk5DXptAA51uVgGXAXcDAAkIdPfvv9ZWBApgAVDXgwCZPguRnEaBr479bWWOIjstku3ABYGVg4r8q6BTi9SNpPCy5cfJMXMJ0vzUgel6Au+QGwvB8UoGq1sQPU+WbJomwXDQjEJhw/LLomeHD91a0f9SzIQbI77a8LkZJB3Sgz8GcW87EIbC6LBJj/Wyw8zwMi9Q/Ngnwn8WlxmqNyUTm1U8W18+IROk+/gHrxvh0QdxZFMHwp5iIZzKZ6pMjTPGARsIz3cunH2edzCQZ44DfvvB9rnLm66Y8qV38pmlf4O3XwqOpAlHERdYk/F4W/vEKqicsu8x/2A5LOlF5e8F9eecSg+M97BuqPfcKjrC++dAgErxf/n3uOWVbicFDpA6HT+wV90lXracO5M5pt/WymQOl/MHvky/d24B1M3jH1S5ElICDq8S/PlQ/Lv9Y8caqrAXOVUB/0gVTAhjPdR1TOUVbXczw7X4p38P4AHP1AKuAYkMIgxOfIemc4X32XNAZ5Oh9/L+QvO81WAZG3qDoXWGYRBoHvOl4KpKrnzHpZHoRoMGfZECde/CetFoA6iARAfwGEmN0DAP5hulMJ1ARJFdZl/n15MjsISOF3HpAWtJ7Bp4UBkmMOkAZkJOhx5jXACj88SC3yANgYiPjNwk3sVE9h5m71JaAzY3YSDH+0/+vS92B+SDILD2g6vtMCSw4zwPrB/enXb1K+PAWIzsH29NGfnf3SdPHHGvOXL8VDwm+YDrI6m8vzH0yzANmUP2NxBqUGAEsevMIHxMGjEn96FtNntf4my+e/adB//Pd6+Ed5PP/Zb58XcdtWzefV6lnS3ivaJ5AhKxAhSRU0z+r28T3tPs5p9/GVdh/f0+5PtJ+m+rz49+T7E4lXWH9ewJ+gT9B86QjYzXH7egFzUB9J6+N6vvqlUIPvfgbsyxxA3mz+EZTTbxXmfQkoM1EdRPPiZ8Vp5kI1gNr4gFjgiS/Ft1h45QlA8CKay2NT/iF/H6UWePbpuG+VAFwqWsDbnxu0KJjHl2wWvwnePhddln14K5w8+NfGlhnwQcACe8zzDkgd0PK0SfA4AnqBC4kzf//zfCY9vjjZM7CbFgjq1A94eCXKC/c+zP1uAaBlni3mqvasAGAicrqsnQVvx2qW9DnKzG3Vt57rb7k+Mhnw8MvPc0J/WMz98YfFt1b3w+J9+HhMdEUHpq+f5zZ71hMsBR/f1n4bOd3g7Ze/I8ar6/4HQiQzmMzw81Q38L8jxcNxldMCQDyrRyBS6T36ibmGNuOj1v6t2oDhHOqgaPqzyN9t8F208inP7w9V2udo+dvbO9a8nPdqI8FykNQfm7lsrkCIA4bg+BmM4Nr/VYP5ogHwETQ3gMjahWEf81zIRWEvdCDIw1zIxxAU8rx1iKNrZ4Nsw42D4bgb4OAA8l3PDX3E3yAh6nuA3jOsv879QTLLFUBhgO5gxPPRLbLZrHcwhjg731ljjuNDOI5BWOiDEvJ9awrg9aXsU7nZkt963dkoL51/e3O3a7CSXTcc8XxRq93F2W6Obhuby3rrE7m60vj4mEmsqY0nWIKr7rTdFBbujL595dy90mkpofSqzhHOpfARO8VVfj3ou2O/FgV3czT9lkf4+zrNiGu0lviwDwn/TBPatYKnnAk3V1XLxqq8bI+qTGZysmHqWsOOk5VVealSW8jOfVhIegQZlyskXTpusAtqWtVujDZdHMaCYpPGN9pF1Ry9N6EusDZwSMBqlwu3qVGaTXZLj6ec2zA3ttyx9hoPTGa9ks1sg0/aNujdCRcNpT8NwtGDkuYgLGvdYdJW992L2lWGxx/ZphOLjnFjL4NvWpMtWec8XuJ7a+5KfrtJ+X4460Ki3zLXWobHBioTVks5u3E5AbFFIaoMjcg9yzXT7jJdy4xlESOJ2mRzz1RTOMEXU3Xp4Go2+Am+91vzBnDGu55KBzmNFHeVhd31wBltTMfXIrvveSjmrp45cXHQGEfWVxPHRYvU4oVmNxq2Ep3uGsYKFsbkJL681G12ZNoKakYNteQtpG+PqaqVehMPUHFbBs5d42r/qrD3O+4qxlBbpxaCydhw0bg6acW5vRxOypKvBdP28508nWwwKXGX9krcUnGt3zPGx1tOPuGwhjfmpmlZqYvOhHAMunNfyP5SjRnqmh7V1pNVyJr6xHIPu11xsFYx3FpBTfI3ZxD7dJXDNoAVAR6hQdoxtcqR+cQiQ3FvGCaNCPxOTus+kRp75co8hfPD7h5bGnwVtRiWOfRcH/zLuQwVwUZX3q41KPeW1LB13ciTeKRrpVMpVKajcWSKQhYaPpMbMs0QcZjfhcEEUOsLVGjHiKmkXUyGDbQig4DAryjC9VTGouTWWhcTuvVCu9hz604NWt9l4CbQTB5jGwPbZFJGDbUc+jpXbwIBO+SjzdzTCDvKGmcPu+Qs78kb1+wzBTvGwD2lcJl07SJu99fivIza5dRLiRVX+8Ay2vOQ3Z1VdCeO1KlsosIhtfsZtaYyFelDRY0b70CR1s3ceGMp4gEfbVN/WmWGxep4Fpqnad+zUqKP+7LgOJuZNEnxxcKmCirjpwKycFheybyxneRoiVctLsoREpUa3PjAHcPEmlHjeludiCHDN+HVvfXc2206RCXnrnYbumuqUjrZ29G73GstqBhFaOjVjpvC02gwJprA8b3BWFhhLvRNLEsiiKo9JzGMEDPQqm/AABCnFdqtFcraLrtpIjeMsjGv1YUuhxBGSllFbs3WVpdB4NDYhslUPV8f92bbYPc7jUcO1GQ+pY8wqiF2IN6XlMrINwaBZDkS1reVFAw3etOcI7vf0mYfZFygrHz5ck2Sy8iFtwKKaJ6zboyr1/BkFujayxubyPU2MpqKZPvLrUC6idnXko1rLe1tMjs36bbZ6JEIX8aLde7882QoZu5qV4vOm+mAb4Ib056QSdzK9qE8weeuwAMaL+7aftynYwNbtu4Oe9Xtjj0LAci+1EbvLSG2Og/HHl2pe0iuK4acUnHPeoVt6SzS1hy3OqiezcWXlWCpsHA2scQy91ekWR8iKxrVDHLh+FZGWoPJiCOGB926UzZ0vlm5X0G7IC4tkItVu+2TZjzKOyKj2X12jlYiY8KkU+HJMoqT1VaNxv5ITFFKaueEUcKkvlXwGd217bSHhkDJaPes50JKxk09XhGVPbRru6fJc6xSEo1PirFn8lqmokCSiJ2nnJvw4Kkl0Rbu+qSvesm0AiAWXmGy1KPwGPZsc1cMnuTSWyuq9m61tC88r+K6z5j5IPPkwB/3NYSKuGwiBYEcULYxEUU8sVO2akNU7sdkCFH2Oq1XR3k94ju/PMaMYklruzPcsVRokaiQ6qAdTu1q0ImO0urMGR1dItjDUYGnkyTe6j0WcUaCWuJEXq6HCbQ4g5MGlu9phnY+CRBZnopBImzL3TP++rjVyDNDl6oQ4UvnVsWbgNkhfMbxgdfgHTWwzd7eqJPj96OYZbgzMfRNrQf9qjqh1R0ZkLQ3z/FaNcWJrJ4syKe1cDeIzHjihhzbGsbZZrt7WuCMdmftNhkaZ9APdymU6Zy2Uziuwwr2EOsAVQ1G9Ht1GxnCuVJtozQcE0EpZFtgxFpNe30rmZ15pYz0eoBFXrC3anyLz4dmMlbMZXOWUQ6Sl4MV3c680Mqte7mQI70vRjXUpEudW/y6QUfGjo+YkqZVSTjmsk8ON8gWDrykCHtmyKzd6gSpAbfvkT2sNJrCyINesWEsWJxL8m2qZz291SdbYq/3S0lSFzGSTyHDkuFguAFSTvaIg13E4OsIQBQGzUfhetTjkSGbtea4FL1s2wCvLE+67g1vuEgxObZTN62NUDHxJe6cY68pmKw7HszyvJH5M9ReYmO/Ulu/tmrayTdseT/Qx+buEFtNiszAIjey22TEJYA0eequvEZR67Esd6q9tChT09C7RkBDl0EHztJ8S8UsnokgozKOdJl2JH3WdZXLelJxrg00OJi+u212XJDHe2XP8uhSUu+NIi8hTN2x3L3BLwpNcLnrtDyA+1ZwLicvcwRkYPs6xhCvN8NTbwEMG0BpU7EqgEcikdjKxzBdRxobFBH01qVXtNmhXrA/jFKSFchaDrIti6rWSAQ6XLtDakU6eY6OJBkgG8fREDozWHzwuWTQj+feJMA7XnpnrJ3sqIb2iawfrWsFjXBxghKy4kd9UMbKFmxNuG1QmcR2nVobG3ji23W0WqbBsFW6zFtFLKlqa11NubTKtn1Wbs6VfaMoLGWtkUSQLM3jMe2stXwhFaVTeCTSqNiqt0v4nNOlsoJSWt9xbK2X0EH0kShla+UaV4jqImsvPAi0SJ3xSaLZ6eytybzUdoTVN5cKIphbX4R838jdprtSpoARKXaORdfZRepA6d24TFNdGEEXo1SqIBSRUUeZO/J8geb7fB2pVdOBue6u3jYRLMTVHRu2LIIATLqsjicQcxiN3lzElzXYyjIUT9xaOuYBFYl910T1Nt226+sRx53QJo/6fRMtRdJB9uyeaUFPaB3CRi8v6IqHKxrNcnqQlyMsdRNpXDrMvl/97XlUzyDJ8qUIQZs9fZdUfTMZp6ysun7N+PfDuUH81FFcDupWNd/7ob2vxG2k6W2BZrudJFyw+qid91Ba9GsPbjXhfIAU1o30kK6am7Y6DyTMcicwRFTngDD1MGPw2/lYIRjW66FzqvcHvk1qXzzIKR4MCO76u306IUKcTENCTDTF0+WKsv0TleA3PyUbQrObmqLDM4s5qAmpvGCxN1Q6cxEPNXchDck75thkucI95nrE/DN/CbiEJ/3NnlAtpdT5FGkvtLS/eUya3o+xiJy3Ck5KhNFWhkPgugFfTUMpfEbSfJKHk6E652Ocp8f6fowuDQVddgWUpiFxEM/o4Z6vkqBHuuRmNE1oRXtha53kOMaYPase+Gl98nY3Cr4iduNdTuhdtA1+v+UHIYaH+KJDxl1ullRMQutTniM0fXc9hGZFwVZ6lysV6UaZu4sgD1fIiKzBSJzBS5jegE+ZkJQU0+VacTN8rq1p9HIzL4ZNIRozwMZpe+32HatfBJAvd2NCPSnTYbHf+0fB4DXOYJjxxnGmn9mmefC3EMXLCMrtt4IbprFhuJf44LA57RAqfkEol0liV7Tco3XK+5xSL6ixLk57m1rpfSlNssDwtmNeM19CsmO7zXGF5L3lajgzabLMskQnGgiu5W2Sl24WSHBdS5ixM3Yhi8F8L7OVe3dXFa4wK9n3uGLlsOTdb1CtJ24rLALD/uhvRcQ4RfZhu55Kro3OWIWKviCeoUMO4obq9onFNhuiPfvDpbeDGxH6p6UsTf0uE2SfHkKOi3D7hOo50noM5vKKQaHVRaRM59rjKKxEEYbcVFpbEna8M3prXcK8466XNV70/GSLocvhmzuM5lXn8vV+r4lRgwnI5GgONIYFp+3II0Mi69WYgimSLjBsp4Y4GfTHhhGwGl1y/R1ae/RmguXdNh5syUco8iAbMMJI8ikqPJPZ7xXJybbOmUJWB1sfE1fTyZIZ71KxE+quTC9sftySwFnjESY9UtBkvOc1A7fx5tCY5Lg+8EZyqVOfVaBgV5AdN10JhEePjg9agZJABcNmNT674KcAt/bBoczw05ndbLabTtsdVqR32l3WpGcPzCrgIlls2q5TOuy2yRHjXhEUpW/A5vYK155ryJM2mNz9RPonaYKzq4VLx3OIjdhgrOB+hRwkes2sIpk8WeTtyLG5u3VNYgQzuY9OtK6cV6EDBWLmH2qyFi6jNx1gHDuOkHRFiiIgz1hwY0VPwk4rtu6P/C7KKfoe2herjxITixmkJRq786jjlT/c8oK7ZlsKPRarPgeDgDTt2XFzQDm3jGgJSzW1IVBuB+lgeDmSnnQhDLSB8C15s4HZJ7tOXM/f3In1Fda2l5Dyblyp+2Glh8EqWIVtfDiV8oW5J/RRJS1oK0tKJ1GHzlq2jXYkp7Ihx0PSHsAUSS0lAtlc+XbF2AOYD+DELFd2X9fXbuwQex/wDSprmk5jIhx1HcTavcRt1jR0U8wrTFkxhmMcvj/5KjpaaG+a12Mnxnc+x9n0PpjKdNAj93C41sNKLVRLom/SYbdicqo7q87pvitraozMPW+fkG6LGz5ZIXJza7d2Vd9l7HJVBviY4iJKQrDSQ3ZPcjnbEFSCVf79COX1sBM1AUydDB5bmwaKoo2k5jsOpiU9NEBZOq/3+QbtaBrnjrp7QZT1UjyMqwgXmQYZsaqrpV24MYfloJiTtVn7x3hTsjv6yPVENPrItEN3SyursuB0F9kG2W0w2XQU/CQs0bUcdn6veEIsSyUyMfUWVcKrGAqSSJhqJIRncW+ZvrQxOTq4bmPifqir3L3HpxOOLcW9ciJ5iYJPJnOd8KXAXc9s6xqeGHaGuBzZCwIbrqyYDoVdt7oBcU05pmIASaySRctIRqJKsWN12AkxWW3EpVnXo2P07Q5tQDckhZpoJgMT49bUVbspu6mmNQQHvVwKTt4TXeAFNoHsyQsRs8ympDx0mMqk7m+uF58UcevBSn4IYwsJrVzW6qp2pmzLFN16n9RrqUek+sysurUv4GQWOB693EigRaBc93iTsrU3tNjkRqm9vMN2N+QKd+0zWO+umkqNmOCVK0GlbuGKFKsOnno1jvTa8yQCU/Roa9QuEt3pq8YoJSmtYIEKt8J0WIpgrt9M4aRYq6O03SA6dPChZidVkwO+uzi5Uu5eE3gVQRB/ffvwNt9Qfd3P/reeVM93Cf+f3ax83ld8f7r1uK0cOP7nB6/P/55Yv3x4q70ECPW8MdtkXfS6hfnfbst+/FeejMwUxudD4Plh3L19fwTQOtH8Y6Y3MG53TVuPX5sy6x43hz+8uV0z/6yimX9544HPt4dyeTXfFX8wnam+FGjLr6+fgrzNv3mYHzAFfuK0weswet2p/vDmj8BNidd8Rbebr0FdzZq+HrQABZFP0Cf47ff/A7cdt2AkJgAA -->
