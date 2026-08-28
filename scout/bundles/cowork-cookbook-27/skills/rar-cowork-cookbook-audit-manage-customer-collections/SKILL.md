---
name: "rar-cowork-cookbook-audit-manage-customer-collections"
description: "Audits manage customer collections records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_customer_collections", "rar_sha256": "6bc8c8d81f81166d6ad3208486bf287d59bb046ffce6c7bc483a3a8ad4d1c092", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_manage_customer_collections`. The original RAPP
agent is preserved byte-for-byte in `audit_manage_customer_collections_agent.py` and in the RCI capsule.

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

Manage customer collections Completeness Audit — Audits manage customer collections records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-customer-collections
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_customer_collections_agent.py` and embedded as the fenced Python below (sha256 6bc8c8d81f81166d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_customer_collections_agent.py` first:

```bash
python3 audit_manage_customer_collections_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_manage_customer_collections_agent.py   # or on stdin
python3 audit_manage_customer_collections_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage customer collections Completeness Audit — Audits manage customer collections records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-customer-collections
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_manage_customer_collections',
    "version": '2.0.0',
    "display_name": 'Manage customer collections Completeness Audit',
    "description": 'Audits manage customer collections records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-manage-customer-collections',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-manage-customer-collections',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd10b0e6ddeca0080',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections/manage-customer-collections'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/audit-manage-customer-collections', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditManageCustomerCollections(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditManageCustomerCollections'
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
    print(AuditManageCustomerCollections().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716ebOiWLbvV/Gd+0dWtZlHGQTMjo54TCIIgoxCZUUWM8gok2Ld+u53o56TWberursiXjxzUGHtNa/fWnvjry9u3yVV8/L5RQvdcsa5eZ4mYTNzy2BGV5eqycBblXng38yvyq5Jvb6rmvbl40sQtn6T1l1alWA52Qdp184Kt3TjcOb3bVcVgI9f5XnoTzTtrAn9qgnaWVRN14s6D7uwDNv2Lqyu8tQfH9dTt/TDmRu7adl2s6bPw0+e24bBzE9CP2tfgfDw6k4M2pfPP/388SUFn18+//ri527bvikj3VWhn5rQ3xQBy3O3jAFdPQLjS/C9DhugVQEuBWE0e377oQ3z6OPsb3/LLm4Ttz9+/lLOnq8vL9MftS9nXRLOusptu0k9t3a9NE+78XVG5hd3nGzu+gbY7s5a4Lsyfn2s/Mapqmf/mO798BDyGofdD19eKqCCOyn75eXHGXDXl5emnz6/TlzqH358zatL2Pzw4zc+be+dgH0TM6D169fn9ydbQPiNNI3uUv8BuD5i6IVfXr4zbno99J7sBCtfXk9VWv7wYFw31RCWU4R++PHP2N7jlKdt9x/x/enBOAndANj0VPzHj3cn/zybPw165/nnYmsQ1r9iCSB/E/dx9nTUn/G++/9/sc5TkL7vHv9Ddn+0YP6P2U9/atu/WvBxFn15YcI8HUB2eHn4efbrV01h6Z8+BN8ufvj5N8D637LRqr7x7xy+gppNo7Dtvn796UN7v/zh558+9DXItdAtvvZN/kc8/8ivdzm/8+CT6offrwXyjTIrq0s5e8/02a9V/X+a315nppunwbfr7efZ9/UyveazyYg3oQ8XfFczLdD1Oz/++PIbQAiAJE3/rP/PL//1XzMp9ZuqraJupvlVP8FM2aVFOCmvJ2k7A3+n2m5C4Nc2BY590oH8Pz2AZFZFs1/+r39HyU/+EyUX7oQ9Xx84+PUNB79+h4O/vM50wLhq0jgt3XymkoryZaIuu0lo3YRt2AwATryxCz8BIPo0fZil5eyXf8v7653Naz3+cgfV9IFPKs1P2NQCIH2d7LOSsHxa4wPQD6+h3wMJeeUDdaIUwOpHYHdb5QPAtskXbZbm+SxIAYID8B/vvIG/Pk/MfvnlFwDOyZfyAabI7NEV2gUgeFdn9ukTsCvK0zjpvpShn1SzD7/+9mH237N/terOfJKhAFh/RgNoKGjyfgaqqy8AGQgUCC2Ajns0fv3t6V3ApgTtB8QujdLwsRhkZxYGb67WtuQneIXNvBC4GLi3qKumAwg9S7vXGR/N3vUFQqdbE4YnFehHQViHZRCWoFt1iQvMefdkWXWzFqRgG40fZ30b3qX+4jX3PhYWoMzd7peZRCugY1Q5+G9S804EFldlCtz/ngiP64BJ86GdUW8sXmf7KR9ntdu4ddK4TxmR+4gL6BRvywFzd1aGly/l1BzDyVX34ni4BxABz/jPkH6aYj61XpBZQfsm+07jTn1Nv/e35kvZPhPfbcJ7NweqjLO4T4OpHfz9mVJtUvV5cPcf0HTi9IxC8IzKPQelfzEo0N8PB/dePvvSw0sInf3/nDImLUmOU1mO1Flmxu511X54bxqEJi8/ZifQ7u/C7pXybQR4A5A3HP1S5ilIhWb8+4Py7vMnzQOb+gYIV0n1zh9oBQyb+N7zccqvppky2f1SvgH2RxDiOzqBkIDiBck95dSbwOnum6YJqNDp+7fm/fTT5BWQc7O694BnZlEYBp7rZ0CrZqqpp9tBcoZTfV2S1E9+Z9UMcAc5APjPgBJTbACo3123r4CZoJyipiq+kadTgIAWQe8DbcGkGb7OLFAWU2q0oBbBXDPRAC98uLOaFSHwMVDx3cNt4tYPZabh9KmgO+F0Gl6+9//z1rc0vmsyKQ94uoHbAU9eJlwNwusjru9aPiMFmBZTdtwX/T7YT0tn3/eVv38p7xq+Qzmo53xqyd+5ZgbqqHjk4gRHLYCUInymD8iDe/d9fTTQR4d+1+XzP83jP/y1kf3eEo3fx+3zLOm6uv28WDza2FsXewUVsgAZktZh++honx419+mt5j59V3O/Y/zw0+fZX1PudyyeOf15Br0uX5fTLTH1wylpny/gC/oTZX9Cp7tfSjX8FmQgvioA0k2+H0ELfW8sbySgu8RNGE/Ej0bTTv3pAlriHVlBGL6U74nwLBIA3GU8dcW2+q547x0WhPURtfcGAG6VHZAdTBNZHE67lXxSvw1fPpd9nn98Kd0i/E92KRPKg1wF3pg2N6BqwITTpeH9G7AK3Ejd6fPvd2Ly/YObP3K67YCabnNHhmeNPCHv4zTelgBVpq3E1MoesA82QG6fd5Pa3VhPej52LtMU9T5i/bPUexEDGUH1earlj7NpHP44e59sP87e9hr37VvZg83WT9NUPdkJSMHbO+375tILX37+AzWeQ/afKJFOODIhz8PcMPgGEvew1W4HsNBQRaBS5d+HiKlxtuO9wf6z2UBgE5570CmDSeVvPvimWvXQ57e7Kd1jJ/nryxvMPIP3nBoBOajnT+3UKxcgwYFA8P2RiuDeX58nnwwALoJxBnDAPJ/wiYCAIgKCMCzA3ACBlwRKYF4EE3iwWnveEsWiyA8xH/d8lEBcxCXcAA0gf7mGAb9HRn+dJoJ0Ugp2XcATh9BgjbuYHyJLD/FDCIYCHAmXqzUSEUSIAv+8L80ArD4tfVg2ufF9tJ088jT41xcPQwHlFm158vGiF2vTxVDcuybHeYOFtnSaZ7qmnkvdofhjKDaM70FLpuW4vjx4pFrQ7CprHTGLDpJr5oEo0NuRUgotOgd9RBahtUQ8m7X19Hp1WsyXnWiIuLDiyYTTkVKGUD7vXGzXmGS78wRJEIzWb5d9WsBOajTZoejg4zkc7WaxJs7Dut6XcFmbO4E3d3uzNdfi5QRyt96hnSSUA35UeIK1x6H3r9DV1ILULKXOSJw22Qqnw2pbLZTtCSP67Wq+GJTRPeorPIzM07hZ9S3XqwdY3IQbqKNTqxmC4gxnpz2b46PFeUtmT5z13Uo8aiXVYXvpWp2bhSHhvmbcUDeIDzVkdL4om/PgqJ6uxuWc883uSq/PGm3vrOxC5Zws1j5tQnvOCoZkz6MS0e9WpNucMdE5Ze66TPp+v9DWpmR4mdMx1rVXVcNBj61/ofNWyHyb6O2NnAmk68+DjZinV7vp9zrjrokbxZtlr91ckpy7ur3SGae9iOW4DtrarjsZKjQLpxZWGh38UTbofaZwy5WVEEGaqQZeVMrphC7jLrEunl6fmV2LDKLmbuSGO0t2QthLo8fwPRZl7i13icvJ4aiAdy7labe74e4ldFa7buUqN8+Vg4BEBSe9uLdaXofBCeKyTJSqJYXJJ87lD+uTPWdwMSRHpBucODcpj0NS58YRS3ik3KOnk/jS6tiY86TIoyPuYlgaQ9wMdkh7vriW65bIxEvJINwmES3putsaxCnQWgcytWRN1mW0vsGQLfTn3WCmSraQLq3W0StW9AmNEXkr9JfnofDhvvDnvaWFeF/uulT1WhTSG61krj1MKpdOuWxoJRoz9RCJ1aKVlA2+55QWX8f+9pBbXZBisCjulhmM4Hv0hmipsynr3iE0IjLdVDf3p2rcBptTz/q2fT072SLfnqLal0bbK12MKwm2LdV5hq5YpBGZeHVD+517uOUbz5EFX+tQ/0CGjLvj63lg+LoMyzDPJJsKlQqLurTWboNZEqbIW9qX69ImVlBPLaPNETqxN/xaNic/wfiFGKZME3JMK9wqNFtt5bHezkMth4qIWqy2Oir7VFtf8uaIR8wi4eghjpcQPCCnuIWHZpG49uIIcXKmJIExX2amleHiaacO285xs2OssdpADoqvbD2zVAV41V18G2Xba7QxWfqwM7bSOSI255wtlHJwl1rErobePoYOyAjliKAqbVpyvsQ8SlGOSdDooV43XAFF0OoWi7tzJnEhd/Yc6JQG8zjZDS5WsKdMnycVBnnM1aR7yivPlLFUlHiHnlEZVCC7arnYGTD6OIQmLx8W4XWnOurOYRlIWvLR2aV2VIhgjj+u1ueNIGgax+LuRuRUucG1ep/Prxf4WhzJRj1yjuXkN1GkraUumL4JyDYAkIw9WpwW5jwjOnSRi6bdnWU4KlR9BydhnC2V+lZKMHvYs0EBpecT2ECQThmq3XKetUi9x9aYWLPBcUAWOrP0ztWCxw8KF5NXtTAyzz5jEKTIVchpvuOnljLXhE1pm7fxmJ+Ua1ftfPsQWseld4oFtFfS+IRgmcXqGWEKmXOuwqjJHCupMnrB1QWjpKebJ16pgWfbDZksWJWDVUEhaFM5nb1Wv4w9KM2sTFLqBB3c1Ku6i+Fm7aiwBMnBOYtrKud2dA+u6wW+sZyrbfCskYSKtGRR9dAwWTMwUR9yxJ4/mu2wcymraLfWIItlHpW+6bH+rWkW+7bcrCLlmI+aJtL5Iev9IJpHmmY4m+PaW0lH+CDt1PNOYG4LhCAEg4v3ELTd91sKPR/W0qaO6PNc38gqsVf0YVGTvt3TVOHtxyY06UMRs/Mr7x6u3dBzzibWNL+xNM1ZUgjlblOhvuYbPvIpbmk1VFntDjYc2KasG+lNH1LtrEU1l+3nLUYOpz19vAznRJ6ru6renbAs5NgxMv2jZCvnUUKD3bXnjN4n0HZ7zLbLXV8gym2+EK5ucN35qr4iT1QYSGeRwwa4Ngq7i0kINofRzfZMZC/nJJnFB2JvzTOn4FTkHBS38mQgXSzRadpCjrgmCr7ZFwTvEkMC3XjCtzeBKxvUVTMFfJfTJ21dYjiyRBxF4zMsMrBwNZcEV5M8jczqPOG4ARs6p+jmu2YkorNQRU6sqEf+CtkRBmVnprW5Q5vOM6M+theVcupSwKBzpWhbZqOcUg3q/GrB0hRxqee4acP0bjvcOpphSK+/+Lt8p/HJSK/JmyTcGKbiy4GWcrwcfU84oPHxzPT5TSJPR0i9HNttUba6BNst21N76ehHudzqQd0mFY3i7JV0ZDDMVCo3eKcTa22V+rIp5c2iEn3cX7UFdVpCt/3AJbujt7mZXnjNtb2ga6YsguqMF0vneB53aiEOqktqCY0rVrULTzAFp5dQA51e32w77uQj1cjGad8WgrI8mAVZIun+YlzWG75eUxSXlSbbw4xKbsizmY47gU4OGxZejhvnwpLNqiO3bYbY/cJla95fkrQbLJjY92pm3fSEoo6ko5gHCkp5CT6FVnzEDwV0NAQSiEwQHL0C0IDWlUeypXrLFD9zcKs7EvwpXynyfLlsBjbU8Dm2C8S1x/jIsRpbvW2c9Zm+OWHSspoUW2CvKF8obiRbk+duh0joOOvQJY6aLFpR5VvythGT60ZcraJjziyk3t410vKU9TCyM6VOxkM+dnWfhdbS2UCLLK66/XIMlQhsZ3rNT72Ij/BzLu1yca/LKMntDYilDj60cOpqZTW1tqEbXnS14NZutHM82qVr4zoJGZkqYDGvUfZ5l+DH6zZ1jWrL2IJ0CnXDpRh9cUhrag5XWzMyXLU9NpeY0snlQl0kqnvZjLHFs6dw45Wk3ZW9g+fzC45zmCy2N5PWrw43d1LuWvJ8yLB42glb4doGST0nfOtoyiarVsvUPnQO0V2822YUeXZpIUfZirn1YDBihlCtTAXzMPAwzcMiGxbKA0yMYZ6uOHGfc0hxMPeE32g95zHKzj2Xstgz12HBZoVkwaIbBantt6SJ3BotduBrvzI8P4oKCzs4N/uKigSx8mv/IOYiF0Sa7uQ+f5BV9Dboga+Qq42eSWhoniwXO+ULytN0EyEToY/nYyn1GAw2EYXo0rueNqLjAsIdPe2ClSaldLCm8BDhHcNNyKClEP5QjOfdulQ2LNlBa+ZYJlgeBZxx1NSoL5lz163xCobB5nakB6M6LphkxYhdhzBwKKHyHnRViZRiCWBJt9tcYNHTKoQsVqRDL3trf8GVaxLiwUYRDtpZWgWnmLFHQ0CpjS4f9d2+XIBxwQyO55pvVFbnxVK2U4be0I5cmOcmGTpVabNCIIRsLLVNXKM0GLavh/LswomGjSxe7TT9LPSZsTlnSwOkaBAKPt1VVroHEx/boOT1XKAwCxHBmoCWgQ5lOs7G6lGnkrmk2JUtdYv4yq1RMx/INveRpjkl9ljp3BJ0I+aU0efy3GpMuIY4siIVZd8aclrkjdAfDrdEG9ULGhgsgp6XYrJFy/4SJ9zpcnHF/hrs0iRSjaO9zBWtxQ64VfeVMe/PY35Rdtexd3M94nwtTyH9uknzwkLtpsSEcHt29U67qK3LxEZs1LiMZYOEX+rMsjvZ5yB2vhI0ooVxbbeUM/6yWK1NjvRaNrLiUy5tula+6WOCFmjTemUFfMxt0JV1bLTW73jLzYN1PNIo0WXDjr8SvGcY5HHVzYeEEg/IHg9KVevmNb6Hz0qzivpoWx2D47xr/c1iD3k80rjb68qvtsdhjeF4DDrM2GE5bFGJA4/oLSZ7MkNqJIF4aYlvih2q0XMltLcVSq6MMDZLZ4eRobefy/JtWOTw1s8uusgfLtr+dizhvc1h+Ea10lsFwmnsmGGOQIeUFMfmsHQJUhDWR9nAqpzy3AprCKTb3VZsgKMoel0jfh06cHPaHiSywnbzhavt0Gt05LV1JzJUsVyM2Zprsi2KB0FEUKEkEvsd7uFzPlrBF4lc3YLtvLjC7n69pChL1PewoCyCLPO3e4q+yE6OuQpdjIhzwxKH9qhqY124LcSJc7Ywy5THVJlX6C2Aio2gKWgrjOHa8eNtiwhXlBOM1GzyoDwsw33C9DYSk5yAiOdgBQCdQXaavdU2udluI6ISA66s54rBoCsHGrT9bkER+7WJbiJHouah7UuSNPR9fF71qxqx1JqhYx09bZbDCSojr2Cu2iUSrwHl72WkPTHGXG4OPq4tbtYAMMmSFdYW8DhcSzZV8HzZ29gxosaAgoMS3+rkYR25RCCZDidedd5M7RsHEbg4EsrJasBU6qOhq8h+eJMWZdmK9TopRvKiOKYzHFILZ/bwcKjsnrCEkyBX2ZFP8/MeEbeLnoN8XmbE7SjsEd5rc7K/ZVoSUwh6Xeo3uxSTg6Rf3GV7CAMSkpJKDSooEQe5RROfwupgN8RywBrCvGnrRbNcK4pyudHLLZaiV5oqY8z1t6Vkbamt1SoqIpgxuuTYFUNZp+gWJtGWdaUkQxZggwN2BbureGHbGwRdkejoSXnPwlFZC/s0KNzLcesybVl4PkG7Ji9esEQ6rFdCHqppX+GrvVcOzTVHODCz3EJdtlGmsk/CUjox5hLl/VvVbmnzyKjDQCLmmIrXQumCg2XQF08UCghMELdqL3fr3Bz0bhMKkda6nFz7JZWhfY9uwtMeFaTLmiTN45ps+TCOwjKJ1YOS2UPGI/uiYEthlJBaqhLMwQ7pWtmSMiKvL+k2YVw8aC9b5Rpb0bwk0a6wIn8NeUizYAkGpsk5rihMbSh7EqkYZ48ThdJDi3Td6GIniStLiNflUR6cM9jqJPURXlD44mZe8cTYrxBf6BwNX1Q2c+WQhCt4qrnkQrNZlaK88PCTuzkEfOYw0PzWVX3Jwuqcq6sNQDUa64dTXV/8TeY0DJw0Pawg59BzT+7NaTZNtQ22oQpRCcYa5mokJWy7b0YyOmxFzQDTUW3LnU5mYx55N3i1Viy4wGEwzebDiuOvPD2Gywg2+tsIkacWjbaCcdxIOpJGg7yVSFEA274woQ2Ylr2lY6wOCrQ/q8WBC+UxPTDbcfCQs7oVPFjv1Mt6vC1952oSiInlXctEg0lsevo25Ba18ETDtuv9HlpsR1Z2rTU0HEZ5YY8ZbDMSex2ITDg6Z97xgs1c8zeHwVTKtlhGLnokiVudxyBcQSNcvB20WR1szatJ3qLLcmSoI6LyhQEqbdWsdD/KFNPHBWyrrGA3kladI2D7BQl5kCVrq92BJF8+vkynp8+j6//8QfR0JPj/7GTycYj49gjrfoAcusHnu6zPf0Gnnz++NH4KNHqcv7Z5Hz8PK//X6eunf/vsY1o+Pp7uTs/art3bIX/nxtOvk17SMgDLmvFrW+X9/QD444vXt9MvJdrpxzQ+eH+5m1XU08n3XSJ4r5oAqN9VX323TV6mXzBMj47CIHW78Pk1fh5Ef3wJRhCY1G+/Itjqa9jUk4XPpyjT8e30GOXlt/8BVisrcO0lAAA= -->
