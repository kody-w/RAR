---
name: "rar-cowork-cookbook-audit-conduct-current-state-analysis"
description: "Audits conduct current state analysis records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_conduct_current_state_analysis", "rar_sha256": "b203070b9e71395b6dc2107d14375c79343be03ddb60d785faa6f3dcdfc2a394", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_conduct_current_state_analysis_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-conduct-current-state-analysis:5186349ba205d830c9673240239c7c279520c5d973a8acba72bde9d9305563e7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_conduct_current_state_analysis`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_conduct_current_state_analysis_agent.py` is
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

Conduct current state analysis Completeness Audit — Audits conduct current state analysis records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-conduct-current-state-analysis
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_conduct_current_state_analysis_agent.py` and embedded as the fenced Python below (sha256 b203070b9e71395b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_conduct_current_state_analysis_agent.py` first:

```bash
python3 audit_conduct_current_state_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_conduct_current_state_analysis_agent.py   # or on stdin
python3 audit_conduct_current_state_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct current state analysis Completeness Audit — Audits conduct current state analysis records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-conduct-current-state-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_conduct_current_state_analysis',
    "version": '2.0.0',
    "display_name": 'Conduct current state analysis Completeness Audit',
    "description": 'Audits conduct current state analysis records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-conduct-current-state-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-conduct-current-state-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd40b9115cc24174b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/conduct-current-state-analysis'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/audit-conduct-current-state-analysis', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditConductCurrentStateAnalysis(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditConductCurrentStateAnalysis'
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
    print(AuditConductCurrentStateAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716eZOjSJbnV9HG/FFVQ2YgbhRtbbYIkIQObiRQZVkUN4j7FKimvvs6kiIza7q6p2ttbRUWIQ73d7/fe+4ev73YXRsV9cvbi+bb+Wxtp2kc+fXMzr0ZW1yLOgFfReKA35lb5G0dO11b1M3LpxfPb9w6Ltu4yMF0pvPitpnGeJ3bztyurv28nTWt3fqAmp2OTdzMat8taq+ZBUUNhmZl6rd+7jfNnV9ZpLE7Pp7Hdu6CeaEd5007q7vU/+zYje/N3Mh3k+YV8PcHeyLQvLz9/Munlxhcv7z99uKmdtN8yMM+pGEfwmiTLMxTFEAgtfMQjCxHYIEc3Jd+DeTKwCPPD2bPux8bPw0+zf7zP5OrXYfNT29f8tnz8+Vl+lG7fNZG/qwt7KadBLRL24nTuB1fZ0x6tcdJ67arc6AkMEcd5+HrY+Y3SkU5+/v07scHk9fQb3/88lIAEezJvF9efpoBg315qbvp+nWiUv7402taXP36x5++0Wk65+ID6wNiQOrX9+f9kywY+G1oHNy5/h1QfTjS8b+8fKfc9HnIPekJZr68Xoo4//FBuKyL3s8nH/340z8je/dUGjftv0X35wfhyLc9oNNT8J8+3Y38ywx6KvSV5j9nWwK3/hVNwPAPdp9mT0P9M9p3+/830mkMAvirxf+U3J9NgP4++/mf6vavJnyaBV9eOD+NexAdTuq/zX5712Se/fkH79vDH375HZD+H8loRVe7dwrvmZ3Hgd+07+8//9DcH//wy88/dCWINd/O3rs6/TOaf2bXO58/WPA56sc/zgX8jTzJi2s++xrps9+K8n/Vv7/OjnYae9+eN2+z7/Nl+kCzSYkPpg8TfJczDZD1Ozv+9PI7wAiAJTXAg+k1yPL/+I/ZIXbroimCdqa5RTcBTd7GmT8Jr0cAr/RnUv+q7YT9/jXzfp2Bp1O6A4iwu7SdrWs7TmcgHyaPTxoUwezX/+3eofOz+4RO2J7Q6P0Jju9PcHy/g+P7Bzj++jrTI8C6qOMwBs9mKiPLAAInGAVMH8DXZZ/7iS+QKX7gjsoKE+Y0ACL/Nvv132H0fqf5Wo6TMl9y4B2AsoBg62dlUdt1nI4ze0IrZ2z9zwBmAaLURZo6tpvMpj9d+TpZ6BT5+dNuLqgd/uC7HQD7tHCB8EEMoPkTcH1TpD1Ax8maTRKn6cyLQRUANWS8gz6w+NtE7NdffwUAH33JH3CMzR7FpYHBgK8Czz5/Lms/SOMwar/kvhsVsx9++/2H2X/N/tWsO/GJhwxKw91mIKTT2VaTxBnIzy4Dw5rZFBwAfO7+++33hzMm6XJQDUFWxUHs3ycDat+CYdLg4aEP9wCdJxH9+snpj3abXSNgl1ncAmuBTG8+fcknEgUYWl/jxv8w4mPyw/Qf/n7wmXzSPG0I/BTURXYfe4/DyZlTgX2dCcHsq6WAusCv7eTRqADV1PNLP/f8HNTaNrLbby7MC1CwQfY0wfhp1jVA1Ynyr059r8J+BiDKbn+dHVgZVLsiBX8mA93Zg9lFHk+Ofwbs4zEgUv8AYmz5QeJ1JvrAmrPSru0yqkFJv48L7EdEgCr3MR8Qt2e5f51Nld2ffHTP63vksf+6y2C/7yzujcDsS4fOEXz2/7lLmWRl1muVXzM6z814UVetR2BNvdTE+dF+gWbhzuyeJd8aiA+s+UDhL3kaA2fU498eI4N7LD3GPJCtqwFzlVHv9Kesru904xZExOTiup6i2P6Sf8D9J2Bk4I9mQi6QuMkEA8VXhtPbD0kjkJ3T/bfS/7TTZBUQxrOyc4BlZoHve/eIb6N6yqen5UF4+FNugQRwoz9oNQPUgesB/RkQYnIPKAl304kgL0C79Ajyr8PvDgJSAA8CaUHi+K+z0xTHIBabmeODrmgaA6zww53ULPOBjYGIXy3cRHb5EGbqb58C2oBqH4N4+87+z1cgIqeqArh9TTdA0/bsFljyClwAsml4+PWrlE9PAaLZFB33SX909lPT2fdV6W9TygEJv6E+aMingv6daQBO19kjFkGpTRqQ1Jn/DB8QB/fa/foov4/6/lWWt39o6X/8a13/vaAaf/Tb2yxq27J5g+FH0fuoea8gQ2AQIXHpN4/69/mZdp+faff5nnafP9LuD7Qfpnqb/TX5/kDiGdZvM+R1/jqfXu1j15/i9vkB5mA/L63P+PT2S6763/wM2BcZwJvJ/CPA3K915WMIKC5h7YfT4EedaabydAUV8Q5v9zrxNRaeeQLQMw+notgU3+XvpNPk2YfjvsIweJVPAO9NLV3oTwuedBK/8V/e8i5NP73kdub/ewudCWxBwAJ7TCskkDqgSWpj/34H9AIvYnu6/uOKTrpf2OkjsIGvcs+u7/DwTJQn7n2aOuQcQMu0GpkqSv59gzQJ3o7lJOlj8TM1Yl+7tH/kes9kwMMr3qaEBtUUdNSfZl+b40+zj+XKfQ2Yd2C99vPUmE96gqHg6+vYr4tUx3/55U/EePbp/0SIeAKTCX4e6vreN6S4O660WwCIhroHIhXuvYuY6lcz3uvcP6oNGNZ+1YHK7U0if7PBN9GKhzy/31VpH4vR314+sGa6frQRj5ADE/5SuzeZ5qNMv0/E7YnEvSm7W+rur3cbhMZUjr97FU69xfsjil/eAFj5n17A5Cls0vh2X4G/PCQCqnxrhQEFADufm6m9gEESAkqg6JeTGgmAzO8YTI9j7z5+unj78/75f8CPNwKhSQxfODY6Jzwam7sLksJQfI5iC5dyUWpBoHOX8BYUZtO269gU6nj+wltgc4IgMZ8CgjQgdjL7KQiMTJ4AKnw19/9VX//yoAGKDkqQgIiDzrE5NXcWPoVgC8IhPRdF5pSH4BhFuNQCwzHHn2Oe55Bzj6KJwLbJAPNcL3BRG1vgE71nV/kQ7P2jg//wzQNKgFhZFk9io7bt0i6F4EB3m3R9bO5gro+giEdh/pxYYAFN+ziY/3Xq0z+T+x66T9ELGkrQzvUTn9+e/p4iksTByA3eCMzjw8KLo00Se6eNTKgmPQZVYdvRzJ1eiugudyn0dEWrk6ttKRFF6bQRtUFQot24OiRMKQbVraHmQrDjg/MWIq5cqJ73bbf3z345WELBciEmE7fcY9QjP+/setcf5nbimOtqL6htuRb5emcMHlHtSLIyj2ihlubulG/ORF2oMHyhLhCpr7yMWg3d8ajZmJXOz/pyLiSZ0ZFVraAevkCo/aFZ4xfvlDiWV7K3o1geNXKs3bpzuPFsbiiCcDEkJfy+vtAmMi58zLyaMeI5atBg7W7RZCiSens5r89Fu2iIZH8UvTkn0vaNJeoTcknFQWTLuW0HjowdNGSfalYYJriedVeaxlLO6jZaU11PIsbjl1zaFZjKZr5FrbUSoQv0MG5WNnpq6qRUj2LiHS/esR1QcXlBsXlGlT6KVghZJ8qtcRLDyHyRzA5Cae2IU36oO04vWaWhzX2VavGp6KnaJdECPggad6aSGA2ZfZZ28SJqIvd4S71uEEujw/Cxu5rUFYUVl+wOcXMKWmLXmGmlVsDi5S3B4VJZxWeUdQJxe0ZiKnVMveS2WL2t+EH0bExZtHpDY+7+vFQkVVp6wvmaKd36lhERje3NPTIE3TinSXJ5XWIrpqLP0sIPdIRNkr0YenLbXMt6y3mZFRxp41AcHR/rBLXMPJYa2BTzTs6u8+iWZ3vEb0dVbbaNuofbsGwSZU3z677qim4w4ZjanbQyCLUTGlmX0fD1eIWtCRTVT2YjnXTI9cey9EJwj5rx3FyzNwneJ1a3XzJyl55RQcs54kIt77/lENLEMlQWG0lL+sHyCnEbhIpZVDl9lnHWsKF5mcW8fIQtoaqhUxDcdHiNS+p64VErpD1KYlkf+igozfZyIPfVEN+YNDl3oqF2dr5ndWd163k3sYbKSUIjMRkdD5pq3oh0LeHbcpm122HcbSQTXt5OxzOzUcYj5ziS6KotfnCFK3feJiUbaprQDQeJ56LVWTmUkpo06vqYmy5yzkNV3BxuHtAcY0lZ1QmiJVyBuGmS4CV5vNlKo7LlooQsjrhB7NwLHVu4mXXOERMCVUChE3elFKU8oxI8BrR1KQ6nfXcWQgXadzULJWq3RxxPV3h+D0O0fhqMdnMqSH4hzdtzbWj48rQOyPQMx3g19OR2OyeGpZYb54xPiKYKzRVRaXiJHU+dG1DXwBKFxXZ/k9UxPBA9TbZ+sD3Uxpw4mruDDBiYqLfTl1lCRRuk3JJba37q14NlI94J2m6zNWdw5BwdY7sK+Hl+wkyoisywbgZF8iNiwaYr7Lo9IecUdJCRDDs5DhbJUhPEdT0M27rkxdsRUpdJuDeGthBJosLqXpZ2qLJdURZX7xTVFndnuHYHhbpJZnMsKqPLD+McMY7Ab4nTn4g4v8Wui3D+9izsQ5bs6WA82t6p2WDyjSfmlIKjmm0WdD2HtoY3upmY2WFsQ8xc2sT4dsGn3XyN1JiBc0gpcBgFNxG6Qcb4uurkJRYuE7piBbRtkA2Dq/Jly0v9Qstkgo0hl1sT7rLMmBt8XLHb/iSfpGrJ4aaQy30kW5F4AErtpNyGgh6vzmvc2N2OR9oszVVQZAUDKeFGw6y4TaJjgK9vTJjmtCkMBc9wSbqMjVAsTjGltcjRoV2ayRNG9VMeO3WHlmHJqsX1wVyvV1fcEw5GGB062gAIX1yaesOFnrRhOOGE7S61xNQ4sqlp8zju1/t2d9GWZwShPfNWQY25JxfbLRsZZ92Uuh42y+3uoNZkOWYltpVWvCWuoxW6guD9fHXhgOG4Zs1alQJLh5w8QYHcz5PxRpGQlPZyQiwKOVoZlo/18la8jvzywgqJqm+5bFwklnpclkey9zzrFO4v6cHGT9G+ifDltmhVpb+uDkOTNSWaIWwWwjxiRKzuHUhui3Mh5PNXhfJYP9QN5CTmx23ESgzkkAURwm11ELDdQKfneBjporpUvhZGI4fuGheB6DOZmPtVvzvHmsF02ThfD/RJFvvObki3VVN6hzh7aw5iXtevh5W2F64Zhemqsd74RJTRKw3JMGHgj6K17YybScHbo7Q58KeBhG7sURcu5/6ypMOsUotBQcy9KBCgP8I3fIbFKzZBcHglQXpj7YzK6raXXZO7pH6is+sFmc8F7EzfFpbXrtuoOs9hRBTmfK6Izmq1KBhEzGIu2Bxzoki9RNcOV0a0N6dSm9uHgeOTgmOq6gRa7ojSIWbZdjKqHExtJV+VswQvj7HgL0vXuM2NCL3tHT/PhEVYrSrRWmmSs1/2ZD2wgpLhRzxT1mxR5v24uW58B2rZtgTe84fwHPCrM447i4VaAjDcjKlme0s42feL7Jx5iklTHGlFrpefUghgaTK6fWvN22OBMb3Texuj4quWyPlrxu/rpFXGJM9pORMCpaOK8RLEh02KaQmesq54EqFl6VnVRlExQmUMsr8Ya+563rkCXKzGK7l3a+Ok2ftlfN4nt10Zc4ofNQ1NUhzVEwshyKK9znHLOdR5eMPIi5giqJwfXJpTjodiwG3Pwze9pt8qDa2NVZUGspLDiyvkVhgcXhPJKxcx16s0XKP8gR/IPM1D2kKxk1yWmHfsSzjYL+J97MlbX2x8z8HZXFvEy8OtVs3FRmBivlB2/EbXc4yPnPJ8PSyKQKiut70hB7EW7EcUasAak8zmBbdeHocR1qO0yuSGu6yVdNPECZcdb/yg387mgWrM2w1BkH1xJEN4zE/XQTK1KpirRlEeVuXIK4cjEQm7RbBWFPMcObq+PYV1auiSdq4vC2MJbMXn9lIQVlFdUa2/GtMbZzVrq3I7t1GsEjtDit+yEpofuVyPKZ+fC1fJpPlutaGUM77sCk0Uzr2r1vMAcbrA2QcW5kJdt6tXZjye1f0li3pB8Dmeylqx3A7NItYhYisGBr3Sl+ZJjVgEREYbHvY4qpyLJoL8Jj0nm5AQohW9ulYy1tVChwQXmRtakr+enK7dqAPehhhdnYvtEuqr1CykJqrLeO7hdS1Fma9rTizjGn492vhBY0Wsz9TwDA1SZAYkp/vbJme3TAAdO12lFd/oHXN0QCtJXpSBv7SLm3bFuQSR1NuwPZ0bpMkwXG6JldFfNpq3ghNy64EWmxbxC8mR3fIAy5usGvKVTXWXM8+QqI7SndWVCMuQFtdfo1Kt92ImsyR3XEOXWi9orYfG3Z4QehMrEQiCLnOHWJzPbVgvio08J/1rRjgBDec3n421+hoy0m65Dg0/crs0Op5EmVwlzCGj2GskI1sY8ZAFr2nZEm33OSuwHmjlNwqIiu1CnvtK6HvUMV3XyFo96DFw3ZZdSaAnVhGjTNYGfihvWcXf5jeLCXmKIUG3apmjuBFb73hy5zdkKyYXY6OVyojwjbAxHJOprWPhkHKCJwGzPhjYashwTQrQOM5OdKPgIbdDLU+umUUVKaMJyXyNmqrULMcFqDSdtLrUl4OppJ4hyYoNut+rIKKyYbEhQ0Moos+NhiYOI7t2d6od+KbKiOdNcLw6sM0pINtBRR1iws39Njvy4uq02Rz5XM464mraeynfNXZ/wdes29l6f6TUdCTt1bFP1rvOp8LtTq0TSy/P48Cry2sBHc8cCzdCRTJDLxX6VkUJBvYUim52lU42vG7BsRov+aXjbBtb2LhE2Hju3JbJTUzFxYDBMD6SSj2MQ2BEqu+nBIGUXmVi0GW3L7aQTRcJL5SepizzDrEhXKzWvZyiTQpoXNorVUDBeUHO6dzZ9RQXMxA/UqkEra90sGEXYn1l+uVcrkPCvHSUzkWWNISUefDDGBWunmkNcxzRFNImByvyNg10OFeyJYCli8fiaAihPInKCcxJp+WOC/3r6QJaVUQ/3WTfIiX61O72YZSrXj/C1dxi/CO0P+2vbJYj1kKvImO16PSqv1GEFvC3BspzVuppag8wsjssltGKGU5yb6vYek+iZkJrEWO20qGQCRjfdnwgw7gX0BuSrcY5DBqLwaOXmw1YdPsl7OH0+hYSYahekNwr9QtmnSAnC6OS72yITIU2GGjNN0BikvbSdfUUVmKquG1vt/WCkwSZDTC1XRG6TDY3mtiMBCP3my1BrLdG3NqGk6sjvWF5F2lSxnUgc0XdQlM4YJVmrcdVirSbfkwKGhRwWDY4ArQThdbvAxUPqLqSrjGzghdWeMDXJ1nBTRpxMWcvzCNm2NLCiTBL8taLOYefbflIt0tXlLBYyRVIqi2XsuH9sUcw2Jck0DzBYSC5V11Q1MAJSQtWIXvTYvK4zJSIHFKcsuyRdYpcOJbjGfSKixQJNmpu3sKwo/tDHkprKoO4oUuRRZyNl7gvStCzSUdod8JNw2NlaclTrFqV9SggvtKOAKduWsPn2wtH9+plvySF5aYj1onDiITls5J/5q5mNhYMSpvq1WKLZCE44snftsMtWd8i6ehEyEJD9FVM1bgG98louMFgbho5XQ6asVG4qLz58bDy+K01LPQgzbghVMj6iiwj2HK3K6vWhTPwIQpdRrD8VYNLmkldvaRIaqX1Q7JJqDN+MNybdEFOhZWK8zqPZSDYjkcIkAmc21eQeM2toaUvS1sc5uMm2bnNwt3w2NUMqc2NQQ+e1LP5gdxxkd8XVb9QmRV02XOdvDi6J4PFydPGOXlQ4IXJhpNTmxDnCAxqGyo0wK3y7oD7EbqSLh4uJFfuyhiYx/ZbKUx9cxGrDJda8HUh1bub3lwIyFcWsbltqi6Y75vjzd0HHAMJy8JDYUBveSFsMUDIK7W1RAwZFy6CAecyeMzAGLy5lIVvqb3Kxav5ih5uDrRQUOwma2Omx5ZP95e69f2D1njQDSNFjN7yEbyDrucOp8x5daUjA1I8S6lixoBKy792pDz0Ck+sJzd5G13E9OUojhTkoKHNstaqsqF9D19WhrFOFvUSiS4tMmDlGRPFY3Y77DHFJKF5VHGWJFQXKmOUg0QFIQMVks83ykrUrpwdccJxF2PhcVz7l/5gtnUnXNSx0otwL2xU2Dbnvl/wHMgFeKfhdWzT+oIoiXBp4UwdkcbWtHiiV1M93UK1WEo2cytHQ1Ms6OjYnGYsdn7c1pKZnTyMdb1AJQICsxkYvl7AerLJq3wp+1wtGZFYp/PcJiXrRCFO2I2wsG5hQbspGNNQ85JNRyIeDPEI0yNjgAoJqk2fL/qU8a3DiG9yRsYSWzQddl4exBUa8XtOdwg93N+qZF/KvIQjMLnZoFjXefQtSrx9oIPa29J0AjN+eMkgKt0pDPPy6eV+ovzyhswplPj0Mm1tP08W/urmcniLy/cnNYyiyU8v/+/2PB/7jx8nj/ctf9/23u7c3/6aoL98eqndGAj12JJu0i58bnX+t93dz//OrvNEYXwcjk8HpUP7cTzT2uF9YzwGs5u2Ht+bIu3u2+LA5F0z/ZNMM/0flQu+X+7KZeV0YnFnCr6DovZdu2nf2+L9ebAR59PRn+/FQIDnbfg8Q/j04o3AbbHbvGMk8e7X5aTn8whs2gKezsBefv8/XAPl4/AnAAA= -->
