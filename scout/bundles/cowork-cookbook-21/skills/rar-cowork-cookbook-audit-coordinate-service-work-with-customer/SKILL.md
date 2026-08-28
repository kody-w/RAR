---
name: "rar-cowork-cookbook-audit-coordinate-service-work-with-customer"
description: "Audits coordinate service work with customer records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_coordinate_service_work_with_customer", "rar_sha256": "3bba7e650c661f385787d70b31d3ba01628318ddf55f4b47b65af18de7fda71c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_coordinate_service_work_with_customer`. The original RAPP
agent is preserved byte-for-byte in `audit_coordinate_service_work_with_customer_agent.py` and in the RCI capsule.

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

Coordinate service work with customer Completeness Audit — Audits coordinate service work with customer records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-coordinate-service-work-with-customer
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_coordinate_service_work_with_customer_agent.py` and embedded as the fenced Python below (sha256 3bba7e650c661f38…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_coordinate_service_work_with_customer_agent.py` first:

```bash
python3 audit_coordinate_service_work_with_customer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_coordinate_service_work_with_customer_agent.py   # or on stdin
python3 audit_coordinate_service_work_with_customer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Coordinate service work with customer Completeness Audit — Audits coordinate service work with customer records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-coordinate-service-work-with-customer
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_coordinate_service_work_with_customer',
    "version": '2.0.1',
    "display_name": 'Coordinate service work with customer Completeness Audit',
    "description": 'Audits coordinate service work with customer records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-coordinate-service-work-with-customer',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-coordinate-service-work-with-customer',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cd8116ca1f4d874a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/coordinate-service-work-with-customer'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/audit-coordinate-service-work-with-customer', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditCoordinateServiceWorkWithCustomer(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditCoordinateServiceWorkWithCustomer'
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
    print(AuditCoordinateServiceWorkWithCustomer().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6abPi1pblX6FvfbBdZF4JEBLKFy+iNSMQEmhASE5HWrOE5nlw+7/3EZCZdr33qsvVHdF4uIDO2Xvtae19JH57s9omzKu3T2+KZ2ULzkqSKPSqhZW5Cyrv8yoGf/LYBv8tnDxrqshum7yq3z68uV7tVFHRRHkGthOtGzU1WJNXbpRZjbeovaqLHG/xENJHTbhw2rrJUyC98hywrF74eQV2pEXiNV7m1fVDbZEnkTM+v4+sDEiwAivK6mZRtYn30bZqz104oefE9TuA4Q3WLKB++/TzLx/eIvD+7dNvb05i1fVXWNQ3UMoTkw4g6QAR9QIExCRWFoD1xQjckYHPhVcBdCn4yvX8xevTj7WX+B8W//7vcW9VQf3Tp8/Z4vX6/Db/I7fZogm9RZNbdTPDtArLjpKoGd8XRNJbYw1sb9oqA6YuauDNLHh/7vwuKS8Wf5+v/fhU8h54zY+f33IAwZp9/fntpwVw2+e3qp3fv89Sih9/ek/y3qt+/Om7nLq1757TzMIA6vcvr88vsWDh96WR/9D6dyD1GVXb+/z2B+Pm1xP3bCfY+fZ+z6Psx6fgoso7L5sj9eNP/0rsI15JVDf/Jbk/PwWHnuUCm17Af/rwcPIvi+XLoG8y/7XaAoT1r1gCln9V92HxctS/kv3w/38QnUQgjb95/J+K+2cbln9f/PwvbfvPNnxY+J/faC+JOpAdduJ9Wvz2RTkz1M8/uN+//OGX34Ho/6MYJW8r5yHhS2plke/VzZcvP/9QP77+4Zeff2gLkGuelX5pq+Sfyfxnfn3o+ZMHX6t+/PNeoF/L4izvs8W3TF/8lhf/o/r9fXG1ksj9/n39afHHeplfy8VsxFelTxf8oWZqgPUPfvzp7XfAFIBRqtZ5XAZV/m//tjhFTpXXud8sFCdvZ7rJmij1ZvBqGNUL8O9c25UH/FpHwLGvdSD/5wjPiHN/8ev/dB68+dF58SZkzRz05Tszfnkx45d52ZeZGb98ZcZf3xcqUJFXUQCWJguZOJ8/Z1bgZc2svqi8eS8gFntsvI+Akj7ObxZRtvj1L2j58hD4Xoy/Pgg3enKWTPEzX9WAZN9nm/XQy14WOqA1eIPntEBXkjsAmB8Byv0AfFHnSQf4bvZPHUdJsnAjwO6gRYwP2cCHn2Zhv/76KyDu8HP2JNjN4tk7aggs+AZn8fEjsNBPoiBsPmeeE+aLH377/YfF/1r8Z7sewmcdZ0D5rwgBhAdFEheg4toULAPBA+EGdPKI0G+/v/wMxGSgHYF4Rn7kPTeDjI0996vTlT3xcb1FF7YHnA0cnRZ51QDWXkTN+4L3F9/wAqXzpZnXwxz0KtcrvMz1MtDJmtAC5nzzZJY3ixqkZe2PHxZt7T20/mpXjx7npaD0rebXxYk6gy6SJ+B/M8zHIrA5zyLg/m8p8fweCKl+qBfkVxHvC3HO0UVhVVYRVtZLh2894wK6x9ftQLi1yLz+czY3Tm921aNgnu4Bi4BnnFdIP84xn9syYAe3/qr7scaae5366HnV56x+FYNVeY9OD6CMi6CN3LlF/O2VUnWYt4n78B9AOkt6RcF9ReWRg9R/aZyg/jhCPDr+4nO7hlfI4v/PVDIjJzhOZjhCZegFI6qy8fToPELNnn9OXWAseCh7VM/3UeEr0Xzl289ZEoH0qMa/PVc+4vBa8+SwtgLKZUJ+yAeogDGz3EeOzjlXVXN2W5+zr8T+AYT9wWIgTKCgQcLPefZV4Xz1K9IQVO38+XuTf/lp9grIw0XR2sAzC9/zXNtyYoCqmuvsFQCQsN5cc30YOeGfrFoA6SAvgPwFADFHCZD/w3ViDswEJeZXefp9eTSPTgCF2zoALZhRvfeFDkplTpca1CeYf+Y1wAs/PEQtUg/4GED85uE6tIonmDn2L4DWzOeR1//R/69L31P7gWQGD2RartUAT/Yz67re8IzrN5SvSAGh6Zwdj01/DvbL0sUf+8/fPmcPhN+IHtR4MrfuP7hmAWorfebiTFE1oJnUe6UPyINHl35/NtpnJ/+G5dM/TPI//rVh/9E6tT/H7dMibJqi/gRBz3b3tdu9gwqBQIZEhVc/O9/H79X38VV9Hx8Ncq6+j1+r708qnh77tPhrMP8k4pXdnxard/gdni8JQPGcvq8X8Ar1kTQ+IvPVz5nsfQ83UJ+ngAfnKIyg1X5rO1+XgN4TVF4wL362oXruXj1omA/eBQH5nH1LiVe5AFrPgrln1vkfyvjRf0GAn/H71h7ApawBut15hgu8+ZyTzPBr7+1T1ibJh7fMSr2/cr6ZewHIXuCV+XgE6gjMRk3kPT4B68CFyJrf//lUJz3eWMkzy+sGwLWqB1e8quZFgh/mwTgDPDMfQuaG92wO4OhktUkzw2/GYsb7PPPM89e34ewftT7KGuhw809zdX9YzIP0h8W3mfjD4usp5XEAzFpwTPt5nsdnO8FS8Ofb2m8HVdt7++WfwHiN5/8CRDQzy8xFT3M99zttPMJXWA1gR00WAKTceYwac3utx0cb/kezgcLKK1vQT90Z8ncffIeWP/H8/jCleZ5Bf3v7Sjyv4L3mTbAcVPjHeu6oEEh0oBB8fqYkuPZ/M4m+RAHOBOMPkLWxbQvz0C3soOjK3+y22A5zMdjerNyNbcErdL3brHau62+3PmIjmI1uLR984WG+a2ErB8h75viXeYKIZnge7HsbfLV23A263m4RfIWtLdy1EMyyXHi3w2CwF7SV71tjQLkvm582zg79NhTPvnmZ/tubjSJg5R6peeL5oiD8aqEA2BDelhXqGaf7MlYV9agWJzgWGnZVtKI1ksNduKo8HvDTgXAUT0qUfcnd2MQVDtR+JM+p4pdu6xPp0rTgI8cjtaOY0k1qN1hyucjUacobqlCFLNFJqyRbkxKMakXf7FGv6DgpbsPVyN1kW4/woPGha9XYCU3kG4aZro8pvhh3XpRrCmWbJahsTd3f8p26SkyTFsz10lO2KE2sVlPapsdyqi/1NiljQUz5LVvuc3xv5rB3YxFIyhJ8Nymodxag3UlXz2J/3DsrquaOy0q12LhR3dtVrg90lh2MbSafNmNVC3HrWhqzQZCRU9oWD6B6KG6nUFxS9O2qrC755rbdulx3CCiTv+jXlMX2DNvHxYGQE07fYkLi0tdkz675raLLDjryVcahFhiOS/E6LT0O7Ve4sLoO/Ia/N6ImW7rCbDfaqbCpK8Nlp3jd9SRRFtpt8LY8fz1itj1yqhojHglyU7UvBjfSFSvk/jELlYuwWk6JUq4x3eTLQG3VZc34HMowEYvVHhfj13HSOZW9dyYBCUw4CAbVxqv9XRdWYeHpzDTH0CR3mnW8Xf0M3/eiMbaIwhUmf9iS96O3Q8qT6x7QDKn0lbGT3FMP83Yd36ZDunTM1e5Oj+yd0BO0d+79kPgxgoqYLZ2GiazKHtcpW1/dC/8AseVEq5PmXbr61lxKxiVMYwedBsSSyYtAUnyZtwY27Lf1jpmG7L6h2PBsnAaP0U+VpzhX+KoUS2Ib4LgyboyiLI6deT8zm1MPxiJqOPEOFJFC7nkOkW70oclOg5ue1LrPp9RYTlW+0TmtWfPOsLZuwXmfkVjub/qsMZaytYlLDz3jNL/0pvCOnc81HaHscS07N33YmlqMebjZcQ6q2ccaF4cu8kO0chRLjH3ues9rfEPmgiQqp1rJncvlxtYpt123YYGRl8OqOOyFYyXK3SnzXHZQFX0XFLdiEOLVncwI4WLLJneGxzAqlsNaZniGq6Nx63AUaZS3rTP2J8Rneldpt5u+qulqORZFvk1XMSYfV26eOjdFsNiCdfl0eautcyIyVXzOrxIGdVnpysnQeXK37DZEJtLqKhJbrFueV3ST2pyk7IddSnXobrj61nZccsEp7Y+qJWMVbxWH5szd7oAhlDXfEiaRLQvdR1oKrpa10lybu7FGjTJP5HhL2vBVMhgyOl5hPoO63KKlpir2gSVHBrZc1rcsvtIJoBZDqUjoZgU45WpbGKN3ZWsx/pVJQplxlk2lSyaG0Fq5K0tNkUJhSzvp2iaGG5WTYRZRHXw+B8eNcJR8kEtDXQRuhzK3zip49AJ506gU8pFkstUJ5WnYOhxJD0MlBzJxhDuItSLxmMEKF/km9MtSLOWhXw8pRlTKjbN0M5kEgbrmqnl1rhYnHAbpaIgYl2x08tBMAySk5WDLbg3V9/RasLh+qH0h6miT87bDZOpWexIrhDXsdt/tEUDd10rqHLLet9pUtR00wIQPKSld5kYhbdsxiMbG1Q1yWd9RWKar9jIsUZlf0QTC3dTa7cV4kINYQGBGvTJ0NsWQ2eOQKdyZcO8qxclSu6zbnWl5lZyg9NCez9F9sgVAXaVgHEniVHLYlUXOPYi2IBCwxF0HQ+MpZXs8T7qEmm2dlSqqr69IUIsJfRKP7iHWLLE97nI80UQd2o0RaQW5tFc8Mz8G0aSPfY7d7+HmxrPCfsgQywE0bdEGhOHJZp+67JlyzS2+W54rHNm1I6UcBedYKUx17nx5e82v52EVy75N9MUe4lsm6zoc0WpRE7qKE4wzp9goHEHdBtpFiO/eMvTqQy08YeHE7i+5BdFadlv53MEgDZiSWLG6b8PUtZg9fVxpeepebEIfxsg+WXJgb2jZI8veRIOivh2bEuNLkh02EXvjo0ti6/XFu5hMFjKRjl0yhMc17SqjKp9RA4xfJ3oyhKm2jxa3M2T8lARi6g0M4mMQfyNzOoaBvff1id3Cp61olb6eUMVuJavyeOvE6gKH3PocBNGFPdCRX1hmGB+8e7u21pJqiYHh5aUIkV7HbFlzdQvEG76WWiVN7rYZhkFkHhjdKuN+yS9t3y4o7HirBUpLdp1TebJ+OhzTc8Ub2aE6cJyBqxbGmrvrLdlDdQDTVuQei0ulb9Y1h+bIMSa0VOrtUpWB25ZT44yVXgb4xTG0XjpPBjveC00UU/lUWwLXczILuf0lKflbvXfCNI55MjxfpEYbgiRhl3Xt1MhG92yyx5d7lDywtyO9vxV1X6SCeHeSaTXhUU/yxFVd7QCFZdLmqB7RIBIjx+DupsBDiZM0wpALdIYgEZZQiuan7v1or4PNDt0mN9pkBTHasiKUj6Z73cSVoZdIQUL9uktivfSkLZcPHC/Ug0mgbWtKuHbQhnaED1eMYnCpPGV8v8+OUbfe+5WgHgkasgyiZZE8NDFGE46cRexqLpWPg1GwsabgLKOpgs1faV6pz+v1BTqqrrLBcwUOME1U1TPiCeolR2y/k2AnQNWVRtzLsLSvlX5R3PIKjgUgm7qaNNGds5y2621uMERSmRrRKme3TusakUfczjLLMrL72dgu3es6XuJJa5e9oZuoBi9X5LSbLqeduAcG4RaosjtFAJfRRn6EN4Id6H3D93hKFrFHGHVKIFGB4J0aZX56P7FavqNX1DpGXb7x9Z186ZmtiR7H7UWxKL4gNqK6xM77G944mXoeuI497/qd2hbyKdhIWtJXSszneXJMDsXhVJkWR+GM4IxynwjKlWe2EjxAHImTfKQ2JMVQgyaSrmEq/HC7rEeR48F0R2sOSatb/mYQG19Dqa5EjPXhilyIQ5X6vb/OOW1/DZSevaesrfCSrvkSTkGGC84EETVJWqBcKw0XjFXgwhQdDku4UHoNQdvBXUJdfEvOSG2F0jqm7HN3Ek49cQ3r9n7UL/lq14Pu5KA4khAHnc2yI5SgUd66VLWRKuECOxV3lTw+LbFArkYwPMF33iorSfCEsROYrHRUWDqa1zt/FYnVNFRabbZkutGG3PPXO1QxMbPnaXwHauyEFyMyYDeSQc0b8AbjnTB4d6V7XdYGWtonwSpr863fpwOzckbrwKwtm2bTyZtS5Wjsc+OCmCru+Pc68dH1hiV6/oCt96LthIVcIORG2R8jfj2aNmxOBSG4frCCy7Mr4Hl9pyhhBSNu03Wdq69bVUP76zpxNlt+H4sdNzmhy5X9rdY9hqDMUD6a+zwTwlzTE1O6cD15SLcpe8Rrv2FPE4yEtHW7tUagEmpYUTxKjlh+KCAxwO7D+lhqZYuQTNjuopCvee0Qj6Aoy/R4tNMYXh3b01JDL70k9Xpd6DqJ08pKvXly5pL5wYsZNDTMkja9iSFXCAwf16R19GJeVc4BxR392IigYYdQbVRaLepfWrocDbELA5zdM1eRJJCw9Vay1WPUnT+o7k7lrtHNixwmdx3+esHZWsXOQX5xJdoEh1vypG+uIRlRKsViqEiQa0OBBFJdxnqA0RwDEN/PoblRDnGhJbzcbLRil9xVvDEYtLGscpJI82JHpXFbZczB5RqJX13qac0UzlKmYdym3GatCUyQ8wJrKH26YbdZyorRRBZTP/HZ5iBck2htyHpIysdU8Ekv0BvlhKuDQaDXwTZXJ3gHMrM52bzJYB5dpArc30bS7Ayq3qIomgmXw3p9C3kiaM+XnHciz9e4dUGc6/Xkg6kSMdNj5sDIxhl92sPu+PI8+vtcdTOoSRx7KSaes9PhbuqNcXPLwpWPD96tN7kdIU53Q5dbDxTPaVhJqAiTxSqKtzAajSfJkIrcweJzFpYH3d1D1wDa207rpxAttUtLIFahtk8PgeO2eBGcx+0x6nXcLkKFMiBI3MaHQILGOGK6gOv9pE6lk6ikWXuuoQOruZLKteOZc3QJWvHTmgs0sbMA9ZXYaktW9mF0QwEeaxiycIhTYy63fb+DWX/FkOY9KjauAw3uTjrS0b1V7cDL3VTNfCIAHGxhHOBCWGkFOGd6yUxQq6PSaWNOSBgqNpnv9T7dr44VVKdJFvGYLF3O1H4ia/agnI36MHq4gQR7Z3MYDO4Q369V4mYa7Ikh3SKbgOCMLFlKu37bk04qnKqQmMol3XkOC6AkS1Gjd1tz1WniASJPInZFGMg8kZBnOPzp5LdtMG5zB7VFHk5CQ0ASFm7u68y/pfSg9L4wXEm3kTZwQmtrqbk4GwWa9G7oMP3MUiwHjoOoeaFPgezn/Xq5pGJ032JnVEqDEF0mBpaX4+kWp5cqHmKxMtfXBPGOza3djWCKZAzX8Sapu0/rJMZ7VaaMfd06t0AW8CDF9EA/bTQ+Mka5rMjxsPUCcdhCqBwazL3tB1yS3ZFDC35vwgdTIWzEQoUJyabwetpchtyAHIxITlEuu/A1FDumdS4Sj8dtcuuTU67LywouoMrrtB1EO+eLX9IxU4oGN6kFfogmhIiGIi0gDaFYYkD1y8oZoL1Dj5GXGdrtjic71uxTcPAaKlFs7u562AymXYsZi6p30NozhxvXt9vRbG6Xi3+N4Sq4dTA1COtQl0FBoVEX453X3rgNEu2Z1O3B7B5JZFpnxFoTaf++ZN19gFCgz29wy2CMMtqZEeYH1ETotLGV1toaHIwP1eZct43VVLKRLAUyN9BguoCJ3MHl9U6/Y9GWROkgzrbVxYMMHclCQlbOiNbA5lbixlN2QMk16ZRROUCKPlxvEZ6b9pIQnXazvpI1c753V6gAku/Z1bftzSo7QwUhd0i4WS29vcp7GtVFdV/xd7FDoSU3YOoZZ0vLutMYVHvSOgQHtUru8CUBdiLxXhSwfWpM5jLd8Mi0j+iOYvcBnSXCtCamakPhh3tWXXmdh7dm6YpFJWXnVTHeL2B+VGIhwpfQmSUv5SWtbesoTWZ3dpq1uLcmq+S2+aERtfycK7KaGPLmUlpsczboZU7Bhz7vrSTeFghfF9kaxx0vm2zVRVG7UDe7O2skFBh2q7bAJ7ZUbkbvcWq+VKzsTLTz3UpyR1GjTIGwBcp03gslK29VbCtq6ik3EUw5EJqv4I1XaE7R2WwpKZWgr0vn6pMraVU0gb3D7F5HBBE/9j5aW9OeOYRtiyy1cKI2fhWzdIeeqmbNjOTJ30mRC1vqqG9kO7kNl2OZQYN6tBsHgw2DQTZ7O7ByEXYEtsEDI5ULhjkSaocPRLbmIzbZxzfJkow9b543+7PuhDTaplAj2Ybi3s8ITatRpwC2Iwji728f3uZ7rK8b3f+dx9vzjcP/Z/cvn7cavz4Ee9xw9iz300PXp/8Wul8+vFVOBLA979zWSRu8bm7+h/u2H//Cc5RZ0Ph8jjw/wRuarw8MGiuYfyP1Bs7hYGk1fqnzpH3cRP7wZrf1/DuNev4pjwP+vj1MTYv57vlD9yz1ZVGTf3n9tuRt/hHF/FTKcyMA6vUxeN3R/vDmjiB2kVN/2aDbL15VzAa/HssAO9fv8Pvq7ff/DRvP/+qCJgAA -->
