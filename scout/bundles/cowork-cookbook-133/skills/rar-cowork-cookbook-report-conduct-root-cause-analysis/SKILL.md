---
name: "rar-cowork-cookbook-report-conduct-root-cause-analysis"
description: "Builds a structured summary report of conduct root cause analysis activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_conduct_root_cause_analysis", "rar_sha256": "a66f5418fa672958ca11053c074e9c5f6aba888f1cf185aa95d5a69efab2e697", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_conduct_root_cause_analysis_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-conduct-root-cause-analysis:948b91158174e3b9fd4896fe95eb273aaa033533463c5f3e29f1956ca79e57b8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_conduct_root_cause_analysis`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_conduct_root_cause_analysis_agent.py` is
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

Conduct root cause analysis Summary Report — Builds a structured summary report of conduct root cause analysis activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-conduct-root-cause-analysis
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
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_conduct_root_cause_analysis_agent.py` and embedded as the fenced Python below (sha256 a66f5418fa672958…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_conduct_root_cause_analysis_agent.py` first:

```bash
python3 report_conduct_root_cause_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_conduct_root_cause_analysis_agent.py   # or on stdin
python3 report_conduct_root_cause_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct root cause analysis Summary Report — Builds a structured summary report of conduct root cause analysis activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-conduct-root-cause-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_conduct_root_cause_analysis',
    "version": '2.0.0',
    "display_name": 'Conduct root cause analysis Summary Report',
    "description": 'Builds a structured summary report of conduct root cause analysis activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-conduct-root-cause-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-conduct-root-cause-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd90fd871db10dde2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/conduct-root-cause-analysis'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-conduct-root-cause-analysis', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.333, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportConductRootCauseAnalysis(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportConductRootCauseAnalysis'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(ReportConductRootCauseAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716eZPixpbvV9HU/NH2qLrQvtQNRzyQEAgQEkICgdtRrX1f0IIWj7/7pICq7p6x7x2/ePFUUaAl8+znd06m+P3JbOogL59en/aumUELM0nCwC0hM3MgLm/zMgZfeWyBf8jOs7oMrabOy+rp+clxK7sMizrMMzB91oSJU0EmVNVlY9dN6TpQ1aSpWfZQ6RZ5WUO5N5JwwFOozPMass2mcgEnM+mrEEy16/Aa1j3UhnUA1XltJtUzVJdu5oDvUSCrdM3YydusegH83c5Mi8Stnl5//e35KQTnT6+/P9mJWYFbT+qNJ3fnpwJ23Mht+mAGpidm5oNxRQ/0z8B14ZZeXqbgluN60OPqp8pNvGfoP/4jbs3Sr35+/ZJBj+PL0/inNhlUBy4Q16xqoLJtFqYVJkCNF2iatGZfAe2BNbKHacLMf7nP/EYpL6Bfxmc/3Zm8+G7905enHIhgjsb98vQzlJeAX9mM5y8jleKnn1+SvHXLn37+RqdqrMgFxgXEgNQvb4/rB1kw8NvQ0Ltx/QVQvbvRcr88fafceNzlHvUEM59eojzMfroTLsr86mZmZrs//fxXZO3AteMkrOr/Fd1f74QD13SATg/Bf36+Gfk3CH4o9EHzr9kWwK1/RxMw/J3dM/Qw1F/Rvtn/v5FOwsytPiz+p+T+bAL8C/TrX+r2zyY8Q96XJ95NwiuIDitxX6Hf3/bKnPv1k/Pt5qff/gCk/yWZfd6U9o3CW2pmoedW9dvbr5+q2+1Pv/36qSlArLlm+taUyZ/R/DO73vj8YMHHqJ9+nAv461mcgWSGPiId+j0v/q384wU6mEnofLtfvULf58t4wNCoxDvTuwm+y5kKyPqdHX9++gMgRHaHpvExyPJ//3dICu0yr3KvhvZ23gBUarI6TN1ReC0AiKQ9kvrrfi1uNi+p8xUCd8d0BxBhNkkNLUozTCCQD6PHRw0Axn39P/YNOD/bD+Cc3PHv7QF+byP4vd3A7+0d/L6+QFoAGOdl6IfgHqROFQUyfTerR5a34ABo+vk6cgUShXfUUTlxRJyqSdx/QF//NZu3G8WXoh8V+ZIBz5jAXQ5UuymYapZh0kPmiFRWX7ufAcDeoDpJLNOOofGjKV5G6xwDN3vYzAZVw+1cu6ldKMltILoXAlB+Bm6v8uQKkHG0ZBWHSQI5YQnMlIOKMKI5sPbrSOzr16+WWQVfsjsU49C9rFQTMOBDYOjz56J0vST0g/pL5tpBDn36/Y9P0H9C/2zWjfjIQwFF4WYxEM4JtNrLWwjkZpOCYRU0BgYAnpvvfv/j7opRugzUQZBRoRe6t8mA2rdAGDW4++fdOUDnUUS3fHD60W5QGwC7QGENrAWyvHr+ko0kcjC0bENQBx9GvE++m/7d23c+o0+qhw2Bn7wyT29jbzE4OtPOS+cFEj3ow1KPyjt6NMirGoRtAaqpm9k9mGnW31yYgXJcgcypvP4ZAhHzJRspf7UA6dE4KYAns/4KSZwCKl2egI/RQDf2YHaehaPjH+F6vw2IlJ9AjM3eSbxAWxdYEyrM0iyC0qzc2zjPvEcEqHDv8wFxE8rcFhprujv66JbTt8jj/kkDsX+0G/fSD31pMAQloP/Pjcko5HSxUOeLqTbnoflWU0/3iBrbp1HBe8c10gMdxj09vnUN7wDzDr1fsiQEXij7f9xHercguo/5TiF1qt7oj+lc3uiGNQiFUZWyHMPX/JK9YzwQeQzraoQrkLHxmP/5B8Px6bukAUjL8fpbvYfuUTYqDeIXKhorCW3Ic13nFup1UI6J9LA8iAt3tC2IfDv4QSsIUAfmB/QhIEQIAhTY7ma6LUgI0CPdo/tjeDh2UUAK4CIgLcgY9wU6jgEMgrCCLBe0QuMYYIVPN1JQ6gIbAxE/LFwFZnEXZmxpHwKaD198b//HIxCKYykB3D7yDNA0HbMGlmyBC0AadXe/fkj58BQQNR1j/jbpR2c/NIW+L0X/GHNtjLIPsAc9+FjFvzMNAOgyrW6hBuprXIFsTt1H+IA4uBXsl3vNvRf1D1le/0cX/9Pfa/RvVVT/0W+vUFDXRfU6mdwr3Xuhe7HzFBQ7Oyzc6lH0Pj8S6/OYWJ9vifX5PbF+oHw31Cv096T7gcQjqF8h9AV5QcZHm9B2x6h9HMAY3OfZ6TMxPv2Sqe43LwP2eQpgZjR+D6D2o5y8DwE1xS9dfxx8Ly/VWJVaUAhvqHYrDx+R8MgSAJqZP9bCKv8ue0edRr/e3faBvuBRNuK6M3ZxvjuucJJR/Mp9es2aJHl+yszU/d+sbEaEBcEKrDEuiEDagK6oDt3bldk44WiS8fzHBZx8OzGTMbPysU4C0Aw/UPQmvlMC2cZU9EEFc8tnCIjsA0gcNWrHdBybAQtoWAGAdZ1RhbovRpnvK5+xC/to0f6nBLeMBlDk5K9jYoNyCtrpZ+ijM36G3tcqt+Vf1oDF2q9jVz7qDIaCr4+xH+tTy3367U/EeDTpfy3EA23u+G5aY50cVfwTnQC10r00oC47ozzfFPzGN78z++MmZ31fZv7+9A4o4/m9SbhHFpjwN1q5Uev3Evw2kjZHAreG62aEW6P6ZoIIGEvtd4/8sW94u4fq0yvAI/f5CUwGDQ/ovofbuvrpLg9Q5FuLO0pnlp+rsXWYgEwDlEBBL0YlYoCK3zEYb4fObfx48voXffE/g4hXlmAsFkVJBqUJF7dYzyEYlvJclnQtjMZN00RwnMRxgsJt0sNdjPVQlqRsk2ZdkrYYIEYFgiI1H2JM0NELQIEPU/9fdOtPdwqgpmAkBUiYFOWRBMp4JkVjLMnYJooiJG4jQGYWiEWZlskwjIfaHsqQpsmSDmlSLHCNhbkUS4/0Ht3iXay398783S93rAAypWk4Co2Zps3YNEo4LG1StosjFm67KIY6NO4iJIt7DOMSYP7H1IdvRtfdNR/jFjSKoE27jnx+f/h6jEWKACOXRCVO7wc3YQ8mhdHRNrBgmvL8SwTb9WbOJDRGpYg+mMcz5i9P1H5h4mthxe+RBhl087hd7/VuVs2puYJwXhXDJMpTaZ5JLCoIsO9baq8qfMskMMsEuLibrRVNmTeXZrZLB6RSeya/iJp8ti4YRlw2prXWzmG2PZDrk65MJkSMByql7budX1iLsC+j+WXOOrKUkqer6vWiPksNOLkYR3wR9bSeM+g6ZeNQV1N95VVVNd81ESkc9zi2w5YiKhslQil4jTINXe3xJUbWOOlQAlGjJrIz016vwoshu4uCQweRyVFScvt42jhIpDCH46o/6LPzSnOjA8dIgoLb2mG4HLYHTb7YpDIkGXNYZX05OxknK9yecX6xRlt/KyzO2aWwpgnaWXp/aNzzXlEI7nLdXLeprKYVi7LrhnInHLm1LzGaVqc1Qmzb2HFFLUP3m0N18C/Jvou96dEROSEIMYcsqjDdYpVT4tdsfp5KFSJj/nRNdWvY4rkzHcNbBtPzSrPIYgXLsb3iV4Qa5c3hvAjcjVWf9tql6teBXg4L8sITBHuOt36O8afz9mSiJhoTmrEaOrNYWRO4GdyM3FcCUlU7rJxuCn4x72NTt3GbT4/mqslUxqKtrsxlcRFkjkxpVyNr4TKztr6jXMmQP2prWuzggdySu1VjuUiwT3UsaaQL6qQHwa2ZHO+RVmbJ81EU0jbpWkBTPQJbyi6fNRaJ7jaT8CRtVprScUmdH0Um4S/uriFQ97A4NDQnxJOLcr2ck1OCHYIzuy2GaR1de0piGERnzOnmbNpN2J/gYG/qu2Ar53rq7BJ8NsSngbFrhELKdqq1msZIGaHKkrc+ROpueZkw811BSgaOoHDELNXmWLAhhQ/RvkUXBlIKSR2cKHmDxHS5Pgt2eepMxN2LxlHjp2k66aIptvIaZXGd0JYYGVJSFYTIb2UkWXe9gMvpZNaj8cLYzE99XFTZMRSPzGIz9WaVMD+gbmyq8uyMi0MxP8kSKobNKbR5MS/CVk5kW+aDniAzey328hXn3NTZN4xLiVe+Cu3Ym9N5cHGInuUWrBhf15IGTKXRu1ov0y0VIvAym1ucfTmj8XWiYNu2POmb7WHjJ+3BulqUviauhwRTYq81DjW53CJELm81Yk8gh2RqRUc15/LFZlIsNLIJCxFeHBlFOlsrNfVM8dJEUj7p/VDezjJ1kZrEHvcSOtDnV4XNuEl0wRBPmkxCYV8EkXI95B15YfuKOvKOc0LMEr6upoJ1WJRCgLiNdcklDc5Xaolda2GO6XWMZseJ666xqXIW1utZiShKyO1SmIoFa7kJGE6Z6BpjmQVHLYmkZ0zdXKtcc5zEU0XkDtLJ3NpXkydLpXHtXX4mTupVFDMHC8mumHc2rXFnMZj46/xykDO7FWaqEZzTDVL5HYtmPLczUkPdE1J60RYM7qZ67NXpqvIoe3e+FM6KYFHS0i0kTz1lkC7xVpmrsNwCMEQ0zFJNxMqVE1y6pDpxWXc7c2FmsbQDAsvnUlbs9rxQZ1l3mbJEr/EbXIfpXs1li7u6e9jWEKtdZ4v5MpPDyGNmM6F3QZfucW7L7R0k42x7i8ITL7D7lZlvpM677s9UgnVxyAecLk7UmV61C9NbXUVBcKhDKm1miESspnosRnvZ72qd4kCXhIgqg5zbeQuSR9XcnX7qiaqW1BoU02U7PYhSGzkbPT74q/NlaDM8iq71cS6INbZAjtON1cO8ztJWgjZxNHRnTQbBemHd7JwSzbDI4KpLUnxConqcLNfYMGy2Q7Vn891haRTm0LKTSuRamCAjuJ3N5ucNQ9pxD3uyl4XmpkDgvcrjg++KxmyHh0xVWnEscfB0R+vhik9JN5+Kha+HsCFfyH27rSsB3WohWB/O0HZeAqzhXb9Qo/Nhr1PbvSLLzVRcXRaJ6dOMRsjwnNl6gYzMWQHV6aLe7PJrEw+cjTYVQ9tUulb4DjUvDSexQiNZ6w5h7N6uKLnQwzUVim2WHcpIZaq6NTJNaOTU3zXnTZrmHr72pu1ltwoF3O0PWiJRGMiy4HLth7NfhmoQDaeN4uIn68Luz3lkXUgHPUmBkE4ZpZ/rheBHhW5X87BWJ3jrYao7389XJe4WHbyXTq5e7Zp1Oq+z82y+SVzjrIb0Rs5Ok5OdK5tkz3nppLomVJpws54Qs7DQTscu3kxll4avySrd90E3W/cFx2LhLpYWZuGr88RH7V5XlMGdLy9ZT6qAUqIgO5Jjp8f5yp35lV62x4vZ966MJ6LTDYe1wBXUTBKw44ESOsnEiEFQ7U7ifIIpsBPddVc0S9ZHxI/XmtXGZcjM2bqWmVSIw6Na5zpC8VcR92gAhNc5smVls5Z3zTKqTXwWbeCzbGCNmYYswM8Kb6L8EDobO0JOEbfCu2N83g90S9dzJefPylyYaHmwoiRBXJdryTCoKakFHt2ddwSjaNKi3B02dk7mAtOa0rzU9Xin+gGLwAx3cabxMjdbb+vOWEyiEm/YJcUs88mrWjr0bDZxZczs+q2hcLqsTsVNylhDPPcovVuvV7N9iRAufLWuK9Aj9Qzjx/m03bG9a9QuHuxC2biwNLpIcgGtqokrXjTa1NI+oSVDpBbHiZWdSAMgsRCJM+x6zK4zfx9Iwn5azQVt8DHkYJer0xIWVyLc8aJ+Xc51w2JY+WIi530ryQdE1gjY1C/6UC3nm17V48vW8+BkJTUHJGrjerURtisR2aLhoGfCwTDrnMtWsr5dtCS3bnWhOi+WhXWRK9Vb21v2kE53p0her88X7igrgrbQlUFbCisOC+v9zsG5tSaI00Hihbg9L7V1Lh4Wx7T2e9ARr2BlIG2qWKwvhhullrrWYZFLG7qLQOFfk2zsGecjL1yMVusFCYOZktTJoiyCpq6kbXs5XdjTfuedBqVc2WtrvZSjVckLBedHgZKv6OqkX/cR73eXBTYTCoK2Pc9eVynIZr/fp+c5e3EVuw44sdguosTWm5Oor441xam7klmkMyfeWme0n5T8gfBtwme0odxhNuEqiyVWz2ZicgxarbwIWCucSqStdSSYzY0FVRu61Dpz6oCQeeUsd+ZFWNCgs6XRlos1HObVrM3WorM86Ktut5+LaMc3Fuh2z1PShD3C2VBlVutry2bPIdWZS3I/8+JtZm99NpBTjBMm8JS+EFGcb1Fvvd4l/tb0xXxJ98ehLEtbX89PuRFOVjVvzwuqne6jnQjITS78wez0LjJPgVzBx+2Vyvi8U3YSJVBzk9kdo5AmO6VS6Mu88oOmmGDGUpwTk82Gw2uK3x7mwnm/SmCViihnszqdgvjAk1ZqHqqIPdn1mZ4uyO54NrFANda8cTa2lilt6NVKjvazbcl5xnKdcmHuZRS2z1ZV1Z34zbLplqbJH8ik2x+QXt8HKL2k2RDdxfCJVHhnY22WBZnGYTMMh35Wo1lv7IjJ5diGBqKRoUjO6O60x6NznDqVK8sBz9u7k6O3woDaluN7kRVnSpsLcqiFriurGNLZgZFyU4Aqk5w4CBpo4Q/BstgSQ54L/dJbwEh9LvAQ3aM2wTjogmDcdRrgV2Nl4EOO5vmEagnZymF6i6aHic2TNmZV3SIcqmiKG5I5LU6rTb318K281a0m1jaYZcwQl5BAf+cfy5yOOqLCc4SWJ6wpCbGhCvZ1sYstewtnOwJL9hoVhZNp1PsDcyWWjIjOeSWvjaNlkOf9IYwQsU54OB9yZXeNvXCiEleYb4pAhp2FL0m4g55dB15YolHMCCfYtKztKBYPG3zcu7SiTDBxSXNGzU0xQgGFz+uQqibo7qCcLl2FiKWpTeydVLL7Y1hvZ4TshoI+ywxjpsw3kRxo8CyRvJmvnN2e3oWkyGt8MbTzraSIynpHxfluKVrxAG/8auNIGxZfYydqE+mrVe8Mualw7Qxzylm2nWwuLKkOyeKMbqToPO17mLse93STLgqXT2eMl8AaBavX1uC982F6PcW9h/cK5zoJe+iFyWyy2BWg2dUXaxnx6KaiaaudLg68aw65leTYdQFSqUfMITMNzD3AmcESBKH2udj4O9ZfnPzQnfAIDM9ak6/wKyalfmHC6OR0CjFfwoh8qCYLlJ2sGJQKGqNBuA020eUTZWEarGCwPliz7c5fwRQK1kKbiNASpp6GfGOHK3S+mbhMqGS57x6uVH+SpldLOhkZpQQqrs5D1pjj1a7Tq6XKS4MTzvjWSMvTFAMro+G06ud4Nyf3Q4dkAu7jgrJPKsHKw62LKkscPUvZQFLCyfXhuZBft7wSW/l2FVG6yPrhMDMjQNlWVolPIIs5zM+M45Wsd443P+vBaTIZRCI0U5ZkPbmMJhUsA1bSwaFlxHaAP4bdkDIYuds2TOE0oRqqwrjpERjdRHKYLYpuvJVxnDjNvK655VwufVtTpvgCk5egNZCWXjSgi31nzy5evccwmC98dJnWltX7Br86OfUKFD2K13DlfLBiXDPyK1rafotu4vkpCil6eqAk2s+GRTXlKrrYaDBLpqgSTUPfm3aTfnnAkKlPKrOOBX0tpnlH0/AL4tKgWDOXGHGjWezQErBE9ZPm2h0tAH/tJkUMA8Uwpgun7GRprQdnHZC7BYPBIrLAOwO9DjhnkQg+8/KuifmorhJnjuOydth4NLOcwHNsYXPRdUGHW7C2x4Xc54xITsVZ2SbCBSMvmxXA88BCtVqMzzzKdtvjbglCWcR37HYqcYnoHXCG3cqOnwdHvljKTp3gBzzc41VYs0ew0Gb5wsgRqhWKudEMvT+llk7WTicbOJktFibezTI6m+UqZV3cpNF6unSdUjbqqGlk2hQWAQdqrsBmk5hxdiItL3vigHbafCBia2CHKde1gTdD8n3cwoMdXa5r1Y3kYuFw56u2WbXKde2k+P56Ft0zh9LDRBS7cf1Kn42ox1sHZqLpnh7U/khsOm0b1FGMZDqDE0cSdqXjWYkdsPpazZBtO6yJflfY6ak6OMZ1kH2BZ3XqRJnniYXtZkPTGFObmGF2NLvSOz1Ri6LZ+9GJOlQYM7MdsIRXyRW+wNET8OX0MKTCicTlYaCXm1JSVK/lcGuLVRnnT6fTX355en66vW19ekURnKWen8aN+8f2+9/bmvWHsHh70MIpAn9++n+3a3jfwXt/NXfbC3dN5/XG/fXviPnb81Nph0Ck+3ZulTT+Y6vwv+2Nfv7XO7bj/P7+ynh8i9jV728vatO/bSmHYGpVl/1blSfNbUMZGLupxp+NVOMvi2zw/XRTLC3Gbfw7S3BiOmmY3V48vNX5232b3X0af9cxvh1znfDbpf/YgX9+cnrgttCu3nCKfHPLYtT18Z5o3EYdXxQ9/fFfXBiu4wYnAAA= -->
