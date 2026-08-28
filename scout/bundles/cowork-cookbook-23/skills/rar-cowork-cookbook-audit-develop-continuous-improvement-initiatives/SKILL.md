---
name: "rar-cowork-cookbook-audit-develop-continuous-improvement-initiatives"
description: "Audits develop continuous improvement initiatives records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_continuous_improvement_initiatives", "rar_sha256": "c9978031e22a86515028a1a9f3800b2b239c111ae4720f6e29ac21ec28e5ffe3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_develop_continuous_improvement_initiatives`. The original RAPP
agent is preserved byte-for-byte in `audit_develop_continuous_improvement_initiatives_agent.py` and in the RCI capsule.

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

Develop continuous improvement initiatives Completeness Audit — Audits develop continuous improvement initiatives records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-continuous-improvement-initiatives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_continuous_improvement_initiatives_agent.py` and embedded as the fenced Python below (sha256 c9978031e22a8651…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_continuous_improvement_initiatives_agent.py` first:

```bash
python3 audit_develop_continuous_improvement_initiatives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_develop_continuous_improvement_initiatives_agent.py   # or on stdin
python3 audit_develop_continuous_improvement_initiatives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop continuous improvement initiatives Completeness Audit — Audits develop continuous improvement initiatives records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-continuous-improvement-initiatives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_develop_continuous_improvement_initiatives',
    "version": '2.0.0',
    "display_name": 'Develop continuous improvement initiatives Completeness Audit',
    "description": 'Audits develop continuous improvement initiatives records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-develop-continuous-improvement-initiatives',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-develop-continuous-improvement-initiatives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e6719447b00e196d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/develop-continuous-improvement-initiatives'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/audit-develop-continuous-improvement-initiatives', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditDevelopContinuousImprovementInitiatives(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDevelopContinuousImprovementInitiatives'
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
    print(AuditDevelopContinuousImprovementInitiatives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6adOj1pLmX9G8/cF2U1UIibVu3IiRQBsgkNgkcDnKLId9X4U8/u9zkFSL+9o97Z6JGFW8JQkOmU9uT+YB/fZmd21Y1G8f31Rg57OdnaZRCOqZnXszthiKOoFvReLAv5lb5G0dOV1b1M3buzcPNG4dlW1U5PDyVedFbTPzQA/SonysjfKu6JpZlJV10YMM5O0syqM2stuoB82sBm5Re83ML2q4PCtT0IIcNM1Dd1mkkTs+j0d27oKZHdhR3rSzukvBe8dugDdzQ+AmzQeIBdzsSUDz9vHnX969QY3p28ff3tzUbpov2LgnMvYrsMM3XIdvsKCw1M4DeFU5Qs/k8HsJaogxg4c84M9e335sQOq/m/37vyeDXQfNTx8/5bPX69Pb9E/p8lkbgllb2E07gbVL24nSqB0/zFbpYI+TB9quzqHBswY6Ng8+PK/8Jgk68p/TuR+fSj4EoP3x01sBIdiT2z+9/TSDzvv0VnfT5w+TlPLHnz6kxQDqH3/6JqfpnBi47SQMov7w+fX9JRYu/LY08h9a/wmlPgPsgE9v3xk3vZ64JzvhlW8f4iLKf3wKfng0n+L1409/JfYRtTRq2v+S3J+fgkNge9CmF/Cf3j2c/MsMeRn0VeZfqy1hWP+OJXD5F3XvZi9H/ZXsh///g+g0gsn81eN/Ku7PLkD+Ofv5L237zy54N/M/vXEghUlc204KPs5++6yeNuzPP3jfDv7wy+9Q9P9RjFp0tfuQ8Dmz88gHTfv5888/NI/DP/zy8w9dCXMN2Nnnrk7/TOaf+fWh5w8efK368Y/XQv16nuTFkM++Zvrst6L8H/XvH2aGnUbet+PNx9n39TK9kNlkxBelTxd8VzMNxPqdH396+x3yBeSVunMfp2GV/9u/zY6RWxdN4bcz1S26iXQga2RgAq+FEeS05lHbNeSUuomgY1/rYP5PEZ4QF/7s1//pPij0vfuiUNSemOjziyQ/fyPJz9+R5OfvSPLXDzMN6inqKIhyO50pq9PpU24HDy5toDrQgLqH7OKMLXgPeen99AHS7OzXv6vq80Pqh3L89UHA0ZO9FPYwMVcDSffDZP0lBPnLVhf2C3ADbgcVpoUL0fkRpOB30CtNkfaQ+SZPNUmUpjMvgmwP+8b4kA29+XES9uuvv0IiDz/lT6pdzp4NpUHhgq9wZu/fQzP9NArC9lMO3LCY/fDb7z/M/tfsP7vqIXzScYIt4BUriJBXZWkGa6+brIdhhIGHxPKI1W+/v5wNxeSwA8LIRn4EnhfD3E2A98Xz6n71fkGQMwdAj4OpwRU19G4wi9oPs4M/+4oXKp1OTQwfFrB3eaAEuQdy2Nna0IbmfPVkXrSzBgai8cd3s64BD62/OvWj54EMkoDd/jo7sifYT4oU/jfBfCyCFxd5BN3/NS+ex6GQ+odmtv4i4sNMmrJ1Vtq1XYa1/dLh28+4wD7y5XIo3J7lYPiUT430kSiP0nm6By6CnnFfIX0/xXxq05AnvOaL7scae+p62qP71Z/y5lUWdg0enR9CGWdBF3lTs/jHK6WasOhS7+E/iHSS9IqC94rKIwe5//qMwX4/VzzGgNmnbjHH8Nn/x3llsmG12ymb3UrbcLONpCnm07cTikntcyiDo8JD2aOOvo0PX8jnCwd/ytMIJko9/uO58hGR15onr3U1VK6slId8iAr6dpL7yNYp++p6ynP7U/6F7N/BBHgwGwwYLG2Y+lPGfVE4nf2CNIT1O33/1vhffpq8AjNyVnYO9MzMB8BzbDeBqOqp4l5RgKkLpuobwsgN/2DVDEqHGQLlzyCIKVSwITxcJxXQTFhsfl1k35ZHU4AgCq9zIVo4woIPswssmilxGlipcCaa1kAv/PAQNcsA9DGE+NXDTWiXTzDT1PsCaE8cH4Hhe/+/Tn1L8geSCTyUaXt2Cz05TCTsgdszrl9RviIFhWZTdjwu+mOwX5bOvu9J//iUPxB+5X1Y7enUzr9zzQxWWfbMxYmsGkg4GXilD8yDR+f+8Gy+z+7+FcvHfxn0f/x7e4FHO9X/GLePs7Bty+Yjij5b4JcO+AFWCAozJCpB8+yG718l+P5bCb7/rgTff1eCf9DzdNvH2d/D+gcRrxT/OMM+zD/Mp1Ni5IIph18v6Br2/dp8j09nP+UK+BZzqL7IIKwpFCNsv1+70JclsBUFNQimxc+u1EzNbID980HDMCqf8q958aoZyPJ5MLXQpviulh/tGEb5GcSv3QKeyluo25uGuwBM26B0gt+At495l6bv3nI7A39/+zM1CJjI0DfTHgougqNTG4HHN2gjPBHZ0+c/7v/kxwc7fSZ800LQdv2gjVcBvfjw3TQ355Bypj3K1AWfHQPurOwubScj2rGcUD+3RNN49nV2+1etjwqHOrzi41To72bTnP1u9nVkfjf7sol57BLzDu7ifp7G9clOuBS+fV37dUvrgLdf/gTGa3r/CxDRRDITLT3NBd43BnkEsbRbSJS6IkJIhfuYP6ae24yP3vyvZkOFNag62GS9CfI3H3yDVjzx/P4wpX1uUX97+8JBr+C9xlG4HBb7+2ZqsyhMd6gQfn8mJjz3fz2ovuRBDoWDERToMgxFz5cYWCxsmiQwYr6gbcxm/CU9nzsLZ7FkXAzDbIBTi7lPggVjuwsMuAsaEL4PllDeM90/T7NFNGFc2LZLuxSGewxlky5Yzp2lC7AF5lFLMCeYpU/TAIfu+nppAin4ZfjT0MmrX2fmyUEv+397c0gcrtzjzWH1fLEoY9jO9egoiojUKX1rl+OZ8w4Vrq70sU8EnIjcamSTfL/SLUMT7b2XaM7dXrr3ZhFuOgPdxMjhSid5R1qoZaiFGNYVcVhfxP7ea3Pm2Gsa5err476InPJiG+RBPjJCbhiEZV7BlrVRI+yMVOfzrlVHTPKFqJRonVQrg89GI7xdI5XaOhRKkzk5HvqcCYpRcAnJhGGW0hxsxmhQFIuqgNwBm8i3ahOKlSY5bCqndl3pRqRH16rHx8KO5/5eKxGQazjj5zGulDQD8p4+R6VX37T6XDiHCqNyhbDsk9D6dpQGF7dKNVA4vhqNHZs2Nq+B2GARSZL6vdNthZIsQRAYxnVr7niC9nNKwivhfIwYIxWOhMBy1g5f8mPL76xrlDpacdYxujTzixvdwbGmWOpOxCF5QToizS2pp2TiWJPz5ra1rIOWYwq/26hdmlQXeHil8azSoOr9lB7DKw7ZGV9e+1MgqHfLStgxXIlN2R/LuLmYFGVZXmT5vNRhkXZZrhG9uZ5dcnFkm+vSnqeXO3kzh1pftivnuqeOQWPsBkfjK27XX5uctQnZFgxLPgNhaWienzGnQb3H9njjds2qS46mJiilcvcG2bKKFsdPd8cGnrfCD1YU+P4ctoGeH0N13CZDl89ps1km/NkNEI2QCIXvHDAP1UxfiP1azQ3Malx8OSauiPLElU/tIVNWPXL0domWjYHKkEnnXVV0yLkULzIzy+WNyIHodusOmgsjNAq5FHPj/t5RZE5kvJcWF+++MG8Ofmf6kCWOmyNNbkQrs5UmQ8skoxzonHmyoFTNkbA4P14zPCdtL7riLk+KIbLj6NUe+AIWK2BfofSq4WFS+0SIBCWIXcYgd4mf72AxiG0kEIZjLuQoakWJVNVzL+ILsjzqikyPu5tiKbHn4qk43OxKXBNzm07bLG1CGa8sefTW2Fj3R8/niRSoSXPN9DROiGC7P/L5YK56bKNjbmIrgD8sD1SxKTbbfndLjmuwTnT9Zl2NrNtvBhfQ987Y4jJKscgltWW6IHhUlCOjzpX18vEXi9jKwWwV0TZWm5PA3naJG/bGGsXLZkduhMyjfIRDNw5Rx8bNTWJxGdE30h+TXrxafrzaeNsLn+yYhK5BxOJ4YopjV6vO/NDi+U28L7mY6KKSR5IjPjfxu1mlQbQ5FkzgSWR1xA/7FHBZ1VPMpt1XvOo58sbZS31NFXM6tsz6NkSNbqJY6tTWvHRJoHT7a6qe5/GmahGpGrDKZkPHx1aVBAymKHZk3mQZubD3t6twXMfb6qTOT6eAxevzzh4rk3AXgYGSwTUGW146o/K51iylsDZ3YoMdtrC8hBWyJA1vTTH3Xb4PRZ5l2tU2FlrjlkoZQ+OmVqb1XJhjQqZ19m2ehZzJJ3Y/tqt8i7hpuofRC4RgvM5pf5FU0iX3O/+iaOUYgiBZLlPsWtJF4PR2U29uAssg687DpPY6jzLMvrYygpzF23VxajFEkPEeBTjX4DQlr47ivOBHe3G/mssQMKTGiUsVuY9GcYg5Bmi268zthdDvNvtcxhbBgSPFnNgoNGKeVgfrnrkWMWh77M7EfBKnxhVkJje/38R2KW0ORGDOW5VlrEDSuzA3N6m0N6KjuJ7jOH/Q60McyInS6jAjtt3K1DYYe97rtq65tjOWQ1ff4SXGqIUrWVK57UFU7/xW35i2QAjEQFBxfN8kQsVrvbJqze5k15KWl3IeLTWfy+KOJpFT3MCuCLcfG5WNOuOCk5RzGm3D4rVRs6g0u815gAtHMV7UGA56Uebg5uFknvLwHArhPr8vaZSXTqe0QYCwAn6PF7S5j6RBl7j+JEvjZb8WWXGztnguWyBJlRprYUu2Hn9LzyJJ1C2e3Q4AGzbXs90RYGUjkKCdKlJzpVIIBRvXhKTO6+M+E5w1obZxo/O0cN5pYy8qsRAGGLlBRf9YBT0SNAUljB5jHK1Y9NDiVhGwdNrtOlPUDd/wS+8wd6/UrhJqO+h2QCLK0SE85LLAWaWqMFubm3qDoUpl0AaFD5fkksb6tUvm5bX34+yIHz3k2Pnk4WiOC2svu32RGmR0MzK0j7xotFzqVOLW8bBWrTWjVsSd3yMU6shLXaXP+DnrDTKnCPkW8OqNJYDJLohko14MwjN2dVOQVYwGVMAvhCatvRR1jE01KPz6TFv64rjrjvr+vCGWl/TOO4M5HPSq6eMmgUzOkNZGt0wJtvdNzvTs1lsl0mAJe8GmA4GlVvOD1rD92dhvMz1MU9eoxQHhE0FabLVi6y0xZSgBkUmGa7MWuG3Y3JQF59QiybK639MDeVa3tIuz+k1QV9VSs+HkcAnjmyLaHhdBCExu5efzlaZqHePwTsBqZpR6K6x9W4I7XLxag7tPyqXOs/xculXSYa/J4JbGJ3vZJ+tLlIlJebP8OclHIF6rbDXGWwlyvI4bF8ZuXHXfVtypuKTd2Z1fSFO6s0bFXw7ZFtvPza1Bngt5FWamJK6RhUCmJ+qclGs9QHvtRDVdtg9HjANlQRyEHBZKq+wuzjJ3zk1caYuqWHGYI58ZFCXRKM1HfLhFqqEr7LIkl4u9GrEF4120e8XQS0GsDcYl3HQBYikW55bMI1LbMZLL3rVrtN6d24vf7jaH8yk5btl1P0eZsb6QF5c72Xv1dDAX2EodIGy8z0vWN47mIl+hu+roRnPUsosYOeO3hFccvBx4w5NM/Z7BUYI9NCPo3J3H9voemZPsRifcyl6u2IITcM7KDnqZ2KpXEccAhyMkmeQutfKE1HYTSt1V9N5OFofTZuufnfV5HqzD1C5M3GTmDRyYMPEmXw7HNL6Eh9MlhF1ty901kgIb/TDwV2Qnb/f7c1Gwm+IiHazeVbp5alid74g+vleRrhNLTrtZR4e5oQqXbPZcxPB6tk/oBbitEaRL4qrQqxLYenPQG2AMTsy6d5WXCIYgC1k62cVOO1wuc3y+4pcYkwo9kQfmDmUXGdxlx6rjmmcPWPIlqZDrliw74xjWZVO4eF1m0RZoqhNjuGqNlTFYyQZiO+arUYs8G04FFwS/WaBQVyglbrIUX3dOfq7xe76KmHNgRrcFgs9xsB7t/GANSd0s7MWlJtnFPKg4Up/H9tk9LqWOCY65kywKPqE2HuL5GmwzAkL4iU4s2AXTnaMCi1aUyZVKNPqXC3V0t3O5FEm57WKkQJ2huCURYoHl1Vku236Bk1fHFO5siNLdKVG9tKd0+7AM8KaizWEVbWldOJnFlcXbmq0ZTtU5VRKPkjbufWaUMTxq9YA3MpdWVlxrsQdkNZbpqey31l67dSCzhF7nN6F8mAd4ctBxLYKNRs3UraaNhcwW2kmRAn2lNeuaNbZxD1nSwvA8pFSEvXa8XOy2dhwJa/vcVYTHtuElTMutFmn0KoxyvDvIlelurook+Sxjh/doMFsxWDFNfJ2LmXQhaNE7CSvLdLZoHoUhre2d5ixXe7YwvAOmFGLaNggbwsYnJWSPbyOsTHjZPFMh4MV4IAu+5w2nZ09KgLJBu80DcqglmpRitSpZrlHVJcxJ1lpEWnmD+2finGFD5/AKappKurAJMsDUO6dfIHcKWC8MuXBPo0PArS26UncbdE22WBi73hCdGYlcI3A9YXq7zDAVRN3vTvrG3cZJNhSDcc929xKJQ+TcXD3jcgB7NCOwTc4dG8ZOcrjDaEauze7UJRw2wzWT1mbFVhFZxzG3GmksMbdr60xQPmUvqVyr/drfx1Ahua8XEgsnZ7A5MOxikLNe8bnRgluNPFZ8NDXr6C6RpuPII71DiPi4Mc+7tnMaTesrg9NsTsqxAWhL5TKscWHhsXK2rzQ/jpscJeCkGZnnOKUHNfYxW0KV68obdF48kZossN6WQEWk1IM1eiUls1+JwtJGKsrYFaJ+ojA/uVuX/BRdPSqXj3kwpCf0VnCcLQcNKncxOAvjQMsDRo6dwLUKmocj5556dEmyKMlytmPa/qL38QzdX+JB64/t4OnSLu6d4BxGi9SrVGrpnAF3DeLDTo46/DaULk8HaGHdd4PNSu4pZBSeVvZxHB4s0z/L57DT3AOXnEZruR0WUrfzZdajb/NrgfNwdyv1Ci7vT+7NEYbszPT+mOVAN7FVfvMGR89MA2VP4k3FNAZv1kiEdmRmpsjFHU5718D4Dt+w9y5Z7WjKJuuERxf9camCnbGKC3Rzuwg+483XXM00DR+c7vpVjAtig5OSN6JJGaK1jzSedxjO/ermksFOD6Luvh4RhB3Ifbs8VXJ2DkkkpRyTHPV10iYCTR1vrQ9GvPUKqsTac0f3WzhcZkSK3qkuPTCDtl4PPX2hCHrL+uy5M4rNuaUCRYYbU5FlouO1Fhk44OpDswaMDW2Zwy1wE90wsgvD/bCbd30EojUHk3N+WC1oZ3031SJhDjvQ0JpT10cx3zfVUi1xLdR20b0mm2s94LJ8Gu7r+Qlb3y4m7DdKuYD7wG2z8cwB4fw048Lzwd8et4qJLggWc41y3PU0UvSBLFg39orKRF+3cPDsbhvRvbWU7Kr+dnksgwYEO8uXyvmZ3B/jPVvNmRV6cPGIwYa9b7Ru2zsSgo/7RIAb2X69alEPl5bhsA25NUogSqyZ3aqUFx0d0/swXeZRs78Yq+7CDpTNtYuykXLdRuolX2e5c1yIbjRg67w6WoMnbURGdtI8ZvuVGuDlyBTznT9S5lxZWeoJV9u5HQApOZ64+bVRLc/TLVS7RYgfU4Xi3FYS26GLOaf4/sJzUKuRafjO4HLnIUjVC0W49sU477BunwX+fKfwqNeo9xbFrz4VGWWDtJEpExzuuAt5fmsYAVniRxRRL7rLxv2FiiSGOVy1QnEPHX3QoUKwqSSLk3Eao9GF0hodHitzTl8CcO6u/i21+RpdH6/X25lGl2x2wNjycs85yqrQPXleSDh/s+yNUxCEpvOtGdGZcF0vz3grHzlyxdhqyGYY3IhUm61UdiV5IU5i1xKLhgCyTBZOZ+v2hrftub8wEe2GreIG98Xwet0etWXk9aflcSXu2S29V0NB4yhulCs67jErPdwLTqIsS1gzxLVdVArFOwujBSMz3hv8HpX4vCCsC8L1d9iixaJdqjnnr63m1LhZSi6jG7uURQ/rzsTVawjFdbnj5tbRxeFqVYet4xG05nLn3ugzUCX+hcpX9L1Mg9Np5dXbwRawLXE2baXKNyKnGaQYiFSV3CvxIOML9Ljkh5ran0wjzD1YoInb3Qdmi65WQ6sR9kYIVqu3d2/TjdfXPfD/9tPw6W7i/7Obms/7j1+elD1uRQPb+/jQ9fG/D/GXd2+1G0GAzxu7TdoFr9ue/+G27vu/+8RlkjY+H0BPD/xu7ZdHC60dTD+2eotyr2vaevzcFGn3uNH87s3pmumnHs30ayAXvr89jM7K6Q77A8AUmqIGrt20n9vi8+tGfJRPj7CAB1WD19fgdc/73Zs3wkBGbvN5SRKfQV1ONr8e30y3hqfnN2+//2+dE1utziYAAA== -->
