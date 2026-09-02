---
name: "rar-cowork-cookbook-audit-use-the-knowledge-base-to-find-a-solution"
description: "Audits use the knowledge base to find a solution records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_use_the_knowledge_base_to_find_a_solution", "rar_sha256": "e8a88322482652b9f7349783b4372dfb6f860218406fd2a105ae7b2990dbe13e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_use_the_knowledge_base_to_find_a_solution_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-use-the-knowledge-base-to-find-a-solution:1bf7e41803cab983ba81d758e74ddd32fc401b4444a3117113d8bd0c0e46a01f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_use_the_knowledge_base_to_find_a_solution`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_use_the_knowledge_base_to_find_a_solution_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

Use the knowledge base to find a solution Completeness Audit — Audits use the knowledge base to find a solution records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-use-the-knowledge-base-to-find-a-solution
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_use_the_knowledge_base_to_find_a_solution_agent.py` and embedded as the fenced Python below (sha256 e8a88322482652b9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_use_the_knowledge_base_to_find_a_solution_agent.py` first:

```bash
python3 audit_use_the_knowledge_base_to_find_a_solution_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_use_the_knowledge_base_to_find_a_solution_agent.py   # or on stdin
python3 audit_use_the_knowledge_base_to_find_a_solution_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Use the knowledge base to find a solution Completeness Audit — Audits use the knowledge base to find a solution records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-use-the-knowledge-base-to-find-a-solution
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_use_the_knowledge_base_to_find_a_solution',
    "version": '2.0.0',
    "display_name": 'Use the knowledge base to find a solution Completeness Audit',
    "description": 'Audits use the knowledge base to find a solution records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-use-the-knowledge-base-to-find-a-solution',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-use-the-knowledge-base-to-find-a-solution',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'afe979484d3e65e7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/use-the-knowledge-base-to-find-a-solution'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/audit-use-the-knowledge-base-to-find-a-solution', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditUseTheKnowledgeBaseToFindASolution(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditUseTheKnowledgeBaseToFindASolution'
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
    print(AuditUseTheKnowledgeBaseToFindASolution().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6+ZOiWJvuv8LN+aG7h6oCBATri464oLIoi8qmdnVksRwE2TcVevp/vwc1s6rn65779cyNuFZUpuI57/4+73Mgf3txuzYq6pfPLwZwc0R00zSOQI24eYDMi2tRJ/BXkXjwP+IXeVvHXtcWdfPy4SUAjV/HZRsXOdzOdUHcNkjXAKSNAJLkxTUFwQkgnjteKpAwhiJdpCnSbtyC1MAv6qBBwqKGkrMyBS3IQdPcVZdFGvv943rs5j5A3JMb502L1F0KPo4yA8SPgJ80n6Ap4OaOApqXz7/8+uElhu9fPv/24qdu07yZZjXAjMD6zSweSjALAdrEGU+LoJzUzU9wQ9nDmIyfS1BD8zJ4KQAh8vz0YwPS8APy7/+eXN361Pz0+UuOPF9fXsZ/uy6/x6At3KYd7XRL14vTuO0/IVx6dfsGOt92dd6M8YAhzU+fHju/SSpK5Ofxux8fSj6dQPvjl5cCmuCOtn55+QmBcfvyUnfj+0+jlPLHnz6lxRXUP/70TU7TeWfgt6MwaPWn1+fnp1i48NvSOLxr/RlKfaTWA19evnNufD3sHv2EO18+nYs4//EhuKyLC8jHVP3401+JvScsjZv2X5L7y0NwBNwA+vQ0/KcP9yD/iqBPh95l/rXaEqb173gCl7+p+4A8A/VXsu/x/0+i0xjW8XvE/1Tcn21Af0Z++Uvf/qsNH5Dwy8sCpPEFVoeXgs/Ib6/GZjn/5Yfg28Uffv0div6/ijGKrvbvEl4zN49D0LSvr7/80Nwv//DrLz90Jaw14GavXZ3+mcw/i+tdzx8i+Fz14x/3Qv1WPiJHjrxXOvJbUf6v+vdPiO2mcfDtevMZ+b5fxheKjE68KX2E4LueaaCt38Xxp5ffIVRASKk7//417PJ/+zdEjf26aIqwRQy/6Ea8yds4A6PxZhQ3iPls6q/GWlaUT1nwFYFXx3aHEOF2aYuItRunCOyHMeOjB0WIfP3f/h1MP/pPMMXcEZReIVy+wr2v73D5OkLba1u8jnD56r6+weXXTwiEry95UcenOHdTZMdtNhAUQd6O+h9Q2GUfL6MJ0Lz4AUG7uTzCTwNB8x/I17+p8/Uu/lPZjy5+yWHOIARD2S3IyqJ26zjtEXfEMK9vwUeIwRBn6iJNPddPkPFHV34a4+ZEIH9G04czBtyA37UASQsf+hHGELc/wIKAWi/j7IDeNEmcpkgQwxEBZ01/nwgwD59HYV+/foXmRl/yB0iTyGMINRhc8G4w8vFjWYMwjU9R+yUHflQgP/z2+w/IfyD/1a678FHHBs6Ne/hgoafIytA1BHZtl8FlDTKWDISke1Z/+/2Rl9G6HE5N2GtxGIP7ZijtW4mMHjyS9ZYp6PNoIqifmv4YN+QawbggcQujBfu/+fAlH0UUcGl9jeFAfQbxsfkR+rfUP/SMOWmeMYR5Cusiu6+9V+eYzHH6fkLkEHmPFHQX5rUdMxoVcNQGoAR5AHI4iNvIbb+lMC9apIE91YT9h3Hif8lHyV+9+j6iQQaBy22/Iup8A2dgkY7Tv37ORLi7yOMx8c/afVyGQuofYI3xbyI+IRqA0URKt3bLqHaftCJ0HxUBZ9/bfijcRXJwRcaxD8Yc3bv9XnnWv8xG5t8zkDthQL50E5ygkP9/xGb0gBPF3VLkzOUCWWrm7vAot5GJjd4/yBskFndl9975RjbecOkNsb/kaQxTVPf/eKwM7xX2WPNAwa6Gynfc7i5/7PX6LjduYZ2Mia/rsbbdL/nbaPgA/YZZaka3YTsnIzgU7wrHb98sjWDPjp+/0YRnnMaowOJGys6DkUFCAIJ7H7RRPXbZMwmwaMDYcbAt/OgPXiFQOiwIKB+BRoyZguPjHjoNdgukVo/Sf18ej+QLWhF0PrQWthP4hDhjdcMKbRAPQAY1roFR+OEuCskAjDE08T3CTeSWD2NGdvw00IVSLzGswu/i//wK1uk4gaC29yaEMt3AbWEkrzAFsMduj7y+W/nMFBSajdVx3/THZD89Rb6fYP8YGxFa+G0sQDo/Dv/vQgPRu84etQjHctLAVs/As3xgHdzn/KfHqH5wgXdbPv/TgeDHv3dmuA9f6495+4xEbVs2nzHsMSDf5uMn2CEYrJC4BM1jVn6EHfgR2vjxvQPv3fKxLT6OHfjR/fjWgX9Q84jaZ+TvmfoHEc8K/4wQn/BP+PiVEvtgLOHnC0Zm/pE/fKTGb7/kO/At5VB9kUFAGjPRQ1B+HzxvS+D0OdXgNC5+DKJmnF9XODLv+HcfJO9l8WwZCK/5aZyaTfFdK48+jUl+5PAdp+FX+TgBgpEJnsB4XEpH8xvw8jnv0vTDS+5m4G8dk0ZQhiUMwzIes2AzQYrVxuD+CboHv4jd8f0fT4j6/Y2bPkq9aaG9bn0HjGfrPJHww8ivcwg241lmnDz59/RqtL/ty9Hgx9FppHHvHO+ftd57G+oIis9ji8OpC/n4B+SdWn9A3g4794Nk3sHT3i8jrR/9hEvhr/e174deD7z8+idmPFn+XxgRj/AyAtLDXRB8w457/kq3hRBp7RRoUuHf2cY455r+Pg//2W2osAZVByd8MJr8LQbfTCse9vx+d6V9HGV/e3lDn/H9g248Kg9u+O8yxDFKb5P9ddTjjtLuPO4etHvqXl1YJeME/+6r00hHXh91/fIZIhn48AI3jxWUxsP9RP/yMA569Y1TQwkQkz42IyPBYFtCSZAnlKNHCTTxOwXj5Ti4rx/ffP5zIv6vg8tnwgsZQBEsTvquN2NJz2WJgKFZwFBBEJCT0KdwwqPgyyUJgiEIMmC9APdxQE1dnAihTQ2sqMx92oQRY36gN+9J+J+eFV4e4uCcmtBTKA+wLsuSkwnFTqb0xJuFDEnNGGg5RTKTIPSmITvFJwRL4dMwmLgETruA8SazGR54gCDBKO9JTx82vr4dBd4y9oCcV4jZWTx6MHFdn/UZggpmjDv1AYl7pA+ICQwUCXB6RoYsCyi4/33rM2tjUh9hGMsbMlPICy+jnt+eVTCW7JSCKyWqkbnHa47NbHdKK96O91BmGhaCiTWc3egpu4gZ8XoTDe9ILFeyeVynlbpMJ6niMcW1WRt4ec6DqspPcl5y+QSgPtN6QpDI846xhXXEe+SenO6V2ZAc1JO4uF5S9+wY6S1HzaPdW9UqcndSZ58rhReMVEpde6g3NylD1/bKrqzeLs24XhKT1Z7E0NueqnYhqQdyv/Zp3TqUibfcB6XRXWs2NSUda/2+vznbapoMTbnOFqW9nK6PsRS3VNf0Ejfo0nnKXqSImnVD7JLSDdXydDEVKD7y4g23EYwmnjpdINpDh1ZpXVuN0ScQ2vGzxsokUxdVryZly1dRIGYtPutIsbRQhzws1cBm9vxwDPIUvwJlni+OkmXHiW/P+e4sONuDJxpZOq2aW7mgU1NO4+OQsaatb2E49LQmwjWddq53ifw0rA690MKD+Hk7XC8Cza2ddWkr6y1cT3GFs0yPWJrtFNrKhr2eMiTNiydPOi4diuObdI4O7ry/DXnSE8fYDVdad8sMsdgzyVCI+aRN7XmM7vGLAVJ3HVn1oIAJjy7VbLU4rLsEF8+OorTGtVkxGX1sD8laYQy3vdi6SYTXIBLtOhYdYw621jWDoV4oewOsQEW0zmaRm6o2FxlZwCKVZCJ9k4hg27hzvGkZDj2qdXKWvE2Dp9vu0AaOVK3Mo6MGSrA/BnHuoJZPe4cNYLVanA/Fjuoj1ttlBxnmCN+o6AXK3ZxXVJUdMqlbrhYAv93Ca3ecoJGwB0624SSNJgll8I1pVZS9VpJiuOAnNK4sr5GJFlxrm7ElTK7GTYNVmfSeo8+pzDankbO6yPEBJZiYcA7m5hYWt8najC55kW2uwyWS3BtbTDSB7Gp0O7/kCdZg5oJZUB1vtDDDRJiKdlk0Da8ruRGdC6qr8k3RJnbfnoV6Rxfn1j54wiKZakf7tr5FJ3zo+LlMMIq33q9Vd7Bi+2REk1ttboF5JFIQ71aKc3Dq5ZXo1/QJ5zayVjRnyY2MlUUuB3kuzpdd3Ce+oPLLg3M7mMfMUuKDOOxVJt05PIEefRxn927fFukpu57ZXUG0cr3SbN3aTQzXSLxQwzVhcGLHyGkeYKG2THGrCmgRYyiWCyzNdPwJg2I0huv4sUno1UXpQwerh9TubV3CCX6tEpJo7i2XPShdaSzJZpfMSfGCbVVpCITdEU2Iw/Vwa2hul1ubKTVwW8Ny9x3kqui88c758WpyU6XSNhuG9da2qtLUNBU37b4Lsp21woeF31xcPD2Igg3Re7Elpp7OqruLqpdp7QtKqaz2sNpZ1Z5GnEwfz4vbYqD0S78Uc3zd6V6wXXpdI1FJZhqJckvYZrBceadq9uaoWba+8E51yS7yPXnxwTY6R/1t4ZwiXCpp3DOj867JlsyhNpZd4JSV4lT+ausQ8UyR13vndnPkFS1OLg5/rLc3TMvL1DsHDdmdyV0sBI7SolK0idgK0PRwFIPWamtKaMxWuijT2K/wfSvSM8qMCmaHZtQ+nIel5KHdaVD9INUFbe0LlGvucy4cZL2VtgZJquYpMXTutokickpueaBtzZVBu/F67510NMypC7XhyuCaqQF9jRiCcbVcDoL9pmmHlblYNeSWPPVoPG+aHQRtmJUDPxNnp9hgvUzuG2URcYa0stH1jMQVZTVLcOGwbvZ7an4axFT2TNtx290APPGsNrm7Fc4Wx1uLGzs1bF5cxtbRmUjKoQHWeqcXwoThlvUa96uE3IDBBUq7YlXDPpYzltXrGYVtjLmxltUebzRnD7BzX+8q3aw3akPyN0NH+dNqE+6Z681PSR1MDrMTGiiLWpk5+z050BObxYyBtvPZzN4PkeQfwJwvQprWu/V+q8i8SRixrHv8ILfCFqJiTBP7tc9d2iSaVAfDCRJmzxndsZNvbjppPL1an/liR9+InrdWJs4cxMwIOPqURA1uz4zTfNeHeiUJyjwWyGuw5DGyTeUYWBo6mfcLiWNOQaCJK6n3lmum7zImQmNfsSadEKaserwRVrnyKvIg3Ii5164qTskMoqysM6bg5L7gmomMrV16kq02e02VDzuWnWwbij1ss0SxG0+YEnFqJzNA2j65ZXNCqxqg1QKxKHsxuV1XrOTVpMwIDh5BSGpTNG1wuuL6VqcMn6k0I49W+3DVyTSwZ2ix6RSNO9hOFLWZdSOqzKhWyx1nVVIWmXapHurspOQrQKjny/w8CNt+Hkq7wwRd4Ha+i6JdVaZagsXMyr7xJ8e8bOXaFHj/ZIv0juIM9rwprQ2/LmtFoxhwipbSKqmTdb4W+tA+86lSuahQVutykLbrXcxEDUtUWkvkrWwvO1GZ366pcsqKc0Z5ROEY1BLEl7NWeOzZN7NDN1V5TA/FSt4rt0m3b3fpzHfJSe06HVpzJk5ifOW4234qHa6ivCjOKtvf6sq9pHo1V/DST/UVipkFnDOqsOrrSjVId7kyI9MjtttpcjE50dy2ZlMciwV7dbNlbVmJsdtFS3vnakZpNYf5es91skQk5OGCuctWBgRHWBgmzakJCua4Z1EShzasvaUh91xPps6FnKROjddyZ3F+7U6lC0ZKk2GJO6IoGpM43uqzldGhlDm0Ql35ILjk2e06Ey/1RUu0WapPDtWO9hOK3EEafVpr2v66LIP6HJy20XyF8RycP5DB+iUdroOT5bVFILPRWUp4ZbENTbz3LVqzbgvXXpDgOO8Zk9oTwpA4LMy+PqXOU76BxGd9o2WPu0iFS3eUOhWAjNGloa4jg04IfRlqrsFp1SGaZ14p6zUEjLiUFdYIhnSRW7WXZOvt7HzCkizib6d6Oj+sxZjyl71tSr6ECtuiMbIh36vS/FZslpvmZHYuH0XVTMuXBi5zw2WX+wussrj5YAj5SVRcQdNPpcGkw9VjBMbop1STaIqQDqGzYeSAiyjVbA2csDd63pj5mWQ6YM0Je50baTSf5P0w79RykOWESPdDAnmj7RfrvVIJB9Bf1WK6B/X+QAyNrUfEsXLS7nBtiduSdCF2XZTb9pLgUUUn04Y61Q3rgpJfdaESS/t57PGVsRNpv/cXWlfSVxaTac9c5e5VXsyaZOvmOUpnx0W9UIO5chP5eLNsWyzdqnxis0YfHYHb1Lx/OSzcuD+ppQnUwqHTo8q00XLws5Q3JeqSp9pk0xNkubge+Os6B1c6dhOb21xOOr214itFHRW0g0xstq1Zp8t26CTQVol3XZkbybt0s3ZWTi7rq0kKFkVTYTJHo5bxXdk8kU7F7s5czIP1atEmXtQ4K6Pyo9WaL+eJ6FSUeKGBTlRnt7TmlUr7Z25xMCyN4gVT3y84TSLzvDmqg4Um6WYuW8IttXarUyzIoCz9wlZzJzmkJhf6bmzq4vXA8q7V7WRzsvFiEJZznwBUMj155Zx3L8eYc8vaIxSuPSvWWpJP1LY95au1cvG3m7lXVGLd6oTSUI2o+BS3qWUC5ei4lbFllbVbq9H7tu+3eLi8EZ4wVPltLe7ngrPhISuVrpasX/gmdzDeEXM74uO5uRYpZsbxE8tAe45EcRDx2WI+9Xiz7gu6P0zVymjWk3huobBsdxOcCxwCEosVPlmu6crR2J5qZd9mCDHWcpFq11K1BhLjbluHig6WNI9OET/ZDouNOr2VS8Mrs61EWxNMnl/USQ2BaUuVDK+zdjf3+HjnqYW3FhiwoeaGTWZUSoOLwdrc+RZihbucpceN34RbPR7K6ZSVFOs4me4jmTt1m+21YGFQLWfScpxKypQ4K/m6J3W66Ds0QUV6KjHUOWU3fIYpmOmyU1bXMbqgbyGZXtzWD1ToiICGzIrshs6bLHJvP/OvA+8vCHPWHarBrNIjXWZ0NlwPUk9xTBLWaX1sbHnTi6iYHy9Yzy66/nr0bJObaEQOqbWjYvWp6J0Qt7OVujMHlES32VZhFHN5A1xwAQrtBwc30jZNeESNzWqqxlqLA5WauvzcwljxtG8BLuW0SNa96UzOODPfl7dDCWk96udcu+0x7CIPWCWLpiT2gYBhgsQylT5X6ajipz3pdt56sUh34X7aBIHTn686IRS7c1HrC31dL2YSOZsvi8niAjy+uBzKy87yHSBHbTHj2MJUxesWcqxsEFckfo6XANXN5qqassjsV4xenpjJcsO0xzVXVsFeZoZFDrmubxz2hpCljRQ26eD7qoC2h5BmiUtYxDtsgXmX/daDx7QNhvGH3VUNuu7a06KPepqMpydaoWxh0M6TPNxni1t1HbKGJAjc80xrJh2mAj8ECqa7FwdrD6wt41siOpUFr044Qc8W7YwVV1g3bbCGcWOlmNqXNlZW8Iyo8V2nyJ44tPXiitnrOqBx8jTl8CnVxkG4zxtlh0VZvDgpRbsZqDWNLiNf2arwVM3tRAoeMvEg3uTnBWsANN06vEx2h7ymtNt2Yt/kaRdFyvXs5gybb5K9vKyP+NxDldNZnVsGKIJcC5eZv53yLB5nzvW4qSQeNgiN1Trmo8AwVW5oebzo5mQdEQ5mTr2ldd0JsRmQaHnilBkZHximWbMzVluvUH+WNG6LsZUut3BurS7EpN+TnhSkx1jJZudSB9NlpuHHQQ+CcjKAJex6s3dFgFnKchPGx5wp6kJHzYye0pQXxIW/PWK7yqM2tevxk6YCY+OhAHfwgOSOuQKwrT6P+qq/OYsLx0kbnqyF3WQKOe1Qt4DGUvu8b31FvOxgcQ9xrFEgrmj0rFHRkpxdOWuvrTZqdyLCeXPbyItY3fc8lg3WcpHQYngTC76vppE4CyQx7RQy4i8UR0yYsFlK19NkMyMHRc2yTdASxGUDAiw3FhNMVdHN0E8HMuU8Cjb8TtiQmwKbgSUc87RjXYlsfw2Ph6CZ1UnNBCcMpdSZfs2JKckKTbg6oodYSbhckDJudbkKWiXR7S0PL3xvixc9MdQy7QcW97rBd8IyuS1OVqpPL0oc3ViwWprVMuvqTlRNgtFwg1LJ6ua6C6UuV5Ij58kOSNqBz3e1S5w2xWJWGfKyLw8gs/h6emAvuSPQPkqS7jmdQng+kP62w20FHqfQQYAqi1WQLyh6HtOrOGSFmjynW+10MvXl+gZcXtqwalzaZClclKye9GV21pY5f5utJzaa7owMbZyCWbPlwT3eUpbc0nsHXVzM9MorF5206jmGlXV7oFWNQCV2qXuZN/NPOIoVfYYfmIN23nVY567MfCN4Pq3a4YKrqpBNrRVKDpDlSXpA4JRYcUGuXj3MElYn113FyZLZbOu1FiuRtjsKi+zMgtly17FTZpGsQocjBZpxl4vmiHGBGV3c1OsLjuN+/vnlw8v98fXLZwJnp+SHl/H++PMpxf/gDvVpiMvXp2CSJYgPL//vbpE+ble+Pdu8P0IAbvD5rv3zf9vmXz+81H4M7Xvc4m7S7vS8SfqfbhF//Jt3sUdh/eNR/fiA9ta+PQtq3dP9njtc3jVt3X9/U9nrmvEPeZrxb718+Pvl7nJWjs9F7vrvTwEeLt3/nuNtY5yPDx1BELsteH48PZ9VfHgJepjZ2G9eySn9CupydPr5xG28kzw+cnv5/f8APk3TpqgoAAA= -->
