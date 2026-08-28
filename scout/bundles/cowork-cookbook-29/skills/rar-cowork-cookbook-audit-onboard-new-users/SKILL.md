---
name: "rar-cowork-cookbook-audit-onboard-new-users"
description: "Audits onboard new users records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_onboard_new_users", "rar_sha256": "411f42fd0fa1a4da7a1eb620a09cd9bfcd6559cb27827ad2566660273b17a9ff", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_onboard_new_users`. The original RAPP
agent is preserved byte-for-byte in `audit_onboard_new_users_agent.py` and in the RCI capsule.

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

Onboard new users Completeness Audit — Audits onboard new users records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-onboard-new-users
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_onboard_new_users_agent.py` and embedded as the fenced Python below (sha256 411f42fd0fa1a4da…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_onboard_new_users_agent.py` first:

```bash
python3 audit_onboard_new_users_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_onboard_new_users_agent.py   # or on stdin
python3 audit_onboard_new_users_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Onboard new users Completeness Audit — Audits onboard new users records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-onboard-new-users
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_onboard_new_users',
    "version": '2.0.0',
    "display_name": 'Onboard new users Completeness Audit',
    "description": 'Audits onboard new users records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-onboard-new-users',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-onboard-new-users',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '910d3d8f3015fc9f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-04', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/onboard-new-users'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-onboard-new-users', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditOnboardNewUsers(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditOnboardNewUsers'
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
    print(AuditOnboardNewUsers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/7V6adPiSJLmX2Hf+VBVo8wESejKtjZb0AHoRBISgsqyLN33fSBRW/99Q0C+WTXdNT1ttkseIBTh4f64++MeIX57s/suKpu3z2+6bxeLnZ1lceQ3C7vwFnR5K5sUvJWpA/4t3LLomtjpu7Jp3z68eX7rNnHVxWUBpm96L+7aRVk4pd14i8K/LfrWb9pF47tl47WLoGyAhLzK/M4v/LZ9LFGVWexOz+9ju3D9hR3acdF2i6bP/I+O3frewo18N20/gSX90Z4FtG+ff/7lw1sMPr99/u3Nzey2/aaC8lRA9m/GvDyYlNlFCO5WEzC0ANeV3wBdcvCV5weL19WPrZ8FHxb/+Z/pzW7C9qfPX4rF6/Xlbf6j9cWii/xFV9ptNytlV7YTZ3E3fVpssps9zZZ2fVMAwxYtwKkIPz1nfpdUVou/z/d+fC7yKfS7H7+8lUAFe0bxy9tPCwDSl7emnz9/mqVUP/70KStvfvPjT9/ltL2T+G43CwNaf/r6un6JBQO/D42Dx6p/B1Kf/nL8L29/MG5+PfWe7QQz3z4lZVz8+BRcNeXgF7Nffvzpr8Q+vJPFbfc/kvvzU3Dk2x6w6aX4Tx8eIP+ygF4Gvcv862Ur4NZ/xxIw/NtyHxYvoP5K9gP//yI6i0HQviP+T8X9swnQ3xc//6Vt/92ED4vgyxvjZ/EAosPJ/M+L377qR5b++Qfv+5c//PI7EP0vxehl37gPCV9zu4gDv+2+fv35h/bx9Q+//PxDX4FY8+38a99k/0zmP8P1sc6fEHyN+vHPc8H6RpEW5a1YvEf64rey+l/N758Wpp3F3vfv28+LP+bL/IIWsxHfFn1C8IecaYGuf8Dxp7ffAS8A/mh693EbZPl//MdCit2mbMugW+hu2c/kUnRx7s/Kn6K4XYC/c243PsC1jQGwr3Eg/mcPzxqXweLX/+0+GPGj+2LEpT0zztcX530FnPf1wXm/flqcgLiyicO4sLOFtjkevxR26BfdvFTV+GDUAEjEmTr/I6Cfj/OHRVwsfv0LiV8fkz9V068P2oyfXKTRh5mHWkCVn2ZbzpFfvDR3AZn7o+/2QG5WukCJIAbE+QHY2JbZAHhstrtN4yxbeDHgaEDq00M2wObzLOzXX38F9Bt9KZ7EiS6ebN8uwYB3dRYfPwJrgiwOo+5L4btRufjht99/WPyfxX836yF8XuMIiPuFPNCQ1xV5ATKpz8Ew4BTgRkATD+R/+/2FKRBTgPIE/BQHsf+cDCIx9b1vAOv7zUcEwxeOD4AFoOZV2XSAjRdx92lxCBbv+oJF51szX0clqDieX/mF5xegHnWRDcx5R7Iou0ULwq0Npg9zVXus+qvTPCqVn4OUtrtfFxJ9BNWhzMB/s5qPQWByWcQA/nf3P7+fnfpDu9h+E/FpIc+xt6jsxq6ixn6tEdhPv4Cq8G06EG7P1fVLMZc/f4bqkQhPeMAggIz7cunH2edzcQVZ77Xf1n6MsecadnrUsuZL0b6C3G78R70GqkyLsI+9mfr/9gqpNir7zHvgBzSdJb284L288ohB5R8aAPqPRf9RoxdfemQFrxf//3uGWaPNbqexu82JZRasfNIuT6TmZmZG9Nn/gDL+WOyRFd9L+zdi+MaPX4osBm5vpr89Rz7wfY15ck7fgMW1jfaQD7QCSM1yH7E3x1LTzFFrfym+EfEH4M4H6wD4QaKCQJ7j59uC891vmkYgG+fr70X5hdOMCoivRdU7AJlF4PueY7sp0KqZ8+cFNghEf86lWxS70Z+sWgDpwN9APnDF4uGRW/GATi6BmSB1gqbMvw+PZwcBLbzeBdqCbtH/tDiDFJjDoAV5B/qVeQxA4YeHqEXuA4yBiu8It5FdPZWZG8yXgvbMvzGIgT/g/7r1PWQfmszKA5m2Z3cAydvMnJ4/Pv36ruXLU0BoPkfHY9Kfnf2ydPHHevG3L8VDw3eyBrmbzaX2D9AsQM7kz1icqacF9JH7r/ABcfCoqp+ehfFZed91+fwPPfWP/17b/Sh1xp/99nkRdV3Vfl4un+XpW3X6BDJkCSIkrvz2Wak+vjLtI8i0j49M+5O4JzqfF/+eSn8S8Yrkzwv40+rTar4lxq4/h+rrBRCgP24vH9fz3S+F5n93LVi+zAGXzYhPoDS+l45vQ0D9CBs/nAc/S0k7V6AbKHoP7gTgfyne3f9KDUDNRTjXvbb8Q8o+aihw5tNX7xQPbhUdWNub+6vQn3cc2ax+6799Lvos+/BW2Ln/1zuNmb1BXM4XYFsCMgR0KV3sP66ALeBGbM+f/7xzUh4f7OwZv20HlJvZcK4iz3x40duHuUUtAIPM24G5RD3pHGxi7D7rZmW7qZq1e+4+5k7ovU36x1UfCQvW8MrPc95+WMwt7YfFe3f6YfFtv/DYeBU92DD9PHfGs51gKHh7H/u+GXT8t1/+iRqvRvkvlIhnzphZ5mmu730nhIezKrsDvGdoIlCpdB/NwVwQ2+lROP/RbLBg49c9qIDerPJ3DL6rVj71+f1hSvfcDf729o1SXs57dX5gOMjdj+1cA5cgrMGC4PoZgODe/7QnfE0DzAeaEzBvDcPBGgm8VWDD9tqzCRv2HRxZ2SvK9SgncD0cwyjXQQgSIWwPTAKvFUKgDkzYVBAAec/o/TrX93hWBbFtl3QJeO1RhI27PrpyUNeHEdgjUH+FUWhAkv4aoPI+NQXE+bLvac8M3nt7OuPwMvO3Nwdfg5H7dXvYPF/0kjJtHCEcLXKgBvcvWICrKFsb6d3hzCwd8Cbq5ZR2timOaz4roDSLpbGd64cro3WsvR1KNXAP0GQRxf24qZVzjiIjKaNck9/5GwZDlCtIy7vWQflFt8WzoNX8VCd0LPVtjvg1J2RTFI1We8Y5cUlS4pG6shrSipRqmA6r1dOkpievvQuydl1nStc4GFznqcZPomXWesYZ8bXmVnV00batiWrRUmaqJTScarIvsJpsh9G37ibsLiFFNLWeu9FlnaXcGZvUyiOGvHZrRY53aq9iqCotR/NSKGZO8KqbdILHJYfLsLw42b3SZNNphZ0w1c3mbgaFubr5opDTk9/oHEkJLL0WGp1hbLo7DaaQF5uyQlMelHkjnuyDU9D4HUsAvwSFq4tKNCyl2Mc7neuaOmbU6TZIdcSJrF6n60xmZX8jcDl/dq91qiNG08pJY1OKqpXcvY1PV+kgh3o/qrWPYduhUDszPSPOyWukcOgTvD0EO8worfu4NGwdzqRErcxUoUqGdD1J391Mb9sfd+3ZTtxbx8PZeMNH3thPzSU4K3eA3a699NdD1uQbK965WiqyLYak+8K27/751CIoU5xChT4Hh/2ROqANtj2mwlltBXlF7hOucNMVfu3aIlbHCM4uQZmdODip/LKTnMPduZpJNoQecq/L0PBoh9WXxEUShc2KUEIOzhAWOiwlK6+udO2vw1ImTnturV0mD98zdXsT3Jtgo0uj6zTaadu7fEnwI7Rj0vuQH6JTQap+INxpg4PdOwdvbqPsKxc8E+5xlh9Q8qpma/GOlOZ6zS/xCk6wc+oLgyxS4VK12sld3hmCW/eR0KkOB3vZOavK1aAFkVXF5WqfVdhwPqsCYUVmc8JKprsMI8lAASfF66y6kHZJtGrMXCZLb+/RycBTo4jTDdLFZ8aWJVi4OLSRNSEOxzQa9Sl5kC8lrdQXZsOPfI7t+YNWhDTv4DrCmmRIFneWcFdJe/JhXGhcoYakoWGyvDshLaPyRXjbILQc7i5ooNgXSDnGJwp2qcQJeJYoFZuoye2qB7u1qlp5R2ptC6uhazHWW64RD2+OGcp37rHCE5HuL3JEXUQhPSTFzrizioAr/KAyBxZi0aN73DsmofNICocbkDB1YB84m5HCfio4hOcKTSABW6NBRiSGuT92GAPfy+mm+8FRrYz0AllJ3R4gyru2uo8pOWipO8pI+00tiGaMnDl98A5107kiZTt6dBK2egfpnjTsTmJKB4KhSSFLUcQ6hLGKae/1tOxxrLFIUxzrG0Wel5Z+OVxC2AKUIu/XwZFD0y02VNcpK9aS60qHdqMh68NZrXWrv5SItN8zjmSft+e8YlftvdmrOjsmu1QgVpap3dQDh+0m60xf63AMZEuzzzlxbbw9Etm7kIyv1rRuUAcKfdJFzNSkzzDJTFeEoSycNka9Af3T0dhilDTtm2W5WW7xDGl32+24ctfsit/Y9ZjXcURJEW4wg196gCnY2yUNb3BTuMymMy68AF0Q3CZDmnKtQ1gcb5F7K1nneuKIiQmO1pC5K0/DMksaRnZA6GV4xqu1dCrXdkmF8X5YM54QnuSrolUqDKg877co1O7d9QpyLL53roCPJYgu+x3MgvWNA5f5JiGkU9uUFrcxN9VaiKqCBlHp7Q901cvK/eqEq9Bs65UU7oDHdhW0co7ZkZ0ml8Wne0NBXrHHloqRpcYpSsdUPgfBcgefY8Ot0PO16pgpdEnd0P2MGCiYdC6y6Y3ElhLozREK7ls7GPmlGJg8DgKvRuI7HCiGd4uaFXc+Dnl/5d0Nm+6OnCiGWNxfd6y5rjm32Zsm32vkwLTsPXXjY+dK0eDt/AjIOWK9t+69E9LsOj3he3XLryblclBc1LFJ2ttY22Irhuf7Dez5J1HUEyU3ZYaG7Lt0Tc6ueO8I4Ty4w2jsTptdLhHH/a245Id7eQ9XgZIcyloIiyIad/iVVU7XmwFDJWkV2j2B24q6x3vjWrN5UchXZ0gOxpXoNfWqSjJ97T2OV1PRS2LlIlC9opyhg+SpeluDKjsJ5pmxDLpBoL3R91czx1b7ejNuNwmO6W5xSSwKGpYO6JzU1eFkIZDOUNwlLCsx1PbFBEKJmUq9ahHJQ02/JA+eZ+A8m2tNUhhpZWhZ1PJHkGOiQa5jiEe6E4UZdReezuxtq1hmTiOcujlQCq3R0rkL3QgjvVBN6h3a7slKyUFzEbUrmVoPIAhScTzR+qSDGgta3uGObRG3QkKrGK+3vL7msp/duYlMNlsO7U6wgRNLBEGmSMDVmDPdNR2NxzqYOn+1Vydrm4x6JMobKpXOHph3DC3yXsMmgwmCrBO1PDSRAaXOCc5Hk67icO2dJ522JPQcrjYdyxWIufFsc1WRa9WvukLTc38lyHc/4XVSgEhOhsJx1Rp9Sw9Sy9RXcxeayFaAI6YLjTOjO5wd6/RmhctQEcVms9uE2JGrQogtCJPANbgjkZKLc3TtiYkTBpSDBLWiedf1BJyk8V69Si5yvxIaw2QK4bwzOuq4Wt5hCBur1ciz9p0p+L2SORYqsZgfoU0nK+eoaN2lf8jjpX9Hr1O342KfrgMnJDCz3EFcgjOK32EIdBA3O3raIAINY4lzEXZm1TIwW7DGOhruRbIWLHFaDzVLXqcbz51vMN9VfX4RDbgPDXmr0P7Uni9G7qdC4AlNH3DtRHVZinN+6B7KbcpqE5QZPklvz9LWNiKOk1BjkPe8ed5r4aDRqJIaml5nWonxSH9cq1JCxFtltVVBlgVWXq80zt1DbLjiqNMGTTImPdhBtSUOLGE3FxGvj9eR7ugNSzQYulnayVZ1pg1gs+OF64QwO8kTseapiOqunnRmWDOe1rm46xIlVKmYR2Df1gtGR+xiictckR0jQw1X0UXtKrIZz7sNSbG0LTbVbUNxeWdwYjpwF9cONw2OThm6gsfWlKPmJDXiZUU5AiL3bCZMvngVJbbbgpJbcwexT/iOYNN6bdvcmUBV3tCuk4CKuya8dvAx3ltLsbC3krNjNkGeSYFOq/cL7Fo7CeWsmqNZXSKImIhKka8PUUHrq/sVvwgWKbcabxXHa50fnYvUIlekHe+9EIfcCbS4JkwdJxNqRNVgbm2aXypoYpwb06dHit3zOB/AI5NoOGPhHSUlfTw5w2FI4uisoEunR5HEbpvt0c1OQxFBakSJ19G418W278x1km5ZeplOCnqwTpc2oWsv4g9bfofltI2BeB6Vpg5XlUrXRuQmm72js9v1NjMl66TIRRccLzdT0/DIIMGm3hJMjc3pgxHheTb15m172pgpsEUajTx0ZWVz7sYiZqnTeZUUulHIR+GglDtcU+0aObRcvcPq9CYgpsF5+9DVlyEtGagwZpRKBZnHGZS3g+O10vAhAkkMPrGiGmx6HiXrtC23mXZX+97nkoY+NmrkG8pRFUqzSlQnGcrbdrvFsK6NVhcJvsoxvT9gh7ZgIkQ9+aemkTZDcrEZ2pY5LT/3hKCuhEzjdS86N5JWnCL5ssOjk43XekSQXES3Dlz4Us+ouemT6qWxxV6omE6w94Stdud1dDH2dBRGW6TFffsKJ6dDenel23GqKFznrtfuvDHLIFLRrWhaa7688HB5i8iKRojTyK6aXo6O91Ry5fiKN6jlGacUbCSVcWp6DzNRSxJQwVcK1L6FzNnhG1RVHdg/XRHQ1qJkkaLZGjq2J9VHr8HVQTtswPBCVvVi6VtbX7gRLTH04oTveRSUTXe/vXfNbX+QmkIob4PF7dsVzmekzeyug56PRK9y9p7FrgjSKQwudyMGOUsJOVnby67jQNufL8eJ2DU7z7wZ11trYyuoOkrBMsdvjLR3sYhMm1K+DhPM73e75jQ3kEEK2YolJqi2T3qa8+4HZa2lHCNCsTvsWqp3RWS6FAF9a5puvxqOY45de9oq0CXN4DXBCy7WHNH7abk/heq2kLkgRqG7WvOpwnFMFghHBD508lF0Ld6mixU2EnxLId5w4/HTftrmyHb0pbtfrZDW1SiHhzbYJr/CS1kJRL44JkW1NySSlAouvOQaa5dxZ/fJzZX8LkeMrRLivXYv9v7lUh3SsV+JgEimZYXla8wUSb9k8onoceiSLNcqOlhWAR9UB8G0VRwelp6nZVOJNYR8QLJNa/W5E/n7ToEGl4mz5e4c4zvclodrfo5a0M9hfQYVWVAlxPnIkRxXlI59VUE3rgVNSFiBP5lb1Cuo/UkFOWO3nmFe6WbcHsxxuiY24mVXf683FmFH0tqvFUXZXwtrxIiJ9NfjoKwDSDzRCFkdI8cSVtABpCrYlwv5dOUuSb/GljXfG+k+nLZ4XkEU6RoD19RKU6oncvROza0QY+vANZeUdnx5o+XbAz9o+j1vomPBHsMjL1Zmtwa7jdStHSmoqeMpulEUSriBIOasIKk75hRSWXsg1HqqJoUUpf1yc0PFUmjHpYwzNcborUXdIRsiyXJg98PSnpbWce91Xiyc10kF+SWL8EhFeK5XIZNvcXeDbk3WmxprTa+pqRBV1PUoy5yQe4sS2YWMmPjUrSW5yQaQsNnmbEjMcqhBNm9vmImsGgjDLJEvRdlW+JZ25XuI2M5ww1K6kHzojgp1vtcGpHNBE7/NdUkbPWqcqPPpHmOJsfHNYGWpIJEpWGA2YOtw1IJyqdgyqymn9BLQvMaYJyTxJr8nmguKSodgLTddPJGHoKDb5XTeaJbSQqhYD35Qw0vAhNslAvl77eC7PtivxdydJHWoW2rrq3NBa/nEnC+B3SUjEh97vekQgHLhLS0gcTWU1hWiR0peHQ/sntvnG364cXLN8N22OPb5mO0GJdWlKpvu6erU9+05qNKRCY1MwQcx1kbS40Fk0Hrf9DvlDh/lVJskuB5tG3Jy7ECcGfmStkeQ+0pyXjVqoO4JNQuvlHqjDhXjV3Hd4qhncVeM6npK5uEraiQcXm1vJm95DJSL6bq7qWulGG8ZDOksQ7GElaQbLomYfi9E+onZi7isY2Yw3Q1LLvkbpleSEdBjB08lpfeFX/fnUlSgyjUdP4PQS7exICK+mWuRJ8WbRXR2wbF81/YH3IruNBqI5C63sL2JEMx1Eyu4AQu4zK8bMZHJhjQEIYF4TfI6cgl28BsMtU6hXYKQIbyWUo1cq5odH55aSjRi5NCz8C5VFeE4wnc310h3zYNecVRRWBq7I48fl5uW2e/WVSaom83bh7f5/PR1ZP2vHizPh4L/z84mn8eI3x5TPQ6Ofdv7/Fjr87/U5JcPb40bAz2ep61t1oevQ8r/ctb68S+easyTpueT2fnZ2dh9O77v7HD+7dBbXHh92zXT17bM+sch74c3p2/nXzS0849eXPD+9jAhr+bT7cc687uXx0U8PzP92pVfnyfL/tv8i4P5kZDvxd8vw9eh84c3bwIuiN32K4pjX/2mmu17PSeZD23nByVvv/9fNakHBYklAAA= -->
