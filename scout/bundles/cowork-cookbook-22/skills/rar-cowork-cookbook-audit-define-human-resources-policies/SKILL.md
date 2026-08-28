---
name: "rar-cowork-cookbook-audit-define-human-resources-policies"
description: "Audits define human resources policies records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_human_resources_policies", "rar_sha256": "45fcf0e19dfc8bce49b61042c7c994aae39a0212a9c3340497ea105e5f1d018e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_define_human_resources_policies`. The original RAPP
agent is preserved byte-for-byte in `audit_define_human_resources_policies_agent.py` and in the RCI capsule.

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

Define human resources policies Completeness Audit — Audits define human resources policies records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-human-resources-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_human_resources_policies_agent.py` and embedded as the fenced Python below (sha256 45fcf0e19dfc8bce…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_human_resources_policies_agent.py` first:

```bash
python3 audit_define_human_resources_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_define_human_resources_policies_agent.py   # or on stdin
python3 audit_define_human_resources_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define human resources policies Completeness Audit — Audits define human resources policies records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-human-resources-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_define_human_resources_policies',
    "version": '2.0.1',
    "display_name": 'Define human resources policies Completeness Audit',
    "description": 'Audits define human resources policies records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-define-human-resources-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-define-human-resources-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c56ca562d432f324',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/define-human-resources-policies'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-define-human-resources-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditDefineHumanResourcesPolicies(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDefineHumanResourcesPolicies'
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
    print(AuditDefineHumanResourcesPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/71a+ZOj1nb+V5TODx5HM80uYF69qqCFRSABWtg8rhl2EPsmQI7/91wkdY+dZyfPqVQ0S0vi3nO+s33nXOhfXuyujYr65fPL0bfzGWenaRz59czOvdmq6Is6AT+KxAH/Zm6Rt3XsdG1RNy8fXzy/ceu4bOMiB9uZzovbZub5QZz7s6jLgLTab4qudv1mVhZp7MbgTe27Re01s6CogbysTP3Wz/2muSu8rxof38d27vozO7TjvGlndZf6nxy78b2ZG/lu0rwCAP5gTwKal88//fzxJQbvXz7/8uKmdtO8AVrf4fATmsMbGOWJBUhI7TwES8sR+CAHn0u/BsAy8BWwY/b89KHx0+Dj7N/+LentOmx+/Pwlnz1fX16mP4cun7WRP2sLu2knhHZpO3Eat+PrjEl7e5zMbrs6B1bOGuDCPHx97PwuqShnf5+ufXgoeQ399sOXlwJAsCcHf3n5cQY89uWl7qb3r5OU8sOPr2nR+/WHH7/LaTrn4rvtJAygfv36/PwUCxZ+XxoHd61/B1IfoXT8Ly+/MW56PXBPdoKdL6+XIs4/PASXdXH18ylIH378M7H3UKVx0/5Tcn96CI582wM2PYH/+PHu5J9n86dB7zL/XG0JwvpXLAHL39R9nD0d9Wey7/7/L6JTkGLNu8f/UNwfbZj/ffbTn9r23234OAu+vKz9NL6C7HBS//Psl69HZbP66Qfv+5c//PwrEP0/ijnea2KS8BXUSBz4Tfv1608/PErlh59/+qErQa75dva1q9M/kvlHfr3r+Z0Hn6s+/H4v0H/Ok7zo89l7ps9+Kcp/qX99nWl2Gnvfv28+z35bL9NrPpuMeFP6cMFvaqYBWH/jxx9ffgUkAcik7tz7ZVDl//qvs13s1kVTBO3s6BbdxDR5G2f+BP4Uxc0M/J1qu/aBX5sYOPa5DuT/FOEJcRHMvv27eyfLT+6TLCF7op+vDzr8eqfDr+90+PWNDr+9zk5AeFHHYZzb6ezAKMqX3A79vJ0Ul2CHX18BpThj638CZPRpejOL89m3f0r+17uo13L8dufX+MFTh5UwcVQDOPV1slOP/PxplQtY2x98twNa0sIFkIIYMOzHO5WnV8Bxk0+aJE7TmRcDMge9YLzLBn77PAn79u0b4OnoS/4gVWz2aBINBBa8w5l9+gRsC9I4jNovue9GxeyHX379YfYfs/9u1134pEMBDP+MCkC4Pcr7GaiyLgPLQMBAiAGF3KPyy69PDwMxOehqIIZxMLWhaTPI0sT33tx95JlPKLGYOT5wM3BxVhZ1C5h6FrevMyGYveMFSqdLE5dHBWhNnl/6uefnoHG1kQ3MefdkXrSzBqRiE4wfZ13j37V+c+p7S/MzUO52+222WymgcxQp+G+CeV8ENhd5DNz/ngyP74GQ+odmtnwT8TrbT3k5K+3aLqPafuoI7EdcQMd42w6E27Pc77/kU5/0J1fdi+ThHrAIeMZ9hvTTFPOpC4Ok8po33fc19tTfTvc+V3/Jm2cB2LV/b+wAyjgLu9ib2sLfninVREWXenf/AaSTpGcUvGdU7jm4/h/mhtVvZ4V7a5996VAYwWf/34PHhJbhuMOGY06b9WyzPx3Mhxen+Wjy9mOkAu3/ruxeMd9HgjdCeePVL3kag5Sox789Vt59/1zz4KquBsoPzOEuH6ACXpzk3vNyyrO6nuyzv+RvBP4RhPrOViA0oIhBkk+59aZwuvqGNAKVOn3+3syffpq8AnJvVnYO8Mws8H3Psd0EoKqn2nq6HiSpP9VZH8Vu9DurZkA6yAUgfwZATPEBJH933b4AZoKyCuoi+748ngIEUHidC9CCAdR/nemgPKYUaUBNgjlnWgO88MNd1CzzgY8BxHcPN5FdPsBMM+sToD3xduz3v/X/89L3dL4jmcADmbZnt8CT/cSxnj884vqO8hkpIDSbsuO+6ffBflo6+22f+duX/I7wndZBXadTi/6Na2agnrJHLk601ABqyfxn+oA8uCfz66OhPjr2O5bP/zCmf/hrk/y9RZ5/H7fPs6hty+YzBD3a2ltXewUVAoEMiUu/eXS4T4+6+3Svu0/vdffpre5+J/zhq8+zvwbwdyKeef15hrzCr/B0SYpdf0rc5wv4Y/VpaX7Cp6tfwNT/PdBAfZEB1pv8P4KW+t5k3paAThPWfjgtfjSdZupVPWiPd5YFofiSvyfDs1AAiefh1CGb4jcFfO+2ILQPd7w3A3Apb4Fub5rSQn86xKQT/MZ/+Zx3afrxJbcz/588vEykD1IWOGQ69oDiAYNPO12aDkEgIwHL2tP735/T5PsbO32kdtMCpHZ9J4hnqTyZ7+M09eaAXKYTxtTZHl0AhNvu0nZC3o7lBPVxoJmGq/fJ6x+13msZ6PCKz1NJf5xNU/LH2fvA+3H2dgS5H+zyDpzBfpqG7clOsBT8eF/7fvR0/Jef/wDGc/b+ExDxRCcTAT3M9b3vXHGPXGm3gBLPBwlAKtz7TDH10Wa899t/NBsorP2qA43TmyB/98F3aMUDz693U9rHAfOXlze2eQbvOUyC5aCsPzVT64RAjgOF4PMjG8G1/92Y+RQCKBJMOEAKTgRuAPsI7QUu5bg+TjsLBMZRl3RpGrdtH6NtGEVQm3YxDIdxmvRtBCZ8IkA8GKF8IO+h4us0JMQTMB8OwC4EdT1sgRIETiMk2O7ZOGnbHkxRJEwGHugi37cmgGGf1j6sm1z5PvFOXnka/cuLs8DBSh5vBObxWkG0ZpOG5Owjh64XAdNc6KQdRK2MKChVNNlwvf2OljPuGHinJtCaJbPVzbBMQkOQ2UqxoEINXGE+WgTJaExSuqe9l3t5liROrDKd1JF85/uruNoWNBu3nshvujYX1ChKR8pOxqKqbrxeUT7XYOyRqFI9qpd6frKtmgq665UEKLITVq/NSjoj2WAXsNAhYpIYmZVhnjuiksakxNbQQFA429igBlyVu5LrNKNt8f26pKnuFEM7MEdDCo9fb9aIN4EJsWPtrPBwd7BH0fJT2DF0elEZWVOf03xbumTJOaSW7Ydze7FEJ7EJIyrLtoDcYWvImhWvVmfE3vcmaRCD3/BxUTKjhBjnJm9N1WF671QQ4NCKHNsSF0QNr00M7JKGXU1yC6m9tvb6VHSWhZ48qj6ThL48QDZqhs2ukW5WmF3irXZENTFDaGa7uQior/EruNNETByQrlt4B3g1ota2YVRDkObanrF2tIhxczypmpOUWyfPSdhuDPbHHDZW3cW88mu9lLTV2OliTF9tZiErqLU0q32Iorcz19qd5Z9h0YWRajQjytH0PYI6MLSr5f1V4NquX1XqLdqlOyTfwgzRGJlRX6B9VBEIvA4PnbjUyJO3wKF8sRQEPVguFOcQr/WThh4udI7642i4XS3z1dawut1a8gy2HZzaFZdUS61bXsr6bGCuc3RVjIe+7lUXEqm82kLU6bDCtSLAhXYv3vhN4Z3GPcJJRLfYK6a5q6GrjxYdkmseGqRNepVWiDiXErW5DYLcpVtke6y5ciSZ0qJj+OYsy1FadQ7nZ50RQrRTHAPmpgxuMIRQuDzU5KGyBZM26DAmlTK90bJCGeFiI7WY0LUjjjZ7L6VFwnJMTb5UdC335WFjpLDlnfXTBrKPFzDdq1G+RrcHd8eV637lbbrSYVNHOM1F+1RiqktV4W25HDyWO7eSYItc2uZcJ3b4LhTQtSUm5So6HrfyIKPCOmItE2T2Id8dOC3VzoiVR9Ge39w8fxSw1UIJJYIYSkogb0dZoJJ6ySeteTkGawHdXIc2PizXKL+/UMrttG+qlG4SUpHmzH4Qzw0pBmUA7UeV32s3M1GdK4tFUXBErxJrBZdww6/P2zCjw9GZR2ccT0xp6OqjA29iQbvpfMVdiK4qE+iInuUdQldFuSKjy1AFCyHpRJkFnMLe8KDRVBDmm2P14YZoqSbP89EQNRksGAMWEq9HR06Z/KSDeZ2CkyvTVo4Rq9RezxYOk9zWy4ql7AU4NGjOmLkjYnvIWQxZX2XnEUEzOov1PYrYOZhnIgU6M5RDtWuJJ9H2qGz3ezGCopQIpb5PTRaFnDoLgk6g+tLCC60VmLZExBaxSp9Cuc3CsuhVuz8SCZk23hY/BJzF1fPatHqc3xAHLPNPLjaaaA6wXqy6GdobdeAC+SwhDddBympMhnhbrHdDd4KpA1ZwEXZ2lop5VQDfO7Sgh7Qo8/OLR0nXEOrg80YeOr4rtz2Dnop6eQznuw0+0psioJKMY8I+TwaFN09mqAlwRBVbxKESEe9OzYm/EQXFZPmOKDODhwPlClvujRLZQ1l3p1PTxJhLqZ7OHrcNLg4Zgx4JDWIu7BrVzbHh1UuYLI96vD+rF8lukQxmvXl/2TAXNWWd88W1BOZG6FraxbJLjn21WZfLcONafBpXS7HlfHZJud4aIZZHaZ/ckJxBCI2v6dS6kfLN0vDOwk46IDzlRi2C6ynME3t5KL0zvoBMKIGL0b5mmbSr93mhrpOzzueFQVDHRhKkay1LprIhhiHHAI801DwgInre5Gvk6CoKpC/xyGMljxzHi4tE/UFd5XbiCSZqULkrhlvpqtVlu0uW7nVPWzs4XWSN0DEH++aeby6r75xtZefbSiUiZGC9rQqTKph0PAY/ZlGz2WPMtd6knNYOiGqu9mPunXIEl8jiJIJU09eyxMjtuGsrvUqOrL4QzUFsHDTACF9eYedySIXDarclsEXRBxXpaltq7Da1YelUuriZZCNCKo+rq5XEDFmN6T5Msd0wppTGkZyxuWy4tWVRea5gC7XyFqaA1CPFn7usRwcrW9+WVpSL5x2GxOlh3kL8ddsJnnA5lfS5ned4z5bC4O3FgysfZEngwuYGWqFm+iFkrrYKGanrYzU2prvI0mo14psqruZwE5zhg60S+XUrFdSo49xmlTAp4rRZKKk7UmLCVb2tyLjwoX2vOvg67daIWp/0jaIGJqesjNg8LLeUdkqaOD+2ls/LK/oQrSovRLl5JfPMuelXpZVt2TFntkQNKOKGXW5BvavcdisJJw6LtsYe3VIyuRht/QhvfLE8nQqluXhQc9uNCwYqGtGJmmNqI/OVjjWDFZQ6TB9GTb2aV9rQqnO8IzIc5hK+yPfuGPH1iOkbT83mFdye4iNWwseE5lYNqyH+FhRmTKhRQGhqEionl8NUTXIL0pSsGBMFlWHhLO5N/0js4ipgznxhl4reqnOsQVPlpqZllIUEdFKgjJHo0SexfAO7DXtKccY3q0OL3vJiWyJbR5OXt7jOi8N8ruRYyWEUl6i3vdKo3oKPaBe/hAtepxKYcDp6iBeHwLAc28Oamxnj+Wk0Lg551Wkmh69meGwWdN5FCaNCG4FdLTuYaAdOX+juWrH5cVecR2Q94Ck/4tec4IwzaqIpg6tC0+kLd9dqg2e65nFXtInr7+JMryqvFImrES/0vZH2XYTFa2ihLtZnwhUtTOXmWdRzF+FQnkTEJw+jdRjOCYsIMoIyTSoMxHZMZA1X0q1g+qaEhtwqKltintrNGTdpuOHWEsJtZV3YpZi1UP12JWe5tg5OMelvzkIvGBQrc7nBzddxeNyL/Vaxr4sGU8rkSvFdwJ9Ydrz21k6BB+eMJBuFiT3EyMKQQP1hCS0TTS61EwODmTM3qbXvxOKwS0ZnIMeksuwTk2fGRr8Jtk3C+EKfJ9gGvdXrQ9gQDSGmoy17476m0nrE3VKMjMU64Gy777hWYstrknB4OOdRZ57Xxekw4n3DeY3TafyaxzAWE3nZYK9LPznn6xRR5n1jY94gRxoVQpYS7r35rpfI5Iweh8iknd2+aQ13WW4Jr4lPhsdecpPYQp0jyHhfMZE8KK6BwX2hl82+VMXjqJPRCCO7SLUH1T73R8JyzV06N5RFcy3EOXlVC/Iqo1QMGlKdGh7k03uyrHU6yVDxOhbm/CShHNY60IVCrX531P1NcOtVwagutZQmjVihJa3u8iEhPXS9nceKd/X8w+ZcBla9svoozI/j5kCtk74KjnMuEfjcby29otXktMHrkYnV6BDJQuJpogWl21o08Sra0Rt0eYvkkCssTd/il8NAGkeLp3fa0Su3cI9VJ2p/kFZLhNd6EWZtTr4QsoD1y5jdl67VbU41XRdFehXPssCMSSadql5xi9SSSC7WIOnKsz1hE3DA5esBHnOpOMkVdyvYg4AIO3ZEKZdhQpzSCRc77/rFbuR4kNVmIIMR1NE217jYQy1b7NiwR7Nz7/pGp2sgXnG9vFTcMY8MDyPLTX6KDMQYEIdf4V1q0NGV06U017jF0VwMRacWBedbkYzkAjwI3Oo06EkjzevVpV5nPRE0Je6c1xgS1WOPipoWZhbvqju1CCXHYuMhxETTkTN7zxOr0sM00yFx1/MEY5CHKxNTVJ3l6dknjx0mOcOBZfsNw260YyVOU+AKcTQwRINuZCx6T1J0D27xdjHfk/ShU7DUGRyspYT9bdd6Qg75/BLRaozu5qNChmbdDV6pwrrX2NxiiNCNTnJ0TLBovqlG/nTQJfFUUPl8zR7IiAtasjgscB4mye5GGb1zU5eqe0HBDBZflcKGLcphD1pDlnuX29jr6xyjzUsvjddDPPiMC/k1hntnLjJcZlFTqCvCwsYjexwfECi1jMFDhrLgGN1LDWAvh/eQH+Jkpgsrupyny7kSbJV+js4hPKZNA19oSA7RR+jW4gKLZVUwR25egXM9z+LRwVg0La1HfGJRkh1dyqLb+mIueDxGr/DzeAEjcJgo1cZod57sb4YyopfEmiP2eCWb0Db3jJOr4xaFb42bcvAv2uWYuaJ86d2dD4uotlzeSBfL9zJVDMF2H4Mjxlk/g8SEy2EcTrRbrG8xKNCUO0Gx4JB1JfbxioVc093hnIYZpkGVLuZIYM5jhi0lxLgRLW7Xfb7GLVthAy7sstwahbQISK2T6dZjC2iBQTnPxzue6XmAc5kJQn7taela+FxIgqhftoXoX1tX5lZdrvVDIlLkDmkDf8RbuiBLolc1H6uiG7/2b8GwwEY4MLdFhddzSaPQMFIi0ajgWNCJUcjPp3269AdOQtJ5oKjXDZgIQKs/0RCLl1bRbP3aVA+UOc+WbkQSZ26FrrnwxGOufBL0jVFRxJG8tbJyZXx7faxtKT+wNlVt5SALXYW/LHY4HdGFLI7LzdnZyw6sCzUojZVekVTb++JyXbRRJa3nmKmKg54K1vVGjfMQLvXmEMRYNu8qmRxJVm3HDGuIcksZ7o2LhwVjpXOszC+32GJlXtuO63nttrGCDHxgXV26tfcdPvIbOShofbUi0V3vXfoeaVfLgOgP64PdFbXinXoJ5zLD97MBs1Q+LRpuLBAEw2Ky2MsDDXI1QzU4pytM2IGzhMLt8K7rWf8C0nLXr5nN2aCXwFOJPJdvmzhUhCEodJ8UQ83Ne6qLvQOdYEi6X8T+Uuq8OmKV1Qr2FhDvKivaCuCApcCJykMNraNdFsNxgXEG3CKv0oBUfMvVAo+zA+81EGgA7n6/q4lsG5I5Js+JBXngbnBNBsUNImRiiYsyRXYCZsAZNY/YPib76LRhEPwYIxcf5vOgZ8edWKMbW07t+YJLgnagLD+yjyuTFY9zKSdxXCOWpbLoXdMkvZ23yFpI1azmtqJhdn5thUWIrmNJsol+4607DGeUas0fdcFFS1Nu1TARU9XpZWKt6GhGojB2Tgtia1UqG64KqCspPq+WvNXPlTjsJDPDVsF1x+8YiV+xFH+MpNOK349yRYUBYqXCDZzAeMsCuUIYrbkX10lLinq48IkD7FrDmcZStCCLFeRTjeiyGXUGg73sWVS8gTvD9aXAipzrvltJEn0Rb1BkM7E8GNpysd9ytRS2IBetjVhCYzrk3dxDlWblOpe85zkGk7W6IZlzOp3CzszFXKieSC1d7xyBE2WJcQok4N11viJuoSx6SOf54nGBXWBn0cL+7ZKJKsO8fHyZ7qo+72r/tWfW063C/7M7lo+bi29Pue43l33b+3zX9fkv4vr540vtxgDV4/5sk3bh80bmf7k7++mfekQyiRgfD4Snx3JD+/YsoLXD6XebXuLc65q2Hr82RdrdbxJ/fHG6Zvoli2b6PRwg7P48oC6ycro7ftcKfkZx7X9tC2BLC969TL/9MD1m8r3Ybt8+hs+71R9fvBFEKXabr9iC+OrX5WTm82kLsA59hV+Rl1//E+pB2i8wJgAA -->
